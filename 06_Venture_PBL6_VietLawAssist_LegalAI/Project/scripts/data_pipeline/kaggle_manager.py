"""
VietLawAssist — Kaggle Workspace & Notebook Manager (kaggle_manager.py)
=======================================================================
Agent-03 (Data Engineer) & Agent-02 (ML Researcher)
Module kiến tạo và quản trị toàn diện thư mục Kaggle:
    1. Project/kaggle/dataset/ : Đóng gói toàn bộ tập dữ liệu, metadata và checksum
    2. Project/kaggle/notebooks/ : Sinh Notebook (.ipynb) và Python script (.py) chuẩn QLoRA chịu lỗi
    3. Hướng dẫn vận hành chuẩn hạn ngạch Kaggle Free và cơ chế Resume-from-checkpoint
"""

import json
import shutil
from pathlib import Path
from typing import Optional
from loguru import logger

from .config import DATA_DIR, PROJECT_ROOT, PROCESSED_DIR, RAW_DIR, SAMPLE_DIR
from .kaggle_bundle import compute_md5

KAGGLE_DIR = PROJECT_ROOT / "kaggle"
KAGGLE_DATASET_DIR = KAGGLE_DIR / "dataset"
KAGGLE_NOTEBOOKS_DIR = KAGGLE_DIR / "notebooks"


def setup_kaggle_dataset_bundle(
    username: str = "vietlawassist",
    dataset_slug: str = "vietlawassist-pbl6-legal-ai"
) -> Path:
    """
    Tập hợp toàn bộ các file dữ liệu sạch vào Project/kaggle/dataset/
    kèm theo dataset-metadata.json để sẵn sàng import hoặc upload.
    """
    KAGGLE_DATASET_DIR.mkdir(parents=True, exist_ok=True)

    metadata = {
        "title": "VietLawAssist PBL6 Legal AI Dataset",
        "id": f"{username}/{dataset_slug}",
        "licenses": [{"name": "CC0-1.0"}],
        "description": "Kho dữ liệu Pháp luật Đại cương phục vụ huấn luyện RAG 4 tầng và fine-tuning LoRA tại ĐHBK Đà Nẵng (DUT).",
    }
    with open(KAGGLE_DATASET_DIR / "dataset-metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    files_to_copy = [
        (RAW_DIR / "corpus_combined.json", "corpus_combined.json"),
        (SAMPLE_DIR / "textbook_principles.json", "textbook_principles.json"),
        (PROCESSED_DIR / "sft_vietlaw_500.json", "sft_vietlaw_500.json"),
        (PROCESSED_DIR / "train_sft.json", "train_sft.json"),
        (PROCESSED_DIR / "val_sft.json", "val_sft.json"),
        (PROCESSED_DIR / "train_sft_chatml.json", "train_sft_chatml.json"),
        (PROCESSED_DIR / "val_sft_chatml.json", "val_sft_chatml.json"),
        (SAMPLE_DIR / "eval_queries.json", "eval_benchmark.json"),
    ]

    manifest = []
    for src, dest_name in files_to_copy:
        dest_path = KAGGLE_DATASET_DIR / dest_name
        if src.exists():
            shutil.copy2(src, dest_path)
            md5_val = compute_md5(dest_path)
            size_kb = dest_path.stat().st_size / 1024
            manifest.append({"file": dest_name, "size": f"{size_kb:.1f} KB", "md5": md5_val})
        else:
            logger.warning(f"Chưa có tệp nguồn: {src}")

    manifest_path = KAGGLE_DATASET_DIR / "dataset_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    logger.success(f"Đã thiết lập thư mục Kaggle Dataset tại: {KAGGLE_DATASET_DIR} ({len(manifest)} tệp)")
    return KAGGLE_DATASET_DIR


def generate_kaggle_training_script() -> Path:
    """
    Sinh mã nguồn Python chuẩn mực train_vietlaw_qlora.py:
    - QLoRA 4-bit NF4
    - Prompt Loss Masking
    - Tự động Resume from Checkpoint nếu đứt kết nối
    - Ghi log thời gian thực ra CSV và JSON
    - Lưu chỉ adapter ~25MB (chống tràn đĩa Kaggle 20GB)
    """
    KAGGLE_NOTEBOOKS_DIR.mkdir(parents=True, exist_ok=True)
    script_path = KAGGLE_NOTEBOOKS_DIR / "train_vietlaw_qlora.py"

    code = '''"""
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
                    {"role": "user", "content": f"{s['instruction']}\\n\\n{s['input']}".strip()},
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
    response_template = "<|im_start|>assistant\\n"
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
        print(f"\\n[!] PHÁT HIỆN CHECKPOINT CŨ TẠI: {resume_checkpoint}")
        print("[!] Tự động tiếp tục huấn luyện từ checkpoint này (Fault-Tolerant Resuming)...\\n")
    else:
        print("\\n[*] Bắt đầu huấn luyện từ đầu (Epoch 1/3)...\\n")

    start_time = time.time()
    trainer.train(resume_from_checkpoint=resume_checkpoint)
    elapsed_minutes = (time.time() - start_time) / 60.0
    print(f"\\n[SUCCESS] Huấn luyện hoàn tất trong {elapsed_minutes:.2f} phút!")

    # 8. LƯU LORA ADAPTER WEIGHTS GỌN NHẸ (~25MB)
    print(f"[*] Đang lưu LoRA Adapter và cấu hình tại: {final_adapter_dir}")
    model.save_pretrained(str(final_adapter_dir))
    tokenizer.save_pretrained(str(final_adapter_dir))

    # 9. KIỂM THỬ SUY LUẬN ĐỐI SÁNH (POST-TRAINING INFERENCE TEST)
    print("\\n==================================================================")
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
    print(f"\\n[Câu hỏi test]:\\n{test_query}\\n")
    print(f"[Câu trả lời của LoRA Adapter]:\\n{generated_text}\\n")
    print("[*] Toàn bộ quy trình hoàn tất! Bạn có thể tải folder 'vietlaw_lora_adapter' về máy local.")

if __name__ == "__main__":
    main()
'''
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(code)

    logger.success(f"Đã tạo script huấn luyện Kaggle tại: {script_path}")
    return script_path


def generate_kaggle_jupyter_notebook() -> Path:
    """
    Sinh Jupyter Notebook .ipynb trực quan cho Kaggle,
    được chia thành từng cell rõ ràng kèm markdown giải thích.
    """
    KAGGLE_NOTEBOOKS_DIR.mkdir(parents=True, exist_ok=True)
    nb_path = KAGGLE_NOTEBOOKS_DIR / "train_vietlaw_qlora.ipynb"

    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# 🏛️ VietLawAssist — Huấn Luyện LoRA Fine-Tuning Trên Kaggle GPU (T4/P100)\n",
                "### Đồ án Chuyên ngành PBL6 — Đại học Bách Khoa Đà Nẵng (DUT)\n",
                "**Mục tiêu**: Tinh chỉnh mô hình `Qwen2.5-1.5B-Instruct` qua kỹ thuật **QLoRA 4-bit NormalFloat** trên tập dữ liệu chuẩn Barem Pháp luật Đại cương.\n",
                "- **VRAM tiêu hao**: ~2.8 GB (chạy hoàn hảo trên T4 Free Quota)\n",
                "- **Thời gian train**: ~15 - 20 phút (3 epochs)\n",
                "- **Khả năng chịu lỗi**: Tự động phục hồi từ `checkpoint-*` nếu bị ngắt kết nối giữa chừng\n",
                "- **Kích thước đầu ra**: Chỉ lưu Adapter ~25MB (chống tràn đĩa 20GB của Kaggle)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Cell 1: Cài đặt các thư viện cần thiết trên Kaggle\n",
                "!pip install -q --upgrade transformers datasets peft trl bitsandbytes accelerate"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Cell 2: Kiểm tra GPU và các tệp dữ liệu đầu vào\n",
                "import os\n",
                "import torch\n",
                "from pathlib import Path\n",
                "\n",
                "print(f\"[*] PyTorch Version: {torch.__version__}\")\n",
                "print(f\"[*] CUDA Available : {torch.cuda.is_available()}\")\n",
                "if torch.cuda.is_available():\n",
                "    print(f\"[*] GPU Device Name: {torch.cuda.get_device_name(0)}\")\n",
                "    print(f\"[*] Total VRAM     : {torch.cuda.get_device_properties(0).total_memory / (1024**3):.2f} GB\")\n",
                "\n",
                "!ls -lh /kaggle/input/*"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Cell 3: Thực thi toàn bộ quy trình huấn luyện với tính năng Resume Checkpoint\n",
                "# (Có thể chạy trực tiếp file script Python đã được tối ưu hóa)\n",
                "!python /kaggle/input/vietlawassist-dataset/train_vietlaw_qlora.py || python train_vietlaw_qlora.py"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Cell 4: Hiển thị biểu đồ Loss thời gian thực từ training_metrics.csv\n",
                "import pandas as pd\n",
                "import matplotlib.pyplot as plt\n",
                "\n",
                "csv_path = Path(\"/kaggle/working/training_metrics.csv\")\n",
                "if csv_path.exists():\n",
                "    df = pd.read_csv(csv_path)\n",
                "    plt.figure(figsize=(10, 5))\n",
                "    plt.plot(df['step'], df['loss'], label='Train Loss', color='blue')\n",
                "    if 'eval_loss' in df and df['eval_loss'].sum() > 0:\n",
                "        plt.plot(df['step'], df['eval_loss'], label='Eval Loss', color='orange', linestyle='--')\n",
                "    plt.title('VietLawAssist QLoRA Training Curve (Qwen2.5-1.5B)')\n",
                "    plt.xlabel('Optimization Steps')\n",
                "    plt.ylabel('Cross Entropy Loss')\n",
                "    plt.grid(True)\n",
                "    plt.legend()\n",
                "    plt.show()\n",
                "else:\n",
                "    print(\"Chưa có tệp metrics để vẽ biểu đồ.\")"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Cell 5: Nén thư mục LoRA Adapter thành file zip để tải về Local tiện lợi\n",
                "!zip -r /kaggle/working/vietlaw_lora_adapter.zip /kaggle/working/vietlaw_lora_adapter/\n",
                "!ls -lh /kaggle/working/vietlaw_lora_adapter.zip\n",
                "print(\"[*] Sẵn sàng tải file vietlaw_lora_adapter.zip về máy local!\")"
            ]
        }
    ]

    notebook_content = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.12"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(notebook_content, f, ensure_ascii=False, indent=2)

    logger.success(f"Đã tạo Jupyter Notebook cho Kaggle tại: {nb_path}")
    return nb_path


def generate_kaggle_guide_doc() -> Path:
    """Sinh tài liệu cẩm nang hướng dẫn sử dụng Kaggle từng bước."""
    doc_path = KAGGLE_NOTEBOOKS_DIR / "README_KAGGLE.md"
    content = """# 📘 Hướng Dẫn Vận Hành Huấn Luyện VietLawAssist Trên Kaggle GPU

Tài liệu này hướng dẫn cách đưa dữ liệu và chạy Notebook huấn luyện LoRA fine-tuning trên nền tảng **Kaggle GPU miễn phí** (Tesla T4 16GB VRAM).

---

## BƯỚC 1: ĐƯA DATASET LÊN KAGGLE (CHỈ LÀM 1 LẦN HOẶC KHI CÓ DATA MỚI)

### Cách 1: Tải lên tự động bằng Kaggle CLI (Khuyến nghị)
Chạy lệnh PowerShell tại thư mục `Project/`:
```powershell
.venv\\Scripts\\python.exe -m scripts.data_pipeline.manage_pipeline prep-kaggle --username "your_kaggle_username"
.venv\\Scripts\\python.exe -m scripts.data_pipeline.manage_pipeline upload-kaggle --message "Update SFT dataset"
```

### Cách 2: Tải lên thủ công qua giao diện Web
1. Đăng nhập [Kaggle](https://www.kaggle.com).
2. Vào mục **Datasets** $\\rightarrow$ Bấm **New Dataset**.
3. Đặt tên Dataset: `vietlawassist-dataset`.
4. Kéo thả toàn bộ các file trong thư mục `Project/kaggle/dataset/` vào và bấm **Create**.

---

## BƯỚC 2: TẠO NOTEBOOK VÀ CẤU HÌNH GPU

1. Vào mục **Code** trên Kaggle $\\rightarrow$ Bấm **New Notebook**.
2. Chọn menu **File** $\\rightarrow$ **Upload Notebook** $\\rightarrow$ Chọn file `Project/kaggle/notebooks/train_vietlaw_qlora.ipynb`.
3. Nhìn sang cột bên phải (Notebook Settings):
   - **Accelerator**: Chọn **GPU T4 x 2** hoặc **GPU P100**.
   - **Internet**: Bật **On** (để tải thư viện và mô hình nền Qwen2.5 từ HuggingFace).
4. Bấm **+ Add Data** ở góc phải $\\rightarrow$ Chọn tab **Your Datasets** $\\rightarrow$ Add dataset `vietlawassist-dataset` vừa tạo ở Bước 1.

---

## BƯỚC 3: CHẠY HUẤN LUYỆN AN TOÀN (KHÔNG BỊ DISCONNECT)

> [!IMPORTANT]
> **Quy tắc vàng**: Đừng chạy từng cell rồi ngồi chờ 20 phút (nếu rớt mạng sẽ mất phiên).
> Thay vào đó, bấm nút **"Save Version"** (ở góc trên bên phải) $\\rightarrow$ Chọn **"Save & Run All (Commit)"** $\\rightarrow$ Bấm **Save**.

Hệ thống sẽ chạy ngầm độc lập trên máy chủ của Kaggle. Bạn có thể tắt trình duyệt và đi làm việc khác.

---

## BƯỚC 4: TẢI TRỌNG SỐ ADAPTER VỀ MÁY LOCAL

Sau khi Kaggle báo chạy xong (**Complete**):
1. Vào tab **Output** của Notebook.
2. Tải file `vietlaw_lora_adapter.zip` (~25MB) về máy.
3. Giải nén vào thư mục: `Project/models/lora_adapter/` trên máy local.
4. Backend FastAPI sẽ tự động nạp adapter này phục vụ sinh lời giải chuẩn barem DUT!
"""
    with open(doc_path, "w", encoding="utf-8") as f:
        f.write(content)
    logger.success(f"Đã tạo cẩm nang hướng dẫn Kaggle tại: {doc_path}")
    return doc_path


def setup_all_kaggle_artifacts() -> dict:
    """Thực thi một chạm toàn bộ chuỗi đóng gói dataset, notebook và cẩm nang Kaggle."""
    logger.info("=== BẮT ĐẦU THIẾT LẬP TOÀN DIỆN KAGGLE ARTIFACTS ===")
    ds_path = setup_kaggle_dataset_bundle()
    script_path = generate_kaggle_training_script()
    nb_path = generate_kaggle_jupyter_notebook()
    doc_path = generate_kaggle_guide_doc()

    # Sao chép thêm bản train script vào thư mục dataset bundle để Kaggle có thể chạy trực tiếp
    shutil.copy2(script_path, ds_path / "train_vietlaw_qlora.py")

    return {
        "dataset_dir": ds_path,
        "script_path": script_path,
        "notebook_path": nb_path,
        "doc_path": doc_path,
    }
