# 📜 ĐIỀU LỆ PHÒNG KỸ THUẬT, CODE & THỰC NGHIỆM (ENGINEERING LABS & CODE DEPT)
## Phòng 03 — Công Ty Công Nghệ Thị Giác Máy Tính (CORP-01-CV)

> **Mã Phòng Ban:** `CV-DEPT-03`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (`HM-00`) & Giám Sát Kỹ Thuật (`SMS-02`)  
> **Cố vấn chuyên môn:** DUT Computer Vision Mentor (`AGENT_PROFILE.md`)  
> **Tiêu chuẩn chất lượng:** PyTorch 2.x / OpenCV 4.x / Albumentations / CUDA Tensor Safety / No-Magic Philosophy

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kỹ Thuật & Thực Nghiệm là **trung tâm tác chiến mã nguồn thị giác máy tính**:
1. **Lập Trình Thị Giác Máy Tính Cổ Điển & Hiện Đại**: Phát triển các bộ lọc không gian, trích xuất đặc trưng hình học (SIFT, ORB, RANSAC, Homography) và mạng nơ-ron tích chập (CNNs, Vision Transformers).
2. **Xây Dựng Training Pipelines Bền Vững**: Tự tay viết toàn bộ Custom PyTorch Dataset, DataLoader, Training Loop, và Validation Loop theo triết lý "No Magic" (không dùng các thư viện tự động đóng gói che giấu bản chất).
3. **Tối Ưu Hóa Bộ Nhớ GPU (RTX 3050 4GB / Colab T4)**: Kiểm soát nghiêm ngặt dung lượng VRAM, sử dụng Mixed Precision Training (`torch.cuda.amp`) và Gradient Accumulation.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (AGENT BẮT BUỘC TUÂN THỦ)

1. **Quy Tắc Chú Thích Tensor Shape Bắt Buộc (Tensor Shape Invariant)**:
   - **BẮT BUỘC**: Mọi biến Tensor tại đầu vào và đầu ra của mỗi layer trong PyTorch `forward()` phải có chú thích kích thước rõ ràng theo chuẩn: `[Batch_Size, Channels, Height, Width]` (`[B, C, H, W]`).
   - Ví dụ bắt buộc:
     ```python
     # x: [B, 3, 224, 224] - Batch ảnh đầu vào RGB
     out = self.conv1(x)
     # out: [B, 64, 112, 112] - Sau Conv2D kernel 7x7 stride 2 + padding 3
     ```
2. **Quy Tắc Cố Định Seed Tái Lập (Reproducibility Rule)**:
   - Mọi script huấn luyện hoặc notebook bắt buộc phải cố định random seed ở dòng đầu tiên:
     ```python
     torch.manual_seed(42)
     np.random.seed(42)
     torch.backends.cudnn.deterministic = True
     ```
3. **Quy Tắc Quản Trị Bộ Nhớ GPU (VRAM Safety Invariant)**:
   - **CẤM TUYỆT ĐỐI**: Tích lũy tensor có giữ lịch sử tính toán vào list gây rò rỉ VRAM (ví dụ cấm: `losses.append(loss)`).
   - **BẮT BUỘC**: Rút trích giá trị số thực bằng `losses.append(loss.item())`.
   - Luôn sử dụng context manager `torch.no_grad()` trong pha validation / inference.
4. **Quy Tắc Chuẩn Hóa Ảnh (Normalization Invariant)**:
   - Mọi ảnh nạp vào PyTorch Model phải được chuẩn hóa về dải $[0, 1]$ sau đó trừ mean và chia std chuẩn của ImageNet (`mean=[0.485, 0.456, 0.406]`, `std=[0.229, 0.224, 0.225]`).

---

## 🛠️ 3. SKILLS ROUTE & TOOLCHAIN ĐIỀU HÀNH CHUẨN

### 3.1 Toolchain Yêu Cầu
- **Python Runtime**: Python 3.10 / 3.11.
- **Deep Learning Core**: PyTorch 2.1+, Torchvision 0.16+, CUDA 11.8 / 12.1.
- **Xử lý ảnh & Tăng cường**: OpenCV (`opencv-python-headless`), Albumentations, Pillow.
- **Đo đạc & Trực quan**: Matplotlib, Seaborn, TensorBoard, Torchinfo.

### 3.2 Bộ Lệnh CLI Tác Nghiệp Chuẩn

```powershell
# 1. Kiểm tra trạng thái GPU và phiên bản CUDA khả dụng
python -c "import torch; print('CUDA Available:', torch.cuda.is_available(), '| Device:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU')"

# 2. Chạy script huấn luyện với theo dõi log qua TensorBoard
python train.py --epochs 30 --batch-size 16 --lr 0.001 --data-dir ./data

# 3. Khởi chạy TensorBoard kiểm tra đồ thị Loss và mAP
tensorboard --logdir=./runs --port=6006
```

---

## 💻 4. MẪU KHUNG CODE / TEMPLATE CHUẨN NGHIỆP VỤ (GOLD MASTER PYTORCH BOILERPLATE)

Mẫu chuẩn mực **PyTorch Custom Dataset + Mixed Precision Training Loop**:

```python
"""
Custom PyTorch Dataset & Mixed Precision Trainer for Medical Bone Age / Image Classification
Tuân thủ nghiêm ngặt tiêu chuẩn VRAM Safety và Tensor Shape Annotations.
"""
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import albumentations as A
from albumentations.pytorch import ToTensorV2
import cv2
import numpy as np


class SafeVisionDataset(Dataset):
    """Custom Dataset sử dụng OpenCV & Albumentations đảm bảo tốc độ I/O cực đại."""
    def __init__(self, image_paths: list[str], labels: list[int], transform: A.Compose | None = None) -> None:
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform

    def __len__(self) -> int:
        return len(self.image_paths)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        # Đọc ảnh dạng BGR qua OpenCV và chuyển sang RGB
        img = cv2.imread(self.image_paths[idx])
        if img is None:
            raise FileNotFoundError(f"Không thể đọc file ảnh: {self.image_paths[idx]}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if self.transform:
            augmented = self.transform(image=img)
            img = augmented['image'] # img: [C, H, W] tensor
        else:
            img = ToTensorV2()(image=img)['image'].float() / 255.0

        label = torch.tensor(self.labels[idx], dtype=torch.long)
        return img, label


def train_one_epoch(
    model: nn.Module,
    dataloader: DataLoader,
    criterion: nn.Module,
    optimizer: torch.optim.Optimizer,
    scaler: torch.cuda.amp.GradScaler,
    device: torch.device
) -> float:
    """Vòng lặp huấn luyện 1 Epoch hỗ trợ Mixed Precision tăng tốc x2 và tiết kiệm 40% VRAM."""
    model.train()
    running_loss = 0.0

    for images, targets in dataloader:
        # images: [B, 3, H, W], targets: [B]
        images = images.to(device, non_blocking=True)
        targets = targets.to(device, non_blocking=True)

        optimizer.zero_grad()

        # Tự động chuyển đổi FP16 / FP32 để tăng tốc GPU
        with torch.cuda.amp.autocast(enabled=(device.type == 'cuda')):
            outputs = model(images) # outputs: [B, num_classes]
            loss = criterion(outputs, targets)

        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()

        # BẮT BUỘC: .item() để ngắt tensor khỏi computational graph, chống rò rỉ VRAM
        running_loss += loss.item() * images.size(0)

    return running_loss / len(dataloader.dataset)
```

---

## 🛡️ 5. BỘ TIÊU CHÍ NGHIỆM THU CHẤT LƯỢNG (DEFINITION OF DONE - DoD)

- [ ] **DoD-1 (Zero CUDA OOM)**: Script huấn luyện chạy trọn vẹn 100% epochs mà không gặp lỗi `CUDA out of memory`.
- [ ] **DoD-2 (Tensor Shape Validated)**: 100% layers trong mạng đều có ghi chú shape `[B, C, H, W]` tại file model definition.
- [ ] **DoD-3 (Data Leakage Free)**: Bộ Validation / Test Set hoàn toàn tách biệt, không bị fit transform từ Training Set.
- [ ] **DoD-4 (Metric Target Achieved)**: Mô hình đạt tối thiểu độ chính xác mục tiêu (Accuracy $\ge 85\%$ hoặc mAP@0.5 $\ge 0.70$).

---

## 🚑 6. CẨM NANG XỬ LÝ SỰ CỐ THỊ GIÁC MÁY TÍNH (TOP 3 RUNBOOKS)

### 🚨 RUNBOOK 1: XỬ LÝ LỖI CUDA OUT OF MEMORY (OOM)
* **Triệu chứng**: `RuntimeError: CUDA out of memory. Tried to allocate X.XX GiB`.
* **Khắc phục theo thứ tự ưu tiên**:
  1. Giảm kích thước Batch Size: từ 32 $\rightarrow$ 16 $\rightarrow$ 8.
  2. Bật Mixed Precision Training (`torch.cuda.amp.autocast()`).
  3. Sử dụng Gradient Accumulation để tích lũy gradient qua nhiều micro-batches nhỏ.
  4. Thu hồi bộ nhớ đệm: `torch.cuda.empty_cache()`.

### 🚨 RUNBOOK 2: XỬ LÝ LỖI LOSS BỊ NaN HOẶC INFINITY
* **Triệu chứng**: `Loss: nan` ngay sau vài batch đầu tiên.
* **Nguyên nhân & Khắc phục**:
  1. Tốc độ học (Learning Rate) quá lớn $\rightarrow$ Giảm Learning Rate xuống 10 lần (vd: $10^{-3} \rightarrow 10^{-4}$).
  2. Dữ liệu đầu vào chưa chuẩn hóa $\rightarrow$ Đảm bảo giá trị pixel nằm trong $[0, 1]$ hoặc được trừ mean/std.
  3. Áp dụng Gradient Clipping trước bước `optimizer.step()`: `torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)`.

### 🚨 RUNBOOK 3: XỬ LÝ LỆCH SHAPE TENSOR (RUNTIME MAT1 AND MAT2 SHAPES MISMATCH)
* **Triệu chứng**: `RuntimeError: mat1 and mat2 shapes cannot be multiplied (BxN and MxC)`.
* **Khắc phục**:
  - Chèn lệnh debug in shape: `print(x.shape)` ngay trước layer Linear kết nối Fully Connected.
  - Sử dụng thư viện `torchinfo.summary(model, input_size=(1, 3, 224, 224))` để quan sát dòng chảy shape qua từng layer.
