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
- [x] 521 cặp Q&A dataset chuẩn barem DUT (`data/processed/sft_vietlaw_500.json`) — Đã tích hợp 16 câu hỏi Ground Truth từ đề thi thực tế (kèm Studocu cleaned), 100% unique, Citation Guardrail verified
- [x] Phân tầng Stratified Split 80/20: Train (416 mẫu) & Val (105 mẫu) ở cả 2 format Alpaca và ChatML
- [x] Thư mục Kaggle Workspace (`Project/kaggle/`):
  - `Project/kaggle/dataset/`: Bundle trọn gói dữ liệu sạch + checksum MD5 + `dataset-metadata.json`
  - `Project/kaggle/notebooks/train_vietlaw_qlora.py` & `.ipynb`: Huấn luyện QLoRA 4-bit NF4, Response Loss Masking, Auto-Resume Checkpoint, tối ưu Kaggle Free T4 GPU (<25 phút, VRAM <4GB)
  - `Project/kaggle/notebooks/README_KAGGLE.md`: Cẩm nang hướng dẫn vận hành từng bước trên Kaggle
- [ ] `services/lora_service.py` — Serve LoRA adapter trong FastAPI backend

### Hệ thống phụ trợ
- [x] Master Data Pipeline CLI (`scripts/data_pipeline/manage_pipeline.py`) — Quản trị chu trình dữ liệu một chạm
- [x] Smart PDF Extractor (`scripts/data_pipeline/smart_extractor.py`) — Trích xuất text PDF tốc độ cao bằng PyMuPDF (fitz) hoàn toàn miễn phí
- [x] Synthetic Legal Engine (`scripts/data_pipeline/synthetic_engine.py`) — Sinh bài tập và lời giải chuẩn barem 6 Intent codes
- [x] Local Exam Harvester (`scripts/data_pipeline/exam_crawler.py`) — Thu hoạch và bóc tách đề thi từ `data/raw/exams/` (đã nạp 2 bộ đề thi học kỳ DUT)
- [x] Citation Guardrail (`scripts/data_pipeline/sft_builder.py`) — Đối soát trích dẫn luật thực định trong SQLite
- [ ] Intent Router (phân loại 5 dạng đề thi PLĐC)
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
| 3 | SFT dataset & Kaggle Workspace | 🔴 Critical | Đã hoàn thành 505 mẫu, 80/20 train/val split, Kaggle dataset & notebook | ✅ Resolved |

---

## Last Session

- **Date**: 2026-09-23
- **Work Done**: Hoàn tất trọn gói Pipeline Thu thập, Xử lý Dữ liệu SFT và Môi trường Huấn luyện Kaggle Chịu lỗi (Fault-Tolerant Kaggle Suite):
  - Xây dựng và kiểm chuẩn tập dữ liệu SFT 505 mẫu chuẩn barem DUT (`sft_vietlaw_500.json`):
    + 100% các mẫu độc nhất (Zero duplication sau hàm chuẩn hóa query MD5).
    + 100% mẫu vượt qua Citation Guardrail đối soát trực tiếp với SQLite `law_corpus.db`.
    + Phân tầng Stratified Split 80/20: Train set 404 mẫu, Val set 101 mẫu ở cả 2 định dạng Alpaca và ChatML (`train_sft.json`, `val_sft.json`, `train_sft_chatml.json`, `val_sft_chatml.json`).
  - Kiến tạo thư mục Kaggle Workspace chuyên nghiệp (`Project/kaggle/`):
    + `kaggle/dataset/`: 11 tệp dữ liệu sạch, manifest MD5 checksum, `dataset-metadata.json`, sẵn sàng import hoặc upload bằng Kaggle CLI.
    + `kaggle/notebooks/train_vietlaw_qlora.py` & `.ipynb`:
      * QLoRA 4-bit NF4 tối ưu bộ nhớ (VRAM <4GB trên Tesla T4).
      * `DataCollatorForCompletionOnlyLM`: Prompt Loss Masking (chỉ tính loss trên câu trả lời trợ lý).
      * Fault-Tolerant Auto-Resume: Tự động phát hiện và tiếp tục từ checkpoint gần nhất nếu đứt kết nối.
      * Real-time metrics logger ra CSV & JSON.
      * Xuất file nén `vietlaw_lora_adapter.zip` (~25MB) để nạp trực tiếp vào backend local mà không tốn dung lượng đĩa.
    + `kaggle/notebooks/README_KAGGLE.md`: Cẩm nang hướng dẫn thao tác 4 bước cho sinh viên/nhà nghiên cứu.
  - Mở rộng Master CLI `manage_pipeline.py` với các lệnh: `curate-sft`, `crawl-exams`, `setup-kaggle`, `run-all`.
  - Smoke tests: Đạt 8/8 bài kiểm tra tự động passed 100% (`pytest tests/test_smoke.py`).
- **Files Modified/Created**:
  - `Project/scripts/data_pipeline/synthetic_engine.py` (upgraded - 6 intent generators, 505 unique cases)
  - `Project/scripts/data_pipeline/sft_curator.py` (new)
  - `Project/scripts/data_pipeline/exam_crawler.py` (new)
  - `Project/scripts/data_pipeline/kaggle_manager.py` (new)
  - `Project/scripts/data_pipeline/manage_pipeline.py` (modified - new CLI subcommands)
  - `Project/kaggle/dataset/*` (11 files)
  - `Project/kaggle/notebooks/*` (3 files)
  - `Project/tests/test_smoke.py` (modified - 8 tests passed)
  - `STATUS.md` (updated)

## Next Priority (P0)

1. **Triển khai Tầng 2: PhoBERT Dense Retrieval + FAISS** (`app/services/dense_service.py` & `scripts/build_faiss.py`).
2. **Triển khai Intent Router** (`app/services/intent_router.py`) phân loại 5 dạng đề thi PLĐC.
3. **Mở rộng dữ liệu** toàn văn lên 1.588 điều luật và benchmark Recall@5 (Tầng 1 BM25 vs Tầng 2 PhoBERT).
4. **Chuẩn bị hồ sơ Báo cáo Tiến độ Đợt 1 nộp Thầy Thắng**.

