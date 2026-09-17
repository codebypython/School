# 📋 TASKS — Agent 04: System Architect Agent

> **Cập nhật lần cuối:** 2026-09-09  
> **Giai đoạn hiện tại:** Phase 1 — Backend Foundation  
> **Phân công bởi:** PM-01 (Project Manager)

---

## Phase 0: Nghiên cứu & Khám phá (Tuần 0) ✅ HOÀN THÀNH

- [x] Đọc Proposal — nắm kiến trúc hệ thống tổng thể
- [x] Xác định tech stack: FastAPI + React + SQLite + Nginx + Docker
- [x] Thiết kế API endpoints (4 routes chính)
- [x] Thiết kế component diagram: Frontend ↔ Backend ↔ ML ↔ DB
- [x] Viết phần kiến trúc cho Grand Design Overview

---

## Phase 1: Backend Foundation (Tuần 1-2)

> **Triết lý:** Tài liệu hóa kiến trúc + hướng dẫn sử dụng tech stack, bên cạnh code đã tạo.  
> **Thư mục output:** `.agents/outputs/phase1/`  
> **Ghi chú:** Code backend đã được tạo trong Phase 0→1 (12 files trong `Project/`). Phase 1 tasks tập trung vào tài liệu hóa, giải thích, và hướng dẫn.

### Sóng 1 — Tài liệu hóa kiến trúc (không phụ thuộc agent khác)

- [x] **S1** 📖 Báo cáo Kiến trúc Clean Architecture ✅
    - Output: `.agents/outputs/phase1/sa-04_architecture_report.md`
    - Nội dung bắt buộc:
        1. Clean Architecture là gì? (trích dẫn Robert C. Martin / "Uncle Bob")
        2. 3 tầng trong VietLawAssist: Router/Controller → Service → Repository → DB
        3. Sơ đồ phân tầng (Mermaid) mapping cụ thể vào files đã tạo
        4. Tại sao chọn pattern này cho dự án ML: tách biệt ML logic khỏi HTTP logic
        5. Luồng xử lý 1 request cụ thể: `POST /api/retrieve` → đi qua từng tầng như thế nào
        6. Dependency Injection trong FastAPI: `Depends()` dùng ở đâu, tại sao
    - DoD: File .md, có sơ đồ Mermaid, có mapping files, có ví dụ luồng request

### Sóng 2 — Hướng dẫn sử dụng (dựa trên code đã tạo)

- [x] **S2** 🛠 Hướng dẫn Setup & Chạy dự án ✅
    - Output: `.agents/outputs/phase1/sa-04_setup_guide.md`
    - Nội dung bắt buộc:
        1. Prerequisites: Python 3.10+, pip, git
        2. Clone repo: `git clone https://github.com/codebypython/PBL6.git`
        3. Tạo virtual environment: `python -m venv venv` + activate
        4. Install dependencies: `pip install -r requirements.txt`
        5. Copy env: `cp .env.example .env`
        6. Chạy server: `uvicorn app.main:app --reload --port 8000`
        7. Test health: `curl http://localhost:8000/api/health`
        8. Truy cập Swagger docs: `http://localhost:8000/docs`
        9. Troubleshooting: port conflict, missing module, .env errors
    - DoD: File .md, step-by-step có expected output mỗi bước, troubleshooting 3+ lỗi phổ biến

- [x] **S4** 🛠 Hướng dẫn Tech Stack (FastAPI + SQLite + Pydantic) ✅
    - Output: `.agents/outputs/phase1/sa-04_tech_stack_guide.md`
    - Nội dung bắt buộc:
        1. **FastAPI:** Tạo router, define endpoint, async/await, request validation, response model, lifespan events. Link docs: https://fastapi.tiangolo.com
        2. **SQLite + sqlite3:** Connection, cursor, parameterized queries (chống SQL injection), context manager. Link docs: https://docs.python.org/3/library/sqlite3.html
        3. **Pydantic v2:** BaseModel, Field (validators, examples, description), BaseSettings, model_config. Link docs: https://docs.pydantic.dev/latest/
        4. **Loguru:** Cách import, logger.info/warning/error/success, cấu hình file rotation. Link: https://github.com/Delgan/loguru
        5. Mỗi mục kèm: code snippet mẫu lấy từ codebase VietLawAssist + link docs chính thức
    - DoD: File .md, 4 mục đầy đủ, mỗi mục có code snippet + link docs

### Sóng 3 — Tổng hợp

- [x] **S3** 📖 Bản đồ Code hiện tại (Code Map) ✅
    - Output: `.agents/outputs/phase1/sa-04_code_map.md`
    - Nội dung:
        1. Cây thư mục `Project/` đầy đủ (tree output)
        2. Mỗi file: mục đích 1 dòng, agent tạo ra, dependencies (imports), số dòng code
        3. Sơ đồ import graph: module nào import module nào (Mermaid)
        4. Files còn thiếu cần tạo thêm (từ approved plan)
    - DoD: File .md, liệt kê MỌI file hiện có, sơ đồ import graph Mermaid
    - Phụ thuộc: S1 (hiểu kiến trúc trước khi map code)

---

## Phase 2: Frontend Foundation & API Integration (Tuần 3-4)

- [ ] Khởi tạo React project (Vite hoặc CRA)
- [ ] Build Query Input component (textarea + submit)
- [ ] Build basic Results Display component
- [ ] Connect frontend → backend API
- [ ] Implement Comparison View (4 tabs hoặc side-by-side)

## Phase 3: ML Integration (Tuần 5-6)

- [ ] Integrate BM25Index service vào `/api/retrieve`
- [ ] Integrate FAISSIndex service vào `/api/retrieve`
- [ ] Integrate RAG pipeline vào `/api/generate`
- [ ] Implement `/api/compare` — orchestrate all 4 approaches
- [ ] Handle async long-running inference (loading states)

## Phase 4: Metrics & Dashboard (Tuần 7-8)

- [ ] Implement `/api/evaluate` endpoint
- [ ] Build Metrics Dashboard component (ROUGE-L, BERTScore, charts)
- [ ] Build Law Article Panel (retrieved docs with highlight)
- [ ] Integrate fine-tuned model endpoint

## Phase 5: Testing & Optimization (Tuần 9-10)

- [ ] Write Artillery load test scripts
- [ ] Write Selenium E2E test scripts
- [ ] Run load tests, collect performance metrics
- [ ] Server optimization: caching, connection pooling
- [ ] Polish UI: error handling, loading states, responsive

## Phase 6: Deployment & Documentation (Tuần 11-15)

- [ ] Docker Compose for full stack (frontend + backend + nginx)
- [ ] Write deployment README
- [ ] Final server deployment
- [ ] Hỗ trợ Agent-06 viết phần hệ thống trong báo cáo
