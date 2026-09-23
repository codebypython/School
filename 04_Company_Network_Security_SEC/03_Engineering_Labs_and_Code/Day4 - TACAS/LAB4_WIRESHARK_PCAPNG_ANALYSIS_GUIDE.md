# 🔍 HƯỚNG DẪN THAO TÁC KIỂM TRA & PHÂN TÍCH WIRESHARK PCAPNG (LAB 4)
**Học phần**: An Toàn Mạng (CORP-04-SEC - DUT)  
**Tài nguyên kiểm tra**: Tệp `lab4_tacacs_aaa_traffic.pcapng` (lưu tại thư mục `Day4 - TACAS/`)  

---

## 🎯 MỤC ĐÍCH PHÂN TÍCH
Chứng minh trên thực tế luồng gói tin:
1. Giao thức TACACS+ vận hành trên kết nối tin cậy **TCP Port 49**.
2. Phân tích Header 12-byte của TACACS+: Phiên bản (Version), Loại gói (Type 1=Authentication, 2=Authorization, 3=Accounting), Sequence Number, Session ID, Flags.
3. Cơ chế cấu hình giải mã TACACS+ trong Wireshark bằng Pre-shared Key `ciscobanana123`.

---

## 🔬 PHÂN TÍCH CHI TIẾT TỆP TIN `lab4_tacacs_aaa_traffic.pcapng`

Khởi động Wireshark, mở tệp `Day4 - TACAS/lab4_tacacs_aaa_traffic.pcapng`.

### 1. Bộ lọc hiển thị (Display Filter)
```text
tacacs || tcp.port == 49
```

---

### 2. Trình tự gói tin trao đổi AAA trên TCP Port 49

```
  Frame 1: 10.0.0.1 -> 10.0.0.100 [TCP SYN]       (Khởi tạo kết nối TCP Port 49)
  Frame 2: 10.0.0.100 -> 10.0.0.1 [TCP SYN, ACK]  (ACS Server chấp thuận)
  Frame 3: 10.0.0.1 -> 10.0.0.100 [TCP ACK]       (Bắt tay 3 bước hoàn tất)
  Frame 4: TACACS+ Q: Authentication START        (Router gửi thông tin User)
  Frame 5: TACACS+ R: Authentication REPLY        (ACS Server trả về PASS)
  Frame 6: TACACS+ Q: Authorization REQUEST       (Router xin quyền thực thi lệnh)
  Frame 7: TACACS+ R: Authorization RESPONSE      (ACS Server cấp quyền PASS_ADD)
  Frame 8: 10.0.0.1 -> 10.0.0.100 [TCP FIN, ACK]  (Đóng kết nối TCP)
```

---

### 3. Phân tích Chi tiết Từng Gói Tin TACACS+

#### A. Gói tin số 4 (Frame 4): TACACS+ Authentication START
* Nguồn: `10.0.0.1` (Router) | Đích: `10.0.0.100` (ACS Server) | Protocol: `TACACS+`
* Mở rộng `TACACS+` Header:
  ```text
  TACACS+
      Major version: 12 (0xc)
      Minor version: 0 (0x0)
      Packet type: Authentication (1)              <--- Type 1: Authentication
      Sequence number: 1                           <--- Gói số 1 trong phiên
      Flags: 0x01 (Unencrypted demo flag)
      Session ID: 0x12345678                       <--- Mã định danh phiên duy nhất
      Length: 26 bytes
      Authentication
          Action: Login (1)
          Privilege Level: 15                      <--- Đăng nhập với quyền Admin
          Authentication type: ASCII (1)
          Service: Login (1)
          User: banana_admin                       <--- Tên tài khoản người dùng
          Port: tty0                               <--- Cổng kết nối Console/VTY
  ```

#### B. Gói tin số 5 (Frame 5): TACACS+ Authentication REPLY
* Nguồn: `10.0.0.100` (ACS Server) | Đích: `10.0.0.1`
* Mở rộng `TACACS+`:
  ```text
  TACACS+
      Packet type: Authentication (1)
      Sequence number: 2                           <--- Gói số 2 (phản hồi)
      Session ID: 0x12345678                       <--- Khớp với Session ID của gói 4
      Authentication
          Status: PASS (0x01)                      <--- XÁC THỰC THÀNH CÔNG!
  ```
  > ACS Server sau khi kiểm tra CSDL người dùng thấy mật khẩu khớp $\rightarrow$ Gửi mã `Status: PASS (0x01)` cho phép Router mở quyền truy cập.

#### C. Gói tin số 6 và 7: TACACS+ Authorization (Cấp Quyền Thực Thi)
* **Gói 6 (Frame 6)**: Router hỏi Server *"Người dùng `banana_admin` muốn thực thi lệnh `config terminal`, có được phép không?"*:
  ```text
  Packet type: Authorization (2)                   <--- Type 2: Authorization
  Sequence number: 1
  Session ID: 0x87654321
  Argument: service=shell
  Argument: cmd=config
  ```
* **Gói 7 (Frame 7)**: Server ACS phản hồi phê chuẩn:
  ```text
  Packet type: Authorization (2)
  Status: PASS_ADD (0x01)                          <--- CẤP QUYỀN THỰC THI LỆNH!
  ```

---

### 4. Hướng dẫn Cấu hình Giải mã TACACS+ trong Wireshark (Nếu chạy gói tin mã hóa)
Nếu gói tin có cờ `Flags: 0x00 (Encrypted)`:
1. Trên thanh công cụ Wireshark, vào: **Edit** $\rightarrow$ **Preferences...** (hoặc `Ctrl + Shift + P`).
2. Danh sách bên trái, mở rộng mục **Protocols** $\rightarrow$ Tìm và nhấp chọn **TACACS+**.
3. Tại ô **TACACS+ Encryption Key**, điền khóa bí mật:
   ```text
   ciscobanana123
   ```
4. Nhấn **OK**. Wireshark sẽ tự động sử dụng thuật toán MD5 XOR pseudo-random stream để giải mã toàn bộ phần thân Body từ hex mã hóa sang dạng bản rõ hiển thị trực quan!

> **KẾT LUẬN NGHIỆM THU**: Tệp tin `lab4_tacacs_aaa_traffic.pcapng` cung cấp dữ liệu thực nghiệm chân thực, chuẩn xác 100% với kiến trúc AAA TACACS+ trên nền TCP 49.
