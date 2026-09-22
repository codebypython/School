# 🚀 BỘ BÀI TẬP LUYỆN PHẢN XẠ CƠ TAY: NGÀY 08 ĐẾN NGÀY 14
## Huấn luyện Làm chủ Antigravity Agentic Workflows & Multi-Modal AI

---

### DRILL 08 (DAY 08): BẮT NHỊP ANTIGRAVITY TAB & TAB TO JUMP
* **Nhiệm vụ**:
  1. Mở một file mới `calculator.py`.
  2. Gõ dòng đầu tiên: `class ScientificCalculator:`.
  3. Xuống dòng gõ `def add(` $\rightarrow$ Quan sát gợi ý mờ (Ghost text).
  4. Bấm <kbd>Tab</kbd> nhận gợi ý.
  5. Bấm tiếp <kbd>Tab</kbd> để nhảy con trỏ ra ngoài dấu ngoặc tròn (Tab to Jump).
  6. Gõ tiếp `def subtract(` $\rightarrow$ Chỉ bấm <kbd>Ctrl</kbd> + <kbd>→</kbd> để nhận 2 từ đầu tiên của gợi ý.
* **Tiêu chuẩn đạt**: Hoàn thành 4 phương thức cơ bản (`add`, `subtract`, `multiply`, `divide`) trong dưới 30 giây nhờ tận dụng trên 80% gợi ý từ Tab.

---

### DRILL 09 (DAY 09): INLINE REFACTORING VỚI <kbd>Ctrl</kbd> + <kbd>I</kbd>
* **Nhiệm vụ**:
  1. Bôi đen phương thức `divide` vừa viết.
  2. Bấm <kbd>Ctrl</kbd> + <kbd>I</kbd>.
  3. Gõ: *"Handle division by zero exception with custom error and add Google style docstring"*.
  4. Chờ xem Visual Diff xuất hiện: dòng cũ đỏ, dòng mới xanh.
  5. Bấm <kbd>Ctrl</kbd> + <kbd>Enter</kbd> để Accept thay đổi.
* **Tiêu chuẩn đạt**: Thao tác diễn ra hoàn toàn trên Editor, không mở khung chat sidebar, thời gian dưới 20 giây.

---

### DRILL 10 (DAY 10): ĐỊNH HƯỚNG NGỮ CẢNH BẰNG `@` MENTIONS
* **Nhiệm vụ**:
  1. Mở terminal, chạy lệnh test gây lỗi cố tình (ví dụ: `pytest tests/test_smoke.py`).
  2. Nhấn phím chuyển sang khung chat.
  3. Nhập prompt chính xác:
     ```
     Phân tích lỗi trong @terminal và kiểm tra lại file @file:Project/tests/test_smoke.py. Đề xuất bản vá tối giản nhất.
     ```
  4. Quan sát Agent đọc trực tiếp terminal log và nội dung file mà không yêu cầu bạn phải dán log thủ công.
* **Tiêu chuẩn đạt**: Gửi prompt hoàn chỉnh chỉ trong 10 giây nhờ gõ fuzzy suggest của `@`.

---

### DRILL 11 (DAY 11): VẬN HÀNH QUY TRÌNH KẾ HOẠCH (PLANNING MODE)
* **Nhiệm vụ**:
  1. Yêu cầu Agent: *"Lập kế hoạch thiết kế module lưu trữ cache Redis cho hệ thống"*.
  2. Đọc file `implementation_plan.md` sinh ra trong khung Artifact.
  3. Kiểm tra 3 phần: User Review, Proposed Changes, Verification Plan.
  4. Bấm nút **Proceed** (hoặc gửi lệnh duyệt) để Agent tự động triển khai.
* **Tiêu chuẩn đạt**: Không can thiệp sửa code thủ công; để Agent tự động hoàn thành và báo cáo qua `walkthrough.md`.

---

### DRILL 12 (DAY 12): PHẢN BIỆN THIẾT KẾ VỚI `/grill-me` & TÁCH NHÁNH BẰNG `/fork`
* **Nhiệm vụ**:
  1. Trong khung chat, gõ: `/grill-me Tôi muốn thiết kế hệ thống xếp hạng sinh viên theo barem điểm rèn luyện`.
  2. Trả lời liên tiếp 3 câu hỏi phản biện của Agent về Edge cases, Database Concurrency và Quy tắc làm tròn điểm.
  3. Khi hội thoại đã dài trên 10 tin nhắn, gõ lệnh: `/fork Thử nghiệm giải thuật tối ưu theo Priority Queue`.
  4. Xác nhận một phiên chat nhánh mới được mở ra với bộ nhớ sạch sẽ, phản hồi tức thì.
* **Tiêu chuẩn đạt**: Hoàn thành cuộc phỏng vấn phản biện và tách nhánh thành công.

---

### DRILL 13 (DAY 13): ĐÓNG GÓI CHUẨN MỰC VÀO `.agents/rules/`
* **Nhiệm vụ**:
  1. Tạo file `.agents/rules/test_standards.md` trong workspace.
  2. Thêm quy định: *"Mọi test case phải tuân thủ chuẩn Arrange-Act-Assert (AAA) và có docstring tiếng Việt"*.
  3. Mở phiên chat mới, ra lệnh ngắn gọn: *"Viết 1 test case cho hàm tính điểm trung bình"*.
  4. Kiểm tra code do Agent sinh ra: Nếu có cấu trúc AAA và docstring tiếng Việt $\rightarrow$ Thành công!
* **Tiêu chuẩn đạt**: Agent tự động tuân thủ quy tắc mà không cần bạn phải nhắc lại trong prompt.

---

### DRILL 14 (DAY 14): THỬ THÁCH TỐT NGHIỆP CAPSTONE 15 PHÚT
* **Đề bài Thử thách**:
  - Xây dựng hoàn chỉnh một **Module Quản lý Task bất đồng bộ (Async Task Manager)** trong Python/FastAPI từ con số 0.
* **Yêu cầu khắt khe**:
  1. Phải dùng Planning Mode lập kế hoạch trước.
  2. Sử dụng Auxiliary Windows để mở song song: 1 cửa sổ Code, 1 cửa sổ Chat AI, 1 cửa sổ Terminal test.
  3. Viết đầy đủ Unit tests và chạy `pytest` pass 100%.
  4. Tuyệt đối không dùng chuột quá 3 lần trong suốt 15 phút.
* **Nghiệm thu**: Sau khi pass 100% tests, ghi lại log thời gian và tự đánh giá điểm số theo rubric của Company 12.
