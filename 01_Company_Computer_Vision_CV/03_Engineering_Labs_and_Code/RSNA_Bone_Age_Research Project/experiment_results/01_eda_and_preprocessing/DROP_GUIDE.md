# 📥 DROPBOX 01: DỮ LIỆU EDA & ẢNH TIỀN XỬ LÝ (TỪ NOTEBOOK 01)
> **Mã nguồn phát sinh:** `01_Data_Audit_Classical_Preprocessing_Cache.ipynb`  
> **Bộ phận thụ hưởng:** Phòng Tư Liệu Học Thuật (`02_Lectures_and_Raw_Materials`)

### 📋 Danh mục File thả vào đây:
1. `eda_distribution_plots.png`: Biểu đồ 4 đồ thị phân phối lâm sàng (Histogram, Boxplot theo giới tính, Phân phối mật độ KDE, Cơ cấu tỷ lệ Nam/Nữ).
   - 👉 **Áp dụng vào Báo cáo:** Chương 2, Mục 2.2 (Hình 2.1: Thống kê mô tả tập dữ liệu RSNA 12.611 ca).
   - 👉 **Áp dụng vào Slide:** Slide 10 (Phân tích thống kê lâm sàng EDA).
2. `classical_cv_5steps_demo.png`: Dải 5 ảnh đối chiếu thực tế (Ảnh thô -> CLAHE -> Lọc Gauss -> Phân ngưỡng Otsu -> Morphology -> Bounding Crop 512x512).
   - 👉 **Áp dụng vào Báo cáo:** Chương 2, Mục 2.3 (Hình 2.2: Pipeline 5 bước tiền xử lý ảnh X-quang).
   - 👉 **Áp dụng vào Slide:** Slide 14 (Pipeline chuẩn hóa thị giác cổ điển).
3. `train_stratified.csv`: File phân tầng 80/10/10 cố định (10.088 train, 1.261 val, 1.262 test).
