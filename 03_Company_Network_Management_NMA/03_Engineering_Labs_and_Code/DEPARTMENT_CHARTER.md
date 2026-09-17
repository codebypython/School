# 📜 ĐIỀU LỆ PHÒNG KỸ THUẬT & PHÒNG LAB THỰC CHIẾN (ENGINEERING LABS & OPERATIONS DEPT)
## Phòng 03 — Công Ty Hạ Tầng & Quản Trị Mạng Doanh Nghiệp (CORP-03-NMA)

> **Mã Phòng Ban:** `NMA-DEPT-03`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (`HM-00`) & Giám Sát Kỹ Thuật (`SMS-02`)  
> **Cố vấn chuyên môn:** DUT Network Admin Mentor (`AGENT_PROFILE.md`)  
> **Tiêu chuẩn chất lượng:** Cisco CCNA Enterprise Standard / Mô hình FCAPS / IETF RFCs / Wireshark Verified

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kỹ Thuật & Phòng Lab Thực Chiến là **trung tâm hạ tầng mạng và máy chủ doanh nghiệp**:
1. **Thiết Kế & Mô Phỏng Topo Mạng Chuẩn Mực**: Xây dựng các sơ đồ mạng phức hợp trên Cisco Packet Tracer và GNS3 (VLANs, 802.1Q Trunking, EtherChannel, OSPF Single/Multi-Area, BGP, NAT/PAT).
2. **Triển Khai Dịch Vụ Mạng Cốt Lõi (Core Network Services)**: Cấu hình hệ thống DHCP Server (kèm DHCP Relay Agent), DNS Server (BIND9 & Windows Server DNS), Active Directory Domain Services (AD DS) và Group Policy Objects (GPO).
3. **Giám Sát & Vận Hành Theo Chuẩn FCAPS**: Thiết lập hệ thống giám sát qua giao thức SNMPv2c/v3, tập trung hóa nhật ký qua Syslog Server và đo lường lưu lượng qua NetFlow.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (AGENT BẮT BUỘC TUÂN THỦ)

1. **Quy Tắc Bảng Phân Bổ IP & Sơ Đồ Topo Bắt Buộc**:
   - **CẤM TUYỆT ĐỐI**: Đưa ra các câu lệnh cấu hình mà không có **Bảng Phân Bổ Địa Chỉ IP (IP Addressing Table)** và **Sơ Đồ Topo Kết Nối Cổng** đứng trước.
   - Mọi bảng IP bắt buộc phải có đủ các cột: `Thiết bị`, `Giao diện (Interface)`, `Địa chỉ IP`, `Subnet Mask (CIDR)`, `Default Gateway`.
2. **Quy Tắc Chú Thích Dòng Lệnh CLI 100%**:
   - Mọi khối lệnh Cisco IOS, PowerShell hoặc Bash Linux bắt buộc phải có comment giải thích chi tiết mục đích của từng dòng lệnh.
3. **Quy Tắc Bộ Ba Kiểm Chứng (Verification Triad)**:
   - Sau mỗi khối lệnh cấu hình, **BẮT BUỘC** phải có:
     1. Lệnh kiểm tra trạng thái: `show ip interface brief`, `show ip route`, `show vlan brief`.
     2. Lệnh kiểm tra thông tuyến: `ping` và `traceroute` từ các trạm đầu cuối (Endpoints).
     3. Lệnh lưu cấu hình: `copy running-config startup-config` (`write memory`).
4. **Quy Tắc Cô Lập Lỗi Theo 7 Tầng OSI (Bottom-Up Troubleshooting)**:
   - Khi xảy ra sự cố mất kết nối, bắt buộc phải kiểm tra từ Layer 1 (Cáp, Link up/down) $\rightarrow$ Layer 2 (VLAN, Port Security, STP) $\rightarrow$ Layer 3 (IP, Routing Table) $\rightarrow$ Layer 4-7 (ACL, Dịch vụ). Cấm nhảy thẳng lên Layer 7.

---

## 🛠️ 3. SKILLS ROUTE & TOOLCHAIN ĐIỀU HÀNH CHUẨN

### 3.1 Toolchain Yêu Cầu
- **Mô phỏng mạng**: Cisco Packet Tracer $\ge 8.2$, GNS3 $\ge 2.2$, EVE-NG.
- **Hệ điều hành máy chủ**: Windows Server 2022 / 2025, Ubuntu Server 22.04 LTS, Rocky Linux 9.
- **Phân tích giao thức**: Wireshark $\ge 4.0$ (Display Filters chuyên sâu: `bootp`, `dns`, `icmp`, `ospf`).
- **Giao thức quản trị**: SSHv2, SNMPv3, Syslog RFC 5424.

---

## 💻 4. MẪU KHUNG CẤU HÌNH CHUẨN NGHIỆP VỤ (GOLD MASTER CISCO IOS ROUTER-ON-A-STICK + DHCP RELAY)

Mẫu chuẩn mực cấu hình **Inter-VLAN Routing & DHCP Relay Agent** kèm chú thích từng dòng:

```cisco
! ================================================================
! THIẾT BỊ: CISCO ROUTER R1 (GATEWAY ĐIỀU HÀNH DOANH NGHIỆP)
! TÍNH NĂNG: ROUTER-ON-A-STICK CHO VLAN 10 (IT) & VLAN 20 (SALES)
! ================================================================

enable
configure terminal

! 1. Kích hoạt giao diện vật lý kết nối với Switch (không gán IP trực tiếp)
interface GigabitEthernet0/0/0
 no ip address
 no shutdown
 description Ket noi trunking toi Switch SW1
exit

! 2. Cấu hình Sub-interface cho VLAN 10 (Khối Kỹ Thuật IT)
interface GigabitEthernet0/0/0.10
 encapsulation dot1Q 10                           ! Đóng gói chuẩn 802.1Q cho VLAN 10
 ip address 192.168.10.1 255.255.255.0            ! Gateway cho subnet 192.168.10.0/24
 ip helper-address 10.0.0.100                     ! Chuyển tiếp DHCP Broadcast (DORA) toi DHCP Server
 description Gateway VLAN 10 - IT Department
exit

! 3. Cấu hình Sub-interface cho VLAN 20 (Khối Kinh Doanh Sales)
interface GigabitEthernet0/0/0.20
 encapsulation dot1Q 20                           ! Đóng gói chuẩn 802.1Q cho VLAN 20
 ip address 192.168.20.1 255.255.255.0            ! Gateway cho subnet 192.168.20.0/24
 ip helper-address 10.0.0.100                     ! Chuyển tiếp DHCP Broadcast toi DHCP Server
 description Gateway VLAN 20 - Sales Department
exit

! 4. Lưu cấu hình vào NVRAM
end
copy running-config startup-config
```

---

## 🛡️ 5. BỘ TIÊU CHÍ NGHIỆM THU CHẤT LƯỢNG (DEFINITION OF DONE - DoD)

- [ ] **DoD-1 (Bảng IP Đầy Đủ)**: Có bảng phân bổ IP trước khi thực hiện các bước cấu hình.
- [ ] **DoD-2 (Giao Diện Up/Up)**: Toàn bộ interface có trạng thái `Status: up`, `Protocol: up`.
- [ ] **DoD-3 (End-to-End Connectivity)**: Lệnh `ping` giữa các PC ở các VLAN khác nhau đạt tỷ lệ thành công 100% ($5/5$).
- [ ] **DoD-4 (DHCP Lease Verified)**: PC nhận đủ 4 thông số: IP, Subnet Mask, Default Gateway, DNS Server.
- [ ] **DoD-5 (NVRAM Saved)**: Đã chạy lệnh `write memory` hoặc `copy run start` trên toàn bộ routers/switches.

---

## 🚑 6. CẨM NANG XỬ LÝ SỰ CỐ MẠNG (TOP 3 RUNBOOKS)

### 🚨 RUNBOOK 1: XỬ LÝ PC KHÔNG NHẬN ĐƯỢC ĐỊA CHỈ IP DHCP (DORA FAILURE)
* **Triệu chứng**: PC nhận dải IP tự động `169.254.x.x` (APIPA).
* **Quy trình cô lập lỗi 4 bước**:
  1. *Kiểm tra Layer 2*: Cổng switch nối với PC có nằm đúng Access VLAN mong muốn không? (`show vlan brief`).
  2. *Kiểm tra Trunk Port*: Đường kết nối Switch-Router có cho phép VLAN đó đi qua không? (`show interfaces trunk`).
  3. *Kiểm tra DHCP Relay*: Trên Router Sub-interface đã có lệnh `ip helper-address <IP_Server>` chưa?
  4. *Kiểm tra DHCP Pool trên Server*: Scope có bị cạn kiệt địa chỉ (Exhausted Pool) hoặc bị deactive không?

### 🚨 RUNBOOK 2: XỬ LÝ LỖI KHÔNG THÔNG TUYẾN INTER-VLAN (PING FAILED)
* **Triệu chứng**: PC thuộc VLAN 10 không thể ping tới Gateway `192.168.10.1`.
* **Khắc phục**:
  - Kiểm tra xem cổng vật lý chính của router đã gõ `no shutdown` chưa.
  - Kiểm tra số hiệu VLAN trong lệnh `encapsulation dot1Q <vlan_id>` có khớp với ID trên switch không.
