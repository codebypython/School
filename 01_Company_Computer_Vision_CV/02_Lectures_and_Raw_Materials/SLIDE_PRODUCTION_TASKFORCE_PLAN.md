# 🎖️ ĐIỀU LỆ TÁC CHIẾN BIỆT ĐỘI THIẾT KẾ SLIDE CHUẨN KỸ THUẬT (SQUAD-02-SLIDE-PRO)
## SLIDE PRODUCTION TASKFORCE & TECHNICAL VISUALIZATION PLAYBOOK
> **Mã biệt đội:** `SQUAD-02-SLIDE-PRO` | **Trực thuộc:** `CORP-01-CV` (VisionLab Deep Tech Corp)  
> **Dự án chuẩn tham chiếu:** `MECHANICAL_FAULT_XRAY Project\Slide.pptx` (43 Slides chuẩn mực)  
> **Văn bản căn cứ:** `slide_content_43_pages.md` & `master_project_report_80_pages.md`  
> **Chuẩn sư phạm & Hội đồng:** Đại học Bách Khoa — ĐH Đà Nẵng (DUT) & Chuẩn công bố quốc tế IEEE/RSNA  

---

## 1. TỔ CHỨC ĐỘI NGŨ & PHÂN CÔNG TRÁCH NHIỆM (TASKFORCE ROLES)

Để hiện thực hóa bộ 43+ slide (47 slides chi tiết) với ưu tiên **hình ảnh minh họa chính xác, tối giản, chuẩn kỹ thuật**, biệt đội tác chiến được tổ chức thành 5 vị trí chuyên trách:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               SƠ ĐỒ TỔ CHỨC BIỆT ĐỘI THIẾT KẾ SLIDE (SQUAD-02-SLIDE-PRO)               │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                   🎯 GIÁM ĐỐC HỌC THUẬT & TỔNG ĐẠO DIỄN (ACD MENTOR)                    │
│                     • Quản trị cấu trúc logic 4 trụ cột & thời lượng 20-25p            │
│                     • Thẩm định chuẩn đầu ra DUT & Rubric phản biện Hội đồng           │
├──────────────────────────┬─────────────────────────────┬───────────────────────────────┤
│ 📐 KỸ SƯ TRỰC QUAN HÓA   │ 🔬 CHUYÊN VIÊN DỮ LIỆU &    │ 🧠 KIẾN TRÚC SƯ HỌC SÂU       │
│    (VISUAL ILLUSTRATOR)  │    LÂM SÀNG (DATA & XAI)    │    (DEEP LEARNING ARCHITECT)  │
│ • Thiết kế sơ đồ khối SVG│ • Trực quan hóa RSNA EDA    │ • Minh họa ResNet/ConvNeXt/Swin│
│ • Chuẩn hóa bảng màu tối │ • Cây quyết định cảnh báo   │ • Cơ chế FiLM Affine Layer    │
│ • Tối giản hóa thông tin │   lâm sàng WHO & AAP        │ • Ma trận đối đầu Benchmark   │
├──────────────────────────┴─────────────────────────────┴───────────────────────────────┤
│                   💻 KỸ SƯ PHẦN MỀM THUYẾT TRÌNH (PRESENTATION ENGINEER)               │
│                     • Phát triển Web Presentation 16:9 Widescreen tương tác            │
│                     • Đóng gói Marp Markdown & Script sinh mã tự động PPTX             │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.1. Bảng phân nhiệm cụ thể từng thành viên:
| Mã vai trò | Tên vai trò | Trách nhiệm then chốt | Tiêu chuẩn bàn giao |
|:---|:---|:---|:---|
| **R1-DIR** | Giám đốc Học thuật (Mentor) | Phê duyệt thông điệp học thuật, phân bổ thời gian Sinh viên 1 (Slide 01-16, 38-43) và Sinh viên 2 (Slide 17-37). | Khung kịch bản chuẩn xác từng giây. |
| **R2-ILLUST**| Kỹ sư Trực quan hóa | Vẽ và chuẩn hóa các sơ đồ khối vector SVG (Pipeline, Kiến trúc mạng, Cơ chế Attention, Phễu quyết định). | 100% hình vẽ tối giản, đường nét sắc sảo, không viền thừa. |
| **R3-CLINIC**| Chuyên viên Dữ liệu & XAI | Đối soát số liệu RSNA (12.611 ca), phân bổ 4 lứa tuổi, biên an toàn $\pm 12$m WHO/AAP và bản đồ Grad-CAM. | Số liệu khớp 100% với CSV và Báo cáo. |
| **R4-DLEARN**| Kiến trúc sư Học Sâu | Chuẩn hóa thông số kỹ thuật 3 mô hình (2048D, 768D, 7x7 Depthwise, Inverted Bottleneck, Window $8\times 8$, FiLM). | Bảng đối đầu chuẩn mực, minh họa toán học chuẩn. |
| **R5-ENGIN** | Kỹ sư Phần mềm Thuyết trình | Triển khai giao diện trình chiếu Web HTML5 responsive, bộ slide Marp, và script tạo PPTX tự động. | 3 định dạng xuất bản: HTML5, Marp, PPTX script. |

---

## 2. NGUYÊN TẮC THIẾT KẾ: CHÍNH XÁC — TỐI GIẢN — CHUẨN KỸ THUẬT

### 2.1. Triết lý Thiết kế Tối giản Chuẩn Kỹ thuật (Minimalist Technical Standard)
- **Tỉ lệ khung hình:** Chuẩn Widescreen **16:9** (1920x1080 px, SVG viewBox 1200x620).
- **Hệ màu Lâm sàng Xanh nhạt & Trắng (Light Blue & White Clinical Theme):**
  - **Nền chính (Canvas Background):** Pure White `#ffffff` / Soft Clinical Off-White `#f8fafc`.
  - **Khối chứa nội dung (Card Panels):** Light Blue Tint `#f0f7ff` / Clean Card `#f8fafc` với viền sắc nét `#bae6fd` hoặc `#e2e8f0`.
  - **Màu chữ chính (High Contrast Typography):** Dark Slate `#0f172a` (Tiêu đề chính), Slate Grey `#334155` (Nội dung chính), Muted Slate `#64748b` (Nội dung phụ & Chú thích).
  - **Màu nhấn công nghệ y tế (Clinical Accent Sky/Blue):** Medical Sky Blue `#0284c7` / Deep Sky Blue `#0369a1` / Soft Sky Tint `#e0f2fe`.
  - **Màu trạng thái chuẩn y khoa:**
    - 🟢 Emerald Green `#059669` (Nền badge: `#ecfdf5`, Viền: `#86efac`): Mô hình Quán quân, đạt chuẩn an toàn AAP $\le 12$m, phát triển bình thường.
    - 🟡 Amber Warning `#d97706` (Nền badge: `#fffbeb`, Viền: `#fde68a`): Cảnh báo chậm tăng trưởng / suy giáp $\Delta < -12$m.
    - 🔴 Crimson Red `#dc2626` / Rose `#e11d48` (Nền badge: `#fff1f2`, Viền: `#fecdd3`): Cảnh báo dậy thì sớm $\Delta > +12$m, nguy cơ sai số.
    - 🟣 Indigo / Violet `#6366f1` / `#4338ca` (Nền badge: `#e0e7ff`, Viền: `#c7d2fe`): Vision Transformer, FiLM modulation, Attention shifted windows.
- **Quy tắc "Một Slide - Một Thông Điệp Kỹ Thuật":** Mỗi slide chỉ giải quyết duy nhất một luận điểm then chốt. Không dồn quá 4 gạch đầu dòng; ưu tiên biểu đồ, sơ đồ luồng và bảng số liệu so sánh.
- **Tính chính xác tuyệt đối:** Mọi số liệu kiểm thử (MAE, RMSE, $R^2$, FPS) và siêu tham số ($lr$, $\delta=1.0$, $T_{\max}=15$, patch $4\times 4$, window $8\times 8$) phải trích xuất chính xác từ file thực nghiệm `BENCHMARK_LOG.md` và `result_tranning.ipynb`.

---

## 3. DANH MỤC TÀI SẢN TRỰC QUAN CẦN SẢN XUẤT (VISUAL ASSET INVENTORY)

Biệt đội chịu trách nhiệm sản xuất và tích hợp trọn vẹn 24 tài sản trực quan vector kỹ thuật chuẩn mực vào thư mục `figures/`:

| STT | Tên tệp vector SVG | Slide áp dụng | Mục đích kỹ thuật |
|:---:|:---|:---:|:---|
| 1 | `fig_slide08_ossification_timeline.svg` | Slide 08 | Minh họa tiến trình cốt hóa 8 xương cổ tay & đóng sụn ngón tay |
| 2 | `fig_slide10_clinical_eda_distribution.svg` | Slide 10 | Đồ thị phân phối lâm sàng: 54.18% Nam / 45.82% Nữ, đường chuông Gauss |
| 3 | `fig_slide11_stratified_split.svg` | Slide 11 | Ma trận phân tầng 80/10/10 cố định (10.088 / 1.261 / 1.262 ca) |
| 4 | `fig_slide14_classical_cv_pipeline.svg` | Slide 14 | Sơ đồ luồng 5 bước Classical CV (CLAHE ➔ Gauss ➔ Otsu ➔ Morph ➔ Crop) |
| 5 | `fig_slide15b_dl_taxonomy.svg` | Slide 15B | Cây tiến hóa 4 thế hệ học sâu trong BAA từ 2017 đến nay |
| 6 | `fig_slide16_multimodal_film_architecture.svg` | Slide 16 | Sơ đồ khối kiến trúc Đa phương thức tổng thể & Điều biến FiLM $\gamma(g), \beta(g)$ |
| 7 | `fig_slide18_resnet50_bottleneck.svg` | Slide 18 | Cấu trúc khối Bottleneck $1\times 1 \to 3\times 3 \to 1\times 1$ & Skip Connection |
| 8 | `fig_slide20_resnet_learning_dynamics.svg` | Slide 20 | Đồ thị thực nghiệm 15 epochs ResNet-50: Val MAE 111.4m ➔ 12.8m ➔ 6.82m sweet spot |
| 9 | `fig_slide22_residual_distribution.svg` | Slide 22 | Phân tích phần dư: Scatter plot tương quan 45° hành lang ±12m & Histogram Gauss μ≈0 |
| 10 | `fig_slide24_convnext_inverted_bottleneck.svg` | Slide 24 | Cấu trúc Inverted Bottleneck $7\times 7$ Depthwise, $C\to 4C\to C$ & GRN |
| 11 | `fig_slide26_convnext_learning_dynamics.svg` | Slide 26 | Động học hội tụ ConvNeXt-Tiny: Val MAE mượt mà đạt đỉnh 6.18m tại Epoch 17 |
| 12 | `fig_slide28_convnext_vs_resnet_gain.svg` | Slide 28 | Biểu đồ đối chiếu bước nhảy ConvNeXt: -15.2% MAE, -12.5% RMSE, +18.2% CPU FPS |
| 13 | `fig_slide30_swin_shifted_window.svg` | Slide 30 | Cơ chế tính Self-Attention theo cửa sổ thường vs Cửa sổ trượt Shifted Window |
| 14 | `fig_slide32_swin_learning_dynamics.svg` | Slide 32 | Động học hội tụ Swin-T: Warm-up 2 epochs, giảm sâu đạt 6.22m tại Epoch 18 |
| 15 | `fig_slide34_mae_by_age_groups.svg` | Slide 34 | Phân tích sai số MAE theo 4 nhóm tuổi sinh lý (Nhũ nhi, Nhi đồng, Tiền dậy thì, Vị thành niên) |
| 16 | `fig_slide35b_evaluation_criteria_pyramid.svg`| Slide 35B | Tháp 5 trụ cột đánh giá lâm sàng (MAE, RMSE, $R^2$, AAP 6m/12m, FPS) |
| 17 | `fig_slide36_tri_model_benchmark_card.svg` | Slide 36 | Dashboard so sánh đối đầu toàn diện 3 mô hình + Baseline |
| 18 | `fig_slide36b_sota_comparison.svg` | Slide 36B | Biểu đồ đối chiếu trực diện SOTA với các công bố quốc tế (2018-2024) |
| 19 | `fig_slide37_convnext_superiority.svg` | Slide 37 | Phân tích 3 nguyên nhân ConvNeXt vượt Swin-T và ResNet-50 |
| 20 | `fig_slide38_regression_gradcam.svg` | Slide 38 | Sơ đồ nguyên lý Regression Grad-CAM trích xuất đạo hàm ngược |
| 21 | `fig_slide39_gradcam_clinical_verification.svg`| Slide 39 | Kiểm chứng 3 Panel: Ảnh gốc ➔ Heatmap Grad-CAM ➔ Overlay giải phẫu (Act=0 dị vật) |
| 22 | `fig_slide40_who_alert_decision_tree.svg` | Slide 40 | Lưu đồ cây quyết định phân loại lâm sàng $\Delta$ theo chuẩn WHO |
| 23 | `fig_slide41_cdss_webapp_wireframe.svg` | Slide 41 | Bản vẽ wireframe giao diện chẩn đoán Streamlit CDSS WebApp |
| 24 | `fig_slide42b_scientific_publication_roadmap.svg`| Slide 42B | Lộ trình và khung cấu trúc bài báo khoa học chuẩn IEEE/Springer (+2đ) |

---

## 4. TIÊU CHÍ ĐÁNH GIÁ CHẤT LƯỢNG SLIDE (100-POINT RUBRIC)

Biệt đội áp dụng bộ tiêu chí chấm điểm khắt khe để đảm bảo điểm bảo vệ đồ án tối đa (A+):

| Tiêu chuẩn | Trọng số | Mô tả kiểm tra nghiệm thu |
|:---|:---:|:---|
| **1. Độ chính xác kỹ thuật & dữ liệu** | 25đ | Mọi thông số (tham số mạng, MAE, R², tỉ lệ %) trùng khớp 100% giữa Slide, Báo cáo và Notebook. |
| **2. Chất lượng hình ảnh trực quan & tính tối giản** | 25đ | Hình ảnh rõ ràng, phong cách vector tối giản hiện đại, màu sắc tương phản cao, không có chữ thừa. |
| **3. Sư phạm & Phân bổ thời lượng thuyết trình** | 20đ | Tổng thời lượng 20-25 phút, nhịp điệu chuyển vai mượt mà giữa SV1 và SV2, script súc tích, tự tin. |
| **4. Tính minh bạch học thuật & Chiều sâu nghiên cứu** | 20đ | Đầy đủ phần XAI Grad-CAM, giải thích nguyên nhân chênh lệch mô hình, đối chiếu SOTA quốc tế. |
| **5. Tính hoàn thiện & Đa nền tảng trình chiếu** | 10đ | Có sẵn bản trình chiếu Web HTML5 responsive, file Marp Markdown, và mã nguồn sinh PPTX. |

---

## 5. KẾT LUẬN & BÀN GIAO TÁC CHIẾN

Biệt đội tiến hành triển khai đồng bộ:
1. Phát hành toàn bộ 24 hình vẽ vector SVG vào `02_Lectures_and_Raw_Materials/figures/`.
2. Xây dựng bản trình chiếu web tương tác toàn diện 47 slide tại `slides_presentation_43_pages.html`.
3. Xây dựng tài liệu Marp Markdown `presentation_43_slides.marp.md`.
4. Viết mã tự động tạo file PowerPoint `generate_pptx_slides.py` (đầy đủ 47 slide dữ liệu và speaker notes).
5. Cập nhật Dashboard `STATUS.md`.
