# 🏆 CẨM NANG MASTER LAB 3: EXTENDED ACL TRÊN GNS3 & VMWARE WORKSTATION PRO (A - Z)
## Học Phần: An Toàn Mạng & Mật Mã Học Ứng Dụng (`CORP-04-SEC`)
> **Tác giả:** DUT Cyber Security Mentor — CyberDefense & Cryptography Corp  
> **Nền tảng mục tiêu:** GNS3 All-in-One + **VMware Workstation Pro (100% Free for Personal Use)**  
> **Máy chủ khách:** Windows Server 2003 R2 (Import từ `Server 2003 R2.ova`)  
> **Tiêu chuẩn kiểm định:** Đạt 10/10 điểm theo barem đánh giá của Thầy Nguyễn Thế Xuân Ly

---

## 📑 MỤC LỤC
1. [Tại Sao VMware Workstation Vượt Trội Hơn VirtualBox Trong Lab Này](#1-tại-sao-vmware-workstation-vượt-trội-hơn-virtualbox-trong-lab-này)
2. [Sơ Đồ Topo & Bảng Phân Bổ IP / Card Mạng VMnet](#2-sơ-đồ-topo--bảng-phân-bổ-ip--card-mạng-vmnet)
3. [Giai Đoạn 1: Thiết Lập Mạng Ảo Trong VMware Virtual Network Editor](#giai-đoạn-1-thiết-lập-mạng-ảo-trong-vmware-virtual-network-editor)
4. [Giai Đoạn 2: Import & Nhân Bản (Clone) 2 Máy Ảo Server 2003 Trên VMware](#giai-đoạn-2-import--nhân-bản-clone-2-máy-ảo-server-2003-trên-vmware)
5. [Giai Đoạn 3: Tích Hợp VMware Card Vào GNS3 Bằng Node Cloud](#giai-đoạn-3-tích-hợp-vmware-card-vào-gns3-bằng-node-cloud)
6. [Giai Đoạn 4: Cấu Hình Toàn Bộ CLI Cho 3 Router (Gateway, West, East)](#giai-đoạn-4-cấu-hình-toàn-bộ-cli-cho-3-router-gateway-west-east)
7. [Giai Đoạn 5: Cấu Hình IP & Dịch Vụ IIS (Web/FTP) Trên 2 Máy Ảo](#giai-đoạn-5-cấu-hình-ip--dịch-vụ-iis-webftp-trên-2-máy-ảo)
8. [Giai Đoạn 6: Kịch Bản Nghiệm Thu & Kiểm Thử ACL (Đạt Điểm 10/10)](#giai-đoạn-6-kịch-bản-nghiệm-thu--kiểm-thử-acl-đạt-điểm-1010)

---

## 1. TẠI SAO VMWARE WORKSTATION VƯỢT TRỘI HƠN VIRTUALBOX TRONG LAB NÀY

1. **Không bị lỗi Bridge Adapter driver**: VirtualBox trên Windows 10/11 thường bị lỗi không bind được card mạng ảo Host-Only `VBoxNetAdp`, làm rơi rớt gói tin ICMP/FTP ngẫu nhiên.
2. **Quản lý Card mạng ảo đa kênh (Custom VMnet)**: VMware cho phép tạo độc lập `VMnet2` (dành riêng cho LAN 2) và `VMnet3` (dành riêng cho LAN 3) mà không cần can thiệp IP trên Windows Host.
3. **Hiệu năng và Tính tương thích với Windows Server 2003**: VMware SVGA và VMware Tools trên Server 2003 chạy cực kỳ mượt mà, hỗ trợ copy-paste và điều khiển ngầm bằng script mà không bao giờ bị đơ chuột.

---

## 2. SƠ ĐỒ TOPO & BẢNG PHÂN BỔ IP / CARD MẠNG VMNET

### Sơ đồ liên kết mạng:
```
                      ┌─────────────────────────┐
                      │     ROUTER GATEWAY      │
                      │  (Fa0/0: 16.19.16.19)   │
                      └───┬─────────────────┬───┘
            Se1/0: .2     │                 │     Se1/1: .2
     (172.16.3.0/24)      │                 │     (172.16.4.0/24)
            Se1/0: .1     │                 │     Se1/1: .1
        ┌──────────────────┴──┐           ┌──┴──────────────────┐
        │     ROUTER WEST     │           │     ROUTER EAST     │
        │ Loopback0: 10.10.1.1│           │ Loopback0: 10.10.4.1│
        └──────────┬──────────┘           └──────────┬──────────┘
                   │ Fa0/1: 10.10.2.1                │ Fa0/0: 10.10.3.1
                   ▼                                 ▼
            ┌──────────────┐                  ┌──────────────┐
            │ GNS3 Cloud 1 │                  │ GNS3 Cloud 2 │
            │   (VMnet2)   │                  │   (VMnet3)   │
            └──────┬───────┘                  └──────┬───────┘
                   │                                 │
                   ▼                                 ▼
        ┌──────────────────────┐          ┌──────────────────────┐
        │   VM_Server2003_LAN2 │          │   VM_Server2003_LAN3 │
        │    (VMware VMnet2)   │          │    (VMware VMnet3)   │
        │   IP: 10.10.2.10     │          │   IP: 10.10.3.10     │
        │  (Client kiểm thử)   │          │ (IIS Web & FTP Srv)  │
        └──────────────────────┘          └──────────────────────┘
```

### Bảng phân bổ IP và Card mạng ảo:
| Node mạng | Cổng kết nối | Địa chỉ IP / Subnet Mask | Default Gateway | VMware Network Mapping |
|:---|:---|:---|:---|:---|
| **Router Gateway** | `Se1/0`<br>`Se1/1`<br>`Fa0/0` | `172.16.3.2 /24`<br>`172.16.4.2 /24`<br>`16.19.16.19 /24` | -<br>-<br>- | GNS3 Serial<br>GNS3 Serial<br>Loopback (giả lập) |
| **Router West** | `Se1/0`<br>`Fa0/0`<br>`Loopback0` | `172.16.3.1 /24`<br>`10.10.2.1 /24`<br>`10.10.1.1 /24` | -<br>-<br>- | GNS3 Serial<br>Nối vào Cloud 1 (VMnet2)<br>Cổng nội bộ |
| **Router East** | `Se1/1`<br>`Fa0/0`<br>`Loopback0` | `172.16.4.1 /24`<br>`10.10.3.1 /24`<br>`10.10.4.1 /24` | -<br>-<br>- | GNS3 Serial<br>Nối vào Cloud 2 (VMnet3)<br>Cổng nội bộ |
| **Server 2003 LAN2**| `Ethernet0` | `10.10.2.10 /24` | `10.10.2.1` | **Custom: VMnet2** |
| **Server 2003 LAN3**| `Ethernet0` | `10.10.3.10 /24` | `10.10.3.1` | **Custom: VMnet3** |

---

## 3. GIAI ĐOẠN 1: THIẾT LẬP MẠNG ẢO TRONG VMWARE VIRTUAL NETWORK EDITOR

1. Mở **Virtual Network Editor** (chạy quyền Run as Administrator).
2. Nhấn **Change Settings** để cấp quyền quản trị:
   - Chọn **Add Network...** $\rightarrow$ Thêm `VMnet2`.
     - Tích chọn: **Host-only (connect VMs internally in a private network)**.
     - **BỎ TÍCH**: *"Use local DHCP service to distribute IP address to VMs"* (chúng ta sẽ gán IP tĩnh chuẩn theo sơ đồ).
     - Subnet IP: `10.10.2.0`, Subnet mask: `255.255.255.0`.
   - Chọn **Add Network...** $\rightarrow$ Thêm `VMnet3`.
     - Tích chọn: **Host-only**.
     - **BỎ TÍCH**: *"Use local DHCP service..."*.
     - Subnet IP: `10.10.3.0`, Subnet mask: `255.255.255.0`.
3. Bấm **Apply** $\rightarrow$ **OK**.

---

## 4. GIAI ĐOẠN 2: IMPORT & NHÂN BẢN (CLONE) 2 MÁY ẢO SERVER 2003 TRÊN VMWARE

1. Mở **VMware Workstation Pro** $\rightarrow$ `File` $\rightarrow$ `Open...` $\rightarrow$ Chọn `Server 2003 R2.ova`.
   - Đặt tên VM gốc: `Server2003_Base`.
2. Tạo 2 bản sao độc lập (Full Clone hoặc Linked Clone):
   - Chuột phải vào `Server2003_Base` $\rightarrow$ `Manage` $\rightarrow$ `Clone...`.
   - Chọn **Create a linked clone** (nhanh và tiết kiệm ổ cứng).
   - Đặt tên máy 1: `Server2003_LAN2`.
     - Vào `Edit virtual machine settings` $\rightarrow$ Chọn `Network Adapter` $\rightarrow$ Tích chọn: **Custom: Specific virtual network** $\rightarrow$ Chọn **VMnet2**.
   - Nhân bản tiếp máy 2: `Server2003_LAN3`.
     - Vào settings $\rightarrow$ Chọn `Network Adapter` $\rightarrow$ Chọn **Custom: Specific virtual network** $\rightarrow$ Chọn **VMnet3**.

---

## 5. GIAI ĐOẠN 3: TÍCH HỢP VMWARE CARD VÀO GNS3 BẰNG NODE CLOUD

Trong giao diện thiết kế GNS3:
1. Kéo 2 node **Cloud** vào Topology (hoặc dùng sẵn `CLOUD_VMnet2`, `CLOUD_VMnet3` trong file `acl_cloud_vmnet.gns3`):
   - Đặt tên Cloud 1: `CLOUD_VMnet2`.
   - Đặt tên Cloud 2: `CLOUD_VMnet3`.
2. Cấu hình Cloud (Kết nối vào switch mạng ảo VMware):
   - Chuột phải vào `CLOUD_VMnet2` $\rightarrow$ Chọn `Configure` $\rightarrow$ Tab `Ethernet interfaces`:
     - **BẮT BUỘC**: Tích chọn vào ô ☑ **`Show special Ethernet interfaces`** ở góc dưới bên trái (mặc định GNS3 trên Windows sẽ ẩn các card mạng ảo của VMware).
     - Bấm nút **Refresh**.
     - Nhấp vào menu thả xuống (dropdown) $\rightarrow$ Chọn **VMware Network Adapter VMnet2**.
     - Bấm nút **Add** (card sẽ xuất hiện trong danh sách phía dưới).
     - (Tùy chọn) Chọn các card thừa như `Ethernet`, `Ethernet 2`,... rồi bấm **Delete** để xóa bớt cho gọn.
     - Bấm **Apply** $\rightarrow$ **OK**.
   - Chuột phải vào `CLOUD_VMnet3` $\rightarrow$ `Configure`:
     - Tích chọn ☑ **`Show special Ethernet interfaces`** $\rightarrow$ Bấm **Refresh**.
     - Dropdown chọn **VMware Network Adapter VMnet3** $\rightarrow$ Bấm **Add** $\rightarrow$ Apply $\rightarrow$ OK.
3. Cắm dây mạng:
   - Dùng cáp mạng nối từ cổng `Fa0/0` của Router West sang `SW-LAN2`, từ switch nối sang `CLOUD_VMnet2` (cổng `VMware Network Adapter VMnet2`).
   - Dùng cáp mạng nối từ cổng `Fa0/0` của Router East sang `SW-LAN3`, từ switch nối sang `CLOUD_VMnet3` (cổng `VMware Network Adapter VMnet3`).

> ⚠️ **LƯU Ý TRÁNH XUNG ĐỘT IP VỚI ROUTER**:
> Khi VMware tạo VMnet2 (`10.10.2.0/24`) và VMnet3 (`10.10.3.0/24`), Windows Host thường tự động lấy IP `.1` (`10.10.2.1` và `10.10.3.1`). Tuy nhiên, hai IP này chính là IP của Router West (`Fa0/1`) và Router East (`Fa0/0`) đóng vai trò Default Gateway.
> Để tránh xung đột IP (Duplicate IP Address), hãy vào `ncpa.cpl` trên máy thật Windows $\rightarrow$ Chuột phải vào `VMware Network Adapter VMnet2` $\rightarrow$ Properties $\rightarrow$ IPv4 $\rightarrow$ Đổi IP máy thật thành `10.10.2.254` (hoặc bỏ tích `Internet Protocol Version 4`). Tương tự đổi `VMnet3` thành `10.10.3.254`.

---

## 6. GIAI ĐOẠN 4: CẤU HÌNH TOÀN BỘ CLI CHO 3 ROUTER

### 6.1. Cấu hình Router GATEWAY
```cisco
enable
configure terminal
hostname Gateway

interface FastEthernet0/0
 ip address 16.19.16.19 255.255.255.0
 no shutdown
exit

interface Serial1/0
 ip address 172.16.3.2 255.255.255.0
 no shutdown
exit

interface Serial1/1
 ip address 172.16.4.2 255.255.255.0
 no shutdown
exit

router rip
 version 2
 network 16.0.0.0
 network 172.16.0.0
 no auto-summary
exit
end
write memory
```

### 6.2. Cấu hình Router WEST (Chứa Bộ Lọc Extended ACL)
```cisco
enable
configure terminal
hostname West

interface Loopback0
 ip address 10.10.1.1 255.255.255.0
exit

interface FastEthernet0/1
 ip address 10.10.2.1 255.255.255.0
 no shutdown
exit

interface Serial1/0
 ip address 172.16.3.1 255.255.255.0
 no shutdown
exit

router rip
 version 2
 network 10.0.0.0
 network 172.16.0.0
 no auto-summary
exit

! === THIẾT KẾ ACCESS CONTROL LIST EXTENDED BẢO VỆ CHÍNH XÁC ===
ip access-list extended ACL_FILTER_LAN2
 ! 1. Cho phép kết nối điều khiển FTP (Control port 21)
 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp
 ! 2. Cho phép kết nối truyền file dữ liệu FTP (Data port 20)
 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp-data
 ! 3. Cho phép các gói tin TCP phản hồi hợp lệ
 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 established
 ! 4. CHẶN TOÀN BỘ CÁC KẾT NỐI KHÁC GIỮA LAN2 VÀ LAN3 (Chặn Ping ICMP, chặn Web HTTP port 80)
 deny ip 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255
 ! 5. Cho phép mọi kết nối khác ra bên ngoài (LAN1, LAN4, Gateway)
 permit ip any any
exit

! Áp dụng ACL theo chiều đi vào từ LAN2
interface FastEthernet0/1
 ip access-group ACL_FILTER_LAN2 in
exit
end
write memory
```

### 6.3. Cấu hình Router EAST
```cisco
enable
configure terminal
hostname East

interface Loopback0
 ip address 10.10.4.1 255.255.255.0
exit

interface FastEthernet0/0
 ip address 10.10.3.1 255.255.255.0
 no shutdown
exit

interface Serial1/1
 ip address 172.16.4.1 255.255.255.0
 no shutdown
exit

router rip
 version 2
 network 10.0.0.0
 network 172.16.0.0
 no auto-summary
exit
end
write memory
```

---

## 7. GIAI ĐOẠN 5: CẤU HÌNH IP & DỊCH VỤ IIS (WEB/FTP) TRÊN 2 MÁY ẢO

### Máy 1: `Server2003_LAN2` (Client Kiểm Thử)
1. Bật máy ảo trên VMware. Đăng nhập: `Administrator` / `123qwe!@#`.
2. Mở `Control Panel` $\rightarrow$ `Network Connections` $\rightarrow$ `Local Area Connection` $\rightarrow$ `Properties` $\rightarrow$ `Internet Protocol (TCP/IP)`:
   - IP address: `10.10.2.10`
   - Subnet mask: `255.255.255.0`
   - Default gateway: `10.10.2.1`
3. Mở CMD gõ: `ping 10.10.2.1` $\rightarrow$ Phải nhận được Reply thành công từ Router West!

### Máy 2: `Server2003_LAN3` (Server Cung Cấp Web & FTP)
1. Đăng nhập vào máy ảo LAN3.
2. Cấu hình IP tĩnh:
   - IP address: `10.10.3.10`
   - Subnet mask: `255.255.255.0`
   - Default gateway: `10.10.3.1`
3. Mở `Windows Firewall`: Tắt Firewall (hoặc chọn `Off`) để không chặn cổng IIS.
4. Kiểm tra dịch vụ IIS:
   - Mở `Administrative Tools` $\rightarrow$ `Internet Information Services (IIS) Manager`:
   - Kiểm tra **Default Web Site** đang ở trạng thái `Running` (Port 80).
   - Kiểm tra **Default FTP Site** đang ở trạng thái `Running` (Port 21). Tạo sẵn 1 file văn bản test: `C:\Inetpub\ftproot\test_dut.txt`.

---

## 8. GIAI ĐOẠN 6: KỊCH BẢN NGHIỆM THU & KIỂM THỬ ACL (ĐẠT ĐIỂM 10/10)

Đứng từ máy ảo **`Server2003_LAN2`** mở CMD và thực hiện 4 bước nghiệm thu:

### 1. Kiểm tra Chặn PING (ICMP) $\rightarrow$ PHẢI THẤT BẠI:
```cmd
ping 10.10.3.10
```
- **Kết quả mong đợi**: `Destination host unreachable` hoặc `Request timed out`.
- **Minh chứng**: Khớp với luật `deny ip 10.10.2.0 ... 10.10.3.0`.

### 2. Kiểm tra Chặn WEB (HTTP) $\rightarrow$ PHẢI THẤT BẠI:
- Mở trình duyệt Internet Explorer trên máy LAN2, gõ địa chỉ: `http://10.10.3.10`
- **Kết quả mong đợi**: Trình duyệt báo `The page cannot be displayed` (Connection timed out).

### 3. Kiểm tra Cho phép TRUYỀN FILE (FTP) $\rightarrow$ PHẢI THÀNH CÔNG RỰC RỠ:
```cmd
ftp 10.10.3.10
```
- **Kết quả mong đợi**: Xuất hiện lời chào: `Connected to 10.10.3.10. 220 Microsoft FTP Service`.
- Nhập User: `Administrator`, Password: `123qwe!@#` $\rightarrow$ Báo `230 User Administrator logged in`.
- Gõ lệnh tải file:
  ```cmd
  dir
  get test_dut.txt
  quit
  ```
- **Kết quả mong đợi**: Lệnh `dir` liệt kê danh sách file, lệnh `get` tải file về thành công!

### 4. Kiểm tra Counter trên Router West:
Trên console Router West gõ:
```cisco
West# show access-lists
```
- Sẽ thấy số lượng gói tin đếm (matches) tăng vọt trên các dòng `permit tcp ... eq ftp` và `deny ip ...`!
