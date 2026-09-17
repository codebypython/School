# 🏛️ GRAND DESIGN OVERVIEW — VietLawAssist

> **Dự án:** VietLawAssist — Hệ thống Hỗ trợ Tra cứu Luật và Sinh Câu trả lời Chuẩn cấu trúc  
> **Trường:** Đại học Bách Khoa Đà Nẵng (DUT) | **Học phần:** PBL6 Đồ án chuyên ngành  
> **Nhóm:** 2 sinh viên K2023 | **Thời gian:** 15 tuần  
> **Phần cứng:** RTX 3050 4GB + Google Colab T4  
> **Tổng hợp bởi:** Agent Team — Phase 0 Research | **Ngày:** 2026-09-08

---

## I. TUYÊN BỐ VẤN ĐỀ & GIẢI PHÁP

### Vấn đề
Học phần **Pháp luật Đại cương** bắt buộc cho ~100% sinh viên ĐH Việt Nam. Sinh viên gặp khó khăn:
- Không biết điều luật nào áp dụng cho tình huống
- Viết sai cấu trúc bài làm (thiếu khái niệm, ví dụ, trích dẫn)
- Tra cứu thủ công qua hàng trăm điều luật mất thời gian

**→ Hậu quả:** Điểm thấp vì sai cấu trúc, không phải vì thiếu kiến thức.

### Giải pháp
Hệ thống web cho phép sinh viên nhập câu hỏi PLĐC → hệ thống **tự động tìm điều luật + sinh câu trả lời** theo đúng cấu trúc rubric, so sánh **4 phương pháp ML** khác nhau.

### Đối tượng
- **Primary:** Sinh viên năm 1-2 đang học PLĐC (~100 SV DUT K2023)
- **Secondary:** Giáo viên/Trợ giảng PLĐC

---

## II. KIẾN TRÚC CẦU THANG 4 TẦNG (COMPARISON LADDER)

> *Output từ Agent-02 (ML Research) — Trái tim kỹ thuật của dự án*

```mermaid
graph TD
    subgraph INPUT
        Q["📝 Câu hỏi PLĐC<br/>'Phân tích quyền bất khả xâm phạm<br/>về thân thể'"]
    end

    subgraph TIER1["🔵 TẦNG 1 — BM25 Sparse Retrieval"]
        T1A["Vietnamese Tokenizer<br/>(underthesea)"] --> T1B["BM25Okapi<br/>Keyword Matching"]
        T1B --> T1C["Top-5 Articles<br/>⚡ <50ms | CPU only"]
    end

    subgraph TIER2["🟡 TẦNG 2 — PhoBERT Dense Retrieval"]
        T2A["PhoBERT Encoder<br/>(vietnamese-bi-encoder)"] --> T2B["FAISS Index<br/>Cosine Similarity"]
        T2B --> T2C["Top-5 Articles<br/>⚡ <200ms | ~1GB VRAM"]
    end

    subgraph TIER3["🟠 TẦNG 3 — RAG Base"]
        T3A["Dense Retrieval<br/>Top-5 docs"] --> T3B["Qwen2.5-1.5B<br/>4-bit Quantization"]
        T3B --> T3C["Structured Answer<br/>⏱️ 3-8s | ~1.2GB VRAM"]
    end

    subgraph TIER4["🔴 TẦNG 4 — RAG Fine-tuned"]
        T4A["Dense Retrieval<br/>Top-5 docs"] --> T4B["Qwen2.5-1.5B + LoRA<br/>Fine-tuned on PLĐC"]
        T4B --> T4C["Better Answer<br/>⏱️ 4-10s | Colab T4"]
    end

    Q --> T1A
    Q --> T2A
    Q --> T3A
    Q --> T4A

    T1C --> COMPARE["📊 Comparison Dashboard<br/>Side-by-side 4 methods"]
    T2C --> COMPARE
    T3C --> COMPARE
    T4C --> COMPARE
```

### Lý thuyết Mỗi Tầng

| Tầng | Phương pháp | Nguyên lý | Ưu điểm | Hạn chế |
|:----:|------------|----------|---------|---------|
| **1** | BM25 (Sparse) | Keyword overlap, TF-IDF scoring | Cực nhanh, không cần GPU | Không hiểu từ đồng nghĩa |
| **2** | PhoBERT + FAISS (Dense) | Semantic embedding → cosine similarity | Hiểu ngữ nghĩa tiếng Việt | Không sinh câu trả lời |
| **3** | RAG = Dense + Qwen2.5 | Retrieve docs → augment prompt → generate | Sinh câu trả lời có cấu trúc | Đôi khi hallucinate |
| **4** | RAG + LoRA Fine-tuned | Domain adaptation cho PLĐC | Cấu trúc chuẩn, trích dẫn đúng | Cần training data |

### Câu chuyện Tiến hóa (Dùng cho Q&A Hội đồng)

> *"BM25 chỉ tìm từ khóa → miss từ đồng nghĩa (Recall@5 ~58%). PhoBERT dense retrieval nắm ngữ nghĩa → Recall@5 ~78%. Dense retrieval không sinh câu trả lời → thêm Qwen2.5 RAG pipeline. LoRA fine-tune giúp model biết cấu trúc đáp án → BERTScore 0.75→0.82, trích dẫn đúng 65%→88%."*

---

## III. DATA STRATEGY

> *Output từ Agent-03 (Data Engineer)*

### A. Corpus Pháp luật (~1.588 điều)

| Bộ luật | Số điều | Nguồn | Effort |
|---------|:------:|-------|:------:|
| Hiến pháp 2013 | 120 | vbpl.vn | 0.5 ngày |
| Bộ luật Dân sự 2015 | 689 | thuvienphapluat.vn | 1 ngày |
| Bộ luật Hình sự 2015 (sửa đổi 2017) | 426 | thuvienphapluat.vn | 1 ngày |
| Luật Hôn nhân & Gia đình 2014 | 133 | vbpl.vn | 0.5 ngày |
| Luật Lao động 2019 | 220 | vbpl.vn | 0.5 ngày |
| **Tổng** | **~1.588** | | **~3.5 ngày** |

**Chunking:** 1 điều luật = 1 document (giữ nguyên ngữ cảnh pháp lý)

### B. Q&A Fine-tuning Dataset (~500 cặp)

| Nguồn | Số cặp | Effort |
|-------|:------:|:------:|
| Đề thi PLĐC các trường ĐH | ~150 | 1 ngày |
| Giáo trình PLĐC (NXB CTQG) | ~100 | 1 ngày |
| Tự tạo từ điều luật quan trọng | ~250 | 2 ngày |
| **Tổng** | **~500** | **~4 ngày** |

**Format:** Alpaca (`instruction` / `input` / `output`)

### C. Evaluation Test Set (100 câu)
- 100 câu hỏi PLĐC điển hình + đáp án chuẩn cấu trúc 4 phần
- Split: 70 train / 30 test (không overlap)
- Ground truth retrieval annotations

---

## IV. KIẾN TRÚC HỆ THỐNG

> *Output từ Agent-04 (System Architect)*

```mermaid
graph TB
    subgraph CLIENT["🌐 Client Layer"]
        BROWSER["User Browser"]
    end

    subgraph FRONTEND["⚛️ Frontend — React.js 18"]
        UI_QUERY["Query Input"]
        UI_COMPARE["Comparison View<br/>(4 tabs / side-by-side)"]
        UI_ARTICLES["Law Article Panel<br/>(highlighted docs)"]
        UI_METRICS["Metrics Dashboard<br/>(charts & scores)"]
    end

    subgraph BACKEND["⚡ Backend — FastAPI (Python 3.10)"]
        API_RETRIEVE["/api/retrieve"]
        API_GENERATE["/api/generate"]
        API_COMPARE["/api/compare"]
        API_EVALUATE["/api/evaluate"]
    end

    subgraph ML["🧠 ML Components"]
        BM25["BM25Index<br/>(rank_bm25)"]
        FAISS["FAISSIndex<br/>(faiss + embeddings)"]
        PHOBERT["PhoBERT Encoder<br/>(sentence-transformers)"]
        QWEN_BASE["Qwen2.5-1.5B<br/>(4-bit quantized)"]
        QWEN_LORA["Qwen2.5-1.5B + LoRA<br/>(fine-tuned)"]
    end

    subgraph STORAGE["💾 Storage"]
        SQLITE["SQLite<br/>law_articles table"]
        FAISS_FILE["FAISS Index<br/>.bin file"]
        BM25_FILE["BM25 Index<br/>.pkl file"]
    end

    subgraph INFRA["🖥️ Infrastructure"]
        NGINX["Nginx<br/>Reverse Proxy + HTTPS"]
        UBUNTU["Ubuntu Server 22.04"]
        DOCKER["Docker Compose"]
    end

    BROWSER -->|HTTPS| NGINX
    NGINX --> FRONTEND
    FRONTEND -->|REST API| BACKEND
    API_RETRIEVE --> BM25
    API_RETRIEVE --> FAISS
    FAISS --> PHOBERT
    API_GENERATE --> QWEN_BASE
    API_GENERATE --> QWEN_LORA
    API_COMPARE --> API_RETRIEVE
    API_COMPARE --> API_GENERATE
    BM25 --> BM25_FILE
    FAISS --> FAISS_FILE
    BM25 --> SQLITE
    FAISS --> SQLITE
    DOCKER --> UBUNTU
```

### API Endpoints

| Method | Endpoint | Chức năng | Response Time |
|:------:|----------|----------|:------------:|
| POST | `/api/retrieve` | BM25 + Dense retrieval | <200ms |
| POST | `/api/generate` | RAG text generation | 3-10s |
| POST | `/api/compare` | Chạy cả 4 approaches | 10-30s |
| POST | `/api/evaluate` | Tính ROUGE-L, BERTScore | <2s |
| GET | `/api/health` | Health check | <50ms |

### Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React.js 18, TanStack Query |
| Backend | FastAPI, Python 3.10+ |
| ML | PyTorch, transformers, PEFT, TRL |
| Database | SQLite |
| Search | FAISS, rank_bm25 |
| Server | Ubuntu 22.04, Nginx, Docker |
| Testing | Artillery (load), Selenium (E2E) |

---

## V. EVALUATION FRAMEWORK

> *Output từ Agent-05 (Evaluation)*

### Metrics Matrix

| Metric | Tầng 1 | Tầng 2 | Tầng 3 | Tầng 4 | Loại |
|--------|:------:|:------:|:------:|:------:|:----:|
| **Recall@5** | ~55-60% | ~75-80% | ~75-80% | ~80-85% | Retrieval |
| **MRR** | ~0.42 | ~0.65 | ~0.65 | ~0.70 | Retrieval |
| **ROUGE-L** | N/A | N/A | ~0.40-0.50 | ~0.58-0.68 | Generation |
| **BERTScore** | N/A | N/A | ~0.75 | ~0.82 | Generation |
| **Faithfulness** | N/A | N/A | ~70% | ~85% | Generation |
| **Structure Score** | ❌ | ❌ | ~60% | ~90%+ | Custom |
| **Citation Score** | ❌ | Có ref | ~65% | ~88% | Custom |

### Evaluation Pipeline

```mermaid
graph LR
    TESTSET["Test Set<br/>(100 câu hỏi)"] --> TIER["Chạy 4 Tầng"]
    TIER --> RETRIEVAL["Retrieval Metrics<br/>Recall@K, MRR, NDCG"]
    TIER --> GENERATION["Generation Metrics<br/>ROUGE-L, BERTScore"]
    TIER --> CUSTOM["Custom Metrics<br/>Structure, Citation"]
    RETRIEVAL --> COMPARE["Comparison Table<br/>+ Bar Charts"]
    GENERATION --> COMPARE
    CUSTOM --> COMPARE
    COMPARE --> ERROR["Error Analysis<br/>Phân loại lỗi"]
    ERROR --> REPORT["Báo cáo<br/>Chương 5"]
```

---

## VI. RISK MATRIX

| # | Rủi ro | Xác suất | Impact | Giải pháp |
|:-:|--------|:--------:|:------:|-----------|
| 1 | Qwen2.5 hallucinate điều luật | 🔴 Cao | 🔴 Cao | Faithfulness check + warning UI |
| 2 | Colab T4 hết quota fine-tune | 🟡 TB | 🟡 TB | Backup: Kaggle GPU (30h/tuần) |
| 3 | Crawl bị block | 🟢 Thấp | 🟡 TB | PDF từ website Chính phủ |
| 4 | Dataset 500 cặp chất lượng kém | 🟡 TB | 🔴 Cao | Peer review + GPT validate format |
| 5 | LoRA không cải thiện đáng kể | 🟢 Thấp | 🟡 TB | Nhấn mạnh citation + structure score |
| 6 | `/api/compare` timeout (30s+) | 🟡 TB | 🟡 TB | Async processing + loading UI |

---

## VII. TIMELINE 15 TUẦN

```mermaid
gantt
    title VietLawAssist — Timeline 15 tuần
    dateFormat YYYY-MM-DD
    axisFormat %V

    section Data
    Crawl & Clean Corpus        :a1, 2026-09-08, 14d
    Q&A Dataset Creation        :a2, after a4, 14d

    section ML Pipeline
    BM25 Implementation         :a3, 2026-09-15, 7d
    Dense Retrieval (PhoBERT)   :a4, after a3, 14d
    RAG Pipeline (Qwen2.5)     :a5, after a4, 14d
    LoRA Fine-tuning            :a6, after a5, 14d

    section System
    FastAPI + React Setup       :b1, 2026-09-08, 14d
    API Integration             :b2, after b1, 14d
    Frontend Polish             :b3, after b2, 28d

    section Evaluation
    Retrieval Evaluation        :c1, after a4, 7d
    Full Evaluation (4 tầng)   :c2, after a6, 14d
    Error Analysis              :c3, after c2, 7d

    section Testing
    Artillery Load Test         :d1, after c2, 7d
    Selenium E2E Test           :d2, after c2, 7d

    section Report
    Báo cáo tiến độ 1          :milestone, 2026-10-06, 0d
    Báo cáo tiến độ 2          :milestone, 2026-11-17, 0d
    Viết báo cáo đồ án         :e1, 2026-11-17, 21d
    Slide bảo vệ               :e2, after e1, 7d
    BẢO VỆ                     :milestone, 2026-12-22, 0d
```

---

## VIII. RUBRIC ALIGNMENT — ĐẢM BẢO 9-10/10

| Tiêu chí DUT | Điểm | Cách đáp ứng | Agent phụ trách |
|-------------|:----:|-------------|:--------------:|
| **Tính cấp thiết (1đ)** | 1/1 | PLĐC bắt buộc cho 100% SV VN, nhu cầu rõ ràng | PM-01 |
| **Kết quả nhiệm vụ (3đ)** | 2.5-3 | End-to-end system, demo live, 4 tầng hoạt động | SA-04, MLR-02 |
| **Am hiểu giải pháp (2đ)** | 1.8-2 | Bảng so sánh 4 phương pháp + lý thuyết từng tầng | MLR-02, EVAL-05 |
| **Chất lượng báo cáo (2đ)** | 1.8-2 | Lý thuyết + bảng metric + đồ thị + trích dẫn | RW-06 |
| **Thuyết trình & Demo (2đ)** | 1.8-2 | Chat live PLĐC, side-by-side comparison | RW-06, SA-04 |

---

## IX. AGENT TEAM — PHÂN CÔNG & TRÁCH NHIỆM

```mermaid
graph TB
    PM["🎯 PM-01<br/>Project Manager<br/>Điều phối tổng thể"]

    MLR["🧠 MLR-02<br/>ML Research<br/>4 tầng ML pipeline"]

    DE["🗄️ DE-03<br/>Data Engineer<br/>Corpus + Dataset"]

    SA["🏗️ SA-04<br/>System Architect<br/>Backend + Frontend"]

    EVAL["📊 EVAL-05<br/>Evaluation<br/>Metrics framework"]

    RW["📝 RW-06<br/>Report Writer<br/>Báo cáo + Slide"]

    PM --> MLR
    PM --> DE
    PM --> SA
    PM --> EVAL
    PM --> RW

    MLR -->|"Lý thuyết"| RW
    DE -->|"Data"| MLR
    DE -->|"Schema"| SA
    SA -->|"API specs"| MLR
    EVAL -->|"Metrics"| RW
    SA -->|"Test results"| RW

    style PM fill:#e74c3c,color:#fff
    style MLR fill:#3498db,color:#fff
    style DE fill:#2ecc71,color:#fff
    style SA fill:#f39c12,color:#fff
    style EVAL fill:#9b59b6,color:#fff
    style RW fill:#1abc9c,color:#fff
```

| Agent | Tương ứng Người | Chuyên trách |
|-------|:--------------:|-------------|
| PM-01 | Cả 2 | Điều phối timeline, milestone tracking |
| MLR-02 | Người A (ML) | BM25 → Dense → RAG → LoRA |
| DE-03 | Người A (ML) | Crawl corpus, tạo dataset |
| SA-04 | Người B (System) | FastAPI, React, Docker, Nginx |
| EVAL-05 | Người A (ML) | ROUGE, BERTScore, Faithfulness |
| RW-06 | Cả 2 | Báo cáo, slide bảo vệ |

---

## X. ĐIỂM ĐỘC ĐÁO — TẠI SAO ĐỀ TÀI NÀY KHÁC BIỆT

| Đề tài RAG thông thường | VietLawAssist |
|------------------------|---------------|
| 1 phương pháp duy nhất | **4 tầng so sánh có hệ thống** |
| Không metric rõ ràng | **7 metrics: Recall@K + MRR + ROUGE-L + BERTScore + Faithfulness + Structure + Citation** |
| Domain chung | **Domain cực hẹp: PLĐC cho SV Việt Nam** |
| Chỉ retrieve hoặc chỉ generate | **Retrieve + Generate + Evaluate + Compare** |
| Prompt engineering | **LoRA Fine-tune + Evaluation framework đầy đủ** |
| Không ground truth | **Test set 100 câu với đáp án chuẩn** |

---

> **📌 Tài liệu này là bản đại thiết kế tổng quan (Grand Design Overview) được tổng hợp từ Phase 0 Research của toàn bộ đội ngũ 6 AI Agents. Mọi thay đổi lớn trong quá trình triển khai sẽ được cập nhật tại đây.**

*VietLawAssist Grand Design | Agent Team Output | 2026-09-08 | PBL6 DUT K2023*
