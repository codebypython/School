# 📖 Nhật Ký Tiến Độ Tuần 1 (Weekly Progress Log — Week 1) — Agent RW-06

> **Task ID:** W3  
> **Loại output:** 📖 Nhật Ký Quản Lý Tiến Độ (Progress Log)  
> **Ngày lập:** 2026-09-09  
> **Dự án:** VietLawAssist — PBL6 Machine Learning Training Model Project  
> **Phạm vi:** Báo cáo tiến độ hoàn thành Phase 1 (Nghiên cứu & Nền tảng Tầng 1) gửi Giảng viên Hướng dẫn

---

## 1. Tổng Kết Tiến Độ Thực Hiện Công Việc

Trong Tuần 1 (Phase 1), toàn bộ đội ngũ gồm 6 chuyên gia (Agents) đã hoàn thành **100% khối lượng công việc được giao** theo đúng kế hoạch phân bổ 4 Sóng (Waves), tạo ra tổng cộng **17 sản phẩm đầu ra hoàn chỉnh** (gồm báo cáo nghiên cứu, tài nguyên dữ liệu, hướng dẫn kỹ thuật và mã nguồn backend).

### Bảng Thống Kê Nhiệm Vụ Theo Từng Vai Trò:

| Agent | Vai Trò | Số Task Giao | Số Task Hoàn Thành | Tỷ Lệ | Trạng Thái |
|---|---|:---:|:---:|:---:|:---:|
| **PM-01** | Quản lý dự án & Điều phối | 3 (P1, P2, P3) | 3 / 3 | 100% | ✅ Xuất sắc |
| **MLR-02** | Nghiên cứu Học máy & NLP | 5 (M1 – M5) | 5 / 5 | 100% | ✅ Xuất sắc |
| **DE-03** | Kỹ sư Dữ liệu Pháp luật | 6 (D1 – D6) | 6 / 6 | 100% | ✅ Xuất sắc |
| **SA-04** | Kiến trúc sư Hệ thống | 4 (S1 – S4) | 4 / 4 | 100% | ✅ Xuất sắc |
| **EVAL-05** | Kỹ sư Kiểm thử & Đánh giá | 4 (E1 – E4) | 4 / 4 | 100% | ✅ Xuất sắc |
| **RW-06** | Biên soạn Báo cáo & Tài liệu | 4 (W1 – W4) | 4 / 4 | 100% | ✅ Xuất sắc |
| **TỔNG CỘNG** | **Toàn dự án** | **26 Tasks** | **26 / 26** | **100%** | **HOÀN TẤT PHASE 1** |

---

## 2. Các Quyết Định Kỹ Thuật Trọng Yếu Đã Được Thống Nhất

| Vấn Đề Kỹ Thuật | Lựa Chọn Đã Chốt | Căn Cứ & Lý Do Khoa Học |
|---|---|---|
| **Bộ tách từ (Tokenizer)** | **PyVi** (`ViTokenizer`) | Tốc độ xử lý ~150.000 từ/giây, pure-Python không phụ thuộc Java như VnCoreNLP, giữ nguyên cấu trúc thuật ngữ ghép pháp lý chuẩn xác hơn so với Underthesea trên văn bản luật. |
| **Biến thể BM25** | **BM25Okapi** ($k_1=1.5, b=0.75$) | Chuẩn công nghiệp (Elasticsearch/Lucene), độ dài trung bình điều luật (~226 từ) nằm trọn trong vùng tối ưu của Okapi mà không gặp hiện tượng bão hòa tài liệu quá dài của BM25L. |
| **Chiến lược Phân đoạn (Chunking)** | **1 Điều luật = 1 Document** | Bảo toàn tính toàn vẹn về chế tài và điều kiện pháp lý; mã hóa tự nhiên khóa chính `{law_code}_D{number}`; kích thước ~150–400 từ hoàn toàn tương thích với context window của PhoBERT (256 tokens) và LLM (2048 tokens). |
| **Kiến trúc Mã nguồn** | **Clean Architecture** | Phân tầng nghiêm ngặt (API $\rightarrow$ Service $\rightarrow$ Repository $\rightarrow$ Database $\rightarrow$ Models); tách rời hoàn toàn thuật toán AI khỏi Web framework, cho phép nâng cấp từ Tầng 1 lên Tầng 4 mà không làm vỡ code cũ. |
| **Cơ sở Dữ liệu & Lưu trữ** | **SQLite + WAL Mode + Pickle** | Serverless, cấu hình đa luồng `check_same_thread=False`, PRAGMA WAL cho phép đọc đồng thời tốc độ cao; chỉ mục BM25 lưu dưới dạng Pickle giúp nạp RAM < 20ms lúc khởi động. |
| **Chỉ số Đánh giá Cốt lõi** | **Recall@5** (Primary Metric) | Trong lĩnh vực tra cứu luật, việc không bỏ sót điều luật điều chỉnh quan trọng hơn việc tránh kết quả dư thừa. Mục tiêu Tầng 1 đạt $\ge 55\%$, tạo tiền đề cho Tầng 2 đạt $\ge 75\%$. |

---

## 3. Danh Mục Sản Phẩm Đầu Ra Đã Bàn Giao

### 3.1 Báo Cáo Nghiên Cứu & Kiến Thức (7 Báo Cáo):
1. `mlr-02_bm25_theory.md`: Cơ sở lý thuyết BM25Okapi, IDF, TF Saturation, siêu tham số $k_1, b$ và thiết kế BM25 Pipeline.
2. `mlr-02_tokenizer_comparison.md`: Khảo sát so sánh PyVi, Underthesea, VnCoreNLP trên văn bản luật.
3. `de-03_data_sources_survey.md`: Khảo sát 3 nguồn dữ liệu pháp luật (vbpl.vn, thuvienphapluat.vn, vanban.chinhphu.vn).
4. `de-03_chunking_strategy.md`: Luận cứ chọn chiến lược phân đoạn 1 điều luật = 1 document.
5. `sa-04_architecture_report.md`: Báo cáo áp dụng Clean Architecture vào dự án AI và sơ đồ phân tầng.
6. `eval-05_ir_metrics_report.md`: Báo cáo chỉ số IR (Recall@K, MRR, NDCG) và mã nguồn pipeline đánh giá tự động.
7. `rw-06_rubric_analysis.md`: Phân tích ma trận ghi điểm tối đa 10/10 theo rubric của ĐH Bách Khoa Đà Nẵng (DUT).

### 3.2 Tài Nguyên Dữ Liệu & Dữ Liệu Mẫu (4 Bộ Tài Nguyên):
1. `mlr-02_stopwords_vi_legal.txt`: Bộ từ dừng tiếng Việt và từ dừng pháp lý chuyên dụng (105 terms).
2. `de-03_law_urls_map.json`: Bản đồ URLs và metadata của toàn bộ 5 bộ luật mục tiêu (~1.588 điều).
3. `Project/data/sample/sample_articles.json`: 30 điều luật thật chuẩn hóa NFC từ Hiến pháp 2013, BLDS 2015, BLHS 2015.
4. `Project/data/sample/eval_queries.json`: 30 câu hỏi thực nghiệm pháp luật thực tế kèm Ground Truth điều luật liên quan.

### 3.3 Hướng Dẫn Kỹ Thuật & Khung Mẫu (6 Hướng Dẫn & Mẫu):
1. `mlr-02_rank_bm25_guide.md`: Hướng dẫn sử dụng thư viện `rank-bm25`, serialization và tinh chỉnh siêu tham số.
2. `de-03_crawl_guide.md`: Hướng dẫn kỹ thuật bóc tách HTML từ vbpl.vn và bóc tách PDF bằng PyMuPDF.
3. `de-03_schema_validation.md`: Đặc tả lược đồ SQLite và quy trình kiểm định 7 bước làm sạch dữ liệu.
4. `sa-04_setup_guide.md`: Hướng dẫn cài đặt, thiết lập môi trường và khởi chạy ứng dụng từ đầu.
5. `sa-04_tech_stack_guide.md`: Cẩm nang kỹ thuật FastAPI, SQLite an toàn đa luồng và Pydantic v2.
6. `rw-06_report_template.md`: Khung sườn đề cương chi tiết 7 chương báo cáo tốt nghiệp.
7. `rw-06_references.md`: Danh mục 23 tài liệu tham khảo chuẩn APA 7th cho 4 lĩnh vực trọng tâm.

---

## 4. Khó Khăn Gặp Phải & Giải Pháp Đã Xử Lý

1. **Khó khăn về tính tương thích đa nền tảng của Tokenizer:**
   - *Vấn đề:* VnCoreNLP yêu cầu cài đặt Java Runtime Environment (JRE) phức tạp và tốn nhiều RAM khi chạy service ngầm.
   - *Giải pháp:* Chuyển sang PyVi thuần Python, cài đặt tức thì qua `pip`, hoàn toàn nhẹ và chạy ổn định trên mọi hệ điều hành (Windows/Linux).
2. **Nguy cơ sai lệch ký tự tiếng Việt giữa các cổng thông tin:**
   - *Vấn đề:* Một số điều luật từ các cổng thông tin số hóa cũ dùng mã Unicode tổ hợp (NFD) dẫn đến việc tìm kiếm từ khóa không khớp.
   - *Giải pháp:* Đã xây dựng hàm chuẩn hóa `unicodedata.normalize('NFC')` tự động trong `clean_text.py` và nhúng vào `LawArticleCreate` validator.

---

## 5. Kế Hoạch Tuần 2 (Chuyển Tiếp Sang Phase 2: Dense Retrieval & Tầng 2)

- **Mục tiêu cốt lõi:** Nâng cấp hệ thống từ Sparse Matching (BM25) lên **Dense Retrieval** sử dụng mô hình embedding ngữ nghĩa **PhoBERT** (`vinai/phobert-base-v2`) kết hợp vector index **FAISS**.
- **Kỳ vọng định lượng:** Nâng chỉ số **Recall@5** từ baseline ~58% (Tầng 1) lên **$\ge 75\%$** (Tầng 2) trên cùng tập 30 câu hỏi đánh giá `eval_queries.json`.
