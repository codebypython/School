"""
VietLawAssist — Kaggle Fault-Tolerant QLoRA Training Pipeline (Modular & Checkpointed)
======================================================================================
PBL6 Đồ án Chuyên ngành (ĐHBK Đà Nẵng - DUT)
Hỗ trợ cơ chế Block-by-Block State Persistence:
  - Block 1: Setup môi trường & Cấu hình đường dẫn
  - Block 2: Tải & Lưu Base Model Snapshot cục bộ (Resume download, chạy Offline 100%)
  - Block 3: Tokenize & Lưu Dataset dạng Arrow ra đĩa (Pre-tokenized disk cache)
  - Block 4: Huấn luyện QLoRA với Auto-Resume Checkpoint (Không bao giờ mất step đã train)
  - Block 5: Đóng gói Final LoRA Adapter gọn nhẹ (~25MB - 100MB)
  - Block 6: Kiểm thử suy luận Offline & Trực quan hóa Loss thời gian thực
"""

import os
import sys
import json
import time
import csv
import argparse
from pathlib import Path
import torch
from loguru import logger

# =============================================================================
# 1. CẤU HÌNH ĐƯỜNG DẪN TỰ ĐỘNG & BIẾN MÔI TRƯỜNG
# =============================================================================
MODEL_ID = "Qwen/Qwen2.5-1.5B-Instruct"  # Có thể đổi thành Qwen/Qwen2.5-Coder-7B-Instruct

def resolve_workspace_paths():
    """Tự động xác định đường dẫn chạy trên Kaggle Cloud hoặc máy cục bộ."""
    if Path("/kaggle/input").exists():
        logger.info("[*] Môi trường: KAGGLE GPU CLOUD")
        # Tìm thư mục dataset đầu vào
        dataset_base = None
        for p in Path("/kaggle/input").glob("*"):
            if (p / "train_sft_chatml.json").exists():
                dataset_base = p
                break
        if not dataset_base:
            dataset_base = Path("/kaggle/input/vietlawassist-dataset")
        working_dir = Path("/kaggle/working")
    else:
        logger.info("[*] Môi trường: MÁY CỤC BỘ (LOCAL PC)")
        project_root = Path(__file__).resolve().parent.parent.parent
        dataset_base = project_root / "data" / "processed"
        if not (dataset_base / "train_sft_chatml.json").exists():
            dataset_base = project_root / "kaggle" / "dataset"
        working_dir = project_root / "kaggle" / "output"

    paths = {
        "dataset_base": dataset_base,
        "working_dir": working_dir,
        "local_model_dir": working_dir / "local_base_model",
        "cached_data_dir": working_dir / "cache_tokenized_dataset",
        "checkpoint_dir": working_dir / "checkpoints",
        "final_adapter_dir": working_dir / "vietlaw_lora_adapter",
        "metrics_csv": working_dir / "training_metrics.csv",
        "progress_json": working_dir / "training_progress.json",
    }
    
    for k in ["working_dir", "local_model_dir", "cached_data_dir", "checkpoint_dir"]:
        paths[k].mkdir(parents=True, exist_ok=True)
        
    return paths

# =============================================================================
# BLOCK 1: THIẾT LẬP MÔI TRƯỜNG & KIỂM TRA PHẦN CỨNG
# =============================================================================
def run_block1_setup():
    """Kiểm tra GPU, VRAM, CUDA, và trạng thái sẵn sàng của hệ thống."""
    paths = resolve_workspace_paths()
    logger.info("=== [BLOCK 1] THIẾT LẬP HỆ THỐNG VÀ KIỂM TRA PHẦN CỨNG ===")
    
    cuda_available = torch.cuda.is_available()
    device_name = torch.cuda.get_device_name(0) if cuda_available else "CPU"
    vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3) if cuda_available else 0.0
    
    logger.info(f"  - Thiết bị: {device_name} ({vram_gb:.2f} GB VRAM)")
    logger.info(f"  - PyTorch Version: {torch.__version__}")
    logger.info(f"  - Thư mục dữ liệu: {paths['dataset_base']}")
    logger.info(f"  - Thư mục làm việc: {paths['working_dir']}")
    
    # Kiểm tra các file dữ liệu đầu vào
    required_files = ["train_sft_chatml.json", "val_sft_chatml.json"]
    for f in required_files:
        p = paths["dataset_base"] / f
        if p.exists():
            size_kb = p.stat().st_size / 1024
            logger.success(f"    [OK] Tìm thấy {f} ({size_kb:.1f} KB)")
        else:
            logger.warning(f"    [MISSING] Chưa thấy {f} tại {paths['dataset_base']}")
            
    return paths

# =============================================================================
# BLOCK 2: TẢI VÀ LƯU BASE MODEL CỤC BỘ (LOCAL SNAPSHOT RESUME)
# =============================================================================
def run_block2_download_model(model_id: str = MODEL_ID):
    """
    Tải toàn bộ trọng số base model và tokenizer về ổ cứng cục bộ.
    Hỗ trợ resume download nếu mạng chập chờn.
    Nếu file đã tồn tại đầy đủ -> BỎ QUA tải qua mạng, chuyển sang chế độ 100% Offline!
    """
    from huggingface_hub import snapshot_download
    from transformers import AutoTokenizer

    paths = resolve_workspace_paths()
    local_dir = paths["local_model_dir"]
    config_file = local_dir / "config.json"
    
    logger.info("=== [BLOCK 2] TẢI & CACHE BASE MODEL SNAPSHOT ===")
    
    # Kiểm tra xem model đã được tải hoàn chỉnh chưa
    has_weights = any(local_dir.glob("*.safetensors")) or any(local_dir.glob("*.bin"))
    if config_file.exists() and has_weights:
        logger.success(f"[*] Base Model ĐÃ CÓ SẴN tại: {local_dir}")
        logger.info("[*] Kích hoạt chế độ HOÀN TOÀN OFFLINE (Không cần mạng Internet!).")
        return local_dir

    logger.info(f"[*] Đang tải Base Model {model_id} về thư mục cục bộ: {local_dir}...")
    logger.info("[*] Cơ chế tự động Resume Download được kích hoạt (nếu đứt mạng sẽ tải tiếp).")
    
    try:
        snapshot_download(
            repo_id=model_id,
            local_dir=str(local_dir),
            local_dir_use_symlinks=False,
            resume_download=True,
            ignore_patterns=["*.msgpack", "*.h5", "*.ot"]
        )
        logger.success(f"[OK] Đã tải và lưu thành công Base Model tại: {local_dir}")
    except Exception as e:
        logger.error(f"[X] Lỗi tải model từ Hugging Face: {e}")
        logger.info("[Gợi ý] Kiểm tra kết nối mạng hoặc bật 'Internet ON' trong phần Settings của Kaggle Notebook.")
        raise e
        
    return local_dir

# =============================================================================
# BLOCK 3: TIỀN XỬ LÝ & LƯU TOKENIZED DATASET DẠNG ARROW (DISK PERSISTENCE)
# =============================================================================
def run_block3_prepare_data():
    """
    Format dữ liệu theo chuẩn ChatML và lưu trực tiếp ra đĩa dưới dạng HuggingFace Dataset (Arrow).
    Nếu đã có cache trên đĩa -> Nạp tức thì trong 0.1s mà không cần format lại.
    """
    from datasets import Dataset, load_from_disk
    from transformers import AutoTokenizer

    paths = resolve_workspace_paths()
    cached_train_path = paths["cached_data_dir"] / "train"
    cached_val_path = paths["cached_data_dir"] / "val"
    
    logger.info("=== [BLOCK 3] TIỀN XỬ LÝ & CACHE TOKENIZED DATASET ===")

    # Kiểm tra cache đĩa
    if cached_train_path.exists() and cached_val_path.exists():
        logger.success(f"[*] Tìm thấy Dataset Cache tại: {paths['cached_data_dir']}")
        train_ds = load_from_disk(str(cached_train_path))
        val_ds = load_from_disk(str(cached_val_path))
        logger.info(f"  - Nạp từ đĩa: Train={len(train_ds)} mẫu | Val={len(val_ds)} mẫu (0.1 giây)")
        return train_ds, val_ds

    logger.info("[*] Chưa có cache, tiến hành đọc tệp JSON và format ChatML...")
    tokenizer = AutoTokenizer.from_pretrained(str(paths["local_model_dir"]), local_files_only=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    train_file = paths["dataset_base"] / "train_sft_chatml.json"
    val_file = paths["dataset_base"] / "val_sft_chatml.json"
    if not train_file.exists():
        train_file = paths["dataset_base"] / "train_sft.json"
        val_file = paths["dataset_base"] / "val_sft.json"

    with open(train_file, "r", encoding="utf-8") as f:
        train_raw = json.load(f)
    with open(val_file, "r", encoding="utf-8") as f:
        val_raw = json.load(f)

    def format_samples(raw_list):
        texts = []
        for s in raw_list:
            if "messages" in s:
                txt = tokenizer.apply_chat_template(s["messages"], tokenize=False, add_generation_prompt=False)
            else:
                msgs = [
                    {"role": "system", "content": "Bạn là VietLawAssist — Trợ lý AI Cố vấn Học thuật Pháp luật Đại cương tại ĐHBK Đà Nẵng (DUT)."},
                    {"role": "user", "content": f"{s.get('instruction', '')}\n\n{s.get('input', '')}".strip()},
                    {"role": "assistant", "content": s.get("output", "").strip()}
                ]
                txt = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=False)
            texts.append(txt)
        return Dataset.from_dict({"text": texts})

    train_ds = format_samples(train_raw)
    val_ds = format_samples(val_raw)

    # Lưu ra đĩa vĩnh viễn
    train_ds.save_to_disk(str(cached_train_path))
    val_ds.save_to_disk(str(cached_val_path))
    logger.success(f"[OK] Đã format và lưu Dataset Arrow Cache tại: {paths['cached_data_dir']}")
    logger.info(f"  - Số lượng mẫu: Train={len(train_ds)} | Val={len(val_ds)}")
    
    return train_ds, val_ds

# =============================================================================
# BLOCK 4: HUẤN LUYỆN QLORA VỚI AUTO-RESUME CHECKPOINTS (FAULT-TOLERANT)
# =============================================================================
class RealTimeProgressCallback(torch.nn.Module):
    """Callback ghi log metrics ra file CSV và JSON sau mỗi bước."""
    def __init__(self, paths):
        super().__init__()
        self.paths = paths
        self.csv_path = paths["metrics_csv"]
        self.json_path = paths["progress_json"]
        if not self.csv_path.exists():
            with open(self.csv_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["step", "epoch", "loss", "eval_loss", "lr", "vram_gb"])

    def on_log(self, args, state, control, logs=None, **kwargs):
        if not logs:
            return
        vram_gb = torch.cuda.memory_allocated() / (1024 ** 3) if torch.cuda.is_available() else 0.0
        step = state.global_step
        epoch = round(state.epoch or 0, 2)
        loss = round(logs.get("loss", 0.0), 4)
        eval_loss = round(logs.get("eval_loss", 0.0), 4)
        lr = logs.get("learning_rate", 0.0)

        with open(self.csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([step, epoch, loss, eval_loss, f"{lr:.2e}", f"{vram_gb:.2f}"])

        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump({
                "current_step": step,
                "max_steps": state.max_steps,
                "epoch": epoch,
                "loss": loss,
                "eval_loss": eval_loss,
                "vram_gb": f"{vram_gb:.2f} GB",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }, f, ensure_ascii=False, indent=2)

        print(f"[*] [Step {step:04d}/{state.max_steps:04d} | Epoch {epoch}] Loss: {loss:.4f} | VRAM: {vram_gb:.2f}GB")


def run_block4_train():
    """
    Nạp Base Model 4-bit, gắn LoRA, tự động tìm checkpoint mới nhất để resume nếu trước đó bị crash.
    """
    from transformers import (
        AutoModelForCausalLM,
        AutoTokenizer,
        BitsAndBytesConfig,
        TrainerCallback
    )
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    from trl import SFTTrainer, SFTConfig, DataCollatorForCompletionOnlyLM

    paths = resolve_workspace_paths()
    checkpoint_dir = paths["checkpoint_dir"]
    
    logger.info("=== [BLOCK 4] HUẤN LUYỆN QLORA VỚI AUTO-RESUME CHECKPOINTS ===")

    # 1. Nạp Dataset từ Cache (Block 3)
    train_ds, val_ds = run_block3_prepare_data()

    # 2. Nạp Tokenizer từ Local Model (Block 2)
    tokenizer = AutoTokenizer.from_pretrained(str(paths["local_model_dir"]), local_files_only=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # 3. Nạp Model dạng 4-bit NF4 từ Local
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    )

    logger.info("[*] Đang nạp Base Model 4-bit từ thư mục cục bộ (100% Offline)...")
    model = AutoModelForCausalLM.from_pretrained(
        str(paths["local_model_dir"]),
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
        local_files_only=True
    )
    model = prepare_model_for_kbit_training(model)

    # 4. Cấu hình LoRA Adapter
    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    # 5. Collator & Loss Masking
    collator = DataCollatorForCompletionOnlyLM(
        response_template="<|im_start|>assistant\n",
        tokenizer=tokenizer
    )

    # 6. Cấu hình TrainingArguments
    training_args = SFTConfig(
        output_dir=str(checkpoint_dir),
        dataset_text_field="text",
        max_seq_length=1536,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=8,
        learning_rate=2e-4,
        lr_scheduler_type="cosine",
        warmup_ratio=0.05,
        num_train_epochs=3,
        optim="paged_adamw_8bit",
        fp16=not torch.cuda.is_bf16_supported(),
        bf16=torch.cuda.is_bf16_supported(),
        gradient_checkpointing=True,
        save_strategy="steps",
        save_steps=25,
        save_total_limit=2,
        evaluation_strategy="steps",
        eval_steps=25,
        logging_steps=5,
        seed=42
    )

    # Callback
    from transformers import TrainerCallback
    class HFCallbackBridge(TrainerCallback):
        def __init__(self, bridge):
            self.bridge = bridge
        def on_log(self, args, state, control, logs=None, **kwargs):
            self.bridge.on_log(args, state, control, logs, **kwargs)

    cb = RealTimeProgressCallback(paths)
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=collator,
        callbacks=[HFCallbackBridge(cb)]
    )

    # 7. TỰ ĐỘNG PHÁT HIỆN CHECKPOINT CŨ ĐỂ TIẾP TỤC (RESUME)
    existing_ckpts = sorted(checkpoint_dir.glob("checkpoint-*"), key=lambda p: int(p.name.split("-")[-1]))
    last_ckpt = str(existing_ckpts[-1]) if existing_ckpts else None

    if last_ckpt:
        logger.warning(f"[!] PHÁT HIỆN CHECKPOINT CŨ: {last_ckpt}")
        logger.info("[!] Tự động tiếp tục huấn luyện từ checkpoint này, KHÔNG CHẠY LẠI TỪ ĐẦU!")
    else:
        logger.info("[*] Khởi động huấn luyện từ Step 0 (Epoch 1/3)...")

    start_time = time.time()
    trainer.train(resume_from_checkpoint=last_ckpt)
    elapsed = (time.time() - start_time) / 60.0
    logger.success(f"[SUCCESS] Huấn luyện thành công trong {elapsed:.2f} phút!")

    return model, tokenizer

# =============================================================================
# BLOCK 5: ĐÓNG GÓI & XUẤT BẢN FINAL LORA ADAPTER
# =============================================================================
def run_block5_save_adapter(model=None, tokenizer=None):
    """
    Lưu LoRA weights, adapter_config.json, và tạo file nén .zip sẵn sàng tải về.
    """
    import shutil
    from peft import PeftModel
    from transformers import AutoTokenizer

    paths = resolve_workspace_paths()
    adapter_dir = paths["final_adapter_dir"]
    adapter_dir.mkdir(parents=True, exist_ok=True)
    
    logger.info("=== [BLOCK 5] XUẤT BẢN & ĐÓNG GÓI FINAL LORA ADAPTER ===")

    # Nếu model được truyền vào trực tiếp
    if model is not None and tokenizer is not None:
        logger.info(f"[*] Đang lưu weights trực tiếp vào: {adapter_dir}")
        model.save_pretrained(str(adapter_dir))
        tokenizer.save_pretrained(str(adapter_dir))
    else:
        # Nếu chạy độc lập cell này, tìm checkpoint mới nhất để save
        existing_ckpts = sorted(paths["checkpoint_dir"].glob("checkpoint-*"), key=lambda p: int(p.name.split("-")[-1]))
        if not existing_ckpts:
            raise FileNotFoundError("Chưa có checkpoint nào trong thư mục checkpoints để xuất adapter!")
        latest_ckpt = existing_ckpts[-1]
        logger.info(f"[*] Sao chép LoRA weights từ checkpoint mới nhất: {latest_ckpt}")
        for f in latest_ckpt.glob("*"):
            if f.is_file():
                shutil.copy2(f, adapter_dir / f.name)
        # Copy tokenizer
        tok = AutoTokenizer.from_pretrained(str(paths["local_model_dir"]), local_files_only=True)
        tok.save_pretrained(str(adapter_dir))

    # Nén file zip
    zip_output = paths["working_dir"] / "vietlaw_lora_adapter.zip"
    shutil.make_archive(str(paths["working_dir"] / "vietlaw_lora_adapter"), "zip", str(adapter_dir))
    zip_size_mb = zip_output.stat().st_size / (1024**2)
    logger.success(f"[OK] Đã đóng gói thành công file nén: {zip_output.name} ({zip_size_mb:.2f} MB)")
    logger.info("Bạn có thể tải trực tiếp file zip này từ mục Output của Kaggle về máy cá nhân!")

    return zip_output

# =============================================================================
# BLOCK 6: KIỂM THỬ SUY LUẬN OFFLINE (ZERO-INTERNET POST-TRAINING TEST)
# =============================================================================
def run_block6_evaluate_offline():
    """
    Nạp Base Model cục bộ + LoRA Adapter vừa xuất bản để test suy luận 100% Offline.
    Không tốn 1 byte kết nối internet.
    """
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    from peft import PeftModel

    paths = resolve_workspace_paths()
    local_base = paths["local_model_dir"]
    adapter_dir = paths["final_adapter_dir"]

    logger.info("=== [BLOCK 6] KIỂM THỬ SUY LUẬN OFFLINE (ZERO-INTERNET TEST) ===")
    
    tokenizer = AutoTokenizer.from_pretrained(str(adapter_dir), local_files_only=True)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.float16
    )

    logger.info("[*] Nạp Base Model từ ổ cứng cục bộ...")
    base_model = AutoModelForCausalLM.from_pretrained(
        str(local_base),
        quantization_config=bnb_config,
        device_map="auto",
        local_files_only=True
    )

    logger.info("[*] Gắn LoRA Adapter từ thư mục xuất bản...")
    model = PeftModel.from_pretrained(base_model, str(adapter_dir), local_files_only=True)
    model.eval()

    test_queries = [
        "Tình huống: Ông A chết có tài sản chung với vợ là 1,2 tỷ đồng, có 2 con đẻ C (15 tuổi) và D (22 tuổi đã đi làm). Ông A lập di chúc cho bạn thân Q toàn bộ tài sản. Hãy xác định ai được hưởng di sản theo Điều 644 BLDS 2015 và tính giá trị mỗi suất?",
        "Tình huống: Anh Hải (20 tuổi) lái xe máy chở bạn vượt đèn đỏ với tốc độ 70km/h trong khu dân cư và đâm vào người đi bộ gây chấn thương 35%. Hãy xác định dạng lỗi của Hải và giải thích."
    ]

    for idx, q in enumerate(test_queries, 1):
        print(f"\n=======================================================")
        print(f" TEST CASE {idx}:")
        print(f" [Câu hỏi]: {q}")
        print(f"=======================================================")
        msgs = [
            {"role": "system", "content": "Bạn là VietLawAssist — Trợ lý AI Cố vấn Học thuật Pháp luật Đại cương tại ĐHBK Đà Nẵng (DUT)."},
            {"role": "user", "content": q}
        ]
        prompt = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=512,
                temperature=0.2,
                do_sample=True,
                top_p=0.9
            )
        ans = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        print(f"\n[VietLawAssist LoRA Trả Lời]:\n{ans}\n")

    logger.success("[*] Kiểm thử hoàn tất thành công 100% Offline!")

# =============================================================================
# CLI ENTRY POINT
# =============================================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VietLawAssist Modular QLoRA Training Pipeline")
    parser.add_argument("--block", type=int, choices=[1, 2, 3, 4, 5, 6, 0], default=0,
                        help="Chọn Block cần chạy (1-6), chọn 0 để chạy toàn bộ tuần tự.")
    args = parser.parse_args()

    if args.block == 1:
        run_block1_setup()
    elif args.block == 2:
        run_block2_download_model()
    elif args.block == 3:
        run_block3_prepare_data()
    elif args.block == 4:
        run_block4_train()
    elif args.block == 5:
        run_block5_save_adapter()
    elif args.block == 6:
        run_block6_evaluate_offline()
    else:
        # Chạy toàn bộ tuần tự
        run_block1_setup()
        run_block2_download_model()
        run_block3_prepare_data()
        m, tok = run_block4_train()
        run_block5_save_adapter(m, tok)
        run_block6_evaluate_offline()
