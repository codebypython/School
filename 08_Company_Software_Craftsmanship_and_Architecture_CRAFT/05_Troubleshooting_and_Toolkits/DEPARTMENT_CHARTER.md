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

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN (DEBUGGING & REFACTORING INVARIANTS)

1. **Nguyên Tắc Không Thay Đổi Hành Vi Bên Ngoài (Behavior-Preserving)**:
   - Tái cấu trúc chỉ thay đổi cấu trúc bên trong của mã nguồn, tuyệt đối không làm thay đổi hành vi quan sát được từ bên ngoài.
2. **Nguyên Tắc "Chỉ Refactor Khi Test Đang Xanh" (Green-to-Green Rule)**:
   - Tuyệt đối không refactor khi đang có Unit Test bị đỏ (fail). Bắt buộc phải đưa toàn bộ test suite về trạng thái Green trước khi tiến hành refactor.
3. **Nguyên Tắc Bước Nhỏ (Baby Steps)**:
   - Mỗi bước tái cấu trúc phải cực kỳ nhỏ (đổi tên biến, tách 1 hàm 5 dòng), sau đó chạy lại test ngay lập tức. Nếu test gãy, `git checkout` quay lại ngay.

---

## 🛠️ 3. TOOLCHAIN & SKILLS ROUTE CHẨN ĐOÁN MÃ NGUỒN

| Mục Tiêu | Bộ Công Cụ Chuyên Dụng | Cú Pháp Thực Thi CLI |
| :--- | :--- | :--- |
| **Phân tích Tĩnh (Static Analysis)** | Ruff (Python), ESLint (TS), Clang-Tidy (C++) | `ruff check . --fix` / `eslint . --max-warnings=0` |
| **Kiểm thử Đột biến (Mutation Testing)**| Mutmut (Python), Stryker (JS/TS) | `mutmut run` / `npx stryker run` |
| **Đo lường Độ bao phủ (Coverage)** | Pytest-Cov, C8, Istanbul | `pytest --cov=app --cov-report=term-missing` |
| **Kiểm soát Kiểu nghiêm ngặt (Typing)** | Mypy Strict, TypeScript Compiler | `mypy --strict .` / `tsc --noEmit` |

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
05_Troubleshooting_and_Toolkits/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 refactoring_recipes/                  # Các công thức tái cấu trúc chuẩn hóa
│   ├── extract_class_recipe.md             # Hướng dẫn chi tiết kỹ thuật tách lớp
│   └── replace_conditional_with_polymorphism.md
└── 📁 test_triage_toolkits/                 # Bộ công cụ xử lý sự cố kiểm thử
    ├── detect_flaky_tests.py               # Script chạy lặp test case 100 lần tìm flakiness
    └── mock_audit_checklist.md             # Bảng kiểm tra chống lạm dụng Over-mocking
```

---

## 💻 5. MẪU KHUNG CODE CHẨN ĐOÁN & KIỂM THỬ ĐỘT BIẾN (BOILERPLATE TOOLKIT)

```python
# Script chẩn đoán: Tự động chạy lặp 50 lần để phát hiện Flaky Test
import subprocess
import sys


def detect_flaky_test(test_target: str, runs: int = 50) -> bool:
    print(f"[TEST TRIAGE] Bắt đầu quét Flaky Test cho target: {test_target}")
    for i in range(1, runs + 1):
        res = subprocess.run(
            ["pytest", "-q", test_target], capture_output=True, text=True
        )
        if res.returncode != 0:
            print(f"❌ Phát hiện FLAKY tại lần chạy thứ {i}/{runs}!")
            print(res.stdout)
            return False
    print(f"✅ Tuyệt đối ổn định! Vượt qua {runs}/{runs} lần thực thi.")
    return True
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU TÁI CẤU TRÚC (DEFINITION OF DONE - DoD)

Một ca tái cấu trúc mã nguồn được nghiệm thu khi:
- [ ] **DoD-1**: Toàn bộ Unit Test hiện hữu tiếp tục PASS (100% Green).
- [ ] **DoD-2**: Độ phức tạp Cyclomatic của các hàm liên quan giảm xuống dưới 10.
- [ ] **DoD-3**: Không phát sinh cảnh báo linter mới (`0 warnings`).
- [ ] **DoD-4**: Điểm Mutation Score (nếu có) không bị suy giảm.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & CẨM NANG ĐIỀU TRỊ CODE SMELLS (TOP 4 REFACTORING RUNBOOKS)

### 🚨 RUNBOOK 1: CHỮA TRỊ LỚP THẦN THÁNH (GOD CLASS / LARGE CLASS)
* **Triệu chứng**: Một lớp dài hàng trăm dòng, đảm nhận từ tính toán tiền tệ, xác thực người dùng đến ghi log và truy vấn database.
* **Kỹ thuật điều trị**:
  1. *Extract Class*: Tách các nhóm phương thức có cùng lý do thay đổi thành các lớp chuyên biệt mới.
  2. Áp dụng nguyên lý *Single Responsibility Principle (SRP)*: Mỗi lớp chỉ phục vụ 1 đối tượng nghiệp vụ (Actor).

---

### 🚨 RUNBOOK 2: KHỬ BỆNH ÁM ẢNH KIỂU NGUYÊN THỦY (PRIMITIVE OBSESSION)
* **Triệu chứng**: Sử dụng chuỗi trần `str` đại diện cho email, số điện thoại; dùng số thực `float` đại diện cho số tiền gây sai số dấu phẩy động.
* **Kỹ thuật điều trị**:
  1. Thay thế kiểu nguyên thủy bằng **Value Object** bất biến (Immutable Value Object).
  2. Đóng gói logic tự kiểm thực (Validation) ngay trong Constructor của Value Object.

---

### 🚨 RUNBOOK 3: XỬ LÝ GHEN TỊ TÍNH NĂNG (FEATURE ENVY)
* **Triệu chứng**: Một phương thức trong lớp A liên tục truy cập dữ liệu của lớp B để tính toán thay vì để lớp B tự thực hiện.
* **Kỹ thuật điều trị**:
  1. Áp dụng nguyên tắc *Tell, Don't Ask*.
  2. Sử dụng kỹ thuật *Move Method* để đưa phương thức về đúng lớp sở hữu dữ liệu đó.

---

### 🚨 RUNBOOK 4: CẤP CỨU FLAKY TEST DO PHỤ THUỘC THỜI GIAN
* **Triệu chứng**: Test fail ngẫu nhiên lúc nửa đêm hoặc khi chạy trên máy CI/CD do dùng `time.sleep()` hoặc gọi `datetime.now()` trực tiếp.
* **Kỹ thuật điều trị**:
  1. Trừu tượng hóa đồng hồ thời gian qua Interface: `ClockInterface` với phương thức `now()`.
  2. Trong môi trường test, tiêm `FakeClock` hoặc `FrozenClock` để kiểm soát thời gian hoàn toàn xác định (Deterministic).
