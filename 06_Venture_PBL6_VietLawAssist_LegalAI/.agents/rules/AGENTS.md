# Agent Directives — VietLawAssist (VENTURE-06-PBL6)

> Đây là file DUY NHẤT agent cần đọc đầu tiên khi bắt đầu phiên làm việc với công ty này.
> Sau khi đọc xong, đọc tiếp [STATUS.md](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/STATUS.md) để biết trạng thái hiện tại.

---

## 1. IDENTITY

- **Tên dự án**: VietLawAssist — Hệ thống Trợ lý Thông minh Ôn thi Pháp luật Đại cương
- **Mã công ty**: `VENTURE-06-PBL6` | Khoa CNTT — ĐHBK Đà Nẵng (DUT)
- **Bản chất**: Đồ án Chuyên ngành PBL6 (Semester 7), nhóm 2 người, 15 tuần
- **Mục tiêu**: Đạt 10/10 Rubric DUT bằng hệ thống QA pháp luật RAG 4 tầng

## 2. CORE ARCHITECTURE — Pipeline 3 Khối + 4 Tầng ML

```
[User Query] → [Khối 1: Intent Router] → [Khối 2: Hybrid Retrieval] → [Khối 3: Template Generator] → [Output chuẩn barem]
```

| Tầng | Công nghệ | Vai trò |
|:---:|:---|:---|
| T1 | BM25Okapi + PyVi/Underthesea | Sparse keyword retrieval |
| T2 | PhoBERT `vietnamese-bi-encoder` + FAISS | Dense semantic retrieval |
| T3 | Qwen2.5-1.5B-Instruct (4-bit NF4) | RAG generation with Few-Shot CoT |
| T4 | LoRA Adapter (r=16, α=32) | Fine-tuned RAG on 500 Q&A pairs |

## 3. DOMAIN — 5 Dạng Đề thi PLĐC + Intent Codes

| Intent Code | Dạng đề thi | Mô tả ngắn |
|:---|:---|:---|
| `QPPL_STRUCTURE` | Phân tích QPPL | Tách Giả định / Quy định / Chế tài |
| `VPPL_ELEMENTS` | Phân tích VPPL | 4 yếu tố: Khách quan, Chủ quan, Khách thể, Chủ thể |
| `TRUE_FALSE` | Nhận định Đ/S | Kết luận + Giải thích + Trích dẫn luật |
| `CIVIL_INHERIT` | Chia thừa kế | Bước 5: Di sản → Di chúc → 2/3 suất → Thế vị → Chia |
| `CRIMINAL_AGE` | Tuổi TNHS | Đối chiếu Điều 9 + Điều 12 BLHS |
| `GENERAL_THEORY` | Lý thuyết chung | Khái niệm, so sánh, giải thích |

## 4. TECH STACK

- **Language**: Python 3.11
- **Backend**: FastAPI + Uvicorn + Pydantic v2
- **Database**: SQLite (WAL mode) — `Project/data/law_corpus.db`
- **ML/NLP**: `rank_bm25`, `sentence-transformers`, `transformers`, `peft`, `bitsandbytes`, `faiss-cpu`
- **Tokenizer**: `pyvi` (default) | `underthesea` (alternative)
- **Testing**: pytest + smoke tests
- **Hardware**: RTX 3050 4GB VRAM (budget ≤ 3.5GB)

## 5. HARD RULES (Bắt buộc tuân thủ)

1. **Random Seed**: `torch.manual_seed(42)`, `np.random.seed(42)` trong MỌI script ML
2. **VRAM Budget**: Tổng mô hình + index ≤ 3.5GB để fit RTX 3050 4GB
3. **SQL Safety**: 100% parameterized queries (`?` placeholder), KHÔNG BAO GIỜ nối chuỗi SQL
4. **No Hallucination**: Không bịa số Điều/Khoản — mọi trích dẫn phải verify từ DB
5. **Clean Architecture**: `api/routes/` → `services/` → `repositories/` → `core/` → `models/`
6. **Config via .env**: Zero secrets in code — dùng `pydantic_settings` + `.env`
7. **TDD Workflow**: RED → GREEN → REFACTOR cho mọi service mới

## 6. FILE MAP — Đọc gì khi nào

| Khi cần... | Đọc file |
|:---|:---|
| Hiểu dự án (ý tưởng, bài toán) | [`02_Domain_and_Specifications/01_PROJECT_CONCEPT.md`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/02_Domain_and_Specifications/01_PROJECT_CONCEPT.md) |
| Xem spec kỹ thuật (DB schema, API, VRAM) | [`02_Domain_and_Specifications/02_TECHNICAL_SPECIFICATIONS.md`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/02_Domain_and_Specifications/02_TECHNICAL_SPECIFICATIONS.md) |
| Xem barem 5 dạng đề + output mẫu | [`02_Domain_and_Specifications/03_EXAM_BAREM_TEMPLATES.md`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/02_Domain_and_Specifications/03_EXAM_BAREM_TEMPLATES.md) |
| Xem lộ trình 15 tuần | [`02_Domain_and_Specifications/04_PROJECT_ROADMAP.md`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/02_Domain_and_Specifications/04_PROJECT_ROADMAP.md) |
| Xem Rubric DUT (5 tiêu chí / 10đ) | [`01_Strategy_and_Proposal/02_DUT_RUBRICS_AND_SCHEDULE.md`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/01_Strategy_and_Proposal/02_DUT_RUBRICS_AND_SCHEDULE.md) |
| Tra cứu nguồn tài liệu học tập | [`01_Strategy_and_Proposal/03_CURRICULUM_AND_KNOWLEDGE_MAP.md`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/01_Strategy_and_Proposal/03_CURRICULUM_AND_KNOWLEDGE_MAP.md) |
| Xem đề xuất gốc (Full proposal) | [`01_Strategy_and_Proposal/01_PROJECT_PROPOSAL.md`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/01_Strategy_and_Proposal/01_PROJECT_PROPOSAL.md) |
| Xem code backend | [`Project/app/`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/Project/app/) |
| Xem tests | [`Project/tests/`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/Project/tests/) |
| Quy tắc an toàn AAP | [`antigravity-agent-protocol/RULES-SAFETY-GOVERNANCE.md`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/antigravity-agent-protocol/RULES-SAFETY-GOVERNANCE.md) |

## 7. AGENT TEAM (6 + Handmade)

| Mã | Vai trò | Trách nhiệm chính |
|:---|:---|:---|
| PM-01 | Project Manager | Lịch trình, milestone, báo cáo tiến độ |
| MLR-02 | ML Researcher | BM25, PhoBERT, RAG, LoRA pipeline |
| DE-03 | Data Engineer | Crawl, clean, DB schema, FAISS index |
| SA-04 | System Architect | FastAPI, Clean Architecture, API design |
| EVAL-05 | Evaluator | ROUGE-L, BERTScore, Citation Guardrail |
| RW-06 | Report Writer | Báo cáo đồ án, slide, demo script |
| Handmade | CEO (Sinh viên) | Quyết định tối cao, review, merge |
