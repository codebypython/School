# 🧪 HƯỚNG DẪN THAO TÁC KIỂM TRA CHI TIẾT LAB 4
**Học phần**: An Toàn Mạng (CORP-04-SEC - DUT)  
**Nội dung**: Quy trình kiểm định xác thực AAA, phân quyền lệnh và kiểm tra nhật ký trên Cisco Secure ACS  

---

## 📋 MỤC TIÊU NGHIỆM THU
1. **Kiểm tra 1 (Authentication)**: Đăng nhập thành công bằng tài khoản lưu trên Server ACS thay vì tài khoản cục bộ của Router.
2. **Kiểm tra 2 (Authorization)**: Chứng minh tài khoản thường (`banana_operator`, Level 1) bị từ chối khi gõ lệnh cấu hình; tài khoản quản trị (`banana_admin`, Level 15) có toàn quyền.
3. **Kiểm tra 3 (Accounting & Audit Log)**: Nhật ký thời gian thực trên giao diện Web ACS hiển thị chính xác mọi phiên đăng nhập và câu lệnh đã thực thi.
4. **Kiểm tra 4 (High Availability / Fallback)**: Ngắt kết nối tới Server ACS, Router tự động cho phép tài khoản cục bộ `admin` đăng nhập.

---

## 🛠️ CÁC BƯỚC THAO TÁC KIỂM THỬ

### Bước 1: Kiểm thử Xác thực Người dùng Thường (banana_operator - Level 1)
Từ máy trạm Banana Client (hoặc qua Telnet từ máy tính nối vào `192.168.1.1`):
1. Kết nối Telnet:
   ```cmd
   telnet 192.168.1.1
   ```
2. Màn hình yêu cầu đăng nhập:
   ```text
   User Access Verification
   Username: banana_operator
   Password: Operator123
   ```
3. Đăng nhập thành công, màn hình hiển thị dấu nhắc User EXEC:
   ```text
   TACACS_Client>
   ```
4. Kiểm tra phân quyền lệnh: Gõ các lệnh xem thông thường $\rightarrow$ Thành công:
   ```text
   TACACS_Client> show ip interface brief
   ```
5. Thử nghiệm can thiệp cấu hình hệ thống:
   ```text
   TACACS_Client> configure terminal
   ```
   *Kết quả thực tế bắt buộc*:
   ```text
   % Command authorization failed.
   ```
   > ✅ **CHỨNG NHẬN ĐẠT**: Module Authorization của TACACS+ đã chặn đứng hành vi vượt quyền!

---

### Bước 2: Kiểm thử Xác thực Quản trị viên (banana_admin - Level 15)
1. Kết nối Telnet lại vào Router:
   ```text
   Username: banana_admin
   Password: AdminBanana!@#
   ```
2. Đăng nhập thành công, màn hình hiển thị ngay dấu nhắc Privileged EXEC:
   ```text
   TACACS_Client#
   ```
3. Gõ lệnh cấu hình:
   ```text
   TACACS_Client# configure terminal
   Enter configuration commands, one per line.  End with CNTL/Z.
   TACACS_Client(config)#
   ```
   > ✅ **CHỨNG NHẬN ĐẠT**: Người dùng `banana_admin` được ACS cấp Privilege Level 15, toàn quyền quản trị!

---

### Bước 3: Kiểm tra Nhật Ký Kiểm Toán trên Giao Diện Web Cisco Secure ACS 4.2
1. Trên máy ảo Windows Server 2003, mở trình duyệt **Firefox** (hoặc Internet Explorer).
2. Truy cập URL: `http://localhost:2002` hoặc `http://10.0.0.100:2002`.
3. Menu bên trái, chọn **Reports and Activity**:
   * Nhấp chọn mục **Passed Authentications**:
     * Quan sát thấy dòng ghi nhận: `User: banana_admin`, `Authen: TACACS+`, `Port: tty0`, `Status: Authen Passed`.
     * Dòng ghi nhận: `User: banana_operator`, `Status: Authen Passed`.
   * Nhấp chọn mục **Failed Attempts**:
     * Nếu có ai gõ sai mật khẩu, ACS ghi nhận rõ: `User: hacker`, `Reason: User unknown` hoặc `Invalid password`.
   * Nhấp chọn mục **TACACS+ Administration**:
     * Xem chi tiết từng câu lệnh mà `banana_admin` đã gõ (`configure terminal`, `interface FastEthernet0/0`...).

---

### Bước 4: Kiểm tra Trạng thái TACACS+ Server trên Cisco IOS
Tại console của Router `TACACS_Client`:
```cisco
TACACS_Client# show tacacs
```
*Kết quả mong đợi*:
```text
Tacacs+ Server -  alive: 10.0.0.100/49
               socket: 1
               opens: 12
               closes: 11
               aborts: 0
               errors: 0
               packets in: 48
               packets out: 48
```
> Trạng thái máy chủ hiển thị **`alive`** và số lượng gói `packets in / out` tăng đều $\implies$ Kết nối TCP port 49 hoạt động hoàn hảo.

---

### Bước 5: Kiểm thử Tính năng Dự phòng Fallback (Server Down)
1. Tạm dừng dịch vụ Cisco Secure ACS trên máy ảo (hoặc ngắt card mạng VMnet1).
2. Thử đăng nhập lại vào Router:
   ```text
   Username: admin
   Password: AdminBackupPass!
   ```
3. Router sau thời gian timeout 5 giây sẽ tự động chuyển sang CSDL cục bộ và cho phép đăng nhập vào chế độ `#`.
   > ✅ Hệ thống đảm bảo tính sẵn sàng cao (High Availability), không bao giờ bị khóa ngoài (Lockout).

---

## ⚠️ LỖI PHỔ BIẾN SINH VIÊN HAY GẶP
1. **Lệch Khóa Bí Mật TACACS+ Key**: Khóa trên Router (`tacacs-server key ciscobanana123`) khác với khóa khai báo trong Network Device Configuration trên Cisco ACS Web Interface. Khi đó Router kết nối được TCP port 49 tới Server nhưng gói tin giải mã bị lỗi $\rightarrow$ Người dùng bị từ chối đăng nhập.
2. **Quên tạo tài khoản cục bộ dự phòng (Fallback Account)**: Cấu hình `aaa authentication login default group tacacs+` mà không có từ khóa `local` ở cuối. Nếu máy chủ ACS gặp sự cố hoặc dây mạng bị đứt, Router sẽ khóa toàn bộ quản trị viên ngoài hệ thống (Lockout).
3. **Card mạng VMnet trên VMware bị bật DHCP**: Nếu `VMnet1` để chế độ DHCP tự động của VMware, máy ảo Server 2003 có thể bị nhận nhầm địa chỉ IP ngẫu nhiên thay vì IP tĩnh `10.0.0.100/24`. Cần đảm bảo tắt DHCP trên VMnet1 trong Virtual Network Editor.

---

## 💡 CÂU HỎI GỢI MỞ / MICRO-QUIZ
**Câu hỏi**: *So sánh giữa 2 giao thức bảo mật AAA phổ biến nhất hiện nay: TACACS+ (Cisco proprietary/RFC 8907) và RADIUS (IETF RFC 2865), điểm khác biệt then chốt về mặt kiến trúc vận hành và bảo vệ dữ liệu là gì?*
- A) TACACS+ chạy trên UDP trong khi RADIUS chạy trên TCP.
- B) TACACS+ phân tách độc lập 3 thành phần Authentication, Authorization, Accounting và mã hóa toàn bộ Payload gói tin (chỉ để lộ Header 12 bytes); trong khi RADIUS kết hợp Authentication và Authorization làm một, chạy trên UDP, và chỉ mã hóa duy nhất trường Password.
- C) RADIUS có tính bảo mật cao hơn TACACS+ vì mã hóa cả Header lẫn Payload.
- D) TACACS+ không hỗ trợ ghi nhận nhật ký (Accounting).
*(Đáp án đúng: **B**)*

