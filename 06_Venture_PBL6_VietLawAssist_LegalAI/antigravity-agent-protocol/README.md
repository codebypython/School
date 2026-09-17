# ANTIGRAVITY AGENT PROTOCOL (AAP)
> **Bộ Quy Chuẩn & Tri Thức Vận Hành AI Agents Trong Thực Tế**  
> *Được tối ưu cho Antigravity IDE, Antigravity 2.0 (Gemini 2.5/3.7) & Cursor*

---

## 🌟 TỔNG QUAN

Thư mục `antigravity-agent-protocol` là trung tâm tri thức và hành lang an toàn bắt buộc dành cho các AI Agent dạng Box Chat và Pair-programmer. Hệ thống này giúp triệt tiêu hoàn toàn các rủi ro kinh điển khi dùng AI: **Tràn ngữ cảnh (Context Rot), Hiếu động sửa lan man (Autonomous Drift), Ghi đè sai lệch (Overwrite Collision), và Lệnh Terminal nguy hiểm**.

```
antigravity-agent-protocol/
├── 📄 STEP-0-SESSION-ONBOARDING.md      # [ĐỌC ĐẦU TIÊN] Pre-flight impact analysis, budget token, health check
├── 📄 RULES-SAFETY-GOVERNANCE.md        # Quy tắc an toàn, Handover Report, Quick Git Helpers
├── 📄 ECC-ROUTER-10-SCENARIOS-GUIDE.md  # Cẩm nang 10 kịch bản thực tế + Mẫu schema mở rộng kịch bản mới
├── 📄 PROMPTS-AND-TEMPLATES-PLAYBOOK.md # Thư viện Prompt chuẩn hóa (Plan, TDD, Hotfix, Handover)
└── 📄 README.md                         # Hướng dẫn tổng quan & tích hợp vào dự án
```

---

## 🚀 HƯỚNG DẪN BẮT ĐẦU NHANH CHO NGƯỜI DÙNG

### Bước 1: Điều phối Skills cho dự án của bạn (nếu có dùng ECC)
Tại thư mục dự án của bạn, chạy công cụ điều phối để trích xuất đúng các skills cần thiết:
```powershell
node D:\Development\tools\skill-router\skill-router.js init
node D:\Development\tools\skill-router\skill-router.js inject
```

### Bước 2: Bắt đầu phiên làm việc trong Box Chat Antigravity
Mỗi khi mở một phiên chat mới, gửi câu lệnh kick-off chuẩn sau:
```markdown
Đọc STEP-0-SESSION-ONBOARDING.md và RULES-SAFETY-GOVERNANCE.md.
Mục tiêu của tôi: [Mô tả tính năng hoặc bài toán bạn cần làm].
Hãy phân tích hiện trạng, tính toán context budget và báo cáo trước khi thực hiện.
```

### Bước 3: Đọc Báo cáo Tổng kết Phiên (Handover Report) khi xong việc
Khi hoàn thành, Agent sẽ tự động xuất bản **Session Handover Card** để bạn gửi báo cáo cho nhóm hoặc lưu vết tiến độ.

---

## 🔗 CÁCH LIÊN KẾT GIAO THỨC NÀY VÀO DỰ ÁN MỚI

Bạn có thể liên kết bộ giao thức này vào bất kỳ dự án mới nào theo 2 cách:

### Cách 1: Tạo tệp quy tắc `.gemini/AGENTS.md` hoặc `.agents/rules/protocol.md` trong dự án:
```markdown
# Agent Directives
When starting any session or receiving technical tasks, you MUST read and follow the protocol at:
- `D:\Development\TDD concept\antigravity-agent-protocol\STEP-0-SESSION-ONBOARDING.md`
- `D:\Development\TDD concept\antigravity-agent-protocol\RULES-SAFETY-GOVERNANCE.md`
```

### Cách 2: Sử dụng `@ Mention` trực tiếp trong Box Chat:
Gõ `@D:\Development\TDD concept\antigravity-agent-protocol\STEP-0-SESSION-ONBOARDING.md` vào tin nhắn đầu tiên của phiên chat.
