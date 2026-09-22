# 📊 PROJECT STATUS DASHBOARD — VietLawAssist

> **Cập nhật lần cuối**: 2026-09-13 | **Tuần hiện tại**: Tuần 0 (Pre-development)
> 
> File này được cập nhật sau mỗi phiên làm việc. Agent mới đọc file này để biết ngay trạng thái dự án.

---

## Current Phase: 🔵 FOUNDATION (Tuần 0/15)

Dự án đang ở giai đoạn thiết lập nền tảng. Tầng 1 BM25 đã có skeleton code, 3 tầng còn lại chưa triển khai.

---

## Implementation Progress

### Tầng 1: BM25 Sparse Retrieval
- [x] FastAPI skeleton (`main.py`, `config.py`)
- [x] SQLite DB manager (`core/database.py`) — WAL mode, parameterized queries, dual tables
- [x] Pydantic models (`models/law_article.py`, `models/textbook_principle.py`)
- [x] Repositories (`repositories/article_repo.py`, `repositories/textbook_repo.py`) — CRUD + batch insert
- [x] BM25 Search Service (`services/bm25_service.py`) — 358 dòng, production-ready
- [x] API routes: `/api/health`, `/api/retrieve`
- [x] Smoke tests: 6/6 pass (schema, textbook, tokenizer, BM25, dual DB integrity, routes)
- [x] Sample data: 40 articles (đủ 5 bộ luật) + 5 nguyên lý giáo trình + 20 eval queries
- [x] **Thu thập & Cấu trúc corpus 5 bộ luật** — Đã khởi tạo `data/raw/corpus_combined.json` & `scripts/crawl_laws.py`
- [x] **Ingest script kép** (`scripts/ingest_db.py`) — Nạp thành công vào `law_corpus.db`

### Tầng 2: PhoBERT Dense Retrieval
- [ ] `services/dense_service.py` — PhoBERT + FAISS
- [ ] `scripts/build_faiss.py` — Build FAISS index offline
- [ ] API endpoint `/api/retrieve/dense`

### Tầng 3: RAG (Qwen2.5-1.5B 4-bit)
- [ ] `services/rag_service.py` — Load model + generate
- [ ] Prompt templates cho 5 dạng đề (Few-Shot CoT)
- [ ] API endpoint `/api/generate/rag`

### Tầng 4: LoRA Fine-tuned RAG
- [ ] 500 cặp Q&A dataset (`data/sft_vietlaw_500.json`)
- [ ] `scripts/train_lora.py` — LoRA training script
- [ ] `services/lora_service.py` — Serve LoRA adapter

### Hệ thống phụ trợ
- [ ] Intent Router (phân loại 5 dạng đề thi PLĐC)
- [ ] Citation Guardrail (Regex + DB verify)
- [ ] Evaluation pipeline (ROUGE-L, BERTScore, Recall@5)
- [ ] React Frontend (Dual-Mode UI)
- [ ] Docker deployment
- [ ] Barem template schemas (JSON)

### Tài liệu & Tổ chức Doanh nghiệp
- [x] Onboarding Protocol & Cẩm nang giao tiếp (`COMMUNICATION_PLAYBOOK.md` + Corporate `AGENTS.md`)
- [x] Agent Entry Point (`.agents/rules/AGENTS.md`)
- [x] Domain Protocol Hard Rules (`.agents/rules/protocol.md`)
- [x] Ban Chiến Lược & Học Thuật (`01_Strategy_and_Proposal/` — Proposal, Rubrics, Knowledge Map, Governance)
- [x] Ban Nghiệp Vụ & Đặc Tả (`02_Domain_and_Specifications/` — Concept, Tech Spec, Barem Templates, Roadmap)
- [x] Master Sitemap Dashboard (`README.md`)
- [x] Điều Lệ Hoạt Động Doanh Nghiệp chuẩn mực (`COMPANY_CHARTER.md`)

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú | Trạng thái |
|:-:|:---|:---:|:---|:---:|
| 1 | `data/raw/` rỗng | 🔴 Critical | Đã nạp `corpus_combined.json` và script crawl | ✅ Resolved |
| 2 | Chưa có bảng `textbook_principles` | 🟡 Medium | Đã thêm DDL, model, repo và nạp 5 nguyên lý | ✅ Resolved |

---

## Last Session

- **Date**: 2026-09-22
- **Work Done**: Hoàn tất triển khai toàn diện Hệ thống Quản trị & Xử lý Dữ liệu Chuẩn mực (Data Pipeline Suite):
  - Xây dựng gói mô-đun hóa `Project/scripts/data_pipeline/`:
    + `config.py`: Cấu hình đa nguồn (CSDL Quốc gia VBPL + Thư viện Pháp luật TVPL) cho cả 5 bộ luật cốt lõi.
    + `downloader.py`: Crawler tự động bóc tách vùng văn bản luật sạch (`divContentDoc`) với cơ chế retry và exponential backoff.
    + `parser.py`: Bộ giải mã HTML/Text chuyên sâu sang Article-level JSON kèm tokenization từ ghép tiếng Việt (PyVi/Underthesea).
    + `sft_builder.py`: Khung quản lý và sinh dữ liệu SFT 500 mẫu kèm Golden Seeds chuẩn barem cho cả 5 Intent codes và Citation Guardrail.
    + `split_sft.py`: Thuật toán phân tầng dữ liệu (Stratified Split) chia 80/20 Train/Val ở cả 2 định dạng Alpaca và ChatML (ShareGPT).
    + `kaggle_bundle.py`: Đóng gói tự động bộ dữ liệu lên Kaggle Dataset (`data/kaggle_bundle/`) kèm checksum MD5 và kết nối Kaggle CLI.
    + `benchmark_builder.py`: Quản lý và kiểm định tập Hold-out Test Benchmark (đảm bảo Zero Data Leakage).
    + `manage_pipeline.py`: Master CLI một chạm điều phối toàn bộ chu trình sống của dữ liệu.
  - Vượt qua 100% (6/6) bài kiểm tra smoke tests tự động (`pytest tests/test_smoke.py`).
  - Kiểm thử thực tế các lệnh: `download`, `parse`, `ingest`, `split-sft`, `prep-kaggle`, `benchmark`, `stats`.
- **Files Modified/Created**:
  - `Project/scripts/data_pipeline/config.py` (new)
  - `Project/scripts/data_pipeline/__init__.py` (new)
  - `Project/scripts/data_pipeline/downloader.py` (new)
  - `Project/scripts/data_pipeline/parser.py` (new)
  - `Project/scripts/data_pipeline/sft_builder.py` (new)
  - `Project/scripts/data_pipeline/split_sft.py` (new)
  - `Project/scripts/data_pipeline/kaggle_bundle.py` (new)
  - `Project/scripts/data_pipeline/benchmark_builder.py` (new)
  - `Project/scripts/data_pipeline/manage_pipeline.py` (new)
  - `Project/scripts/ingest_db.py` (modified UTF-8 safeguard)
  - `STATUS.md` (updated)

## Next Priority (P0)

1. **Triển khai Tầng 2: PhoBERT Dense Retrieval + FAISS** (`app/services/dense_service.py` & `scripts/build_faiss.py`).
2. **Triển khai Intent Router** (`app/services/intent_router.py`) phân loại 5 dạng đề thi PLĐC.
3. **Mở rộng dữ liệu** toàn văn lên 1.588 điều luật và benchmark Recall@5 (Tầng 1 BM25 vs Tầng 2 PhoBERT).
4. **Chuẩn bị hồ sơ Báo cáo Tiến độ Đợt 1 nộp Thầy Thắng**.
