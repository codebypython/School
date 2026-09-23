# 📝 BẢN THIẾT KẾ & TÍNH TOÁN KỸ THUẬT (NHÁP TAY SINH VIÊN BÁCH KHOA)
**Học phần**: An Toàn Mạng & Mật Mã Học Ứng Dụng (CORP-04-SEC - DUT)  
**Bài thực hành**: Lab 4 - Hạ Tầng Xác Thực Tập Trung AAA TACACS+ (Banana Corp)  
**Người thực hiện**: Sinh viên Khoa CNTT - ĐHBK Đà Nẵng  

---

### [PHẦN 1] THIẾT KẾ PHÂN ĐOẠN MẠNG (NETWORK SEGMENTATION)

* **LAN Banana Clients**: `192.168.1.0 /24`
  * Gateway (Fa0/0 Router): `192.168.1.1`
  * Dải Client: `192.168.1.10` $\rightarrow$ `192.168.1.254`
  * Vai trò: Khu vực mạng nội bộ của nhân viên (Untrusted / User zone).
* **Mạng Quản trị AAA Server**: `10.0.0.0 /24`
  * Router Fa0/1: `10.0.0.1`
  * Server ACS 4.2: `10.0.0.100` (VMware VMnet1 Host-Only)
  * Vai trò: Khu vực mạng quản trị cách ly (Management DMZ), chỉ chấp nhận lưu lượng TCP 49 từ Router.
* **Mạng WAN Internet**: `2.2.2.0 /24`
  * Router Fa1/0: `2.2.2.1`
  * ISP Gateway: `2.2.2.2`

---

### [PHẦN 2] SO SÁNH KỸ THUẬT: TACACS+ vs RADIUS (CÂU HỎI BẢO VỆ ĐỒ ÁN)

| Tiêu chí kỹ thuật | TACACS+ (Cisco Proprietary / RFC 8907) | RADIUS (IETF RFC 2865 / 2866) |
|:---|:---|:---|
| **Tầng vận chuyển** | **TCP Port 49** (Hướng kết nối, tin cậy, có ACK) | UDP Port 1812 & 1813 (Không tin cậy, tự retransmit) |
| **Mức độ mã hóa** | **Mã hóa TOÀN BỘ gói tin** (Header 12 bytes để hở) | Chỉ mã hóa duy nhất trường Password (lộ Username, Attributes) |
| **Kiến trúc AAA** | **Tách biệt độc lập** 3 module A - A - A | Gộp chung Authentication & Authorization làm một |
| **Kiểm soát lệnh** | Cấp quyền chi tiết theo **từng câu lệnh (Per-command authorization)** | Phân quyền theo User Profile / VSA tĩnh |
| **Ứng dụng thực tế**| Quản trị thiết bị mạng Router, Switch, Firewall | Quản lý truy cập mạng người dùng (Wi-Fi 802.1X, VPN) |

---

### [PHẦN 3] NGUYÊN LÝ MẬT MÃ: CẤU TRÚC GÓI TIN & MÃ HÓA TACACS+

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|major  | minor |     type      |     seq_no    |     flags     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                          session_id                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            length                             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|       Encrypted Body (Dữ liệu người dùng, lệnh, mật khẩu)     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

* **Header cố định**: Đúng **12 bytes**.
  * `major_version`: `0xc` (12) | `minor_version`: `0x0` hoặc `0x1`.
  * `type`: `1` (Authentication), `2` (Authorization), `3` (Accounting).
  * `seq_no`: Số thứ tự gói trong phiên (1, 2, 3...).
  * `flags`: `0x01` (Unencrypted - chế độ debug), `0x00` (Encrypted).
  * `session_id`: Số ngẫu nhiên 32-bit đại diện cho phiên làm việc.
  * `length`: Độ dài phần Body đi kèm phía sau.

* **Thuật toán sinh khóa dòng giả ngẫu nhiên (Pseudo-random Stream Generation)**:
  Phần thân (Body) được bảo vệ bằng phép toán XOR với chuỗi băm MD5 lặp:
  $$\text{Pad}_1 = \text{MD5}(\text{session\_id} \parallel \text{key} \parallel \text{version} \parallel \text{seq\_no})$$
  $$\text{Pad}_2 = \text{MD5}(\text{session\_id} \parallel \text{key} \parallel \text{version} \parallel \text{seq\_no} \parallel \text{Pad}_1)$$
  $$\text{Ciphertext}[i] = \text{Plaintext}[i] \oplus \text{Pad}[i]$$
  > Kẻ tấn công trên đường truyền không có khóa bí mật `ciscobanana123` sẽ không thể giải mã được chuỗi `Pad` $\implies$ Toàn bộ thông tin mật khẩu và câu lệnh quản trị được bảo vệ tuyệt mật.

---

### [PHẦN 4] BẢNG TỔNG HỢP CẤU HÌNH (CLI SCRATCHPAD)

```cisco
! 1. Bật cơ chế AAA
aaa new-model

! 2. Khai báo máy chủ TACACS+ (ACS 4.2 trên VMware)
tacacs-server host 10.0.0.100
tacacs-server key ciscobanana123
tacacs-server timeout 5

! 3. Cấu hình Xác thực (Authentication) kèm Fallback
aaa authentication login default group tacacs+ local
aaa authentication enable default group tacacs+ enable

! 4. Cấu hình Cấp quyền (Authorization)
aaa authorization exec default group tacacs+ local
aaa authorization commands 15 default group tacacs+ local

! 5. Cấu hình Ghi nhật ký (Accounting)
aaa accounting exec default start-stop group tacacs+
aaa accounting commands 15 default start-stop group tacacs+

! 6. Tạo tài khoản dự phòng khẩn cấp
username admin privilege 15 secret AdminBackupPass!
```
