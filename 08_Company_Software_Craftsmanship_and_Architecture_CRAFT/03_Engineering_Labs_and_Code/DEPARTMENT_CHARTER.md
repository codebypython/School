# 📜 ĐIỀU LỆ PHÒNG KỸ THUẬT, TDD STARTERS & REFACTORING (ENGINEERING LABS & CODE DEPT)
## Phòng 03 — Công Ty Thiết Kế Phần Mềm & Kiến Trúc Hướng Đối Tượng (CORP-08-CRAFT)

> **Mã Phòng Ban:** `CRAFT-DEPT-03`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (`HM-00`) & Giám Sát Kỹ Thuật (`SMS-02`)  
> **Cố vấn chuyên môn:** DUT Software Craftsmanship & Architecture Mentor (`AGENT_PROFILE.md`)  
> **Tiêu chuẩn chất lượng:** Clean Architecture / 100% TDD / SOLID Strict Compliance / Pytest & Vitest

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kỹ Thuật & TDD là **xưởng rèn luyện tay nghề thủ công phần mềm (Craftsmanship Studio)**:
1. **Thực Hành Lập Trình Hướng Kiểm Thử (TDD Mastery)**: Cung cấp các kho bài tập dạng "Test-First". Học viên phải đọc hiểu requirement qua Unit Test, viết code tối thiểu để pass test (Green), và tái cấu trúc mã nguồn (Refactor).
2. **Triển Khai Mẫu 23 Gang of Four Design Patterns**: Xây dựng mã nguồn thực tế áp dụng các mẫu thiết kế hướng đối tượng hiện đại, chứng minh sự linh hoạt khi thay đổi yêu cầu nghiệp vụ.
3. **Phòng Thí Nghiệm Refactoring (Code Smells Laboratory)**: Cung cấp các đoạn code "bốc mùi" (Spaghetti Code, God Classes, Feature Envy) và hướng dẫn quy trình chuyển dịch an toàn sang Clean Architecture.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (AGENT BẮT BUỘC TUÂN THỦ)

1. **Chu Trình TDD Bất Biến (Red - Green - Refactor)**:
   - **BẮT BUỘC**: Viết Unit Test trước khi viết bất kỳ dòng mã logic nào.
   - Mỗi chu trình commit Git phải gồm 3 bước tách bạch:
     1. `test(unit): add failing test for [feature]` (RED).
     2. `feat(core): implement minimal logic to pass test` (GREEN).
     3. `refactor(core): clean up smells while keeping tests green` (REFACTOR).
2. **Quy Tắc Thiết Kế Hướng Đối Tượng (OOP & SOLID Hard Rules)**:
   - **CẤM TUYỆT ĐỐI**: Tạo "Lớp Thần Thánh" (God Class $> 300$ dòng code hoặc gộp quá 2 trách nhiệm nghiệp vụ).
   - **CẤM TUYỆT ĐỐI**: Kế thừa quá 2 cấp trừ khi là Abstract Base Classes / Interfaces. Bắt buộc áp dụng *Composition over Inheritance*.
   - **CẤM TUYỆT ĐỐI**: Tạo các Getter/Setter tự động làm mất tính đóng gói (vi phạm nguyên lý *Tell, Don't Ask*).
3. **Quy Tắc Kiểm Thử Hiện Đại (Modern Testing Constraints)**:
   - **CẤM TUYỆT ĐỐI**: Mock các lớp nghiệp vụ nội bộ (Private methods / Internal domain logic). Chỉ được mock ở ranh giới hệ thống (External APIs, Database, Network I/O).
   - Test Coverage bắt buộc đạt $\ge 85\%$ toàn diện (Line & Branch Coverage).

---

## 🛠️ 3. SKILLS ROUTE & TOOLCHAIN ĐIỀU HÀNH CHUẨN

### 3.1 Toolchain Yêu Cầu Đa Ngôn Ngữ
- **Python Stack**: Python 3.11+, `pytest`, `pytest-cov`, `pytest-mock`, `ruff`, `mypy`.
- **TypeScript Stack**: Node.js 20 LTS, `vitest`, `ts-node`, `eslint`, `prettier`.
- **C++ Stack**: GCC 13/Clang 17, `Catch2 v3`, `gMock`, `valgrind`.

### 3.2 Bộ Lệnh CLI Tác Nghiệp Chuẩn

```powershell
# --- PYTHON TDD WORKFLOW ---
# 1. Chạy toàn bộ Unit Tests với đo đạc độ bao phủ (Coverage)
pytest --cov=src --cov-report=term-missing --cov-fail-under=85

# 2. Chạy kiểm tra Code Smell & Static Analysis qua Ruff & Mypy
ruff check .
mypy src/ --strict

# --- TYPESCRIPT TDD WORKFLOW ---
# 1. Chạy Vitest ở chế độ theo dõi (Watch Mode)
pnpm vitest run --coverage

# 2. Kiểm tra định dạng và linter
pnpm eslint . --max-warnings=0
```

---

## 📁 4. CẤU TRÚC THƯ MỤC VÀ TÀI SẢN NỘI BỘ QUY CHUẨN

```
03_Engineering_Labs_and_Code/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 clean_architecture_template/          # Khung mẫu Clean Architecture chuẩn (Domain, Use Cases, Adapters)
│   ├── domain/                              # Entities & Value Objects bất biến
│   ├── use_cases/                           # Application Business Rules
│   └── adapters/                            # Controllers, Presenters, Gateways
├── 📁 labs/                                 # 15 Bài Lab phân kỳ TDD theo tuần
│   ├── Week01_Encapsulation_Invariants/
│   │   ├── README.md                        # Đề bài & Tiêu chí nghiệm thu
│   │   ├── test_bank_account.py             # Bộ test viết sẵn (Test-First)
│   │   └── bank_account.py                  # Mã nguồn học viên triển khai
│   ├── Week04_SOLID_Violations_Refactoring/
│   ├── Week07_Design_Patterns_Creational/
│   └── Week15_Capstone_Payment_Engine/      # Đồ án Cổng thanh toán đa kênh TDD
└── 📁 refactoring_catalog/                  # Kho mã nguồn "bốc mùi" phục vụ luyện tập
    ├── 01_spaghetti_order_service/
    └── 02_anemic_domain_model_fix/
```

---

## 💻 5. MẪU KHUNG CODE / TEMPLATE CHUẨN NGHIỆP VỤ (GOLD MASTER TDD BOILERPLATE)

Mẫu chuẩn mực minh họa **Domain Model bất biến + Bộ Test TDD** bằng Python:

```python
"""
Domain Model: Money Value Object & BankAccount Aggregate Root
Tuân thủ nguyên lý Domain-Driven Design (DDD), Tell Don't Ask & Clean Code.
"""
from dataclasses import dataclass
from decimal import Decimal
from typing import Self


@dataclass(frozen=True)
class Money:
    """Value Object bất biến đại diện cho tiền tệ."""
    amount: Decimal
    currency: str = "VND"

    def __post_init__(self) -> None:
        if self.amount < Decimal("0"):
            raise ValueError("Số tiền không được phép là số âm.")

    def add(self, other: Self) -> "Money":
        if self.currency != other.currency:
            raise ValueError(f"Không thể cộng 2 loại tiền khác nhau: {self.currency} và {other.currency}")
        return Money(self.amount + other.amount, self.currency)

    def subtract(self, other: Self) -> "Money":
        if self.currency != other.currency:
            raise ValueError("Không thể trừ 2 loại tiền khác nhau.")
        if self.amount < other.amount:
            raise ValueError("Số dư không đủ để thực hiện giao dịch trừ.")
        return Money(self.amount - other.amount, self.currency)


class BankAccount:
    """Aggregate Root bảo vệ toàn vẹn trạng thái (Invariant Protection)."""
    def __init__(self, account_id: str, initial_balance: Money) -> None:
        self._account_id = account_id
        self._balance = initial_balance
        self._is_active = True

    @property
    def balance(self) -> Money:
        """Chỉ cung cấp quyền đọc (Read-only property), không có public setter."""
        return self._balance

    def deposit(self, amount: Money) -> None:
        """Tell, Don't Ask: Yêu cầu tài khoản tự nạp tiền và kiểm tra tính hợp lệ."""
        if not self._is_active:
            raise RuntimeError("Tài khoản đã bị khóa, không thể nạp tiền.")
        self._balance = self._balance.add(amount)

    def withdraw(self, amount: Money) -> None:
        """Tell, Don't Ask: Yêu cầu tài khoản tự rút tiền và kiểm tra số dư."""
        if not self._is_active:
            raise RuntimeError("Tài khoản đã bị khóa, không thể rút tiền.")
        self._balance = self._balance.subtract(amount)
```

**Bộ Test TDD Tương Ứng (`test_bank_account.py`)**:
```python
import pytest
from decimal import Decimal
from bank_account import BankAccount, Money


def test_cannot_create_negative_money():
    """Kiểm tra Value Object Money không bao giờ có giá trị âm."""
    with pytest.raises(ValueError, match="không được phép là số âm"):
        Money(Decimal("-1000"))


def test_deposit_increases_balance_correctly():
    """Kiểm tra việc nạp tiền làm tăng số dư an toàn."""
    account = BankAccount("ACC-001", Money(Decimal("50000")))
    account.deposit(Money(Decimal("20000")))
    assert account.balance.amount == Decimal("70000")


def test_withdraw_insufficient_funds_raises_error():
    """Kiểm tra rút tiền vượt quá số dư bị chặn đứng."""
    account = BankAccount("ACC-001", Money(Decimal("10000")))
    with pytest.raises(ValueError, match="Số dư không đủ"):
        account.withdraw(Money(Decimal("50000")))
```

---

## 🛡️ 6. BỘ TIÊU CHÍ NGHIỆM THU CHẤT LƯỢNG (DEFINITION OF DONE - DoD)

- [ ] **DoD-1 (100% Test-Driven)**: Toàn bộ chức năng đều có Unit Test kiểm chứng trước.
- [ ] **DoD-2 (Zero Code Smells)**: Không tồn tại God Class, Feature Envy, Long Method ($> 25$ dòng).
- [ ] **DoD-3 (Test Coverage $\ge 85\%$)**: Báo cáo `pytest --cov` hoặc `vitest --coverage` đạt từ 85% trở lên.
- [ ] **DoD-4 (Strict Typing)**: 100% Type Annotations, kiểm tra `mypy --strict` (Python) hoặc `tsc --noEmit` (TypeScript) không có lỗi.
- [ ] **DoD-5 (Linter Clean)**: Đạt 0 cảnh báo từ `ruff` hoặc `eslint`.
