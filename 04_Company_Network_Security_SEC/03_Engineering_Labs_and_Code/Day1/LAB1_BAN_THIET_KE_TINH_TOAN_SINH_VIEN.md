# 📝 BẢN THIẾT KẾ & TÍNH TOÁN KỸ THUẬT (NHÁP TAY SINH VIÊN BÁCH KHOA)
**Học phần**: An Toàn Mạng & Mật Mã Học Ứng Dụng (CORP-04-SEC - DUT)  
**Bài thực hành**: Lab 1 - Xác Thực Giao Thức Định Tuyến (RIPv2 / OSPF / EIGRP MD5)  
**Người thực hiện**: Sinh viên Khoa CNTT - ĐHBK Đà Nẵng  

---

### [PHẦN 1] TÍNH TOÁN PHÂN CHIA ĐỊA CHỈ IP (SUBNETTING / VLSM)

#### 1. Mạng WAN Serial (Liên kết điểm - điểm R1 <-> R2)
* **Yêu cầu**: Cần đúng 2 địa chỉ IP khả dụng cho 2 đầu Serial (tiết kiệm không gian IP tối đa).
* **Tính toán số bit Host**:
  $$2^h - 2 \ge 2 \implies 2^h \ge 4 \implies h = 2 \text{ bits host}$$
* **Độ dài Prefix**:
  $$p = 32 - h = 32 - 2 = /30$$
* **Subnet Mask**:
  $$/30 = 11111111.11111111.11111111.11111100_2 = \mathbf{255.255.255.252}$$
* **Bước nhảy (Block Size)**:
  $$256 - 252 = 4$$
* **Dải mạng gán**: `6.9.6.8 /30`
  * Network ID: `6.9.6.8`
  * IP đầu (gán R1 Serial1/0): `6.9.6.9`
  * IP cuối (gán R2 Serial1/0): `6.9.6.10`
  * Broadcast ID: `6.9.6.11`
  * Wildcard Mask (dùng cho OSPF/EIGRP):
    $$255.255.255.255 - 255.255.255.252 = \mathbf{0.0.0.3}$$

#### 2. Mạng Loopback giả lập LAN nội bộ
* **LAN R1 (Loopback0)**: `192.168.1.0 /24`
  * Subnet Mask: `255.255.255.0`
  * IP gán: `192.168.1.1`
  * Wildcard Mask: `0.0.0.255`
* **LAN R2 (Loopback0)**: `192.168.2.0 /24`
  * Subnet Mask: `255.255.255.0`
  * IP gán: `192.168.2.1`
  * Wildcard Mask: `0.0.0.255`

---

### [PHẦN 2] THIẾT KẾ THAM SỐ MẬT MÃ XÁC THỰC (MD5 AUTHENTICATION)

```
                       CƠ CHẾ BẢO MẬT HMAC-MD5 (16 BYTES)
  Packet Data ──┐
  Secret Key  ──┼──> [ Thuật toán MD5 ] ──> Digest: 128-bit (16 Bytes) ──> Gắn vào Trailer/Header
  Seq Number  ──┘                                                          (Không lộ mật khẩu!)
```

* **Mật khẩu dùng chung (Pre-shared Key)**: `MatKhau123` (Độ dài: 10 ký tự = 80 bits).
* **Key ID**: `1` (Khớp tuyệt đối giữa hai Router).
* **Key-chain**: `CAY_KHOA`.

#### Bảng so sánh kỹ thuật gói tin xác thực trong Wireshark:
| Đặc tính kỹ thuật | RIPv2 (RFC 2082) | OSPFv2 (RFC 2328) | EIGRP (RFC 7868) |
|:---|:---|:---|:---|
| **Cổng / Protocol ID** | UDP Port 520 | Protocol Number 89 | Protocol Number 88 |
| **Địa chỉ Multicast** | `224.0.0.9` | `224.0.0.5` | `224.0.0.10` |
| **Loại xác thực MD5** | Type = 3 (Keyed Digest) | Type = 2 (Cryptographic) | Type = 2 (Auth TLV 0x0002) |
| **Vị trí lưu mã băm** | Authentication Trailer (cuối gói tin) | OSPF Packet Header (cuối header) | Authentication TLV Data |
| **Độ dài mã băm MD5** | 16 bytes (128 bits) | 16 bytes (128 bits) | 16 bytes (128 bits) |
| **Chống Replay Attack**| Sequence Number 4 bytes | Cryptographic Sequence Number 4 bytes | Key Sequence Number |

---

### [PHẦN 3] BẢNG LỆNH CỐT LÕI (BẢN TÓM TẮT ĐỂ CẤU HÌNH NHANH TRONG PHÒNG THI)

```cisco
! ======================== CẤU HÌNH R1 (DCE) ========================
hostname R1
key chain CAY_KHOA
 key 1
  key-string MatKhau123

interface Loopback0
 ip address 192.168.1.1 255.255.255.0

interface Serial1/0
 ip address 6.9.6.9 255.255.255.252
 clock rate 2016000
 ! RIP MD5:
 ip rip authentication mode md5
 ip rip authentication key-chain CAY_KHOA
 ! OSPF MD5:
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 MatKhau123
 ! EIGRP MD5:
 ip authentication mode eigrp 100 md5
 ip authentication key-chain eigrp 100 CAY_KHOA
 no shutdown

router rip
 version 2
 network 6.0.0.0
 network 192.168.1.0
 no auto-summary

router ospf 1
 router-id 192.168.1.1
 network 6.9.6.8 0.0.0.3 area 0
 network 192.168.1.0 0.0.0.255 area 0

router eigrp 100
 network 6.9.6.8 0.0.0.3
 network 192.168.1.0
 no auto-summary
```

```cisco
! ======================== CẤU HÌNH R2 (DTE) ========================
hostname R2
key chain CAY_KHOA
 key 1
  key-string MatKhau123

interface Loopback0
 ip address 192.168.2.1 255.255.255.0

interface Serial1/0
 ip address 6.9.6.10 255.255.255.252
 ! RIP MD5:
 ip rip authentication mode md5
 ip rip authentication key-chain CAY_KHOA
 ! OSPF MD5:
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 MatKhau123
 ! EIGRP MD5:
 ip authentication mode eigrp 100 md5
 ip authentication key-chain eigrp 100 CAY_KHOA
 no shutdown

router rip
 version 2
 network 6.0.0.0
 network 192.168.2.0
 no auto-summary

router ospf 1
 router-id 192.168.2.1
 network 6.9.6.8 0.0.0.3 area 0
 network 192.168.2.0 0.0.255.255 area 0

router eigrp 100
 network 6.9.6.8 0.0.0.3
 network 192.168.2.0
 no auto-summary
```
