# CẨM NANG 10 KỊCH BẢN THỰC CHIẾN VỚI ECC & SKILL ROUTER
> **Vị trí tài liệu:** `d:\Development\TDD concept\antigravity-agent-protocol\ECC-ROUTER-10-SCENARIOS-GUIDE.md`  
> **Mục đích:** Hướng dẫn chi tiết cách khai thác 183 skills của Everything Claude Code (ECC) qua công cụ `skill-router` cho 10 tình huống phát triển thực tế, kèm Khung Mẫu Kịch Bản Chuẩn để mở rộng kịch bản mới.

---

## 🛠️ CƠ CHẾ ĐIỀU PHỐI SKILL ROUTER TỔNG QUAN

Trước khi đi vào từng kịch bản, ghi nhớ 2 lệnh điều phối cốt lõi chạy tại thư mục dự án của bạn:
```powershell
# 1. Quét nhận diện công nghệ & tạo file cấu hình .agent-skills.json
node D:\Development\tools\skill-router\skill-router.js init

# 2. Sinh các file quy chuẩn nạp lười cho Cursor (.mdc) và Antigravity (.gemini/)
node D:\Development\tools\skill-router\skill-router.js inject
```

---

## PHẦN I: 10 KỊCH BẢN THỰC CHIẾN CHI TIẾT

---

### 🟢 KỊCH BẢN 1: DỰ ÁN MỚI TOANH (GREENFIELD) — CHƯA CÓ CODE, CHƯA CÓ PLAN
* **Tình huống:** Bắt đầu đồ án hoặc dự án startup từ con số 0.
* **Skills trọng tâm:** `coding-standards`, `tdd-workflow`, `api-design`, `architecture-decision-records`.
* **Quy trình thực hiện:**
  1. Khởi tạo thư mục và `git init`.
  2. Tạo file `package.json` hoặc `requirements.txt` cơ bản rồi chạy `skill-router init` và `skill-router inject`.
  3. Mở Box Chat Antigravity, gửi Prompt: *"Đọc STEP-0-SESSION-ONBOARDING.md. Hãy đóng vai trò Solution Architect để thiết kế cấu trúc thư mục, định nghĩa Model dữ liệu và tạo Implementation Plan ban đầu."*
  4. Duyệt bản kế hoạch $\rightarrow$ Bắt đầu khởi tạo khung dự án (Boilerplate).

---

### 🟢 KỊCH BẢN 2: DỰ ÁN ĐÃ CÓ CODEBASE LỚN — THÊM TÍNH NĂNG MỚI
* **Tình huống:** Dự án đang chạy, cần mở rộng 1 module thanh toán hoặc phân quyền mới.
* **Skills trọng tâm:** `backend-patterns`, `frontend-patterns`, `database-migrations`, `verification-loop`.
* **Quy trình thực hiện:**
  1. Tạo nhánh Git mới: `git checkout -b feature/new-module`.
  2. Chạy `skill-router inject` để đảm bảo skills phù hợp với tech stack hiện có.
  3. Prompt cho Agent: *"Đọc STEP-0-SESSION-ONBOARDING.md và file @schema.prisma. Tôi muốn thêm module thanh toán VNPAY. Hãy kiểm tra các file bị ảnh hưởng, báo cáo context budget và lập kế hoạch các endpoint cần tạo."*
  4. Thực thi từng endpoint theo chu trình TDD.

---

### 🟢 KỊCH BẢN 3: DỰ ÁN ĐÃ CÓ PLAN TỪ TRƯỚC — CHỈ CẦN THỰC THI CHÍNH XÁC
* **Tình huống:** Tech Lead hoặc nhóm đã chốt tài liệu `implementation_plan.md`, cần AI code chính xác theo spec.
* **Skills trọng tâm:** `tdd-workflow`, `coding-standards`, `verification-loop`.
* **Quy trình thực hiện:**
  1. Ghim file kế hoạch: `@implementation_plan.md`.
  2. Prompt cho Agent: *"Đọc STEP-0-SESSION-ONBOARDING.md và tuân thủ tuyệt đối các bước trong @implementation_plan.md. Bắt đầu thực thi Task 1.1: Viết Unit Test trước (RED), sau đó viết code triển khai (GREEN). Tuyệt đối không tự ý thêm tính năng ngoài plan."*
  3. Duyệt từng bước cho đến khi hoàn tất checklist.

---

### 🟢 KỊCH BẢN 4: DỰ ÁN ĐANG CHẠY CẦN ĐIỀU CHỈNH / SỬA LẠI PLAN (MID-COURSE CORRECTION)
* **Tình huống:** Khi đang code phát hiện API bên thứ 3 thay đổi hoặc yêu cầu nghiệp vụ thay đổi đột ngột.
* **Skills trọng tâm:** `architecture-decision-records`, `strategic-compact`, `verification-loop`.
* **Quy trình thực hiện:**
  1. Tạo checkpoint an toàn: `git commit -m "checkpoint: before updating plan"`.
  2. Prompt cho Agent: *"Dừng thực thi code. Hiện tại phương thức xác thực thay đổi từ Session Cookie sang JWT Bearer Token. Hãy phân tích các xung đột với plan cũ, cập nhật lại @implementation_plan.md và báo cáo sự thay đổi."*
  3. Người dùng duyệt plan mới $\rightarrow$ Chạy lệnh `/compact` để làm sạch context cũ $\rightarrow$ Tiếp tục thực thi.

---

### 🟢 KỊCH BẢN 5: XỬ LÝ SỰ CỐ KHẨN CẤP (EMERGENCY DEBUGGING / HOTFIX)
* **Tình huống:** Hệ thống báo lỗi 500, crash server hoặc rò rỉ bộ nhớ.
* **Skills trọng tâm:** `agent-introspection-debugging`, `terminal-ops`, `connections-optimizer`.
* **Quy trình thực hiện:**
  1. Sao chép đoạn log lỗi từ terminal hoặc Sentry/CloudWatch.
  2. Prompt cho Agent: *"Đọc STEP-0-SESSION-ONBOARDING.md. Đây là log lỗi hệ thống: `[Dán Log]`. Hãy xác định root cause tại file nào, báo cáo dung lượng cần đọc và đề xuất bản vá tối thiểu (minimal patch) không gây side-effect."*
  3. Áp dụng bản vá $\rightarrow$ Chạy test kiểm thử hồi quy $\rightarrow$ Xuất Session Handover Report.

---

### 🟢 KỊCH BẢN 6: TÁI CẤU TRÚC MÃ NGUỒN CŨ (LEGACY CODE REFACTORING)
* **Tình huống:** Codebase cũ chằng chịt (Spaghetti code), hàm dài 200 dòng, vi phạm Clean Code.
* **Skills trọng tâm:** `coding-standards`, `plankton-code-quality`, `tdd-workflow`.
* **Quy trình thực hiện:**
  1. Viết bài test bao phủ (Characterization Test) cho đoạn code cũ để bảo toàn logic hiện tại.
  2. Prompt cho Agent: *"Đọc file @legacyService.ts. Hãy áp dụng nguyên tắc Single Responsibility và Clean Code để tách nhỏ thành các hàm dưới 25 dòng. Bắt buộc đảm bảo toàn bộ unit test hiện có vẫn PASS."*
  3. Soi kỹ Visual Diff (Xanh/Đỏ) trước khi accept.

---

### 🟢 KỊCH BẢN 7: DỰ ÁN HỌC MÁY & THỊ GIÁC MÁY TÍNH (PYTORCH / CV / EDGE AI)
* **Tình huống:** Xây dựng mô hình phân loại ảnh, nhận diện vật thể, huấn luyện PyTorch.
* **Skills trọng tâm:** `pytorch-patterns`, `eval-harness`, `benchmark`, `foundation-models-on-device`.
* **Quy trình thực hiện:**
  1. Chỉnh sửa `.agent-skills.json`, thêm `"pytorch-patterns"` vào `extraSkills` $\rightarrow$ Chạy `skill-router inject`.
  2. Prompt cho Agent: *"Đọc STEP-0-SESSION-ONBOARDING.md và skill @pytorch-patterns. Hãy xây dựng Custom Dataset đọc ảnh kèm pipeline Data Augmentation, DataLoader đa luồng có `pin_memory=True`, và vòng lặp huấn luyện hỗ trợ Mixed Precision `torch.amp`."*
  3. Kiểm tra tính độc lập thiết bị (`device-agnostic`) và seed tái lập.

---

### 🟢 KỊCH BẢN 8: KIỂM THỬ TDD & RÀ SOÁT AN TOÀN THÔNG TIN (SECURITY AUDIT)
* **Tình huống:** Chuẩn bị nộp đồ án hoặc triển khai release sản phẩm lên Production.
* **Skills trọng tâm:** `security-review`, `security-scan`, `security-bounty-hunter`, `e2e-testing`.
* **Quy trình thực hiện:**
  1. Prompt cho Agent: *"Đọc STEP-0-SESSION-ONBOARDING.md và @security-review. Hãy thực hiện quét bảo mật toàn bộ các API endpoints: kiểm tra SQLi, XSS, CSRF, cấu hình CORS, xác thực phân quyền và rà soát xem có API key nào bị hardcode không."*
  2. Yêu cầu Agent xuất bảng chấm điểm rủi ro (Risk Matrix) và đề xuất cách khắc phục.

---

### 🟢 KỊCH BẢN 9: CHUYỂN GIAO ĐỒ ÁN / ONBOARDING THÀNH VIÊN MỚI
* **Tình huống:** Thành viên mới vào nhóm cần hiểu kiến trúc dự án và cách chạy local.
* **Skills trọng tâm:** `code-tour`, `codebase-onboarding`, `documentation-lookup`.
* **Quy trình thực hiện:**
  1. Prompt cho Agent: *"Hãy quét cấu trúc dự án và tạo tài liệu hướng dẫn `ONBOARDING.md` bao gồm: Sơ đồ kiến trúc tổng quan, các biến môi trường cần thiết, các lệnh cài đặt dependencies và quy trình chạy test."*
  2. Sinh tài liệu giải thích luồng dữ liệu (Data Flow Diagram).

---

### 🟢 KỊCH BẢN 10: DỰ ÁN ĐA NỀN TẢNG / MULTI-STACK & MICROSERVICES
* **Tình huống:** Hệ thống gồm Frontend (Next.js), Backend API (Spring Boot/Go), Database (PostgreSQL) và Container (Docker).
* **Skills trọng tâm:** `docker-patterns`, `deployment-patterns`, `mcp-server-patterns`, `golang-patterns`.
* **Quy trình thực hiện:**
  1. Cấu hình `.agent-skills.json` chọn đủ các categories: `webapp-core`, `frontend-react`, `backend-java`, `database`, `devops`.
  2. Chạy `skill-router inject`.
  3. Prompt cho Agent: *"Đọc STEP-0-SESSION-ONBOARDING.md. Hãy viết file `docker-compose.yml` để dàn dựng toàn bộ cụm dịch vụ (Web, API, DB) kèm healthcheck và network bridge an toàn."*

---

## PHẦN II: KHUNG MẪU KỊCH BẢN CHUẨN ĐỂ MỞ RỘNG (CUSTOM SCENARIO SCHEMA)

> [!TIP]
> Người dùng có thể sao chép khung cấu trúc mẫu dưới đây để định nghĩa thêm bất kỳ kịch bản chuyên biệt nào (Kịch bản 11, 12, v.v.). Cấu trúc này đã được chuẩn hóa để mọi AI Agent đều có thể đọc hiểu và tuân thủ tuyệt đối.

```markdown
### 🟢 KỊCH BẢN [SỐ]: [TÊN KỊCH BẢN IN HOA]
* **Bối cảnh & Tình huống kích hoạt:** [Mô tả chi tiết hoàn cảnh khi nào cần dùng kịch bản này]
* **Mục tiêu cốt lõi:** [Mục tiêu cụ thể cần đạt được sau khi kết thúc phiên]
* **Skills ECC trọng tâm cần nạp:** `[skill-1]`, `[skill-2]`, `[skill-3]`

#### 1. Thao tác chuẩn bị môi trường (Pre-requisites):
- [ ] Kiểm tra Git: `git checkout -b [ten-nhanh]`
- [ ] Cấu hình `.agent-skills.json`: bổ sung các skills cần thiết và chạy `skill-router inject`
- [ ] Xác nhận các file biến môi trường hoặc dependencies liên quan

#### 2. Quy trình thực hiện chi tiết (Step-by-step Workflow):
1. **Bước 1 (Khám phá & Đánh giá):** [Hướng dẫn Agent cần đọc những gì]
2. **Bước 2 (Lập kế hoạch / Phân tích):** [Hướng dẫn Agent tạo plan và xác nhận]
3. **Bước 3 (Thực thi mã nguồn):** [Quy chuẩn code cần tuân thủ trong bước này]
4. **Bước 4 (Kiểm thử & Hậu kiểm):** [Lệnh test và tiêu chí pass]

#### 3. Mẫu Prompt Chuẩn Khởi Động (Kick-off Prompt):
> *"Đọc STEP-0-SESSION-ONBOARDING.md và tuân thủ Kịch bản [SỐ] trong ECC-ROUTER-10-SCENARIOS-GUIDE.md. Mục tiêu của tôi là [Mô tả mục tiêu]. Hãy thực hiện phân tích tác động, dự toán context budget và đưa ra đề xuất bước 1."*

#### 4. Tiêu chí nghiệm thu & Bàn giao (Acceptance Criteria & Handover):
- [ ] 100% tests liên quan đều PASS.
- [ ] Không có lỗi lint/type.
- [ ] Xuất bản Báo cáo Tổng kết Phiên (Session Handover Report) theo mẫu.
```
