# 🛠 Role: HANDMADE (Human-in-the-Loop Operator)

> **Mã Vai Trò:** `HM-00` / `HANDMADE`  
> **Tên vai trò:** Kỹ Sư Thực Thi Thủ Công (Hands-on Practitioner & Project Owner)  
> **Ngày khởi tạo:** 2026-09-09  
> **Dự án:** VietLawAssist — PBL6 Machine Learning Training Model Project  
> **Người đảm nhận:** Bạn (Chủ dự án / Sinh viên bảo vệ đồ án)

---

## 1. Mục Đích & Ý Nghĩa của Role "Handmade"

Trong đồ án tốt nghiệp Kỹ sư Công nghệ Thông tin (PBL6), việc **tự tay thực hiện (Hands-on / Handmade)** các công đoạn kỹ thuật then chốt mang ý nghĩa quyết định:

1. **Hiểu sâu bản chất (Deep Understanding):** Tránh hiện tượng "black-box" (dùng AI sinh code nhưng không hiểu dữ liệu vào/ra thế nào). Tự tay mở từng tệp luật, kiểm tra từng dòng text, gõ từng lệnh tiền xử lý giúp bạn thấu suốt cấu trúc văn bản pháp luật.
2. **Bảo vệ vững vàng trước Hội đồng chấm thi (Defense Confidence):** Khi giảng viên hỏi:
   - *"Em lấy dữ liệu từ đâu? Dữ liệu có bị lỗi font không? Em xử lý ra sao?"*
   - *"Tại sao lại chọn mô hình này mà không chọn mô hình khác?"*
   - *"Tại sao phải tách từ PyVi và bỏ từ dừng trước khi đưa vào BM25?"*  
   $\rightarrow$ Bạn có thể tự tin trả lời từ kinh nghiệm thực chiến do chính tay mình làm.
3. **Mô hình phối hợp Người - AI (Human-AI Teaming):**
   - **Các AI Agents (PM, MLR, DE, SA, EVAL, RW):** Đóng vai trò **Cố vấn chuyên môn (Advisors & Instructors)** — nghiên cứu lý thuyết, phân tích giải pháp, viết cẩm nang hướng dẫn tuần tự từng bước (SOP / Runbooks).
   - **Role "Handmade" (Bạn):** Đóng vai trò **Người thực thi trực tiếp (Primary Operator)** — kiểm soát dữ liệu, bấm chạy các lệnh, xác nhận kết quả và đưa ra quyết định cuối cùng.

---

## 2. Phạm Vi Trách Nhiệm Của Role "Handmade"

| Hạng mục | Trách nhiệm của Handmade | AI Agent Hỗ trợ |
|---|---|---|
| **1. Thu thập dữ liệu (Data Collection)** | Trực tiếp truy cập các cổng thông tin pháp luật chính thống, tải văn bản toàn văn (HTML/PDF), kiểm tra số lượng điều luật và lưu trữ vào thư mục chuẩn. | **DE-03** (Cung cấp URLs, hướng dẫn tải, selector) |
| **2. Chọn model (Model Selection)** | Đọc phân tích so sánh mô hình, tự tay thử nghiệm các thư viện/weights trên terminal hoặc notebook, đánh giá ưu nhược và quyết định lựa chọn. | **MLR-02** (Cung cấp bảng so sánh, lý thuyết, benchmark) |
| **3. Tiền xử lý dữ liệu (Preprocessing)** | Tự tay thực hiện chuỗi tiền xử lý: Chuẩn hóa Unicode NFC $\rightarrow$ Regex bóc tách Điều/Khoản $\rightarrow$ Tách từ PyVi $\rightarrow$ Lọc Stopwords $\rightarrow$ Đóng gói JSON. | **DE-03 & MLR-02** (Cung cấp script mẫu, bộ regex, stopwords) |
| **4. Kiểm thử & Vận hành (Testing & Run)** | Chạy lệnh khởi tạo CSDL SQLite, nạp dữ liệu, thử nghiệm truy vấn BM25 và quan sát kết quả trả về. | **SA-04 & EVAL-05** (Cung cấp script test, query mẫu) |

---

## 3. Quy Tắc Hoạt Động Giữa Các Agents và Role "Handmade"

```
┌────────────────────────────────────────────────────────┐
│             AI AGENTS (CỐ VẤN CHUYÊN MÔN)              │
│  PM-01 (Lộ trình)   │  MLR-02 (Mô hình & Thuật toán)   │
│  DE-03 (Dữ liệu)    │  SA-04 (Kiến trúc & CSDL)        │
│  EVAL-05 (Kiểm thử) │  RW-06 (Báo cáo & Tài liệu)      │
└──────────────────────────┬─────────────────────────────┘
                           │ Viết hướng dẫn Step-by-Step chi tiết
                           │ Cung cấp lệnh mẫu & tiêu chí kiểm tra
                           ▼
┌────────────────────────────────────────────────────────┐
│             ROLE "HANDMADE" (BẠN - OPERATOR)           │
│  1. Đọc hướng dẫn tuần tự từng bước (SOP)              │
│  2. Mở trình duyệt / Terminal tự tay thực hiện         │
│  3. Kiểm tra kết quả đầu ra (Sanity Check)             │
│  4. Đánh dấu hoàn thành vào TASKS.md                   │
└────────────────────────────────────────────────────────┘
```

1. **Nguyên tắc "No Magic":** Các hướng dẫn gửi cho Handmade role phải giải thích rõ **Lệnh này làm gì? Tại sao phải gõ lệnh này? Kết quả mong đợi là gì?**
2. **Nguyên tắc "Fail-Safe":** Mọi thao tác thủ công đều có bước kiểm tra chéo (sanity check) để phát hiện sai sót ngay lập tức.
3. **Bảo toàn dữ liệu gốc:** Dữ liệu thô tải về phải được lưu trữ bất biến (immutable raw data) trong `data/raw/` trước khi tiến hành tiền xử lý.

---

## 4. Tài Liệu Giao Tiếp Của Role "Handmade"

- **Kế hoạch thực hành:** [.agents/team/handmade/TASKS.md](file:///d:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/)
- **Cẩm nang hướng dẫn tuần tự từng bước:** [.agents/team/handmade/MANUAL_GUIDE.md](file:///d:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/)
- **Bảng tự nghiệm thu kết quả:** [.agents/team/handmade/REVIEW.md](file:///d:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/)
