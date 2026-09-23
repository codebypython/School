# 🍌 CẨM NANG MASTER LAB 4: TRIỂN KHAI AAA (TACACS+) CHO CÔNG TY BANANA TRÊN VMWARE & GNS3 (A - Z)
## Học Phần: An Toàn Mạng & Mật Mã Học Ứng Dụng (`CORP-04-SEC`)
> **Tác giả:** DUT Cyber Security Mentor — CyberDefense & Cryptography Corp  
> **Nền tảng ảo hóa:** VMware Workstation Pro (100% Free) + GNS3 All-in-One  
> **Mục tiêu:** Kiểm soát tập trung truy cập Internet cho nhân viên Banana Corp qua xác thực Authentication và cấp quyền Authorization của Cisco Secure ACS 4.2 trên VMware Windows Server 2003.

---

## 📑 MỤC LỤC
1. [Thiết Kế Mạng Ảo Banana Corp Với VMware VMnet](#1-thiết-kế-mạng-ảo-banana-corp-với-vmware-vmnet)
2. [Giai Đoạn 1: Cấu Hình Card Mạng Ảo Trên VMware Workstation](#giai-đoạn-1-cấu-hình-card-mạng-ảo-trên-vmware-workstation)
3. [Giai Đoạn 2: Dựng Máy Chủ TACACS_SERVER & Cài Đặt Cisco Secure ACS 4.2](#giai-đoạn-2-dựng-máy-chủ-tacacs_server--cài-đặt-cisco-secure-acs-42)
4. [Giai Đoạn 3: Cấu Hình Quản Trị Hệ Thống Trên Giao Diện Web Cisco ACS](#giai-đoạn-3-cấu-hình-quản-trị-hệ-thống-trên-giao-diện-web-cisco-acs)
5. [Giai Đoạn 4: Cấu Hình Toàn Bộ CLI Cho TACACS_CLIENT (Router Cisco)](#giai-đoạn-4-cấu-hình-toàn-bộ-cli-cho-tacacs_client-router-cisco)
6. [Giai Đoạn 5: Kịch Bản Nghiệm Thu Xác Thực & Cấp Quyền Đạt Điểm 10/10](#giai-đoạn-5-kịch-bản-nghiệm-thu-xác-thực--cấp-quyền-đạt-điểm-1010)

---

## 1. THIẾT KẾ MẠNG ẢO BANANA CORP VỚI VMWARE VMNET

### Sơ đồ liên kết:
```
           ┌───────────────────────────┐
           │        CLIENTS LAN        │ (Nhân viên Banana Corp)
           │     (192.168.1.0/24)      │ (GNS3 VPCS hoặc VMware VMnet2)
           └─────────────┬─────────────┘
                         │
                         ▼ Fa0/0: 192.168.1.1
           ┌───────────────────────────┐ Fa1/0: 2.2.2.1     ┌─────────────────┐
           │       TACACS_CLIENT       ├───────────────────►│    INTERNET     │
           │      (Router Cisco)       │ (2.2.2.0/24)       │ (VMnet8 NAT/vbox)
           └─────────────┬─────────────┘                    └─────────────────┘
                         │ Fa2/1: 10.0.0.1
                         ▼ (10.0.0.0/24)
           ┌───────────────────────────┐
           │       TACACS_SERVER       │
           │   (Windows Server 2003)   │ (VMware VM: TACAS_Server)
           │      IP: 10.0.0.100       │ (VMware Custom: VMnet1 Host-Only)
           │  (Cisco Secure ACS v4.2)  │
           └───────────────────────────┘
```

### Bảng phân bổ IP và Card mạng VMware:
| Thiết bị / Node | Cổng kết nối | Địa chỉ IP / Prefix | Default Gateway | VMware Network Mapping |
|:---|:---|:---|:---|:---|
| **TACACS_Client** | `Fa0/0`<br>`Fa1/0`<br>`Fa2/1` | `192.168.1.1 /24`<br>`2.2.2.1 /24`<br>`10.0.0.1 /24` | -<br>-<br>- | Cổng mạng Clients<br>Cổng kết nối Internet<br>Nối sang Cloud TACACS (VMnet1) |
| **TACACS_Server** | `Ethernet0` | `10.0.0.100 /24` | `10.0.0.1` | **Custom: Specific virtual network VMnet1** |
| **Client PC** | `Ethernet0` | `192.168.1.10 /24` | `192.168.1.1` | GNS3 VPCS hoặc VMnet2 |

---

## 2. GIAI ĐOẠN 1: CẤU HÌNH CARD MẠNG ẢO TRÊN VMWARE WORKSTATION

1. Mở VMware Workstation Pro $\rightarrow$ `Edit` $\rightarrow$ `Virtual Network Editor...` (Run as Admin).
2. Kiểm tra `VMnet1`:
   - Kiểu: **Host-only**.
   - Subnet IP: `10.0.0.0`, Subnet mask: `255.255.255.0`.
   - **Bỏ chọn**: *"Use local DHCP service..."* (đảm bảo không bị DHCP cấp sai IP).
3. Bấm **Apply** $\rightarrow$ **OK**.

---

## 3. GIAI ĐOẠN 2: DỰNG MÁY CHỦ TACACS_SERVER & CÀI ĐẶT BỘ 3 PHẦN MỀM

1. Import `Server 2003 R2.ova` vào VMware $\rightarrow$ Đặt tên máy ảo: `TACACS_Server_Banana`.
2. Vào `Settings` máy ảo $\rightarrow$ Chọn `Network Adapter` $\rightarrow$ Đổi sang **Custom: Specific virtual network** $\rightarrow$ Chọn **VMnet1**.
3. Khởi động máy ảo $\rightarrow$ Gán IP tĩnh trong Windows:
   - IP: `10.0.0.100` | Subnet: `255.255.255.0` | Gateway: `10.0.0.1`.
4. **Cài đặt bộ 3 phần mềm theo đúng thứ tự giảng viên yêu cầu**:
   - **Bước 1**: Cài đặt Java Runtime: Chạy file `jre-6u13-windows-i586-p-s.exe`.
   - **Bước 2**: Cài đặt Cisco Secure ACS: Giải nén `ACSv4.2.124 FULL-K9.zip` $\rightarrow$ Chạy `setup.exe`:
     - Chọn Database: **Local Database**.
     - Đặt TACACS+ Shared Secret Key: `ciscobanana123`.
   - **Bước 3**: Cài đặt Firefox: Chạy file `Firefox 2.0.exe` (giúp hiển thị giao diện web ACS mà không bị lỗi script như trên Internet Explorer 6).

---

## 4. GIAI ĐOẠN 3: CẤU HÌNH QUẢN TRỊ TRÊN GIAO DIỆN WEB CISCO ACS

1. Mở Firefox 2.0 trên máy Server 2003, truy cập: `http://127.0.0.1:2002` (hoặc `http://10.0.0.100:2002`).
2. Vào menu **Network Configuration**:
   - Bấm **Add Entry** trong mục `AAA Clients`.
   - AAA Client Hostname: `TACACS_Client` (hoặc `Banana_Router`).
   - AAA Client IP Address: `10.0.0.1` (IP cổng Fa2/1 của Router).
   - Shared Secret: `ciscobanana123`.
   - Authenticate Using: Chọn **TACACS+ (Cisco IOS)**.
   - Nhấn **Submit + Restart**.
3. Vào menu **User Setup**:
   - User: `nhanvien` $\rightarrow$ Bấm **Add/Edit**.
   - Password: `Password Authentication Protocol (PAP)` $\rightarrow$ Nhập mật khẩu: `123456`.
   - Group: Gán vào `Group 1`.
   - Nhấn **Submit**.

---

## 5. GIAI ĐOẠN 4: CẤU HÌNH TOÀN BỘ CLI CHO TACACS_CLIENT (ROUTER CISCO)

```cisco
enable
configure terminal
hostname TACACS_Client

! 1. Cấu hình địa chỉ IP các cổng giao tiếp
interface FastEthernet0/0
 description Mạng nội bộ nhân viên Clients
 ip address 192.168.1.1 255.255.255.0
 no shutdown
exit

interface FastEthernet1/0
 description Cổng đi ra ngoài Internet
 ip address 2.2.2.1 255.255.255.0
 no shutdown
exit

interface FastEthernet2/1
 description Cổng kết nối máy chủ TACACS Server
 ip address 10.0.0.1 255.255.255.0
 no shutdown
exit

! 2. Tạo tài khoản cục bộ dự phòng (Phòng khi TACACS Server sập)
username admin privilege 15 password 0 AdminBackupPass!

! 3. Kích hoạt kiến trúc bảo mật AAA (Authentication, Authorization, Accounting)
aaa new-model

! 4. Khai báo máy chủ TACACS+ Server và khóa bí mật chia sẻ chung
tacacs-server host 10.0.0.100
tacacs-server key ciscobanana123

! 5. Cấu hình danh sách xác thực đăng nhập (Login Authentication)
! Ưu tiên hỏi TACACS+ Server trước; nếu sập, fallback về tài khoản local
aaa authentication login default group tacacs+ local
aaa authentication enable default group tacacs+ enable

! 6. Cấu hình cấp quyền lệnh thực thi (Authorization)
aaa authorization exec default group tacacs+ local

! 7. Áp dụng chính sách xác thực lên cổng Console và VTY (Telnet/SSH)
line con 0
 login authentication default
exit

line vty 0 4
 login authentication default
 transport input telnet ssh
exit
end
write memory
```

---

## 6. GIAI ĐOẠN 5: KỊCH BẢN NGHIỆM THU & KIỂM THỬ ĐẠT ĐIỂM 10/10

### 1. Kiểm tra kết nối mạng giữa Router và Server 2003:
Trên Router gõ: `ping 10.0.0.100` $\rightarrow$ Phải nhận kết quả `Success rate is 100 percent (5/5)`.

### 2. Kiểm thử đăng nhập xác thực qua TACACS+:
Từ máy Client PC (hoặc mở session Telnet vào IP `192.168.1.1` của Router):
- Màn hình hiện prompt: `User Access Verification` $\rightarrow$ `Username: nhanvien`.
- Nhập Password: `123456`.
- **Kết quả thành công**: Router cấp quyền vào dấu nhắc `TACACS_Client>`.

### 3. Kiểm tra bắt gói tin Wireshark (Validation):
- Chuột phải vào đường link `Fa2/1` nối sang Cloud TACACS $\rightarrow$ Start capture.
- Bộ lọc hiển thị Wireshark: `tacacs`.
- **Kết quả quan sát**:
  1. Thấy các gói tin bắt tay TCP 3 bước cổng 49 (`Destination Port: 49`).
  2. Mọi gói tin mang cờ `TACACS+` đều hiển thị: **`Encrypted: Yes`** (Toàn bộ payload đã được mã hóa an toàn, không lộ mật khẩu).
