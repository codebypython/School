# 🔍 HƯỚNG DẪN THAO TÁC KIỂM TRA & PHÂN TÍCH WIRESHARK PCAPNG (LAB 1)
**Học phần**: An Toàn Mạng (CORP-04-SEC - DUT)  
**Tài nguyên kiểm tra**: Các tệp `rip.pcapng`, `ospf.pcapng`, `eigrp.pcapng` (lưu tại thư mục `Day1/`)  

---

## 🎯 MỤC ĐÍCH PHÂN TÍCH
Chỉ ra trên thực tế bắt gói tin (Packet Capture):
1. Sự nguy hiểm của chế độ Simple Password (lộ mật khẩu rõ 100%).
2. Cấu trúc trường xác thực băm Cryptographic MD5 trong OSPF, EIGRP và RIPv2.
3. Cơ chế bảo vệ toàn vẹn và chống phát lại (Replay Attack) bằng Sequence Number.

---

## 🔬 PHẦN 1: PHÂN TÍCH TỆP TIN `rip.pcapng`

Khởi động Wireshark, mở tệp `Day1/rip.pcapng`.

### 1.1. Bộ lọc hiển thị (Display Filter)
```text
rip
```

### 1.2. Phân tích đối chiếu giữa 2 chế độ xác thực
Trong file `rip.pcapng`, ta quan sát thấy quá trình chuyển đổi cấu hình từ Plaintext sang MD5:

#### A. Gói tin số 2 (Frame 2): Xác thực Văn bản rõ (Simple Password)
* **Thời gian**: `1.299177s` | Nguồn: `6.9.6.10` | Đích: `224.0.0.9` (Multicast RIP)
* Mở rộng cây giao thức `Routing Information Protocol`:
  ```text
  Routing Information Protocol
      Command: Response (2)
      Version: RIPv2 (2)
      Authentication: Simple Password
          Authentication type: Simple Password (2)
          Password: MatKhau123      <--- NGUY HIỂM: Lộ rõ hoàn toàn mật khẩu!
      IP Address: 192.168.2.0, Metric: 1
  ```
  > **Đánh giá bảo mật**: Bất kỳ ai cắm máy tính vào switch hoặc lắng nghe trên đường truyền đều đọc được mật khẩu `MatKhau123` mà không cần giải mã.

#### B. Gói tin số 66 (Frame 66): Xác thực Băm Mật Mã MD5 (Keyed Message Digest)
* **Thời gian**: `156.402120s` | Nguồn: `6.9.6.10` | Đích: `224.0.0.9`
* Mở rộng cây giao thức `Routing Information Protocol`:
  ```text
  Routing Information Protocol
      Command: Response (2)
      Version: RIPv2 (2)
      Authentication: Keyed Message Digest
          Authentication type: Keyed Message Digest (3)
          Digest Offset: 44
          Key ID: 1                     <--- Khớp với cấu hình key 1
          Auth Data Len: 20
          Seq num: 0                    <--- Sequence chống Replay Attack
          Authentication Data Trailer
              Authentication Data: faa9a008741fcb8e61cd4e0287b28140  <--- Chuỗi băm 16 bytes MD5
  ```
  > **Đánh giá bảo mật**: Mật khẩu `MatKhau123` đã được thay thế bằng mã băm MD5 `faa9a008...`. Kẻ tấn công không thể suy ngược lại mật khẩu gốc.

---

## 🔬 PHẦN 2: PHÂN TÍCH TỆP TIN `ospf.pcapng`

Mở tệp `Day1/ospf.pcapng`.

### 2.1. Bộ lọc hiển thị
```text
ospf && ospf.auth.type == 2
```

### 2.2. Phân tích Gói tin số 1 (Frame 1 - OSPF Hello)
* Nguồn: `6.9.6.10` (R2) | Đích: `224.0.0.5` (AllSPFRouters) | Protocol: `89 (OSPF)`
* Mở rộng phần `Open Shortest Path First` $\rightarrow$ `OSPF Header`:
  ```text
  Open Shortest Path First
      OSPF Header
          Version: 2
          Message Type: Hello Packet (1)
          Source OSPF Router: 192.168.2.1
          Area ID: 0.0.0.0 (Backbone)
          Auth Type: Cryptographic (2)        <--- Type 2: MD5 Cryptographic
          Auth Crypt Key id: 1                <--- Key ID 1
          Auth Crypt Data Length: 16          <--- Độ dài Digest đúng chuẩn 16 bytes MD5
          Auth Crypt Sequence Number: 1014940905 <--- Tăng liên tục để chống Replay Attack
          Auth Crypt Data: ec35ba752e6e36f3f20384c436c56153 <--- Giá trị băm HMAC-MD5
  ```
  > **Đặc điểm OSPF**: Giá trị băm được đặt trực tiếp trong Header của OSPF. Nếu gói tin bị can thiệp sửa đổi nội dung trên đường truyền, Router nhận sẽ tính toán lại mã băm và phát hiện không khớp $\rightarrow$ Drop gói tin ngay lập tức.

---

## 🔬 PHẦN 3: PHÂN TÍCH TỆP TIN `eigrp.pcapng`

Mở tệp `Day1/eigrp.pcapng`.

### 3.1. Bộ lọc hiển thị
```text
eigrp
```

### 3.2. Phân tích Gói tin số 1 & 2 (Frame 1 - EIGRP Hello)
* Nguồn: `6.9.6.10` | Đích: `224.0.0.10` (AllEIGRPRouters) | Protocol: `88 (EIGRP)`
* Mở rộng cây giao thức `Cisco EIGRP`:
  ```text
  Cisco EIGRP
      Version: 2
      Opcode: Hello (5)
      Autonomous System: 100                  <--- AS Number 100
      Authentication MD5
          Type: Authentication (0x0002)       <--- TLV Type 0x0002
          Length: 40 bytes
          Type: MD5 (2)                       <--- Thuật toán MD5
          Length: 16 bytes                    <--- Chuỗi băm 16 bytes
          Key ID: 1                           <--- Khớp với Key ID cấu hình
          Key Sequence: 0
          Nullpad: 0000000000000000
          Digest: 0e3732c514881ae278f1fe6f4125051e <--- Giá trị băm MD5 duy nhất cho gói này
  ```
  > **Ý nghĩa thực tế**: EIGRP đóng gói phần xác thực theo cấu trúc TLV (Type-Length-Value). Khi bắt được gói tin này trên Wireshark, sinh viên chứng minh được 100% hệ thống EIGRP đã được bảo vệ bằng mật mã học ứng dụng.
