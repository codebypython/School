# 📜 ĐIỀU LỆ PHÒNG KỸ THUẬT, CODE & THỰC NGHIỆM AN TOÀN MẠNG (ENGINEERING LABS & CODE DEPT)
## Phòng 03 — Công Ty An Toàn Thông Tin & Tác Chiến Mạng (CORP-04-SEC)

> **Mã Phòng Ban:** `SEC-DEPT-03`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (`HM-00`) & Giám Sát Kỹ Thuật (`SMS-02`)  
> **Cố vấn chuyên môn:** DUT Network Security Mentor (`AGENT_PROFILE.md`)  
> **Tiêu chuẩn chất lượng:** NIST Special Publications / Cisco Network Security / TLS 1.3 / IKEv2 IPsec

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng Kỹ Thuật & Tác Chiến Mạng là **trung tâm phòng thủ hạ tầng và mật mã học ứng dụng**:
1. **Kiểm Soát Truy Cập Mạng Chuyên Sâu (Access Control Lists - ACL)**: Thiết kế và triển khai Standard ACL, Extended ACL, Named ACL lọc lưu lượng theo giao thức (TCP, UDP, ICMP), số hiệu cổng (Port Numbers) và cờ trạng thái (Established).
2. **Xây Dựng Hạ Tầng Xác Thực Tập Trung (AAA & TACACS+/RADIUS)**: Triển khai mô hình Authentication, Authorization, Accounting với Cisco Secure ACS hoặc Banana TACACS+ Server.
3. **Mã Hóa Đường Truyền & VPN An Toàn (IPsec VPN & TLS)**: Thiết lập Site-to-Site IPsec VPN (IKEv2, ESP Tunnel Mode, Diffie-Hellman Group 14/19), Tường lửa vùng Zone-Based Policy Firewall (ZBF).
4. **Phân Tích Gói Tin Tấn Công Với Wireshark**: Bắt gói và mổ xẻ byte dữ liệu để nhận diện các đòn tấn công: ARP Spoofing, SYN Flood, Brute Force mật khẩu, và bắt tay mật mã SSL/TLS.

---

## 2. BỘ QUY TẮC BẤT BIẾN (HARD CONSTRAINTS & CODING INVARIANTS)
1. **Quy Tắc Vị Trí Đặt ACL (ACL Placement Golden Rule)**:
   - **Standard ACL**: Đặt **càng gần đích đến (Destination) càng tốt** (để tránh chặn nhầm lưu lượng hợp lệ đi các hướng khác).
   - **Extended ACL**: Đặt **càng gần nguồn phát (Source) càng tốt** (để loại bỏ gói tin rác ngay tại cửa ngõ, tiết kiệm băng thông đường truyền).
   - Bắt buộc làm rõ chiều lọc: `inbound` (kiểm tra trước khi định tuyến) vs `outbound` (kiểm tra sau khi định tuyến ra cổng).
2. **Quy Tắc Tiêu Chuẩn Mật Mã Hiện Đại (Cryptographic Hard Constraints)**:
   - **CẤM TUYỆT ĐỐI**: Sử dụng các thuật toán mật mã đã bị bẻ gãy: DES, 3DES, MD5, SHA-1, RC4, Diffie-Hellman Group 1/2/5.
   - **BẮT BUỘC**: Sử dụng thuật toán chuẩn NIST: Mã hóa khối AES-256 hoặc AES-GCM; Băm toàn vẹn SHA-256 hoặc SHA-512; Khóa trao đổi Diffie-Hellman Group 14 trở lên (2048-bit) hoặc Group 19 (ECDH 256-bit).
3. **Quy Tắc An Toàn Quản Trị Thiết Bị (AAA Lockout Prevention)**:
   - Khi cấu hình xác thực AAA qua máy chủ TACACS+/RADIUS, **CẤM ĐƯỢC BỎ QUÊN TÙY CHỌN LOCAL FALLBACK**:
     ```cisco
     ! BẮT BUỘC: Có fallback 'local' để admin không bị nhốt ở ngoài khi mất kết nối tới TACACS Server
     aaa authentication login default group tacacs+ local
     ```
4. **Quy Tắc Minh Chứng Bắt Gói Tin (Wireshark Verification Invariant)**:
   - Mọi bài lab bảo mật bắt buộc phải có minh chứng gói tin (`.pcap`/`.pcapng` hoặc ảnh chụp Wireshark Display Filter) chứng minh gói tin đã bị drop (đối với ACL) hoặc nội dung đã được mã hóa thành dữ liệu rác (đối với VPN/SSH).

---

## 3. BỘ LỆNH & SKILLS ROUTE ĐIỀU HÀNH CHUẨN (TOOLCHAIN)
- **Mô phỏng an ninh mạng**: GNS3 $\ge 2.2$, Cisco Packet Tracer Security, VMware Workstation Pro ($\ge 17.5$).
- **Phân tích gói tin**: Wireshark $\ge 4.0$ (Bộ lọc chuyên dụng: `tacplus`, `radius`, `isakmp`, `esp`, `tls`).
- **Máy chủ AAA**: Banana AAA Server, Cisco ACS 5.x, FreeRADIUS.
- **Mật mã ứng dụng**: OpenSSL 3.x, Hashcat, John the Ripper.

```bash
# 1. Bắt gói tin chẩn đoán xác thực RADIUS / TACACS+ bằng tshark
tshark -i eth0 -f "udp port 1812 or tcp port 49" -V

# 2. Kiểm tra tính toàn vẹn và chữ ký số chứng chỉ SSL/TLS
openssl verify -CAfile ca.crt server.crt
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (STANDARDIZED LAB ASSETS)
Mỗi bài thực hành trong phòng ban được chuẩn hóa toàn diện theo cấu trúc 6 thành phần:
1. File cấu hình thiết bị chuẩn (`*_startup-config.cfg`, `.vpc`, `.gns3`)
2. File mô tả chi tiết bài thực hành (`*_OVERVIEW.md`)
3. Sơ đồ topo mạng mẫu trực quan độ nét cao (`sodo_*.png`)
4. Bản thiết kế & tính toán kỹ thuật kiểu sinh viên làm tay (`*_BAN_THIET_KE_TINH_TOAN_SINH_VIEN.md`)
5. Bản hướng dẫn thao tác kiểm tra chi tiết (`*_HUONG_DAN_KIEM_TRA_CHI_TIET.md`)
6. Tệp bắt gói tin thực nghiệm `.pcapng` & Cẩm nang phân tích Wireshark (`*_WIRESHARK_PCAPNG_ANALYSIS_GUIDE.md`)

```
03_Engineering_Labs_and_Code/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban chuẩn hóa
├── Day1/                              # Lab 1: Routing Authentication (RIPv2 / OSPF / EIGRP MD5)
│   ├── R1_startup-config.cfg & R2_startup-config.cfg
│   ├── sodo_lab1_routing_auth.png
│   ├── LAB1_ROUTING_AUTHENTICATION_OVERVIEW.md
│   ├── LAB1_BAN_THIET_KE_TINH_TOAN_SINH_VIEN.md
│   ├── LAB1_HUONG_DAN_KIEM_TRA_CHI_TIET.md
│   ├── LAB1_WIRESHARK_PCAPNG_ANALYSIS_GUIDE.md
│   └── rip.pcapng, ospf.pcapng, eigrp.pcapng
├── Day2 - PPP/                        # Lab 2: PPP Authentication (CHAP WAN 3 Quốc Gia)
│   ├── VN/LAO/CAM_startup-config.cfg
│   ├── sodo_lab2_ppp_chap.png
│   ├── LAB2_PPP_CHAP_AUTHENTICATION_OVERVIEW.md
│   ├── LAB2_BAN_THIET_KE_TINH_TOAN_SINH_VIEN.md
│   ├── LAB2_HUONG_DAN_KIEM_TRA_CHI_TIET.md
│   ├── LAB2_WIRESHARK_PCAPNG_ANALYSIS_GUIDE.md
│   └── VN-LAO.pcapng, LAO-CAM.pcapng, VN-CAM.pcapng, ppp.pcapng
├── Day3 - ACL/                        # Lab 3: Extended Access Control Lists (FTP/HTTP/Ping)
│   ├── West/East/Gateway/Internet_startup-config.cfg
│   ├── sodo_lab3_extended_acl.png
│   ├── LAB3_EXTENDED_ACL_OVERVIEW.md
│   ├── LAB3_BAN_THIET_KE_TINH_TOAN_SINH_VIEN.md
│   ├── LAB3_HUONG_DAN_KIEM_TRA_CHI_TIET.md
│   ├── LAB3_WIRESHARK_PCAPNG_ANALYSIS_GUIDE.md
│   ├── lab3_extended_acl_traffic.pcapng
│   └── acl/ (acl.gns3 & acl_cloud_vmnet.gns3)
└── Day4 - TACAS/                      # Lab 4: AAA TACACS+ Banana Corp (Cisco ACS 4.2 VMware)
    ├── TACACS_Client/Internet_startup-config.cfg & Clients_startup.vpc
    ├── sodo_lab4_aaa_tacacs_banana.png
    ├── LAB4_AAA_TACACS_BANANA_OVERVIEW.md
    ├── LAB4_BAN_THIET_KE_TINH_TOAN_SINH_VIEN.md
    ├── LAB4_HUONG_DAN_KIEM_TRA_CHI_TIET.md
    ├── LAB4_WIRESHARK_PCAPNG_ANALYSIS_GUIDE.md
    ├── lab4_tacacs_aaa_traffic.pcapng
    └── TACAS/ (TACAS.gns3 & TACAS_cloud_vmnet.gns3)
```

---

## 5. MẪU KHUNG CODE / GOLD MASTER BOILERPLATE (NAMED EXTENDED ACL & AAA TACACS+)
```cisco
! ================================================================
! THIẾT BỊ: CISCO ROUTER R1 (BIÊN AN NINH TẬP ĐOÀN)
! TÍNH NĂNG: NAMED EXTENDED ACL + AAA TACACS+ WITH LOCAL FALLBACK
! ================================================================

enable
configure terminal

! --- PHẦN 1: CẤU HÌNH EXTENDED ACCESS CONTROL LIST (NAMED ACL) ---
ip access-list extended SECURE_INTERNAL_TRAFFIC
 remark Cho phep giao thuong FTP (Control port 21 & Data port 20)
 permit tcp 192.168.1.0 0.0.0.255 host 10.0.0.50 eq 21
 permit tcp 192.168.1.0 0.0.0.255 host 10.0.0.50 eq 20
 
 remark Chan tuyet doi truy cap Web HTTP (80) va HTTPS (443) toi Web Server
 deny tcp 192.168.1.0 0.0.0.255 host 10.0.0.50 eq 80
 deny tcp 192.168.1.0 0.0.0.255 host 10.0.0.50 eq 443

 remark Chan goi tin do tim Ping (ICMP Echo Request)
 deny icmp 192.168.1.0 0.0.0.255 host 10.0.0.50 echo

 remark Cho phep toan bo luu luong con lai di qua (Implicit Deny override)
 permit ip any any
exit

! Ap dung ACL vao cong Gigabit0/0/0 theo chieu Inbound (ngay tai cua ngo)
interface GigabitEthernet0/0/0
 ip access-group SECURE_INTERNAL_TRAFFIC in
 description Cong tiep nhan luu luong phong IT da qua kiem duyet
exit

! --- PHẦN 2: CẤU HÌNH XÁC THỰC AAA TACACS+ AN TOÀN ---
! Tao tai khoan cuc bo du phong khi TACACS Server chet
username admin_backup privilege 15 secret SuperAdmin@2026!Pass

! Kich hoat che do AAA
aaa new-model

! Khai bao May chu TACACS+ Server
tacacs server TACACS_PRIMARY
 address ipv4 10.0.0.200
 key SecretTacacsKey2026#
exit

! Dinh nghia nhom may chu
aaa group server tacacs+ TACACS_GROUP
 server name TACACS_PRIMARY
exit

! Thiet lap xac thuc Login: Uu tien TACACS+, neu server timeout thi dung Local
aaa authentication login default group TACACS_GROUP local
aaa authorization exec default group TACACS_GROUP local

! Khoa console va vty vao che do AAA
line console 0
 login authentication default
line vty 0 4
 transport input ssh
 login authentication default

end
write memory
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [ ] **DoD-1 (ACL Lọc Chính Xác)**: Lệnh ping bị chặn (`Destination Host Unreachable`), Web HTTP bị từ chối kết nối, nhưng FTP kết nối thành công 100%.
- [ ] **DoD-2 (Zero Lockout Risk)**: Đã kiểm chứng việc rút dây mạng nối với TACACS Server, router vẫn cho phép đăng nhập thành công qua tài khoản `admin_backup`.
- [ ] **DoD-3 (Wireshark Captured)**: Có bản ghi file `.pcapng` xác thực bản tin AAA hoặc gói tin ICMP bị Drop.
- [ ] **DoD-4 (Strong Crypto Only)**: Không xuất hiện DES/3DES/MD5 trong toàn bộ file cấu hình running-config.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ KHẨN CẤP (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: Khắc phục bị khóa ngoài Router khi cấu hình AAA (Admin Lockout)
* **Triệu chứng**: Gõ mật khẩu đăng nhập báo `Authentication Failed` hoặc router đơ do chờ TACACS Server timeout.
* **Khắc phục**:
  - Không tắt nguồn thiết bị. Mở thêm 1 phiên SSH thứ hai kiểm tra xem tài khoản local có kích hoạt không.
  - Nếu mất quyền truy cập trên thiết bị thật: Phải khởi động vào chế độ ROMMON (`Break key`), đổi thanh ghi `confreg 0x2142`, bypass startup-config để khôi phục mật khẩu.

### Sự cố 2: Debug nguyên nhân lưu lượng bị ACL Drop nhầm
* **Lệnh theo dõi realtime**:
  ```cisco
  ! Bật log cho dòng deny trong ACL:
  deny ip any any log
  
  ! Xem số lượng gói tin match vào từng dòng ACL:
  show ip access-lists SECURE_INTERNAL_TRAFFIC
  ```
* Nếu số lượng `matches` ở dòng `deny` tăng vọt bất thường, đối chiếu địa chỉ IP nguồn/đích xem có bị lệch subnet mask dạng Wildcard Mask (`0.0.0.255`) không.
