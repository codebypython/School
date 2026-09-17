# ✅ REVIEW — Role: HANDMADE (Tự Đánh Giá Thực Hành)

> **Người thực hiện:** Bạn (Chủ dự án / Kỹ sư thực thi)  
> **Người nghiệm thu:** PM-01 & Giảng viên hướng dẫn  
> **Giai đoạn:** Phase 1 — Thu thập, Chọn mô hình & Tiền xử lý dữ liệu

---

## 1. Tiêu Chí Tự Nghiệm Thu (Self-Evaluation Rubric)

| Tiêu chí | Thang điểm | Yêu cầu đạt được |
|---|:---:|---|
| **1. Khả năng giải trình nguồn gốc (Provenance)** | 1-5 | Nêu được chính xác nguồn tải văn bản luật, số hiệu văn bản, ngày ban hành và lý do chọn nguồn đó. |
| **2. Am hiểu lựa chọn mô hình (Model Justification)** | 1-5 | Giải thích được tại sao Tầng 1 chọn BM25Okapi thay vì BERT/LLM; tại sao chọn PyVi tokenizer thay vì khoảng trắng thông thường. |
| **3. Nắm vững kỹ thuật tiền xử lý (Preprocessing Mastery)** | 1-5 | Tự tay thao tác và giải thích được tác dụng của: Chuẩn hóa NFC, Regex bóc tách Điều/Khoản, Lọc từ dừng pháp lý. |
| **4. Kiểm thử độc lập (Independent Verification)** | 1-5 | Tự chạy được server, gửi truy vấn thử nghiệm và đọc hiểu cấu trúc phản hồi JSON. |

---

## 2. Bảng Theo Dõi Tiến Độ Thực Hành

| Mã Task | Nội Dung Nhiệm Vụ | Trạng Thái | Ngày Hoàn Thành | Điểm Tự Đánh Giá | Nhận Xét & Ghi Chú Cá Nhân |
|:---:|---|:---:|:---:|:---:|---|
| **HM-01.1** | Tải về văn bản gốc Hiến pháp 2013 | [ ] | — | — | |
| **HM-01.2** | Tải về BLDS 2015 & BLHS 2015 | [ ] | — | — | |
| **HM-01.3** | Kiểm tra số lượng điều luật và font chữ | [ ] | — | — | |
| **HM-02.1** | Thử nghiệm so sánh PyVi vs Underthesea | [ ] | — | — | |
| **HM-02.2** | Thử nghiệm thuật toán BM25Okapi trên terminal | [ ] | — | — | |
| **HM-02.3** | Định hướng mô hình PhoBERT & Qwen 1.5B | [ ] | — | — | |
| **HM-03.1** | Thực hành chuẩn hóa Unicode NFC | [ ] | — | — | |
| **HM-03.2** | Thực hành Regex bóc tách 1 điều = 1 doc | [ ] | — | — | |
| **HM-03.3** | Thực hành tách từ PyVi & lọc từ dừng pháp lý | [ ] | — | — | |
| **HM-03.4** | Đóng gói nạp dữ liệu vào SQLite | [ ] | — | — | |
| **HM-04.1** | Khởi động server Uvicorn và test API `/api/retrieve` | [ ] | — | — | |

---

## 3. Nhật Ký Ghi Nhận Khó Khăn & Kinh Nghiệm (Self-Reflection Log)

*(Bạn hãy ghi lại các điểm lưu ý hoặc lỗi gặp phải khi tự tay thực hiện vào phần này để làm tư liệu đưa vào Chương 4 & 5 báo cáo đồ án)*:

- **Ghi chú 1 (Về dữ liệu):** ...
- **Ghi chú 2 (Về mô hình & thuật toán):** ...
- **Ghi chú 3 (Về xử lý chuỗi tiếng Việt):** ...
