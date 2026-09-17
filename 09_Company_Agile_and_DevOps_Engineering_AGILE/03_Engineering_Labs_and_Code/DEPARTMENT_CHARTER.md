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

## 📁 4. CẤU TRÚC THƯ MỤC VÀ TÀI SẢN NỘI BỘ QUY CHUẨN

```
03_Engineering_Labs_and_Code/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 workflows_template/                   # Thư viện GitHub Actions chuẩn
│   ├── .github/workflows/
│   │   ├── ci.yml                           # Pipeline kiểm thử & lint tự động
│   │   └── security_scan.yml                # Quét lỗ hổng dependency qua Trivy
│   └── .pre-commit-config.yaml              # Cấu hình Git Pre-commit hooks
├── 📁 labs/                                 # 15 Bài Lab phân kỳ theo tuần
│   ├── Week01_Git_Internals_DAG/
│   ├── Week05_Branching_Conflict_Rebase/
│   ├── Week09_GitHub_Actions_CI_Pipeline/
│   └── Week15_Capstone_DevOps_Delivery/
└── 📁 scripts/                              # Kịch bản tự động hóa DevOps
    ├── simulate_git_conflict.sh             # Tự động tạo kịch bản merge conflict
    └── verify_conventional_commit.py        # Hook kiểm tra thông điệp commit
```

---

## 💻 5. MẪU KHUNG CI/CD PIPELINE CHUẨN NGHIỆP VỤ (GOLD MASTER WORKFLOW)

```yaml
name: Production CI Quality Gate

on:
  pull_request:
    branches: [main]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  quality-checks:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Runtime Environment
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - name: Install Dependencies
        run: pnpm install --frozen-lockfile

      - name: Static Type Check
        run: pnpm tsc --noEmit

      - name: Linter Verification
        run: pnpm eslint . --max-warnings=0

      - name: Run Automated Test Suite
        run: pnpm vitest run --coverage

      - name: Enforce Coverage Threshold (>= 85%)
        run: npx nyc check-coverage --lines 85
```

---

## 🛡️ 6. BỘ TIÊU CHÍ NGHIỆM THU CHẤT LƯỢNG (DEFINITION OF DONE - DoD)

- [ ] **DoD-1 (Linear Git History)**: Nhánh PR được rebase sạch sẽ, không có merge commit rác `Merge branch 'main' into ...`.
- [ ] **DoD-2 (Green Pipeline)**: Toàn bộ jobs trong GitHub Actions đều xanh (Pass).
- [ ] **DoD-3 (Peer Reviewed)**: Có tối thiểu 1 Approved Review từ đồng đội trước khi merge.
- [ ] **DoD-4 (Signed Commits)**: 100% commit được ký số bằng GPG Key hợp lệ.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK CẤP CỨU GIT & CI/CD (GIT EMERGENCY RUNBOOK)

Khi gặp thảm họa Git hoặc Pipeline bị tắc nghẽn:
1. **Lỡ Push Nhầm Secret / Password Lên Git**:
   - Ngay lập tức thu hồi (Revoke) secret đó trên dashboard của dịch vụ.
   - Sử dụng `git-filter-repo` hoặc BFG Repo-Cleaner để xóa sạch secret khỏi toàn bộ lịch sử Git commits.
   - Force push với lease: `git push --force-with-lease`.
2. **Khôi Phục Commit Bị Mất (Lost Commits via Reflog)**:
   - Chạy lệnh `git reflog` để tìm mã hash SHA-1 của commit trước khi bị rebase/reset nhầm.
   - Khôi phục lại nhánh: `git checkout -b rescue-branch <commit-hash>`.
3. **Pipeline CI Bị Đơ Vô Hạn (Hung Jobs)**:
   - Bổ sung `timeout-minutes: 10` vào từng job trong workflow `.github/workflows/ci.yml` để tự động ngắt kết nối.
