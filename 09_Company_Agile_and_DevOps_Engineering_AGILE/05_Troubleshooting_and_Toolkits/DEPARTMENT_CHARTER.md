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

## 🚑 2. CẨM NANG CỨU HỘ GIT KHẨN CẤP (TOP 4 GIT DISASTER RUNBOOKS)

---

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
* **Tình huống**: Đang chạy `git rebase` và xung đột nổ ra liên tục ở hàng chục commits khiến học viên bị hoảng loạn.
* **Quy trình xử lý an toàn**:
  - Tuyệt đối không xóa folder `.git`! Chỉ cần chạy:
    ```bash
    git rebase --abort
    ```
  - Git sẽ đưa nhánh trở lại trạng thái chính xác trước khi bắt đầu rebase mà không mất một byte dữ liệu nào.

---

### 🚨 RUNBOOK 3: GIẢI QUYẾT XUNG ĐỘT 3-WAY MERGE CHUẨN MỰC
* **Quy tắc vàng**: Khi mở trình giải quyết conflict, luôn xác định rõ 3 thành phần:
  - `Base`: Trạng thái commit chung gần nhất của cả 2 nhánh (Common Ancestor).
  - `Ours / Current`: Code trên nhánh hiện tại bạn đang đứng.
  - `Theirs / Incoming`: Code trên nhánh bạn đang kéo về hoặc rebase lên.
* **Lệnh kích hoạt trình giải quyết xung đột**:
  ```bash
  git mergetool
  # Sau khi giải quyết xong, tiếp tục luồng rebase/merge:
  git add <resolved_files>
  git rebase --continue
  ```

---

### 🚨 RUNBOOK 4: GỠ LỖI WORKFLOW GITHUB ACTIONS TRÊN LOCAL VỚI `act`
* **Tình huống**: Pipeline CI chạy trên GitHub bị fail nhưng không muốn push commit liên tục chỉ để test pipeline.
* **Khắc phục**:
  - Sử dụng công cụ `act` để chạy GitHub Actions runner ngay trên Docker local:
    ```bash
    act pull_request -j quality-gate
    ```
  - Quan sát log chi tiết trên máy tính cá nhân để sửa file YAML trước khi push lên remote.
