# 📋 TASKS — Agent 03: Data Engineer Agent

> **Cập nhật lần cuối:** 2026-09-09  
> **Giai đoạn hiện tại:** Phase 1 — Corpus Collection  
> **Phân công bởi:** PM-01 (Project Manager)

---

## Phase 0: Nghiên cứu & Khám phá (Tuần 0) ✅ HOÀN THÀNH

- [x] Đọc Proposal — xác định 5 bộ luật target (~1.588 điều)
- [x] Khảo sát nguồn crawl: vbpl.vn, thuvienphapluat.vn, vanban.chinhphu.vn
- [x] Thiết kế data schema (corpus document + Q&A pair)
- [x] Xác định chunking strategy: 1 điều = 1 document
- [x] Ước tính effort: crawl 3.5 ngày + Q&A 4 ngày

---

## Phase 1: Corpus Collection (Tuần 1-2)

> **Triết lý:** Khảo sát kỹ nguồn dữ liệu + ghi chép hướng dẫn TRƯỚC KHI viết crawler.  
> **Thư mục output:** `.agents/outputs/phase1/`

### Sóng 1 — Khảo sát & Nghiên cứu nguồn (không phụ thuộc agent khác)

- [x] **D1** 📖 Khảo sát chi tiết nguồn dữ liệu ✅
    - Output: `.agents/outputs/phase1/de-03_data_sources_survey.md`
    - Nội dung bắt buộc:
        1. **vbpl.vn:** Cấu trúc URL (pattern link tới từng bộ luật), cấu trúc HTML (thẻ chứa nội dung điều luật, class/id cần select), anti-bot measures (nếu có), robots.txt
        2. **thuvienphapluat.vn:** Tương tự — URL pattern, DOM structure, rate limiting
        3. **vanban.chinhphu.vn:** Backup source — có download PDF không, format PDF thế nào
        4. Mỗi nguồn kèm: snippet HTML mẫu (copy 1 đoạn HTML chứa 1 điều luật), CSS selector cần dùng
        5. Kết luận: nguồn nào crawl HTML, nguồn nào cần PDF, nguồn nào không crawl được
    - DoD: File .md phân tích đầy đủ 3 nguồn, có snippet HTML mẫu, có kết luận chọn nguồn

- [x] **D3** 📖 Báo cáo Chunking Strategy ✅
    - Output: `.agents/outputs/phase1/de-03_chunking_strategy.md`
    - Nội dung bắt buộc:
        1. Giải thích 3 chiến lược chunking: (a) theo Điều, (b) theo Khoản, (c) theo Paragraph/cửa sổ trượt
        2. Bảng so sánh ưu/nhược từng chiến lược cho bài toán legal retrieval
        3. Tại sao chọn "1 điều = 1 document": giữ nguyên ngữ cảnh pháp lý, dễ trích dẫn "Điều X Khoản Y"
        4. Ví dụ minh họa: 1 điều luật thực tế → cách nó trở thành 1 document với metadata
        5. Trường hợp đặc biệt: điều luật quá dài (>1000 từ), điều luật bị sửa đổi/bổ sung
    - DoD: File .md, có bảng so sánh, có ví dụ minh họa cụ thể, có xử lý edge cases

### Sóng 2 — Dữ liệu & Hướng dẫn (dựa trên D1)

- [x] **D2** 🗂 Bản đồ URLs toàn bộ 5 bộ luật ✅
    - Output: `.agents/outputs/phase1/de-03_law_urls_map.json`
    - Nội dung: JSON chứa thông tin mỗi bộ luật:
        ```json
        {
          "HP2013": {
            "law_name": "Hiến pháp nước CHXHCN Việt Nam 2013",
            "source": "vbpl.vn",
            "base_url": "https://vbpl.vn/...",
            "total_articles_expected": 120,
            "effective_date": "2014-01-01",
            "notes": "Crawl HTML, 11 chương"
          }
        }
        ```
    - DoD: JSON valid, đủ 5 bộ luật, URL có thể truy cập được (đã verify)
    - Phụ thuộc: D1 (biết nguồn nào dùng, URL pattern thế nào)

- [x] **D4** 🛠 Hướng dẫn Crawl & Parse từng nguồn ✅
    - Output: `.agents/outputs/phase1/de-03_crawl_guide.md`
    - Nội dung bắt buộc:
        1. Công cụ cần cài: `pip install beautifulsoup4 httpx PyMuPDF lxml`
        2. Cách crawl HTML (BeautifulSoup): step-by-step với code snippet mẫu
        3. Cách parse PDF (PyMuPDF/fitz): step-by-step với code snippet mẫu
        4. Regex patterns cho cấu trúc Điều luật VN: `r"Điều\s+(\d+)\.\s*(.*)"`, `r"(\d+)\.\s+"`
        5. Cách xử lý: rate-limiting (sleep 1s), User-Agent rotation, retry on failure
        6. Cách lưu raw data: cấu trúc thư mục `data/raw/{law_code}/`
    - DoD: File .md, code snippets copy-paste chạy được, đủ cho cả HTML và PDF path
    - Phụ thuộc: D1 (biết cấu trúc HTML/PDF mỗi nguồn)

- [x] **D5** 🗂 Bộ dữ liệu mẫu 30 điều luật ✅
    - Output: `Project/data/sample/sample_articles.json`
    - Nội dung: 30 điều luật thật (10 HP2013, 10 BLDS2015, 10 BLHS2015)
    - Format: Array of objects đúng schema `LawArticleCreate` (article_id, law_code, law_name, chapter, article_number, title, content, full_text, effective_date, source_url, word_count)
    - DoD: JSON valid, 30 objects, nội dung copy chính xác từ nguồn chính thống, đã clean Unicode NFC
    - Phụ thuộc: D2 (biết URL nguồn), D1 (biết cách trích xuất)

- [x] **D6** 📖 Báo cáo Data Schema & Validation Checklist ✅
    - Output: `.agents/outputs/phase1/de-03_schema_validation.md`
    - Nội dung bắt buộc:
        1. Mô tả schema SQLite `law_articles`: từng cột, kiểu dữ liệu, ràng buộc, ý nghĩa
        2. Mapping: schema ↔ Pydantic model `LawArticleCreate` trong code
        3. Checklist validate sau khi crawl:
            - [ ] HP2013: 120 điều?
            - [ ] BLDS2015: 689 điều?
            - [ ] BLHS2015: 426 điều?
            - [ ] LHNGD2014: 133 điều?
            - [ ] LLD2019: 220 điều?
            - [ ] Encoding: tất cả NFC?
            - [ ] Duplicate: 0?
        4. Cách chạy validation query SQL
    - DoD: File .md, checklist cụ thể với con số expected, SQL queries mẫu
    - Phụ thuộc: Hiểu schema từ `app/core/database.py` đã tạo

---

## Phase 2: Corpus QA & Indexing Support (Tuần 3-4)

- [ ] Cross-validate dữ liệu crawl với nguồn chính thống
- [ ] Loại bỏ duplicates, fix encoding errors
- [ ] Hỗ trợ Agent-02 build BM25 index từ corpus
- [ ] Hỗ trợ Agent-02 encode corpus embeddings (PhoBERT)

## Phase 3: Q&A Dataset Creation (Tuần 7-8)

- [ ] Thu thập đề thi PLĐC từ các trường ĐH (~150 cặp)
- [ ] Trích xuất câu hỏi từ giáo trình PLĐC (~100 cặp)
- [ ] Tự tạo câu hỏi từ điều luật quan trọng (~250 cặp)
- [ ] Format toàn bộ theo Alpaca format (instruction/input/output)
- [ ] Peer review: kiểm tra chéo chất lượng Q&A
- [ ] Split dataset: 70% train / 30% test
- [ ] Export dataset statistics report

## Phase 4: Test Set for Evaluation (Tuần 8-9)

- [ ] Curate 100 câu hỏi evaluation điển hình
- [ ] Viết đáp án chuẩn cho mỗi câu hỏi (theo cấu trúc 4 phần)
- [ ] Annotate relevant articles cho mỗi câu hỏi (ground truth retrieval)
- [ ] Validate: không overlap giữa test set và training set
