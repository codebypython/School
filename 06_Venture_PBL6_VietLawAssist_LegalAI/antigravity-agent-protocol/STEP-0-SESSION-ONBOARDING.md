# STEP 0: SESSION ONBOARDING & PRE-FLIGHT IMPACT PROTOCOL
> **Vị trí tài liệu:** `d:\Development\TDD concept\antigravity-agent-protocol\STEP-0-SESSION-ONBOARDING.md`  
> **Mục đích:** Chỉ định bắt buộc AI Agent đọc và thực thi ngay khi bắt đầu một phiên làm việc mới (New Session) hoặc khi nhận yêu cầu mới từ người dùng.

---

## 📌 QUY TẮC TỐI THƯỢNG CHO AI AGENT (MANDATORY DIRECTIVE)

Khi người dùng mở một phiên làm việc mới hoặc yêu cầu: *"Đọc STEP-0-SESSION-ONBOARDING.md và bắt đầu phân tích"*, Agent **BẮT BUỘC** phải tuân thủ nghiêm ngặt quy trình 4 bước dưới đây **TRƯỚC KHI** thực hiện bất kỳ thao tác ghi đè mã nguồn (`write_to_file`, `replace_file_content`) hoặc chạy lệnh terminal thay đổi hệ thống.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         QUY TRÌNH 4 BƯỚC KHỞI ĐỘNG                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  Bước 1: Khám phá Codebase & Kiểm tra Hệ thống (System Health Discovery)    │
│  Bước 2: Phân tích Tác động Yêu cầu (Pre-flight Impact Analysis)            │
│  Bước 3: Dự toán Ngân sách Ngữ cảnh (Context Budget Calculation)             │
│  Bước 4: Xuất Bản Báo Cáo Pre-flight & Chờ Xác Nhận từ Người Dùng            │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. BƯỚC 1: KHÁM PHÁ CODEBASE & KIỂM TRA HỆ THỐNG (SYSTEM HEALTH)

Agent thực hiện quét nhẹ (Dry-run Scan) các chỉ số sau mà không nạp toàn bộ mã nguồn chi tiết:

### A. Kiểm tra Trạng thái Git (Git Health Check)
Agent kiểm tra xem working tree có sạch sẽ không:
- Nhánh hiện tại là gì? (Ví dụ: `main`, `dev`, `feature/...`)
- Có thay đổi nào chưa được commit không (`git status --short`)?
- *Cảnh báo bắt buộc:* Nếu có mã nguồn chưa commit, Agent phải nhắc người dùng tạo Git Checkpoint ngay lập tức để phòng ngừa rủi ro mất mã khi sửa đổi.

### B. Kiểm tra Môi trường & Dependencies (Dependency Health)
- Quét các tệp quản lý gói: `package.json`, `pom.xml`, `requirements.txt`, `pyproject.toml`, `go.mod`, `Cargo.toml`.
- Xác nhận các dependencies cốt lõi đã được cài đặt chưa (Ví dụ kiểm tra thư mục `node_modules/`, `.venv/`, `target/`).
- Kiểm tra tệp biến môi trường `.env` có tồn tại dựa trên `.env.example` hay chưa.

---

## 2. BƯỚC 2 & 3: PHÂN TÍCH TÁC ĐỘNG & DỰ TOÁN NGỮ CẢNH (PRE-FLIGHT BUDGET)

Khi nhận prompt từ người dùng, Agent phải tự động trả lời 4 câu hỏi trọng yếu:
1. **Tôi cần đọc những tệp nào?** (Liệt kê chính xác đường dẫn tệp và ước tính dung lượng token).
2. **Tôi sẽ thực hiện những hành động gì?** (Tạo mới, sửa đổi, chạy test hay debug).
3. **Tổng dung lượng có vượt trần Context Window của model không?** (Tính toán tỷ lệ chiếm dụng `%`).
4. **Cần thực hiện giải pháp quan trọng nào TRƯỚC KHI code?** (Tạo checkpoint Git, nén context, cài dependency, chạy test baseline).

### Công thức tính Context Budget:
$$\text{Tổng dung lượng yêu cầu} = \text{Lịch sử hội thoại hiện tại} + \text{Mã nguồn dự kiến đọc} + \text{System Prompt \& Rules}$$
$$\text{Tỷ lệ chiếm dụng (\%)} = \left( \frac{\text{Tổng dung lượng yêu cầu}}{\text{Giới hạn Token của Model}} \right) \times 100\%$$

* **Ngưỡng An Toàn ($< 60\%$):** Tiến hành phân tích bình thường.
* **Ngưỡng Cảnh Báo ($60\% - 80\%$):** Khuyến nghị người dùng cân nhắc nén `/compact` hoặc chỉ định đọc giới hạn dòng (`StartLine` - `EndLine`).
* **Ngưỡng Nguy Hiểm ($> 80\%$):** **DỪNG LẠI** không đọc toàn bộ file; đề xuất tách thành phiên làm việc mới (Task Decomposition).

---

## 3. BƯỚC 4: ĐỊNH DẠNG BẢNG BÁO CÁO PRE-FLIGHT CHUẨN MỰC

Mỗi khi bắt đầu phân tích một yêu cầu kỹ thuật, Agent **BẮT BUỘC PHẢI PHẢN HỒI** theo đúng cấu trúc mẫu sau trước khi đưa ra code:

```markdown
## 📋 [PRE-FLIGHT IMPACT & CONTEXT BUDGET REPORT]

### 1. 🔍 Phân tích Hiện trạng Hệ thống:
- **Git Status:** Nhánh `feature/auth` | [SẠCH SẼ] (hoặc [⚠️ CẢNH BÁO: Còn 3 file chưa commit])
- **Dependencies:** Đã phát hiện `package.json` (Node.js/React) | Đã cài đặt `node_modules`
- **Tech Stack nhận diện:** Next.js 14, TypeScript, TailwindCSS, Prisma

### 2. 📂 Tệp dự kiến sẽ đọc (Text need to read):
1. `src/modules/auth/authService.ts` (~3,500 tokens)
2. `src/types/user.d.ts` (~800 tokens)
3. `prisma/schema.prisma` (~1,800 tokens)
*=> Tổng mã nguồn nạp thêm: ~6,100 tokens*

### 3. 🛠️ Hành động dự kiến thực hiện:
- Phân tích cấu trúc schema hiện tại để bổ sung trường `googleId`.
- Viết logic xử lý OAuth callback trong `authService.ts`.
- Viết Unit Test kiểm thử luồng đăng nhập thành công và thất bại.

### 4. 📊 Dự toán Dung lượng Ngữ cảnh (Context Budget):
- Lịch sử chat hiện tại: 22,000 tokens
- Mã nguồn dự kiến nạp: 6,100 tokens
- System Prompt & Agent Rules: 4,500 tokens
- **Tổng dung lượng yêu cầu:** 32,600 tokens / 1,000,000 tokens (Gemini Limit)
- **Tỷ lệ chiếm dụng:** ~3.26% ➔ **[TRẠNG THÁI: AN TOÀN]**

### 5. ⚠️ Các giải pháp quan trọng CẦN LÀM TRƯỚC KHI THỰC HIỆN:
1. Chạy lệnh checkpoint nhanh: `git add . && git commit -m "checkpoint: pre-auth-implementation"`
2. Xác nhận cổng dịch vụ backend không bị xung đột.
3. Đảm bảo biến `GOOGLE_CLIENT_SECRET` đã được cấu hình trong `.env.local`.

---
👉 **[XÁC NHẬN]:** Tôi đã sẵn sàng. Bạn có muốn tôi tiến hành đọc các tệp trên và xây dựng Implementation Plan không?
```

---

## 4. CHU KỲ KIỂM SOÁT PHIÊN LÀM VIỆC (SESSION HYGIENE)

1. **Nguyên tắc "1 Nhiệm Vụ = 1 Phiên Chat":** Không tích lũy nhiều tính năng không liên quan vào 1 phiên chat.
2. **Kích hoạt nén `/compact` định kỳ:** Khi giải quyết xong 1 bug hoặc hoàn thiện 1 phase, yêu cầu AI tóm tắt ngắn gọn và giải phóng các đoạn hội thoại dài.
3. **Xuất Bản Báo Cáo Tóm Tắt (Handover Report):** Khi kết thúc phiên, Agent bắt buộc phải xuất bản tóm tắt bàn giao theo quy định tại `RULES-SAFETY-GOVERNANCE.md`.
