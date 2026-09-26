# 📘 SỔ TAY CẤU HÌNH CISCO SECURE ACS 4.2 TRÊN WINDOWS SERVER 2003 (LAB 4)
## Hệ Thống Quản Trị Xác Thực & Cấp Quyền Tập Trung Cho Công Ty Banana Corp

> **Mục tiêu:** Cài đặt và cấu hình máy chủ TACACS+ Server (Cisco Secure ACS v4.2) chuẩn xác từng thao tác, đối chiếu 100% với giao diện thực tế trên máy ảo Windows Server 2003 (`TACACS_Server_Banana`).

---

## 🗺️ TỔNG QUAN BẢN ĐỒ ĐỊA CHỈ & THÔNG SỐ KỸ THUẬT

| Thành phần | Tên thiết bị / Dịch vụ | Địa chỉ IP / Port | Thông số xác thực |
|:---|:---|:---|:---|
| **TACACS+ Server** | `TACACS_Server_Banana` (Win 2003) | `10.0.0.100/24` (VMnet1) | Web Admin: Port `2002` |
| **AAA Client (Router)** | `TACACS_Client` (Cisco c3725) | `10.0.0.1/24` (Cổng Fa2/1) | TACACS+ Port: `49 TCP` |
| **TACACS+ Shared Secret** | Khóa bí mật dùng chung | Toàn mạng nội bộ | **`ciscobanana123`** |
| **Tài khoản User** | Nhân viên vận hành | Username: **`nhanvien`** | Pass: **`123456`** (Privilege: **1**) |
| **Tài khoản Admin** | Quản trị viên hệ thống | Username: **`admin`** | Pass: **`cisco123`** (Privilege: **15**) |

---

## PHẦN 1: QUY TRÌNH CÀI ĐẶT CISCO SECURE ACS V4.2 (TỪNG MÀN HÌNH WIZARD)

Trước khi bắt đầu, bảo đảm máy ảo Windows Server 2003 đã đặt IP tĩnh: `10.0.0.100`, Subnet mask: `255.255.255.0`, Default Gateway: `10.0.0.1`, và **Windows Firewall đã TẮT (OFF)**.

### Bước 1.1: Cài đặt Java Runtime Environment (JRE)
1. Trên màn hình Desktop, chạy file: **`jre-6u13-windows-i586-p-s.exe`**.
2. Chọn **`Typical Setup`** $\rightarrow$ Bấm **`Next`** $\rightarrow$ Chờ copy file $\rightarrow$ Bấm **`Finish`**.
   > *Giải thích:* ACS 4.2 sử dụng các Java Applet để render cây thư mục phân quyền trên giao diện quản trị.

---

### Bước 1.2: Cài đặt Cisco Secure ACS v4.2 (Chi tiết từng hộp thoại)
Giải nén file **`ACSv4.2.124 FULL-K9.zip`** ra Desktop $\rightarrow$ Mở thư mục $\rightarrow$ Nhấp đúp vào **`setup.exe`**:

1. **Hộp thoại 1: Welcome**
   - Tiêu đề: *Welcome to the CiscoSecure ACS Setup Program*.
   - Thao tác: Bấm **`Next >`**.

2. **Hộp thoại 2: Software License Agreement**
   - Tiêu đề: *Software License Agreement*.
   - Thao tác: Bấm nút **`Accept`**.

3. **Hộp thoại 3: Internet Authentication Service Detected**
   - Nội dung: Windows Server 2003 phát hiện dịch vụ IAS (RADIUS mặc định của Microsoft) có thể xung đột cổng.
   - Thao tác: Tích chọn ô tròn 👉 **`Disable IAS (recommended)`** $\rightarrow$ Bấm **`Next >`**.

4. **Hộp thoại 4: Before You Begin (Kiểm tra điều kiện tiên quyết)**
   - Hiện trạng: Nút `Next >` mặc định bị **mờ (vô hiệu hóa)**.
   - Thao tác: **Tích chọn đủ cả 4 ô vuông (Checkboxes)**:
     - ☑ `End-user clients can successfully connect to AAA clients`
     - ☑ `This Windows Server can ping the AAA clients`
     - ☑ `Any Cisco IOS AAA clients are running Cisco IOS release 11.1 or later`
     - ☑ `Microsoft Internet Explorer v6.0 SP1/7.0 or Netscape v8.0 or Firefox 2.0 is installed`
   - Quan sát: Nút **`Next >`** sáng lên $\rightarrow$ Bấm **`Next >`**.

5. **Hộp thoại 5: Advanced Options**
   - Nội dung: Hỏi bạn có muốn hiển thị các tính năng nâng cao (như giới hạn thời gian đăng nhập, số session, nhân bản CSDL) lên giao diện Web hay không.
   - Thao tác: **Để nguyên mặc định (không tích chọn ô nào cả)** $\rightarrow$ Bấm **`Next >`**.
   - *(Lưu ý: Tất cả các mục này có thể bật lại bất cứ lúc nào trong menu web sau này)*.

6. **Hộp thoại 6: Active Service Monitoring**
   - Nội dung: Cơ chế tự động giám sát và phục hồi khi dịch vụ ACS gặp lỗi.
   - Thao tác: **Giữ nguyên toàn bộ mặc định**:
     - ☑ `Enable Log-in Monitoring` (Script to execute: `*Restart All`)
     - ☐ `Enable Mail Notifications` (để trống vì không dùng SMTP Server)
   - Bấm **`Next >`**.

7. **Hộp thoại 7: Database Option**
   - Nội dung: Chọn loại cơ sở dữ liệu lưu trữ tài khoản người dùng.
   - Thao tác: Tích chọn ô tròn 👉 **`Local Database`** (Cơ sở dữ liệu người dùng cục bộ của ACS) $\rightarrow$ Bấm **`Next >`**.

8. **Hộp thoại 8: TACACS+ Shared Secret**
   - Nhập vào 2 ô:
     - **Secret Key**: gõ `ciscobanana123`
     - **Confirm Secret Key**: gõ `ciscobanana123`
   - Bấm **`Next >`**.

9. **Hộp thoại 9: Service Initiation & Tiến trình cài đặt**
   - Tích chọn: **`Yes, I want to start the CiscoSecure ACS Service now`** (Khởi động dịch vụ ngay).
   - Bấm **`Next >`** để bộ cài bắt đầu giải nén file.

10. **Hộp thoại 10: Setup Complete**
    - Trình cài đặt hoàn tất đăng ký các Windows Service (`CSAdmin`, `CSAuth`, `CSTacacs`).
    - Bấm nút **`Finish`**.

---

### Bước 1.3: Cài đặt Trình duyệt Mozilla Firefox 2.0
1. Trên Desktop, chạy file: **`Firefox Setup 2.0.0.20.exe`**.
2. Chọn kiểu cài đặt: **`Standard`** $\rightarrow$ Bấm **`Next`** đến khi kết thúc $\rightarrow$ Bấm **`Finish`**.
   > *⚠️ Cảnh báo bắt buộc:* Không dùng Internet Explorer 6 có sẵn của Windows Server 2003 vì IE6 chặn iframe và Script của ACS khiến màn hình trắng xóa. Luôn dùng Firefox 2.0!

---

## PHẦN 2: NHẬN DIỆN GIAO DIỆN WEB QUẢN TRỊ CISCO ACS (PORT 2002)

Mở trình duyệt **Firefox 2.0**, gõ địa chỉ vào thanh URL:  
👉 **`http://127.0.0.1:2002`** (hoặc `http://10.0.0.100:2002`).

Giao diện Web của Cisco Secure ACS v4.2 gồm 2 phần chính:
- **Cột Menu màu xanh bên trái:** Chứa các phân hệ chức năng:
  - `User Setup` *(Tạo/sửa user)*
  - `Group Setup` *(Quản lý nhóm quyền)*
  - `Shared Profile Components` *(Bộ lọc lệnh Command Authorization)*
  - `Network Configuration` *(Khai báo Router AAA Client)*
  - `System Configuration` *(Cấu hình cổng, service, thời gian)*
  - `Interface Configuration` *(Bật/tắt các thuộc tính hiển thị trên Web)*
  - `Reports and Activity` *(Xem log đăng nhập PASS / FAIL)*
- **Khung nội dung bên phải:** Nơi hiển thị bảng dữ liệu và form cấu hình chi tiết.

---

## PHẦN 3: 4 BƯỚC CẤU HÌNH BẮT BUỘC TRÊN WEB ACS

Thực hiện chuẩn xác theo đúng thứ tự 4 bước sau (không được nhảy cóc):

```
[Bước 1: Network Config]  --> Khai báo Router TACACS_Client & Key
         ↓
[Bước 2: Interface Config]--> BẬT tính năng Shell (exec) để ACS hiển thị ô phân quyền
         ↓
[Bước 3: Group Setup]     --> Cấu hình Group 1 gán Privilege Level = 1
         ↓
[Bước 4: User Setup]      --> Tạo User nhanvien gán vào Group 1
```

---

### BƯỚC 1: KHAI BÁO ROUTER CISCO (NETWORK CONFIGURATION)

Mục đích: Cho phép máy chủ ACS chấp nhận yêu cầu xác thực gửi đến từ Router `10.0.0.1`.

1. Nhìn sang cột Menu bên trái, click vào: **`Network Configuration`**.
2. Tại khung nội dung bên phải, tìm bảng có tiêu đề **`AAA Clients`**, click vào nút: **`Add Entry`**.
3. Điền thông tin vào các trường:
   - **AAA Client Hostname**: Gõ chính xác `TACACS_Client` (hoặc hostname của Router).
   - **AAA Client IP Address**: Gõ `10.0.0.1` *(Địa chỉ IP cổng Fa2/1 của Router nối với máy chủ)*.
   - **Key**: Gõ `ciscobanana123` *(Khóa bí mật dùng chung)*.
   - **Authenticate Using**: Tích chọn ô tròn 👉 **`TACACS+ (Cisco IOS)`**.
4. Kéo xuống dưới cùng trang, click vào nút: **`Submit + Restart`**.
   > *Lưu ý:* ACS sẽ mất khoảng 5–10 giây để khởi động lại tiến trình `CSTacacs` và nạp cấu hình Router mới.

---

### BƯỚC 2: KÍCH HOẠT THUỘC TÍNH PHÂN QUYỀN (INTERFACE CONFIGURATION)

> ⚠️ **ĐÂY LÀ BƯỚC QUAN TRỌNG NHẤT VÀ DỄ BỊ BỎ SÓT:**  
> Nếu không bật bước này, khi vào `Group Setup` hoặc `User Setup`, bạn sẽ **KHÔNG THẤY** bất kỳ tùy chọn nào liên quan đến `Shell (exec)` hay `Privilege level`!

1. Tại Menu bên trái, click vào: **`Interface Configuration`**.
2. Tại khung bên phải, click vào dòng chữ màu xanh: **`TACACS+ (Cisco IOS)`**.
3. Trang cấu hình bảng dịch vụ hiện ra, tìm đến mục **`TACACS+ Services`**:
   - Tìm hàng có tên: **`Shell (exec)`**:
     - Tích chọn ô vuông ở cột 👉 **`User`**
     - Tích chọn ô vuông ở cột 👉 **`Group`**
4. Kéo xuống dưới cùng trang, click nút: **`Submit`**.

---

### BƯỚC 3: CẤU HÌNH NHÓM QUYỀN HẠN (GROUP SETUP)

Mục đích: Thiết lập mức đặc quyền mặc định cho nhóm nhân viên thông thường.

1. Tại Menu bên trái, click vào: **`Group Setup`**.
2. Tại khung bên phải, ở danh sách thả xuống (dropdown) chọn: **`Group 1`** $\rightarrow$ Click nút: **`Edit Settings`**.
3. Đổi tên nhóm (tùy chọn):
   - **Group Name**: Gõ `NhanVien_Banana`.
4. Cuộn chuột xuống dưới đến mục **`TACACS+ Settings`**:
   - Tích chọn ô vuông: ☑ **`Shell (exec)`**.
   - Ngay dưới mục Shell (exec), tích chọn ô vuông: ☑ **`Privilege level`** $\rightarrow$ Điền số: **`1`**.
5. Cuộn xuống cuối trang, click nút: **`Submit + Restart`**.

---

### BƯỚC 4: TẠO TÀI KHOẢN NGƯỜI DÙNG (USER SETUP)

#### 4.1. Tạo tài khoản nhân viên thường (`nhanvien` - Privilege 1)
1. Tại Menu bên trái, click vào: **`User Setup`**.
2. Tại ô nhập liệu *User*, gõ: **`nhanvien`** $\rightarrow$ Click nút: **`Add/Edit`**.
3. Điền thông tin tại các mục:
   - **Password Authentication**: Chọn **`ACS Internal Database`**.
   - **Password**: Gõ `123456`.
   - **Confirm Password**: Gõ lại `123456`.
   - **Group Assigned**: Chọn **`Group 1`** (hoặc `Group 1 (NhanVien_Banana)`).
   - Cuộn xuống mục **`TACACS+ Settings`**:
     - Tích chọn: ☑ **`Shell (exec)`**.
     - Tích chọn: ☑ **`Privilege level`** $\rightarrow$ Điền: **`1`**.
4. Kéo xuống cuối trang, click nút: **`Submit`**.

#### 4.2. (Tùy chọn) Tạo tài khoản quản trị viên tối cao (`admin` - Privilege 15)
1. Vẫn ở trang **`User Setup`**, gõ vào ô *User*: **`admin`** $\rightarrow$ Click **`Add/Edit`**.
2. Đặt mật khẩu: `cisco123` (xác nhận lại `cisco123`).
3. Cuộn xuống mục **`TACACS+ Settings`**:
   - Tích chọn: ☑ **`Shell (exec)`**.
   - Tích chọn: ☑ **`Privilege level`** $\rightarrow$ Điền: **`15`** *(Quyền Enable cao nhất, cấu hình toàn bộ Router)*.
4. Click nút: **`Submit`**.

---

## PHẦN 4: KIỂM TRA NHẬT KÝ VÀ GIÁM SÁT (REPORTS AND ACTIVITY)

Sau khi từ máy trạm Client hoặc Router thực hiện đăng nhập kiểm thử qua Telnet/Console:

1. Click vào Menu bên trái: **`Reports and Activity`**.
2. Chọn xem các loại báo cáo:
   - **`Passed Authentications`**:
     - Click vào tên file báo cáo ngày hiện tại (ví dụ: `Passed Authentications.csv`).
     - Bảng nhật ký sẽ hiển thị đầy đủ:
       - **Date & Time**: Thời điểm đăng nhập.
       - **User Name**: `nhanvien` hoặc `admin`.
       - **Group**: `Group 1`.
       - **Caller-ID**: IP của máy trạm truy cập (ví dụ: `192.168.1.10`).
       - **NAS IP**: `10.0.0.1` (Router TACACS_Client).
       - **Status**: **Authen OK / PASS**.
   - **`Failed Attempts`**:
     - Hiển thị các trường hợp bị từ chối kèm nguyên nhân:
       - *Wrong Password* (Sai mật khẩu).
       - *Unknown User* (User chưa khai báo trên ACS).
       - *Invalid Shared Secret* (Sai khóa bí mật giữa Router và ACS).

---

## ⚠️ CÁC LỖI THỰC TẾ HAY GẶP VÀ CÁCH KHẮC PHỤC

| Hiện tượng lỗi | Nguyên nhân gốc rễ | Cách khắc phục triệt để |
|:---|:---|:---|
| **Mở Firefox vào `http://127.0.0.1:2002` báo "Unable to connect"** | Các Windows Service của ACS chưa chạy hoặc bị treo sau khi khởi động lại máy. | Mở `Start` $\rightarrow$ `Run` $\rightarrow$ gõ `cmd` $\rightarrow$ gõ lệnh `net start csadmin` và `net start cstacacs`. |
| **Vào `Group Setup` không thấy mục `TACACS+ Settings`** | Chưa kích hoạt dịch vụ TACACS+ trong Interface Configuration. | Vào lại `Interface Configuration` $\rightarrow$ `TACACS+ (Cisco IOS)` $\rightarrow$ Tích chọn `Shell (exec)` cho cột User và Group $\rightarrow$ Bấm `Submit`. |
| **Router báo `Authentication Failed` dù nhập đúng user/pass** | Sai Shared Secret Key giữa Router và Server (`ciscobanana123`). | Kiểm tra lại lệnh trên Router: `tacacs-server key ciscobanana123` và mục Key trong `Network Configuration` của ACS xem có gõ thừa khoảng trắng không. |
| **Giao diện Web ACS bị trắng xóa, không bấm được menu** | Sử dụng trình duyệt Internet Explorer 6 thay vì Firefox 2.0. | Đóng IE6 lại, cài đặt và mở bằng **Firefox 2.0**. |

---

### 💡 Micro-quiz / Câu hỏi phản biện
Tại sao trong mô hình bảo mật AAA TACACS+, việc phân chia `Privilege level = 1` cho nhân viên thường và `Privilege level = 15` cho quản trị viên lại có thể ngăn chặn nhân viên gõ các lệnh nguy hiểm như `configure terminal` hay `reload` ngay từ cấp độ giao tiếp dòng lệnh (CLI)?
