"""
VietLawAssist — Kaggle Fault-Tolerant QLoRA Training Pipeline
============================================================
PBL6 Đồ án Chuyên ngành (ĐHBK Đà Nẵng - DUT)
Mô hình nền: Qwen/Qwen2.5-1.5B-Instruct
Kỹ thuật: QLoRA 4-bit NF4 + Prompt Loss Masking + Auto-Resume Checkpoints
"""

import os
import sys
import json
import time
import csv
from pathlib import Path
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainerCallback,
    TrainingArguments,
)
from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training,
    PeftModel,
)
from trl import SFTTrainer, SFTConfig, DataCollatorForCompletionOnlyLM
from datasets import Dataset

# =============================================================================
# 1. CẤU HÌNH ĐƯỜNG DẪN TỰ ĐỘNG (KAGGLE CLOUD vs LOCAL PC)
# =============================================================================
def resolve_paths():
    """Tự động xác định đường dẫn chạy trên Kaggle Cloud hoặc máy cục bộ."""
    if Path("/kaggle/input").exists():
        print("[*] Đang chạy trên môi trường KAGGLE GPU CLOUD")
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
        print("[*] Đang chạy trên môi trường MÁY CỤC BỘ (LOCAL PC)")
        project_root = Path(__file__).resolve().parent.parent.parent
        dataset_base = project_root / "data" / "processed"
        working_dir = project_root / "kaggle" / "output"

    working_dir.mkdir(parents=True, exist_ok=True)
    return dataset_base, working_dir

# =============================================================================
# 2. LOGGING REAL-TIME VÀ THEO DÕI TIẾN ĐỘ HUẤN LUYỆN
# =============================================================================
class RealTimeProgressCallback(TrainerCallback):
    """Callback lưu lại tiến trình train real-time ra CSV và JSON sau mỗi logging step."""
    
    def __init__(self, log_dir: Path):
        self.log_dir = log_dir
        self.csv_path = log_dir / "training_metrics.csv"
        self.json_path = log_dir / "training_progress.json"
        self.history = []
        
        # Khởi tạo file CSV
        if not self.csv_path.exists():
            with open(self.csv_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["step", "epoch", "loss", "eval_loss", "learning_rate", "vram_allocated_gb"])

    def on_log(self, args, state, control, logs=None, **kwargs):
        if not logs:
            return
            
        vram_gb = torch.cuda.memory_allocated() / (1024 ** 3) if torch.cuda.is_available() else 0.0
        step = state.global_step
        epoch = round(state.epoch or 0, 2)
        loss = round(logs.get("loss", 0.0), 4)
        eval_loss = round(logs.get("eval_loss", 0.0), 4)
        lr = logs.get("learning_rate", 0.0)

        # Ghi CSV
        with open(self.csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([step, epoch, loss, eval_loss, f"{lr:.2e}", f"{vram_gb:.2f}"])

        # Ghi JSON
        progress_data = {
            "current_step": step,
            "max_steps": state.max_steps,
            "current_epoch": epoch,
            "total_epochs": args.num_train_epochs,
            "latest_train_loss": loss,
            "latest_eval_loss": eval_loss,
            "vram_gb": f"{vram_gb:.2f} GB",
            "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(progress_data, f, ensure_ascii=False, indent=2)

        print(f"[*] [Step {step:04d}/{state.max_steps:04d} | Epoch {epoch}] Loss: {loss:.4f} | VRAM: {vram_gb:.2f}GB")

# =============================================================================
# 3. HÀM MAIN THỰC THI TOÀN BỘ PIPELINE
# =============================================================================
def main():
    dataset_base, working_dir = resolve_paths()
    checkpoint_dir = working_dir / "checkpoints"
    final_adapter_dir = working_dir / "vietlaw_lora_adapter"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    print("==================================================================")
    print(" VIETLAWASSIST — KAGGLE HUẤN LUYỆN QLORA CHO QWEN2.5-1.5B")
    print("==================================================================")
    print(f"[*] Thư mục dữ liệu: {dataset_base}")
    print(f"[*] Thư mục lưu checkpoint: {checkpoint_dir}")
    print(f"[*] Thiết bị khả dụng: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU'}")

    # 1. Nạp Dataset
    train_file = dataset_base / "train_sft_chatml.json"
    val_file = dataset_base / "val_sft_chatml.json"
    
    if not train_file.exists():
        # Fallback thử tìm file train_sft.json
        train_file = dataset_base / "train_sft.json"
        val_file = dataset_base / "val_sft.json"

    print(f"[*] Đang nạp tập Train từ: {train_file.name}")
    with open(train_file, "r", encoding="utf-8") as f:
        train_raw = json.load(f)
    with open(val_file, "r", encoding="utf-8") as f:
        val_raw = json.load(f)

    # 2. Cấu hình Model & Tokenizer
    model_id = "Qwen/Qwen2.5-1.5B-Instruct"
    print(f"[*] Đang tải Tokenizer cho {model_id}...")
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Định dạng văn bản theo Chat Template của Qwen2.5
    def format_chatml_prompts(samples):
        formatted_texts = []
        for s in samples:
            if "messages" in s:
                text = tokenizer.apply_chat_template(s["messages"], tokenize=False, add_generation_prompt=False)
            else:
                messages = [
                    {"role": "system", "content": "Bạn là VietLawAssist — Trợ lý AI Cố vấn Học thuật Pháp luật Đại cương tại ĐHBK Đà Nẵng (DUT)."},
                    {"role": "user", "content": f"{s['instruction']}\n\n{s['input']}".strip()},
                    {"role": "assistant", "content": s["output"].strip()}
                ]
                text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
            formatted_texts.append(text)
        return formatted_texts

    train_texts = format_chatml_prompts(train_raw)
    val_texts = format_chatml_prompts(val_raw)
    
    train_dataset = Dataset.from_dict({"text": train_texts})
    val_dataset = Dataset.from_dict({"text": val_texts})
    print(f"[*] Số lượng mẫu: Train={len(train_dataset)} | Validation={len(val_dataset)}")

    # 3. Lượng tử hóa 4-bit (NF4)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    )

    print(f"[*] Đang nạp Base Model {model_id} ở chế độ 4-bit NormalFloat...")
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True
    )
    model = prepare_model_for_kbit_training(model)

    # 4. Cấu hình LoRA Adapter (r=16, alpha=32)
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

    # 5. Prompt Loss Masking
    response_template = "<|im_start|>assistant\n"
    collator = DataCollatorForCompletionOnlyLM(
        response_template=response_template,
        tokenizer=tokenizer
    )

    # 6. Thiết lập Training Arguments (Tối ưu Free Limit & Tiết kiệm ổ cứng)
    training_args = SFTConfig(
        output_dir=str(checkpoint_dir),
        dataset_text_field="text",
        max_seq_length=1536,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=8,       # Effective batch size = 16
        learning_rate=2e-4,
        lr_scheduler_type="cosine",
        warmup_ratio=0.1,
        num_train_epochs=3,
        optim="paged_adamw_8bit",
        fp16=not torch.cuda.is_bf16_supported(),
        bf16=torch.cuda.is_bf16_supported(),
        gradient_checkpointing=True,
        save_strategy="steps",
        save_steps=25,
        save_total_limit=2,                  # Chỉ giữ 2 checkpoint gần nhất (Tránh tràn đĩa 20GB)
        evaluation_strategy="steps",
        eval_steps=25,
        logging_steps=5,
        seed=42
    )

    # Khởi tạo Trainer
    progress_callback = RealTimeProgressCallback(working_dir)
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        data_collator=collator,
        callbacks=[progress_callback]
    )

    # 7. TỰ ĐỘNG PHÁT HIỆN CHECKPOINT CŨ ĐỂ RESUME (CHỐNG LỖI MẤT KẾT NỐI)
    existing_checkpoints = sorted(checkpoint_dir.glob("checkpoint-*"), key=lambda p: int(p.name.split("-")[-1]))
    resume_checkpoint = str(existing_checkpoints[-1]) if existing_checkpoints else None

    if resume_checkpoint:
        print(f"\n[!] PHÁT HIỆN CHECKPOINT CŨ TẠI: {resume_checkpoint}")
        print("[!] Tự động tiếp tục huấn luyện từ checkpoint này (Fault-Tolerant Resuming)...\n")
    else:
        print("\n[*] Bắt đầu huấn luyện từ đầu (Epoch 1/3)...\n")

    start_time = time.time()
    trainer.train(resume_from_checkpoint=resume_checkpoint)
    elapsed_minutes = (time.time() - start_time) / 60.0
    print(f"\n[SUCCESS] Huấn luyện hoàn tất trong {elapsed_minutes:.2f} phút!")

    # 8. LƯU LORA ADAPTER WEIGHTS GỌN NHẸ (~25MB)
    print(f"[*] Đang lưu LoRA Adapter và cấu hình tại: {final_adapter_dir}")
    model.save_pretrained(str(final_adapter_dir))
    tokenizer.save_pretrained(str(final_adapter_dir))

    # 9. KIỂM THỬ SUY LUẬN ĐỐI SÁNH (POST-TRAINING INFERENCE TEST)
    print("\n==================================================================")
    print(" BÀI KIỂM TRA SUY LUẬN THỰC TẾ TRỰC TIẾP TRÊN ADAPTER VỪA TRAIN")
    print("==================================================================")
    test_query = "Tình huống: Ông A chết có tài sản 600 triệu, lập di chúc cho bạn thân B. Vợ và con 15 tuổi có được hưởng thừa kế không?"
    test_messages = [
        {"role": "system", "content": "Bạn là VietLawAssist — Trợ lý AI Cố vấn Học thuật Pháp luật Đại cương tại ĐHBK Đà Nẵng (DUT)."},
        {"role": "user", "content": test_query}
    ]
    prompt_formatted = tokenizer.apply_chat_template(test_messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt_formatted, return_tensors="pt").to("cuda")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.2,
            do_sample=True,
            top_p=0.9
        )
    generated_text = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    print(f"\n[Câu hỏi test]:\n{test_query}\n")
    print(f"[Câu trả lời của LoRA Adapter]:\n{generated_text}\n")
    print("[*] Toàn bộ quy trình hoàn tất! Bạn có thể tải folder 'vietlaw_lora_adapter' về máy local.")

if __name__ == "__main__":
    main()
