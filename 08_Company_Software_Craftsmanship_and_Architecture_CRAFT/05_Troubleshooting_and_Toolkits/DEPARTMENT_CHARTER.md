# 📜 ĐIỀU LỆ PHÒNG KIỂM SOÁT CODE SMELLS & TÁI CẤU TRÚC (TROUBLESHOOTING & TOOLKITS DEPT)
## Phòng 05 — Công Ty Thiết Kế Phần Mềm & Kiến Trúc Hướng Đối Tượng (CORP-08-CRAFT)

> **Mã Phòng Ban:** `CRAFT-DEPT-05`  
> **Trưởng phòng phụ trách:** Agent `SMS-02` (Syllabus Sentinel & Technical Auditor)  
> **Thẩm quyền kỹ thuật:** Chẩn đoán Code Smells, Triệt tiêu Anti-patterns, Khắc phục Flaky Tests & Cẩm nang Tái cấu trúc an toàn  
> **Bộ công cụ cốt lõi:** SonarLint / Ruff / ESLint / Mutation Testing (Mutmut / Stryker)

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kiểm Soát Code Smells là **"Trung tâm Chẩn đoán và Điều trị Bệnh Mã Nguồn"**:
1. **Phát Hiện & Khử Trừ 22 Code Smells Kinh Điển**: Áp dụng danh mục của Martin Fowler để nhận diện các vùng code xuống cấp (Long Method, Large Class, Primitive Obsession, Feature Envy, Shotgun Surgery).
2. **Triệt Tiêu Các Anti-Patterns Trong Thiết Kế**: Chuyển dịch các thiết kế sai lầm (Lạm dụng Singleton, Kế thừa quá sâu, Mô hình thiếu máu Anemic Domain Model) về các mẫu thiết kế chuẩn GoF.
3. **Cứu Hộ Bộ Test Bị Xuống Cấp (Test Triage)**: Xử lý tình trạng **Flaky Tests** (test lúc pass lúc fail ngẫu nhiên) và tình trạng **Over-mocking** (mock quá nhiều khiến test gắn chặt vào cấu trúc nội bộ, cản trở việc refactor).

---

## ⚖️ 2. BỘ NGUYÊN TẮC TÁI CẤU TRÚC AN TOÀN (REFACTORING INVARIANTS)

1. **Nguyên Tắc Không Thay Đổi Hành Vi Bên Ngoài (Behavior-Preserving)**:
   - Tái cấu trúc chỉ thay đổi cấu trúc bên trong của mã nguồn, tuyệt đối không làm thay đổi hành vi quan sát được từ bên ngoài.
2. **Nguyên Tắc "Chỉ Refactor Khi Test Đang Xanh" (Green-to-Green Rule)**:
   - Tuyệt đối không refactor khi đang có Unit Test bị đỏ (fail). Bắt buộc phải đưa toàn bộ test suite về trạng thái Green trước khi tiến hành refactor.
3. **Nguyên Tắc Bước Nhỏ (Baby Steps)**:
   - Mỗi bước tái cấu trúc phải cực kỳ nhỏ (đổi tên biến, tách 1 hàm 5 dòng), sau đó chạy lại test ngay lập tức. Nếu test gãy, `git checkout` quay lại ngay.

---

## 🚑 3. CẨM NANG ĐIỀU TRỊ CODE SMELLS (TOP 4 REFACTORING RUNBOOKS)

---

### 🚨 RUNBOOK 1: CHỮA TRỊ LỚP THẦN THÁNH (GOD CLASS / LARGE CLASS)
* **Triệu chứng**: Một lớp dài hàng trăm dòng, đảm nhận từ tính toán tiền tệ, xác thực người dùng đến ghi log và truy vấn database.
* **Kỹ thuật điều trị**:
  1. *Extract Class*: Tách các nhóm phương thức có cùng lý do thay đổi thành các lớp chuyên biệt mới.
  2. Áp dụng nguyên lý *Single Responsibility Principle (SRP)*: Mỗi lớp chỉ phục vụ 1 đối tượng nghiệp vụ (Actor).

---

### 🚨 RUNBOOK 2: CHỮA TRỊ MÔ HÌNH THIẾU MÁU (ANEMIC DOMAIN MODEL)
* **Triệu chứng**: Entity chỉ chứa các trường dữ liệu và getter/setter rỗng tuếch, toàn bộ logic nghiệp vụ bị dồn sang các lớp `Service`.
* **Kỹ thuật điều trị**:
  1. Chuyển các hàm Setter thành các phương thức có ý nghĩa nghiệp vụ (Domain Methods) bảo vệ Invariant (Ví dụ: thay vì `order.setStatus("PAID")`, viết `order.mark_as_paid()`).
  2. Áp dụng nguyên tắc *Tell, Don't Ask*: Đẩy logic tính toán và kiểm tra hợp lệ ngược trở lại vào chính Entity.

---

### 🚨 RUNBOOK 3: CHỮA TRỊ ÁM ẢNH KIỂU NGUYÊN THỦY (PRIMITIVE OBSESSION)
* **Triệu chứng**: Dùng chuỗi `str` để đại diện cho Số điện thoại, Email, Mã định danh, hoặc dùng `float` để tính toán Tiền tệ (dễ dính lỗi làm tròn số học).
* **Kỹ thuật điều trị**:
  1. *Replace Data Value with Object*: Tạo các Value Objects bất biến (`EmailAddress`, `Money`, `PhoneNumber`) có cơ chế tự kiểm tra tính hợp lệ lúc khởi tạo.

---

### 🚨 RUNBOOK 4: XỬ LÝ OVER-MOCKING TRONG UNIT TESTS
* **Triệu chứng**: Mỗi khi đổi tên hàm private hoặc tách một hàm phụ bên trong, hàng chục Unit Test bị gãy dù logic nghiệp vụ của hệ thống vẫn hoạt động hoàn hảo.
* **Kỹ thuật điều trị**:
  1. Xóa bỏ toàn bộ các Mock trỏ vào phương thức nội bộ của cùng một Aggregate.
  2. Chuyển sang phong cách **Classicist Testing**: Kiểm thử dựa trên kết quả đầu ra (Output-based testing) hoặc trạng thái cuối cùng (State-based testing) thay vì kiểm tra luồng gọi hàm nội bộ (Interaction testing).
