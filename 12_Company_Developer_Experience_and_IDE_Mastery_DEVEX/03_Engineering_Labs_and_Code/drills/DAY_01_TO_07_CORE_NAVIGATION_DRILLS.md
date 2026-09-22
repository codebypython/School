# 🏋️ BỘ BÀI TẬP LUYỆN PHẢN XẠ CƠ TAY: NGÀY 01 ĐẾN NGÀY 07
## Huấn luyện Điều hướng, Đa cửa sổ & Thao tác Mã nguồn "Không chuột"

---

### DRILL 01 (DAY 01): THỬ THÁCH BUNG 3 CỬA SỔ ĐỘC LẬP TRONG 10 GIÂY
* **Nhiệm vụ**:
  1. Mở IDE ở chế độ 1 cửa sổ ban đầu.
  2. Bấm <kbd>Ctrl</kbd> + <kbd>K</kbd> rồi bấm <kbd>O</kbd> để bung tab file hiện tại ra cửa sổ Editor độc lập.
  3. Chuột phải vào tiêu đề Chat (hoặc mở Command Palette <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> $\rightarrow$ gõ `Move View into New Window`) để bung khung Chat AI ra cửa sổ thứ 2.
  4. Mở Terminal bằng <kbd>Ctrl</kbd> + <kbd>`</kbd>, chuột phải tab Terminal $\rightarrow$ `Move Terminal into New Window` thành cửa sổ thứ 3.
  5. Dùng <kbd>Alt</kbd> + <kbd>Tab</kbd> lướt qua lại giữa 3 cửa sổ liên tục 5 vòng.
* **Thời gian chuẩn**: < 10 giây. Không được bấm nhầm cửa sổ khác của Windows.

---

### DRILL 02 (DAY 02): FUZZY FILE SEARCH TỐC ĐỘ CAO
* **Nhiệm vụ**:
  1. Đóng toàn bộ tab đang mở bằng <kbd>Ctrl</kbd> + <kbd>K</kbd> <kbd>W</kbd>.
  2. Bấm <kbd>Ctrl</kbd> + <kbd>P</kbd>, gõ `charter` $\rightarrow$ dùng phím mũi tên chọn file `COMPANY_CHARTER.md` của Company 12 $\rightarrow$ <kbd>Enter</kbd>.
  3. Bấm <kbd>Ctrl</kbd> + <kbd>P</kbd>, gõ `settings.json` $\rightarrow$ <kbd>Enter</kbd>.
  4. Bấm <kbd>Ctrl</kbd> + <kbd>P</kbd>, gõ `settings.json:25` $\rightarrow$ <kbd>Enter</kbd> (con trỏ phải nhảy đúng vào dòng 25).
  5. Bấm <kbd>Ctrl</kbd> + <kbd>B</kbd> để tắt thanh Sidebar nếu đang mở.
* **Thời gian chuẩn**: < 6 giây cho cả 5 bước.

---

### DRILL 03 (DAY 03): SẮP XẾP LẠI KHỐI MÃ BẰNG <kbd>Alt</kbd> + <kbd>↑</kbd>/<kbd>↓</kbd>
* **Đoạn code giả lập bài tập**:
```python
# [BÀI TẬP]: Hãy dùng Alt + Up/Down để sắp xếp lại đúng thứ tự logic thực thi
def process_order(order_id):
    send_confirmation_email(order_id)  # Dòng 3 (Đáng lẽ phải ở cuối)
    order = fetch_order_from_db(order_id)  # Dòng 1
    charge_credit_card(order.total)  # Dòng 2
    log_order_success(order_id)  # Dòng 4
```
* **Nhiệm vụ**: Đặt con trỏ tại dòng `send_confirmation_email`, bấm <kbd>Alt</kbd> + <kbd>↓</kbd> hai lần để đưa nó xuống trước dòng `log_order_success`. Dùng <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>↓</kbd> để nhân bản dòng log. Xóa dòng thừa bằng <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>K</kbd>.
* **Thời gian chuẩn**: < 5 giây.

---

### DRILL 04 (DAY 04): ĐA CON TRỎ <kbd>Ctrl</kbd> + <kbd>D</kbd> BIẾN HÓA DỮ LIỆU
* **Đoạn code giả lập bài tập**:
```python
# [BÀI TẬP]: Hãy đổi toàn bộ tiền tố "temp_" thành "final_" và chuyển giá trị thành chuỗi
temp_alpha = 100
temp_beta = 200
temp_gamma = 300
temp_delta = 400
```
* **Nhiệm vụ**:
  1. Đặt con trỏ tại chữ `temp_` đầu tiên.
  2. Bấm <kbd>Ctrl</kbd> + <kbd>D</kbd> 3 lần nữa để chọn cả 4 chữ `temp_`.
  3. Gõ `final_`.
  4. Bấm phím <kbd>End</kbd> (con trỏ của cả 4 dòng nhảy về cuối dòng).
  5. Bấm <kbd>Home</kbd> để nhảy về đầu dòng.
* **Thời gian chuẩn**: < 4 giây.

---

### DRILL 05 (DAY 05): TRUY VẾT HÀM XUYÊN DỰ ÁN
* **Nhiệm vụ**:
  1. Mở bất kỳ file Python nào có gọi hàm ngoại vi.
  2. Bấm <kbd>F12</kbd> để nhảy vào file định nghĩa gốc.
  3. Bấm <kbd>Shift</kbd> + <kbd>F12</kbd> để mở bảng danh sách tham chiếu (References panel).
  4. Dùng phím mũi tên xem nhanh 2 nơi gọi hàm khác.
  5. Bấm <kbd>Alt</kbd> + <kbd>←</kbd> hai lần để lùi về đúng vị trí file và dòng code ban đầu.
* **Thời gian chuẩn**: < 8 giây.

---

### DRILL 06 (DAY 06): TÁI CẤU TRÚC TOÀN CỤC BẰNG <kbd>F2</kbd>
* **Nhiệm vụ**:
  1. Đặt con trỏ vào tên một hàm hoặc biến dùng chung trong nhiều file.
  2. Bấm <kbd>F2</kbd>.
  3. Gõ tên mới chuẩn mực $\rightarrow$ Nhấn <kbd>Enter</kbd>.
  4. Bấm <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>M</kbd> để mở Problems panel $\rightarrow$ Đảm bảo không có lỗi import hay cú pháp nào phát sinh.
* **Thời gian chuẩn**: < 5 giây.

---

### DRILL 07 (DAY 07): THỬ THÁCH "MOUSE LOCKOUT" 60 PHÚT
* **Quy tắc**:
  - Dán một mẩu giấy che mắt đọc laser của chuột quang, hoặc rút đầu thu USB / tắt bluetooth chuột.
  - Viết hoàn chỉnh một module kiểm thử unit test mới hoặc giải một bài tập thuật toán.
  - Nếu bàn tay bạn chạm vào chuột $\rightarrow$ Thử thách thất bại và phải bấm giờ lại từ đầu!
