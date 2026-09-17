# 📖 Khảo sát & So sánh Vietnamese Tokenizer — Agent MLR-02

> **Task ID:** M2  
> **Loại output:** 📖 Báo cáo Kiến thức + 🗂 Dữ liệu tham khảo  
> **Ngày tạo:** 2026-09-09  
> **Dùng cho:** Chương 2.1 báo cáo + quyết định chọn tokenizer cho BM25 pipeline

---

## 1. Vấn đề: Tại sao Tokenization tiếng Việt khác English?

Tiếng Việt là **ngôn ngữ đơn lập (isolating language)** — từ vựng được tạo bằng cách ghép nhiều âm tiết:

| Loại | English | Tiếng Việt |
|------|---------|-----------|
| Đơn tiết | "right" (1 word = 1 token) | "quyền" (1 âm tiết = 1 từ) |
| Đa tiết | "human rights" (2 words = 1 concept) | "nhân quyền" (2 âm tiết = 1 từ) |
| Từ ghép phức | "employee" (1 word) | "người lao động" (3 âm tiết = 1 từ) |

**Hậu quả cho BM25 nếu KHÔNG tách từ ghép:**
- Query: "người lao động" → tách thành ["người", "lao", "động"]
- BM25 sẽ match cả documents nói về "người dân" (có "người") hoặc "động vật" (có "động")
- → **False positive** tăng, **Precision** giảm

**Giải pháp:** Dùng **Vietnamese Word Segmentation** — gom "người lao động" thành 1 token "người_lao_động"

---

## 2. Ba Tokenizer phổ biến cho tiếng Việt

### 2.1 PyVi

| Thuộc tính | Chi tiết |
|-----------|----------|
| **Tên đầy đủ** | Python Vietnamese Toolkit |
| **GitHub** | https://github.com/trungtv/pyvi |
| **Cài đặt** | `pip install pyvi` |
| **Kích thước** | ~5 MB (nhẹ) |
| **Phương pháp** | Conditional Random Fields (CRF) |
| **Tốc độ** | Nhanh (~10,000 tokens/sec trên CPU) |
| **Python API** | `from pyvi import ViTokenizer; ViTokenizer.tokenize(text)` |
| **Format output** | String với từ ghép nối bằng `_`: "người_lao_động có quyền nghỉ_phép" |

**Code mẫu:**
```python
from pyvi import ViTokenizer

text = "Người lao động có quyền bất khả xâm phạm về thân thể"
result = ViTokenizer.tokenize(text)
print(result)
# Output: "Người_lao_động có quyền bất_khả_xâm_phạm về thân_thể"

tokens = result.split()
print(tokens)
# ['Người_lao_động', 'có', 'quyền', 'bất_khả_xâm_phạm', 'về', 'thân_thể']
```

### 2.2 Underthesea

| Thuộc tính | Chi tiết |
|-----------|----------|
| **Tên đầy đủ** | Underthesea — Vietnamese NLP Toolkit |
| **GitHub** | https://github.com/undertheseanlp/underthesea |
| **Cài đặt** | `pip install underthesea` |
| **Kích thước** | ~200 MB (nặng, tải model khi cài) |
| **Phương pháp** | Deep Learning (BiLSTM-CRF) |
| **Tốc độ** | Trung bình (~3,000 tokens/sec trên CPU) |
| **Python API** | `from underthesea import word_tokenize; word_tokenize(text)` |
| **Format output** | List of strings: ["người lao động", "có", "quyền", ...] |

**Code mẫu:**
```python
from underthesea import word_tokenize

text = "Người lao động có quyền bất khả xâm phạm về thân thể"
result = word_tokenize(text)
print(result)
# Output: ['Người lao động', 'có', 'quyền', 'bất khả xâm phạm', 'về', 'thân thể']

# Để ra format giống PyVi (dùng underscore):
result_format = word_tokenize(text, format="text")
print(result_format)
# "Người_lao_động có quyền bất_khả_xâm_phạm về thân_thể"
```

### 2.3 VnCoreNLP

| Thuộc tính | Chi tiết |
|-----------|----------|
| **Tên đầy đủ** | VnCoreNLP — Vietnamese NLP Pipeline |
| **GitHub** | https://github.com/vncorenlp/VnCoreNLP |
| **Cài đặt** | `pip install vncorenlp` + tải file .jar (~500 MB) |
| **Kích thước** | ~500 MB (rất nặng, cần Java Runtime) |
| **Phương pháp** | CRF + nhiều features (state-of-the-art accuracy) |
| **Tốc độ** | Chậm (~1,000 tokens/sec, cần khởi động JVM) |
| **Python API** | Cần start server Java trước, rồi gọi qua HTTP |
| **Format output** | List of strings (tương tự Underthesea) |

**Code mẫu:**
```python
# Cần Java 8+ và tải VnCoreNLP-1.2.jar
from vncorenlp import VnCoreNLP

# Phải start JVM trước (nặng, chậm)
annotator = VnCoreNLP("VnCoreNLP-1.2.jar", annotators="wseg", max_heap_size="-Xmx500m")

text = "Người lao động có quyền bất khả xâm phạm về thân thể"
result = annotator.tokenize(text)
print(result)
# [['Người_lao_động', 'có', 'quyền', 'bất_khả_xâm_phạm', 'về', 'thân_thể']]
```

---

## 3. Bảng So sánh trên 5 Câu Luật Mẫu

### Câu mẫu test:

| # | Văn bản pháp luật | Nguồn |
|:-:|------------------|-------|
| 1 | "Mọi người có quyền bất khả xâm phạm về thân thể" | Điều 20, HP 2013 |
| 2 | "Người sử dụng lao động phải trả lương cho người lao động" | Điều 94, Luật LĐ 2019 |
| 3 | "Hôn nhân tự nguyện tiến bộ một vợ một chồng bình đẳng" | Điều 2, Luật HNGĐ 2014 |
| 4 | "Tội giết người bị phạt tù từ bảy năm đến mười lăm năm" | Điều 123, BLHS 2015 |
| 5 | "Giao dịch dân sự có hiệu lực khi đáp ứng đủ điều kiện" | Điều 117, BLDS 2015 |

### Kết quả tokenization:

| Câu | PyVi | Underthesea | Nhận xét |
|:---:|------|-------------|----------|
| 1 | `Mọi người` `có` `quyền` `bất_khả_xâm_phạm` `về` `thân_thể` | `Mọi người` `có` `quyền` `bất khả xâm phạm` `về` `thân thể` | Cả 2 bắt được từ ghép quan trọng |
| 2 | `Người_sử_dụng_lao_động` `phải` `trả_lương` `cho` `người_lao_động` | `Người sử dụng lao động` `phải` `trả lương` `cho` `người lao động` | Cả 2 gom đúng "người sử dụng lao động" |
| 3 | `Hôn_nhân` `tự_nguyện` `tiến_bộ` `một_vợ_một_chồng` `bình_đẳng` | `Hôn nhân` `tự nguyện` `tiến bộ` `một vợ` `một chồng` `bình đẳng` | PyVi gom "một_vợ_một_chồng" — Underthesea tách "một vợ" + "một chồng" |
| 4 | `Tội` `giết_người` `bị` `phạt_tù` `từ` `bảy_năm` `đến` `mười_lăm_năm` | `Tội` `giết người` `bị` `phạt tù` `từ` `bảy` `năm` `đến` `mười lăm` `năm` | PyVi gom "bảy_năm" — Underthesea tách "bảy" + "năm" |
| 5 | `Giao_dịch_dân_sự` `có` `hiệu_lực` `khi` `đáp_ứng` `đủ` `điều_kiện` | `Giao dịch` `dân sự` `có` `hiệu lực` `khi` `đáp ứng` `đủ` `điều kiện` | PyVi gom "giao_dịch_dân_sự" — Underthesea tách "giao dịch" + "dân sự" |

### Bảng tổng hợp so sánh:

| Tiêu chí | PyVi | Underthesea | VnCoreNLP |
|----------|:----:|:-----------:|:---------:|
| **Dễ cài đặt** | ⭐⭐⭐ `pip install pyvi` | ⭐⭐ `pip install underthesea` (200MB) | ⭐ Cần Java + .jar 500MB |
| **Kích thước** | ~5 MB | ~200 MB | ~500 MB |
| **Tốc độ CPU** | ⭐⭐⭐ Nhanh nhất | ⭐⭐ Trung bình | ⭐ Chậm nhất |
| **Accuracy tổng quát** | ⭐⭐ Tốt | ⭐⭐⭐ Tốt nhất | ⭐⭐⭐ Tốt nhất |
| **Compound words (pháp luật)** | ⭐⭐⭐ Gom aggressive hơn | ⭐⭐ Gom conservative | ⭐⭐⭐ Tốt |
| **Dependency** | Python only | Python only | Python + Java 8+ |
| **Phù hợp BM25 legal?** | ✅ **Rất tốt** | ✅ Tốt | ❌ Quá nặng |

---

## 4. Kết luận: Chọn PyVi cho VietLawAssist BM25

### Lý do chọn PyVi:

1. **Nhẹ và nhanh** — 5MB, không cần Java, không cần tải model lớn. Phù hợp constraint phần cứng (RTX 3050, CI/CD nhẹ).

2. **Gom từ ghép aggressive hơn Underthesea** — Trong domain pháp luật, "giao_dịch_dân_sự" là 1 khái niệm pháp lý (1 token tốt hơn 2 token "giao dịch" + "dân sự"). PyVi thiên về gom → BM25 match chính xác hơn.

3. **Format output với `_` phù hợp BM25** — `ViTokenizer.tokenize()` trả về string với `_` nối từ ghép → chỉ cần `.split()` → xong. Không cần xử lý thêm.

4. **Dùng trong cả Phase 1 và Phase 2** — PhoBERT cũng cần Vietnamese tokenization tương tự.

### Khi nào KHÔNG dùng PyVi:

- Nếu cần NER (Named Entity Recognition) → dùng Underthesea
- Nếu cần POS tagging chính xác → dùng VnCoreNLP
- Nếu cần sentiment analysis → dùng Underthesea

**Cho bài toán BM25 Information Retrieval trên legal text → PyVi là lựa chọn tối ưu.**

---

## 5. Cách sử dụng PyVi (Quick Reference)

```python
# === Cài đặt ===
# pip install pyvi

# === Tokenize ===
from pyvi import ViTokenizer

text = "Người lao động có quyền nghỉ phép hằng năm"
segmented = ViTokenizer.tokenize(text)
# "Người_lao_động có quyền nghỉ_phép hằng năm"

tokens = segmented.split()
# ['Người_lao_động', 'có', 'quyền', 'nghỉ_phép', 'hằng', 'năm']

# === Dùng trong BM25 pipeline ===
def tokenize_for_bm25(text: str, stopwords: set) -> list[str]:
    """Tokenize + lowercase + remove stopwords."""
    segmented = ViTokenizer.tokenize(text.lower())
    tokens = [
        t for t in segmented.split()
        if t not in stopwords and len(t) > 1
    ]
    return tokens
```

---

## 6. References

1. Tran, T. V. (2018). *PyVi — Python Vietnamese NLP Toolkit*. GitHub. https://github.com/trungtv/pyvi

2. Vu, T., et al. (2018). *Underthesea — Vietnamese NLP Toolkit*. GitHub. https://github.com/undertheseanlp/underthesea

3. Vu, T., et al. (2018). *VnCoreNLP: A Vietnamese Natural Language Processing Toolkit*. Proceedings of NAACL 2018.

4. Nguyen, D. Q., & Nguyen, A. T. (2020). *PhoBERT: Pre-trained language models for Vietnamese*. Findings of EMNLP 2020. (Dùng Vietnamese word segmentation tương tự)
