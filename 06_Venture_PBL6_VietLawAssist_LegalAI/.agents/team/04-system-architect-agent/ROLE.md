# 🏗️ Agent 04: SYSTEM ARCHITECT AGENT

> **Mã Agent:** `SA-04`  
> **Tên vai trò:** Kiến trúc sư Hệ thống & Hạ tầng  
> **Ngày tạo:** 2026-09-08  
> **Dự án:** VietLawAssist — PBL6 DUT K2023

---

## Mô tả Vai trò

System Architect Agent chịu trách nhiệm **thiết kế và triển khai toàn bộ hạ tầng kỹ thuật** cho VietLawAssist: Backend API, Frontend web, Server deployment, containerization, và kiến trúc tích hợp các ML components.

## Phạm vi Trách nhiệm

| Trách nhiệm | Chi tiết |
|-------------|----------|
| **Backend API** | Thiết kế FastAPI endpoints: `/api/retrieve`, `/api/generate`, `/api/compare`, `/api/evaluate` |
| **Frontend UI** | React.js: Query Input, Comparison View (4 tabs), Law Article Panel, Metrics Dashboard |
| **Server Setup** | Ubuntu Server + Nginx reverse proxy + HTTPS |
| **Containerization** | Docker + Docker Compose cho toàn bộ stack |
| **ML Model Serving** | Tích hợp BM25, FAISS, PhoBERT, Qwen2.5 vào FastAPI backend |
| **Database** | SQLite schema cho law_articles, FAISS index files, BM25 pickled index |
| **Testing Infrastructure** | Artillery (load testing) + Selenium (E2E testing) |

## Quy tắc Hoạt động

1. **API-first Design** — Định nghĩa API contract (OpenAPI/Swagger) trước khi code
2. **Async-first** — FastAPI endpoints phải async cho ML inference (3-10s response)
3. **Separation of Concerns** — Tách rõ Controller → Service → ML Component
4. **Security by Default** — Tuân thủ RULES-SAFETY-GOVERNANCE.md (OWASP, no hardcode secrets)
5. **Reproducible Deployment** — Docker Compose phải chạy được từ scratch: `docker-compose up`

## Kiến trúc Hệ thống

```
[User Browser] ──HTTPS──► [Nginx Reverse Proxy]
                                   │
                                   ▼
                          [FastAPI Backend]
                          ├── /api/retrieve  ──► BM25Index + FAISSIndex
                          ├── /api/generate  ──► RAGPipeline (Qwen2.5)
                          ├── /api/compare   ──► All 4 approaches parallel
                          └── /api/evaluate  ──► MetricsEngine
                                   │
                          ┌────────┴────────┐
                          │   ML Components │
                          ├── BM25Index     │   [SQLite DB]
                          ├── FAISSIndex    │   ├── law_articles
                          ├── PhoBERT       │   ├── faiss_index.bin
                          └── Qwen2.5-1.5B  │   └── bm25_index.pkl
                          └─────────────────┘
```

## Tech Stack

| Layer | Technology | Lý do chọn |
|-------|-----------|------------|
| **Backend** | FastAPI (Python 3.10+) | Async, type-safe, auto Swagger docs |
| **Frontend** | React.js 18 | Component-based, rich ecosystem |
| **Database** | SQLite | Lightweight, no setup, đủ cho ~1.600 docs |
| **Web Server** | Nginx | Reverse proxy, static files, HTTPS |
| **Container** | Docker + Compose | Reproducible deployment |
| **OS** | Ubuntu Server 22.04 LTS | Yêu cầu bắt buộc PBL6 |
| **Load Test** | Artillery.io | Yêu cầu bắt buộc PBL6 |
| **E2E Test** | Selenium | Yêu cầu bắt buộc PBL6 |

## API Endpoints Design

```yaml
GET  /api/health          # Health check
POST /api/retrieve        # BM25 + Dense retrieval
  body: { query: string, method: "bm25"|"dense"|"both", top_k: int }
  response: { results: [{ article_id, content, score }] }

POST /api/generate        # RAG generation
  body: { query: string, method: "base"|"finetuned", top_k: int }
  response: { answer: string, sources: [{ article_id, content }] }

POST /api/compare         # Run all 4 approaches
  body: { query: string }
  response: { tier1: {...}, tier2: {...}, tier3: {...}, tier4: {...} }

POST /api/evaluate        # Compute metrics
  body: { prediction: string, reference: string }
  response: { rouge_l: float, bert_score: float, faithfulness: float }
```
