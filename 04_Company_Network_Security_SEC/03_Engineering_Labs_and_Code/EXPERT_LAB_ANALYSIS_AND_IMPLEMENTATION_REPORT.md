# 🛡️ BÁO CÁO PHÂN TÍCH CHUYÊN SÂU & HƯỚNG DẪN TRIỂN KHAI LAB THỰC HÀNH
## Học Phần: An Toàn Mạng & Mật Mã Học Ứng Dụng (`CORP-04-SEC`)
> **Cơ quan thẩm định:** Hội đồng Cố vấn Kỹ thuật — CyberDefense & Cryptography Corp  
> **Cố vấn chuyên trách:** DUT Cyber Security Mentor  
> **Tài liệu nguồn trích xuất:** [Mô tả các lab và settings.md](file:///D:/User/7th/School/04_Company_Network_Security_SEC/02_Lectures_and_Raw_Materials/M%C3%B4%20t%E1%BA%A3%20c%C3%A1c%20lab%20v%C3%A0%20settings.md)  
> **Phiên bản:** 1.0.0 — Tiêu chuẩn Học thuật & Doanh nghiệp DUT

---

## 📑 MỤC LỤC TỔNG QUAN

1. [Tổng Quan Danh Mục Các Bài Lab Thực Chiến](#1-tổng-quan-danh-mục-các-bài-lab-thực-chiến)
2. [LAB 1: Xác Thực Định Tuyến EIGRP & Phân Tích Bắt Gói Tin Wireshark](#2-lab-1-xác-thực-định-tuyến-eigrp--phân-tích-bắt-gói-tin-wireshark)
3. [LAB 2: Giao Thức PPP Xác Thực CHAP & Thiết Kế Phân Mạng VLSM](#3-lab-2-giao-thức-ppp-xác-thực-chap--thiết-kế-phân-mạng-vlsm)
4. [LAB 3: Danh Sách Kiểm Soát Truy Cập (Extended ACL) & Kiểm Thử Dịch Vụ Mạng (FTP/HTTP/ICMP)](#4-lab-3-danh-sách-kiểm-soát-truy-cập-extended-acl--kiểm-thử-dịch-vụ-mạng-ftphttpicmp)
5. [LAB 4: Triển Khai Hạ Tầng Xác Thực & Cấp Quyền AAA (TACACS+) Doanh Nghiệp Banana](#5-lab-4-triển-khai-hạ-tầng-xác-thực--cấp-quyền-aaa-tacacs-doanh-nghiệp-banana)
6. [⚠️ Tổng Hợp Lỗi Phổ Biến Sinh Viên Hay Gặp & Cách Khắc Phục](#6-️-tổng-hợp-lỗi-phổ-biến-sinh-viên-hay-gặp--cách-khắc-phục)
7. [💡 Bộ Câu Hỏi Phản Biện / Micro-Quiz Bảo Vệ Lab](#7--bộ-câu-hỏi-phản-biện--micro-quiz-bảo-vệ-lab)

---

## 1. TỔNG QUAN DANH MỤC CÁC BÀI LAB THỰC CHIẾN

Dựa trên dữ liệu thu thập từ bài giảng của Giảng viên (Thầy Nguyễn Thế Xuân Ly), hệ thống bài tập thực hành được thiết kế theo mô hình **Bảo mật đa tầng (Defense-in-Depth)**:

```
                      ┌──────────────────────────────────────────────┐
                      │    TẦNG 4: AAA TACACS+ & QUẢN TRỊ TRUY CẬP   │ (Lab 4: Banana Corp)
                      └──────────────────────┬───────────────────────┘
                                             │
                      ┌──────────────────────▼───────────────────────┐
                      │    TẦNG 3: KIỂM SOÁT LUỒNG DỮ LIỆU BẰNG ACL   │ (Lab 3: Extended ACL)
                      └──────────────────────┬───────────────────────┘
                                             │
                      ┌──────────────────────▼───────────────────────┐
                      │  TẦNG 2: BẢO MẬT ĐỊNH TUYẾN (EIGRP / RIPv2)  │ (Lab 1: EIGRP Auth)
                      └──────────────────────┬───────────────────────┘
                                             │
                      ┌──────────────────────▼───────────────────────┐
                      │ TẦNG 1: BẢO MẬT LIÊN KẾT WAN ĐIỂM-ĐIỂM (PPP) │ (Lab 2: PPP CHAP)
                      └──────────────────────────────────────────────┘
```

---

## 2. LAB 1: XÁC THỰC ĐỊNH TUYẾN EIGRP & PHÂN TÍCH BẮT GÓI TIN WIRESHARK

### 2.1. Bản chất Kỹ thuật & Lý do Bảo mật (Why?)
- **Hiểm họa**: Giao thức định tuyến động nếu không xác thực sẽ chấp nhận bất kỳ bảng tin Routing Update nào từ một Router lạ cắm vào mạng (*Rogue Router*), dẫn đến tấn công đầu độc bảng định tuyến (**Route Poisoning**) hoặc chuyển hướng lưu lượng để nghe lén (**Man-in-the-Middle**).
- **Cơ chế**: Cisco EIGRP hỗ trợ cơ chế xác thực thông điệp bằng `key-chain` sử dụng hàm băm **MD5** (theo RFC 7868). Mọi gói tin EIGRP (Hello, Update) đều mang theo một chữ ký số tóm lược; Router nhận sẽ tính toán lại mã hash, nếu khớp mới nạp tuyến vào bảng định tuyến.
- **Giải mã câu hỏi của Giảng viên**:
  > *(2) Wireshark `EIGRP_AUTH_TYPE_TEXT = ?`*
  - Theo chuẩn đặc tả RFC 7868 (Mục 7.4.2) và mã nguồn bộ giải mã Wireshark (EIGRP Dissector):
    - `EIGRP_AUTH_TYPE_NONE = 0`: Không xác thực.
    - `EIGRP_AUTH_TYPE_TEXT = 1`: Xác thực mật khẩu văn bản thô (Plaintext).
    - `EIGRP_AUTH_TYPE_MD5 = 2`: Xác thực băm mật mã MD5.
  - Khi bắt gói tin EIGRP Hello có xác thực MD5, trường `Type` trong Authentication TLV sẽ có giá trị là `0x0002`.

### 2.2. Cấu hình Cisco IOS Mẫu (How?)

```cisco
! --- BƯỚC 1: TẠO CHUỖI KHÓA XÁC THỰC TRÊN TẤT CẢ ROUTER THAM GIA EIGRP ---
key chain EIGRP_KEYCHAIN
 key 1
  key-string CiscoSecPass123!     ! Mật khẩu bí mật chia sẻ chung giữa các Router

! --- BƯỚC 2: ÁP DỤNG XÁC THỰC LÊN CỔNG GIAO TIẾP MẠNG ---
interface Serial1/0
 ip address 10.0.0.1 255.255.255.252
 ! Kích hoạt chế độ xác thực MD5 cho AS 100
 ip authentication mode eigrp 100 md5
 ! Gán chuỗi khóa vào giao thức EIGRP AS 100
 ip authentication key-chain eigrp 100 EIGRP_KEYCHAIN
 no shutdown

! --- BƯỚC 3: KÍCH HOẠT TIẾN TRÌNH ĐỊNH TUYẾN EIGRP ---
router eigrp 100
 network 10.0.0.0 0.0.0.3
 no auto-summary
```

### 2.3. Xác thực với Wireshark (Validation)
1. Trong GNS3, chuột phải vào link Serial $\rightarrow$ **Start capture**.
2. Bộ lọc hiển thị (Display Filter): `eigrp`.
3. Mở một gói tin **EIGRP Hello**:
   - Mở rộng cây giao thức: `Cisco EIGRP` $\rightarrow$ `Authentication TLV`.
   - Kiểm tra trường: `Auth Type: MD5 keyed authorization (2)`.
   - Trường `Key ID: 1` và `Digest: [16 bytes mã băm MD5]`.

---

## 3. LAB 2: GIAO THỨC PPP XÁC THỰC CHAP & THIẾT KẾ PHÂN MẠNG VLSM

### 3.1. Bản chất Kỹ thuật & Cơ chế Bắt tay CHAP (Why?)
- **So sánh PAP vs CHAP**:
  - `PAP (Password Authentication Protocol)`: Bắt tay 2 bước, gửi mật khẩu dạng văn bản thuần qua đường truyền $\rightarrow$ Cực kỳ mất an toàn.
  - `CHAP (Challenge Handshake Authentication Protocol)`: Bắt tay 3 bước dựa trên mã băm MD5. Mật khẩu không bao giờ được truyền qua cáp mạng.
- **Quy trình bắt tay CHAP 3 bước**:
  1. **Challenge (Code 1)**: Router A gửi một chuỗi ngẫu nhiên (Challenge string) kèm ID gói tin cho Router B.
  2. **Response (Code 2)**: Router B kết hợp chuỗi ngẫu nhiên + Mật khẩu bí mật chia sẻ chung, đưa vào hàm băm `MD5(ID + Secret + Challenge)` rồi gửi chuỗi băm ngược lại.
  3. **Success / Failure (Code 3 / Code 4)**: Router A tính toán lại giá trị băm cục bộ. Nếu trùng khớp, gửi `Success` và cho phép đường truyền Link Up.

### 3.2. Thiết Kế Phân Bổ Mạng VLSM (6 Mạng Con)
Sơ đồ tam giác 3 Router: **VN**, **LAO**, **CAM** với dải mạng mẹ `172.16.0.0/16`:

| Thứ tự Subnet | Tên phân vùng mạng | Địa chỉ mạng / Prefix | Subnet Mask | Dải IP khả dụng (Host Range) | IP Cổng kết nối (Interface) |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **LAN VN** | `172.16.0.0/19` | `255.255.224.0` | `172.16.0.1` – `172.16.31.254` | Fa0/0 VN: `172.16.0.1` |
| **2** | **LAN LAO** | `172.16.32.0/20` | `255.255.240.0` | `172.16.32.1` – `172.16.47.254` | Fa0/0 LAO: `172.16.32.1` |
| **3** | **LAN CAM** | `172.16.48.0/21` | `255.255.248.0` | `172.16.48.1` – `172.16.55.254` | Fa0/0 CAM: `172.16.48.1` |
| **4** | **WAN VN - LAO** | `172.16.56.0/30` | `255.255.255.252` | `172.16.56.1` – `172.16.56.2` | Se1/0 VN: `.1` $\leftrightarrow$ Se1/0 LAO: `.2` |
| **5** | **WAN LAO - CAM**| `172.16.56.4/30` | `255.255.255.252` | `172.16.56.5` – `172.16.56.6` | Se1/1 LAO: `.5` $\leftrightarrow$ Se1/0 CAM: `.6` |
| **6** | **WAN CAM - VN** | `172.16.56.8/30` | `255.255.255.252` | `172.16.56.9` – `172.16.56.10`| Se1/1 CAM: `.9` $\leftrightarrow$ Se1/1 VN: `.10`|

### 3.3. Cấu hình Cisco IOS Mẫu (Ví dụ Router VN)

```cisco
! Đổi tên Router chuẩn xác (tên này dùng cho xác thực đối tác CHAP)
hostname VN

! Khai báo username của các Router láng giềng kèm mật khẩu chung
username LAO password ciscochappass
username CAM password ciscochappass

! Cấu hình cổng LAN VN
interface FastEthernet0/0
 ip address 172.16.0.1 255.255.224.0
 no shutdown

! Cấu hình WAN nối sang LAO
interface Serial1/0
 ip address 172.16.56.1 255.255.255.252
 encapsulation ppp               ! Chuyển đổi đóng gói HDLC sang PPP
 ppp authentication chap         ! Bắt buộc xác thực bằng CHAP
 no shutdown

! Cấu hình WAN nối sang CAM
interface Serial1/1
 ip address 172.16.56.10 255.255.255.252
 encapsulation ppp
 ppp authentication chap
 no shutdown
```

### 3.4. Tiêu Chuẩn Kiểm Tra (Validation Checklist)
1. **Kiểm tra bảng định tuyến**: Gõ `show ip route` trên từng Router. Đếm đúng **đủ 6 subnet VLSM** đã hội tụ.
2. **Kiểm tra Wireshark**:
   - Filter: `ppp` hoặc `chap`.
   - Kết quả: Thấy bản tin `PPP CHAP Challenge`, tiếp theo là `PPP CHAP Response` chứa chuỗi hash, cuối cùng là `PPP CHAP Success`.

---

## 4. LAB 3: DANH SÁCH KIỂM SOÁT TRUY CẬP (EXTENDED ACL) & KIỂM THỬ DỊCH VỤ MẠNG (FTP/HTTP/ICMP)

### 4.1. Phân Tích Đề Bài & Kiến Trúc
- **Topo**: 4 phân vùng mạng LAN nối qua các Router chạy định tuyến **RIPv2**:
  - `LAN 1` và `LAN 4`: Cổng Loopback.
  - `LAN 2` (ví dụ subnet `192.168.2.0/24`): Có Client PC và Windows Server 2003 (chạy IIS Web/FTP).
  - `LAN 3` (ví dụ subnet `192.168.3.0/24`): Có Client PC và Windows Server 2003 (chạy IIS Web/FTP).
- **Yêu cầu chính sách bảo mật (Security Policy Matrix)**:
  1. **Cho phép FTP** giữa LAN 2 và LAN 3 (Cả TCP port 21 Control và port 20 Data).
  2. **Chặn toàn bộ các kết nối khác** giữa LAN 2 và LAN 3 (Chặn Ping ICMP, chặn Web HTTP port 80).
  3. **Cho phép các kết nối khác** lưu thông bình thường (`permit ip any any`).

### 4.2. Thiết Kế Extended ACL Chuẩn

Nguyên tắc đặt Extended ACL: **Đặt càng gần nguồn (Source) càng tốt** để sớm loại bỏ lưu lượng rác, tiết kiệm băng thông đường truyền WAN.

```cisco
! --- TẠO ACCESS CONTROL LIST MỞ RỘNG (VÍ DỤ ACL SỐ 101 ÁP DỤNG TRÊN CỔNG ĐẦU VÀO CỦA LAN 2) ---
ip access-list extended SEC_FILTER_LAN2_TO_LAN3

 ! 1. Cho phép truyền file FTP (Port 21 - Control connection)
 permit tcp 192.168.2.0 0.0.0.255 192.168.3.0 0.0.0.255 eq ftp

 ! 2. Cho phép kênh truyền dữ liệu FTP (Port 20 - Data connection)
 permit tcp 192.168.2.0 0.0.0.255 192.168.3.0 0.0.0.255 eq ftp-data

 ! 3. Cho phép các gói tin TCP thiết lập phản hồi hợp lệ (Established sessions)
 permit tcp 192.168.2.0 0.0.0.255 192.168.3.0 0.0.0.255 established

 ! 4. CHẶN TẤT CẢ CÁC GIAO THỨC CÒN LẠI GIỮA LAN 2 VÀ LAN 3 (Bao gồm HTTP, ICMP Ping, v.v.)
 deny ip 192.168.2.0 0.0.0.255 192.168.3.0 0.0.0.255

 ! 5. CHO PHÉP MỌI KẾT NỐI KHÁC RA BÊN NGOÀI (LAN 1, LAN 4, Internet)
 permit ip any any

! --- ÁP DỤNG ACL LÊN CỔNG GIAO TIẾP VÀO CỦA ROUTER NỐI VỚI LAN 2 ---
interface FastEthernet0/0
 ip access-group SEC_FILTER_LAN2_TO_LAN3 in
```

### 4.3. Quy Trình Kiểm Thử Theo Yêu Cầu Của Giảng Viên

Đứng từ máy trạm LAN 2 PC (IP: `192.168.2.10`) kiểm tra tới Server LAN 3 (IP: `192.168.3.100`):

| Thử nghiệm | Thao tác lệnh | Kết quả mong đợi | Giải thích cơ chế |
| :--- | :--- | :--- | :--- |
| **1. Ping (ICMP)** | `ping 192.168.3.100` | **Destination host unreachable** hoặc **Request timed out** | Bị bắt bởi dòng luật `deny ip ...` |
| **2. Web (HTTP)** | Trình duyệt mở `http://192.168.3.100` | Không tải được trang, Connection timed out | Bị chặn cổng TCP 80 |
| **3. FTP (Truyền file)** | Mở CMD gõ: `ftp 192.168.3.100` | Kết nối thành công! Nhắc nhập User/Password | Khớp dòng `permit tcp ... eq ftp` |
| **4. Thao tác FTP** | Gõ `dir`, `get test.txt`, `quit` | Tải file thành công về máy PC | Khớp dòng `permit tcp ... eq ftp-data` |

---

## 5. LAB 4: TRIỂN KHAI HẠ TẦNG XÁC THỰC & CẤP QUYỀN AAA (TACACS+) DOANH NGHIỆP BANANA

### 5.1. Bản chất Kiến trúc AAA & Giao thức TACACS+ (Why?)
- **Mô hình AAA**:
  - **Authentication (Xác thực)**: Bạn là ai? (Username/Password).
  - **Authorization (Cấp quyền)**: Bạn được phép làm những gì? (Chỉ được gõ lệnh `show` hay được vào chế độ `configure terminal`).
  - **Accounting (Ghi nhật ký)**: Bạn đã làm những gì và trong bao lâu?
- **Tại sao dùng TACACS+ thay vì RADIUS?**
  - RADIUS chỉ mã hóa trường Password trong gói tin Access-Request (UDP port 1812/1813).
  - **TACACS+ (Cisco)** chạy trên nền **TCP port 49**, **mã hóa toàn bộ Payload của gói tin**, và tách biệt hoàn toàn 3 tiến trình Authentication, Authorization, Accounting.

### 5.2. Quy Trình Cài Đặt Trên Máy Ảo Windows Server 2003
Theo chỉ dẫn của Giảng viên, thứ tự cài đặt trên Server 2003 là điều kiện tiên quyết:

```text
[BƯỚC 1: Cài Java Runtime]
   Chạy file: jre-6u13-windows-i586-p-s.exe
   (Cần thiết để chạy các Applet quản trị của Cisco ACS Engine)
             │
             ▼
[BƯỚC 2: Cài Đặt Cisco Secure ACS v4.2]
   Giải nén ACSv4.2.124 FULL-K9.zip ──> Chạy setup.exe
   - Chọn database cục bộ (Local Database).
   - Đặt khóa bí mật TACACS+ Shared Secret: "ciscobanana123"
             │
             ▼
[BƯỚC 3: Cài Firefox 2.0]
   Chạy file: Firefox 2.0.exe
   (Tránh lỗi render khung iframe và JavaScript lỗi thời trên Internet Explorer 6 gốc của Server 2003)
             │
             ▼
[BƯỚC 4: Cấu Hình Trên Giao Diện Web Cisco ACS]
   Mở Firefox ──> Truy cập: http://127.0.0.1:2002
   1. Network Configuration:
      - Thêm AAA Client (Router Banana): IP 192.168.1.1, Key: "ciscobanana123", Protocol: TACACS+ (Cisco IOS).
   2. User Setup:
      - Tạo tài khoản nhân viên (vd: user "nhanvien", pass "123456").
```

### 5.3. Cấu hình Cisco IOS Router (TACACS+ Client)

```cisco
! 1. Kích hoạt kiến trúc bảo mật AAA mới
aaa new-model

! 2. Khai báo địa chỉ TACACS+ Server và khóa bí mật chia sẻ
tacacs-server host 192.168.1.100
tacacs-server key ciscobanana123

! 3. Cấu hình danh sách xác thực đăng nhập (Login Authentication)
! Ưu tiên hỏi TACACS+ Server trước; nếu Server chết, fallback về tài khoản local
aaa authentication login default group tacacs+ local
aaa authentication enable default group tacacs+ enable

! 4. Cấu hình cấp quyền (Authorization) chế độ thực thi lệnh
aaa authorization exec default group tacacs+ local

! 5. Tạo tài khoản cục bộ dự phòng (Phòng trường hợp Server 2003 sập)
username admin privilege 15 password 0 AdminBackupPass!

! 6. Áp dụng chính sách AAA lên cổng Console và VTY (Telnet/SSH)
line con 0
 login authentication default
line vty 0 4
 login authentication default
```

### 5.4. Xác Thực Luồng Gói Tin Wireshark
- Bắt gói trên đường truyền giữa Router và Server 2003.
- Filter: `tacacs`.
- Kết quả quan sát:
  - Thấy gói tin bắt tay TCP 3 bước tới port 49 (`syn` $\rightarrow$ `syn-ack` $\rightarrow$ `ack`).
  - Toàn bộ nội dung gói tin TACACS+ mang nhãn `Encrypted payload` $\rightarrow$ Chứng minh tính bảo mật toàn vẹn, kẻ gian nghe lén không thể đọc trộm username/password.

---

## 6. ⚠️ TỔNG HỢP LỖI PHỔ BIẾN SINH VIÊN HAY GẶP & CÁCH KHẮC PHỤC

1. **Lỗi CHAP Authentication Failed trong Lab 2**:
   - *Triệu chứng*: Cổng Serial báo `PPP: Authorization failed`, đường link liên tục flap up/down.
   - *Nguyên nhân*: Cấu hình sai tên `hostname` hoặc mật khẩu không khớp. Đối với CHAP, `username` được khai báo trên Router A phải là **chính xác hostname của Router B**, và `password` giữa 2 bên phải giống nhau 100%.
2. **Lỗi FTP Active Mode bị chặn bởi ACL trong Lab 3**:
   - *Triệu chứng*: Đăng nhập FTP thì được (nhập user/pass OK), nhưng khi gõ lệnh `dir` hoặc `ls` thì báo lỗi *425 Can't build data connection* hoặc treo.
   - *Nguyên nhân*: FTP sử dụng 2 cổng. Cổng 21 chỉ dùng để gửi lệnh (Control), trong khi việc truyền dữ liệu thư mục và file diễn ra trên cổng 20 (Data) hoặc cổng ngẫu nhiên (Passive). Nếu sinh viên chỉ mở `eq ftp` (port 21) mà quên mở `eq ftp-data` (port 20), lệnh `dir` sẽ bị drop ngay lập tức.
3. **Lỗi không đăng nhập được Cisco ACS trên Server 2003 trong Lab 4**:
   - *Triệu chứng*: Dùng IE6 mở trang web ACS bị trắng tinh hoặc báo lỗi script JavaScript.
   - *Nguyên nhân*: Trình duyệt IE6 quá cổ, không hỗ trợ HTML/DOM của ACS. Bắt buộc phải cài Firefox 2.0 theo đúng chỉ dẫn của Giảng viên.
4. **Lỗi Router bị khóa (Lockout) khi cấu hình AAA**:
   - *Triệu chứng*: Vừa gõ xong `aaa new-model` và thoát ra thì không thể Telnet hay Console vào lại Router được nữa.
   - *Khắc phục*: Luôn tạo sẵn một tài khoản cục bộ `username admin privilege 15 secret ...` và thêm tham số `local` ở cuối chuỗi kiểm tra (`group tacacs+ local`) trước khi áp dụng lên `line vty` hay `line con 0`.

---

## 7. 💡 BỘ CÂU HỎI PHẢN BIỆN / MICRO-QUIZ BẢO VỆ LAB

1. **Về EIGRP & Wireshark**: Tại sao cơ chế xác thực định tuyến EIGRP bằng MD5 lại có thể chống được tấn công Replay Attack (tấn công phát lại gói tin cũ đã bắt trộm)?
2. **Về Extended ACL**: Trong chính sách Lab 3, nếu hoán đổi vị trí đưa dòng `permit ip any any` lên đầu tiên trước các dòng `deny ip`, hệ thống mạng sẽ vận hành như thế nào?
3. **Về TACACS+ vs RADIUS**: Trong kịch bản công ty Banana cần kiểm soát chi tiết một nhân viên chỉ được gõ lệnh `show ip route` mà không được phép gõ lệnh `reload`, tại sao bắt buộc phải dùng TACACS+ mà RADIUS không thể làm được điều này?
