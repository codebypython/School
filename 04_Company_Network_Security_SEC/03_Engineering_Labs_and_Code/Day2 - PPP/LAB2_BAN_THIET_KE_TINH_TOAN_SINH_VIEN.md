# 📝 BẢN THIẾT KẾ & TÍNH TOÁN KỸ THUẬT (NHÁP TAY SINH VIÊN BÁCH KHOA)
**Học phần**: An Toàn Mạng & Mật Mã Học Ứng Dụng (CORP-04-SEC - DUT)  
**Bài thực hành**: Lab 2 - Xác Thực PPP CHAP Mạng WAN Tam Giác (VN - LAO - CAM)  
**Người thực hiện**: Sinh viên Khoa CNTT - ĐHBK Đà Nẵng  

---

### [PHẦN 1] BÀI TOÁN TÍNH TOÁN CHIA MẠNG VLSM (TỪ MẠNG GỐC 172.16.0.0/16)

* **Yêu cầu đề bài**: Sắp xếp thứ tự nhu cầu giảm dần theo nguyên tắc VLSM để không bị chồng lấn (Overlapping):
  $$\text{LAN VN (Max Host)} > \text{LAN LAO} > \text{LAN CAM} > 3 \times \text{WAN Links (2 Hosts)}$$

#### 1. Mạng 1: LAN Việt Nam (Cần mạng lớn nhất $\rightarrow$ chọn /19)
* Số bit host: $32 - 19 = 13$ bits $\rightarrow$ Số host: $2^{13} - 2 = 8190$ hosts.
* Subnet Mask: $/19 = 11111111.11111111.\mathbf{111}00000.00000000_2 = \mathbf{255.255.224.0}$.
* Bước nhảy octet 3: $256 - 224 = 32$.
* **Dải mạng**: `172.16.0.0 /19`
  * Network ID: `172.16.0.0`
  * Dải IP khả dụng: `172.16.0.1` $\rightarrow$ `172.16.31.254`
  * IP gán Fa0/0 VN: `172.16.0.1`
  * Broadcast: `172.16.31.255`

#### 2. Mạng 2: LAN Lào (Lấy dải kế tiếp $\rightarrow$ chọn /20)
* Mạng tiếp theo bắt đầu tại: `172.16.32.0`.
* Số bit host: $32 - 20 = 12$ bits $\rightarrow$ Số host: $2^{12} - 2 = 4094$ hosts.
* Subnet Mask: $/20 = 11111111.11111111.\mathbf{1111}0000.00000000_2 = \mathbf{255.255.240.0}$.
* Bước nhảy octet 3: $256 - 240 = 16$.
* **Dải mạng**: `172.16.32.0 /20`
  * Network ID: `172.16.32.0`
  * Dải IP khả dụng: `172.16.32.1` $\rightarrow$ `172.16.47.254`
  * IP gán Fa0/0 LAO: `172.16.32.1`
  * Broadcast: `172.16.47.255`

#### 3. Mạng 3: LAN Campuchia (Lấy dải kế tiếp $\rightarrow$ chọn /21)
* Mạng tiếp theo bắt đầu tại: `172.16.48.0`.
* Số bit host: $32 - 21 = 11$ bits $\rightarrow$ Số host: $2^{11} - 2 = 2046$ hosts.
* Subnet Mask: $/21 = 11111111.11111111.\mathbf{11111}000.00000000_2 = \mathbf{255.255.248.0}$.
* Bước nhảy octet 3: $256 - 248 = 8$.
* **Dải mạng**: `172.16.48.0 /21`
  * Network ID: `172.16.48.0`
  * Dải IP khả dụng: `172.16.48.1` $\rightarrow$ `172.16.55.254`
  * IP gán Fa0/0 CAM: `172.16.48.1`
  * Broadcast: `172.16.55.255`

#### 4. Các Mạng WAN Điểm - Điểm (/30, Cần đúng 2 IP)
Mạng tiếp theo bắt đầu tại: `172.16.56.0`. Subnet Mask: `255.255.255.252`, Bước nhảy octet 4 = 4:
* **Mạng 4: WAN VN - LAO**: `172.16.56.0 /30`
  * Range: `172.16.56.1` (VN S1/0) $\leftrightarrow$ `172.16.56.2` (LAO S1/0). Broadcast: `172.16.56.3`.
* **Mạng 5: WAN LAO - CAM**: `172.16.56.4 /30`
  * Range: `172.16.56.5` (LAO S1/1) $\leftrightarrow$ `172.16.56.6` (CAM S1/0). Broadcast: `172.16.56.7`.
* **Mạng 6: WAN CAM - VN**: `172.16.56.8 /30`
  * Range: `172.16.56.9` (CAM S1/1) $\leftrightarrow$ `172.16.56.10` (VN S1/1). Broadcast: `172.16.56.11`.

---

### [PHẦN 2] NGUYÊN LÝ TOÁN HỌC & CƠ CHẾ BẮT TAY PPP CHAP (3-WAY HANDSHAKE)

```
      ROUTER A (Authenticator)                               ROUTER B (Peer)
                 │                                                  │
                 │   [1] CHAP Challenge (Code 0x01)                 │
                 │   (Identifier ID, Random Value R, Name 'VN')     │
                 ├─────────────────────────────────────────────────>│
                 │                                                  │
                 │                                                  │ Tính toán Response:
                 │                                                  │ Hash = MD5(ID + Secret + R)
                 │   [2] CHAP Response (Code 0x02)                  │
                 │   (Identifier ID, Hash, Name 'LAO')              │
                 │<─────────────────────────────────────────────────┤
                 │                                                  │
  Kiểm tra Hash: │                                                  │
  Local_Hash == ?│                                                  │
                 │   [3] CHAP Success (Code 0x03)                   │
                 ├─────────────────────────────────────────────────>│
                 │                                                  │ Line Protocol: UP!
```

* **Công thức băm 1 chiều**:
  $$\text{Response Hash} = \text{MD5}(\text{Identifier} \parallel \text{Secret} \parallel \text{Challenge Random Value})$$
* **Mật khẩu dùng chung**: `Sinch@u` (Không bao giờ gửi qua dây cáp mạng $\implies$ Miễn nhiễm 100% với kỹ thuật Sniffing!).
* **Chống Replay Attack**: Mỗi phiên bắt tay, Router Authenticator sinh một chuỗi `Challenge Random Value` (16 bytes ngẫu nhiên) hoàn toàn mới. Kẻ tấn công ghi lại gói tin cũ gửi lại sẽ bị từ chối ngay lập tức.

---

### [PHẦN 3] TỔNG HỢP LỆNH THI CÔNG NHANH (CLI CHEATSHEET)

```cisco
! --- CẤU HÌNH ROUTER VN ---
hostname VN
username LAO password Sinch@u
username CAM password Sinch@u

interface Serial1/0
 encapsulation ppp
 ppp authentication chap
 clock rate 2016000

interface Serial1/1
 encapsulation ppp
 ppp authentication chap
 clock rate 2016000

router rip
 version 2
 network 172.16.0.0
 no auto-summary
```
