# 🎯 LỘ TRÌNH HUẤN LUYỆN 14 NGÀY PARETO (80/20 IDE MASTERY CURRICULUM)
## Làm chủ 80% Năng suất IDE bằng 20% Thao tác Cốt lõi

> **Thời lượng**: 14 ngày rèn luyện liên tục (2 tuần)  
> **Phương pháp tiếp cận**: Quy luật Pareto (80/20) + Kỹ thuật lặp lại ngắt quãng (Spaced Repetition) + Luyện phản xạ cơ tay (Deliberate Muscle Memory Practice).  
> **Chuẩn đầu ra (Acceptance Criteria)**: Kỹ sư thao tác lập trình, duyệt file, tái cấu trúc mã và phối hợp cùng AI Agent mà **không cần chạm vào chuột quá 10% tổng thời gian làm việc**.

---

## MA TRẬN 20% THAO TÁC CỐT LÕI (THE PARETO CORE MATRIX)

```
========================================================================================
TUẦN 1: CORE NAVIGATION & MULTI-WINDOW (Cơ tay & Điều hướng không chuột)
----------------------------------------------------------------------------------------
Day 01: Bố cục Đa Cửa sổ Độc lập (Auxiliary Windows) & Chuyển đổi Alt+Tab
Day 02: Điều hướng Tệp & Lệnh tối thượng (Ctrl+P, Ctrl+Shift+P, Ctrl+B)
Day 03: Thao tác Dòng Thần tốc (Alt+Up/Down, Shift+Alt+Down, Ctrl+Shift+K)
Day 04: Đa Con trỏ (Multi-Cursor Ctrl+D, Ctrl+Alt+Up/Down) & Tìm kiếm Nâng cao
Day 05: Duyệt Mã nguồn Thông minh (F12 Definition, Alt+F12 Peek, Shift+F12 References)
Day 06: Tái cấu trúc Toàn dự án (F2 Rename Symbol, Problems Navigation F8)
Day 07: Kiểm tra Phản xạ Tuần 1: Thử thách 24 giờ "Tuyệt đối không chạm chuột"
========================================================================================
TUẦN 2: AGENTIC WORKFLOWS & MULTI-MODAL MASTERY (Làm chủ AI Agent Antigravity)
----------------------------------------------------------------------------------------
Day 08: Tầng Thụ động (Antigravity Tab, Supercomplete, Tab to Jump, Tab to Import)
Day 09: Tầng Chỉ định (Inline Ctrl+I, Visual Diff Overlays, Accept/Reject nhanh)
Day 10: Tầng Hợp tác (Sidebar Agent Mode, Context Mentions @file, @folder, @terminal)
Day 11: Làm chủ Quy trình Lập kế hoạch (Planning Mode & implementation_plan.md)
Day 12: Bộ công cụ Lệnh Slash Đột phá (/grill-me, /goal, /fork, /rewind)
Day 13: Cấu hình Dự án Chuẩn (.agents/rules/, Custom Skills, MCP Server Integration)
Day 14: Tốt nghiệp & Capstone Speed Drill: Xây dựng tính năng khép kín trong 15 phút
========================================================================================
```

---

## TUẦN 1: CORE NAVIGATION, MULTI-WINDOW & CODE EDITING

### 📅 Day 01: Bố cục Đa Cửa sổ Độc lập (Auxiliary Windows) & Phản xạ <kbd>Alt</kbd> + <kbd>Tab</kbd>
- **Mục tiêu**: Giải phóng không gian màn hình, tách rời Editor, Chat AI và Terminal thành các cửa sổ độc lập.
- **Thao tác cốt lõi**:
  - Kéo tab Editor / tab Chat văng ra ngoài viền màn hình để tạo Floating Window.
  - Phím tắt mở file trong cửa sổ mới: <kbd>Ctrl</kbd> + <kbd>K</kbd> sau đó nhấn <kbd>O</kbd>.
  - Lệnh Command Palette: `View: Move View into New Window`.
  - Phản xạ chuyển cửa sổ: <kbd>Alt</kbd> + <kbd>Tab</kbd> và snap cửa sổ <kbd>Win</kbd> + <kbd>←</kbd> / <kbd>→</kbd>.
- **Bài tập luyện cơ tay**: Thực hành bài tập trong [`DAY_01_TO_07_CORE_NAVIGATION_DRILLS.md`](file:///d:/User/7th/School/12_Company_Developer_Experience_and_IDE_Mastery_DEVEX/03_Engineering_Labs_and_Code/drills/DAY_01_TO_07_CORE_NAVIGATION_DRILLS.md) - Drill 01.
- **Tiêu chuẩn đạt**: Tách và sắp xếp bố cục 3 cửa sổ (Editor, Chat, Terminal) trong dưới 10 giây mà không bị lúng túng.

### 📅 Day 02: Điều hướng Tệp & Lệnh tối thượng (<kbd>Ctrl</kbd> + <kbd>P</kbd>, <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
- **Mục tiêu**: Tuyệt đối không dùng chuột click cây thư mục để mở file.
- **Thao tác cốt lõi**:
  - <kbd>Ctrl</kbd> + <kbd>P</kbd>: Nhập tên viết tắt (fuzzy search) để mở file.
  - Mở trực tiếp tới dòng cụ thể: <kbd>Ctrl</kbd> + <kbd>P</kbd> $\rightarrow$ gõ `test_smoke.py:42`.
  - Mở trực tiếp tới hàm/ký hiệu: <kbd>Ctrl</kbd> + <kbd>P</kbd> $\rightarrow$ gõ `@ten_ham`.
  - Ẩn/Hiện thanh Explorer: <kbd>Ctrl</kbd> + <kbd>B</kbd> để giải phóng 20% màn hình khi đang đọc code.
- **Tiêu chuẩn đạt**: Mở đúng 5 file nằm sâu trong các thư mục con khác nhau trong vòng dưới 6 giây.

### 📅 Day 03: Thao tác Dòng Thần tốc (Line Manipulation)
- **Mục tiêu**: Di chuyển, nhân bản và xóa dòng code bằng phím tắt, cấm bôi đen copy-paste thông thường.
- **Thao tác cốt lõi**:
  - Di chuyển cả dòng code lên/xuống: <kbd>Alt</kbd> + <kbd>↑</kbd> / <kbd>↓</kbd>.
  - Nhân bản dòng lên/xuống: <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>↑</kbd> / <kbd>↓</kbd>.
  - Xóa sạch dòng hiện tại: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>K</kbd>.
  - Chèn dòng mới phía dưới ngay lập tức: <kbd>Ctrl</kbd> + <kbd>Enter</kbd> (dù con trỏ đang ở giữa dòng).
  - Chèn dòng mới phía trên: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd>.
- **Tiêu chuẩn đạt**: Sắp xếp lại thứ tự 10 dòng code bị xáo trộn về đúng logic trong dưới 8 giây.

### 📅 Day 04: Đa Con trỏ (Multi-Cursor) & Sửa Đồng loạt
- **Mục tiêu**: Sửa 10 vị trí code giống nhau trong 1 giây mà không dùng Find & Replace của chuột.
- **Thao tác cốt lõi**:
  - Chọn từ kế tiếp giống từ đang chọn: <kbd>Ctrl</kbd> + <kbd>D</kbd> (nhấn liên tiếp để chọn nhiều từ).
  - Bỏ qua từ vừa chọn: <kbd>Ctrl</kbd> + <kbd>K</kbd> sau đó <kbd>Ctrl</kbd> + <kbd>D</kbd>.
  - Đặt con trỏ lên dòng trên/dưới: <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>↑</kbd> / <kbd>↓</kbd>.
  - Đặt con trỏ ở cuối mọi dòng được bôi đen: <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>I</kbd>.
- **Tiêu chuẩn đạt**: Đổi tên biến cục bộ xuất hiện 8 lần trong 1 hàm bằng <kbd>Ctrl</kbd> + <kbd>D</kbd> trong dưới 3 giây.

### 📅 Day 05: Duyệt Mã nguồn Thông minh (Code Navigation)
- **Mục tiêu**: Di chuyển xuyên file như một kiến trúc sư, không bao giờ phải đi tìm file thủ công.
- **Thao tác cốt lõi**:
  - Đi đến định nghĩa hàm/class: <kbd>F12</kbd> (Go to Definition).
  - Mở cửa sổ xem nhanh định nghĩa tại chỗ: <kbd>Alt</kbd> + <kbd>F12</kbd> (Peek Definition).
  - Xem mọi nơi đang gọi hàm này: <kbd>Shift</kbd> + <kbd>F12</kbd> (Find References).
  - Quay lại vị trí con trỏ trước đó: <kbd>Alt</kbd> + <kbd>←</kbd> (Go Back) và tiến lại <kbd>Alt</kbd> + <kbd>→</kbd> (Go Forward).
- **Tiêu chuẩn đạt**: Lần vết 1 biến từ Controller $\rightarrow$ Service $\rightarrow$ Repository $\rightarrow$ Database Model và quay trở lại điểm xuất phát trong dưới 15 giây.

### 📅 Day 06: Tái cấu trúc Toàn diện & Quản lý Lỗi
- **Mục tiêu**: Refactor an toàn toàn bộ project và fix lỗi compiler/linter tức thì.
- **Thao tác cốt lõi**:
  - Đổi tên an toàn toàn bộ dự án: Đặt con trỏ vào tên hàm/class $\rightarrow$ Nhấn <kbd>F2</kbd> $\rightarrow$ Nhập tên mới $\rightarrow$ <kbd>Enter</kbd> (IDE tự động sửa mọi file import).
  - Nhảy trực tiếp tới lỗi gạch đỏ tiếp theo: <kbd>F8</kbd> (Go to Next Problem).
  - Mở Quick Fix tại chỗ: <kbd>Ctrl</kbd> + <kbd>.</kbd> (Quick Fix Menu).
- **Tiêu chuẩn đạt**: Sửa 5 lỗi linting/type hint trên 3 file khác nhau hoàn toàn bằng <kbd>F8</kbd> và <kbd>Ctrl</kbd> + <kbd>.</kbd>.

### 📅 Day 07: Thử thách 24 giờ "Mouse-Free Gatekeeper" (Review Tuần 1)
- **Nhiệm vụ**: Cất chuột vào ngăn kéo hoặc tắt touchpad trong suốt 1 buổi làm việc (ít nhất 2 tiếng code liên tục).
- **Đánh giá**: Hoàn thành một bài lab kỹ thuật mà chỉ dùng các phím tắt đã học từ Day 01 đến Day 06.

---

## TUẦN 2: AGENTIC WORKFLOWS & ANTIGRAVITY AI MASTERY

### 📅 Day 08: Tầng Thụ động (Antigravity Tab, Supercomplete & Predictor)
- **Mục tiêu**: Tối đa hóa tốc độ gõ nhờ khả năng dự đoán ý định (Next-intent prediction).
- **Thao tác cốt lõi**:
  - Nhận toàn bộ đề xuất: <kbd>Tab</kbd>.
  - Nhận từng từ một để kiểm soát: <kbd>Ctrl</kbd> + <kbd>→</kbd>.
  - Từ chối đề xuất: <kbd>Esc</kbd>.
  - Tận dụng **Tab to Jump** để nhảy qua các cặp ngoặc hoặc tới tham số tiếp theo.
  - Tận dụng **Tab to Import** khi khai báo lớp mới.
- **Tiêu chuẩn đạt**: Viết 1 model class có 5 trường và phương thức `__repr__` với trên 70% số ký tự do Tab gợi ý chính xác.

### 📅 Day 09: Tầng Chỉ định Cục bộ (<kbd>Ctrl</kbd> + <kbd>I</kbd> Inline Command)
- **Mục tiêu**: Ra lệnh sửa đổi tại chỗ trong Editor mà không mở khung chat bên cạnh.
- **Thao tác cốt lõi**:
  - Bôi đen khối code $\rightarrow$ Nhấn <kbd>Ctrl</kbd> + <kbd>I</kbd>.
  - Ra lệnh ngắn gọn: *"Thêm docstring chuẩn Google"*, *"Viết unit test tương ứng"*, *"Tối ưu thuật toán từ O(N^2) về O(N)"*.
  - Kiểm tra Visual Diff Overlay: Xanh (Thêm) / Đỏ (Bớt). Chấp nhận: <kbd>Ctrl</kbd> + <kbd>Enter</kbd>, Hủy: <kbd>Esc</kbd>.
- **Tiêu chuẩn đạt**: Refactor và thêm type hints cho 3 hàm độc lập hoàn toàn bằng <kbd>Ctrl</kbd> + <kbd>I</kbd> trong dưới 2 phút.

### 📅 Day 10: Tầng Hợp tác & Định hướng Ngữ cảnh Bằng `@` Mentions
- **Mục tiêu**: Không bao giờ copy-paste thủ công code vào khung chat; nạp ngữ cảnh chính xác tuyệt đối.
- **Thao tác cốt lõi**:
  - Gõ `@file:path/to/file` để nạp file làm ngữ cảnh.
  - Gõ `@folder:path/` để Agent hiểu toàn bộ cấu trúc module.
  - Gõ `@terminal` để nạp log lỗi runtime mà không cần bôi đen terminal copy.
  - Gõ `@mcp` hoặc `@rules` để áp dụng quy tắc dự án.
- **Tiêu chuẩn đạt**: Gửi prompt yêu cầu fix lỗi phức tạp gồm ngữ cảnh của 2 file và terminal log chỉ bằng 1 câu lệnh ngắn kết hợp `@mentions`.

### 📅 Day 11: Làm chủ Quy trình Lập kế hoạch (Planning Mode)
- **Mục tiêu**: Làm việc theo phong cách Technical Lead - Duyệt thiết kế trước, code sau.
- **Thao tác cốt lõi**:
  - Yêu cầu Agent tạo `implementation_plan.md` cho các tính năng từ 3 file trở lên.
  - Kiểm duyệt: User Review Required $\rightarrow$ Proposed Changes $\rightarrow$ Verification Plan.
  - Bấm **Proceed** để Agent tự động thực thi chuỗi sửa đổi và chạy kiểm thử tự động.
- **Tiêu chuẩn đạt**: Triển khai thành công 1 feature gồm 3 file mã nguồn mà không gặp bất kỳ lỗi xung đột logic nào nhờ có kế hoạch trước.

### 📅 Day 12: Bộ công cụ Lệnh Slash Đột phá (`/grill-me`, `/goal`, `/fork`, `/rewind`)
- **Mục tiêu**: Sử dụng các siêu lệnh để giải quyết bế tắc kỹ thuật và tối ưu bộ nhớ hội thoại.
- **Thao tác cốt lõi**:
  - `/grill-me`: Kích hoạt Agent phỏng vấn ngược lại bạn để bóc tách thiết kế hệ thống.
  - `/goal`: Chế độ tự hành cho các task chạy đêm hoặc task dài (chạy test cho đến khi pass 100%).
  - `/fork`: Tách nhánh hội thoại khi chat đã dài để tránh loãng context (Context Bloat).
  - `/rewind`: Quay ngược thời gian nếu Agent đi chệch hướng.
- **Tiêu chuẩn đạt**: Áp dụng `/grill-me` để phác thảo xong kiến trúc của 1 module phức tạp và dùng `/fork` để thử nghiệm 2 hướng giải thuật khác nhau.

### 📅 Day 13: Cấu hình Dự án Chuyên nghiệp (`.agents/rules/` & Custom Skills)
- **Mục tiêu**: Đóng gói kinh nghiệm thành tài sản vĩnh cửu của dự án, không bao giờ phải dặn dò Agent 2 lần.
- **Thao tác cốt lõi**:
  - Thiết lập `.agents/rules/architecture.md` và `.agents/rules/coding_standards.md`.
  - Tạo một Custom Skill đơn giản tự động hóa quy trình chạy benchmark/test.
  - Tích hợp công cụ MCP Server ngoại vi khi cần truy cập dữ liệu bên ngoài.
- **Tiêu chuẩn đạt**: Mở một phiên chat hoàn toàn mới, ra lệnh ngắn gọn và Agent tự động tuân thủ 100% quy ước mã nguồn đã ghi trong `.agents/rules/`.

### 📅 Day 14: Tốt nghiệp & Capstone Speed Drill
- **Mục tiêu**: Kiểm tra toàn diện kỹ năng phối hợp giữa tốc độ cơ tay và khả năng điều phối AI Agent.
- **Thử thách**: Trong vòng **15 phút**, thực hiện một bài toán kỹ thuật từ đầu đến cuối (Tạo file $\rightarrow$ Lập kế hoạch $\rightarrow$ Sinh code $\rightarrow$ Viết Unit test $\rightarrow$ Chạy test xanh 100% $\rightarrow$ Refactor) với quy tắc:
  - Tỉ lệ dùng chuột dưới 5%.
  - Tận dụng tối đa phím tắt điều hướng và 3 tầng AI Modalities.
- **Phần thưởng**: Cấp chứng chỉ năng lực nội bộ của School Holdings: **Certified IDE & Agentic Master Engineer**.
