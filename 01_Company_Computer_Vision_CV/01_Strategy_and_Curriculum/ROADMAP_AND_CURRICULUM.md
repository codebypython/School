## 🧭 MỤC LỤC & TỔNG QUAN HỆ THỐNG

1. [📐 Giai đoạn 1: Nền tảng Toán học & Lập trình Chuyên sâu](#1-giai-đoạn-1-nền-tảng-toán-học--lập-trình-chuyên-sâu)
2. [🖼️ Giai đoạn 2: Xử lý Ảnh Cổ điển & Hình học Thị giác (Classical CV)](#2-giai-đoạn-2-xử-lý-ảnh-cổ-điển--hình-học-thị-giác-classical-cv)
3. [🧠 Giai đoạn 3: Deep Learning cho Computer Vision (Core Architecture & Tasks)](#3-giai-đoạn-3-deep-learning-cho-computer-vision-core-architecture--tasks)
4. [🚀 Giai đoạn 4: Nghiên cứu Tiên tiến & Thị giác Máy tính Ứng dụng (Advanced & Edge CV)](#4-giai-đoạn-4-nghiên-cứu-tiên-tiến--thị-giác-máy-tính-ứng-dụng-advanced--edge-cv)
5. [📄 Notion Paper Reading Tracker (20+ Papers Kinh điển & Modern)](#5-notion-paper-reading-tracker)
6. [🔁 Hệ thống Active Recall & Spaced Repetition (Tự kiểm tra)](#6-hệ-thống-active-recall--spaced-repetition)
7. [💻 Code Snippet Vault & PyTorch Templates](#7-code-snippet-vault--pytorch-templates)
8. [🛠️ Danh mục Dự án Thực chiến (Capstone Projects Portfolio)](#8-danh-mục-dự-án-thực-chiến-capstone-projects-portfolio)

---

## 1. 📐 GIAI ĐOẠN 1: NỀN TẢNG TOÁN HỌC & LẬP TRÌNH CHUYÊN SÂU

### 1.1 Đại số Tuyến tính cho Spatial Tensor

- **Biểu diễn Ảnh dạng Tensor:**
  - Gray Image: $\mathbf{X} \in \mathbb{R}^{H \times W}$
  - Color Image (RGB): $\mathbf{X} \in \mathbb{R}^{H \times W \times C}$ với $C=3$
  - Batch Video Tensor: $\mathbf{V} \in \mathbb{R}^{B \times T \times C \times H \times W}$
- **Phép toán Tích chập Ma trận (Matrix Convolution):**
  $$(I * K)(i, j) = \sum_{m} \sum_{n} I(i-m, j-n) K(m, n)$$
- **Phân rã Ma trận (Matrix Decomposition):**
  - **Singular Value Decomposition (SVD):** $\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$. Ứng dụng trong nén ảnh (Image Compression) và giảm chiều dữ liệu.
  - **Principal Component Analysis (PCA):** Tìm các hướng có phương sai lớn nhất để trích xuất đặc trưng tuyến tính (Eigenfaces).

### 1.2 Vi tích phân & Tối ưu hóa (Calculus & Optimization)

- **Matrix Calculus & Backpropagation:**
  - Tính Gradient cho Tensor: $\frac{\partial \mathcal{L}}{\partial \mathbf{W}} = \frac{\partial \mathcal{L}}{\partial \mathbf{Y}} \cdot \frac{\partial \mathbf{Y}}{\partial \mathbf{W}}$
  - Chain Rule trên mạng tích chập (Convolutional Layers).
- **Hàm Mất Mát Cốt Lõi (Core Loss Functions):**
  - **Cross-Entropy Loss (Phân loại):**
    $$\mathcal{L}_{CE} = -\sum_{i=1}^{C} y_i \log(\hat{y}_i)$$
  - **Focal Loss (Giải quyết Class Imbalance trong Object Detection):**
    $$\mathcal{L}_{FL}(p_t) = -\alpha_t (1 - p_t)^\gamma \log(p_t)$$
  - **IoU & CIoU Loss (Bounding Box Regression):**
    $$\text{IoU} = \frac{|A \cap B|}{|A \cup B|}, \quad \mathcal{L}_{CIoU} = 1 - \text{IoU} + \frac{\rho^2(b, b^{gt})}{c^2} + \alpha v$$
  - **Dice Loss (Medical Image Segmentation):**
    $$\mathcal{L}_{Dice} = 1 - \frac{2 \sum y_i \hat{y}_i}{\sum y_i + \sum \hat{y}_i}$$

### 1.3 Xác suất Thống kê & Nhiễu Tín hiệu

- **Mô hình Nhiễu (Noise Models):** Gaussian Noise $\mathcal{N}(\mu, \sigma^2)$, Salt-and-Pepper Noise, Poisson Noise.
- **Định lý Bayes & Estimate:** Maximum Likelihood Estimation (MLE) và Maximum A Posteriori (MAP) trong bài toán khôi phục ảnh (Image Restoration/Denoising).

---

## 2. 🖼️ GIAI ĐOẠN 2: XỬ LÝ ẢNH CỔ ĐIỂN & HÌNH HỌC THỊ GIÁC (CLASSICAL CV)

### 2.1 Biến đổi Không gian & Tần số (Spatial & Frequency Filtering)

- **Spatial Filters:**
  - **Smoothing:** Gaussian Blur ($G(x,y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2+y^2}{2\sigma^2}}$), Median Filter (lọc nhiễu muối tiêu).
  - **Edge Detection:** Sobel Operator ($G_x, G_y$), Canny Edge Detector (4 bước: Noise Reduction $\rightarrow$ Gradient Calculation $\rightarrow$ Non-Maximum Suppression $\rightarrow$ Hysteresis Thresholding).
- **Frequency Domain (Miền tần số):**
  - 2D Discrete Fourier Transform (2D DFT):
    $$F(u, v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x, y) e^{-j2\pi \left(\frac{ux}{M} + \frac{vy}{N}\right)}$$
  - High-pass Filter (giữ lại chi tiết/biên), Low-pass Filter (làm mịn ảnh).
- **Morphological Operations:**
  - Erosion ($\ominus$), Dilation ($\oplus$), Opening ($A \circ B = (A \ominus B) \oplus B$), Closing ($A \bullet B = (A \oplus B) \ominus B$).

### 2.2 Trích xuất Đặc trưng Thủ công (Handcrafted Feature Engineering)

- **Point Detectors & Descriptors:**
  - **Harris Corner Detector:** Dựa trên ma trận Autocorrelation $M = \sum w(x,y) \begin{bmatrix} I_x^2 & I_x I_y \\ I_x I_y & I_y^2 \end{bmatrix}$.
  - **SIFT (Scale-Invariant Feature Transform):** Bất biến với tỷ lệ (Scale Space Difference of Gaussians) và phép xoay (Orientation Assignment).
  - **ORB (Oriented FAST and Rotated BRIEF):** Tốc độ cao, tối ưu cho các hệ thống thời gian thực (SLAM).
  - **HOG (Histogram of Oriented Gradients):** Tính phân bố hướng của gradient trong các cell, dùng cho phát hiện người (Pedestrian Detection với SVM).

### 2.3 Thị giác Hình học & Calib Camera (Geometric Computer Vision)

- **Pinhole Camera Model & Camera Calibration:**
  $$s \begin{bmatrix} u \\ v \\ 1 \end{bmatrix} = \mathbf{K} [\mathbf{R} | \mathbf{t}] \begin{bmatrix} X \\ Y \\ Z \\ 1 \end{bmatrix}$$
  - Intrinsic Matrix ($\mathbf{K}$): Tiêu cự ($f_x, f_y$), Điểm quang học ($c_x, c_y$).
  - Extrinsic Matrix ($[\mathbf{R} | \mathbf{t}]$): Ma trận xoay 3D và vector tịnh tiến.
  - Distortion Correction: Radial ($k_1, k_2$) và Tangential ($p_1, p_2$).
- **Stereo Vision & Epipolar Geometry:**
  - Fundamental Matrix ($\mathbf{F}$), Essential Matrix ($\mathbf{E}$).
  - Đáy tam giác Stereo (Baseline $B$), Độ lệch vị trí (Disparity $d$). Tính độ sâu:
    $$Z = \frac{f \cdot B}{d}$$
- **Homography Transformation:**
  - Ma trận Homography $\mathbf{H}_{3 \times 3}$ biến đổi phẳng-sang-phẳng (Planar Mapping). Ứng dụng trong ghép ảnh Panorama (Image Stitching).

---

## 3. 🧠 GIAI ĐOẠN 3: DEEP LEARNING CHO COMPUTER VISION (CORE ARCHITECTURE & TASKS)

### 3.1 Kiến trúc CNN & Feature Extraction

- **CNN Building Blocks:** Convolution Layer, Stride, Padding, Pooling (Max/Average), Batch Normalization, Residual Connection.
- **Công thức tính Kích thước Output:**
  $$\text{Output Size} = \left\lfloor \frac{W - F + 2P}{S} \right\rfloor + 1$$
- **Sự tiến hóa kiến trúc (Evolutionary Path):**
  - **AlexNet / VGG:** Tăng chiều sâu mạng ($3 \times 3$ conv stack).
  - **ResNet:** Giải quyết Vanishing/Exploding Gradient bằng Residual Block ($y = F(x) + x$).
  - **MobileNet (v1/v2/v3):** Depthwise Separable Convolution (tách thành Depthwise + Pointwise Conv), giảm $\approx 8-9$ lần chi phí tính toán.
  - **EfficientNet:** Compound Scaling (Mở rộng đồng thời Width, Depth, Resolution).

### 3.2 Phát hiện Đối tượng (Object Detection)

```text
                    ┌── Two-Stage Detector ──► Faster R-CNN (RPN + RoI Align)
Object Detection ───┼── Single-Stage Detector ─► YOLO Series (v5/v8/v9/v10/v11)
                    └── Transformer-based ────► DETR (Bipartite Matching Loss)
```

- **Two-Stage Detectors:**
  - **Faster R-CNN:** Region Proposal Network (RPN) đề xuất Anchor Boxes $\rightarrow$ RoI Pooling/Align $\rightarrow$ Classification + Bounding Box Regression.
  - **Feature Pyramid Networks (FPN):** Kết hợp Feature Maps đa quy mô (Multi-scale) cho đối tượng nhỏ.
- **Single-Stage Detectors (YOLO Paradigm):**
  - **YOLO Pipeline:** Chia grid $S \times S$, dự đoán trực tiếp class probability và Bounding Box coordinates.
  - **Cấu trúc Hiện đại (YOLOv8/v9/v10/v11):** Anchor-free Head, Decoupled Head (tách rời Cls/Bbox), TaskAlignedAssigner, Loss: $\mathcal{L}_{total} = \lambda_1 \mathcal{L}_{BCE} + \lambda_2 \mathcal{L}_{CIoU} + \lambda_3 \mathcal{L}_{DFL}$.
- **Transformer-based Detector:**
  - **DETR:** Sử dụng CNN Backbone + Transformer Encoder-Decoder + Hungarian Loss (Bipartite Matching) để loại bỏ NMS (Non-Maximum Suppression).

### 3.3 Phân vùng Ảnh (Image Segmentation)

- **Semantic Segmentation:**
  - **FCN / U-Net:** Cấu trúc Encoder-Decoder với Skip Connections (giữ lại thông tin không gian độ phân giải cao). Chuẩn mực cho Ảnh y tế.
  - **DeepLabV3+:** Atrous Convolution (Dilated Conv) tăng Receptive Field không làm giảm kích thước feature map; Atrous Spatial Pyramid Pooling (ASPP).
- **Instance & Panoptic Segmentation:**
  - **Mask R-CNN:** Phát triển từ Faster R-CNN, thêm nhánh Fully Convolutional Network để dự đoán Pixel Mask song song với Bbox.
  - **Segment Anything Model (SAM / SAM 2):** Promptable Segmentation Model huấn luyện trên SA-1B dataset.

### 3.4 Phân tích Video & Theo dõi Đối tượng (Video Analysis & Tracking)

- **Optical Flow:** Lucas-Kanade (dense/sparse assumption), Farneback, Deep Optical Flow (RAFT).
- **Multi-Object Tracking (MOT):**
  - **Tracking-by-Detection:** DeepSORT (Kalman Filter + Re-ID Embedding), ByteTrack (tận dụng cả low-score detection boxes để giảm văng track).

---

## 4. 🚀 GIAI ĐOẠN 4: NGHIÊN CỨU TIÊN TIẾN & THỊ GIÁC MÁY TÍNH ỨNG DỤNG (ADVANCED & EDGE CV)

### 4.1 Vision Transformers (ViT) & Multimodal Vision-Language

- **Vision Transformer (ViT):**
  - Tách ảnh $H \times W \times C$ thành các Patch $P \times P$.
  - Linear Projection thành Patch Embeddings + Learnable Class Token + Positional Encodings.
  - Áp dụng Multi-Head Self-Attention (MHSA):
    $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
- **Swin Transformer:** Hierarchical Vision Transformer sử dụng Shifted Windows để giảm độ phức tạp từ $O(N^2)$ xuống $O(N)$.
- **Vision-Language Models (VLM):**
  - **CLIP (Contrastive Language-Image Pre-training):** Đồng bộ không gian nhúng (Embedding Space) giữa Text Encoder và Image Encoder bằng Contrastive Loss.
  - **LLaVA & Grounding DINO:** Kết hợp LLM với Vision Backbone cho phép Visual Question Answering (VQA) và Open-Vocabulary Detection.

### 4.2 Thị giác Máy tính 3D & Mô hình Sinh (3D & Generative CV)

- **Mô hình Sinh (Generative Models):**
  - **GANs:** StyleGAN2/StyleGAN3 cho tổng hợp ảnh chất lượng cao.
  - **Diffusion Models:** DDPM, Latent Diffusion (Stable Diffusion), ControlNet (điều khiển cấu trúc gen qua Edge/Depth/Pose).
- **Thị giác 3D & Implicit Representations:**
  - **NeRF (Neural Radiance Fields):** Biểu diễn cảnh 3D bằng hàm liên tục $f_{\theta}(x, y, z, \theta, \phi) \rightarrow (r, g, b, \sigma)$ sử dụng MLP và Volume Rendering.
  - **3D Gaussian Splatting (3DGS):** Biểu diễn cảnh 3D bằng các hạt Gaussian 3D kỹ thuật số, cho tốc độ render thời gian thực ($> 100$ FPS).

### 4.3 Tối ưu hóa, Nén Mô hình & Triển khai (Model Deployment & Edge CV)

- **Kỹ thuật Nén Mô hình (Model Compression):**
  - **Quantization:** Chuyển đổi trọng số từ FP32 $\rightarrow$ FP16 / INT8. Post-Training Quantization (PTQ) vs Quantization-Aware Training (QAT).
  - **Pruning & Distillation:** Cắt tỉa kênh không quan trọng (Structured Pruning); Knowledge Distillation (Teacher-Student Framework).
- **Inference Engines & Hardware Acceleration:**
  - **ONNX (Open Neural Network Exchange):** Định dạng trung gian chuẩn hóa mô hình.
  - **TensorRT (NVIDIA):** Tối ưu hóa Kernel Fusion, Precision Calibration cho GPU.
  - **OpenVINO (Intel) & TFLite (Mobile/Embedded):** Triển khai lên CPU, Edge TPU, Raspberry Pi, Jetson Orin.

---

## 5. 📄 NOTION PAPER READING TRACKER

> **Ghi chú:** Khi import vào Notion, bạn có thể chuyển bảng bên dưới thành Notion Database bằng cách nhấn nút `...` góc trên bảng $\rightarrow$ `Turn into database`.

| STT | Tên Bài Báo (Paper Title)                 | Chủ đề                |   Năm   | Đóng góp chính / Innovation               | Trạng thái | Priority |
| :-: | :---------------------------------------- | :-------------------- | :-----: | :---------------------------------------- | :--------: | :------: |
|  1  | **ResNet** (_Deep Residual Learning_)     | Classification        |  2015   | Skip Connections, Residual Learning       |    Done    |   High   |
|  2  | **Faster R-CNN**                          | Object Detection      |  2015   | Region Proposal Network (RPN)             |    Done    |   High   |
|  3  | **YOLOv1** (_You Only Look Once_)         | Object Detection      |  2016   | Real-time Unified Detection               |    Done    |   High   |
|  4  | **U-Net**                                 | Segmentation          |  2015   | Encoder-Decoder + Skip Connections        |    Done    |   High   |
|  5  | **DeepLabV3+**                            | Segmentation          |  2018   | Atrous Spatial Pyramid Pooling (ASPP)     |  Reading   |  Medium  |
|  6  | **Attention Is All You Need**             | Transformer           |  2017   | Self-Attention Mechanism                  |    Done    |   High   |
|  7  | **ViT** (_An Image is Worth 16x16 Words_) | Vision Transformer    |  2020   | Pure Transformer applied to Image Patches |  Reading   |   High   |
|  8  | **Swin Transformer**                      | Vision Transformer    |  2021   | Shifted Window Self-Attention             |    Todo    |   High   |
|  9  | **CLIP**                                  | Multimodal VLM        |  2021   | Contrastive Image-Text Pre-training       |  Reading   |   High   |
| 10  | **DETR** (_End-to-End Object Detection_)  | Detection Transformer |  2020   | Bipartite Matching Loss, No NMS           |    Todo    |  Medium  |
| 11  | **Mask R-CNN**                            | Instance Seg          |  2017   | RoIAlign + Mask Branch                    |    Done    |   High   |
| 12  | **ByteTrack**                             | Multi-Object Tracking |  2022   | Low-score Detection Box Association       |    Todo    |  Medium  |
| 13  | **RAFT**                                  | Optical Flow          |  2020   | Recurrent All-Pairs Field Transforms      |    Todo    |   Low    |
| 14  | **NeRF**                                  | 3D Vision             |  2020   | Neural Radiance Fields for View Synthesis |    Todo    |   High   |
| 15  | **3D Gaussian Splatting**                 | 3D Vision             |  2023   | Real-time Radiance Field Rendering        |    Todo    |   High   |
| 16  | **DDPM** (_Denoising Diffusion_)          | Generative Model      |  2020   | Score-based Diffusion Probabilistic       |    Todo    |   High   |
| 17  | **SAM** (_Segment Anything_)              | Foundation Model      |  2023   | Promptable Segmentation at Scale          |  Reading   |   High   |
| 18  | **YOLOv8 / YOLOv11**                      | Edge Detection        | 2023-24 | Anchor-free, C2f/C3k2 Blocks, DFL         |    Done    |   High   |
| 19  | **ControlNet**                            | Generative Model      |  2023   | Adding Conditional Control to Diffusion   |    Todo    |  Medium  |
| 20  | **LLaVA**                                 | Visual Language       |  2023   | Visual Instruction Tuning with LLMs       |    Todo    |   High   |

---

## 6. 🔁 HỆ THỐNG ACTIVE RECALL & SPACED REPETITION

> **Hướng dẫn Notion:** Danh sách bên dưới sử dụng định dạng To-Do Checkbox chuẩn của Notion (`- [ ]`). Khi tick chọn, bạn đánh dấu đã ôn tập thành công!

### 🟢 Cấp độ 1: Cơ bản & Xử lý Ảnh Cổ điển

- [ ] **Q1: Kích thước output của ảnh $224 \times 224 \times 3$ qua Conv Layer với Kernel $7 \times 7$, Stride $2$, Padding $3$ là bao nhiêu?**

  > **Lời giải:**  
  > Áp dụng công thức: $W_{out} = \lfloor \frac{W - F + 2P}{S} \rfloor + 1$  
  > $$W_{out} = \left\lfloor \frac{224 - 7 + 2(3)}{2} \right\rfloor + 1 = \left\lfloor \frac{223}{2} \right\rfloor + 1 = 111 + 1 = 112$$  
  > Kích thước không gian đầu ra là **$112 \times 112$**.

- [ ] **Q2: Sự khác biệt cốt lõi giữa Lọc Median (Median Filter) và Lọc Gaussian (Gaussian Blur) là gì?**

  > **Lời giải:**
  >
  > - **Gaussian Blur:** Là lọc tuyến tính (Linear Filter), tính trung bình có trọng số theo phân phối Gaussian. Làm mịn toàn bộ ảnh nhưng làm mờ biên (edges) và không loại bỏ tốt nhiễu muối tiêu (Salt-and-Pepper).
  > - **Median Filter:** Là lọc phi tuyến (Non-linear Filter), thay thế pixel trung tâm bằng giá trị trung vị trong cửa sổ. Cực kỳ hiệu quả trong việc **loại bỏ nhiễu muối tiêu** mà vẫn **giữ nguyên độ sắc nét của biên**.

- [ ] **Q3: Tại sao SIFT lại bất biến với phép nhân tỷ lệ (Scale Invariant)?**
  > **Lời giải:**  
  > SIFT sử dụng **Scale Space** được tạo bởi hàm Difference of Gaussians (DoG) ở nhiều mức tỷ lệ (octaves) khác nhau. Các điểm đặc trưng (Keypoints) được xác định tại cực trị không gian 3D $(x, y, \sigma)$, đảm bảo dù ảnh bị phóng to hay thu nhỏ, điểm đặc trưng vẫn được phát hiện ở scale $\sigma$ tương ứng.

---

### 🟡 Cấp độ 2: CNN & Deep Learning Core

- [ ] **Q4: Vấn đề Vanishing Gradient là gì và ResNet giải quyết nó bằng cách nào?**

  > **Lời giải:**
  >
  > - **Vấn đề:** Khi mạng quá sâu, đạo hàm lan truyền ngược (Backpropagation) qua nhiều tầng nhân với trọng số $< 1$ sẽ tiệm cận về 0, khiến các tầng đầu không thể cập nhật trọng số.
  > - **ResNet Giải quyết:** Sử dụng **Residual Block** với đường truyền tắt (Skip Connection): $y = F(x) + x$.  
  >   Khi tính đạo hàm: $\frac{\partial y}{\partial x} = \frac{\partial F(x)}{\partial x} + 1$.  
  >   Nhờ có hằng số $+ 1$, Gradient luôn có thể lan truyền ngược trực tiếp về các tầng trước đó mà không bị triệt tiêu về 0.

- [ ] **Q5: Tại sao Depthwise Separable Convolution trong MobileNet lại tiết kiệm phép tính hơn Standard Convolution?**

  > **Lời giải:**  
  > Cho Feature map $H \times W \times D_{in}$, Kernel $D_k \times D_k$, số kênh ra $D_{out}$:
  >
  > - **Standard Conv:** $H \times W \times D_{in} \times D_{out} \times D_k \times D_k$ phép tính.
  > - **Depthwise Separable Conv:**
  >   1. _Depthwise Conv_ (Lọc từng kênh riêng lẻ): $H \times W \times D_{in} \times D_k \times D_k$
  >   2. _Pointwise Conv_ ($1 \times 1$ Conv kết hợp kênh): $H \times W \times D_{in} \times D_{out}$
  > - **Tỷ lệ giảm chi phí tính toán:**  
  >   $$\frac{\text{Depthwise Separable}}{\text{Standard}} = \frac{1}{D_{out}} + \frac{1}{D_k^2} \approx \frac{1}{9} \quad (\text{với } D_k=3)$$

- [ ] **Q6: Phân biệt Anchor-based và Anchor-free trong Object Detection?**
  > **Lời giải:**
  >
  > - **Anchor-based (ví dụ: Faster R-CNN, YOLOv3/v4):** Định nghĩa sẵn các hộp khung mẫu (Anchor Boxes) cố định về tỷ lệ và kích thước tại mỗi vị trí grid. Mô hình học cách dự đoán độ lệch (offset $\Delta x, \Delta y, \Delta w, \Delta h$) so với anchor.
  > - **Anchor-free (ví dụ: FCOS, CenterNet, YOLOv8):** Dự đoán trực tiếp tọa độ tâm đối tượng (Center point) hoặc khoảng cách từ điểm tâm đến 4 cạnh Bounding box ($l, r, t, b$). Loại bỏ hoàn toàn việc tuning hyperparameter cho Anchor Boxes.

---

### 🔴 Cấp độ 3: Advanced, ViT & Optimization

- [ ] **Q7: Độ phức tạp tính toán của Self-Attention trong Vision Transformer (ViT) theo số lượng Patch là gì và Swin Transformer giải quyết nó ra sao?**

  > **Lời giải:**
  >
  > - **Standard ViT:** Độ phức tạp tính toán của Full Self-Attention là $O(N^2)$ với $N$ là số lượng Patch. Khi độ phân giải ảnh tăng, $N$ tăng quadratically khiến chi phí bộ nhớ bùng nổ.
  > - **Swin Transformer:** Áp dụng **Shifted Window Self-Attention (W-MSA / SW-MSA)**. Chỉ tính toán Attention bên trong các cửa sổ local kích thước cố định $M \times M$. Độ phức tạp giảm xuống tuyến tính $O(M^2 \cdot N)$, cho phép xử lý ảnh độ phân giải lớn.

- [ ] **Q8: Post-Training Quantization (PTQ) khác gì so với Quantization-Aware Training (QAT)?**
  > **Lời giải:**
  >
  > - **PTQ (Quantization sau huấn luyện):** Chuyển đổi mô hình đã train (FP32) sang INT8 mà không cần huấn luyện lại. Nhanh chóng nhưng dễ làm giảm độ chính xác (accuracy drop), đặc biệt với các mô hình nhỏ.
  > - **QAT (Huấn luyện nhận biết định lượng):** Mô phỏng sai số định lượng (Fake Quantization) ngay trong quá trình Training/Fine-tuning. Cho phép mạng tự điều chỉnh trọng số thích nghi với định dạng INT8, giữ nguyên độ chính xác ban đầu.

---

## 7. 💻 CODE SNIPPET VAULT & PYTORCH TEMPLATES

### Template 1: Custom PyTorch Dataset & Pipeline chuẩn cho Computer Vision

```python
import os
import cv2
import torch
from torch.utils.data import Dataset, DataLoader
import albumentations as A
from albumentations.pytorch import ToTensorV2

class CVDataset(Dataset):
    # Custom Dataset Template cho Object Classification / Detection sử dụng Albumentations
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

        # Đọc ảnh OpenCV (BGR -> RGB)
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        label = self.labels[img_name]

        # Áp dụng Augmentation
        if self.transform:
            augmented = self.transform(image=image)
            image = augmented['image']

        return image, torch.tensor(label, dtype=torch.long)

# Augmentation Pipeline chuẩn
train_transform = A.Compose([
    A.Resize(height=224, width=224),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ToTensorV2(),
])
```

---

### Template 2: PyTorch Modern Training Loop với Mixed Precision & Checkpoint

```python
import torch
import torch.nn as nn
from torch.cuda.amp import autocast, GradScaler

def train_one_epoch(model, dataloader, criterion, optimizer, scaler, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, targets in dataloader:
        images, targets = images.to(device), targets.to(device)
        optimizer.zero_grad()

        # Automatic Mixed Precision (AMP) nâng cao tốc độ train GPU
        with autocast():
            outputs = model(images)
            loss = criterion(outputs, targets)

        # Backward bằng GradScaler
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()

        running_loss += loss.item() * images.size(0)
        _, preds = outputs.max(1)
        total += targets.size(0)
        correct += preds.eq(targets).sum().item()

    epoch_loss = running_loss / total
    epoch_acc = correct / total
    return epoch_loss, epoch_acc
```

---

### Template 3: Xuất mô hình PyTorch sang ONNX & Kiểm tra Inference

```python
import torch

def export_to_onnx(model, save_path="model.onnx", input_shape=(1, 3, 224, 224)):
    model.eval()
    dummy_input = torch.randn(*input_shape, device='cpu')

    torch.onnx.export(
        model,
        dummy_input,
        save_path,
        export_params=True,
        opset_version=14,
        do_constant_folding=True,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
    )
    print(f"Exported ONNX successfully to {save_path}")

# Kiểm tra Inference bằng ONNX Runtime
import onnxruntime as ort
import numpy as np

def run_onnx_inference(onnx_path, dummy_array):
    session = ort.InferenceSession(onnx_path, providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    input_name = session.get_inputs()[0].name
    outputs = session.run(None, {input_name: dummy_array})
    return outputs
```

---

## 8. 🛠️ DANH MỤC DỰ ÁN THỰC CHIẾN (CAPSTONE PROJECTS PORTFOLIO)

### 📌 Project 1: Real-time Traffic Surveillance & Vehicle Analytics System

- **Bài toán:** Phát hiện, đếm và theo dõi phương tiện giao thông (ô tô, xe máy, xe tải) từ Video Camera đường phố, tính toán tốc độ ước lượng.
- **Công nghệ:** YOLOv8/v11 + ByteTrack + OpenCV + PyTorch.
- **Đầu ra Portfolio:** Codebase Github + Video demo vẽ BBox, Track ID, Speed vector + Dashboard thống kê lưu lượng.

### 📌 Project 2: Automated Medical Image Segmentation (Brain Tumor / Lung Lesion)

- **Bài toán:** Phân vùng chính xác khối u/vùng tổn thương từ ảnh MRI/CT scan y tế.
- **Công nghệ:** 3D/2D U-Net, DeepLabV3+, Dice Loss, MONAI Framework.
- **Đầu ra Portfolio:** Jupyter Notebook phân tích chi tiết Dice Score ($> 0.88$), Visualization so sánh Ground Truth mask vs Predicted mask.

### 📌 Project 3: Edge-AI Driver Drowsiness & Pose Alert System

- **Bài toán:** Nhận diện trạng thái buồn ngủ/mất tập trung của tài xế thời gian thực qua WebCam.
- **Công nghệ:** MediaPipe / RTMPose (Keypoint Detection) + PERCLOS Metric + ONNX Runtime triển khai lên Raspberry Pi / Jetson Orin.
- **Đầu ra Portfolio:** Ứng dụng chạy mượt $> 30$ FPS trên thiết bị nhúng với cảnh báo âm thanh.

### 📌 Project 4: Enterprise Open-Vocabulary Product Retrieval & Search

- **Bài toán:** Tìm kiếm sản phẩm trong kho thương mại điện tử bằng hình ảnh hoặc câu lệnh ngôn ngữ tự nhiên (Text-to-Image Search).
- **Công nghệ:** CLIP Vision Encoder + Qdrant / Milvus Vector Database + FastAPIs.
- **Đầu ra Portfolio:** Hệ thống Web API cho phép truy vấn chuỗi "áo sơ mi nam kẻ caro màu xanh" trả về danh sách ảnh tương quan cao nhất.

---

> **💡 Lời khuyên cuối:** Hãy Import file `.md` này trực tiếp vào **Notion Workspace** của bạn. Bạn có thể sử dụng các tính năng Native của Notion như To-Do Checkbox và Database Table để quản lý tiến độ hiệu quả nhất!
