# 👁️ MASTER WORKSPACE: THỊ GIÁC MÁY TÍNH (COMPUTER VISION)
# Đại học Bách khoa — Đại học Đà Nẵng | Semester 7

> 🎓 **Mã học phần**: CV-DUT
> 📐 **Lộ trình**: 4 Giai đoạn — Toán nền tảng → CV Cổ điển → Deep Learning → Advanced & Edge
> 🛠️ **Công cụ**: Python, PyTorch, OpenCV, Albumentations, ONNX Runtime

---

## 📊 I. ROADMAP PROGRESS — TIẾN ĐỘ 4 GIAI ĐOẠN

> 💡 **Notion**: Convert thành Database → Tạo **Board View** grouped by `Giai Đoạn`.

| Giai Đoạn | Chủ Đề | Mục Tiêu | Trạng Thái | Tiến Độ (%) | Ghi Chú |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **GĐ1** | Đại số Tuyến tính cho Spatial Tensor | Hiểu biểu diễn ảnh dạng Tensor, SVD, PCA | 🔲 Chưa bắt đầu | 0% | Prerequisite |
| **GĐ1** | Vi tích phân & Tối ưu hóa | Matrix Calculus, Backpropagation, Loss Functions | 🔲 Chưa bắt đầu | 0% | |
| **GĐ1** | Xác suất Thống kê & Nhiễu | Noise Models, Bayes, MLE/MAP | 🔲 Chưa bắt đầu | 0% | |
| **GĐ2** | Biến đổi Không gian & Tần số | Gaussian, Canny, DFT, Morphology | 🔲 Chưa bắt đầu | 0% | |
| **GĐ2** | Trích xuất Đặc trưng Thủ công | Harris, SIFT, ORB, HOG | 🔲 Chưa bắt đầu | 0% | |
| **GĐ2** | Thị giác Hình học & Camera Calibration | Pinhole Model, Stereo Vision, Homography | 🔲 Chưa bắt đầu | 0% | |
| **GĐ3** | CNN & Feature Extraction | AlexNet → ResNet → MobileNet → EfficientNet | 🔲 Chưa bắt đầu | 0% | Core |
| **GĐ3** | Object Detection | Faster R-CNN, YOLO, DETR | 🔲 Chưa bắt đầu | 0% | Core |
| **GĐ3** | Image Segmentation | FCN, U-Net, DeepLabV3+, Mask R-CNN, SAM | 🔲 Chưa bắt đầu | 0% | Core |
| **GĐ3** | Video Analysis & Tracking | Optical Flow, DeepSORT, ByteTrack | 🔲 Chưa bắt đầu | 0% | |
| **GĐ4** | Vision Transformers & VLM | ViT, Swin, CLIP, LLaVA | 🔲 Chưa bắt đầu | 0% | Advanced |
| **GĐ4** | 3D Vision & Generative | GANs, Diffusion, NeRF, 3D Gaussian Splatting | 🔲 Chưa bắt đầu | 0% | Advanced |
| **GĐ4** | Model Deployment & Edge | Quantization, Pruning, ONNX, TensorRT | 🔲 Chưa bắt đầu | 0% | Practical |

---

## 🧠 II. CONCEPT MASTERY — ACTIVE RECALL DATABASE (Spaced Repetition)

> 💡 **Notion Formula** cho cột `Cần Ôn?`:
> ```javascript
> if(empty(prop("Lần Ôn")), true, dateAdd(prop("Lần Ôn"), prop("Chu Kỳ"), "days") <= now())
> ```

| Khái Niệm | GĐ | Chủ Đề | Công Thức / Core Idea | Confidence | Lần Ôn | Chu Kỳ | Cần Ôn? | Priority |
| :--- | :---: | :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **Conv Output Size** | 1 | CNN Math | $W_{out} = \lfloor \frac{W - F + 2P}{S} \rfloor + 1$ | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **SVD Decomposition** | 1 | Linear Algebra | $\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$ — Nén ảnh, giảm chiều | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **Cross-Entropy Loss** | 1 | Loss Functions | $\mathcal{L}_{CE} = -\sum y_i \log(\hat{y}_i)$ | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **Focal Loss** | 1 | Loss Functions | $\mathcal{L}_{FL} = -\alpha_t(1-p_t)^\gamma\log(p_t)$ — Giải quyết class imbalance | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | 🟡 Medium |
| **IoU & CIoU Loss** | 1 | Loss Functions | $\text{IoU} = \frac{|A \cap B|}{|A \cup B|}$ — Bbox regression | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **Gaussian Blur** | 2 | Spatial Filter | $G(x,y) = \frac{1}{2\pi\sigma^2}e^{-\frac{x^2+y^2}{2\sigma^2}}$ | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🟡 Medium |
| **Canny Edge Detector** | 2 | Edge Detection | 4 bước: Noise→Gradient→NMS→Hysteresis | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **SIFT — Scale Invariant** | 2 | Feature Engineering | DoG Scale Space → Keypoint Detection ở $(x,y,\sigma)$ | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | 🟡 Medium |
| **Pinhole Camera Model** | 2 | Geometric CV | $s[u,v,1]^T = \mathbf{K}[\mathbf{R}|\mathbf{t}][X,Y,Z,1]^T$ | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | 🟡 Medium |
| **Stereo Depth** | 2 | Geometric CV | $Z = \frac{f \cdot B}{d}$ — Depth from Disparity | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | 🟡 Medium |
| **ResNet Residual Block** | 3 | CNN Architecture | $y = F(x) + x$ → Gradient: $\frac{\partial y}{\partial x} = \frac{\partial F}{\partial x} + 1$ | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **Depthwise Separable Conv** | 3 | MobileNet | Tách Depthwise + Pointwise → Giảm ~9x compute | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **EfficientNet Compound Scaling** | 3 | CNN Architecture | Scale đồng thời Width + Depth + Resolution | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | 🟡 Medium |
| **Faster R-CNN Pipeline** | 3 | Object Detection | RPN → Anchor Boxes → RoI Align → Cls + BBox | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **YOLO — Anchor-free vs Anchor-based** | 3 | Object Detection | Anchor-free: dự đoán trực tiếp center + (l,r,t,b) | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **U-Net Skip Connections** | 3 | Segmentation | Encoder-Decoder + Skip → Giữ spatial info | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **DeepLabV3+ ASPP** | 3 | Segmentation | Atrous Conv → Tăng Receptive Field không giảm size | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | 🟡 Medium |
| **Mask R-CNN** | 3 | Instance Seg | Faster R-CNN + FCN Mask Branch (parallel) | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **DeepSORT Tracking** | 3 | MOT | Kalman Filter + Re-ID Embedding + Hungarian | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | 🟡 Medium |
| **ViT Patch Embedding** | 4 | Vision Transformer | Chia ảnh $H\times W$ thành patches $P\times P$ → Linear Projection | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **Self-Attention** | 4 | Transformer | $\text{Attn}(Q,K,V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$ | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **Swin Transformer** | 4 | Vision Transformer | Shifted Window → $O(M^2 \cdot N)$ thay vì $O(N^2)$ | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **CLIP Contrastive Learning** | 4 | VLM | Text Encoder + Image Encoder → Contrastive Loss | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | 🔥 High |
| **PTQ vs QAT** | 4 | Quantization | PTQ=post-train (nhanh, loss accuracy), QAT=train-aware (chính xác) | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | 🟡 Medium |
| **NeRF** | 4 | 3D Vision | $f_\theta(x,y,z,\theta,\phi) \rightarrow (r,g,b,\sigma)$ + Volume Rendering | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | 🟡 Medium |

---

## 📄 III. PAPER READING TRACKER

> 💡 **Notion**: Convert thành Database → Tạo **Board View** grouped by `Trạng Thái`, **Table View** sorted by `Priority`.

| # | Tên Paper | Chủ Đề | Năm | Innovation | Trạng Thái | Priority | Summary Notes |
| :-: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| 1 | **ResNet** (Deep Residual Learning) | Classification | 2015 | Skip Connections, Residual Learning | ✅ Done | 🔥 High | |
| 2 | **Faster R-CNN** | Object Detection | 2015 | Region Proposal Network (RPN) | ✅ Done | 🔥 High | |
| 3 | **YOLOv1** (You Only Look Once) | Object Detection | 2016 | Real-time Unified Detection | ✅ Done | 🔥 High | |
| 4 | **U-Net** | Segmentation | 2015 | Encoder-Decoder + Skip Connections | ✅ Done | 🔥 High | |
| 5 | **DeepLabV3+** | Segmentation | 2018 | Atrous Spatial Pyramid Pooling (ASPP) | 📖 Reading | 🟡 Medium | |
| 6 | **Attention Is All You Need** | Transformer | 2017 | Self-Attention Mechanism | ✅ Done | 🔥 High | |
| 7 | **ViT** (An Image is Worth 16x16 Words) | Vision Transformer | 2020 | Pure Transformer on Image Patches | 📖 Reading | 🔥 High | |
| 8 | **Swin Transformer** | Vision Transformer | 2021 | Shifted Window Self-Attention | 📋 Todo | 🔥 High | |
| 9 | **CLIP** | Multimodal VLM | 2021 | Contrastive Image-Text Pre-training | 📖 Reading | 🔥 High | |
| 10 | **DETR** (End-to-End Detection) | Detection Transformer | 2020 | Bipartite Matching Loss, No NMS | 📋 Todo | 🟡 Medium | |
| 11 | **Mask R-CNN** | Instance Segmentation | 2017 | RoIAlign + Mask Branch | ✅ Done | 🔥 High | |
| 12 | **ByteTrack** | Multi-Object Tracking | 2022 | Low-score Detection Association | 📋 Todo | 🟡 Medium | |
| 13 | **RAFT** | Optical Flow | 2020 | Recurrent All-Pairs Field Transforms | 📋 Todo | 🟢 Low | |
| 14 | **NeRF** | 3D Vision | 2020 | Neural Radiance Fields | 📋 Todo | 🔥 High | |
| 15 | **3D Gaussian Splatting** | 3D Vision | 2023 | Real-time Radiance Field Rendering | 📋 Todo | 🔥 High | |
| 16 | **DDPM** (Denoising Diffusion) | Generative | 2020 | Score-based Diffusion | 📋 Todo | 🔥 High | |
| 17 | **SAM** (Segment Anything) | Foundation Model | 2023 | Promptable Segmentation at Scale | 📖 Reading | 🔥 High | |
| 18 | **YOLOv8 / YOLOv11** | Edge Detection | 2023-24 | Anchor-free, C2f/C3k2, DFL | ✅ Done | 🔥 High | |
| 19 | **ControlNet** | Generative | 2023 | Conditional Control for Diffusion | 📋 Todo | 🟡 Medium | |
| 20 | **LLaVA** | Visual Language | 2023 | Visual Instruction Tuning with LLMs | 📋 Todo | 🔥 High | |

---

## 💻 IV. CODE SNIPPET VAULT — PYTORCH TEMPLATES

<details>
<summary><b>🐍 Template 1: Custom PyTorch Dataset & Augmentation Pipeline</b></summary>

```python
import os, cv2, torch
from torch.utils.data import Dataset, DataLoader
import albumentations as A
from albumentations.pytorch import ToTensorV2

class CVDataset(Dataset):
    """Custom Dataset Template cho Classification / Detection."""
    def __init__(self, image_dir, labels_dict, transform=None):
        self.image_dir = image_dir
        self.image_names = list(labels_dict.keys())
        self.labels = labels_dict
        self.transform = transform

    def __len__(self):
        return len(self.image_names)

    def __getitem__(self, idx):
        img_name = self.image_names[idx]
        img_path = os.path.join(self.image_dir, img_name)
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # BGR → RGB
        label = self.labels[img_name]
        if self.transform:
            augmented = self.transform(image=image)
            image = augmented['image']
        return image, torch.tensor(label, dtype=torch.long)

# Augmentation Pipeline chuẩn
train_transform = A.Compose([
    A.Resize(224, 224),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2(),
])
```

</details>

<details>
<summary><b>🐍 Template 2: Modern Training Loop (AMP + Checkpoint)</b></summary>

```python
import torch, torch.nn as nn
from torch.cuda.amp import autocast, GradScaler

def train_one_epoch(model, dataloader, criterion, optimizer, scaler, device):
    model.train()
    running_loss, correct, total = 0.0, 0, 0

    for images, targets in dataloader:
        images, targets = images.to(device), targets.to(device)
        optimizer.zero_grad()

        with autocast():  # AMP — tăng tốc GPU
            outputs = model(images)
            loss = criterion(outputs, targets)

        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()

        running_loss += loss.item() * images.size(0)
        _, preds = outputs.max(1)
        total += targets.size(0)
        correct += preds.eq(targets).sum().item()

    return running_loss / total, correct / total

# Checkpoint save/load
def save_checkpoint(model, optimizer, epoch, path):
    torch.save({'epoch': epoch, 'model': model.state_dict(),
                'optimizer': optimizer.state_dict()}, path)
```

</details>

<details>
<summary><b>🐍 Template 3: Export ONNX & Inference</b></summary>

```python
import torch
import onnxruntime as ort
import numpy as np

def export_to_onnx(model, save_path="model.onnx", input_shape=(1, 3, 224, 224)):
    model.eval()
    dummy = torch.randn(*input_shape, device='cpu')
    torch.onnx.export(model, dummy, save_path, export_params=True,
                      opset_version=14, do_constant_folding=True,
                      input_names=['input'], output_names=['output'],
                      dynamic_axes={'input': {0: 'batch'}, 'output': {0: 'batch'}})

def run_onnx_inference(onnx_path, dummy_array):
    session = ort.InferenceSession(onnx_path,
        providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    input_name = session.get_inputs()[0].name
    return session.run(None, {input_name: dummy_array})
```

</details>

---

## 🔁 V. ACTIVE RECALL QUIZ — SELF-TEST

<details>
<summary><b>🟢 Q1: Kích thước output của ảnh 224×224 qua Conv 7×7, Stride 2, Padding 3?</b></summary>

Áp dụng: $W_{out} = \lfloor \frac{224 - 7 + 2(3)}{2} \rfloor + 1 = \lfloor \frac{223}{2} \rfloor + 1 = 112$

**Đáp án: 112 × 112**

</details>

<details>
<summary><b>🟢 Q2: Median Filter khác Gaussian Blur thế nào?</b></summary>

- **Gaussian**: Lọc tuyến tính, trung bình có trọng số → Mờ biên, không hiệu quả với Salt-and-Pepper
- **Median**: Lọc phi tuyến, giá trị trung vị → **Giữ biên + Loại bỏ tốt nhiễu muối tiêu**

</details>

<details>
<summary><b>🟡 Q3: Vanishing Gradient là gì? ResNet giải quyết thế nào?</b></summary>

- **Vấn đề**: Mạng sâu → gradient nhân qua nhiều tầng ($<1$) → tiệm cận 0 → tầng đầu không học được
- **ResNet**: Skip Connection: $y = F(x) + x$ → Gradient: $\frac{\partial y}{\partial x} = \frac{\partial F}{\partial x} + 1$ → Luôn có $+1$, gradient không triệt tiêu

</details>

<details>
<summary><b>🟡 Q4: Tại sao Depthwise Separable Conv tiết kiệm compute?</b></summary>

Tách Standard Conv thành 2 bước:
1. **Depthwise**: Lọc từng kênh riêng lẻ ($H \times W \times D_{in} \times D_k^2$)
2. **Pointwise**: $1\times1$ Conv kết hợp kênh ($H \times W \times D_{in} \times D_{out}$)

Tỷ lệ giảm: $\frac{1}{D_{out}} + \frac{1}{D_k^2} \approx \frac{1}{9}$ (với $D_k=3$) → **Giảm ~9x!**

</details>

<details>
<summary><b>🔴 Q5: Swin Transformer giải quyết vấn đề gì của ViT?</b></summary>

- **ViT**: Self-Attention complexity = $O(N^2)$ với $N$ = số patches → Ảnh lớn = bùng nổ bộ nhớ
- **Swin**: **Shifted Window Attention** — tính attention trong cửa sổ $M \times M$ → $O(M^2 \cdot N)$ = **tuyến tính!**

</details>

<details>
<summary><b>🔴 Q6: PTQ vs QAT trong Model Quantization?</b></summary>

- **PTQ** (Post-Training): Chuyển FP32→INT8 **sau** train → Nhanh nhưng dễ mất accuracy
- **QAT** (Quantization-Aware Training): Mô phỏng quantization **trong** train → Mạng tự thích nghi, giữ accuracy

</details>

---

## 🛠️ VI. CAPSTONE PROJECTS PORTFOLIO

| # | Project | Bài Toán | Stack | Output | Priority | Status |
| :-: | :--- | :--- | :--- | :--- | :---: | :---: |
| 1 | **Traffic Surveillance** | Detect + Track xe từ camera | YOLOv8 + ByteTrack + OpenCV | Github + Video demo + Dashboard | 🔥 High | 📋 Todo |
| 2 | **Medical Image Segmentation** | Phân vùng khối u MRI/CT | U-Net / DeepLabV3+ + MONAI | Notebook + Dice > 0.88 | 🟡 Medium | 📋 Todo |
| 3 | **Driver Drowsiness Alert** | Nhận diện buồn ngủ realtime | MediaPipe + ONNX + Raspberry Pi | App > 30 FPS trên Edge | 🟡 Medium | 📋 Todo |
| 4 | **Product Retrieval** | Text-to-Image Search E-commerce | CLIP + Qdrant + FastAPI | Web API + Top-K results | 🔥 High | 📋 Todo |

---

## 📐 VII. MATH FORMULA CHEATSHEET

<details>
<summary><b>📏 Đại số Tuyến tính</b></summary>

| Công thức | Ý nghĩa |
|:----------|:---------|
| $\mathbf{X} \in \mathbb{R}^{H \times W \times C}$ | Biểu diễn ảnh RGB |
| $(I * K)(i,j) = \sum_m \sum_n I(i-m,j-n) K(m,n)$ | Phép tích chập |
| $\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$ | SVD — Nén ảnh |

</details>

<details>
<summary><b>📐 Loss Functions</b></summary>

| Loss | Công thức | Use Case |
|:-----|:---------|:---------|
| Cross-Entropy | $-\sum y_i \log(\hat{y}_i)$ | Classification |
| Focal Loss | $-\alpha_t(1-p_t)^\gamma\log(p_t)$ | Class Imbalance |
| IoU/CIoU | $1 - \text{IoU} + \frac{\rho^2}{c^2} + \alpha v$ | Bbox Regression |
| Dice Loss | $1 - \frac{2\sum y_i\hat{y}_i}{\sum y_i + \sum \hat{y}_i}$ | Medical Segmentation |

</details>

<details>
<summary><b>🧠 CNN & Transformer</b></summary>

| Công thức | Context |
|:----------|:--------|
| $W_{out} = \lfloor\frac{W-F+2P}{S}\rfloor + 1$ | Conv Output Size |
| $y = F(x) + x$ | ResNet Residual |
| $\text{Attn}(Q,K,V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$ | Self-Attention |

</details>

---

## 🗓️ VIII. DAILY SOP — QUY TRÌNH HỌC HÀNG NGÀY

- [ ] 🌅 **Sáng (15 phút)**: Mở DB Concept Mastery → Lọc `Cần Ôn? = ⚠️` → Tự recall công thức trước khi xem đáp án
- [ ] 🌤️ **Chiều (45 phút)**: Đọc Paper theo Paper Tracker (1 paper/tuần) → Ghi Summary Notes
- [ ] 🌆 **Chiều (60 phút)**: Code thực hành — chạy Template trong Code Vault hoặc implement bài tập
- [ ] 🌃 **Tối (15 phút)**: Làm 2-3 câu Active Recall Quiz → Cập nhật Confidence level

---

> 🏁 **Mỗi tuần quay lại Mục I để cập nhật tiến độ Roadmap. Mục tiêu: hoàn thành GĐ1-2 trong 4 tuần đầu, GĐ3 trong 6 tuần tiếp, GĐ4 song song với Project.**
