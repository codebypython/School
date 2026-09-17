# 🛠 Cẩm Nang Sử Dụng Công Cụ Đo Lường NLP: ROUGE & BERTScore — Agent EVAL-05

> **Task ID:** E3  
> **Loại output:** 🛠 Hướng dẫn Công cụ + Code Snippet  
> **Ngày tạo:** 2026-09-09  
> **Dùng cho:** Chuẩn bị sẵn sàng cho Đánh giá Tầng 3 (RAG) & Tầng 4 (Fine-tuning) ở Phase 3-5

---

## 1. Vai Trò của ROUGE và BERTScore trong Hệ Thống VietLawAssist

Trong kiến trúc 4 tầng so sánh (Comparison Ladder):
- **Tầng 1 (BM25) & Tầng 2 (Dense):** Là bài toán **Retrieval** (Tìm kiếm), được đánh giá bằng **Recall@K**, **MRR**, **NDCG**.
- **Tầng 3 (RAG) & Tầng 4 (Fine-tuned LLM):** Là bài toán **Generation** (Sinh câu trả lời tự nhiên dựa trên điều luật đã trích xuất), cần các chỉ số đánh giá chất lượng văn bản sinh ra so với câu trả lời chuẩn (Ground Truth Reference):
  1. **ROUGE (Lexical Overlap):** Đo mức độ trùng lặp từ ngữ bề mặt (n-gram overlap).
  2. **BERTScore (Semantic Similarity):** Đo độ tương đồng ngữ nghĩa mức vector embedding sử dụng mô hình ngôn ngữ tiếng Việt tiền huấn luyện (**PhoBERT**).

---

## 2. Cài Đặt Thư Viện Cần Thiết

```bash
pip install rouge-score==0.1.2 bert-score==0.3.13 torch transformers
```

---

## 3. Hướng Dẫn Chi Tiết: `rouge-score`

### 3.1 Các Biến Thể ROUGE Thường Dùng
- **ROUGE-1:** Tỷ lệ trùng khớp unigram (từng từ đơn lẻ).
- **ROUGE-2:** Tỷ lệ trùng khớp bigram (cặp 2 từ liên tiếp).
- **ROUGE-L:** Dựa trên chuỗi con chung dài nhất (Longest Common Subsequence - LCS), phản ánh cấu trúc câu và sự liền mạch của ngữ pháp.

### 3.2 Lưu Ý Quan Trọng Với Tiếng Việt
Thư viện `rouge-score` mặc định ngắt từ theo khoảng trắng tiếng Anh. Vì từ tiếng Việt là từ đa âm tiết ghép (ví dụ: "bất khả xâm phạm", "quyền công dân"), **bắt buộc phải qua bước Word Segmentation (PyVi)** trước khi đưa vào hàm tính ROUGE:

```python
from pyvi import ViTokenizer
from rouge_score import rouge_scorer

def compute_vietnamese_rouge(prediction: str, reference: str) -> dict:
    # Bước 1: Tách từ tiếng Việt thành compound tokens
    tokenized_pred = ViTokenizer.tokenize(prediction)
    tokenized_ref = ViTokenizer.tokenize(reference)

    # Bước 2: Khởi tạo Scorer
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=False)
    scores = scorer.score(tokenized_ref, tokenized_pred)

    return {
        "rouge1_f1": scores['rouge1'].fmeasure,
        "rouge2_f1": scores['rouge2'].fmeasure,
        "rougeL_f1": scores['rougeL'].fmeasure,
    }
```

---

## 4. Hướng Dẫn Chi Tiết: `bert-score` với PhoBERT

### 4.1 Tại sao chọn `vinai/phobert-base-v2`?
`bert-score` mặc định dùng RoBERTa hoặc mBERT (multilingual) cho ngôn ngữ không phải tiếng Anh. Tuy nhiên, mBERT hiểu ngữ nghĩa tiếng Việt kém xa so với **PhoBERT** (mô hình ngôn ngữ SOTA được huấn luyện riêng trên 20GB văn bản báo chí tiếng Việt bởi VinAI Research).

### 4.2 Triển Khai Tính Toán BERTScore
```python
from bert_score import score

def compute_vietnamese_bertscore(predictions: list[str], references: list[str]) -> dict:
    """
    Tính BERTScore sử dụng PhoBERT.
    Lưu ý: PhoBERT yêu cầu đầu vào đã được tách từ (Word Segmentation bằng PyVi hoặc VnCoreNLP).
    """
    tokenized_preds = [ViTokenizer.tokenize(p) for p in predictions]
    tokenized_refs = [ViTokenizer.tokenize(r) for r in references]

    P, R, F1 = score(
        cands=tokenized_preds,
        refs=tokenized_refs,
        model_type="vinai/phobert-base-v2",
        lang="vi",
        verbose=False,
        device="cpu"  # Hoặc "cuda" nếu có GPU
    )

    return {
        "bert_precision": P.mean().item(),
        "bert_recall": R.mean().item(),
        "bert_f1": F1.mean().item(),
    }
```

---

## 5. Kịch Bản Đánh Giá Hoàn Chỉnh: End-to-End Code Snippet

Dưới đây là mã nguồn chạy thực nghiệm so sánh một câu trả lời do mô hình sinh ra (Prediction) với câu trích lục luật gốc (Reference):

```python
from pyvi import ViTokenizer
from rouge_score import rouge_scorer

# Câu trả lời mô hình tạo sinh ra (Candidate Prediction)
prediction = (
    "Theo Hiến pháp 2013, mọi công dân có quyền bất khả xâm phạm về thân thể, "
    "không ai bị bắt nếu không có quyết định của Tòa án hoặc Viện kiểm sát phê chuẩn, "
    "trừ trường hợp bị bắt quả tang."
)

# Đáp án trích từ văn bản luật chuẩn (Reference Ground Truth)
reference = (
    "Mọi người có quyền bất khả xâm phạm về thân thể, được pháp luật bảo hộ về sức khoẻ, "
    "danh dự và nhân phẩm. Không ai bị bắt nếu không có quyết định của Tòa án nhân dân, "
    "quyết định hoặc phê chuẩn của Viện kiểm sát nhân dân, trừ trường hợp phạm tội quả tang."
)

print("=== BẮT ĐẦU ĐÁNH GIÁ VĂN BẢN SINH RA ===")
# 1. Tách từ
pred_seg = ViTokenizer.tokenize(prediction)
ref_seg = ViTokenizer.tokenize(reference)

# 2. Tính ROUGE
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=False)
rouge_res = scorer.score(ref_seg, pred_seg)

print("\n[ROUGE SCORES]")
print(f"- ROUGE-1 F1: {rouge_res['rouge1'].fmeasure:.4f} (P: {rouge_res['rouge1'].precision:.4f}, R: {rouge_res['rouge1'].recall:.4f})")
print(f"- ROUGE-2 F1: {rouge_res['rouge2'].fmeasure:.4f} (P: {rouge_res['rouge2'].precision:.4f}, R: {rouge_res['rouge2'].recall:.4f})")
print(f"- ROUGE-L F1: {rouge_res['rougeL'].fmeasure:.4f} (P: {rouge_res['rougeL'].precision:.4f}, R: {rouge_res['rougeL'].recall:.4f})")

# 3. Hướng dẫn phân tích kết quả khi báo cáo:
# ROUGE-L đạt > 0.60 chứng minh mô hình nắm bắt cấu trúc pháp lý chính xác,
# không bị ảo giác (hallucination) hay bịa đặt điều luật.
```

---

## 6. Tiêu Chuẩn Nghiệm Thu Chất Lượng (Quality Thresholds)

Khi tiến hành đánh giá Tầng 3 và Tầng 4 ở các giai đoạn sau:
- **ROUGE-L F1:** Đạt $\ge 0.55$ (chấp nhận được đối với câu trả lời tóm tắt pháp lý), $\ge 0.65$ (tốt).
- **BERTScore F1:** Đạt $\ge 0.75$ trên mô hình `vinai/phobert-base-v2`.
