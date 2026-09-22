# 🤖 CẨM NANG TOÀN TẬP: LÀM CHỦ ANTIGRAVITY AGENTIC WORKFLOWS
## Khai phóng 100% Năng lực Tự hành & Khắc chế Suy thoái Ngữ cảnh

---

## 1. MÔ HÌNH 3 PHƯƠNG THỨC TƯƠNG TÁC (THE 3 AGENTIC MODALITIES)

Antigravity IDE không phải là một plugin chat gắn ngoài; nó tích hợp AI vào 3 tầng tương tác chuyên biệt tùy theo độ phức tạp của bài toán:

```
[MỨC ĐỘ PHỨC TẠP TĂNG DẦN] -------------------------------------------------------->
1. PASSIVE (Thụ động)        2. INSTRUCTIVE (Chỉ định)     3. COLLABORATIVE (Cộng tác)
- Antigravity Tab            - Inline Ctrl + I             - Sidebar Agent / Planning
- Đoán trước ý định          - Tác vụ tại chỗ              - Thiết kế kiến trúc & Multi-file
- 0 giây suy nghĩ            - 5 - 30 giây                 - 1 - 15 phút lập kế hoạch & chạy
```

### Phương thức 1: Passive (Antigravity Tab & Next-Intent Prediction)
- **Cơ chế**: AI liên tục đọc cây AST của file hiện tại, các tab mở gần đây, output gần nhất của terminal và clipboard.
- **Thao tác**:
  - Nhận đề xuất: <kbd>Tab</kbd>.
  - Nhận từng từ: <kbd>Ctrl</kbd> + <kbd>→</kbd>.
  - **Tab to Jump**: Nhấn <kbd>Tab</kbd> để nhảy con trỏ ra ngoài dấu đóng ngoặc hoặc tới vị trí tham số tiếp theo thay vì bấm phím mũi tên.
  - **Tab to Import**: Khi gõ một identifier chưa import (ví dụ `FastAPI`), chỉ cần gõ tên lớp và nhấn Tab, dòng import tương ứng sẽ được tự động thêm lên đầu file.

### Phương thức 2: Instructive (Inline Command `<Ctrl + I>`)
- **Cơ chế**: Chỉnh sửa mã nguồn cục bộ với giao diện so sánh trực quan (Visual Diff).
- **Thao tác**:
  - Bôi đen đoạn code (hoặc đặt con trỏ tại vị trí trống) $\rightarrow$ Bấm <kbd>Ctrl</kbd> + <kbd>I</kbd>.
  - Nhập prompt tinh gọn: *"Viết pytest cho hàm này"*, *"Thêm type hint & docstring chuẩn Google"*.
  - Nhìn thấy diff xanh/đỏ ngay trong code: Bấm <kbd>Ctrl</kbd> + <kbd>Enter</kbd> để đồng ý, hoặc <kbd>Esc</kbd> để hủy bỏ.

### Phương thức 3: Collaborative (Agent Mode & Planning Mode)
- **Cơ chế**: Phối hợp cùng Agent giải quyết các bài toán lớn liên quan đến nhiều file, kiểm thử và tìm kiếm tài liệu.
- **Quy trình chuẩn**:
  1. **Planning Mode**: Agent phân tích codebase và tạo file kế hoạch `implementation_plan.md`.
  2. **Review Kế hoạch**: Bạn xem xét các mục: *User Review Required*, *Proposed Changes*, *Verification Plan*.
  3. **Autonomous Execution**: Nhấn **Proceed**, Agent sẽ tự động tạo/sửa file, chạy terminal kiểm thử, bắt lỗi và tự sửa chữa (Self-Healing Loop).

---

## 2. NGHỆ THUẬT QUẢN LÝ NGỮ CẢNH (CONTEXT ENGINEERING)

Một prompt sơ sài sẽ nhận lại kết quả sơ sài. Kỹ sư giỏi sử dụng cú pháp **`@` Mentions** để nạp chính xác thông tin Agent cần:

| Cú pháp Mention | Ngữ cảnh nạp vào | Ví dụ thực tế |
| :--- | :--- | :--- |
| `@file:path` | Toàn bộ nội dung một file cụ thể | `@file:Project/services/dense_service.py` |
| `@folder:path` | Cây thư mục và danh sách file trong module | `@folder:Project/core/` |
| `@terminal` | Output và error log của terminal gần nhất | `"Giải thích lỗi trong @terminal và sửa giúp tôi"` |
| `@rules` | Các quy ước kiến trúc lưu trong `.agents/rules/` | `"Viết service mới tuân thủ nghiêm ngặt @rules"` |
| `@mcp` | Gọi công cụ ngoại vi (PostgreSQL, Jira, GitHub) | `"Truy vấn schema bảng users qua @mcp"` |

---

## 3. BỘ SIÊU LỆNH SLASH COMMANDS (THE HIGH-LEVERAGE TOOLKIT)

Khi ở trong khung Chat, gõ ký tự `/` để kích hoạt các quy trình tự động hóa:

### 1. `/grill-me` (Phản biện & Khảo sát Thiết kế)
- **Khi nào dùng**: Khi bạn có một ý tưởng nhưng chưa chắc chắn về kiến trúc, database schema hoặc luồng xử lý.
- **Tác dụng**: Agent sẽ đóng vai trò Senior System Architect, liên tục đặt các câu hỏi phản biện sâu sắc để ép bạn làm rõ yêu cầu trước khi bắt tay vào viết code.

### 2. `/goal` (Chế độ Deep-Work Xuyên đêm)
- **Khi nào dùng**: Khi bạn muốn giao một nhiệm vụ lớn (ví dụ: refactor toàn bộ module, viết bao phủ 50 unit tests).
- **Tác dụng**: Agent sẽ hoạt động kiên trì, tự lặp lại chu trình: Code $\rightarrow$ Run Test $\rightarrow$ Fix Bug $\rightarrow$ Run Test cho đến khi pass 100% mục tiêu mới dừng lại.

### 3. `/fork` (Phân nhánh Cuộc trò chuyện)
- **Khi nào dùng**: Khi cuộc trò chuyện đã dài hơn 20 lượt trao đổi, hoặc bạn muốn thử nghiệm một giải pháp kiến trúc khác mà không làm mất luồng hiện tại.
- **Tác dụng**: Tạo một bản sao độc lập của phiên trò chuyện tính từ mốc thời gian đó, giúp bộ nhớ sạch sẽ và tăng tốc độ suy luận của model.

### 4. `/rewind` (Quay ngược Thời gian)
- **Khi nào dùng**: Khi Agent sinh mã sai hướng hoặc hiểu nhầm đề bài.
- **Tác dụng**: Hoàn tác phiên làm việc về bước trước đó để bạn điều chỉnh lại prompt.

---

## 4. NGUYÊN TẮC VỆ SINH PHIÊN LÀM VIỆC (SESSION HYGIENE)

> [!WARNING]
> **Bẫy Context Bloat (Tràn bộ nhớ ngữ cảnh)**:
> Cửa sổ ngữ cảnh (Context Window) của LLM có hạn. Khi bạn giữ một phiên chat quá dài qua nhiều ngày:
> 1. Thời gian chờ phản hồi tăng gấp 3-5 lần.
> 2. Model dễ bị "loạn trí" (Hallucination), lẫn lộn biến của bài toán hôm qua với bài toán hôm nay.
> 3. Trình duyệt Webview bị giật lag và reset thanh cuộn.

### Quy tắc Vàng: "1 Feature = 1 Conversation"
- Khi hoàn thành xong một tính năng hoặc sửa xong một con bug:
  1. Ghi chú tóm tắt vào `STATUS.md` của công ty/project.
  2. Bấm **New Conversation** (hoặc phím tắt <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd> trong chat).
  3. Bắt đầu phiên mới bằng **Prompt Template Chuẩn** với tag nhận diện rõ ràng.
