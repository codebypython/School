# 📜 ĐIỀU LỆ PHÒNG CHIẾN LƯỢC & GIÁO TRÌNH 15 TUẦN (STRATEGY & CURRICULUM DEPT)
## Phòng 01 — Công Ty An Toàn Thông Tin & Tác Chiến Mạng (CORP-04-SEC)

> **Mã Phòng Ban:** `SEC-DEPT-01`  
> **Trưởng phòng phụ trách:** Agent `PSD-04` (Pedagogical Scaffolding Designer) & Giám Đốc An Toàn Thông Tin (CISO)  
> **Cấp bậc quản trị:** Cấp 1 — Định hình khung chương trình 15 tuần An toàn mạng chuẩn DUT, William Stallings & NIST SP 800

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `SEC-DEPT-01` chịu trách nhiệm toàn diện về cấu trúc học thuật, thiết kế sư phạm và chuẩn mực bảo mật cho môn An Toàn Mạng (Network Security):
1. **Chuẩn Hóa Khung Đào Tạo 15 Tuần Chuẩn Quốc Tế**: Tích hợp các chuẩn an toàn thông tin kinh điển: NIST SP 800-series, CIS Controls, ISO/IEC 27001 và giáo trình *Network Security Essentials* (William Stallings).
2. **Cân Bằng 3 Trụ Cột Phòng Thủ**:
   - *Mật Mã Học Ứng Dụng*: Mã hóa đối xứng (AES-GCM), mã hóa bất đối xứng (RSA, ECC), trao đổi khóa Diffie-Hellman, hàm băm và chữ ký số HMAC/SHA-256.
   - *Bảo Mật Giao Thức & Hạ Tầng*: Hạ tầng khóa công khai PKI/X.509, bắt tay an toàn TLS 1.3, đường hầm bảo mật IPsec VPN (IKEv2 / ESP Tunnel mode) và SSHv2 Hardening.
   - *Kiểm Soát Truy Cập & Phòng Thủ Chủ Động*: Access Control Lists (Standard/Extended ACL), Tường lửa hướng vùng Cisco Zone-Based Policy Firewall (ZBF), và Giám sát phát hiện xâm nhập IDS/IPS (Snort/Suricata).
3. **Thiết Kế Phương Pháp Sư Phạm Xác Thực Gói Tin (Packet-Verified Pedagogy)**: Mọi khái niệm bảo mật lý thuyết phải được chứng minh thực tế bằng cách bắt gói tin trên Wireshark (so sánh dữ liệu bản rõ vs dữ liệu đã mã hóa).

---

## 2. BỘ QUY TẮC BẤT BIẾN (SECURITY & PEDAGOGICAL INVARIANTS)
1. **Nguyên tắc Phòng Thủ Theo Chiều Sâu (Defense-in-Depth Invariant)**: Cấm tuyệt đối thiết kế mạng chỉ dựa vào một lớp bảo vệ duy nhất (perimeter firewall). Phải kết hợp phân đoạn mạng (VLAN Segmentation), kiểm soát truy cập (ACL), mã hóa đường truyền (IPsec/TLS) và xác thực tập trung (802.1X/RADIUS).
2. **Nguyên tắc Từ Chối Mặc Định (Explicit Deny All Invariant)**: Mọi chính sách tường lửa hoặc danh sách điều khiển truy cập bắt buộc phải tuân theo quy tắc: Chỉ mở đích danh các cổng và giao thức cần thiết; kết thúc danh sách luôn là luật từ chối toàn bộ ngầm định hoặc tường minh (`deny ip any any log`).
3. **Nguyên tắc "Cấm Mật Mã Tự Chế" (Never Roll Your Own Crypto)**: Cấm sinh viên hoặc trợ giảng tự viết các thuật toán mã hóa tùy biến để bảo vệ dữ liệu thực tế. Bắt buộc phải sử dụng các thư viện chuẩn hóa đã qua kiểm định quốc tế (OpenSSL, PyCryptodome, cryptography library).
4. **Nguyên tắc Đạo Đức Nghề Nghiệp (Ethical Hacking & Legal Compliance)**: Mọi kỹ thuật tấn công mô phỏng (ARP Spoofing, Port Scanning, DoS Simulation) chỉ được thực hiện trong môi trường Lab biệt lập (Isolated Sandbox). Nghiêm cấm mọi hành vi tấn công ra mạng trường hoặc Internet.

---

## 3. BỘ LỆNH & CÔNG CỤ AN TOÀN MẠNG (TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Tạo cặp khóa RSA 4096-bit và yêu cầu ký chứng chỉ CSR với OpenSSL
openssl req -new -newkey rsa:4096 -nodes -keyout server.key -out server.csr -subj "/C=VN/ST=DaNang/O=DUT/CN=secure.dut.edu.vn"

# 2. Tự ký chứng chỉ số X.509 có thời hạn 365 ngày
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

# 3. Phân tích bắt tay TLS 1.3 và cipher suite đang sử dụng của máy chủ từ xa
openssl s_client -connect secure.dut.edu.vn:443 -tls1_3

# 4. Kiểm tra mã hóa và toàn vẹn file bằng SHA-256
sha256sum sensitive_payload.dat
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
01_Strategy_and_Curriculum/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── AGENT_PROFILE.md                   # Hồ sơ Mentor An toàn mạng DUT
├── ROADMAP_AND_CURRICULUM.md          # Khung chương trình 15 tuần chi tiết chuẩn NIST & Stallings
├── CRYPTO_PRIMITIVES_CHEATSHEET.md    # Cẩm nang tóm tắt các thuật toán mật mã và kích thước khóa
└── ETHICAL_SECURITY_POLICY_DUT.md     # Bản cam kết đạo đức an toàn thông tin chuẩn ĐHBK Đà Nẵng
```

---

## 5. MẪU KHUNG CẤU HÌNH & CHÍNH SÁCH BẢO MẬT (GOLD MASTER BOILERPLATE)

### Cấu Hình Đường Hầm Bảo Mật IPsec Site-to-Site VPN (IKEv2 & AES-256) Trên Cisco IOS
```cisco
! GOLD MASTER: CISCO IOS IKEv2 IPsec SITE-TO-SITE VPN TUNNEL
! Tác giả: DUT Network Security Mentor
enable
configure terminal

! 1. Cấu hình IKEv2 Proposal (Pha 1: Đàm phán thuật toán)
crypto ikev2 proposal IKEV2_PROPOSAL
 encryption aes-cbc-256
 integrity sha256
 group 14                                         ! Diffie-Hellman 2048-bit
exit

! 2. Cấu hình IKEv2 Policy liên kết với Proposal
crypto ikev2 policy IKEV2_POLICY
 proposal IKEV2_PROPOSAL
exit

! 3. Cấu hình IKEv2 Keyring chứa Pre-Shared Key bí mật
crypto ikev2 keyring VPN_KEYRING
 peer SITE_BRANCH
  address 203.0.113.2                             ! IP Wan của chi nhánh đối tác
  pre-shared-key DUT_Secret_Key_2026!
exit

! 4. Cấu hình IKEv2 Profile
crypto ikev2 profile IKEV2_PROFILE
 match identity remote address 203.0.113.2 255.255.255.255
 identity local address 198.51.100.2              ! IP Wan của trụ sở chính
 authentication remote pre-share
 authentication local pre-share
 keyring local VPN_KEYRING
 lifetime 86400
exit

! 5. Cấu hình IPsec Transform-Set (Pha 2: Mã hóa tải dữ liệu ESP)
crypto ipsec transform-set IPSEC_TS esp-aes 256 esp-sha256-hmac
 mode tunnel
exit

! 6. Tạo Crypto Map liên kết luồng dữ liệu cần bảo vệ (ACL 101)
access-list 101 permit ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255

crypto map VPN_MAP 10 ipsec-isakmp
 set peer 203.0.113.2
 set transform-set IPSEC_TS
 set ikev2-profile IKEV2_PROFILE
 match address 101
exit

! 7. Áp dụng Crypto Map lên cổng WAN nối Internet
interface GigabitEthernet0/0/1
 crypto map VPN_MAP
exit
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **Xác thực mã hóa định lượng**: Mọi bài thực hành VPN hoặc TLS phải chứng minh được dữ liệu truyền trên dây bị mã hóa 100% bằng Wireshark (`Encrypted Alert` hoặc `ESP payload`).
- [x] **Không sử dụng thuật toán lỗi thời**: Tuyệt đối cấm sử dụng DES, 3DES, MD5, SHA-1, WEP, Telnet trong các giải pháp bảo mật chính thống.
- [x] **Khối lệnh có comment từng dòng**: Mọi tham số bảo mật (Key size, DH Group, Hashing, Lifetime) đều được giải thích cặn kẽ.
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ KHẨN CẤP (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: IPsec VPN Phase 1 (IKE SA) không thể thiết lập kết nối (Down)
- **Hiện tượng**: Lệnh `show crypto ikev2 sa` không hiển thị phiên kết nối hoặc trạng thái dừng ở `MM_WAIT`.
- **Nguyên nhân**: Mâu thuẫn tham số Pha 1 giữa hai đầu: Sai Pre-Shared Key, lệch thuật toán mã hóa (AES-128 vs AES-256), khác biệt Diffie-Hellman Group hoặc Firewall ISP chặn cổng UDP 500/4500.
- **Quy trình xử lý**:
  1. Kiểm tra log debug: `debug crypto ikev2 error` và `debug crypto ikev2 internal`.
  2. Đối chiếu bảng tham số mã hóa giữa hai Gateway.
  3. Kiểm tra Firewall cho phép UDP 500 (ISAKMP) và UDP 4500 (NAT-Traversal).

### Sự cố 2: Trình duyệt cảnh báo chứng chỉ số không tin cậy (`SEC_ERROR_UNKNOWN_ISSUER`)
- **Hiện tượng**: Khi truy cập máy chủ web nội bộ qua HTTPS, trình duyệt hiện màn hình đỏ cảnh báo nguy hiểm.
- **Nguyên nhân**: Chứng chỉ số được cấp phát bởi Internal CA (Root CA tự dựng) nhưng Client chưa import chứng chỉ CA gốc vào `Trusted Root Certification Authorities`.
- **Quy trình xử lý**:
  1. Xuất file `ca.crt` từ Certificate Authority Server.
  2. Trên Windows Client, chạy lệnh: `certutil -addstore -f "Root" ca.crt`.
  3. Khởi động lại trình duyệt và kiểm tra lại chuỗi tin cậy (Certificate Chain).
