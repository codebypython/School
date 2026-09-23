# 🔍 HƯỚNG DẪN THAO TÁC KIỂM TRA & PHÂN TÍCH WIRESHARK PCAPNG (LAB 3)
**Học phần**: An Toàn Mạng (CORP-04-SEC - DUT)  
**Tài nguyên kiểm tra**: Tệp `lab3_extended_acl_traffic.pcapng` (lưu tại thư mục `Day3 - ACL/`)  

---

## 🎯 MỤC ĐÍCH PHÂN TÍCH
Chứng minh trên thực tế dòng gói tin:
1. Lưu lượng FTP qua cổng TCP 21 được chấp thuận hoàn toàn: Quá trình bắt tay 3 bước (SYN, SYN-ACK, ACK) và truyền chuỗi lệnh `USER`, `PASS`, mã kết quả `230 User logged in`.
2. Lưu lượng HTTP cố gắng kết nối tới cổng TCP 80 bị Router chặn lại và gửi trả bản tin `ICMP Destination Unreachable (Communication administratively filtered)`.
3. Lưu lượng Ping (ICMP Echo Request) bị Router từ chối và chặn đứng.

---

## 🔬 PHÂN TÍCH CHI TIẾT TỆP TIN `lab3_extended_acl_traffic.pcapng`

Khởi động Wireshark, mở tệp `Day3 - ACL/lab3_extended_acl_traffic.pcapng`.

### 1. Phân tích Luồng Dịch Vụ FTP (Được Cho Phép - PERMIT)
#### A. Bộ lọc hiển thị (Display Filter)
```text
tcp.port == 21 || ftp
```

#### B. Trình tự gói tin quan sát được
| Gói tin (Frame) | Nguồn | Đích | Giao thức | Phân tích chi tiết |
|:---:|:---:|:---:|:---:|:---|
| **1** | `10.10.2.2` | `10.10.3.2` | TCP | `49152 -> 21 [SYN] Seq=0` (Client khởi tạo kết nối) |
| **2** | `10.10.3.2` | `10.10.2.2` | TCP | `21 -> 49152 [SYN, ACK] Seq=0 Ack=1` (Server đồng ý) |
| **3** | `10.10.2.2` | `10.10.3.2` | TCP | `49152 -> 21 [ACK] Seq=1 Ack=1` (Hoàn tất 3-way handshake) |
| **4** | `10.10.3.2` | `10.10.2.2` | FTP | `Response: 220 Microsoft FTP Service` (Server chào đón) |
| **5** | `10.10.2.2` | `10.10.3.2` | FTP | `Request: USER Administrator` (Gửi tên đăng nhập) |
| **6** | `10.10.3.2` | `10.10.2.2` | FTP | `Response: 331 Password required for Administrator.` |
| **7** | `10.10.2.2` | `10.10.3.2` | FTP | `Request: PASS 123qwe!@#` (Gửi mật khẩu) |
| **8** | `10.10.3.2` | `10.10.2.2` | FTP | **`Response: 230 User logged in.`** (Đăng nhập thành công!) |

> Dòng lệnh khớp: `access-list 102 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp`

---

### 2. Phân tích Luồng Dịch Vụ Web HTTP (Bị Chặn - DENY)
#### A. Bộ lọc hiển thị
```text
tcp.port == 80 || (icmp && ip.src == 10.10.2.1)
```

#### B. Phân tích gói tin số 9 và 10
* **Gói 9 (Frame 9)**: `10.10.2.2` gửi gói `TCP SYN` đến `10.10.3.2` trên cổng `80` (yêu cầu mở trang Web).
* **Gói 10 (Frame 10)**: Router West (`10.10.2.1`) chặn gói tin và gửi trả về `10.10.2.2`:
  ```text
  Internet Control Message Protocol
      Type: 3 (Destination unreachable)
      Code: 13 (Communication administratively filtered)   <--- BỊ CHẶN BỞI ACL!
  ```
  > `Code 13` là mã chuẩn quốc tế của ICMP chỉ ra rằng gói tin bị từ chối bởi cơ chế lọc tường lửa / danh sách kiểm soát truy cập (Access List).

---

### 3. Phân tích Luồng Gói Tin Ping ICMP (Bị Chặn - DENY)
#### A. Bộ lọc hiển thị
```text
icmp
```

#### B. Phân tích gói tin số 11 và 12
* **Gói 11 (Frame 11)**: `10.10.2.2` gửi gói tin `ICMP Echo Request (Type 8, Code 0)`.
* **Gói 12 (Frame 12)**: Router West (`10.10.2.1`) gửi trả ngay:
  ```text
  Internet Control Message Protocol
      Type: 3 (Destination unreachable)
      Code: 13 (Communication administratively filtered)
  ```
  > Gói tin Ping không bao giờ đến được Server LAN 3 vì đã bị Router West hủy bỏ ngay tại cổng `FastEthernet0/0` (Inbound).

> **KẾT LUẬN NGHIỆM THU**: Tệp tin `lab3_extended_acl_traffic.pcapng` cung cấp đầy đủ bằng chứng kiểm định số liệu thực tế, thỏa mãn 100% tiêu chí chấm điểm của học phần An Toàn Mạng DUT.
