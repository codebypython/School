# 📊 PROJECT STATUS DASHBOARD — VisionLab Corp (CORP-01-CV)

> **Cập nhật lần cuối**: 2026-09-25 | **Giai đoạn**: Triển khai Siêu Kế Hoạch Đa Phương Thức RSNA Bone Age  
> **Dự án Chuẩn Tham Chiếu**: `MECHANICAL_FAULT_XRAY Project` (Báo cáo 86 trang, Slide 43 trang, Đối đầu 3 mô hình)  
> **Mentor chuyên trách**: DUT Computer Vision Mentor (`AGENT_PROFILE.md`)  
> **Mô hình Vận hành**: **Kaggle Modular 3-Notebooks** $\longleftrightarrow$ **Local Workstation (Strategic HQ & WebApp)**

---

## 🏛️ Sứ Mệnh & Phân Tầng Trách Nhiệm

| Phân Vùng | Trọng Tâm Nhiệm Vụ | Hiện Trạng & Tài Sản Quản Lý |
|:---|:---|:---|
| ☁️ **Kaggle Cloud Compute** | - **NB01**: Data Audit & Preprocessing Cache (512x512, Otsu+CLAHE, Fixed Split CSV)<br>- **NB02**: Tri-Model Training Matrix (ResNet-50 vs ConvNeXt/EffNet vs Swin-T) với Auto-Resume Checkpoint<br>- **NB03**: Benchmark Evaluation, Statistical Error Analysis, XAI Grad-CAM & Inference | - Đã cấu hình Kaggle CLI 2.2.4 & token<br>- Đã hoàn thành huấn luyện thực tế ResNet-50 (`result_tranning.ipynb`, MAE=7.38m)<br>- Thư mục `kaggle_modular_notebooks/` gồm 3 notebook độc lập |
| 💻 **Local Workstation (HQ)** | - Quản trị Báo cáo Kỹ thuật Chuyên sâu 86 trang (`master_project_report_80_pages.md`)<br>- Quản trị Bộ Slide 43 trang chuẩn Canva (`slide_content_43_pages.md`)<br>- Lưu trữ trọng số (`best_model.pth`), metrics log (`training_history.csv`)<br>- Vận hành Ứng dụng Chẩn đoán Lâm sàng Offline (`clinical_webapp/app.py`) | - Báo cáo đồ án cấu trúc theo `MECHANICAL_FAULT_XRAY`<br>- Bộ kịch bản 43 slide phân công 2 sinh viên thuyết trình<br>- Folder `experiment_results/` & `clinical_webapp/` |

---

## 📈 Ma Trận Thực Nghiệm Đối Đầu (Tri-Model Benchmark Matrix)

| ID | Mô Hình | Trường Phái Kiến Trúc | Tiền Xử Lý Ảnh | Nhánh Lâm Sàng | Hàm Loss | Epochs | Test MAE (tháng) | Test RMSE (tháng) | $R^2$ Score | Tỷ lệ $\le 12$m | Trạng Thái |
|:---:|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **M1** | **ResNet-50** | Residual Bottleneck CNN | CLAHE + Otsu Crop (512x512) | MLP 32D | Huber Loss ($\delta=1.0$) | 15 | **7.38m** (~0.62y) | **9.60m** | **0.9452** | **81.38%** | ✅ Hoàn thành (`result_tranning.ipynb`) |
| **M2** | **ConvNeXt-V2** | Modern Pure CNN (Depthwise 7x7) | CLAHE + Otsu Crop (512x512) | MLP 32D | Huber Loss ($\delta=1.0$) | 20 | *Sẵn sàng NB02* | -- | -- | -- | 🟡 Thiết kế hoàn tất trong NB02 |
| **M3** | **Swin-T (v2)** | Hierarchical Vision Transformer | CLAHE + Otsu Crop (512x512) | MLP 32D | Huber Loss ($\delta=1.0$) | 20 | *Sẵn sàng NB02* | -- | -- | -- | 🟡 Thiết kế hoàn tất trong NB02 |

---

## 🎯 Tiến Độ Thực Hiện & Ưu Tiên Tiếp Theo (P0)

1. ✅ **Giai Đoạn 1 (Notebook 01 - Hoàn Thành Xuất Sắc 100%)**:
   - Chạy trên Kaggle: 12.611 / 12.611 ảnh thật tiền xử lý thành công trong **5.86 phút**.
   - Phiên chạy commit `successful (391.1s)`.
   - Đã xuất `train_stratified.csv` và thư mục ảnh sạch $512 \times 512$ làm cache cố định.
2. 🚀 **Giai Đoạn 2 (Notebook 02 - Sẵn Sàng Triển Khai)**:
   - Nạp `02_Multimodal_Model_Training_Matrix.ipynb` lên Kaggle.
   - Gắn Output của Notebook 01 (`train CV`) qua tab **Notebooks** làm Input.
   - Bật GPU T4 x2 / P100 và khởi động huấn luyện mô hình thế trận Tam Mã.
3. 📊 **Giai Đoạn 3 (Notebook 03) & Giai Đoạn 4 (Báo Cáo / Slide)**:
   - Sẵn sàng đón nhận metrics và trọng số để hoàn thiện bộ 43 slide và báo cáo 80 trang.
