# 📘 SỔ TAY CẤU HÌNH CISCO SECURE ACS 4.2 TRÊN WINDOWS SERVER 2003 (LAB 4)
## Hệ Thống Quản Trị Xác Thực & Cấp Quyền Tập Trung Cho Công Ty Banana Corp
> **Mục tiêu:** Cấu hình máy chủ TACACS+ Server để tiếp nhận các yêu cầu xác thực từ Router `TACACS_Client`, quản lý người dùng và phân quyền truy cập.

![Quy trình trao đổi gói tin AAA TACACS+](aaa_tacacs_protocol_flow.jpg)

---

## 1. QUY TRÌNH CÀI ĐẶT 3 BƯỚC BẮT BUỘC TRÊN WINDOWS SERVER 2003

Khởi động máy ảo **`TACACS_Server`** (đặt IP: `10.0.0.100/24`, Gateway: `10.0.0.1`, tắt Firewall) và chạy bộ cài theo đúng thứ tự:

### Bước 1: Cài đặt Java Runtime Environment (JRE)
1. Chạy file: **`jre-6u13-windows-i586-p-s.exe`**.
2. Bấm `Next` $\rightarrow$ `Typical Setup` $\rightarrow$ Chờ cài đặt xong $\rightarrow$ Bấm `Finish`.
   > *Lý do:* Engine quản trị ACS sử dụng các Java Applet để render cây thư mục bảo mật.

### Bước 2: Cài đặt Cisco Secure ACS v4.2 for Windows
1. Giải nén file: **`ACSv4.2.124 FULL-K9.zip`** ra thư mục trên màn hình Desktop.
2. Mở thư mục vừa giải nén $\rightarrow$ chạy file **`setup.exe`**:
   - Màn hình *Welcome* $\rightarrow$ Bấm `Next` $\rightarrow$ Bấm `Accept` bản quyền.
   - Màn hình *Database Option*: Tích chọn **`Local Database`** (Cơ sở dữ liệu người dùng cục bộ của ACS).
   - Màn hình *TACACS+ Shared Secret*:
     - Nhập Secret Key: **`ciscobanana123`**
     - Xác nhận lại Secret Key: **`ciscobanana123`**
   - Màn hình *Authentication Configuration*: Tích chọn **`Yes, I want to configure authentication`**.
   - Bấm `Next` cho đến khi cài đặt hoàn tất.
3. Khi kết thúc, hệ thống sẽ tự động bật các service của Cisco ACS chạy ngầm. Bấm **`Finish`**.

### Bước 3: Cài đặt Mozilla Firefox 2.0
1. Chạy file: **`Firefox Setup 2.0.0.20.exe`**.
2. Chọn cài đặt **`Standard`** $\rightarrow$ Bấm `Next` đến khi hoàn tất.
   > *Lý do:* Trình duyệt Internet Explorer 6 mặc định trên Windows Server 2003 sẽ bị lỗi JavaScript và vỡ khung iframe khi mở giao diện ACS. Bắt buộc phải dùng Firefox 2.0!

---

## 2. CẤU HÌNH MÁY CHỦ ACS TRÊN GIAO DIỆN WEB (PORT 2002)

Mở **Firefox 2.0** trên máy ảo `TACACS_Server`, gõ địa chỉ:  
👉 **`http://127.0.0.1:2002`** (hoặc `http://10.0.0.100:2002`).

### 1. Thêm Router Cisco làm AAA Client:
1. Nhìn vào thanh menu màu xanh ở cạnh trái, click vào: **`Network Configuration`**.
2. Tại khung **AAA Clients**, bấm nút **`Add Entry`**:
   - **AAA Client Hostname**: Điền `TACACS_Client`
   - **AAA Client IP Address**: Điền **`10.0.0.1`** *(Chính là IP cổng Fa2/1 của Router nối về Server)*
   - **Key**: Điền **`ciscobanana123`**
   - **Authenticate Using**: Tích chọn ô tròn 👉 **`TACACS+ (Cisco IOS)`**
3. Kéo xuống dưới cùng, bấm nút **`Submit + Restart`**.  
   *(Chờ 5–10 giây để service ACS khởi động lại và nhận diện Router)*.

---

### 2. Kích hoạt tính năng phân quyền (Interface Configuration):
1. Click vào menu bên trái: **`Interface Configuration`**.
2. Click vào liên kết: **`TACACS+ (Cisco IOS)`**:
   - Tại mục **User**, tích chọn các ô:
     - ☑ **Shell (exec)**
     - ☑ **Command Authorization**
   - Tại mục **Group**, tích chọn:
     - ☑ **Shell (exec)**
3. Bấm **`Submit`**.

---

### 3. Tạo tài khoản cho nhân viên công ty Banana Corp:
1. Click vào menu bên trái: **`User Setup`**.
2. Tại ô *User*, gõ tên: **`nhanvien`** $\rightarrow$ bấm nút **`Add/Edit`**:
   - Mục **User Setup**:
     - Password Authentication: Chọn **`ACS Internal Database`**.
     - Nhập mật khẩu: **`123456`**
     - Xác nhận lại mật khẩu: **`123456`**
   - Mục **TACACS+ Settings**:
     - Tích chọn ô: ☑ **Shell (exec)**
     - Tích chọn: ☑ **Privilege level** $\rightarrow$ Điền số: **`1`** *(Quyền User thông thường)*.
3. Bấm nút **`Submit`**.

*(Tùy chọn: Bạn có thể tạo thêm user `admin` với Password `cisco123` và gán `Privilege level = 15` để làm tài khoản Quản trị viên cấp cao).*

---

## 3. KIỂM TRA NHẬT KÝ XÁC THỰC (MONITORING & LOGGING)

Mỗi khi một nhân viên từ Client PC gõ lệnh Telnet vào Router:
1. Vào menu bên trái của ACS: **`Reports and Activity`**.
2. Click vào mục: **`Passed Authentications`**:
   - Bạn sẽ nhìn thấy nhật ký hiển thị rõ:
     - Thời gian (Date/Time)
     - User: `nhanvien`
     - Caller-ID / Client IP: `192.168.1.10`
     - AAA Client: `TACACS_Client` (10.0.0.1)
     - Authen status: **PASS**
3. Nếu gõ sai mật khẩu, vào mục **`Failed Attempts`** để xem lý do bị từ chối truy cập!
