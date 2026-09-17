# 🔐 GIÁO TRÌNH & LỘ TRÌNH 15 TUẦN: AN TOÀN MẠNG
## Network Security & Applied Cryptography — DUT Standard Curriculum

> **Chuyên ngành:** Kỹ sư Công nghệ Thông tin — Đại học Bách khoa, ĐH Đà Nẵng (DUT)  
> **Đơn vị thiết kế:** Agent `PSD-04` (Pedagogical Scaffolding Designer)  
> **Nguồn đối chiếu Tier A+:** [Cryptography and Network Security 8th ed](file:///d:/User/7th/School/00_Corporate_Knowledge_Vault/EXTERNAL_KNOWLEDGE_VAULT.md#4--an-toàn-mạng-network-security) (William Stallings), *Wireshark Network Analysis* (Laura Chappell), *NIST SP 800-series*, *Cisco Security Guide*.

---

## 🧭 TỔNG QUAN CHIẾN LƯỢC SƯ PHẠM 4 TẦNG

1. **Tầng 1: Bản chất Mật mã học & Cơ chế Giao thức (Why?)**: Hiểu sâu toán học đằng sau các thuật toán mã hóa (Vành Galois $GF(2^8)$, Đường cong Elliptic, Bắt tay Diffie-Hellman) và cấu trúc các gói tin bảo mật.
2. **Tầng 2: Cấu hình CLI & Triển khai Hệ thống (How?)**: Cấu hình chuẩn xác trên Router/Switch Cisco IOS (ACL, VPN, Routing Authentication) và máy chủ Linux (OpenSSL, iptables, ufw).
3. **Tầng 3: Phân tích Gói tin Bắt giữ với Wireshark (Validation)**: Mở file `.pcapng`, soi từng byte trong frame mạng để chứng minh dữ liệu đã được mã hóa/bảo vệ toàn vẹn.
4. **Tầng 4: ⚠️ Lỗi phổ biến sinh viên hay gặp & Micro-quiz (Troubleshooting & Defense)**: Cảnh báo các lỗi hổng cấu hình nguy hiểm, bẫy bảo mật và câu hỏi phản biện bảo vệ.

---

## 📅 LỊCH TRÌNH 15 TUẦN CHI TIẾT

| Tuần | Chuyên Đề Trọng Tâm | Giao Thức / Thuật Toán Cốt Lõi | Nguồn Đối Chiếu Tier A+ | Bài Tập Thực Chiến (Lab / CLI / Wireshark) |
| :---: | :--- | :--- | :--- | :--- |
| **W1** | **Tổng Quan An Toàn Mạng & CIA Triad** | Confidentiality, Integrity, Availability, Attack Surfaces | Stallings (Chương 1); NIST SP 800-115 | Lập mô hình đe dọa (Threat Modeling) cho hệ thống trường học |
| **W2** | **Mã Hóa Khối Đối Xứng (Symmetric Cipher)** | Feistel Network, DES, 3DES, AES (Rijndael) | Stallings (Chương 3, 5, 6) | Tính bằng tay 1 vòng Round Transformation của AES (SubBytes) |
| **W3** | **Chế Độ Hoạt Động Của Mã Khối (Cipher Modes)**| ECB, CBC, CFB, OFB, CTR, GCM (Galois/Counter Mode) | Stallings (Chương 7); NIST SP 800-38D | Minh họa lỗ hổng rò rỉ hình dạng của ECB mode trên file ảnh BMP |
| **W4** | **Mật Mã Khóa Công Khai & Trao Đổi Khóa** | RSA (Định lý Euler), Trao đổi khóa Diffie-Hellman, ECC | Stallings (Chương 9, 10) | Tự giải bài toán sinh khóa RSA với số nguyên tố nhỏ bằng Python |
| **W5** | **Tính Toàn Vẹn & Mã Xác Thực Thông Điệp** | Hàm băm (Hash): SHA-256, SHA-3, Cơ chế HMAC | Stallings (Chương 11, 12); RFC 2104 | Tự viết script kiểm chứng tính nhạy cảm thay đổi 1 bit (Avalanche Effect) |
| **W6** | **Chữ Ký Số & Hạ Tầng Khóa Công Khai (PKI)** | Digital Signatures, X.509 Certificates, CA, CRL, OCSP | Stallings (Chương 13, 14); RFC 5280 | **[Lab OpenSSL]**: Tự tạo Root CA, ký và thu hồi chứng chỉ số |
| **W7** | **An Toàn Tầng Giao Vận: SSL/TLS & HTTPS** | TLS 1.2 vs TLS 1.3 Handshake, Cipher Suites | Stallings (Chương 17); NIST SP 800-52r2 | **[Lab Wireshark]**: Bắt và phân tích bản tin Client Hello / Server Hello |
| **W8** | **Đánh Giá Giữa Kỳ & An Toàn Tầng Ứng Dụng** | SSHv2 (Port 22), PGP/GPG Email Encryption, DNSSEC | Stallings (Chương 18, 19); RFC 4253 | Dựng SSH Server với xác thực cặp khóa RSA 4096-bit (tắt Password) |
| **W9** | **An Toàn Tầng Mạng: Giao Thức IPsec** | IKEv1 vs IKEv2, AH vs ESP, Tunnel vs Transport Mode | Stallings (Chương 20); NIST SP 800-77r1 | **[Lab GNS3]**: Dựng Site-to-Site IPsec VPN kết nối 2 Router Cisco |
| **W10** | **Kiểm Soát Truy Cập Mạng (Network ACLs)** | Standard ACL, Extended ACL, Named ACL, Time-based ACL | Cisco CCNA Odom; Tài liệu `ACL Samples.pdf` | Cấu hình Extended ACL chặn Ping ICMP nhưng cho phép Web HTTPS |
| **W11** | **Xác Thực Giao Thức Định Tuyến** | MD5 / SHA-256 Authentication trong RIPv2, OSPF, EIGRP | Tài liệu `Authentication OSPF/EIGRP.pdf` | Bắt gói tin OSPF Hello trước và sau khi kích hoạt MD5 Auth |
| **W12** | **Tường Lửa & Phân Vùng Mạng (Firewalls & DMZ)** | Stateful Inspection, Zone-Based Policy Firewall (ZBF), DMZ | Stallings (Chương 22); Cisco Security | Cấu hình Zone-Based Firewall chia vùng INSIDE, OUTSIDE, DMZ |
| **W13** | **Hệ Thống Phát Hiện & Ngăn Ngừa Xâm Nhập** | NIDS / HIDS, Signature-based vs Anomaly, Snort Rules | Stallings (Chương 21); Snort 3 User Guide | Viết Snort Rules phát hiện tấn công quét cổng Nmap Port Scan |
| **W14** | **Phân Tích Gói Tin Bắt Giữ Chuyên Sâu** | Wireshark Display Filters, Tấn công ARP Spoofing, SYN Flood | Laura Chappell (Chương 8, 12) | Phân tích file pcap ghi nhận tấn công SYN Flood và bẻ cờ TCP RST |
| **W15** | **Tổng Kết Học Phần, Kiểm Thử Xâm Nhập & Ôn Thi** | Ethical Hacking (Reconnaissance, Scanning, Exploitation) | NIST SP 800-115; OWASP Top 10 | Báo cáo phân tích an ninh mạng toàn diện cho doanh nghiệp |

---

## 🔬 CHI TIẾT TỪNG MODULE BÀI HỌC CỐT LÕI

### MODULE 1: MẬT MÃ ỨNG DỤNG & HẠ TẦNG KHÓA CÔNG KHAI PKI (TUẦN 2 - 6)

#### 1. Bản chất Toán học (Mathematical Formalism)
- **Chuẩn Mã Hóa Tiên Tiến AES (Advanced Encryption Standard)**:
  - Hoạt động trên ma trận trạng thái State $4 \times 4$ byte (128 bit).
  - 4 phép biến đổi trong mỗi vòng (Round):
    1. `SubBytes`: Thay thế phi tuyến qua S-Box (dựa trên phép nghịch đảo trong trường hữu hạn Galois $GF(2^8)$).
    2. `ShiftRows`: Dịch vòng các hàng của ma trận trạng thái.
    3. `MixColumns`: Phép nhân ma trận trong $GF(2^8)$ (vòng cuối cùng bỏ qua bước này).
    4. `AddRoundKey`: Phép toán XOR từng bit giữa State và khóa vòng con (Round Key).
- **Thuật toán Mã Công Khai RSA**:
  - Chọn 2 số nguyên tố lớn $p, q$. Tính module $n = p \times q$.
  - Tính hàm số Euler: $\phi(n) = (p-1)(q-1)$.
  - Chọn số mũ công khai $e$ sao cho $\gcd(e, \phi(n)) = 1$ (thường chọn $e = 65537$).
  - Khóa bí mật $d$ là nghịch đảo modulo: $d \equiv e^{-1} \pmod{\phi(n)} \iff e \cdot d \equiv 1 \pmod{\phi(n)}$.
  - **Mã hóa**: $C = M^e \pmod{n}$.
  - **Giải mã**: $M = C^d \pmod{n}$.

#### 2. Kịch Bản Thực Hành OpenSSL CLI Chuẩn
```bash
# 1. Tạo khóa riêng tư RSA 2048-bit được mã hóa bằng AES-256
openssl genpkey -algorithm RSA -out ca_private.key -aes256 -pkeyopt rsa_keygen_bits:2048

# 2. Tạo chứng chỉ số tự ký (Root CA Self-signed Certificate) thời hạn 365 ngày
openssl req -x509 -new -nodes -key ca_private.key -sha256 -days 365 -out ca_cert.pem \
    -subj "/C=VN/ST=DaNang/L=LienChieu/O=DUT/OU=IT/CN=DUT-RootCA"

# 3. Xem chi tiết nội dung chứng chỉ X.509
openssl x509 -in ca_cert.pem -text -noout
```

#### 3. ⚠️ Lỗi Phổ Biến Sinh Viên Hay Gặp
1. **Dùng chế độ ECB (Electronic Codebook) để mã hóa dữ liệu**: ECB chia dữ liệu thành các khối độc lập và mã hóa bằng cùng một khóa. Các khối plaintext giống hệt nhau sẽ cho ra ciphertext giống hệt nhau $\rightarrow$ Không che giấu được cấu trúc dữ liệu (Điển hình là bức ảnh chim cánh cụt Tux mã hóa bằng ECB vẫn nhìn rõ hình dạng!). **Luôn dùng CBC (với IV ngẫu nhiên) hoặc GCM!**
2. **Nhầm lẫn giữa Mã hóa (Encryption) và Băm (Hashing)**: Mã hóa là quá trình **2 chiều (Two-way)** nhằm bảo vệ tính bí mật (có thể giải mã khi có khóa). Băm là hàm **1 chiều (One-way)** nhằm bảo vệ tính toàn vẹn (không thể đảo ngược để lấy lại văn bản gốc).

---

### MODULE 2: GIAO THỨC BẢO MẬT GIAO VẬN & MẠNG: TLS & IPSEC (TUẦN 7 - 9)

#### 1. Phân Tích Bắt Tay TLS 1.3 vs TLS 1.2 (Wireshark Perspective)
- **TLS 1.2 (Bắt tay 2-RTT)**: Cần 2 vòng trao đổi (Round-Trip Time) để thỏa thuận Cipher Suite, trao đổi tham số Diffie-Hellman và xác thực chứng chỉ trước khi gửi dữ liệu ứng dụng.
- **TLS 1.3 (Bắt tay 1-RTT & 0-RTT Resumption)**:
  - Bản tin `Client Hello` gửi kèm luôn các dự đoán khóa chia sẻ (`Key Share` extension).
  - Bản tin `Server Hello` phản hồi lại khóa phiên đã thỏa thuận và mã hóa toàn bộ các bản tin phía sau (kể cả Chứng chỉ số của Server).
  - Loại bỏ hoàn toàn các thuật toán mật mã yếu (loại bỏ RSA key-exchange, MD5, SHA-1, RC4, DES, CBC mode). Chỉ hỗ trợ AEAD (Authenticated Encryption with Associated Data như AES-GCM, ChaCha20-Poly1305).

#### 2. Kịch Bản Cấu Hình IPsec Site-to-Site VPN (Cisco IOS)
*(Liên kết bài tập thực tế tại phòng Lab DUT)*
```cisco
! Bước 1: Cấu hình ISAKMP / IKE Phase 1 Policy (Thương lượng hầm bảo mật)
crypto isakmp policy 10
 encr aes 256
 hash sha256
 authentication pre-share
 group 14
 lifetime 86400
exit

! Cấu hình Pre-shared Key cho Router đối tác
crypto isakmp key DUTSecretKey2026 address 203.0.113.2

! Bước 2: Cấu hình IPsec Phase 2 Transform Set (Mã hóa lưu lượng thực)
crypto ipsec transform-set TS-AES-SHA esp-aes 256 esp-sha256-hmac
 mode tunnel
exit

! Bước 3: Định nghĩa Access-list xác định lưu lượng cần bảo vệ (Interesting Traffic)
access-list 105 permit ip 192.168.10.0 0.0.0.255 192.168.20.0 0.0.0.255

! Bước 4: Tạo Crypto Map và gán vào cổng WAN
crypto map CM-SITE-TO-SITE 10 ipsec-isakmp
 set peer 203.0.113.2
 set transform-set TS-AES-SHA
 match address 105
exit

interface GigabitEthernet0/0
 crypto map CM-SITE-TO-SITE
exit
```

#### 3. ⚠️ Lỗi Phổ Biến Sinh Viên Hay Gặp
1. **Lệch cấu hình ISAKMP Policy giữa 2 đầu Router**: Chỉ cần lệch 1 thông số (Ví dụ: Router A dùng `group 14` còn Router B dùng `group 2`, hoặc lệch Pre-shared key) là Phase 1 sẽ thất bại hoàn toàn. Lệnh kiểm tra: `show crypto isakmp sa` (Trạng thái phải là `QM_IDLE`).
2. **Access-list xác định Interesting Traffic không đối xứng**: Nếu Router A cho phép từ Subnet A sang Subnet B, thì Router B bắt buộc phải cho phép ngược lại từ Subnet B sang Subnet A. Nếu viết sai, Phase 2 không thể kích hoạt!

---

### MODULE 3: KIỂM SOÁT TRUY CẬP, XÁC THỰC ĐỊNH TUYẾN & TƯỜNG LỬA (TUẦN 10 - 13)
*(Tích hợp trọn vẹn tài liệu `ACL Samples.pdf`, `Authentication OSPF.pdf`, `Authentication EIGRP.pdf`)*

#### 1. Nguyên Tắc Thiết Kế Access Control List (ACL)
- **Standard ACL (1-99, 1300-1999)**: Chỉ lọc theo Địa chỉ IP Nguồn. **Vị trí đặt: Càng gần ĐÍCH càng tốt**.
- **Extended ACL (100-199, 2000-2699)**: Lọc theo IP Nguồn, IP Đích, Giao thức (TCP, UDP, ICMP), và Cổng dịch vụ (Port 80, 443, 22). **Vị trí đặt: Càng gần NGUỒN càng tốt** (để loại bỏ gói tin rác ngay tại biên mạng).
- **Quy tắc Vàng (Implicit Deny Any)**: Cuối mọi danh sách ACL luôn có một dòng lệnh ngầm định `deny ip any any`. Nếu không có ít nhất 1 dòng `permit`, toàn bộ lưu lượng sẽ bị chặn sạch!

#### 2. Kịch Bản Xác Thực OSPF MD5 (Liên kết tệp `Authentication OSPF.pdf`)
```cisco
interface GigabitEthernet0/1
 ip address 10.0.0.1 255.255.255.252
 ! Kích hoạt xác thực mã hóa MD5 trên giao diện OSPF
 ip ospf message-digest-key 1 md5 CiscoDUTPass2026
 ip ospf authentication message-digest
exit

router ospf 1
 ! Bật xác thực MD5 cho toàn bộ Area 0
 area 0 authentication message-digest
exit
```

#### 3. 💡 Micro-quiz Phản Biện
> *"Tại sao khi cấu hình Extended ACL chặn Web, lệnh `access-list 101 deny tcp any any eq 80` không đủ để chặn người dùng duyệt web mà bắt buộc phải chặn thêm cổng 443?"*  
> **Gợi ý trả lời**: Cổng 80 chỉ dành cho HTTP truyền thống (văn bản rõ). Hiện nay hơn 95% lưu lượng web toàn cầu đã chuyển sang HTTPS (HTTP qua lớp bảo mật TLS) hoạt động trên cổng TCP 443. Nếu chỉ chặn cổng 80, người dùng gõ `https://` vẫn truy cập web bình thường.

---

## 💻 NOTION INTEGRATION: BẢNG THEO DÕI GÓI TIN WIRESHARK

Dành cho Database `PACKET CAPTURE ANALYSIS LOG` trên Notion theo chuẩn [NOTION_SYSTEM_GUIDE.md](file:///d:/User/7th/School/00_Central_Notion_LMS_Hub/NOTION_SYSTEM_GUIDE.md#4-an-toàn-mạng-security):

| Giao Thức / Kịch Bản | Display Filter Wireshark | Các Byte / Trường Quan Trọng | Ý Nghĩa An Ninh Mạng | Trạng Thái Phân Tích |
| :--- | :--- | :--- | :--- | :---: |
| **TCP 3-Way Handshake** | `tcp.flags.syn == 1` | `SYN`, `ACK`, `Sequence Number`, `MSS` | Kiểm tra bắt tay bình thường vs tấn công SYN Flood | ✅ Đã chụp ảnh |
| **TLS 1.3 Client Hello** | `tls.handshake.type == 1` | `Cipher Suites`, `Server Name (SNI)`, `Key Share` | Xác định phiên bản mã hóa và tên miền truy cập | ✅ Đã phân tích |
| **IPsec ESP Traffic** | `esp` | `SPI (Security Parameters Index)`, `Seq Number` | Chứng minh toàn bộ tải Payload đã bị mã hóa đen | ⏳ Chờ làm lab |
| **OSPF MD5 Auth** | `ospf` | `Auth Type: 2 (Cryptographic)`, `Key ID`, `Digest` | Chứng minh mật khẩu không truyền rõ trên đường dây | ✅ Đã hoàn thành |
