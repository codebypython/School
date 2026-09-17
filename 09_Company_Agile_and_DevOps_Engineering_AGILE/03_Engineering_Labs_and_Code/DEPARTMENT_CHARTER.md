# 📜 ĐIỀU LỆ PHÒNG KỸ THUẬT, CI/CD WORKFLOWS & GIT REPOS (ENGINEERING LABS & CODE DEPT)
## Phòng 03 — Công Ty Quy Trình Phần Mềm & Kỹ Nghệ Agile/DevOps (CORP-09-AGILE)

> **Mã Phòng Ban:** `AGILE-DEPT-03`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (`HM-00`) & Giám Sát Kỹ Thuật (`SMS-02`)  
> **Cố vấn chuyên môn:** DUT Agile & DevOps Engineering Mentor (`AGENT_PROFILE.md`)  
> **Tiêu chuẩn chất lượng:** Git Conventional Commits / Trunk-Based CI / GitHub Actions / DORA Metrics

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kỹ Thuật & CI/CD là **trung tâm tự động hóa quy trình và tích hợp liên tục**:
1. **Thiết Lập Môi Trường Git Nâng Cao**: Tạo lập các kịch bản thực hành Git phân nhánh phức tạp, kịch bản tạo xung đột (merge conflicts) và hướng dẫn kỹ thuật rebase an toàn.
2. **Xây Dựng Cổng Kiểm Soát Chất Lượng Tự Động (Quality Gates)**: Cấu hình Pre-commit hooks trên máy local để tự động định dạng và kiểm tra linter trước khi cho phép commit.
3. **Phát Triển CI/CD Pipelines**: Viết các tệp cấu hình GitHub Actions Workflows tự động kiểm thử, quét lỗ hổng bảo mật và đóng gói ứng dụng khi có Pull Request.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (AGENT BẮT BUỘC TUÂN THỦ)

1. **Quy Tắc Thông Điệp Commit (Conventional Commits 1.0.0 Bắt Buộc)**:
   - Cú pháp: `<type>(<scope>): <short description>`
   - Các types hợp lệ: `feat`, `fix`, `refactor`, `test`, `docs`, `style`, `perf`, `chore`.
   - **CẤM TUYỆT ĐỐI**: Commit với thông điệp chung chung: `update`, `fix bug`, `done`, `test commit`.
2. **Quy Tắc Nhánh Git & Bảo Vệ Nhánh (Branch Protection Rules)**:
   - **CẤM TUYỆT ĐỐI**: Commit hoặc push trực tiếp vào nhánh `main` hoặc `master`.
   - Mọi thay đổi bắt buộc phải qua nhánh tính năng: `feature/<name>`, `bugfix/<name>`.
   - **CẤM TUYỆT ĐỐI**: Chạy lệnh `git push --force` trên các nhánh công khai dùng chung.
3. **Quy Tắc Tự Động Hóa (Automated Quality Gate Invariant)**:
   - Không một Pull Request nào được phép merge nếu pipeline CI chạy thất bại hoặc có bất kỳ bài test nào bị fail.

---

## 🛠️ 3. SKILLS ROUTE & TOOLCHAIN ĐIỀU HÀNH CHUẨN

### 3.1 Bộ Lệnh CLI Tác Nghiệp Git Nâng Cao

```bash
# 1. Bắt đầu tính năng mới từ nhánh main mới nhất
git checkout main
git pull origin main
git checkout -b feature/user-authentication

# 2. Cập nhật nhánh tính năng với main bằng Rebase (giữ lịch sử tuyến tính)
git fetch origin
git rebase origin/main

# 3. Gom 4 commit thừa thành 1 commit duy nhất trước khi mở PR
git rebase -i HEAD~4

# 4. Kiểm tra lịch sử commit trực quan dạng đồ thị
git log --graph --oneline --decorate --all -n 10
```

---

## 💻 4. MẪU KHUNG CI/CD PIPELINE CHUẨN NGHIỆP VỤ (GOLD MASTER WORKFLOW)

Tệp workflow `.github/workflows/ci.yml` chuẩn mực tích hợp Linter, Security Scan và Automated Tests:

```yaml
name: Continuous Integration Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  quality-gate:
    name: Code Quality & Automated Tests
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11"]

    steps:
      - name: 📥 Checkout Repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Kéo toàn bộ lịch sử phục vụ commitlint

      - name: 🐍 Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'pip'

      - name: 📦 Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install ruff mypy pytest pytest-cov

      - name: 🔍 Run Ruff Linter & Formatter Check
        run: |
          ruff check .
          ruff format --check .

      - name: 🛡️ Run Static Type Checker (Mypy Strict)
        run: |
          mypy src/ --strict

      - name: 🧪 Run Unit & Integration Tests with Coverage Gate
        run: |
          pytest --cov=src --cov-report=term --cov-fail-under=85
```

---

## 🛡️ 5. BỘ TIÊU CHÍ NGHIỆM THU CHẤT LƯỢNG (DEFINITION OF DONE - DoD)

- [ ] **DoD-1 (100% Conventional Commits)**: Mọi commit đều đúng chuẩn `feat:`, `fix:`, v.v.
- [ ] **DoD-2 (PR Template Đầy Đủ)**: Có mô tả mục tiêu thay đổi, ảnh chụp màn hình kiểm chứng và checklist kiểm thử.
- [ ] **DoD-3 (CI Pipeline Green)**: Pipeline GitHub Actions chạy pass 100% các bước linter, typecheck và tests.
- [ ] **DoD-4 (Branch Up-To-Date)**: Nhánh tính năng đã được rebase mới nhất với `origin/main` không có conflict.
