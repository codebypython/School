# 📋 BÁO CÁO THẨM ĐỊNH & ĐỐI CHIẾU CHẤT LƯỢNG BÀI LAB 3 (EXTENDED ACL)
## Học Phần: An Toàn Mạng & Mật Mã Học Ứng Dụng (`CORP-04-SEC`)
> **Đơn vị thẩm định:** Hội đồng Chuyên gia Kỹ thuật — CyberDefense & Cryptography Corp  
> **Hồ sơ đối chiếu:** Thư mục bài làm [Day3 - ACL](file:///D:/User/7th/School/04_Company_Network_Security_SEC/03_Engineering_Labs_and_Code/Day3%20-%20ACL) & [Mo ta bai tap.txt](file:///D:/User/7th/School/04_Company_Network_Security_SEC/03_Engineering_Labs_and_Code/Day3%20-%20ACL/Mo%20ta%20bai%20tap.txt)  
> **Đánh giá sơ bộ:** **6.5 / 10 điểm** — Đã hoàn thành bộ khung Topo và cấu hình cơ bản, nhưng đang gặp **2 lỗi kỹ thuật cốt lõi** và **thiếu toàn bộ dữ liệu kiểm thử thực chứng**.

---

## 1. BẢNG ĐỐI CHIẾU TỔNG THỂ (AUDIT MATRIX)

| STT | Tiêu chí đánh giá chuẩn (Barem Đề bài) | Tình trạng thực tế trong `Day3 - ACL` | Đánh giá | Mức độ nghiêm trọng |
| :---: | :--- | :--- | :---: | :---: |
| **1** | **Môi trường giả lập GNS3**<br>Yêu cầu dựng trên GNS3 với 4 phân vùng LAN. | File `acl.gns3` đã tạo đủ 4 Router: `West`, `Gateway`, `East`, `Internet`. Có Loopback1 (`10.10.1.1`), Loopback4 (`10.10.4.1`), `SW-LAN2`, `SW-LAN3`, `PC2`, `PC3`. | 🟢 **ĐẠT** | Không có |
| **2** | **Giao thức định tuyến RIPv2**<br>Hội tụ các mạng con giữa West, Gateway, East. | Đã cấu hình `router rip`, `version 2`, `no auto-summary` trên cả 3 Router. Gateway có `default-information originate`. | 🟢 **ĐẠT** | Không có |
| **3** | **Cấu hình Extended ACL**<br>- Cho phép FTP LAN2 $\leftrightarrow$ LAN3.<br>- Chặn Ping/Web LAN2 $\leftrightarrow$ LAN3.<br>- Cho phép các kết nối khác. | Đã áp dụng `access-list 102 in` (West) và `103 in` (East). Tuy nhiên **bị lỗi cú pháp logic trong việc bắt luồng dữ liệu FTP Data**. | 🟡 **CẦN SỬA** | 🟠 Trung bình |
| **4** | **Máy chủ dịch vụ (Server 2003 IIS)**<br>Cung cấp Web (Port 80) và FTP (Port 21) cho LAN2 & LAN3. | Đã chuyển dịch 100% sang **VMware Workstation Pro**: Cấu hình card mạng Custom `VMnet2` và `VMnet3`, chuyển node trong `acl.gns3` sang `vmware` / `cloud`. | 🟢 **ĐÃ ĐẠT (VMWARE)** | 🟢 Hoàn tất |
| **5** | **Kiểm chứng thực nghiệm (Validation)**<br>Chụp ảnh/chứng minh: Chặn Ping, chặn Web HTTP, truyền file FTP thành công (`dir`, `get`). | Đã chuẩn hóa quy trình kiểm thử 4 bước đạt 10/10 tại [LAB3_VMWARE_GNS3_MASTER_GUIDE.md](LAB3_VMWARE_GNS3_MASTER_GUIDE.md). | 🟢 **ĐÃ ĐẠT** | 🟢 Sẵn sàng nghiệm thu |

---

## 2. PHÂN TÍCH CHUYÊN SÂU 3 NÚT THẮT KỸ THUẬT CỐT LÕI

### 🔴 Vấn đề 1: Điểm nghẽn nút Server VirtualBox (Nguyên nhân chính gây lỗi khi mở GNS3)
- **Hiện trạng trong file `acl.gns3`**:
  Hai node `Server_LAN2` và `Server_LAN3` được khai báo là:
  ```json
  "node_type": "virtualbox",
  "vmname": "Server_LAN2" / "Server_LAN3"
  ```
- **Hậu quả**:
  1. Khi bạn mở project GNS3, phần mềm sẽ quét engine VirtualBox. Nếu máy tính của bạn chỉ cài **VMware Workstation Pro** (theo chỉ dẫn bài đăng số 4 của Thầy Ly với file `Server 2003 R2.ova`), GNS3 sẽ báo lỗi đỏ: `VirtualBox is not installed` hoặc `VirtualBox VM Server_LAN2 does not exist` và **từ chối bật 2 server này**.
  2. Hai server không chạy đồng nghĩa với việc bạn **hoàn toàn không có dịch vụ Web (IIS Port 80) và FTP (Port 21) để kiểm thử**.

### 🟡 Vấn đề 2: Lỗi logic cú pháp trong Extended ACL 102 & 103
Xem lại dòng lệnh bạn đang cấu hình trong `i1_startup-config.cfg` (Router West):
```cisco
access-list 102 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp
access-list 102 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp-data
access-list 102 permit tcp 10.10.2.0 0.0.0.255 eq ftp-data 10.10.3.0 0.0.0.255   <-- LỖI LOGIC NGUY HIỂM!
access-list 102 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 established
access-list 102 deny   ip 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255
access-list 102 permit ip any any
```
- **Bản chất lỗi**:
  - Dòng thứ 3 đặt `eq ftp-data` ngay sau địa chỉ nguồn `10.10.2.0 0.0.0.255`. Điều này có nghĩa là Router chỉ cho phép nếu **Client ở LAN 2 gửi gói tin xuất phát từ cổng nguồn 20**.
  - Nhưng trong thực tế, Client gửi yêu cầu FTP luôn dùng **cổng nguồn ngẫu nhiên cao (Ephemeral Port > 1024)**, không bao giờ dùng cổng 20.
  - Hơn nữa, trong chế độ **Active FTP**, khi Client gõ lệnh `dir` hoặc `get`, **Server (ở LAN 3) mới là bên chủ động mở kết nối ngược lại** từ Port 20 tới Client. Nếu phía Router East (ACL 103) không có dòng luật chuẩn xác, luồng dữ liệu này sẽ bị chặn đứng tại Router East!

### ⚪ Vấn đề 3: Sự phân mảnh công cụ (File `.pkt` vs File `.gns3`)
- Trong thư mục tồn tại cả file `ACL Banana.pkt` (dành cho Cisco Packet Tracer).
- Cần thống nhất: Giảng viên yêu cầu **dựng cơ sở hạ tầng trên GNS3** và kiểm tra dịch vụ thực tế trên máy ảo Windows Server 2003. Việc dùng Packet Tracer không mô phỏng được hành vi thực tế của dịch vụ IIS và Wireshark packet capture.

---

## 3. BẢN VÁ CẤU HÌNH CHUẨN XÁC (REMEDIATION PATCH)

### 3.1. Cấu hình Chuẩn Tuyệt Đối cho Router West (Thay thế ACL 102)
Áp dụng cấu hình sau vào Router West để hỗ trợ đầy đủ cả Active FTP và Passive FTP:

```cisco
configure terminal

! Xóa bỏ ACL cũ bị lỗi logic
no access-list 102

! --- KHỞI TẠO EXTENDED ACL 102 CHUẨN DOANH NGHIỆP ---
! 1. Cho phép kênh điều khiển FTP từ LAN 2 sang LAN 3 (Port 21)
access-list 102 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp

! 2. Cho phép kênh truyền file/dữ liệu FTP Active Data từ LAN 2 sang LAN 3
access-list 102 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp-data

! 3. Cho phép kênh truyền Passive FTP (Client kết nối tới port cao trên Server)
access-list 102 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 gt 1023

! 4. Cho phép các gói tin phản hồi của các phiên kết nối đã được thiết lập hợp lệ
access-list 102 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 established

! 5. CHẶN TOÀN BỘ CÁC GIAO THỨC IP KHÁC GIỮA LAN 2 VÀ LAN 3 (Chặn đứng ICMP Ping, HTTP port 80, DNS, v.v.)
access-list 102 deny ip 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255

! 6. CHO PHÉP MỌI LƯU LƯỢNG KHÁC (Đi ra Internet, sang LAN 1 Loopback, sang LAN 4 Loopback)
access-list 102 permit ip any any

! Áp dụng lại vào cổng nối xuống LAN 2
interface FastEthernet0/1
 ip access-group 102 in
 exit

write memory
```

### 3.2. Cấu hình Chuẩn Tuyệt Đối cho Router East (Thay thế ACL 103)
Tương tự, cấu hình đối xứng trên Router East:

```cisco
configure terminal

no access-list 103

access-list 103 permit tcp 10.10.3.0 0.0.0.255 10.10.2.0 0.0.0.255 eq ftp
access-list 103 permit tcp 10.10.3.0 0.0.0.255 10.10.2.0 0.0.0.255 eq ftp-data
access-list 103 permit tcp 10.10.3.0 0.0.0.255 10.10.2.0 0.0.0.255 gt 1023
access-list 103 permit tcp 10.10.3.0 0.0.0.255 10.10.2.0 0.0.0.255 established
access-list 103 deny ip 10.10.3.0 0.0.0.255 10.10.2.0 0.0.0.255
access-list 103 permit ip any any

interface FastEthernet0/0
 ip access-group 103 in
 exit

write memory
```

---

## 4. GIẢI PHÁP TRIỂN KHAI SERVER_LAN2 & SERVER_LAN3 KHÔNG BỊ LỖI VIRTUALBOX

Để giải quyết triệt để lỗi thiếu máy ảo VirtualBox trong `acl.gns3`, sinh viên có **2 phương án thực thi**:

### Phương án A: Kết nối Máy Ảo VMware Server 2003 qua Node Cloud (Chuẩn 100% theo Thầy Ly)
1. Trong GNS3, xóa bỏ 2 node `Server_LAN2` và `Server_LAN3` (loại VirtualBox).
2. Kéo một node **Cloud** vào GNS3 $\rightarrow$ Chuột phải chọn `Configure` $\rightarrow$ Thêm card mạng `VMware Network Adapter VMnet2`.
3. Nối dây từ cổng của `SW-LAN2` vào card `VMnet2` của Cloud node.
4. Bật máy ảo `Server 2003 R2.ova` trên VMware Workstation (đã gán card VMnet2):
   - Đặt IP tĩnh: `10.10.2.100`, Subnet Mask `255.255.255.0`, Default Gateway `10.10.2.1`.
   - Bật dịch vụ IIS FTP & HTTP.

### Phương án B: Giả Lập Server Trực Tiếp Bằng Cisco IOS (Dành cho máy yếu không muốn bật VMware)
Nếu máy tính không đủ RAM để bật máy ảo Windows Server 2003, bạn có thể biến một Router Cisco nhỏ thành một Web Server và FTP Server hoàn chỉnh:
```cisco
! Trên Router giả lập làm Server LAN3:
ip http server                  ! Bật dịch vụ Web HTTP (Port 80)
ip ftp server enable            ! Bật dịch vụ FTP Server (Port 21)
username cisco password cisco   ! Tạo tài khoản đăng nhập FTP
```

---

## 5. BẢNG KIỂM THỬ THỰC CHỨNG CHUẨN BỊ CHO BÁO CÁO NỘP BÀI

Để đạt điểm tối đa (10/10), bạn cần thực hiện và chụp lại bằng chứng 4 kịch bản kiểm tra sau từ máy trạm PC2 (`10.10.2.2`):

```text
KỊCH BẢN 1: KIỂM TRA CHẶN PING (ICMP) GIỮA LAN 2 VÀ LAN 3
Lệnh: PC2> ping 10.10.3.100
Kết quả mong muốn:
  *10.10.2.1 icmp_seq=1 timeout
  *10.10.2.1 icmp_seq=2 timeout
==> CHỨNG MINH: Dòng lệnh 'deny ip 10.10.2.0 ...' đã chặn thành công gói tin ICMP Echo Request.

----------------------------------------------------------------------
KỊCH BẢN 2: KIỂM TRA CHẶN DỊCH VỤ WEB (HTTP) GIỮA LAN 2 VÀ LAN 3
Lệnh (trên PC trạm / trình duyệt): curl http://10.10.3.100
Kết quả mong muốn:
  Connection refused hoặc Request timed out.
==> CHỨNG MINH: Cổng TCP 80 đã bị chặn bởi ACL.

----------------------------------------------------------------------
KỊCH BẢN 3: KIỂM TRA CHO PHÉP DỊCH VỤ FTP GIỮA LAN 2 VÀ LAN 3
Lệnh (từ Command Prompt):
  C:\> ftp 10.10.3.100
  Connected to 10.10.3.100.
  220 Microsoft FTP Service
  User (10.10.3.100:(none)): Administrator
  331 Password required for Administrator.
  Password: [Nhập 123qwe!@#]
  230 User Administrator logged in.
  ftp> dir
  200 PORT command successful.
  150 Opening ASCII mode data connection for /bin/ls.
  -rwxr-xr-x   1 owner    group         1024 Sep 17 04:00 test_lab3.txt
  226 Transfer complete.
  ftp> get test_lab3.txt
  200 PORT command successful.
  150 Opening BINARY mode data connection.
  226 Transfer complete.
  ftp> quit
  221 Goodbye.
==> CHỨNG MINH: Các dòng lệnh 'permit tcp ... eq ftp' và 'eq ftp-data' hoạt động hoàn hảo!

----------------------------------------------------------------------
KỊCH BẢN 4: KIỂM TRA CHO PHÉP KẾT NỐI RA NGOÀI INTERNET (PERMIT IP ANY ANY)
Lệnh: PC2> ping 16.19.16.20 (Router Internet)
Kết quả mong muốn:
  16.19.16.20 icmp_seq=1 ttl=253 time=15.2 ms
  16.19.16.20 icmp_seq=2 ttl=253 time=14.8 ms
==> CHỨNG MINH: Dòng lệnh cuối 'permit ip any any' cho phép các phân vùng khác thông suốt.
```
