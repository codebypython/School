# 🛠 Đề Cương Chi Tiết & Template Báo Cáo Đồ Án PBL6 — Agent RW-06

> **Task ID:** W2  
> **Loại output:** 🛠 Khung Mẫu Tài Liệu Đồ Án (Thesis Master Template)  
> **Ngày tạo:** 2026-09-09  
> **Dùng cho:** Cấu trúc toàn bộ báo cáo tốt nghiệp / đồ án PBL6 nộp trường ĐH Bách Khoa — ĐH Đà Nẵng (DUT)

---

## 1. Quy Chuẩn Trình Bày Chung (DUT Thesis Standards)

- **Số trang mục tiêu:** 70 – 90 trang (không tính phụ lục).
- **Phông chữ:** Times New Roman, cỡ chữ 13pt (hoặc 12pt tùy quy định khoa), giãn dòng 1.3 - 1.5 lines.
- **Lề trang:** Trên 2.0 cm, Dưới 2.0 cm, Trái 3.0 cm (đóng gáy), Phải 2.0 cm.
- **Quy tắc trích dẫn:** Chuẩn APA (American Psychological Association) 7th edition.

---

## 2. Bảng Phân Bổ 7 Chương & Ma Trận Đóng Góp Của Các Agents

| Chương | Tên Chương | Số Trang Dự Kiến | Agent Cung Cấp Input Chính | Tỷ Trọng Điểm Rubric Phục Vụ |
|:---:|---|:---:|:---:|:---:|
| **1** | Mở đầu & Đặt vấn đề | 6 – 8 | PM-01, RW-06 | R1 (1.0đ) |
| **2** | Cơ sở Lý thuyết & Tổng quan Nghiên cứu | 16 – 20 | MLR-02, EVAL-05 | R3 (2.0đ) |
| **3** | Phân tích Yêu cầu & Thiết kế Hệ thống | 12 – 16 | SA-04 | R3 (2.0đ) |
| **4** | Thu thập & Tiền xử lý Dữ liệu Pháp luật | 10 – 14 | DE-03 | R2 (1.0đ) |
| **5** | Thực nghiệm, Đánh giá & So sánh Thang đo 4 Tầng | 16 – 20 | EVAL-05, MLR-02 | R2 (2.0đ) |
| **6** | Xây dựng Ứng dụng & Triển khai Demo | 8 – 10 | SA-04 | R4 (2.0đ) |
| **7** | Kết luận & Hướng phát triển | 4 – 5 | PM-01, RW-06 | R5 (2.0đ) |
| **—** | **TỔNG CỘNG** | **72 – 93 trang** | **Toàn đội ngũ 6 Agents** | **10.0 / 10.0 điểm** |

---

## 3. Cấu Trúc Chi Tiết Từng Chương & Hướng Dẫn Nội Dung

### Chương 1: Mở Đầu & Đặt Vấn Đề (6 – 8 trang)
*Mục tiêu: Thuyết phục hội đồng về tính cấp thiết, giá trị thực tiễn và tính khả thi của đề tài.*
- **1.1 Lý do chọn đề tài:** Khó khăn của sinh viên không chuyên khi học môn Pháp luật Đại cương; hạn chế của công cụ tìm kiếm truyền thống (không hiểu ngữ cảnh, khó tra cứu điều luật cụ thể).
- **1.2 Mục tiêu nghiên cứu:** Xây dựng hệ thống VietLawAssist hỗ trợ tra cứu và giải đáp thông minh dựa trên thang đo so sánh 4 tầng (Comparison Ladder).
- **1.3 Đối tượng và phạm vi nghiên cứu:** 5 bộ luật trọng tâm của môn PLĐC (~1.588 điều luật); giới hạn phần cứng máy tính cá nhân (GPU RTX 3050 4GB).
- **1.4 Phương pháp nghiên cứu:** Nghiên cứu lý thuyết IR/NLP; phương pháp thực nghiệm so sánh định lượng (empirical evaluation).
- **1.5 Bố cục của đồ án:** Tóm tắt ngắn gọn nội dung 7 chương tiếp theo.

---

### Chương 2: Cơ Sở Lý Thuyết & Tổng Quan Nghiên Cứu (16 – 20 trang)
*Mục tiêu: Khẳng định sự am hiểu sâu sắc về mặt giải pháp học máy và mô hình xử lý ngôn ngữ tự nhiên.*
- **2.1 Xử lý ngôn ngữ tự nhiên cho tiếng Việt:** Đặc thù ngữ pháp từ ghép tiếng Việt, kỹ thuật Word Segmentation; so sánh PyVi, Underthesea, VnCoreNLP (lấy từ output `mlr-02_tokenizer_comparison.md`).
- **2.2 Sparse Retrieval và Thuật toán BM25 Okapi:** Nguyên lý xác suất PRF, công thức toán học IDF, TF Saturation, chuẩn hóa độ dài; giới hạn của BM25 (lấy từ `mlr-02_bm25_theory.md`).
- **2.3 Dense Retrieval và Bi-Encoder:** Biểu diễn ngữ nghĩa bằng vector dense embedding, mô hình PhoBERT pre-trained; kỹ thuật tìm kiếm láng giềng gần nhất (FAISS, HNSW).
- **2.4 Mô hình Ngôn ngữ Lớn (LLM) và Kỹ thuật RAG:** Tổng quan RAG (Retrieval-Augmented Generation); giải quyết hiện tượng hallucination trong lĩnh vực pháp lý; mô hình Qwen2.5-1.5B và kỹ thuật lượng tử hóa GGUF/4-bit.
- **2.5 Phương pháp Fine-tuning Hiệu quả Tham số (PEFT / LoRA):** Nguyên lý cập nhật ma trận rank thấp LoRA; huấn luyện có giám sát (SFT) trên tập dữ liệu hỏi đáp pháp luật.

---

### Chương 3: Phân Tích Yêu Cầu & Thiết Kế Hệ Thống (12 – 16 trang)
*Mục tiêu: Minh chứng kiến trúc phần mềm chuẩn mực, chuyên nghiệp và có tính mở rộng cao.*
- **3.1 Kiến trúc Thang đo So sánh 4 Tầng (Comparison Ladder Architecture):** Thiết kế cốt lõi của đề tài: Tầng 1 (BM25) $\rightarrow$ Tầng 2 (Dense) $\rightarrow$ Tầng 3 (RAG) $\rightarrow$ Tầng 4 (Fine-tuned LLM).
- **3.2 Áp dụng Clean Architecture vào Ứng dụng AI:** Phân tầng phần mềm (Presentation, Service, Repository, Core, Domain) giúp tách biệt hoàn toàn thuật toán ML khỏi framework web (lấy từ `sa-04_architecture_report.md`).
- **3.3 Thiết kế Cơ sở Dữ liệu & Lưu trữ Chỉ mục:** Cấu trúc bảng SQLite `law_articles`, thiết kế lưu trữ chỉ mục bộ nhớ đệm (Pickle, FAISS index).
- **3.4 Thiết kế Giao diện Lập trình Ứng dụng (RESTful API Specifications):** Đặc tả chi tiết các endpoints `/api/retrieve`, `/api/generate`, `/api/health`.

---

### Chương 4: Thu Thập & Tiền Xử Lý Dữ Liệu Pháp Luật (10 – 14 trang)
*Mục tiêu: Trình bày quy trình kỹ thuật dữ liệu (Data Engineering) minh bạch và đáng tin cậy.*
- **4.1 Khảo sát & Đánh giá Nguồn Dữ liệu:** Phân tích cấu trúc các cổng thông tin pháp luật vbpl.vn, thuvienphapluat.vn (lấy từ `de-03_data_sources_survey.md`).
- **4.2 Chiến lược Phân đoạn Văn bản (Chunking Strategy):** Biện minh kỹ thuật và pháp lý cho việc chọn đơn vị phân đoạn "1 Điều luật = 1 Document" (lấy từ `de-03_chunking_strategy.md`).
- **4.3 Pipeline Tiền xử lý & Làm sạch Văn bản:** Quy trình chuẩn hóa Unicode NFC, loại bỏ ký tự rác, tách từ ghép, xây dựng bộ từ dừng pháp lý chuyên biệt (`mlr-02_stopwords_vi_legal.txt`).
- **4.4 Xây dựng Tập Dữ liệu Thực nghiệm (Evaluation Benchmark Dataset):** Cấu trúc 30 câu hỏi mẫu PLĐC kèm ground truth đa mức độ khó (lấy từ `eval_queries.json`).

---

### Chương 5: Thực Nghiệm, Đánh Giá & So Sánh Thang Đo 4 Tầng (16 – 20 trang)
*Mục tiêu: Đỉnh cao học thuật của đồ án — Cung cấp số liệu định lượng chứng minh sự tiến bộ qua từng tầng.*
- **5.1 Hệ chỉ số đo lường hiệu năng (Evaluation Metrics):** Giải thích công thức và ý nghĩa của Recall@K, MRR, NDCG@K, ROUGE-L, BERTScore (lấy từ `eval-05_ir_metrics_report.md`).
- **5.2 Thiết lập Môi trường Thực nghiệm:** Cấu hình phần cứng (RTX 3050, Colab T4), siêu tham số huấn luyện và đánh giá.
- **5.3 Kết quả Thực nghiệm & Phân tích So sánh 4 Tầng:**
  - Bảng tổng hợp số liệu chi tiết: Recall@5 tăng từ ~58% (Tầng 1) lên ~78% (Tầng 2); ROUGE-L tăng ở Tầng 3 và Tầng 4.
  - Biểu đồ trực quan hóa tiến trình cải thiện hiệu năng.
- **5.4 Phân tích Lỗi (Error Analysis) & Nghiên cứu Bóc tách (Ablation Study):** Đánh giá các trường hợp hệ thống dự đoán sai; phân tích đóng góp của bước lọc từ dừng và tách từ PyVi.

---

### Chương 6: Xây Dựng Ứng Dụng & Triển Khai Demo (8 – 10 trang)
*Mục tiêu: Thể hiện sản phẩm hoàn thiện có khả năng ứng dụng thực tế cao.*
- **6.1 Hiện thực hóa Backend với FastAPI:** Triển khai dịch vụ web bất đồng bộ, quản lý vòng đời bộ nhớ chỉ mục.
- **6.2 Giao diện Tương tác Tra cứu Pháp luật:** Minh họa các tính năng giao diện người dùng: nhập câu hỏi, hiển thị điều luật trích xuất, câu trả lời giải thích chi tiết.
- **6.3 Đo lường Độ trễ & Hiệu năng Vận hành:** Đánh giá thời gian phản hồi (latency) trung bình trên từng tầng.

---

### Chương 7: Kết Luận & Hướng Phát Triển (4 – 5 trang)
*Mục tiêu: Đúc kết thành quả và mở ra triển vọng tương lai.*
- **7.1 Các kết quả chính đạt được:** Hoàn thành trọn vẹn mục tiêu đề ra; chứng minh hiệu quả của phương pháp so sánh 4 tầng.
- **7.2 Những hạn chế của đề tài:** Giới hạn dữ liệu ở 5 bộ luật; giới hạn tham số mô hình do tài nguyên phần cứng cá nhân.
- **7.3 Hướng phát triển trong tương lai:** Mở rộng toàn bộ hệ thống Pháp điển Quốc gia; tích hợp kỹ thuật Reranking (Cross-Encoder); triển khai ứng dụng trên nền tảng di động.
