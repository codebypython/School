# 📥 DROPBOX 03: ĐỐI ĐẦU 3 MÔ HÌNH & XAI GRAD-CAM (TỪ NOTEBOOK 03)
> **Mã nguồn phát sinh:** `03_Benchmark_Evaluation_XAI_and_Inference.ipynb`  
> **Bộ phận thụ hưởng:** Phòng Tư Liệu Học Thuật & Phòng Chiến Lược

### 📋 Danh mục File thả vào đây:
1. `tri_model_benchmark_table.csv`: Bảng tổng kết đối đầu đa tiêu chí của cả 3 mô hình trên 1.262 ca Test.
   - 👉 **Áp dụng vào Báo cáo:** Chương 3, Mục 3.4 (Bảng 3.4: Ma trận so sánh đối đầu).
   - 👉 **Áp dụng vào Slide:** Slide 36 (Bảng ma trận đối đầu toàn diện 3 mô hình).
2. `test_scatter_and_residuals.png`: Biểu đồ Scatter Plot (Tuổi thật vs Dự đoán) và biểu đồ phân phối phần dư sai số (Residual Distribution).
   - 👉 **Áp dụng vào Báo cáo:** Chương 3, Mục 3.5 (Hình 3.7 & 3.8).
   - 👉 **Áp dụng vào Slide:** Slide 22, Slide 28, Slide 34.
3. `mae_by_age_groups.png`: Biểu đồ cột sai số MAE theo 4 nhóm lứa tuổi sinh học (<3t, 3-8t, 8-12t, 12-19t).
   - 👉 **Áp dụng vào Báo cáo:** Chương 3, Mục 3.5 (Hình 3.9).
4. `gradcam_hand_overlay.png`: Dải 3 ảnh Grad-CAM (Ảnh gốc -> Bản đồ nhiệt Jet -> Lớp phủ Overlay kích hoạt cổ tay & đĩa sụn).
   - 👉 **Áp dụng vào Báo cáo:** Chương 3, Mục 3.6 (Hình 3.10: Kiểm chứng giải phẫu học XAI).
   - 👉 **Áp dụng vào Slide:** Slide 38 & 39 (Minh bạch hóa y tế Grad-CAM).
5. `clinical_report_sample.txt`: Báo cáo chẩn đoán mẫu kèm phân loại cảnh báo WHO.
   - 👉 **Áp dụng vào Báo cáo:** Chương 3, Mục 3.7.
   - 👉 **Áp dụng vào Slide:** Slide 40 (Hậu xử lý lâm sàng & cảnh báo WHO).
