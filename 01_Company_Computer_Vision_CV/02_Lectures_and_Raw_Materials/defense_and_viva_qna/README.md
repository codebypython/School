# 🏛️ KHO TÀI LIỆU PHẢN BIỆN & HỎI ĐÁP BẢO VỆ ĐỒ ÁN (VIVA & DEFENSE VAULT)
## 🦴 Đồ Án Nghiên Cứu: Hệ Thống Đa Phương Thức Dự Đoán Tuổi Xương Nhi Đồng (RSNA)
**VisionLab Corp (CORP-01-CV) — Chuẩn Học Thuật Đại Học Bách Khoa (DUT)**

---

### 🎯 MỤC ĐÍCH & Ý NGHĨA HỌC THUẬT

Khi bảo vệ đồ án tốt nghiệp, đồ án môn học hoặc báo cáo nghiên cứu trước Hội đồng Giảng viên & Chuyên gia, **80% điểm số quyết định không nằm ở việc mô hình chạy được, mà nằm ở phần Phản biện & Hỏi đáp (Q&A Session)**:
1. **Chứng minh sinh viên tự tay thực nghiệm (Authentic Hands-on):** Trả lời rành mạch từng tham số nhỏ trong code (`compression=4`, `clipLimit=3.0`, `gender_dim=32`, `batch_size=32`).
2. **Chứng minh tư duy Kỹ thuật Hệ thống & Tối ưu Tài nguyên (System Engineering):** Hiểu rõ ràng về RAM, GPU VRAM, I/O đĩa cứng, tắc nghẽn DataLoader và hạn ngạch đám mây.
3. **Chứng minh hiểu biết sâu sắc về Miền Y tế Thực tế (Clinical Reasoning):** Phân tích được ý nghĩa sinh học của bức ảnh X-quang, hiện tượng dậy thì, và khả năng giải thích của AI (Explainable AI - XAI).

---

### 📂 CẤU TRÚC BỘ SỔ TAY PHẢN BIỆN (DEFENSE PLAYBOOKS)

| Tệp tài liệu | Chủ đề phản biện trọng tâm | Giai đoạn thực nghiệm tương ứng | Vị trí xuất hiện trên Slide / Báo cáo |
|:---|:---|:---:|:---:|
| **[`01_DATA_PREPROCESSING_AND_PIPELINE_DEFENSE_QNA.md`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/02_Lectures_and_Raw_Materials/defense_and_viva_qna/01_DATA_PREPROCESSING_AND_PIPELINE_DEFENSE_QNA.md)** | • Mức nén PNG (0 vs 4 vs 9), bảo toàn tín hiệu y tế<br>• Đa luồng ThreadPoolExecutor giải phóng CPython GIL<br>• Idempotent Offline Caching<br>• CLAHE bảo tồn sụn tiếp hợp vs Cân bằng lược đồ toàn cục<br>• Otsu + Morphology khử dị vật ký hiệu L/R | **Notebook 01** (Module 01) | **Slide 12 - 16**<br>Báo cáo Chương 2 (Mục 2.2 - 2.3) |
| **[`02_MODEL_ARCHITECTURE_AND_MULTIMODAL_FUSION_DEFENSE_QNA.md`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/02_Lectures_and_Raw_Materials/defense_and_viva_qna/02_MODEL_ARCHITECTURE_AND_MULTIMODAL_FUSION_DEFENSE_QNA.md)** | • Tại sao ResNet-50 đánh bại Swin-T và ConvNeXt?<br>• Bản chất Inductive Bias vs Data-Hungry Transformer<br>• Cơ chế Late Fusion (Concatenation) vs Early Fusion<br>• Giải mã cảnh báo DataLoader multiprocessing | **Notebook 02** (Module 02) | **Slide 17 - 28**<br>Báo cáo Chương 2 (Mục 2.4 - 2.5) |
| **[`03_TRAINING_DYNAMICS_AND_BENCHMARK_DEFENSE_QNA.md`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/02_Lectures_and_Raw_Materials/defense_and_viva_qna/03_TRAINING_DYNAMICS_AND_BENCHMARK_DEFENSE_QNA.md)** | • Ý nghĩa khoa học của mốc 15 Epochs<br>• Đánh giá mức độ hội tụ triệt để (ResNet vs Swin-T)<br>• Ràng buộc tài nguyên Kaggle GPU và rủi ro Overfitting<br>• Lịch suy giảm Cosine Annealing Learning Rate | **Notebook 02** (Module 02) | **Slide 29 - 34**<br>Báo cáo Chương 3 (Mục 3.1 - 3.2) |
| **`04_EXPLAINABLE_AI_AND_CLINICAL_DEPLOYMENT_DEFENSE_QNA.md`** *(Đang cập nhật)* | • Bản đồ nhiệt Grad-CAM tập trung vào sụn ngón tay và xương cổ tay<br>• Chẩn đoán sai lệch tuổi $\Delta$ (Dậy thì sớm vs Chậm lớn)<br>• Triển khai WebApp lâm sàng thời gian thực | **Notebook 03** (Module 03) | **Slide 35 - 43**<br>Báo cáo Chương 3 (Mục 3.3 - 3.4) |
