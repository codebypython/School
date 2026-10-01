# 🎯 KẾ HOẠCH TÁC CHIẾN: PHÒNG TƯ LIỆU HỌC THUẬT, BÁO CÁO & SLIDE (DEPT 02)
> **Mã biệt đội:** `SQUAD-02-SLIDE-PRO` | **Trực thuộc:** `CORP-01-CV`  
> **Nhiệm vụ trọng tâm:** Sản xuất hệ thống Slide 43+ trang (47 trang chi tiết) với ưu tiên hình ảnh minh họa chính xác, tối giản, chuẩn kỹ thuật theo bản thiết kế `slide_content_43_pages.md`.

---

### 📋 Danh mục Tác vụ Đã Hoàn Thành (100%):
1. **Thiết Lập Biệt Đội Tác Chiến Slide (`SLIDE_PRODUCTION_TASKFORCE_PLAN.md`):**
   - Phân định rõ 5 vai trò: Academic Director, Visual Illustrator, Clinical & Data Specialist, Deep Learning Architect, Presentation Engineer.
   - Ban hành bộ chuẩn Rubric 100 điểm thẩm định chất lượng slide.

2. **Sản Xuất Bộ 24 Bản Vẽ Kỹ Thuật Vector Tối Giản (`figures/`):**
   - `fig_slide08_ossification_timeline.svg`: Tiến trình cốt hóa sụn & 8 xương cổ tay.
   - `fig_slide10_clinical_eda_distribution.svg`: Cơ cấu giới tính 54% Nam / 46% Nữ & phân phối Gauss.
   - `fig_slide11_stratified_split.svg`: Phân tầng 80/10/10 cố định (10.088 / 1.261 / 1.262 ca).
   - `fig_slide14_classical_cv_pipeline.svg`: Pipeline 5 bước Classical CV triệt tiêu học đường tắt.
   - `fig_slide15b_dl_taxonomy.svg`: 4 thế hệ học sâu BAA từ 2017 đến nay.
   - `fig_slide16_multimodal_film_architecture.svg`: Kiến trúc Đa phương thức & Điều biến FiLM.
   - `fig_slide18_resnet50_bottleneck.svg`: Cấu trúc Bottleneck & Skip connection (+1 gradient).
   - `fig_slide20_resnet_learning_dynamics.svg`: Động học học tập 15 epochs ResNet-50 (sweet spot 6.82m).
   - `fig_slide22_residual_distribution.svg`: Phân tích phần dư sai số (hành lang ±12m & histogram Gauss).
   - `fig_slide24_convnext_inverted_bottleneck.svg`: ConvNeXt 7x7 Depthwise, Inverted Bottleneck & GRN.
   - `fig_slide26_convnext_learning_dynamics.svg`: Động học hội tụ ConvNeXt-Tiny (Val MAE 6.18m Epoch 17).
   - `fig_slide28_convnext_vs_resnet_gain.svg`: 4 chiều bứt phá ConvNeXt (-15.2% MAE, -12.5% RMSE, +18.2% FPS).
   - `fig_slide30_swin_shifted_window.svg`: Cơ chế Shifted Window Self-Attention của Swin-T.
   - `fig_slide32_swin_learning_dynamics.svg`: Động học hội tụ Swin-T (Warm-up 2 epochs, 6.22m Epoch 18).
   - `fig_slide34_mae_by_age_groups.svg`: Phân tích sai số MAE theo 4 nhóm tuổi sinh lý.
   - `fig_slide35b_evaluation_criteria_pyramid.svg`: 5 trụ cột đánh giá lâm sàng AAP/RSNA.
   - `fig_slide36_tri_model_benchmark_card.svg`: Dashboard ma trận đối đầu chính thức.
   - `fig_slide36b_sota_comparison.svg`: Đối chiếu trực diện SOTA với các công bố quốc tế.
   - `fig_slide37_convnext_superiority.svg`: Luận giải 3 nguyên nhân ConvNeXt thắng áp đảo.
   - `fig_slide38_regression_gradcam.svg`: Thuật toán Regression Grad-CAM.
   - `fig_slide39_gradcam_clinical_verification.svg`: Kiểm chứng lâm sàng 3 Panel (Raw, Grad-CAM, Overlay).
   - `fig_slide40_who_alert_decision_tree.svg`: Cây quyết định cảnh báo lâm sàng WHO/AAP.
   - `fig_slide41_cdss_webapp_wireframe.svg`: Bản vẽ wireframe giao diện CDSS WebApp.
   - `fig_slide42b_scientific_publication_roadmap.svg`: Khung bản thảo bài báo chuẩn IEEE/Springer.

3. **Hệ Thống Trình Chiếu Đa Nền Tảng (3 Định Dạng Xuất Bản):**
   - 🌐 **Web Presentation 16:9 Widescreen Tương Tác:** `slides_presentation_43_pages.html` (Phím tắt `←/→`, Fullscreen `F`, Script `S`, Overview `O`, Print PDF `P`).
   - 📑 **Marp Presentation Chuẩn Markdown:** `presentation_43_slides.marp.md` (Xuất PDF / PPTX 1-click qua VS Code Marp).
   - 🐍 **Script Tự Động Hóa PowerPoint:** `generate_pptx_slides.py` (Sinh file native PPTX chuẩn 16:9).

4. **Đồng Bộ Dữ Liệu Nghiên Cứu:**
   - Đảm bảo 100% số liệu giữa `slide_content_43_pages.md`, `master_project_report_80_pages.md` và `STATUS.md` thống nhất tuyệt đối (MAE 6.26m, RMSE 8.40m, R² 0.9571).
