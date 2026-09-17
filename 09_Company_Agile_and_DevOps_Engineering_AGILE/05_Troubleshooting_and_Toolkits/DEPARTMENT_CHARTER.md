# 📜 ĐIỀU LỆ PHÒNG KIỂM SOÁT XUNG ĐỘT GIT & SỰ CỐ CI/CD (TROUBLESHOOTING & TOOLKITS DEPT)
## Phòng 05 — Công Ty Quy Trình Phần Mềm & Kỹ Nghệ Agile/DevOps (CORP-09-AGILE)

> **Mã Phòng Ban:** `AGILE-DEPT-05`  
> **Trưởng phòng phụ trách:** Agent `SMS-02` (Syllabus Sentinel & Technical Auditor)  
> **Thẩm quyền kỹ thuật:** Cứu hộ dữ liệu Git (Git Disaster Recovery), Giải quyết xung đột 3-Way Merge, Điều tra sự cố CI Runner  
> **Bộ công cụ cốt lõi:** `git reflog` / VS Code 3-Way Merge Editor / GitHub Actions Logs / Act (Local GitHub Actions Runner)

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Cứu Hộ Git & DevOps là **"Trạm Cứu Hỏa Kỹ Thuật"** cho quy trình làm việc nhóm:
1. **Cứu Hộ Dữ Liệu Git (Git Disaster Recovery)**: Khôi phục các commits, branches hoặc stashes bị xóa nhầm hoặc bị ghi đè sau các thao tác rebase/reset sai lầm.
2. **Xử Lý Xung Đột Mã Nguồn Nâng Cao (Conflict Resolution)**: Cung cấp quy trình 3-way merge logic ngăn chặn việc vô tình xóa code của đồng đội khi giải quyết merge conflict.
3. **Chẩn Đoán Lỗi CI/CD Runner**: Điều tra nguyên nhân pipeline thất bại (Flaky tests, thiếu biến môi trường Secrets, lỗi cache dependencies, timeout).

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN (DEBUGGING INVARIANTS)

1. **Nguyên Tắc Bình Tĩnh & Không Xóa Thư Mục `.git` (No Panic Invariant)**:
   - Nghiêm cấm xóa thư mục `.git` hoặc clone lại từ đầu khi gặp xung đột. Mọi dữ liệu đã commit đều được Git bảo toàn trong Object Database.
2. **Nguyên Tắc Không Dùng `git push --force` Mù Quáng**:
   - Nếu bắt buộc phải push lịch sử rebase, chỉ được phép sử dụng `git push --force-with-lease` để bảo vệ commit của người khác.
3. **Nguyên Tắc Sao Lưu Trước Khi Rebase Lớn (Safety Branch Rule)**:
   - Trước khi thực hiện interactive rebase phức tạp, luôn tạo nhánh tạm: `git branch backup-before-rebase`.

---

## 🛠️ 3. TOOLCHAIN & SKILLS ROUTE CỨU HỘ GIT & CI/CD

| Sự Cố / Tình Huống | Công Cụ Cứu Hộ | Lệnh CLI Kích Hoạt |
| :--- | :--- | :--- |
| **Mất Commit / Nhánh** | `git reflog` | `git reflog` $\rightarrow$ `git reset --hard HEAD@{N}` |
| **Kẹt phiên Rebase / Merge** | Git CLI Abort | `git rebase --abort` / `git merge --abort` |
| **Lỡ commit Secret / Token** | BFG Repo-Cleaner / `git-filter-repo` | `bfg --replace-text passwords.txt` |
| **Test cục bộ GitHub Actions** | Nektos Act | `act pull_request` |

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
05_Troubleshooting_and_Toolkits/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 recovery_scripts/                     # Kịch bản cứu hộ tự động
│   ├── find_dangling_commits.sh            # Script quét commits mồ côi qua fsck
│   └── purge_secrets_history.sh            # Script lọc sạch token lộ trong git history
└── 📁 disaster_runbooks/                    # Sổ tay cứu hộ khẩn cấp
    ├── git_merge_conflict_guide.md
    └── github_actions_debugging_guide.md
```

---

## 💻 5. MẪU KHUNG CODE CHẨN ĐOÁN & SỬA LỖI GIT (BOILERPLATE TOOLKIT)

```bash
#!/usr/bin/env bash
# Script chẩn đoán: Tự động kiểm tra tính toàn vẹn của Git Repo và tìm dangling commits
set -euo pipefail

echo "[GIT DIAGNOSTICS] Đang quét Git Object Database..."
git fsck --lost-found | while read -r line; do
    if [[ $line == *"dangling commit"* ]]; then
        commit_hash=$(echo "$line" | awk '{print $3}')
        echo "🔍 Tìm thấy Dangling Commit: $commit_hash"
        git log -1 --format="   Author: %an | Date: %ad | Subject: %s" "$commit_hash"
    fi
done
echo "✅ Hoàn tất kiểm tra!"
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU CỨU HỘ (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: Khôi phục 100% mã nguồn bị mất mà không làm rụng lịch sử commit quan trọng.
- [ ] **DoD-2**: Xung đột merge conflict được giải quyết triệt để, chạy test pass trước khi commit.
- [ ] **DoD-3**: Không để lộ bất kỳ file conflict markers nào (`<<<<<<<`, `=======`, `>>>>>>>`) trong codebase.
- [ ] **DoD-4**: Pipeline CI trên GitHub Actions chuyển sang trạng thái Green sau khi xử lý.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & CẨM NANG CỨU HỘ GIT (TOP 4 GIT RUNBOOKS)

### 🚨 RUNBOOK 1: KHÔI PHỤC COMMIT BỊ MẤT QUA `git reflog`
* **Tình huống**: Học viên vô tình chạy `git reset --hard HEAD~3` và mất toàn bộ các commit vừa làm trong ngày.
* **Quy trình cứu hộ 3 bước**:
  1. *Bước 1 - Xem lịch sử con trỏ HEAD*:
     ```bash
     git reflog
     ```
     Tìm dòng commit trước thời điểm chạy lệnh reset (Ví dụ: `HEAD@{1}: commit: feat: implement payment gateway`).
  2. *Bước 2 - Khôi phục trạng thái*:
     ```bash
     git reset --hard HEAD@{1}
     ```
  3. Toàn bộ code và commit đã trở lại nguyên vẹn!

---

### 🚨 RUNBOOK 2: HỦY BỎ MỘT PHIÊN REBASE BỊ RỐI LOẠN (ABORT REBASE)
* **Tình huống**: Đang rebase nhánh tính năng thì gặp hàng chục file xung đột, terminal rơi vào trạng thái `(main|REBASE 1/5)`.
* **Khắc phục an toàn**:
  ```bash
  git rebase --abort
  ```
  Nhánh sẽ quay trở lại trạng thái chính xác trước khi gõ lệnh rebase.

---

### 🚨 RUNBOOK 3: XỬ LÝ XUNG ĐỘT 3-WAY MERGE CONFLICT
* **Tình huống**: Git thông báo `CONFLICT (content): Merge conflict in src/app.py`.
* **Khắc phục**:
  1. Mở editor (VS Code / JetBrains) để xem 3 phần: *Current Change* (code của mình), *Incoming Change* (code của đồng đội), và *Common Ancestor*.
  2. Bàn bạc với đồng đội để quyết định giữ lại logic nào, xóa sạch các ký hiệu `<<<<<<<`, `=======`, `>>>>>>>`.
  3. Chạy `git add src/app.py` và `git commit -m "fix: resolve merge conflict in app.py"`.

---

### 🚨 RUNBOOK 4: XỬ LÝ LỖI GITHUB ACTIONS THIẾU SECRETS
* **Triệu chứng**: Pipeline CI fail ngay bước kết nối database hoặc deploy với lỗi `Authentication failed / Token not found`.
* **Khắc phục**:
  1. Kiểm tra tab Settings > Secrets and variables > Actions của repository.
  2. Đối chiếu tên biến trong workflow `${{ secrets.MY_SECRET }}` với tên cấu hình trên GitHub (phải khớp từng ký tự viết hoa).
