# 🗺️ CẨM NANG ĐIỀU PHỐI TÁC CHIẾN: LIÊN KẾT THỰC NGHIỆM ➔ BÁO CÁO ➔ SLIDE
## EXPERIMENT-TO-REPORT & SLIDE MASTER INTEGRATION PLAYBOOK
> **Mã quy trình:** `SOP-CORP01-CV-INTEGRATION-2026`  
> **Áp dụng cho:** Toàn bộ kỹ sư và sinh viên vận hành đề tài RSNA Pediatric Bone Age Assessment  
> **Dự án chuẩn tham chiếu:** `MECHANICAL_FAULT_XRAY Project`

---

## 🎯 NGUYÊN TẮC VẬN HÀNH "THỰC NGHIỆM ĐẾN ĐÂU, ĐÓNG ĐINH ĐẾN ĐÓ"

Khi bạn chạy thủ công các tệp Notebook trên **Kaggle** hoặc **Google Colab**, mỗi giai đoạn thực nghiệm sẽ kết xuất ra các tệp biểu đồ (`.png`), tệp số liệu (`.csv`), và tệp trọng số (`.pth`). 

Quy trình này hướng dẫn bạn chính xác: **File nào vừa tải về $	o$ Cất vào thư mục nào $	o$ Cập nhật vào Chương mấy của Báo cáo $	o$ Chiếu lên Slide số mấy.**

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   LUỒNG ĐỒNG BỘ DỮ LIỆU TỰ ĐỘNG (WORKFLOW OVERVIEW)                    │
├──────────────────────────────┬─────────────────────────────┬───────────────────────────┤
│ ☁️ TẠI MÔI TRƯỜNG KAGGLE/COLAB│ 📁 THƯ MỤC DROPBOX LOCAL    │ 📄 TÀI LIỆU ĐÍCH CẬP NHẬT │
├──────────────────────────────┼─────────────────────────────┼───────────────────────────┤
│ Chạy Notebook 01             │ experiment_results/         │ • Báo Cáo: Chương 2       │
│ -> Sinh ảnh EDA & 5 bước CV  │   01_eda_and_preprocessing/ │ • Slide: Slide 10, 14     │
├──────────────────────────────┼─────────────────────────────┼───────────────────────────┤
│ Chạy Notebook 02             │ experiment_results/         │ • Báo Cáo: Chương 3       │
│ -> Sinh đồ thị Loss/MAE M1-M3│   02_model_checkpoints_.../ │ • Slide: Slide 20, 26, 32 │
├──────────────────────────────┼─────────────────────────────┼───────────────────────────┤
│ Chạy Notebook 03             │ experiment_results/         │ • Báo Cáo: Chương 3       │
│ -> Sinh Bảng Ma Trận & XAI   │   03_benchmark_and_xai/     │ • Slide: Slide 36, 38, 39 │
└──────────────────────────────┴─────────────────────────────┴───────────────────────────┘
```

---

## 📊 BẢNG TRA CỨU ĐIỀU HƯỚNG TỪNG TỆP THỰC NGHIỆM (MASTER MAPPING TABLE)

| STT | Tên Tệp Sinh Ra Từ Notebook | Thư Mục Cất Trữ Tại Local | Vị Trí Tương Ứng Trong Báo Cáo (`master_project_report_80_pages.md`) | Vị Trí Tương Ứng Trên Slide (`slide_content_43_pages.md`) | Tác Vụ Cần Làm |
|:---:|:---|:---|:---|:---|:---|
| **1** | `eda_distribution_plots.png` (4 đồ thị phân phối tuổi, giới tính) | `experiment_results/01_eda_and_preprocessing/` | **Chương 2, Mục 2.2** (Hình 2.1: Phân tích mô tả tập dữ liệu lâm sàng RSNA) | **Slide 10** (Card: Phân tích thống kê lâm sàng EDA) | Chèn ảnh vào slide và báo cáo để chứng minh dữ liệu cân bằng. |
| **2** | `classical_cv_5steps_demo.png` (Dải 5 ảnh đối chiếu tiền xử lý) | `experiment_results/01_eda_and_preprocessing/` | **Chương 2, Mục 2.3** (Hình 2.2: Quy trình 5 bước tiền xử lý ảnh X-quang) | **Slide 14** (Card: Pipeline chuẩn hóa thị giác cổ điển) | Dùng để bảo vệ phương pháp làm sạch viền và xóa chữ L/R. |
| **3** | `train_stratified.csv` (File phân tầng 80/10/10 cố định) | `experiment_results/01_eda_and_preprocessing/` | **Chương 2, Mục 2.2** (Bảng phân bổ mẫu Train/Val/Test) | **Slide 11 & 12** (Bảng cơ cấu mẫu theo 4 lứa tuổi) | Đóng băng tập dữ liệu cho cả 3 mô hình. |
| **4** | `resnet50_learning_curves.png` (Đồ thị Loss/MAE ResNet-50) | `experiment_results/02_model_checkpoints_and_curves/M1_ResNet50/` | **Chương 3, Mục 3.1.1** (Hình 3.1: Động học suy giảm hàm mất mát ResNet-50) | **Slide 20** (Đồ thị động học huấn luyện ResNet-50) | Chứng minh mô hình hội tụ tốt sau 15 epochs. |
| **5** | `resnet50_training_history.csv` | `experiment_results/02_model_checkpoints_and_curves/M1_ResNet50/` | **Chương 3, Mục 3.1.1** (Bảng 3.1: Bảng theo dõi tiến trình 15 Epochs) | Dữ liệu đối chiếu nội bộ | Trích xuất các mốc Val MAE: Ep 1 (111m), Ep 5 (12.7m), Ep 13 (7.25m). |
| **6** | `resnet50_checkpoint_best.pth` (~98MB) | `experiment_results/02_model_checkpoints_and_curves/M1_ResNet50/` | **Chương 3, Mục 3.1.2** | Nạp vào WebApp Demo (`clinical_webapp/app.py`) | Copy sang `clinical_webapp/` để chạy demo chẩn đoán trực tiếp. |
| **7** | `convnext_tiny_learning_curves.png` | `experiment_results/02_model_checkpoints_and_curves/M2_ConvNeXt/` | **Chương 3, Mục 3.2.1** (Hình 3.3: Động học hội tụ ConvNeXt-Tiny) | **Slide 26** (Đồ thị hội tụ của ConvNeXt-Tiny) | Chứng minh tích chập hiện đại hội tụ sâu hơn ResNet-50. |
| **8** | `swin_t_learning_curves.png` | `experiment_results/02_model_checkpoints_and_curves/M3_SwinT/` | **Chương 3, Mục 3.3.1** (Hình 3.5: Động học hội tụ Swin-T) | **Slide 32** (Đồ thị hội tụ của Swin-T) | Chứng minh Vision Transformer đạt MAE tối ưu kỷ lục. |
| **9** | `tri_model_benchmark_table.csv` (Bảng so sánh 3 mô hình) | `experiment_results/03_benchmark_and_xai/` | **Chương 3, Mục 3.4** (Bảng 3.4: Ma trận so sánh đối đầu toàn diện) | **Slide 36** (Bảng ma trận đối đầu toàn diện 3 mô hình) | **SLIDE ĐINH CỦA ĐỒ ÁN**: So sánh MAE, RMSE, R², FPS, Kích thước file. |
| **10**| `test_scatter_and_residuals.png` (Scatter $y$ vs $\hat{y}$ & phần dư) | `experiment_results/03_benchmark_and_xai/` | **Chương 3, Mục 3.5** (Hình 3.7 & 3.8: Biểu đồ phân tán và phân phối phần dư) | **Slide 22, 28, 34** (Tương ứng từng mô hình) | Minh chứng các điểm nằm trong hành lang an toàn $\pm 1$ năm. |
| **11**| `mae_by_age_groups.png` (Sai số theo 4 nhóm lứa tuổi) | `experiment_results/03_benchmark_and_xai/` | **Chương 3, Mục 3.5** (Hình 3.9: Sai số MAE theo nhóm tuổi) | Dữ liệu trả lời phản biện hội đồng | Trả lời câu hỏi: Mô hình đoán tốt nhất ở tuổi nào? |
| **12**| `gradcam_hand_overlay.png` (Ảnh gốc + Heatmap + Lớp phủ) | `experiment_results/03_benchmark_and_xai/` | **Chương 3, Mục 3.6** (Hình 3.10: Kiểm chứng giải phẫu học XAI) | **Slide 38 & 39** (Kiểm chứng giải phẫu học trên phim X-ray thật) | Bác bỏ định kiến hộp đen, chứng minh AI nhìn vào cổ tay & sụn. |
| **13**| `clinical_report_sample.txt` (Phiếu chẩn đoán mẫu) | `experiment_results/03_benchmark_and_xai/` | **Chương 3, Mục 3.7** (Phiếu chẩn đoán mẫu) | **Slide 40 & 41** (Demo WebApp lâm sàng & cảnh báo WHO) | Trực quan hóa kết quả chẩn đoán lâm sàng tự động. |

---

## 🛠️ HƯỚNG DẪN CHI TIẾT THEO TỪNG GIAI ĐOẠN THỰC THI THỦ CÔNG

### GIAI ĐOẠN 1: Chạy `01_Data_Audit_Classical_Preprocessing_Cache.ipynb`
1. Đẩy notebook lên **Kaggle** (hoặc Google Colab).
2. Nhấn **Save Version $	o$ Save & Run All (Commit)**.
3. Khi chạy xong, tải về máy 3 tệp:
   - `eda_distribution_plots.png`
   - `classical_cv_5steps_demo.png`
   - `train_stratified.csv`
4. Cất vào thư mục: `03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research Project/experiment_results/01_eda_and_preprocessing/`.
5. Mở Canva hoặc PowerPoint, chèn 2 ảnh biểu đồ vào **Slide 10** và **Slide 14**.

### GIAI ĐOẠN 2: Chạy `02_Multimodal_Model_Training_Matrix.ipynb`
1. **Lần 1 (Huấn luyện M1: ResNet-50):**
   - Đặt `ACTIVE_BACKBONE = "resnet50"` và chạy.
   - Tải về: `resnet50_checkpoint_best.pth`, `resnet50_training_history.csv`, `resnet50_learning_curves.png`.
   - Cất vào: `experiment_results/02_model_checkpoints_and_curves/M1_ResNet50/`.
   - Cập nhật số liệu vào **Slide 20, 21** và **Chương 3, Mục 3.1**.
2. **Lần 2 (Huấn luyện M2: ConvNeXt-Tiny):**
   - Đặt `ACTIVE_BACKBONE = "convnext_tiny"` và chạy.
   - Tải về: `convnext_tiny_checkpoint_best.pth`, `convnext_tiny_training_history.csv`, `convnext_tiny_learning_curves.png`.
   - Cất vào: `experiment_results/02_model_checkpoints_and_curves/M2_ConvNeXt/`.
   - Cập nhật số liệu vào **Slide 26, 27** và **Chương 3, Mục 3.2**.
3. **Lần 3 (Huấn luyện M3: Swin-T v2):**
   - Đặt `ACTIVE_BACKBONE = "swin_t"` và chạy.
   - Tải về: `swin_t_checkpoint_best.pth`, `swin_t_training_history.csv`, `swin_t_learning_curves.png`.
   - Cất vào: `experiment_results/02_model_checkpoints_and_curves/M3_SwinT/`.
   - Cập nhật số liệu vào **Slide 32, 33** và **Chương 3, Mục 3.3**.

### GIAI ĐOẠN 3: Chạy `03_Benchmark_Evaluation_XAI_and_Inference.ipynb`
1. Chạy notebook để tự động đánh giá cả 3 checkpoint trên 1.262 ca Test.
2. Tải về:
   - `tri_model_benchmark_table.csv`
   - `test_scatter_and_residuals.png`
   - `mae_by_age_groups.png`
   - `gradcam_hand_overlay.png`
3. Cất vào: `experiment_results/03_benchmark_and_xai/`.
4. Cập nhật Bảng ma trận vào **Slide 36** và chèn ảnh Grad-CAM vào **Slide 38 & 39**.
5. Cập nhật các bảng số liệu tương ứng trong **Chương 3, Mục 3.4, 3.5, 3.6** của Báo cáo.

---

## 🏥 GIAI ĐOẠN 4: KHỞI CHẠY WEBAPP DEMO BẢO VỆ ĐỒ ÁN
1. Copy file `resnet50_checkpoint_best.pth` (hoặc trọng số tốt nhất) vào thư mục `experiment_results/best_model.pth`.
2. Mở Terminal trên máy Local:
   ```bash
   cd "01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research Project/clinical_webapp"
   pip install streamlit matplotlib pillow numpy
   streamlit run app.py
   ```
3. Giao diện WebApp sẽ tự động mở trên trình duyệt tại `http://localhost:8501`, sẵn sàng để bạn thao tác trực tiếp trước Hội đồng!
