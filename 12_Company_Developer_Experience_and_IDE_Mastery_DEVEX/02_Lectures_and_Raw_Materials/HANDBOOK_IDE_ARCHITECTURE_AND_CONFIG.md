# 📘 CẨM NANG KIẾN TRÚC IDE & NGUYÊN LÝ CODE-AS-CONFIGURATION
## Từ Bản chất Electron/V8 đến Làm chủ Cấu hình Chuẩn Senior

---

## 1. KIẾN TRÚC ĐA TIẾN TRÌNH CỦA ANTIGRAVITY / VS CODE (PROCESS ARCHITECTURE)

Để làm chủ IDE và không bao giờ bị bất ngờ trước các hiện tượng lag giật hay mất trạng thái, một kỹ sư phải hiểu rõ cấu trúc dưới nắp ca-pô:

```
                                +-----------------------------+
                                |     MAIN PROCESS (Node.js)  |
                                |  (Vòng đời App, Native OS,  |
                                |   Tạo Window, Menu, File IO)|
                                +--------------+--------------+
                                               |
                  +----------------------------+----------------------------+
                  |                                                         |
                  v                                                         v
    +---------------------------+                             +---------------------------+
    |  RENDERER PROCESS (DOM)   |                             |   EXTENSION HOST (Node)   |
    |  (Giao diện UI, Editor,   |                             | (Chạy Extension, Plugin,  |
    |   Syntax Highlight, Text) |                             |  Tác vụ nền của tiện ích) |
    +-------------+-------------+                             +-------------+-------------+
                  |                                                         |
                  v                                                         v
    +---------------------------+                             +---------------------------+
    |   WEBVIEW PROCESS (Sand)  |                             |   LANGUAGE SERVER (LSP)   |
    | (Khung Chat AI, Markdown, |                             | (Pyright, TypeScript,     |
    |  Auxiliary Floating Views)|                             |  IntelliSense, AST Index) |
    +---------------------------+                             +---------------------------+
```

### Tại sao điều này quan trọng?
1. **Khung Chat AI chạy trong Webview Process độc lập**:
   - Khung chat Antigravity thực chất là một phiên bản Chromium mini độc lập (IFrame/Webview).
   - Khi hệ điều hành hoặc IDE thiếu RAM, tiến trình Webview này có thể bị hệ điều hành "ép ngủ" (Throttling/Discarding). Đó là lý do khi bạn để lâu không dùng, click lại vào chat thì nó phải tải lại và mất vị trí cuộn nếu chưa cấu hình đúng.
2. **Editor chạy trên Renderer Process riêng**:
   - Thao tác gõ phím và con trỏ chạy trên luồng giao diện cực nhanh với tốc độ khung hình 60-120fps. Nếu bạn thấy gõ chữ bị khựng lại, 90% nguyên nhân là do một Extension trong **Extension Host** đang chiếm dụng tài nguyên CPU.
3. **Language Server Protocol (LSP)**:
   - Các tính năng như <kbd>F12</kbd> (Go to Definition), <kbd>F2</kbd> (Rename Symbol) không phải do IDE tự phân tích văn bản thuần túy, mà do một tiến trình máy chủ ngôn ngữ riêng (như `Pylance` cho Python hay `tsserver` cho TypeScript) tạo cây cú pháp trừu tượng (AST).

---

## 2. CƠ CHẾ CỬA SỔ PHỤ ĐỘC LẬP (AUXILIARY / FLOATING WINDOWS)

Kể từ VS Code 1.85+ và trên Antigravity IDE, bạn có thể tách các tab ra thành các cửa sổ độc lập (Native OS Windows).

### Bản chất kỹ thuật
- Khi bạn kéo một tab Editor hoặc panel Chat ra ngoài, Electron Main Process sẽ tạo một đối tượng `BrowserWindow` con cấp hệ điều hành.
- Cửa sổ này có Process ID riêng, hiển thị trực tiếp trên thanh Taskbar của Windows và có thể chuyển đổi mượt mà bằng <kbd>Alt</kbd> + <kbd>Tab</kbd>.
- **Cơ chế lưu trạng thái**: Vị trí tọa độ màn hình (x, y, width, height) và danh sách file mở trong cửa sổ con được ghi vào database `state.vscdb` của profile người dùng.

### Các thiết lập cốt lõi để giữ vĩnh viễn trạng thái cửa sổ
Trong file `settings.json`:
```json
{
  // Giữ lại toàn bộ các cửa sổ phụ khi khởi động lại IDE
  "window.restoreWindows": "all",
  // Khôi phục vị trí cuộn và con trỏ chính xác trong từng tab
  "workbench.editor.restoreViewState": true,
  // Cho phép kéo thả view linh hoạt ra ngoài cửa sổ
  "workbench.experimental.shareHistory": true
}
```

---

## 3. TRIẾT LÝ CODE-AS-CONFIGURATION (CẤU HÌNH BẰNG MÃ)

Người dùng nghiệp dư mở giao diện Settings dạng form để tìm kiếm và click chuột. **Kỹ sư chuyên nghiệp quản lý cấu hình bằng file JSON**.

### 1. Phân cấp Cấu hình (Configuration Hierarchy)
Cấu hình trong IDE được áp dụng theo thứ tự ghi đè từ dưới lên trên:
1. **Default Settings**: Cài đặt mặc định của hệ thống.
2. **User Settings (`%APPDATA%\Code\User\settings.json` hoặc `~/.gemini/...`)**: Áp dụng toàn cục cho mọi dự án bạn mở trên máy tính.
3. **Workspace Settings (`.vscode/settings.json`)**: Nằm ngay trong thư mục gốc của dự án, ghi đè toàn bộ User Settings. File này được commit lên Git để toàn bộ lập trình viên trong nhóm có chung một chuẩn format, font chữ và linter.
4. **Language-specific Settings**: Ghi đè cho từng ngôn ngữ riêng biệt (ví dụ `[python]` hay `[markdown]`).

### 2. Cách mở nhanh file cấu hình JSON bằng bàn phím
- Nhấn <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>.
- Gõ: `Preferences: Open User Settings (JSON)` $\rightarrow$ Nhấn <kbd>Enter</kbd>.
- Mọi thay đổi lưu trong file này có hiệu lực ngay lập tức trong thời gian thực mà không cần khởi động lại ứng dụng.

### 3. Cách mở nhanh file gán phím tắt JSON (`keybindings.json`)
- Nhấn <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>.
- Gõ: `Preferences: Open Keyboard Shortcuts (JSON)` $\rightarrow$ Nhấn <kbd>Enter</kbd>.
- Tại đây bạn có thể gán bất kỳ phím tắt nào, thiết lập điều kiện khi nào phím tắt có hiệu lực thông qua mệnh đề `"when"`.

---

## 4. BẢNG PHÂN LOẠI CÁC THIẾT LẬP TỐI ƯU DEVEX

| Nhóm thiết lập | Khóa cấu hình then chốt | Giá trị tối ưu | Ý nghĩa thực chiến |
| :--- | :--- | :---: | :--- |
| **Công thái học Font** | `editor.fontFamily` | `"JetBrains Mono", "Fira Code"` | Font monospace lập trình tốt nhất thế giới |
| **Ký tự nối (Ligatures)** | `editor.fontLigatures` | `true` | Biến `!=`, `==`, `=>`, `->` thành ký hiệu toán học liền mạch |
| **Con trỏ mượt** | `editor.cursorSmoothCaretAnimation` | `"on"` | Con trỏ lướt êm ái, giảm mỏi mắt khi code lâu |
| **Nhịp thở con trỏ** | `editor.cursorBlinking` | `"smooth"` | Chớp nháy mượt mà tạo nhịp tập trung |
| **Định dạng tự động** | `editor.formatOnSave` | `true` | Tự động căn chỉnh chuẩn PEP8/Prettier mỗi khi lưu |
| **Lưu tự động** | `files.autoSave` | `"afterDelay"` | Tránh mất code khi đột ngột mất điện/crash |
| **Loại bỏ file rác** | `files.exclude` | `node_modules`, `__pycache__` | Ẩn file rác khỏi cây thư mục, tăng tốc độ search 500% |
| **Loại bỏ theo dõi** | `files.watcherExclude` | `**/.git/**`, `**/build/**` | Giải phóng CPU khỏi việc theo dõi hàng vạn file tĩnh |
