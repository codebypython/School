# 📊 PROJECT STATUS DASHBOARD — VisionLab Corp (CORP-01-CV)

> **Cập nhật lần cuối**: 2026-09-29 | **Giai đoạn**: Hoàn thành Thực nghiệm Đối đầu Tam mã & Hồ sơ Công bố Khoa học  
> **Dự án Chuẩn Tham Chiếu**: `MECHANICAL_FAULT_XRAY Project` (Báo cáo chuyên sâu, Slide 43+ trang, Đối đầu 3 mô hình)  
> **Mentor chuyên trách**: DUT Computer Vision Mentor (`AGENT_PROFILE.md`)  
> **Mô hình Vận hành**: **Kaggle Modular 3-Notebooks** $\longleftrightarrow$ **Local Workstation (Strategic HQ & WebApp)**

---

## 🏛️ Sứ Mệnh & Phân Tầng Trách Nhiệm

| Phân Vùng | Trọng Tâm Nhiệm Vụ | Hiện Trạng & Tài Sản Quản Lý |
|:---|:---|:---|
| ☁️ **Kaggle Cloud Compute** | - **NB01**: Data Audit & Preprocessing Cache (512x512, Otsu+CLAHE, Fixed Split CSV) ✅<br>- **NB02**: Tri-Model Training Matrix (ResNet-50 vs ConvNeXt vs Swin-T) với FiLM Modulation ✅<br>- **NB03**: Benchmark Evaluation, Statistical Error Analysis, XAI Grad-CAM & Export ✅ | - Đã hoàn thành 100% cả 3 Notebook trên Kaggle GPU/CPU<br>- Đã xuất 5 tài sản thực nghiệm chuẩn: Bảng CSV đối đầu, biểu đồ tương quan 4 lứa tuổi, phân tích phần dư, ma trận so sánh, và bản đồ Grad-CAM |
| 💻 **Local Workstation (HQ)** | - Quản trị Báo cáo Kỹ thuật Chuyên sâu (`master_project_report_80_pages.md`) ✅<br>- Quản trị Kịch bản Slide Thuyết trình (`slide_content_43_pages.md`) ✅<br>- Xây dựng Bản thảo Bài báo Khoa học chuẩn IEEE / Springer (Mục 3.11) ✅<br>- Vận hành Ứng dụng Chẩn đoán Lâm sàng Offline (`clinical_webapp/app.py`) ✅ | - Đã đồng bộ số liệu thực tế 100% giữa Report, Slide và CSV<br>- Bổ sung đầy đủ 5 tiêu chí của Thầy: SOTA literature, bộ tiêu chí đa chiều, phân tích cơ chế chênh lệch, và bản thảo bài báo khoa học |

---

## 📈 Ma Trận Thực Nghiệm Đối Đầu Chính Thức (Tri-Model Benchmark Matrix)

| ID | Mô Hình | Trường Phái Kiến Trúc | Tiền Xử Lý Ảnh | Nhánh Lâm Sàng | Test MAE (tháng) | Test RMSE (tháng) | $R^2$ Score | Tỷ lệ $\le 6$m | Tỷ lệ $\le 12$m | GPU FPS | CPU FPS | Xếp Hạng & Trạng Thái |
|:---:|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **Base** | **ResNet-50 Baseline** | Residual Bottleneck CNN | CLAHE + Otsu (512x512) | Naive Concat 1-bit | **7.38m** | **9.60m** | **0.9452** | 51.5% | 81.38% | 67.5 | 1.1 | ⚪ Mô hình nền tảng đối chứng |
| **M1** | **ResNet-50 Multimodal**| Residual Bottleneck CNN | CLAHE + Otsu (512x512) | FiLM Modulation | **6.47m** | **8.70m** | **0.9540** | **59.7%** | **84.70%** | **67.5** | 1.1 | 🥉 Giảm -12.3% lỗi nhờ FiLM |
| **M2** | **ConvNeXt-Tiny** | Modern Pure CNN (7x7 Depthwise) | CLAHE + Otsu (512x512) | FiLM Modulation | **6.26m** | **8.40m** | **0.9571** | **59.2%** | **86.50%** | 55.0 | **1.3** | 🏆 **QUÁN QUÂN TOÀN DIỆN (CHAMPION)** |
| **M3** | **Swin-T (v2)** | Hierarchical Vision Transformer | CLAHE + Otsu (512x512) | FiLM Modulation | **6.37m** | **8.62m** | **0.9549** | **58.7%** | **86.00%** | 37.7 | 0.9 | 🥈 **Á QUÂN XUẤT SẮC** |

---

## 🎯 Đối Chiếu Với Các Công Bố Quốc Tế Gần Nhất (SOTA Benchmark)

| Nghiên Cứu & Tác Giả | Tạp Chí & Năm | Kiến Trúc Mô Hình | Phương Pháp Giới Tính | Test MAE (tháng) | Đánh Giá So Sánh |
|:---|:---|:---|:---|:---:|:---|
| **Đồng thuận Bác sĩ X-quang** (Halabi et al.) | *Radiology* (2019) | Chuyên gia X-quang | Đọc phim lâm sàng | **~7.32 m** | Độ lệch chuẩn giữa các bác sĩ |
| **Larson et al.** | *Radiology* (2018) | ResNet-50 (Single Model) | Naive Concatenation | **7.30 m** | Bài báo nền tảng đầu tiên |
| **Wu et al.** | *CMPB* (2021) | Residual Attention Net | Attention Concatenation | **6.60 m** | Bổ sung cơ chế chú ý |
| **Kasani et al.** | *CBM* (2023) | ConvNeXt-Tiny (Single) | Late Feature Fusion | **6.38 m** | Sử dụng ConvNeXt cơ bản |
| **Pan et al.** | *IEEE JBHI* (2024) | Multimodal CNN + FiLM | Feature Modulation (FiLM) | **6.30 m** | Công bố gần nhất về FiLM |
| **VisionLab DUT (M2: ConvNeXt FiLM)** | *Đề tài nghiên cứu* | **ConvNeXt-Tiny + FiLM** | **FiLM Channel Modulation** | **6.26 m** | 🏆 **Vượt qua tất cả các mô hình đơn lẻ trên** |

---

## 📋 Trạng Thái Tài Liệu & Hồ Sơ Báo Cáo

- ✅ **Slide Thuyết Trình & Hệ Thống Trình Chiếu Chuẩn Kỹ Thuật (`slide_content_43_pages.md`)**:
  - Đã thành lập Biệt đội thiết kế slide chuyên trách: `SLIDE_PRODUCTION_TASKFORCE_PLAN.md` (5 vai trò, Rubric 100 điểm).
  - Đã sản xuất toàn bộ **24 bản vẽ vector SVG kỹ thuật tối giản** trong thư mục `02_Lectures_and_Raw_Materials/figures/`.
  - Đã xuất bản giao diện trình chiếu Web Widescreen 16:9 tương tác: `slides_presentation_43_pages.html` (47 slides, phím tắt navigation, speaker script drawer, overview modal, hỗ trợ in PDF).
  - Đã xuất bản bộ slide chuẩn Marp Markdown: `presentation_43_slides.marp.md` (1-click export PDF/PPTX qua VS Code Marp).
  - Đã phát triển script tự động hóa PowerPoint: `generate_pptx_slides.py`.
  - Đã tích hợp đầy đủ các slide then chốt: 15B (Taxonomy), 35B (5 tiêu chí lâm sàng), 36 (Benchmark đối đầu), 36B (SOTA quốc tế), 37 (Luận giải ConvNeXt), 42B (Bản thảo IEEE/Springer).
- ✅ **Báo Cáo Kỹ Thuật (`master_project_report_80_pages.md`)**:
  - Đã bổ sung Mục 2.1.4 (State-of-the-Art Review & Research Gaps).
  - Đã nâng cấp Mục 2.5 (Toán học FiLM & Vanishing Modality Gradient).
  - Đã mở rộng Mục 2.7 (5 tiêu chuẩn đánh giá lâm sàng và tỷ số RMSE/MAE).
  - Đã cập nhật Mục 3.1 - 3.4 với toàn bộ kết quả kiểm thử thực tế.
  - Đã bổ sung Mục 3.4.1 (Bảng đối chiếu SOTA chi tiết) và 3.4.2 (Phân tích cơ chế chênh lệch).
  - Đã bổ sung Mục 3.11 (Bản thảo bài báo khoa học hoàn chỉnh chuẩn IEEE/Springer).
- ✅ **Kho Lưu Trữ Git**: Đã đồng bộ toàn bộ tài sản nghiên cứu, slide và bản vẽ vector chuẩn kỹ thuật.

---

## 📌 Session Handover Log (2026-09-30)
- **Date**: 2026-09-30
- **Completed**:
  1. Chuyển đổi toàn diện theme sang tông xanh nhạt và trắng y tế tối giản (Light Blue & White Clinical Theme) cho toàn bộ hệ thống thuyết trình:
     - `presentation_43_slides.marp.md`: Toàn bộ frontmatter, CSS styles, bảng biểu, blockquote, bullet points.
     - `generate_pptx_slides.py`: Bảng màu PPTX RGB (canvas trắng, divider xanh nhạt `#f0f7ff`, card `#f8fafc`, border `#bae6fd`).
     - `slides_presentation_43_pages.html`: CSS variables (`--bg-primary: #ffffff`, `--bg-secondary: #f0f7ff`, v.v.), stage, sidebar drawer, overview modal, tất cả 47 slides và inline SVG previews.
     - `slide_content_43_pages.md`: Hướng dẫn Canva palette trắng & xanh nhạt.
  2. Đơn giản hóa & chuẩn hóa toàn bộ 24/24 vector SVG figures trong `02_Lectures_and_Raw_Materials/figures/`:
     - Nền trắng tinh khiết (`#ffffff`), loại bỏ grid lines trang trí và glow filters mờ nhòe.
     - Hệ thống thẻ tinh gọn: Card `#f8fafc` hoặc `#f0f9ff`, viền `#bae6fd` / `#e2e8f0`.
     - Phân cấp thông tin rõ ràng: Tiêu đề xanh `#0284c7`, text xám đậm chuẩn Slate `#0f172a` / `#334155`, thẻ Quán quân `#ecfdf5` viền `#059669`, thẻ cảnh báo `#fffbeb` viền `#fde68a`, thẻ nguy cấp `#fef2f2` viền `#fca5a5`.
- **In Progress**: Không có (Đã hoàn thành 100% yêu cầu).
- **Blockers**: Không có.
- **Next**: Sẵn sàng xuất PDF/PPTX hoặc trình chiếu bảo vệ trước Hội đồng nghiệm thu DUT.
