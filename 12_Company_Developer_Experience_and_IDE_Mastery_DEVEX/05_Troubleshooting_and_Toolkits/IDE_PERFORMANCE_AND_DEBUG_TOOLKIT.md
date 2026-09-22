# 🧰 CẨM NANG XỬ LÝ SỰ CỐ & TỐI ƯU HIỆU NĂNG IDE CHUYÊN SÂU
## Cứu hộ Giao diện, Triệt tiêu Giật lag & Giải quyết Xung đột Trạng thái

---

## 1. XỬ LÝ SỰ CỐ KHUNG CHAT TỰ ĐỘNG RELOAD / MẤT VỊ TRÍ CUỘN

### Triệu chứng
Bạn đang lướt lên trên để đọc đoạn trao đổi hoặc tài liệu dài, sau vài phút hoặc khi có tin nhắn mới, khung chat tự động giật mạnh xuống đáy hoặc trắng xóa tải lại làm mất vị trí đọc dở.

### Nguyên nhân gốc rễ
1. Khung chat chạy trên Webview Process bị hệ điều hành đưa vào trạng thái ngủ (Sleep/Throttling) do bộ nhớ RAM chạm ngưỡng cảnh báo.
2. Cơ chế Autoscroll mặc định của IDE tự kích hoạt khi có socket event từ Agent stream về.

### Giải pháp triệt để
1. **Bật chế độ Always Awake**:
   - Mở Settings (<kbd>Ctrl</kbd> + <kbd>,</kbd>) $\rightarrow$ Tìm `Keep computer awake` $\rightarrow$ Tích chọn bật.
2. **Khóa cuộn bằng bàn phím**:
   - Khi đọc nội dung dài, dùng phím <kbd>Page Up</kbd> thay vì chuột lăn. Phiên bản Antigravity 2.15+ sẽ tự động kích hoạt chế độ **Scroll-Lock** khi nhận tín hiệu từ phím điều hướng.
3. **Đọc qua Editor Tab**:
   - Yêu cầu Agent: *"Xuất toàn bộ hướng dẫn này ra file `doc.md`"*. Mở file `.md` ở một tab Editor bên cạnh. Vì Editor chạy trên Renderer Process chính, vị trí dòng đọc được lưu vĩnh viễn và không bao giờ bị reload.

---

## 2. CHẨN ĐOÁN TIẾN TRÌNH & DỌN DẸP RÒ RỈ RAM (PROCESS EXPLORER)

Khi cảm thấy gõ code bị trễ (typing lag) hoặc quạt tản nhiệt máy tính kêu to:

1. **Mở Process Explorer nội bộ**:
   - Nhấn <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>.
   - Gõ lệnh: `Developer: Open Process Explorer` $\rightarrow$ Nhấn <kbd>Enter</kbd>.
   - Bảng hiển thị CPU và RAM của từng tiến trình sẽ hiện ra:
     - `window (Main)`: Giao diện chính.
     - `extensionHost`: Tiến trình chạy các tiện ích mở rộng.
     - `languageServer`: Tiến trình phân tích cú pháp.
2. **Hành động xử lý**:
   - Nếu thấy một Extension chiếm trên 30% CPU liên tục khi không gõ code $\rightarrow$ Chuột phải vào tiến trình đó chọn **Kill Process** hoặc Disable extension đó.

---

## 3. KHÔI PHỤC BỐ CỤC KHI KÉO THẢ BỊ LỖI (VIEW LOCATIONS RECOVERY)

Nếu bạn lỡ tay kéo tab Chat hoặc Explorer vào một góc kỳ quặc hoặc làm biến mất một panel quan trọng:

1. **Lệnh khôi phục thần tốc**:
   - Nhấn <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>.
   - Gõ: `View: Reset View Locations` $\rightarrow$ Nhấn <kbd>Enter</kbd>.
   - Toàn bộ các panel và thanh công cụ sẽ tự động trở về vị trí tiêu chuẩn ban đầu của IDE.
2. **Khởi động lại Window không mất dữ liệu**:
   - Nhấn <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>.
   - Gõ: `Developer: Reload Window` $\rightarrow$ Nhấn <kbd>Enter</kbd>.
   - Toàn bộ cache DOM được giải phóng chỉ trong 1.5 giây.

---

## 4. GIẢI QUYẾT XUNG ĐỘT PHÍM TẮT (KEYBINDING CONFLICTS)

Khi bạn bấm một phím tắt (ví dụ <kbd>Ctrl</kbd> + <kbd>D</kbd> hay <kbd>Alt</kbd> + <kbd>Up</kbd>) nhưng IDE lại thực hiện một hành động khác không mong muốn:

1. **Truy tìm lệnh xung đột**:
   - Nhấn <kbd>Ctrl</kbd> + <kbd>K</kbd> rồi nhấn <kbd>Ctrl</kbd> + <kbd>S</kbd> để mở bảng Keyboard Shortcuts.
   - Nhấp vào biểu tượng bàn phím nhỏ ở góc phải thanh tìm kiếm (hoặc gõ `"\"alt+up\""`).
   - IDE sẽ liệt kê toàn bộ các lệnh đang tranh chấp cùng một tổ hợp phím.
2. **Khắc phục**:
   - Chuột phải vào lệnh không mong muốn $\rightarrow$ Chọn **Remove Keybinding** (hoặc thêm điều kiện `when` trong file `keybindings.json`).

---

### ⚠️ Lỗi phổ biến sinh viên hay gặp
1. **Lạm dụng quá nhiều Extension làm chậm IDE**: Cài hàng chục extension làm đẹp, hiệu ứng pháo hoa, linter thừa thãi khiến `extensionHost` ngốn hàng GB RAM và làm trễ con trỏ.
2. **Quên không loại trừ thư mục nặng (`files.watcherExclude`)**: Để Language Server quét toàn bộ thư mục `node_modules` hoặc môi trường ảo `.venv` khiến CPU luôn ở mức 100%.
3. **Mở một phiên chat dài qua nhiều tuần**: Khiến context window bị tràn, làm chậm cả IDE và suy giảm độ thông minh của Agent.

---

### 💡 Micro-quiz / Câu hỏi phản biện
**Câu hỏi**: Khi bạn mở một dự án lớn có hàng trăm nghìn file (như monorepo), tại sao việc thêm `"**/node_modules/**": true` vào mục `files.watcherExclude` lại quan trọng hơn nhiều so với việc chỉ ẩn nó đi ở mục `files.exclude`?
*(Gợi ý: Phân biệt giữa cơ chế hiển thị DOM của Explorer và cơ chế theo dõi sự kiện file cấp OS của Inotify/ReadDirectoryChanges)*.
