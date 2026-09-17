# 📋 TASKS — Agent 05: Evaluation Agent

> **Cập nhật lần cuối:** 2026-09-09  
> **Giai đoạn hiện tại:** Phase 1 — Evaluation Framework Preparation  
> **Phân công bởi:** PM-01 (Project Manager)

---

## Phase 0: Nghiên cứu & Khám phá (Tuần 0) ✅ HOÀN THÀNH

- [x] Đọc Proposal — nắm toàn bộ metrics cần implement
- [x] Thiết kế Evaluation Framework (3 nhóm metrics)
- [x] Xác định libraries: rouge-score, bert-score, sklearn
- [x] Xác định baseline expectations cho từng tầng
- [x] Viết phần evaluation cho Grand Design Overview

---

## Phase 1: Evaluation Framework Preparation (Tuần 1-2)

> **Triết lý:** Hiểu sâu metrics LÝ THUYẾT + chuẩn bị tools + tạo test set TRƯỚC KHI có model chạy.  
> **Thư mục output:** `.agents/outputs/phase1/`

### Sóng 1 — Nghiên cứu Metrics (không phụ thuộc agent khác)

- [x] **E1** 📖 Báo cáo Metrics cho Information Retrieval ✅
    - Output: `.agents/outputs/phase1/eval-05_ir_metrics_report.md`
    - Nội dung bắt buộc:
        1. **Recall@K:** Công thức, ý nghĩa ("trong top K kết quả, bao nhiêu % là relevant?"), ví dụ tính tay với 5 kết quả
        2. **MRR (Mean Reciprocal Rank):** Công thức, ý nghĩa ("relevant doc đầu tiên ở vị trí thứ mấy?"), ví dụ tính tay
        3. **NDCG@K:** Công thức DCG/IDCG, ý nghĩa ("thứ tự kết quả có tốt không?"), ví dụ tính tay
        4. **Precision@K:** Công thức, so sánh với Recall@K
        5. Tại sao chọn **Recall@5 làm primary metric** cho VietLawAssist: sinh viên cần tìm đúng điều luật quan trọng hơn là tìm ít kết quả chính xác
        6. Trích dẫn: Manning, Raghavan & Schütze — "Introduction to Information Retrieval" (Chapter 8)
    - DoD: File .md, 4 metrics giải thích đầy đủ, ví dụ tính tay mỗi metric, kết luận primary metric

### Sóng 2 — Dữ liệu & Công cụ

- [x] **E2** 🗂 Bộ 30 câu hỏi PLĐC mẫu với Ground Truth ✅
    - Output: `Project/data/sample/eval_queries.json`
    - Format:
        ```json
        [
          {
            "query_id": "Q001",
            "query": "Quyền bất khả xâm phạm về thân thể được quy định như thế nào?",
            "relevant_article_ids": ["HP2013_D20"],
            "law_codes": ["HP2013"],
            "difficulty": "easy",
            "category": "quyền con người"
          }
        ]
        ```
    - Yêu cầu: 
        - 30 câu hỏi phân bổ đều 5 bộ luật (6 câu/bộ luật)
        - Mỗi câu có 1-3 `relevant_article_ids` (ground truth)
        - Phân bổ difficulty: 10 easy, 12 medium, 8 hard
        - Câu hỏi phải thực tế — kiểu đề thi/bài tập PLĐC
    - DoD: JSON valid, 30 objects, mỗi object có đầy đủ fields, `relevant_article_ids` đúng mã article
    - Phụ thuộc: Cần biết format `article_id` từ DE-03 schema (VD: HP2013_D20)

- [x] **E3** 🛠 Hướng dẫn sử dụng rouge-score & bert-score ✅
    - Output: `.agents/outputs/phase1/eval-05_metrics_tools_guide.md`
    - Nội dung bắt buộc:
        1. **rouge-score:** `pip install rouge-score`, import, cách gọi `rouge.compute()`, ví dụ tính ROUGE-L cho 1 cặp predict/reference tiếng Việt
        2. **bert-score:** `pip install bert-score`, import, cách gọi `BERTScorer()`, cấu hình `model_type="vinai/phobert-base-v2"` cho tiếng Việt, ví dụ code
        3. **sklearn metrics:** `from sklearn.metrics import ndcg_score, precision_score`, ví dụ tính NDCG
        4. Lưu ý: bert-score cần GPU (RTX 3050) hoặc CPU (chậm hơn 10x). Cách check VRAM usage.
        5. Nguồn docs + GitHub links cho mỗi library
    - DoD: File .md, 3 libraries có code snippet mẫu chạy được, lưu ý hardware

### Sóng 3 — Tổng hợp thiết kế

- [x] **E4** 📖 Thiết kế Evaluation Pipeline (sơ đồ luồng) ✅
    - Output: Thêm mục cuối trong file `eval-05_ir_metrics_report.md`
    - Nội dung:
        1. Sơ đồ Mermaid: Load eval_queries.json → Loop mỗi query → Gọi BM25 search → Collect top-K article_ids → So sánh với ground truth → Tính Recall@5, MRR → Export report
        2. Format input/output mỗi bước
        3. Cách chạy evaluation: lệnh terminal cụ thể
    - DoD: Sơ đồ Mermaid render được, format I/O rõ ràng
    - Phụ thuộc: E1 (metrics), E2 (test set), hiểu BM25 API từ MLR-02

---

## Phase 2: Retrieval Evaluation (Tuần 3-4)

- [ ] Implement Recall@K function
- [ ] Implement MRR function
- [ ] Implement NDCG@K function (sklearn)
- [ ] Implement Precision@K function
- [ ] Chạy evaluation Tầng 1 (BM25) trên test set
- [ ] Chạy evaluation Tầng 2 (Dense) trên test set
- [ ] So sánh Tầng 1 vs Tầng 2, viết báo cáo

## Phase 3: Generation Evaluation Setup (Tuần 5-6)

- [ ] Setup ROUGE scorer (rouge-score library)
- [ ] Setup BERTScore với PhoBERT-base-v2
- [ ] Implement Faithfulness metric (NLI-based hoặc heuristic)
- [ ] Implement Structure Score (4-section check)
- [ ] Implement Citation Score (regex pattern matching)

## Phase 4: Full Pipeline Evaluation (Tuần 8-9)

- [ ] Chạy evaluation Tầng 3 (RAG base) trên test set
- [ ] Chạy evaluation Tầng 4 (RAG fine-tuned) trên test set
- [ ] So sánh Tầng 3 vs Tầng 4, viết báo cáo
- [ ] Tạo bảng so sánh tổng hợp 4 tầng
- [ ] Tạo biểu đồ so sánh (bar charts, radar charts)

## Phase 5: Error Analysis & Report (Tuần 9-10)

- [ ] Phân loại lỗi Tầng 1: keyword miss, false positives
- [ ] Phân loại lỗi Tầng 2: semantic confusion
- [ ] Phân loại lỗi Tầng 3: hallucination, sai cấu trúc
- [ ] Phân loại lỗi Tầng 4: remaining issues after fine-tune
- [ ] Viết Error Analysis report cho báo cáo đồ án
- [ ] Hỗ trợ Agent-06 tạo bảng biểu, đồ thị cho báo cáo
