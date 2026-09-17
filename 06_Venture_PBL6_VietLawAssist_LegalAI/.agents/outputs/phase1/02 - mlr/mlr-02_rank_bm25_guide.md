# 🛠 Hướng Dẫn Sử Dụng Thư Viện rank-bm25 — Agent MLR-02

> **Task ID:** M4  
> **Loại output:** 🛠 Hướng dẫn Công cụ  
> **Ngày tạo:** 2026-09-09  
> **Dùng cho:** Tài liệu triển khai BM25 Service + Hướng dẫn kỹ thuật bảo vệ đồ án

---

## 1. Giới thiệu Thư viện `rank-bm25`

`rank-bm25` là thư viện Python mã nguồn mở gọn nhẹ, cung cấp các thuật toán chấm điểm xếp hạng BM25 thuần Python (pure-Python), được xây dựng trên nền tảng NumPy nhằm tối ưu hóa tốc độ tính toán vector.

- **Tác giả:** Dorian Brown
- **GitHub Repository:** [https://github.com/dorianbrown/rank_bm25](https://github.com/dorianbrown/rank_bm25)
- **Các thuật toán hỗ trợ:**
  - `BM25Okapi` (Mặc định trong VietLawAssist)
  - `BM25L`
  - `BM25Plus`

---

## 2. Cài đặt & Yêu cầu Môi trường

Cài đặt thông qua `pip` trong môi trường virtual environment của dự án:

```bash
pip install rank-bm25==0.2.2
```

Dependencies đi kèm:
- `numpy >= 1.14.0`

Kiểm tra cài đặt thành công:
```python
import rank_bm25
print(rank_bm25.__version__)  # Expected: 0.2.2
```

---

## 3. Chi tiết API Reference của `BM25Okapi`

### 3.1 Khởi tạo Object
```python
from rank_bm25 import BM25Okapi

bm25 = BM25Okapi(corpus, k1=1.5, b=0.75, epsilon=0.25)
```
- **`corpus`** (`List[List[str]]`): Tập dữ liệu dạng ma trận danh sách các tokens đã được tiền xử lý (lowercase, tokenize bằng PyVi, loại bỏ stopwords).
- **`k1`** (`float`, default `1.5`): Điều khiển mức độ bão hòa của tần suất xuất hiện từ (Term Frequency Saturation).
- **`b`** (`float`, default `0.75`): Điều khiển mức độ phạt độ dài văn bản (Document Length Normalization).
- **`epsilon`** (`float`, default `0.25`): Hệ số sàn cho giá trị IDF để tránh trường hợp từ xuất hiện trong quá nhiều tài liệu sinh ra điểm IDF âm.

### 3.2 Lấy Điểm của Toàn bộ Corpus (`get_scores`)
```python
scores = bm25.get_scores(tokenized_query)
```
- **Input:** `tokenized_query` (`List[str]`): Danh sách token của câu truy vấn.
- **Output:** `numpy.ndarray` 1 chiều chứa float scores có độ dài đúng bằng số document trong corpus. Thứ tự tương ứng với index ban đầu của corpus.

### 3.3 Lấy Top N Documents trực tiếp (`get_top_n`)
```python
top_docs = bm25.get_top_n(tokenized_query, raw_documents, n=5)
```
- **Input:** Tokenized query, danh sách document gốc, và số lượng `n` muốn lấy.
- **Output:** Danh sách `n` tài liệu có điểm số cao nhất.

---

## 4. Code Mẫu Hoàn Chỉnh: End-to-End Pipeline

Dưới đây là đoạn script Python độc lập, thực thi từ khâu tiền xử lý (sử dụng `pyvi`), xây dựng chỉ mục BM25, truy vấn và trả về Top-K:

```python
import pickle
from pyvi import ViTokenizer
from rank_bm25 import BM25Okapi

# 1. Dữ liệu mẫu điều luật
raw_docs = [
    {
        "article_id": "HP2013_D20",
        "title": "Điều 20. Quyền bất khả xâm phạm về thân thể",
        "content": "Mọi người có quyền bất khả xâm phạm về thân thể, được pháp luật bảo hộ về sức khoẻ, danh dự và nhân phẩm; không bị tra tấn, bạo lực, truy bức, nhục hình hay bất kỳ hình thức đối xử nào khác xâm phạm thân thể, sức khỏe, xúc phạm danh dự, nhân phẩm."
    },
    {
        "article_id": "BLDS2015_D33",
        "title": "Điều 33. Quyền sống, quyền được bảo đảm an toàn về tính mạng, sức khỏe, thân thể",
        "content": "Cá nhân có quyền sống, quyền bất khả xâm phạm về tính mạng, thân thể, quyền được pháp luật bảo hộ về sức khỏe. Không ai bị tước đoạt tính mạng trái luật."
    },
    {
        "article_id": "BLHS2015_D123",
        "title": "Điều 123. Tội giết người",
        "content": "Người nào giết người thuộc một trong các trường hợp sau đây, thì bị phạt tù từ 12 năm đến 20 năm, tù chung thân hoặc tử hình: Giết 02 người trở lên; Giết người dưới 16 tuổi; Giết phụ nữ mà biết là có thai."
    }
]

# 2. Bộ từ dừng rút gọn
STOPWORDS = {"và", "hoặc", "của", "những", "các", "mọi", "có", "được", "bị", "về", "thì", "tại", "điều"}

def preprocess(text: str) -> list[str]:
    """Lowercase -> PyVi word segment -> filter stopwords."""
    text = text.lower()
    tokenized_str = ViTokenizer.tokenize(text)
    tokens = tokenized_str.split()
    return [t for t in tokens if t not in STOPWORDS and len(t) > 1]

# 3. Chuẩn bị corpus tokens
corpus_tokens = [
    preprocess(doc["title"] + " " + doc["content"])
    for doc in raw_docs
]

# 4. Huấn luyện / Khởi tạo BM25 Index
bm25 = BM25Okapi(corpus_tokens, k1=1.5, b=0.75)

# 5. Thực hiện truy vấn
query = "Quyền bất khả xâm phạm về thân thể và sức khỏe được quy định thế nào?"
query_tokens = preprocess(query)
print(f"Query tokens: {query_tokens}")

# 6. Tính điểm và lấy Top-K
scores = bm25.get_scores(query_tokens)
ranked_indices = scores.argsort()[::-1]

print("\n--- KẾT QUẢ TÌM KIẾM ---")
for rank, idx in enumerate(ranked_indices[:2], start=1):
    doc = raw_docs[idx]
    score = scores[idx]
    print(f"#{rank} [{doc['article_id']}] (Điểm: {score:.4f}): {doc['title']}")
```

---

## 5. Lưu trữ & Phục hồi Chỉ mục (Serialization with Pickle)

Vì `BM25Okapi` lưu trữ các thống kê tần suất từ dưới dạng Python dictionaries và NumPy arrays, ta có thể serialize toàn bộ chỉ mục bằng `pickle`:

### 5.1 Lưu chỉ mục ra file
```python
index_data = {
    "bm25_model": bm25,
    "article_ids": [doc["article_id"] for doc in raw_docs],
    "corpus_tokens": corpus_tokens,
    "k1": 1.5,
    "b": 0.75
}

with open("data/bm25_index.pkl", "wb") as f:
    pickle.dump(index_data, f, protocol=pickle.HIGHEST_PROTOCOL)
```

### 5.2 Tải chỉ mục khi ứng dụng khởi động
```python
with open("data/bm25_index.pkl", "rb") as f:
    loaded_data = pickle.load(f)

bm25_loaded = loaded_data["bm25_model"]
article_ids = loaded_data["article_ids"]
```
*Lưu ý: Tốc độ nạp 1.600 điều luật từ file pickle < 20ms, giúp API FastAPI khởi động ngay lập tức (Lifespan Startup).*

---

## 6. Chiến Lược Tối Ưu Siêu Tham Số (Hyperparameter Tuning)

Mặc định $k_1 = 1.5$ và $b = 0.75$ được chứng minh là khá tối ưu cho văn bản thông thường. Tuy nhiên, với văn bản pháp luật, ta thực hiện Grid Search trên tập 30 câu hỏi đánh giá (`eval_queries.json`):

| Siêu tham số | Khoảng khảo sát (Search Space) | Bước nhảy (Step) | Ý nghĩa thực tiễn với văn bản luật |
|---|---|---|---|
| **$k_1$** | $1.0 - 2.0$ | $0.2$ | Nếu query lặp từ khóa pháp lý quan trọng, $k_1$ cao giúp phân tách tài liệu tốt hơn. |
| **$b$** | $0.5 - 0.85$ | $0.05$ | Các điều luật có độ dài rất chênh lệch (từ 50 từ đến 1.500 từ). $b=0.75$ phạt tài liệu dài phù hợp để tránh ưu tiên các điều tổng quát. |

### Grid Search Strategy Script:
```python
best_recall = 0.0
best_params = {}

for k1 in [1.2, 1.4, 1.5, 1.6, 1.8]:
    for b in [0.6, 0.7, 0.75, 0.8]:
        model = BM25Okapi(corpus_tokens, k1=k1, b=b)
        # Tính Recall@5 trên tập eval_queries
        current_recall = evaluate_recall(model, eval_set, k=5)
        if current_recall > best_recall:
            best_recall = current_recall
            best_params = {"k1": k1, "b": b}
```

---

## 7. Các Cạm Bẫy Phổ Biến & Cách Khắc Phục (Gotchas & Troubleshooting)

1. **Query rỗng hoặc toàn từ dừng:**
   - *Hiện tượng:* `query_tokens` rỗng `[]` dẫn đến `bm25.get_scores([])` trả về toàn bộ mảng số 0.
   - *Xử lý:* Kiểm tra nếu `len(query_tokens) == 0`, trả về fallback empty list ngay lập tức, không gọi hàm chấm điểm.
2. **Từ khóa không tồn tại trong từ điển corpus:**
   - *Hiện tượng:* Nếu người dùng gõ từ chưa từng xuất hiện (Out-of-Vocabulary), điểm số của term đó bằng 0.
   - *Xử lý:* Đây là đặc tính tự nhiên của Sparse Retrieval. Đây chính là lý do cần Tầng 2 (Dense Retrieval với Semantic Embedding).
3. **Bộ nhớ RAM:**
   - Với 1.600 điều luật tiếng Việt (~350.000 từ), corpus ma trận tốn chưa đến 5MB RAM. Không có nguy cơ tràn bộ nhớ.
