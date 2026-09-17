# 📋 TASKS — Role: HANDMADE (Thực Hành Thủ Công)

> **Người thực hiện:** Bạn (Chủ dự án / Kỹ sư thực thi)  
> **Cố vấn & Hướng dẫn:** Toàn bộ 6 AI Agents (PM-01, MLR-02, DE-03, SA-04, EVAL-05, RW-06)  
> **Tài liệu hướng dẫn chi tiết:** [.agents/team/handmade/MANUAL_GUIDE.md](file:///d:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/)

---

## Danh Sách Nhiệm Vụ Cần Làm Thủ Công (Phase 1)

### 📥 Phần 1: Thu Thập Dữ Liệu Thủ Công (Data Collection)
- [ ] **Task HM-01.1** 🌐 Tải về văn bản gốc của bộ luật đầu tiên: **Hiến pháp 2013** từ Cổng thông tin Quốc gia `vbpl.vn` (hoặc PDF chính phủ).
  - *Mục tiêu:* Lưu file thô vào `Project/data/raw/HP2013.html` (hoặc `.txt`/`.pdf`).
  - *DoD:* File tồn tại, mở ra đọc được toàn văn tiếng Việt, không bị lỗi font.
- [ ] **Task HM-01.2** 🌐 Thu thập tiếp 2 bộ luật cốt lõi: **Bộ luật Dân sự 2015** (`BLDS2015`) và **Bộ luật Hình sự 2015** (`BLHS2015`).
  - *Mục tiêu:* Lưu trữ tương ứng vào `Project/data/raw/BLDS2015.html` và `Project/data/raw/BLHS2015.html`.
  - *DoD:* Đủ 3 bộ luật chính của môn Pháp luật Đại cương.
- [ ] **Task HM-01.3** 🔍 Kiểm tra sơ bộ số lượng Điều luật bằng mắt và tìm kiếm (Ctrl + F):
  - Hiến pháp 2013: 120 điều.
  - Bộ luật Dân sự 2015: 689 điều.
  - Bộ luật Hình sự 2015: 426 điều.

---

### 🧠 Phần 2: Chọn Model & Kiểm Chứng Lý Thuyết (Model Selection)
- [ ] **Task HM-02.1** 🔬 Thử nghiệm so sánh thực tế 2 Tokenizer tiếng Việt: **PyVi** và **Underthesea** trên cùng một câu luật.
  - *Mục tiêu:* Mở Python terminal trong `.venv`, chạy hàm tokenize và tự mình quan sát xem từ ghép nào được gom (`_`), tốc độ ra sao.
  - *DoD:* Hiểu rõ tại sao dự án chọn PyVi cho văn bản pháp lý.
- [ ] **Task HM-02.2** 📊 Thử nghiệm thuật toán **BM25Okapi** từ thư viện `rank-bm25`.
  - *Mục tiêu:* Tạo 3 câu văn bản mẫu, thử truy vấn với $k_1=1.5, b=0.75$, in điểm `get_scores()` để thấy cách tính điểm tương đồng từ khóa.
  - *DoD:* Thấu suốt cách BM25 xếp hạng văn bản.
- [ ] **Task HM-02.3** 🧭 Định hướng lựa chọn mô hình Tầng 2 (Dense Retrieval) và Tầng 3 (RAG):
  - Đọc tài liệu đối chiếu của MLR-02: Xác nhận chọn `vinai/phobert-base-v2` cho Tầng 2 và `Qwen/Qwen2.5-1.5B-Instruct` cho Tầng 3.

---

### ⚙️ Phần 3: Tiền Xử Lý Dữ Liệu Thủ Công (Data Preprocessing)
- [ ] **Task HM-03.1** 🧹 Tự viết / chạy lệnh chuẩn hóa Unicode tiếng Việt (NFD $\rightarrow$ NFC) trên văn bản vừa tải về.
  - *Mục tiêu:* Loại bỏ ký tự lạ, ngắt dòng thừa, non-breaking space `\xa0`.
  - *DoD:* Text sạch sẽ, hiển thị tiếng Việt chuẩn Unicode chuẩn dựng sẵn.
- [ ] **Task HM-03.2** ✂️ Thực hành bóc tách Điều luật (Regex Parsing theo chiến lược "1 điều = 1 doc"):
  - *Mục tiêu:* Chạy đoạn mã phân tách text thành từng object có `article_id`, `title`, `content`, `full_text`.
  - *DoD:* Bóc tách thử nghiệm thành công 5-10 điều luật mẫu.
- [ ] **Task HM-03.3** 🔤 Thực hành tách từ PyVi và loại bỏ từ dừng:
  - *Mục tiêu:* Áp dụng `ViTokenizer.tokenize()` kết hợp danh sách từ dừng trong `mlr-02_stopwords_vi_legal.txt`.
  - *DoD:* Quan sát được danh sách token sạch trước khi đưa vào chỉ mục BM25.
- [ ] **Task HM-03.4** 📦 Đóng gói dữ liệu vào cấu trúc JSON và SQLite:
  - *Mục tiêu:* Tự tay lưu danh sách điều luật vào file JSON hoặc insert trực tiếp vào bảng SQLite `law_articles`.
  - *DoD:* Bảng SQLite có dữ liệu, truy vấn `SELECT count(*) FROM law_articles` trả về kết quả chính xác.

---

### 🚀 Phần 4: Vận Hành Thử Nghiệm API
- [ ] **Task HM-04.1** 💻 Chạy lệnh khởi động server backend bằng `uvicorn`.
- [ ] **Task HM-04.2** 🌐 Mở trình duyệt truy cập Swagger UI tại `http://127.0.0.1:8000/docs`.
- [ ] **Task HM-04.3** 🎯 Gõ thử một câu hỏi pháp luật vào API `/api/retrieve` (ví dụ: *"Quyền bất khả xâm phạm về thân thể"*) và xem kết quả JSON trả về.
