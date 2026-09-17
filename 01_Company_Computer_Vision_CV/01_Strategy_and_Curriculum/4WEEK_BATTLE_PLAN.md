# ⚡ KẾ HOẠCH TÁC CHIẾN 4 TUẦN: CÔNG TY THỊ GIÁC MÁY TÍNH (VISIONLAB DEEP TECH)
## 4-Week Tactical Execution Plan — Computer Vision (CV)

> **Mã Doanh Nghiệp:** `CORP-01-CV`  
> **Cố vấn chuyên môn:** Giám Đốc Nghiên Cứu CV (`PSD-04`)  
> **Người thực thi:** Kỹ Sư Trưởng Handmade (`HM-00` / Bạn)

---

## 🎯 MỤC TIÊU THÁNG 1
Làm chủ hoàn toàn Giai đoạn 1 (Toán Tensor, SVD nén ảnh, Bộ lọc Canny from-scratch) và Giai đoạn 2 (SIFT + Homography ghép ảnh Panorama); dựng khung huấn luyện PyTorch 2.x chuẩn trên GPU RTX 3050.

---

## 📅 LỘ TRÌNH CHI TIẾT TỪNG TUẦN

### Tuần 1: Đại Số Tuyến Tính Tensor & Phép Tích Chập 2D From-Scratch
- **Lý thuyết**: Ma trận tensor không gian ($H \times W \times C$), SVD nén ảnh ($\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$), bản chất phép tích chập không gian (Cross-correlation vs Convolution).
- **Thực hành (Lab)**:
  - Tự viết hàm `convolve2d(image, kernel, stride=1, padding=0)` bằng Numpy (không dùng thư viện ngoài).
  - Thử nghiệm các ma trận kernel cổ điển: Kernel làm nét (Sharpen), Kernel làm mờ (Box Blur), Kernel phát hiện biên (Laplacian).
- **Sản phẩm bàn giao**: Notebook `03_Engineering_Labs_and_Code/W1_Tensor_Convolution_from_Scratch.ipynb`.
- **KPI nghiệm thu**: Hàm tích chập tự viết cho ra kết quả khớp 100% với `scipy.signal.convolve2d`.

---

### Tuần 2: Bộ Lọc Không Gian & Canny Edge Detector Hoàn Chỉnh
- **Lý thuyết**: Bộ lọc Gauss 2D ($G(x,y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2+y^2}{2\sigma^2}}$), Miền tần số 2D Fourier (High-pass/Low-pass), Thuật toán Canny 4 bước.
- **Thực hành (Lab)**:
  - Tự code trọn vẹn 4 bước của Canny Edge Detector:
    1. Làm mịn bằng Gaussian Filter.
    2. Tính Gradient độ lớn và góc pha ($M(x,y), \theta(x,y)$) bằng toán tử Sobel.
    3. Triệt tiêu các điểm không phải cực đại (Non-Maximum Suppression - NMS theo 4 hướng $0^\circ, 45^\circ, 90^\circ, 135^\circ$).
    4. Lọc ngưỡng kép và theo vết cạnh (Hysteresis Thresholding).
- **Sản phẩm bàn giao**: File script `canny_edge_custom.py` có comment chi tiết từng dòng.
- **KPI nghiệm thu**: Ảnh biên cạnh trích xuất được sạch nét, không dính đứt gãy.

---

### Tuần 3: Trích Xuất Đặc Trưng Cục Bộ & Ghép Ảnh Panorama
- **Lý thuyết**: Điểm đặc trưng bất biến tỉ lệ (Scale-Invariant Features), Ma trận tự tương quan Harris Corner, Thuật toán SIFT/ORB, Biến đổi Homography và thuật toán RANSAC loại bỏ ngoại lai (outliers).
- **Thực hành (Lab)**:
  - Dùng OpenCV trích xuất keypoints và descriptors bằng SIFT/ORB trên 2 bức ảnh chụp phong cảnh lệch góc.
  - Dùng BFMatcher / FlannBasedMatcher để tìm cặp điểm tương đồng.
  - Ước lượng ma trận Homography $3 \times 3$ bằng RANSAC $\rightarrow$ Warp perspective ảnh $\rightarrow$ Ghép nối thành 1 bức ảnh Panorama rộng.
- **Sản phẩm bàn giao**: Notebook `03_Engineering_Labs_and_Code/W3_Image_Stitching_Panorama.ipynb`.
- **KPI nghiệm thu**: Ghép thành công 2 bức ảnh không bị méo lệch góc nhìn.

---

### Tuần 4: Khởi Dựng Pipeline PyTorch 2.x & Huấn Luyện CNN Trên GPU
- **Lý thuyết**: Kiến trúc CNN kinh điển (AlexNet, VGG, ResNet), Receptive Field, Hàm mất mát Cross-Entropy và Focal Loss cho dữ liệu mất cân bằng.
- **Thực hành (Lab)**:
  - Dựng cấu trúc thư viện chuẩn cho dự án Vision:
    - `dataset.py`: Kế thừa `torch.utils.data.Dataset`, tích hợp Albumentations augmentation.
    - `model.py`: Xây dựng Custom CNN hoặc load pre-trained ResNet-18 từ `torchvision.models`.
    - `train.py`: Vòng lặp training loop với `torch.cuda.amp.autocast()` (Mixed Precision) tăng tốc trên RTX 3050.
- **Sản phẩm bàn giao**: Thư mục mã nguồn `03_Engineering_Labs_and_Code/PyTorch_Vision_Boilerplate/`.
- **KPI nghiệm thu**: Huấn luyện thành công mô hình phân loại ảnh đạt Accuracy $\ge 85\%$ trên tập test; sử dụng dưới 3GB VRAM.
