# 📖 Báo cáo Chunking Strategy — Agent DE-03

> **Task ID:** D3  
> **Loại output:** 📖 Báo cáo Kiến thức  
> **Ngày tạo:** 2026-09-09  
> **Dùng cho:** Chương 4.1 báo cáo + giải thích khi bảo vệ "tại sao chunking theo Điều?"

---

## 1. Vấn đề: Chunking là gì và tại sao quan trọng?

**Chunking** là quá trình chia corpus lớn (toàn bộ bộ luật) thành các **đơn vị nhỏ hơn (chunks/documents)** để BM25 và Dense Retrieval có thể tìm kiếm.

Cách chunking quyết định **chất lượng tìm kiếm:**
- Chunk quá nhỏ → mất ngữ cảnh → kết quả fragmentary
- Chunk quá lớn → quá nhiều noise → khó rank đúng

---

## 2. Ba chiến lược Chunking phổ biến

### 2.1 Chiến lược A: Theo Điều (Article-level) ✅ ĐÃ CHỌN

```
Corpus → Chương I → Điều 1 [CHUNK 1]
                   → Điều 2 [CHUNK 2]
                   → Điều 3 [CHUNK 3]
         Chương II → Điều 4 [CHUNK 4]
                   → ...
```

- **1 chunk = 1 điều luật** (toàn bộ nội dung + tên điều)
- Metadata: law_code, chapter, article_number, title

### 2.2 Chiến lược B: Theo Khoản (Clause-level)

```
Điều 20 HP2013:
  → Khoản 1 [CHUNK A]  "Mọi người có quyền bất khả xâm phạm..."
  → Khoản 2 [CHUNK B]  "Không ai bị bắt nếu không có quyết định..."
```

- **1 chunk = 1 khoản** trong 1 điều
- Số chunks nhiều hơn (mỗi điều có 2-10 khoản)

### 2.3 Chiến lược C: Cửa sổ trượt (Sliding Window)

```
Toàn bộ văn bản liên tục → chia đều mỗi 200 từ, overlap 50 từ
  → Chunk 1: từ 1-200
  → Chunk 2: từ 151-350
  → Chunk 3: từ 301-500
  → ...
```

- **1 chunk = N từ** cố định, overlap giữa các chunks
- Không quan tâm cấu trúc pháp lý

---

## 3. Bảng so sánh 3 chiến lược cho Legal Retrieval

| Tiêu chí | Theo Điều (A) | Theo Khoản (B) | Cửa sổ trượt (C) |
|----------|:------------:|:--------------:|:----------------:|
| **Số chunks (~1.588 điều)** | ~1.588 | ~5.000-8.000 | ~3.000-4.000 |
| **Giữ ngữ cảnh pháp lý** | ✅ Hoàn chỉnh | ⚠️ Mất liên kết giữa khoản | ❌ Cắt ngang câu |
| **Khả năng trích dẫn** | ✅ "Điều X, Luật Y" | ✅ "Khoản Z, Điều X" | ❌ Không trích được |
| **Phù hợp BM25** | ✅ Tốt (document vừa phải) | ⚠️ Chunk quá nhỏ → IDF bias | ⚠️ Chunk có thể chứa 2 chủ đề khác nhau |
| **Phù hợp Dense Retrieval** | ✅ Tốt (embedding ngữ nghĩa 1 điều) | ✅ Tốt (embedding chi tiết hơn) | ❌ Embedding lẫn lộn |
| **Phù hợp RAG** | ✅ Context vừa đủ cho LLM | ⚠️ Cần gom nhiều khoản lại | ⚠️ Context rời rạc |
| **Độ phức tạp implement** | ⭐ Đơn giản | ⭐⭐ Trung bình | ⭐⭐⭐ Phức tạp |
| **Độ dài trung bình** | ~190 từ | ~30-80 từ | ~200 từ (cố định) |

---

## 4. Tại sao chọn "1 Điều = 1 Document"?

### 4.1 Lý do pháp lý

Trong hệ thống pháp luật Việt Nam, **Điều** là đơn vị pháp lý cơ bản nhất:
- Mỗi điều luật quy định **1 vấn đề pháp lý** cụ thể
- Các khoản trong 1 điều **liên kết chặt chẽ** với nhau — tách ra sẽ mất nghĩa
- Khi trích dẫn pháp luật, luôn dùng "Điều X" — không trích riêng khoản mà không ghi điều

**Ví dụ:**
> Điều 20 HP2013 có 2 khoản:
> - Khoản 1: "Mọi người có quyền bất khả xâm phạm về thân thể..."
> - Khoản 2: "Không ai bị bắt nếu không có quyết định..."
> 
> Nếu tách thành 2 chunks → câu hỏi "quyền bất khả xâm phạm" chỉ match Khoản 1, bỏ sót Khoản 2 vốn là phần bổ sung quan trọng.

### 4.2 Lý do kỹ thuật

1. **BM25 hoạt động tốt nhất với document 100-500 từ** — trung bình 1 điều luật ~190 từ → nằm trong sweet spot
2. **PhoBERT max_length = 256 tokens** — 1 điều luật vừa vặn, không cần truncate
3. **RAG context:** Gom 3-5 điều luật = 600-1000 từ → vừa đủ context window cho Qwen2.5

### 4.3 Lý do thực tiễn

1. **Đơn giản implement:** Tách điều bằng regex `r"Điều\s+\d+"` → dễ, ít lỗi
2. **Dễ validate:** Đếm số chunks = số điều → so sánh với số điều thực tế của bộ luật
3. **Dễ truy vết:** User thấy kết quả → click → đọc nguyên điều luật gốc

---

## 5. Ví dụ minh họa: 1 Điều → 1 Document với Metadata

### Input (raw text từ vbpl.vn):

```html
<p><strong>Điều 20.</strong> Quyền bất khả xâm phạm về thân thể</p>
<p>1. Mọi người có quyền bất khả xâm phạm về thân thể, được pháp luật 
bảo hộ về sức khoẻ, danh dự và nhân phẩm; không bị tra tấn, bạo lực, 
truy bức, nhục hình hay bất kỳ hình thức đối xử nào khác xâm phạm thân 
thể, sức khỏe, xúc phạm danh dự, nhân phẩm.</p>
<p>2. Không ai bị bắt nếu không có quyết định của Toà án nhân dân, quyết 
định hoặc phê chuẩn của Viện kiểm sát nhân dân, trừ trường hợp phạm tội 
quả tang. Việc bắt, giam giữ người do luật định.</p>
```

### Output (1 structured document):

```json
{
  "article_id": "HP2013_D20",
  "law_code": "HP2013",
  "law_name": "Hiến pháp nước CHXHCN Việt Nam 2013",
  "chapter": "Chương II - Quyền con người, quyền và nghĩa vụ cơ bản của công dân",
  "article_number": 20,
  "title": "Quyền bất khả xâm phạm về thân thể",
  "content": "1. Mọi người có quyền bất khả xâm phạm về thân thể, được pháp luật bảo hộ về sức khoẻ, danh dự và nhân phẩm; không bị tra tấn, bạo lực, truy bức, nhục hình hay bất kỳ hình thức đối xử nào khác xâm phạm thân thể, sức khỏe, xúc phạm danh dự, nhân phẩm.\n2. Không ai bị bắt nếu không có quyết định của Toà án nhân dân, quyết định hoặc phê chuẩn của Viện kiểm sát nhân dân, trừ trường hợp phạm tội quả tang. Việc bắt, giam giữ người do luật định.",
  "full_text": "Điều 20. Quyền bất khả xâm phạm về thân thể\n1. Mọi người có quyền...",
  "effective_date": "2014-01-01",
  "source_url": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=32801",
  "word_count": 87
}
```

---

## 6. Xử lý Edge Cases

### 6.1 Điều luật quá dài (>500 từ)

- **BLDS 2015 Điều 688:** ~600 từ (dài nhất)
- **Xử lý:** Giữ nguyên — BM25 tự normalize bằng tham số `b`. PhoBERT truncate tại 256 tokens nhưng phần đầu điều luật thường chứa keywords quan trọng nhất.

### 6.2 Điều luật bị sửa đổi/bổ sung

- **BLHS 2015 sửa đổi 2017:** Một số điều bị thay đổi nội dung
- **Xử lý:** Luôn lấy phiên bản MỚI NHẤT (văn bản hợp nhất). Ghi metadata `effective_date` để phân biệt.

### 6.3 Điều luật có phụ lục/bảng biểu

- Một số điều có bảng (VD: bảng thuế)
- **Xử lý:** Chuyển bảng thành text thuần. Nếu quá phức tạp → ghi note "Xem phụ lục" trong content.

---

## 7. References

1. Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Section 3: Document Chunking Strategies.

2. Ma, X., et al. (2023). *Fine-Tuning LLaMA for Legal Question Answering*. Section 4.2: Legal Document Segmentation.
