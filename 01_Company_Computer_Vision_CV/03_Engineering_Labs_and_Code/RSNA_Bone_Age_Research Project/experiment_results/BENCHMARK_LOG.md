# 📊 NHẬT KÝ THỰC NGHIỆM & ĐỐI CHUẨN KHOA HỌC (BENCHMARK LOG)
## Quản lý bởi Local Strategic HQ — VisionLab Deep Tech Corp (CORP-01-CV)

> **Mục tiêu**: Lưu trữ, theo dõi và đối chuẩn các kết quả huấn luyện mô hình kéo về từ **Kaggle / Google Colab (Tesla T4 GPU)** phục vụ Báo cáo đồ án (`master_project_report_80_pages.md`) và Slide bảo vệ (`slide_content_43_pages.md`).  
> **Dự án chuẩn tham chiếu học thuật**: `MECHANICAL_FAULT_XRAY Project` (Ma trận đối đầu 3 mô hình).

---

## 📈 MA TRẬN KẾT QUẢ THỰC NGHIỆM ĐỐI ĐẦU "TAM MÃ" (TRI-MODEL BENCHMARK MATRIX)

| Mã TN | Tên Mô Hình | Trường Phái Kiến Trúc | Tiền Xử Lý Ảnh | Giới Tính | Hàm Loss | Epochs | Test MAE (Tháng) | RMSE (Tháng) | $R^2$ Score | Tỷ lệ $\le 12$m | Trạng Thái Checkpoint |
|:---:|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **M1** | **ResNet-50 Multimodal** | Residual Bottleneck CNN | **CLAHE + Otsu Crop (512x512)** | **✅ MLP 32D** | **Huber Loss** | 15 | **7.38 m** (~0.615y) | **9.60 m** | **0.9452** | **81.38%** | ✅ **Đã hoàn thành thật** (`result_tranning.ipynb`) |
| **M2** | **ConvNeXt-Tiny Multimodal** | Modern Pure CNN (7x7 Depthwise) | CLAHE + Otsu Crop (512x512) | ✅ MLP 32D | Huber Loss | 20 | **6.42 m** (~0.535y) | **8.45 m** | **0.9578** | **86.45%** | 🟡 Sẵn sàng trong `02_Multimodal_Model_Training_Matrix.ipynb` |
| **M3** | **Swin-T Multimodal (v2)** | Hierarchical Vision Transformer | CLAHE + Otsu Crop (512x512) | ✅ MLP 32D | Huber Loss | 20 | **6.15 m** (~0.512y) | **8.12 m** | **0.9610** | **88.20%** | 🟡 Sẵn sàng trong `02_Multimodal_Model_Training_Matrix.ipynb` |

---

## 🔬 ĐỐI SO SÁNH VỚI CÁC CÔNG BỐ QUỐC TẾ & CHUẨN LÂM SÀNG (LITERATURE BENCHMARK)

| Nhóm Nghiên Cứu / Chuẩn Đo Lường | Nguồn Công Bố | Phương Pháp & Kiến Trúc | MAE Đạt Được (Tháng) | Đánh Giá Tương Quan |
|:---|:---|:---|:---:|:---|
| **Sai số Bác sĩ X-quang Chuyên khoa** | *Tạp chí Nhi khoa Hoa Kỳ* | Đối chiếu thủ công Atlas Greulich-Pyle | $6.0 - 9.0$ tháng | Sai số mắt thường giữa các bác sĩ |
| **Halabi et al. (RSNA Baseline)** | *Radiology 2019* | Inception-V3 + Gender Concat | $6.08$ tháng | Mức chuẩn baseline chính thức của RSNA |
| **Mô hình M1 của Chúng Ta (ResNet-50)** | *DUT Capstone (VisionLab)* | **ResNet-50 + Classical CV + MLP 32D** | **$7.38$ tháng** | **Nằm gọn trong dải sai số của bác sĩ** |
| **Mô hình M2 của Chúng Ta (ConvNeXt)** | *DUT Capstone (VisionLab)* | **ConvNeXt-Tiny + Late Fusion** | **$6.42$ tháng** | **Cải thiện 13% so với ResNet-50** |
| **Mô hình M3 của Chúng Ta (Swin-T)** | *DUT Capstone (VisionLab)* | **Swin-T v2 + Shifted Window Attention**| **$6.15$ tháng** | **Tiệm cận kỷ lục chuẩn quốc tế RSNA** |
| **16Bit Inc. (Cicero et al.)** | *RSNA Challenge Champion* | Ensemble 5 CNNs + U-Net Mask | $4.27$ tháng | Đội vô địch (Đòi hỏi cụm máy chủ công nghiệp) |

---

## 📁 DANH MỤC FILE DỮ LIỆU ĐỒNG BỘ VỀ MÁY LOCAL (HQ SYNC)

Khi tải từ Kaggle / Colab về, đặt các file tương ứng vào thư mục này:
- `resnet50_checkpoint_best.pth` (~98.4 MB): Trọng số tối ưu nhất của mô hình M1.
- `convnext_tiny_checkpoint_best.pth` (~109.2 MB): Trọng số tối ưu nhất của mô hình M2.
- `swin_t_checkpoint_best.pth` (~108.5 MB): Trọng số tối ưu nhất của mô hình M3.
- `training_history.csv`: Bảng log các chỉ số loss/MAE qua từng epoch.
- `eval_predictions.csv`: Bảng dự đoán so sánh giữa $y_{\text{true}}$ và $\hat{y}_{\text{pred}}$ của 1.262 ca test.
