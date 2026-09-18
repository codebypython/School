# ☁️ HƯỚNG DẪN VẬN HÀNH GOOGLE COLAB (COLAB TRAINING RUNBOOK)
## Dự án: Pediatric Bone Age Assessment (CORP-01-CV)

> **Mục tiêu**: Thực thi toàn bộ quá trình nạp dữ liệu ~10GB, tiền xử lý ảnh, huấn luyện chuỗi mô hình Deep Learning (ResNet-50, EfficientNet-B4, Swin-T) trên đám mây GPU Tesla T4 mà không tốn dung lượng máy cá nhân.

---

## 🚀 QUY TRÌNH 4 BƯỚC THỰC THI TRÊN GOOGLE COLAB

### Bước 1: Mở Google Colab & Kích hoạt GPU
1. Truy cập [Google Colab](https://colab.research.google.com).
2. Chọn **File** $\to$ **Upload notebook** $\to$ Tải lên file:
   [`01_RSNA_Bone_Age_End_to_End_Pipeline.ipynb`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/01_RSNA_Bone_Age_End_to_End_Pipeline.ipynb)
3. Chuyển sang phần cứng GPU:
   - Menu: **Runtime** $\to$ **Change runtime type** (Thay đổi loại môi trường).
   - Chọn **T4 GPU** $\to$ Bấm **Save**.

---

### Bước 2: Tải Dữ liệu Siêu Tốc Bằng Kaggle Token
Chạy cell khởi tạo đầu tiên trong Colab (chứa mã token đã kích hoạt):

```python
import os

# Gán Token đã được cấu hình từ tài khoản Kaggle của bạn
os.environ["KAGGLE_API_TOKEN"] = "KGAT_647e2aba908b47705fadfd3ea663af4f"

# Cài đặt Kaggle CLI mới nhất
!pip install -q --upgrade kaggle

# Tải bộ dữ liệu chính thức vào ổ đĩa RAM/SSD của Colab (~100 MB/s, mất ~1-2 phút)
!kaggle datasets download -d kmader/rsna-bone-age -p /content/data/

# Giải nén trực tiếp vào /content/data/rsna-bone-age/
!unzip -q /content/data/rsna-bone-age.zip -d /content/data/rsna-bone-age/
print("✅ Tải và giải nén dữ liệu RSNA trên Colab thành công!")
```

---

### Bước 3: Huấn Luyện & Tự Động Lưu Checkpoint Sang Google Drive
Để chống mất dữ liệu khi Colab ngắt kết nối (Disconnect):

```python
from google.colab import drive

# 1. Mount Google Drive cá nhân
drive.mount('/content/drive')

# 2. Tạo folder lưu trữ checkpoints trên Drive
save_dir = '/content/drive/MyDrive/RSNA_Bone_Age_Models/'
os.makedirs(save_dir, exist_ok=True)

# 3. Khi train, lưu model sau mỗi epoch tốt nhất
# Ví dụ: torch.save(model.state_dict(), os.path.join(save_dir, 'best_model_e3.pth'))
```

---

### Bước 4: Tải Kết Quả Về Máy Local (Đồng Bộ Vào Local HQ)
Sau khi huấn luyện xong trên Colab, bạn tải 2 tệp về máy cá nhân:
1. **File trọng số tối ưu**: `best_model.pth` (khoảng ~80MB - 120MB) $\to$ Đặt vào:  
   `03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research Project/experiment_results/best_model.pth`
2. **File nhật ký đo lường**: `training_history.csv` (chứa các giá trị Loss, MAE từng epoch) $\to$ Đặt vào:  
   `03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research Project/experiment_results/training_history.csv`
