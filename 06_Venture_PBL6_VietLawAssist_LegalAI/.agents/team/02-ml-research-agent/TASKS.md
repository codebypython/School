# 📋 TASKS — Agent 02: ML Research Agent

> **Cập nhật lần cuối:** 2026-09-09  
> **Giai đoạn hiện tại:** Phase 1 — BM25 Research & Implementation  
> **Phân công bởi:** PM-01 (Project Manager)

---

## Phase 0: Nghiên cứu & Khám phá (Tuần 0) ✅ HOÀN THÀNH

- [x] Đọc Proposal — nắm kiến trúc 4 tầng Comparison Ladder
- [x] Xác định models cần dùng: underthesea, PhoBERT, Qwen2.5-1.5B
- [x] Xác định libraries cần dùng: rank_bm25, sentence-transformers, faiss, peft, trl
- [x] Phân tích hardware constraints: RTX 3050 4GB + Colab T4
- [x] Viết tổng quan lý thuyết 4 tầng cho Grand Design Overview

---

## Phase 1: BM25 Research & Implementation (Tuần 1-2)

> **Triết lý:** Nghiên cứu kỹ lý thuyết + ghi chép thành tài liệu tham khảo TRƯỚC KHI viết code.  
> **Thư mục output:** `.agents/outputs/phase1/`

### Sóng 1 — Nghiên cứu lý thuyết (không phụ thuộc agent khác)

- [x] **M1** 📖 Báo cáo lý thuyết BM25 Okapi ✅
    - Output: `.agents/outputs/phase1/mlr-02_bm25_theory.md`
    - Nội dung bắt buộc:
        1. Giải thích công thức BM25Okapi từng thành phần: IDF, TF saturation, document length normalization
        2. Ý nghĩa siêu tham số k1 (range 1.2-2.0) và b (range 0-1), khi nào tăng/giảm
        3. So sánh BM25Okapi vs BM25L vs BM25Plus — tại sao chọn Okapi cho legal text
        4. Trích dẫn paper gốc: Robertson & Zaragoza (2009), "The Probabilistic Relevance Framework: BM25 and Beyond"
        5. Hạn chế của BM25: vocabulary mismatch, không hiểu ngữ nghĩa → dẫn đến nhu cầu Tầng 2 (Dense)
    - DoD: File .md có đầy đủ 5 mục trên, công thức LaTeX, ít nhất 2 references

- [x] **M2** 📖🗂 Khảo sát & So sánh Vietnamese Tokenizer ✅
    - Output: `.agents/outputs/phase1/mlr-02_tokenizer_comparison.md`
    - Nội dung bắt buộc:
        1. Liệt kê 3 tokenizer: PyVi, Underthesea, VnCoreNLP
        2. Mỗi tokenizer: cách cài đặt (pip command), cách import, cách gọi API tokenize
        3. Bảng so sánh trên 5 câu luật mẫu: tokens output, compound words bắt được, tốc độ
        4. Ưu/nhược điểm từng tokenizer cho domain pháp luật
        5. **Kết luận:** Chọn tokenizer nào, lý do cụ thể (có trích dẫn nếu có paper)
    - DoD: File .md có bảng so sánh cụ thể, code snippet mẫu mỗi tokenizer, kết luận rõ ràng

### Sóng 2 — Dữ liệu & Hướng dẫn (dựa trên Sóng 1)

- [x] **M3** 🗂 Bộ Vietnamese Legal Stopwords ✅
    - Output: `.agents/outputs/phase1/mlr-02_stopwords_vi_legal.txt`
    - Nội dung: Danh sách 80-120 từ dừng, mỗi dòng 1 từ, có comment giải thích nhóm
    - DoD: File .txt, chia nhóm rõ: (1) từ dừng chung tiếng Việt, (2) từ dừng pháp lý. Giải thích tiêu chí chọn ở header file.
    - Phụ thuộc: M2 (biết tokenizer nào để biết format từ ghép dùng `_` hay khoảng trắng)

- [x] **M4** 🛠 Hướng dẫn sử dụng thư viện rank-bm25 ✅
    - Output: `.agents/outputs/phase1/mlr-02_rank_bm25_guide.md`
    - Nội dung bắt buộc:
        1. Cài đặt: `pip install rank-bm25`
        2. API reference: `BM25Okapi(corpus, k1, b)`, `.get_scores(query)`, `.get_top_n(query, docs, n)`
        3. Code mẫu đầy đủ: tạo corpus → build index → query → lấy top-5
        4. Cách serialize index (pickle dump/load)
        5. Cách tune k1, b: grid search strategy
        6. Nguồn đọc thêm: GitHub repo, issues phổ biến
    - DoD: File .md, code mẫu copy-paste chạy được (có import, có data mẫu)
    - Phụ thuộc: M1 (hiểu lý thuyết trước khi hướng dẫn tool)

### Sóng 3 — Tổng hợp thiết kế

- [x] **M5** 📖 Thiết kế BM25 Pipeline (sơ đồ luồng) ✅
    - Output: Thêm mục cuối trong file `mlr-02_bm25_theory.md`
    - Nội dung: Sơ đồ Mermaid: Input Query → Lowercase → Tokenize (PyVi) → Remove Stopwords → BM25 Score → Sort → Top-K → Return. Ghi rõ mỗi bước dùng hàm/class nào trong codebase.
    - DoD: Sơ đồ Mermaid render được, mapping rõ với code trong `app/services/bm25_service.py`
    - Phụ thuộc: M1, M2, M3, M4

---

## Phase 2: Dense Retrieval Research (Tuần 3-4)

- [ ] Nghiên cứu Sentence-BERT architecture
- [ ] So sánh embedding models tiếng Việt: vietnamese-bi-encoder vs phobert-base
- [ ] Nghiên cứu FAISS index types: Flat vs IVF vs HNSW
- [ ] Thiết kế Dense Retrieval pipeline: encode → index → query → cosine sim
- [ ] Benchmark Recall@5: BM25 vs Dense

## Phase 3: RAG Pipeline Research (Tuần 5-6)

- [ ] Nghiên cứu Qwen2.5-1.5B-Instruct architecture & capabilities
- [ ] Nghiên cứu 4-bit quantization (BitsAndBytes): VRAM usage, speed tradeoff
- [ ] Thiết kế prompt template cho legal domain
- [ ] Nghiên cứu context window management: max_new_tokens, temperature
- [ ] Implement RAG pipeline: retrieve → format context → generate

## Phase 4: LoRA Fine-tuning Research (Tuần 7-8)

- [ ] Nghiên cứu LoRA: rank (r), lora_alpha, target_modules
- [ ] Nghiên cứu QLoRA: 4-bit + LoRA combined
- [ ] Thiết kế Alpaca format dataset schema cho legal Q&A
- [ ] Nghiên cứu SFTTrainer configuration: batch_size, gradient_accumulation
- [ ] Setup Colab notebook cho LoRA training

## Phase 5: Evaluation Support (Tuần 9-10)

- [ ] Hỗ trợ Agent-05 interpret metrics kết quả
- [ ] Error analysis: phân loại lỗi từng tầng
- [ ] Viết phần lý thuyết & thực nghiệm cho báo cáo
