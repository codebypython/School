# 📊 PROJECT STATUS DASHBOARD — VisionLab Corp (CORP-01-CV)

> **Cập nhật lần cuối**: 2026-09-13 | **Tuần hiện tại**: Tuần 1 (Foundations & Image Processing)  
> **Mentor chuyên trách**: DUT Computer Vision Mentor (`AGENT_PROFILE.md`)

---

## Current Phase: 🔵 PHASE 1 — FOUNDATIONS & SPATIAL FILTERING (Tuần 1-4)

Tập trung vào nền tảng toán học giải tích ảnh, lọc không gian và trích xuất đặc trưng hình học cục bộ.

---

## Implementation & Lab Progress

### Module 1: Xử lý Ảnh Cơ Bản & Lọc Không Gian
- [x] Thiết lập môi trường OpenCV + PyTorch (GPU CUDA)
- [x] Không gian màu RGB, HSV, Grayscale & Histogram Equalization
- [ ] Lọc tuyến tính: Gaussian Blur, Sobel Edge Filter, Box Filter
- [ ] Lọc phi tuyến: Median Filter, Bilateral Filter khử nhiễu giữ cạnh
- [ ] Canny Edge Detector: Non-maximum suppression & Hysteresis Thresholding

### Module 2: Trích Xuất Đặc Trưng & Hình Học
- [ ] Harris Corner Detector
- [ ] SIFT / ORB Feature Matching
- [ ] RANSAC cho Homography Estimation & Image Stitching (Panorama)

### Module 3: Deep Learning & CNN Backbones
- [ ] Xây dựng Custom CNN từ đầu trên PyTorch
- [ ] Fine-tuning ResNet-50 / MobileNetV3 với Transfer Learning

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | Chưa hoàn tất dataset bài tập lọc ảnh tuần 2 | 🟡 Medium | Cần chuẩn bị folder `data/` mẫu |

---

## Next Priority (P0)
- **Chuẩn hóa Triển khai Dự án qua Jupyter Notebook (`.ipynb`)**: Mọi tính toán kỹ thuật, tiền xử lý và mô hình hóa đều được thực thi trực tiếp, xuất các sơ đồ/biểu đồ kết quả nhúng thẳng vào cell outputs.
- **Tập tin Master Hoàn Tất**: [`03_Engineering_Labs_and_Code/01_RSNA_Bone_Age_End_to_End_Pipeline.ipynb`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/01_RSNA_Bone_Age_End_to_End_Pipeline.ipynb) (23 cells, 10 sơ đồ trực quan thực tế).

