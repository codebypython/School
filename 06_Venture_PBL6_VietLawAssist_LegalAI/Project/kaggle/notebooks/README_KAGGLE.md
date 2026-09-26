# 📘 Hướng Dẫn Vận Hành Huấn Luyện VietLawAssist Trên Kaggle GPU

Tài liệu này hướng dẫn cách đưa dữ liệu và chạy Notebook huấn luyện LoRA fine-tuning trên nền tảng **Kaggle GPU miễn phí** (Tesla T4 16GB VRAM).

---

## BƯỚC 1: ĐƯA DATASET LÊN KAGGLE (CHỈ LÀM 1 LẦN HOẶC KHI CÓ DATA MỚI)

### Cách 1: Tải lên tự động bằng Kaggle CLI (Khuyến nghị)
Chạy lệnh PowerShell tại thư mục `Project/`:
```powershell
.venv\Scripts\python.exe -m scripts.data_pipeline.manage_pipeline prep-kaggle --username "your_kaggle_username"
.venv\Scripts\python.exe -m scripts.data_pipeline.manage_pipeline upload-kaggle --message "Update SFT dataset"
```

### Cách 2: Tải lên thủ công qua giao diện Web
1. Đăng nhập [Kaggle](https://www.kaggle.com).
2. Vào mục **Datasets** $\rightarrow$ Bấm **New Dataset**.
3. Đặt tên Dataset: `vietlawassist-dataset`.
4. Kéo thả toàn bộ các file trong thư mục `Project/kaggle/dataset/` vào và bấm **Create**.

---

## BƯỚC 2: TẠO NOTEBOOK VÀ CẤU HÌNH GPU

1. Vào mục **Code** trên Kaggle $\rightarrow$ Bấm **New Notebook**.
2. Chọn menu **File** $\rightarrow$ **Upload Notebook** $\rightarrow$ Chọn file `Project/kaggle/notebooks/train_vietlaw_qlora.ipynb`.
3. Nhìn sang cột bên phải (Notebook Settings):
   - **Accelerator**: Chọn **GPU T4 x 2** hoặc **GPU P100**.
   - **Internet**: Bật **On** (để tải thư viện và mô hình nền Qwen2.5 từ HuggingFace).
4. Bấm **+ Add Data** ở góc phải $\rightarrow$ Chọn tab **Your Datasets** $\rightarrow$ Add dataset `vietlawassist-dataset` vừa tạo ở Bước 1.

---

## BƯỚC 3: CHẠY HUẤN LUYỆN AN TOÀN (KHÔNG BỊ DISCONNECT)

> [!IMPORTANT]
> **Quy tắc vàng**: Đừng chạy từng cell rồi ngồi chờ 20 phút (nếu rớt mạng sẽ mất phiên).
> Thay vào đó, bấm nút **"Save Version"** (ở góc trên bên phải) $\rightarrow$ Chọn **"Save & Run All (Commit)"** $\rightarrow$ Bấm **Save**.

Hệ thống sẽ chạy ngầm độc lập trên máy chủ của Kaggle. Bạn có thể tắt trình duyệt và đi làm việc khác.

---

## BƯỚC 4: TẢI TRỌNG SỐ ADAPTER VỀ MÁY LOCAL

Sau khi Kaggle báo chạy xong (**Complete**):
1. Vào tab **Output** của Notebook.
2. Tải file `vietlaw_lora_adapter.zip` (~25MB) về máy.
3. Giải nén vào thư mục: `Project/models/lora_adapter/` trên máy local.
4. Backend FastAPI sẽ tự động nạp adapter này phục vụ sinh lời giải chuẩn barem DUT!
