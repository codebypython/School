# 🏆 [ARCHIVE/LEGACY] CẨM NANG MASTER LAB 3: EXTENDED ACL TRÊN GNS3 & VIRTUALBOX
> ⚠️ **THÔNG BÁO CHUYỂN GIAO CÔNG NGHỆ:** Học phần đã chuyển dịch 100% sang hệ sinh thái **VMware Workstation Pro**. Vui lòng sử dụng cẩm nang chính thức mới nhất tại: 👉 **[LAB3_VMWARE_GNS3_MASTER_GUIDE.md](LAB3_VMWARE_GNS3_MASTER_GUIDE.md)**. Tài liệu dưới đây chỉ lưu trữ cho mục đích tham khảo lịch sử.

---

## 📑 MỤC LỤC
1. [Phân Tích & Khắc Phục Các Sai Lầm Của 2 Bản Hướng Dẫn Trước](#1-phân-tích--khắc-phục-các-sai-lầm-của-2-bản-hướng-dẫn-trước)
2. [Sơ Đồ Topo & Bảng Phân Bổ IP Chuẩn Hoá](#2-sơ-đồ-topo--bảng-phân-bổ-ip-chuẩn-hoá)
3. [Giai Đoạn 1: Chuẩn Bị & Cấu Hình 2 Máy Ảo Trên Oracle VirtualBox](#giai-đoạn-1-chuẩn-bị--cấu-hình-2-máy-ảo-trên-oracle-virtualbox)
4. [Giai Đoạn 2: Tích Hợp VirtualBox Vào GNS3 & Cắm Dây Topo](#giai-đoạn-2-tích-hợp-virtualbox-vào-gns3--cắm-dây-topo)
5. [Giai Đoạn 3: Cấu Hình Toàn Bộ CLI Cho 3 Router (Gateway, East, West)](#giai-đoạn-3-cấu-hình-toàn-bộ-cli-cho-3-router-gateway-east-west)
6. [Giai Đoạn 4: Cấu Hình IP, Tắt Firewall & Bật Dịch Vụ IIS Trên 2 Máy Ảo](#giai-đoạn-4-cấu-hình-ip-tắt-firewall--bật-dịch-vụ-iis-trên-2-máy-ảo)
7. [Giai Đoạn 5: Quy Trình Kiểm Thử Nghiệm Thu & Chụp Ảnh Báo Cáo 10/10](#giai-đoạn-5-quy-trình-kiểm-thử-nghiệm-thu--chụp-ảnh-báo-cáo-1010)
8. [⚠️ Lỗi Phổ Biến Sinh Viên Hay Gặp](#️-lỗi-phổ-biến-sinh-viên-hay-gặp)
9. [💡 Micro-Quiz / Câu Hỏi Phản Biện](#-micro-quiz--câu-hỏi-phản-biện)

---

## 1. PHÂN TÍCH & KHẮC PHỤC CÁC SAI LẦM CỦA 2 BẢN HƯỚNG DẪN TRƯỚC

Sau khi thẩm định chéo 2 tài liệu của sinh viên:
- **Bản `Lab3_tut2.md`**: Điểm mạnh là bám sát VirtualBox, nhưng **cắm thẳng Router vào máy ảo mà không qua Switch** (khác sơ đồ đề bài), và **chỉ đặt ACL trên Router West mà bỏ quên Router East** (khiến luồng từ LAN3 sang LAN2 không được kiểm soát đồng bộ).
- **Bản `lab3_tut.md`**: Điểm mạnh là có đầy đủ 4 switch và loopback, nhưng **lại áp dụng cho VMware** và mắc **lỗi logic nghiêm trọng trong ACL**: Đặt luật có source IP `10.10.3.0` vào cổng `FastEthernet0/1 in` trên West — các gói tin này đến từ Serial nên dòng luật đó **không bao giờ khớp (0 matches)**!

👉 **Bản Master Guide dưới đây kết hợp tinh hoa của cả hai, sửa sạch toàn bộ lỗi logic và tối ưu 100% cho hệ thống GNS3 + VirtualBox của bạn.**

---

## 2. SƠ ĐỒ TOPO & BẢNG PHÂN BỔ IP CHUẨN HOÁ

### Sơ đồ liên kết (Topology Diagram):
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
           │   SW-LAN2    │                  │   SW-LAN3    │
           └──────┬───────┘                  └──────┬───────┘
                  │                                 │
                  ▼                                 ▼
       ┌──────────────────────┐          ┌──────────────────────┐
       │       VM LAN2        │          │       VM LAN3        │
       │ (Windows Server 2003)│          │ (Windows Server 2003)│
       │   IP: 10.10.2.10     │          │   IP: 10.10.3.10     │
       │ (Client kiểm thử)    │          │ (IIS Web & FTP Srv)  │
       └──────────────────────┘          └──────────────────────┘
```

### Bảng Phân Bổ Địa Chỉ IP Chi Tiết:
| Thiết bị | Cổng giao tiếp | Địa chỉ IP / CIDR | Subnet Mask | Vai trò kết nối |
| :--- | :--- | :--- | :--- | :--- |
| **Gateway** | `Fa0/0` | `16.19.16.19/24` | `255.255.255.0` | Cổng nối ra ngoài Internet (giả lập) |
| **Gateway** | `Se1/0` | `172.16.3.2/24` | `255.255.255.0` | Nối với Router West `Se1/0` |
| **Gateway** | `Se1/1` | `172.16.4.2/24` | `255.255.255.0` | Nối với Router East `Se1/1` |
| **West** | `Se1/0` | `172.16.3.1/24` | `255.255.255.0` | Nối với Gateway `Se1/0` |
| **West** | `Loopback0` | `10.10.1.1/24` | `255.255.255.0` | Giả lập phân vùng **LAN 1** |
| **West** | `Fa0/1` | `10.10.2.1/24` | `255.255.255.0` | Default Gateway cho **LAN 2** |
| **East** | `Se1/1` | `172.16.4.1/24` | `255.255.255.0` | Nối với Gateway `Se1/1` |
| **East** | `Loopback0` | `10.10.4.1/24` | `255.255.255.0` | Giả lập phân vùng **LAN 4** |
| **East** | `Fa0/0` | `10.10.3.1/24` | `255.255.255.0` | Default Gateway cho **LAN 3** |
| **VM LAN2** | `Ethernet0` | `10.10.2.10/24` | `255.255.255.0` | Máy trạm đóng vai trò Client thử nghiệm |
| **VM LAN3** | `Ethernet0` | `10.10.3.10/24` | `255.255.255.0` | Máy chủ chạy dịch vụ IIS (Web & FTP) |

---

## GIAI ĐOẠN 1: CHUẨN BỊ & CẤU HÌNH 2 MÁY ẢO TRÊN ORACLE VIRTUALBOX

1. **Import máy ảo gốc**:
   - Mở **Oracle VirtualBox** $\rightarrow$ `File` $\rightarrow$ `Import Appliance...` $\rightarrow$ Chọn file máy ảo Windows Server 2003 (nếu yêu cầu Product Key: `HDXR2-62748-6XG6Y-4BT6T-R6H43`).
   - Đổi tên máy vừa import thành: **`LAN2`**.
2. **Nhân bản thành máy `LAN3` (Bắt buộc Full Clone)**:
   - Chuột phải vào máy `LAN2` $\rightarrow$ Chọn **Clone...**:
     - *Name*: Đặt tên là **`LAN3`**.
     - *MAC Address Policy*: Chọn **Generate new MAC addresses for all network adapters** (để tránh trùng địa chỉ MAC).
     - *Clone type*: Chọn **Full clone** $\rightarrow$ Bấm **Clone**.
3. **Cấu hình Card Mạng cô lập (Để GNS3 toàn quyền quản lý)**:
   - Chọn máy `LAN2` $\rightarrow$ Bấm **Settings** $\rightarrow$ Tab **Network** $\rightarrow$ **Adapter 1**:
     - Tại dòng *Attached to*: Chọn **Not attached**.
     - Bấm **OK**.
   - Thực hiện tương tự cho máy `LAN3`: Đổi **Adapter 1** thành **Not attached** $\rightarrow$ Bấm **OK**.
   > *Xác nhận:* Cả 2 máy `LAN2` và `LAN3` đều ở trạng thái *Powered Off* và *Adapter 1: Not attached*.

---

## GIAI ĐOẠN 2: TÍCH HỢP VIRTUALBOX VÀO GNS3 & CẮM DÂY TOPO

### 1. Đăng ký 2 máy ảo vào GNS3
1. Mở GNS3 $\rightarrow$ Tạo Project mới (ví dụ: `Lab3_ACL_VirtualBox`).
2. Vào menu `Edit` $\rightarrow$ `Preferences...` $\rightarrow$ Chọn mục **VirtualBox VMs** ở danh sách bên trái.
3. Thêm máy `LAN2`:
   - Bấm **New** $\rightarrow$ Chọn VM: **`LAN2`** $\rightarrow$ Bấm **Finish**.
   - Chọn máy `LAN2` vừa thêm $\rightarrow$ Bấm **Edit** $\rightarrow$ Chuyển sang tab **Network** $\rightarrow$ **TÍCH CHỌN**:  
     ☑ **Allow GNS3 to use any configured VirtualBox adapter** $\rightarrow$ Bấm **OK**.
4. Thêm máy `LAN3`:
   - Bấm **New** $\rightarrow$ Chọn VM: **`LAN3`** $\rightarrow$ Bấm **Finish**.
   - Bấm **Edit** $\rightarrow$ Tab **Network** $\rightarrow$ **TÍCH CHỌN**:  
     ☑ **Allow GNS3 to use any configured VirtualBox adapter** $\rightarrow$ Bấm **OK**.
5. Bấm **Apply** $\rightarrow$ **OK** để lưu lại.

### 2. Thiết lập phần cứng Slot cho Router Cisco 3725
Để Router có đầy đủ cổng Serial và FastEthernet:
1. Vào `Edit` $\rightarrow$ `Preferences` $\rightarrow$ `Dynamips` $\rightarrow$ `IOS routers` $\rightarrow$ Chọn Router `c3725` $\rightarrow$ Bấm **Edit**.
2. Tab **Slots**:
   - `slot 0`: `GT96100-FE` (2 cổng FastEthernet: Fa0/0, Fa0/1).
   - `slot 1`: `NM-4T` (4 cổng Serial: Se1/0, Se1/1, Se1/2, Se1/3).
3. Bấm **OK**.

### 3. Kéo thiết bị ra màn hình và nối dây chuẩn
1. Kéo ra bảng làm việc:
   - 3 Router c3725: Đặt tên `Gateway`, `West`, `East`.
   - 2 Ethernet Switch: Đặt tên `SW-LAN2`, `SW-LAN3`.
   - 2 VirtualBox VMs: Kéo `LAN2` và `LAN3` ra.
2. Dùng công cụ cáp nối theo đúng bảng sau:

| Thiết bị A | Cổng A | Thiết bị B | Cổng B | Loại cáp |
| :--- | :--- | :--- | :--- | :--- |
| **West** | `Serial1/0` | **Gateway** | `Serial1/0` | Cáp Serial |
| **East** | `Serial1/1` | **Gateway** | `Serial1/1` | Cáp Serial |
| **West** | `FastEthernet0/1` | **SW-LAN2** | Cổng bất kỳ (Port 0) | Cáp Ethernet |
| **SW-LAN2** | Cổng bất kỳ (Port 1) | **LAN2** (VirtualBox) | `Ethernet0` | Cáp Ethernet |
| **East** | `FastEthernet0/0` | **SW-LAN3** | Cổng bất kỳ (Port 0) | Cáp Ethernet |
| **SW-LAN3** | Cổng bất kỳ (Port 1) | **LAN3** (VirtualBox) | `Ethernet0` | Cáp Ethernet |

3. Bấm nút **Start (▶)** màu xanh lá trên thanh công cụ GNS3 để khởi động toàn bộ Router và máy ảo.

---

## GIAI ĐOẠN 3: CẤU HÌNH TOÀN BỘ CLI CHO 3 ROUTER (GATEWAY, EAST, WEST)

Mở Console của từng Router trên GNS3 và copy-paste chính xác các khối lệnh sau:

### 1. Router Gateway
```cisco
enable
configure terminal
hostname Gateway

! Cấu hình cổng WAN nối với Router West
interface Serial1/0
 ip address 172.16.3.2 255.255.255.0
 clock rate 64000
 no shutdown
exit

! Cấu hình cổng WAN nối với Router East
interface Serial1/1
 ip address 172.16.4.2 255.255.255.0
 clock rate 64000
 no shutdown
exit

! Cấu hình cổng giả lập Internet
interface FastEthernet0/0
 ip address 16.19.16.19 255.255.255.0
 no shutdown
exit

! Định tuyến RIPv2 quảng bá các mạng WAN và Internet
router rip
 version 2
 no auto-summary
 network 172.16.0.0
 network 16.0.0.0
 passive-interface FastEthernet0/0
exit

end
write memory
```

---

### 2. Router East
```cisco
enable
configure terminal
hostname East

! Cấu hình cổng Serial nối về Gateway
interface Serial1/1
 ip address 172.16.4.1 255.255.255.0
 no shutdown
exit

! Cấu hình cổng FastEthernet nối xuống LAN 3
interface FastEthernet0/0
 ip address 10.10.3.1 255.255.255.0
 no shutdown
exit

! Cấu hình Loopback đại diện cho LAN 4
interface Loopback0
 ip address 10.10.4.1 255.255.255.0
 no shutdown
exit

! Định tuyến RIPv2
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 172.16.0.0
exit

! --- EXTENDED ACL LỌC LƯU LƯỢNG TỪ LAN 3 SANG LAN 2 ---
no ip access-list extended ACL_FILTER_LAN3
ip access-list extended ACL_FILTER_LAN3
 ! Cho phép kênh FTP Control (Port 21)
 permit tcp 10.10.3.0 0.0.0.255 10.10.2.0 0.0.0.255 eq 21
 ! Cho phép kênh Active FTP Data (Port 20)
 permit tcp 10.10.3.0 0.0.0.255 10.10.2.0 0.0.0.255 eq 20
 ! Cho phép phiên TCP phản hồi hợp lệ
 permit tcp 10.10.3.0 0.0.0.255 10.10.2.0 0.0.0.255 established
 ! Chặn tuyệt đối Ping và Web sang LAN 2
 deny ip 10.10.3.0 0.0.0.255 10.10.2.0 0.0.0.255
 ! Cho phép mọi lưu lượng khác
 permit ip any any
exit

! Áp dụng ACL theo chiều đi vào từ LAN 3
interface FastEthernet0/0
 ip access-group ACL_FILTER_LAN3 in
exit

end
write memory
```

---

### 3. Router West
```cisco
enable
configure terminal
hostname West

! Cấu hình cổng Serial nối về Gateway
interface Serial1/0
 ip address 172.16.3.1 255.255.255.0
 no shutdown
exit

! Cấu hình cổng FastEthernet nối xuống LAN 2
interface FastEthernet0/1
 ip address 10.10.2.1 255.255.255.0
 no shutdown
exit

! Cấu hình Loopback đại diện cho LAN 1
interface Loopback0
 ip address 10.10.1.1 255.255.255.0
 no shutdown
exit

! Định tuyến RIPv2
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 172.16.0.0
exit

! --- EXTENDED ACL LỌC LƯU LƯỢNG TỪ LAN 2 SANG LAN 3 ---
no ip access-list extended ACL_FILTER_LAN2
ip access-list extended ACL_FILTER_LAN2
 ! 1. Cho phép kênh điều khiển FTP (Port 21)
 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq 21
 ! 2. Cho phép kênh dữ liệu Active FTP Data (Port 20)
 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq 20
 ! 3. Cho phép kênh dữ liệu Passive FTP (Port cao > 1023)
 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 gt 1023
 ! 4. Cho phép các gói tin phản hồi TCP hợp lệ
 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 established
 ! 5. Chặn toàn bộ kết nối khác sang LAN 3 (Ping ICMP, Web HTTP Port 80)
 deny ip 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255
 ! 6. Cho phép toàn bộ kết nối ra bên ngoài (LAN 1, LAN 4, Internet)
 permit ip any any
exit

! Áp dụng ACL theo chiều đi vào từ LAN 2
interface FastEthernet0/1
 ip access-group ACL_FILTER_LAN2 in
exit

end
write memory
```

---

## GIAI ĐOẠN 4: CẤU HÌNH IP, TẮT FIREWALL & BẬT DỊCH VỤ IIS TRÊN 2 MÁY ẢO

Đăng nhập vào màn hình VirtualBox của từng máy (Vào menu VirtualBox: `Input` $\rightarrow$ `Keyboard` $\rightarrow$ `Insert Ctrl-Alt-Del` $\rightarrow$ Mật khẩu: `123qwe!@#` hoặc để trống):

### 1. Trên Máy Ảo `LAN2` (Client Kiểm Thử)
1. **Tắt Windows Firewall** *(BẮT BUỘC, nếu không máy sẽ chặn ICMP Ping)*:
   - Vào `Start` $\rightarrow$ `Control Panel` $\rightarrow$ `Windows Firewall`.
   - Chọn **Off (not recommended)** $\rightarrow$ Bấm **OK**.
2. **Đặt IP tĩnh**:
   - `Start` $\rightarrow$ `Control Panel` $\rightarrow$ `Network Connections`.
   - Chuột phải `Local Area Connection` $\rightarrow$ `Properties` $\rightarrow$ Nhấp đúp `Internet Protocol (TCP/IP)`.
   - Điền thông số:
     - **IP address**: `10.10.2.10`
     - **Subnet mask**: `255.255.255.0`
     - **Default gateway**: `10.10.2.1`
   - Bấm **OK** $\rightarrow$ **Close**.

---

### 2. Trên Máy Ảo `LAN3` (Server IIS Web & FTP)
1. **Tắt Windows Firewall**:
   - Vào `Start` $\rightarrow$ `Control Panel` $\rightarrow$ `Windows Firewall` $\rightarrow$ Chọn **Off** $\rightarrow$ Bấm **OK**.
2. **Đặt IP tĩnh**:
   - `Start` $\rightarrow$ `Control Panel` $\rightarrow$ `Network Connections` $\rightarrow$ `Local Area Connection` $\rightarrow$ `Properties` $\rightarrow$ `TCP/IP`.
   - Điền thông số:
     - **IP address**: `10.10.3.10`
     - **Subnet mask**: `255.255.255.0`
     - **Default gateway**: `10.10.3.1`
   - Bấm **OK** $\rightarrow$ **Close**.
3. **Kiểm tra và Khởi động Dịch vụ IIS (Web & FTP)**:
   - Mở `Start` $\rightarrow$ `Administrative Tools` $\rightarrow$ `Internet Information Services (IIS) Manager`.
   - Bung cây thư mục máy chủ:
     - Kiểm tra **Web Sites** $\rightarrow$ `Default Web Site`: Đảm bảo trạng thái là **Running** (cổng 80).
     - Kiểm tra **FTP Sites** $\rightarrow$ `Default FTP Site`: Đảm bảo trạng thái là **Running** (cổng 21).
4. **Tạo file mẫu để test tải FTP**:
   - Mở `My Computer` $\rightarrow$ Ổ đĩa `C:\` $\rightarrow$ Vào thư mục `Inetpub` $\rightarrow$ `ftproot`.
   - Chuột phải tạo file văn bản mới: `lab3_test.txt` (bên trong gõ nội dung: *"Lab 3 Extended ACL Thanh Cong 100%"*).
5. **Bật quyền truy cập Anonymous cho FTP**:
   - Trong IIS Manager, chuột phải vào `Default FTP Site` $\rightarrow$ `Properties` $\rightarrow$ Tab **Security Accounts**.
   - Tích chọn ô: **Allow anonymous connections** (Username: `anonymous`).
   - Bấm **OK**.

---

## GIAI ĐOẠN 5: QUY TRÌNH KIỂM THỬ NGHIỆM THU & CHỤP ẢNH BÁO CÁO 10/10

Thực hiện toàn bộ các bước kiểm tra sau trực tiếp từ cửa sổ **CMD của máy LAN2 (`10.10.2.10`)**:

### Test 1: Kiểm tra thông tuyến nội bộ và các mạng ngoài (Yêu cầu: Thành công)
```cmd
ping 10.10.2.1
:: Kết quả: Reply from 10.10.2.1: bytes=32 time<1ms TTL=255 (Thông Gateway West)

ping 10.10.1.1
:: Kết quả: Reply from 10.10.1.1: bytes=32 time<1ms TTL=255 (Thông Loopback LAN 1)

ping 10.10.4.1
:: Kết quả: Reply from 10.10.4.1: bytes=32 time=15ms TTL=254 (Thông Loopback LAN 4)

ping 16.19.16.19
:: Kết quả: Reply from 16.19.16.19: bytes=32 time=10ms TTL=254 (Thông Internet Gateway)
```
> ✅ **Chứng minh:** Lệnh `permit ip any any` ở cuối ACL hoạt động chính xác, không chặn nhầm các dải mạng hợp lệ.

---

### Test 2: Kiểm tra Ping sang Server LAN3 (Yêu cầu: Bị chặn hoàn toàn)
```cmd
ping 10.10.3.10
```
- **Kết quả hiển thị trên màn hình**:
  ```text
  Pinging 10.10.3.10 with 32 bytes of data:
  Reply from 10.10.2.1: Destination host unreachable.
  Request timed out.
  ```
> ✅ **Chứng minh:** Gói tin ICMP Echo Request đã bị bắt và loại bỏ bởi dòng lệnh `deny ip 10.10.2.0 ... 10.10.3.0 ...` trên Router West!

---

### Test 3: Kiểm tra Truy Cập Web HTTP sang Server LAN3 (Yêu cầu: Bị chặn hoàn toàn)
1. Mở trình duyệt **Internet Explorer** trên máy `LAN2`.
2. Gõ địa chỉ: `http://10.10.3.10` rồi nhấn **Enter**.
- **Kết quả hiển thị**:
  Trình duyệt báo lỗi: *"The page cannot be displayed"* hoặc *"Internet Explorer cannot display the webpage"*.
> ✅ **Chứng minh:** Cổng TCP 80 bị chặn triệt để, không thể thiết lập bắt tay 3 bước HTTP.

---

### Test 4: Kiểm tra Truyền File FTP sang Server LAN3 (Yêu cầu: Cho phép thông suốt)
Mở lại cửa sổ CMD trên máy `LAN2` và gõ từng dòng:

```cmd
C:\> ftp 10.10.3.10
Connected to 10.10.3.10.
220 Microsoft FTP Service
User (10.10.3.10:(none)): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: [Nhấn Enter]
230 Anonymous user logged in.

ftp> dir
200 PORT command successful.
150 Opening ASCII mode data connection for /bin/ls.
-rwxr-xr-x   1 owner    group         38 Sep 17 05:00 lab3_test.txt
226 Transfer complete.

ftp> get lab3_test.txt
200 PORT command successful.
150 Opening BINARY mode data connection.
226 Transfer complete.
ftp: 38 bytes received in 0.01Seconds.

ftp> bye
221 Goodbye.

C:\> type lab3_test.txt
Lab 3 Extended ACL Thanh Cong 100%
```
> ✅ **Chứng minh:** Kênh điều khiển Port 21 và kênh dữ liệu Port 20 truyền tải hoàn hảo, file mẫu tải về máy client nguyên vẹn!

---

### Test 5: Chụp ảnh bộ đếm gói tin ACL trên Router West (Bằng chứng thép)
Vào Console của **Router West**, gõ lệnh:
```cisco
show ip access-lists ACL_FILTER_LAN2
```
**Kết quả hiển thị minh chứng điểm 10**:
```text
Extended IP access list ACL_FILTER_LAN2
    10 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp (42 matches)
    20 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp-data (16 matches)
    30 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 gt 1023
    40 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 established (85 matches)
    50 deny ip 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 (28 matches)
    60 permit ip any any (104 matches)
```
*(Số lượng `matches` tăng lên ở dòng deny chứng minh đã chặn Ping/Web, số matches ở dòng permit chứng minh đã cho qua FTP).*

---

## ⚠️ LỖI PHỔ BIẾN SINH VIÊN HAY GẶP

1. **Quên tích "Allow GNS3 to use any configured VirtualBox adapter"**:
   - Khi cắm dây cáp từ Switch vào máy ảo VirtualBox, GNS3 báo lỗi `Adapter 0 is not available`. Hãy vào `Edit` $\rightarrow$ `Preferences` $\rightarrow$ `VirtualBox VMs` $\rightarrow$ `Edit` máy ảo $\rightarrow$ Tab `Network` $\rightarrow$ Tích chọn ô này.
2. **Quên tắt Windows Firewall trên máy ảo Windows Server 2003**:
   - Sau khi cấu hình ACL xong, ping không được mà FTP cũng không được. Lý do không phải tại Router mà do Firewall tích hợp của chính Windows Server 2003 chặn mọi kết nối vào. Luôn tắt Firewall trước khi test lab.
3. **Lỗi treo khi gõ lệnh `dir` trong FTP**:
   - Xảy ra khi chỉ mở cổng 21 (`eq ftp`) mà quên cổng 20 (`eq ftp-data`) hoặc dòng `established`. Bản cấu hình trên của chúng ta đã bao phủ trọn vẹn cả 3 dòng này.

---

## 💡 MICRO-QUIZ / CÂU HỎI PHẢN BIỆN

> **Câu hỏi:**  
> Tại sao trong bản hướng dẫn Master này, chúng ta áp dụng Access Control List trên Router West ở cổng `FastEthernet0/1` theo chiều **`in`** chứ KHÔNG đặt ở cổng `Serial1/0` theo chiều **`out`**? Việc đặt ACL tại cổng `in` gần nguồn phát lưu lượng mang lại lợi ích gì về mặt hiệu năng và bảo vệ băng thông đường truyền WAN?
