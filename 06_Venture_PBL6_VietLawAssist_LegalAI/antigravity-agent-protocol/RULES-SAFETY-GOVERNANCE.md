# MASTER RULES & SAFETY GOVERNANCE PROTOCOL
> **Vị trí tài liệu:** `d:\Development\TDD concept\antigravity-agent-protocol\RULES-SAFETY-GOVERNANCE.md`  
> **Mục đích:** Thiết lập toàn bộ quy tắc bất khả xâm phạm, kiểm soát rủi ro, bảo mật, chất lượng kỹ nghệ phần mềm và quy chuẩn báo cáo bàn giao phiên cho AI Agents.

---

## 1. QUY TẮC AN TOÀN THỰC THI TERMINAL (TERMINAL GOVERNANCE)

Agent khi vận hành terminal trong Antigravity IDE / Antigravity 2.0 phải tuân thủ nghiêm ngặt bảng phân loại lệnh sau:

### 🚫 DANH SÁCH ĐEN (CẤM TUYỆT ĐỐI NẾU KHÔNG CÓ XÁC NHẬN RÕ RÀNG)
Agent **KHÔNG ĐƯỢC PHÉP** tự ý chạy các lệnh sau ở chế độ tự động (`always-proceed`):
- `git reset --hard` hoặc `git clean -fd` (Nguy cơ xóa sạch toàn bộ mã nguồn đang làm).
- `git push --force` hoặc `git push --no-verify` (Nguy cơ ghi đè mã nguồn của đồng đội hoặc bỏ qua kiểm thử bảo mật).
- `rm -rf /` hoặc xóa đệ quy các thư mục gốc, thư mục dự án bên ngoài workspace.
- Tự ý chạy lệnh cài đặt package mới (`npm install <package>`, `pip install <package>`) mà không giải thích lý do cần thiết cho người dùng trước.
- Các lệnh kill tiến trình không xác định hoặc tắt firewall/antivirus.

### 🟢 DANH SÁCH TRẮNG (AN TOÀN ĐƯỢC PHÉP CHẠY TỰ ĐỘNG)
- Lệnh kiểm tra trạng thái: `git status`, `git diff`, `git log -n 5`, `git branch`.
- Lệnh kiểm thử & Build: `npm test`, `npm run build`, `pytest`, `cargo check`, `go test ./...`.
- Lệnh đọc thông tin hệ thống & file: `ls`, `dir`, `node -v`, `python --version`.

---

## 2. QUY TẮC CHỈNH SỬA TỆP & CHỐNG GHI ĐÈ SAI LỆCH (FILE INTEGRITY)

1. **Bảo tồn tính toàn vẹn (Documentation & Type Integrity):**
   - Giữ nguyên 100% các chú thích (comments), docstrings, type definitions và cấu trúc sẵn có không liên quan trực tiếp đến sửa đổi.
   - Tuyệt đối không xóa code cũ rồi thay bằng placeholder dạng `// ... TODO: implement remaining logic ...`.
2. **Ưu tiên chỉnh sửa cục bộ (Targeted Replacement):**
   - Luôn sử dụng tool thay thế từng khối (`replace_file_content` hoặc `multi_replace_file_content`) thay vì ghi đè toàn bộ tệp (`write_to_file`) đối với các file lớn đang hoạt động ổn định.
   - Bắt buộc kiểm tra chỉ số dòng chính xác trước khi thực hiện thay thế để tránh lệch dòng (Line Mismatch).
3. **Cấm sinh tệp rác bừa bãi:**
   - Không tự ý tạo các file thử nghiệm như `test.js`, `temp.py`, `dummy.json` ở root workspace. Mọi file scratch phải nằm trong thư mục tạm được quy định.

---

## 3. QUY TẮC AN TOÀN THÔNG TIN & BẢO MẬT (SECOPS RULES)

Agent phải hoạt động như một chuyên gia An toàn thông tin:
1. **Zero Secrets in Code:**
   - Tuyệt đối không bao giờ hardcode API Keys, Passwords, Private Keys, JWT Secrets vào mã nguồn.
   - Mọi thông tin nhạy cảm phải nạp qua biến môi trường (`process.env`, `os.environ`).
   - Kiểm tra tệp `.gitignore` luôn có `.env`, `.env.local`, `*.pem`, `*.key`.
2. **Phòng chống OWASP Top 10:**
   - **SQL Injection:** 100% câu truy vấn phải dùng Parameterized Queries / Prepared Statements hoặc ORM an toàn. Cấm nối chuỗi câu lệnh SQL.
   - **XSS (Cross-Site Scripting):** Mọi dữ liệu người dùng render lên giao diện phải được escape/sanitize (dùng DOMPurify hoặc React JSX an toàn).
   - **Authentication:** Lưu trữ token xác thực trong `httpOnly`, `Secure`, `SameSite=Strict` Cookies thay vì lưu ở `localStorage`.
   - **Input Validation:** Xác thực và ép kiểu (Schema Validation với Zod, Pydantic, Joi) ngay tại tầng Controller/Handler.

---

## 4. QUY TẮC CHẤT LƯỢNG KỸ NGHỆ PHẦN MỀM (CLEAN CODE & TDD)

1. **Tuân thủ quy trình TDD (Test-Driven Development):**
   - Viết bài kiểm thử thất bại trước (🔴 RED) $\rightarrow$ Viết mã tối thiểu để vượt qua bài test (🟢 GREEN) $\rightarrow$ Tối ưu và tái cấu trúc mã (🔵 REFACTOR).
2. **Nguyên tắc thiết kế SOLID & Clean Architecture:**
   - **Single Responsibility (SRP):** Mỗi hàm/class chỉ làm một nhiệm vụ duy nhất (hàm không dài quá 25-30 dòng).
   - **DRY & KISS:** Không lặp lại logic; giữ giải pháp đơn giản, không over-engineering.
   - **Phân tầng rõ ràng:** Tách biệt Controller $\rightarrow$ Service / Business Logic $\rightarrow$ Repository / Data Access.
3. **Quy chuẩn mã nguồn Machine Learning / PyTorch:**
   - Code phải độc lập thiết bị (`device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')`).
   - Khóa toàn bộ random seed để tái lập kết quả (`torch.manual_seed(42)`).
   - Chú thích rõ ràng Tensor Shape ở mỗi forward step `(batch_size, channels, H, W)`.

---

## 5. QUY TẮC BÁO CÁO TÓM TẮT PHIÊN LÀM VIỆC (SESSION HANDOVER REPORT)

> [!IMPORTANT]
> **Quy định bắt buộc:** Khi hoàn thành một nhiệm vụ hoặc kết thúc một phiên chat, Agent **BẮT BUỘC** phải tự động tạo một **Bản Báo Cáo Tóm Tắt Bàn Giao (Session Handover Card)** ở cuối phản hồi. Bản báo cáo này được thiết kế để người dùng có thể sao chép ngay gửi cho Tech Lead, giảng viên hướng dẫn hoặc bạn cùng nhóm.

### Định dạng Mẫu Báo Cáo Bàn Giao (Session Handover Card):

```markdown
---
## 📝 BẢN BÁO CÁO TỔNG KẾT PHIÊN LÀM VIỆC (SESSION HANDOVER)
**Thời gian thực hiện:** [Ngày/Giờ]  
**Nhánh Git:** `[Tên nhánh]` | **Mã Commit:** `[Commit Hash ngắn]`  
**Mục tiêu phiên:** [Mô tả ngắn gọn 1 câu về bài toán đã giải quyết]

### 1. 🛠️ Các thay đổi đã thực hiện:
- `[NEW]` `src/services/authService.ts`: Xây dựng logic OAuth2 Google Login.
- `[MODIFY]` `src/controllers/authController.ts`: Bổ sung endpoint `/api/auth/google/callback`.
- `[NEW]` `tests/unit/authService.test.ts`: 4 unit tests kiểm thử luồng xác thực.

### 2. 🧪 Kết quả Kiểm thử & Chất lượng (Verification):
- **Unit Tests:** 4/4 tests passed (100% pass rate).
- **Security Check:** Đã xác thực token bằng JWT qua HttpOnly Cookie, không rò rỉ secret.
- **Lint / Build:** `npm run build` thành công, không có lỗi type.

### 3. ⚠️ Những lưu ý kỹ thuật quan trọng cho người tiếp quản:
- Cần bổ sung biến `GOOGLE_CLIENT_ID` và `GOOGLE_CLIENT_SECRET` vào file `.env.local` trên máy local trước khi test giao diện.
- Đã cấu hình timeout cho OAuth request là 5000ms.

### 4. 📌 Bước tiếp theo đề xuất (Next Steps):
1. Kết nối giao diện nút bấm Google Login trên Frontend (`src/components/LoginModal.tsx`).
2. Viết kiểm thử E2E với Playwright.
---
```

---

## 6. BỘ CÔNG CỤ HỖ TRỢ GIT NHANH (QUICK GIT HELPERS)

Agent và người dùng có thể sử dụng các lệnh một dòng (one-liners) tiện dụng này để xử lý nhanh các tình huống Git trong quá trình làm việc:

```powershell
# 1. TẠO CHECKPOINT NHANH TRƯỚC KHI AI CODE (Cứu cánh an toàn):
git add . ; git commit -m "checkpoint: save state before AI changes"

# 2. XÓA BỎ VÀ ROLLBACK TOÀN BỘ CODE AI VỪA LÀM SAI (Khôi phục tức thì):
git reset --hard HEAD

# 3. TẠO STASH TẠM THỜI ĐỂ THỬ NGHIỆM Ý TƯỞNG MỚI:
git stash save "wip: save current work"
# Khôi phục lại:
git stash pop

# 4. TẠO VÀ CHUYỂN SANG NHÁNH FEATURE MỚI:
git checkout -b feature/ten-tinh-nang-moi

# 5. XEM NHANH CÁC FILE VỪA BỊ THAY ĐỔI (Tránh sót file rác):
git status --short

# 6. COMMIT CHUẨN CONVENTIONAL COMMITS:
git add . ; git commit -m "feat(auth): add google oauth2 login service with unit tests"
```
