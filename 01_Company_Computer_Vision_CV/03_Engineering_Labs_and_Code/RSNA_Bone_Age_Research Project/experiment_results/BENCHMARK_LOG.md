# 📊 NHẬT KÝ THỰC NGHIỆM & ĐỐI CHUẨN KHOA HỌC (BENCHMARK LOG)
## Quản lý bởi Local Strategic HQ — VisionLab Deep Tech Corp

> **Mục tiêu**: Lưu trữ, theo dõi và đối chuẩn các kết quả huấn luyện mô hình kéo về từ **Google Colab (Tesla T4 GPU)** để phục vụ cập nhật Báo cáo đồ án (`project_report.md`) và Slide bảo vệ (`slide_content_20_pages.md`).

---

## 📈 MA TRẬN KẾT QUẢ THỰC NGHIỆM ĐỐI ĐẦU (ABLATION STUDY MATRIX)

| Mã TN | Tên Thí Nghiệm | Kiến Trúc Backbone | Tiền Xử Lý Ảnh | Giới Tính (Clinical) | Hàm Loss | Epochs | Val MAE (Tháng) | RMSE | $R^2$ Score | Trạng Thái Checkpoint |
|:---:|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **E0** | Raw Baseline | ResNet-50 | Resize thô | ❌ Không | MSE ($L_2$) | 30 | *Chờ Colab* | -- | -- | `checkpoints/e0_baseline.pth` |
| **E1** | + Classical CV | ResNet-50 | **CLAHE + Otsu Crop** | ❌ Không | MSE ($L_2$) | 30 | *Chờ Colab* | -- | -- | `checkpoints/e1_classical_cv.pth` |
| **E2** | + Gender Fusion | ResNet-50 | CLAHE + Otsu Crop | **✅ MLP 32D** | **Huber Loss** | 40 | *Chờ Colab* | -- | -- | `checkpoints/e2_multimodal.pth` |
| **E3** | + Modern SOTA | **EfficientNet-B4** | Pipeline 5 bước | ✅ MLP 32D | Huber Loss | 40 | *Chờ Colab* | -- | -- | `checkpoints/best_model.pth` |
| **E4** | Custom ViT | **Swin-T (Custom)** | Pipeline 5 bước | ✅ Cross-Attn | Huber Loss | 40 | *Nghiên cứu sâu*| -- | -- | `checkpoints/e4_swin_transformer.pth` |

---

## 🔬 BẢNG ĐỐI SO SÁNH VỚI CÁC CÔNG BỐ QUỐC TẾ (SOTA LITERATURE BENCHMARK)

| Nhóm Nghiên Cứu / Bài Báo | Nguồn Công Bố | Phương Pháp & Kiến Trúc | MAE Đạt Được (Tháng) | Đánh Giá Tương Quan |
|:---|:---|:---|:---:|:---|
| **Halabi et al.** | *Radiology 2019* (RSNA Official) | Inception-V3 + Gender concatenation | $6.08$ | Chuẩn baseline quốc tế |
| **16Bit Inc. (Cicero et al.)** | *RSNA Challenge Champion* | Ensemble 5 CNNs + U-Net Hand Mask | $4.27$ | Đội vô địch cuộc thi |
| **Mô hình của Chúng ta (E3/E4)** | *DUT Capstone Project (VisionLab)* | **EfficientNet / Swin-T + Late Fusion** | **Mục tiêu $\le 5.2$** | **Tiệm cận SOTA & Vượt bác sĩ X-quang** |
| **Sai số Bác sĩ X-quang chuyên khoa** | *Tạp chí Nhi khoa Hoa Kỳ* | Đối chiếu bản đồ Greulich-Pyle thủ công | $6.0 - 9.0$ | Sai số đọc mắt thường giữa các bác sĩ |

---

## 📁 DANH MỤC FILE DỮ LIỆU ĐỒNG BỘ VỀ MÁY LOCAL
Khi tải từ Google Colab về, đặt các file tương ứng vào thư mục này:
- `best_model.pth`: Trọng số tối ưu nhất dùng cho Clinical WebApp.
- `training_history.csv`: Bảng log các chỉ số loss/MAE qua từng epoch để vẽ đồ thị tự động.
- `eval_predictions.csv`: Bảng dự đoán so sánh giữa $y_{\text{true}}$ và $\hat{y}_{\text{pred}}$ của 1,425 ca test.
