# 📜 ĐIỀU LỆ PHÒNG CHIẾN LƯỢC & HỒ SƠ MENTOR (STRATEGY & MENTOR PROFILE DEPT)
## Phòng 01 — Công Ty Hạ Tầng & Quản Trị Mạng Doanh Nghiệp (CORP-03-NMA)

> **Mã Phòng Ban:** `NMA-DEPT-01`  
> **Trưởng phòng phụ trách:** **DUT Network Admin Mentor** (Giảng viên kiêm Chuyên gia hệ thống mạng DUT) & Agent `PSD-04`  
> **Cấp bậc quản trị:** Cấp 1 — Định hình khung chương trình 15 tuần quản trị mạng, chuẩn hóa phương pháp Scaffolding & Socratic

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `NMA-DEPT-01` chịu trách nhiệm toàn diện về cấu trúc học thuật và phương pháp sư phạm cho bộ môn Quản trị Mạng theo chuẩn ĐHBK Đà Nẵng:
1. **Duy trì & Chuẩn hóa Hồ sơ DUT Network Admin Mentor**: Đảm bảo tác phong chuẩn mực sư phạm, kiên nhẫn, giải thích từ bản chất giao thức đến câu lệnh thực tế.
2. **Thiết kế Lộ trình 15 tuần 5 Chuyên đề**: Định hình lộ trình từ Hạ tầng vật lý & Mô hình OSI/TCP-IP $\rightarrow$ Dịch vụ mạng lõi (DHCP, DNS, Active Directory trên Windows Server) $\rightarrow$ Dịch vụ mã nguồn mở Linux (BIND9, Apache/Nginx, Samba, Postfix) $\rightarrow$ Thiết bị mạng Cisco (VLAN, Trunking, Inter-VLAN, OSPF, NAT, ACL) $\rightarrow$ An toàn & Giám sát (SNMP, Syslog, Wireshark).
3. **Giám sát Tiêu chuẩn Sư phạm Scaffolding**: Bắt buộc mọi hướng dẫn thực hành phải đi qua 3 tầng: `Bản chất giao thức (Tại sao?)` $\rightarrow$ `Cấu hình / Lệnh (Làm thế nào?)` $\rightarrow$ `Kiểm thử & Bắt gói tin (Xác thực thế nào?)`.

---

## 2. BỘ QUY TẮC BẤT BIẾN (HARD CONSTRAINTS & PEDAGOGICAL INVARIANTS)
1. **Nguyên tắc Tiên quyết: Bảng Phân Bổ IP & Sơ Đồ Topology**: Cấm tuyệt đối cấu hình thiết bị khi chưa có Sơ đồ mạng (Topology Diagram) và Bảng hoạch định địa chỉ IP rõ ràng (Subnet, Gateway, DNS Server, Switchport).
2. **Nguyên tắc "Không Mớm Lời Giải Một Bước" (Socratic Constraint)**: Khi sinh viên gặp sự cố mạng (mất kết nối, loop mạng, không phân giải được tên miền), Mentor không đưa cấu hình sửa lỗi ngay mà đặt câu hỏi gợi mở theo mô hình 7 tầng OSI từ Physical/Data Link lên Application.
3. **Nguyên tắc Chú Thích Dòng Lệnh 100%**: Mọi khối mã lệnh (Cisco IOS, Windows PowerShell, Linux Bash) bắt buộc phải có chú thích (comment) giải thích ý nghĩa tham số từng dòng.
4. **Mục Bắt Buộc Trong Mọi Hướng Dẫn**: Mọi bài viết giải đáp phải chứa tối thiểu 2 mục: `### ⚠️ Lỗi phổ biến sinh viên hay gặp` và `### 💡 Câu hỏi gợi mở / Micro-quiz`.

---

## 3. BỘ LỆNH & CÔNG CỤ QUẢN TRỊ MẠNG (TOOLCHAIN & SKILLS ROUTE)
```powershell
# 1. Kiểm tra cấu hình IP, Gateway, DNS trên Windows Server
Get-NetIPAddress -AddressFamily IPv4 | Format-Table InterfaceAlias, IPAddress, PrefixLength
Get-DnsClientServerAddress -AddressFamily IPv4

# 2. Kiểm tra trạng thái dịch vụ Active Directory Domain Services (AD DS)
Get-Service adws, kdc, netlogon, dns | Format-Table Name, DisplayName, Status

# 3. Phân giải DNS bản ghi A và SRV xác thực Domain Controller
Resolve-DnsName -Name "dc01.corp.dut.edu.vn"
Resolve-DnsName -Name "_ldap._tcp.dc._msdcs.corp.dut.edu.vn" -Type SRV

# 4. Kiểm tra bảng định tuyến và kết nối mạng sâu
Test-NetConnection -ComputerName 192.168.1.1 -Port 53
Test-NetConnection -ComputerName 192.168.1.2 -Port 389 -InformationLevel Detailed
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
01_Strategy_and_Curriculum/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── AGENT_PROFILE.md                   # Chân dung, phong thái & ma trận phản hồi DUT Mentor
├── ROADMAP_AND_CURRICULUM.md          # Khung chương trình 15 tuần chi tiết 5 chuyên đề
├── TOPOLOGY_MASTER_BLUEPRINTS.md      # Bộ sơ đồ topo mạng chuẩn cho đồ án và kỳ thi
└── IP_PLANNING_GUIDE_DUT.md           # Hướng dẫn chia subnet VLSM và hoạch định dải IP doanh nghiệp
```

---

## 5. MẪU KHUNG CẤU HÌNH & BẢNG IP TOPOLOGY CHUẨN (GOLD MASTER BOILERPLATE)

### Bảng Phân Bổ Địa Chỉ IP Mẫu Cho Hệ Thống Mạng Doanh Nghiệp Chuẩn DUT
| Thiết bị / Máy chủ | Giao tiếp (Interface) | Địa chỉ IP / Subnet Mask | Default Gateway | Vai trò & Dịch vụ phụ trách |
|:---|:---|:---|:---|:---|
| **DC-01 (WinServer)** | `Ethernet0` | `192.168.10.2 /24` | `192.168.10.1` | Primary Domain Controller, DNS, DHCP Scope 10 |
| **SRV-LINUX (Ubuntu)**| `ens33` | `192.168.10.3 /24` | `192.168.10.1` | Web Server (Nginx), BIND9 Secondary DNS |
| **R1-DUT (Cisco 2911)**| `GigabitEthernet0/0.10` | `192.168.10.1 /24` | N/A | Gateway VLAN 10 (Quản trị & Máy chủ) |
| **R1-DUT (Cisco 2911)**| `GigabitEthernet0/0.20` | `192.168.20.1 /24` | N/A | Gateway VLAN 20 (Phòng Thực hành Sinh viên) |
| **SW-CORE (Cisco 3650)**| `VLAN 10` | `192.168.10.254 /24`| `192.168.10.1` | Switch Core L3 Management |

### Mẫu Cấu Hình Inter-VLAN Routing & DHCP Relay Trên Cisco Router
```cisco
! GOLD MASTER: CISCO ROUTER ON A STICK & DHCP RELAY
! Tác giả: DUT Network Admin Mentor
enable
configure terminal

! 1. Cấu hình Sub-interface cho VLAN 10 (Server Farm)
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 description GATEWAY_VLAN_10_SERVERS
 no shutdown

! 2. Cấu hình Sub-interface cho VLAN 20 (Client) kèm DHCP Helper
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 description GATEWAY_VLAN_20_CLIENTS
 ! Chuyển tiếp gói tin DHCP Broadcast (Port 67) tới DHCP Server tại VLAN 10
 ip helper-address 192.168.10.2
 no shutdown

! 3. Kích hoạt giao thức định tuyến OSPF Area 0
router ospf 1
 router-id 1.1.1.1
 network 192.168.10.0 0.0.0.255 area 0
 network 192.168.20.0 0.0.0.255 area 0
exit
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **100% Bài thực hành có Bảng IP & Topo**: Không chấp nhận hướng dẫn nào chỉ đưa lệnh mà không có sơ đồ và bảng IP.
- [x] **Chú thích lệnh đầy đủ**: 100% dòng lệnh Cisco IOS, PowerShell, Bash được comment rõ ràng.
- [x] **Tích hợp kiểm thử Wireshark**: Mỗi lab dịch vụ mạng phải có chỉ dẫn bắt gói tin xác thực (ví dụ 4 bước D-O-R-A của DHCP, 3-way handshake TCP).
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ KHẨN CẤP (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: Client VLAN 20 không nhận được IP từ DHCP Server VLAN 10
- **Hiện tượng**: Máy tính client chỉ nhận IP tự động dạng `169.254.x.x` (APIPA).
- **Nguyên nhân**: Quên cấu hình lệnh `ip helper-address <DHCP_IP>` trên Gateway sub-interface của Router; hoặc Firewall trên Windows Server đang chặn UDP port 67/68.
- **Quy trình xử lý**:
  1. Kiểm tra cấu hình router: `show running-config interface g0/0.20` xem đã có `ip helper-address` chưa.
  2. Bắt gói tin trên Router: `debug ip dhcp server packet` xem Router có nhận và forward DHCP DISCOVER không.
  3. Mở cổng UDP 67/68 trên Windows Server: `netsh advfirewall firewall add rule name="DHCP" dir=in action=allow protocol=UDP localport=67,68`.

### Sự cố 2: DNS Server không phân giải được tên miền nội bộ `.corp.dut.edu.vn`
- **Hiện tượng**: Client ping theo IP được nhưng ping theo hostname bị báo `Ping request could not find host`.
- **Quy trình xử lý**:
  1. Kiểm tra DNS Server IP trên client: `ipconfig /all` đảm bảo DNS chính là IP của DC-01.
  2. Xóa cache DNS trên client: `ipconfig /flushdns`.
  3. Kiểm tra Forward Lookup Zone trên DNS Server: `Get-DnsServerResourceRecord -ZoneName "corp.dut.edu.vn"`.
