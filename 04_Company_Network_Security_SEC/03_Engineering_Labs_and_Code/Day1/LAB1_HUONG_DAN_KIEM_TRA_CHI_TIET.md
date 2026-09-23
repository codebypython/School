# 🧪 HƯỚNG DẪN THAO TÁC KIỂM TRA CHI TIẾT LAB 1
**Học phần**: An Toàn Mạng (CORP-04-SEC - DUT)  
**Nội dung**: Quy trình kiểm tra định tuyến và xác thực mật mã MD5 trên Cisco IOS  

---

## 📋 MỤC TIÊU KIỂM TRA
1. Kiểm tra bảng định tuyến `show ip route` đã học được mạng Loopback của nhau.
2. Kiểm tra trạng thái thiết lập hàng xóm (Neighbor Adjacency) của OSPF và EIGRP.
3. Kiểm tra tính năng xác thực MD5 đang hoạt động trên interface.
4. Thử nghiệm phản chứng (Negative Testing): Cố tình đổi sai mật khẩu để chứng minh quan hệ láng giềng bị ngắt kết nối ngay lập tức.

---

## 🛠️ CÁC BƯỚC THAO TÁC TRÊN CISCO IOS CLI

### Bước 1: Kiểm tra kết nối vật lý Layer 1/2 và IP Interface
Trên cả R1 và R2:
```cisco
R1# show ip interface brief
```
*Kết quả mong đợi*:
```text
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            unassigned      YES manual administratively down down    
Serial1/0                  6.9.6.9         YES manual up                    up      
Loopback0                  192.168.1.1     YES manual up                    up      
```
> Trạng thái `Serial1/0` bắt buộc phải là **`up/up`**.

---

### Bước 2: Kiểm tra Bảng Định Tuyến (Routing Table)
Trên R1, gõ lệnh:
```cisco
R1# show ip route
```
*Kết quả mong đợi*: R1 phải học được mạng `192.168.2.0/24` từ R2 qua một trong các giao thức (R: RIP, O: OSPF, D: EIGRP):
```text
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 

Gateway of last resort is not set

     6.0.0.0/30 is subnetted, 1 subnets
C       6.9.6.8 is directly connected, Serial1/0
C    192.168.1.0/24 is directly connected, Loopback0
O    192.168.2.0/24 [110/65] via 6.9.6.10, 00:04:12, Serial1/0
```
> Gõ lệnh ping kiểm tra từ R1 sang Loopback R2:
```cisco
R1# ping 192.168.2.1 source loopback 0
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 20/28/44 ms
```

---

### Bước 3: Kiểm tra Xác Thực OSPF MD5
1. Kiểm tra láng giềng OSPF:
```cisco
R1# show ip ospf neighbor
```
*Kết quả mong đợi*:
```text
Neighbor ID     Pri   State           Dead Time   Address         Interface
192.168.2.1       0   FULL/  -        00:00:34    6.9.6.10        Serial1/0
```
> Trạng thái trên cổng Serial điểm - điểm (Point-to-Point) phải là **`FULL/ -`**.

2. Kiểm tra chi tiết xác thực trên Interface:
```cisco
R1# show ip ospf interface serial1/0
```
*Kết quả mong đợi (chú ý 2 dòng cuối)*:
```text
Serial1/0 is up, line protocol is up 
  Internet Address 6.9.6.9/30, Area 0 
  Process ID 1, Router ID 192.168.1.1, Network Type POINT_TO_POINT, Cost: 64
  Transmit Delay is 1 sec, State POINT_TO_POINT
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    Hello due in 00:00:03
  Message digest authentication enabled
    Youngest key id is 1
```

---

### Bước 4: Kiểm tra Xác Thực EIGRP MD5
1. Kiểm tra hàng xóm EIGRP:
```cisco
R1# show ip eigrp neighbors
```
*Kết quả mong đợi*:
```text
IP-EIGRP neighbors for process 100
H   Address                 Interface       Hold Uptime   SRTT   RTO  Q   Seq
                                            (sec)         (ms)       Cnt  Num
0   6.9.6.10                Se1/0             12 00:08:15   24   200  0   4
```

---

### Bước 5: Thử Nghiệm Phản Chứng (Fault Injection / Negative Test)
Để chứng minh cơ chế xác thực MD5 thực sự bảo vệ mạng, ta cố tình đổi sai mật khẩu trên R2:
```cisco
R2(config)# key chain CAY_KHOA
R2(config-keychain)# key 1
R2(config-keychain-key)# key-string MatKhauSaiRoi!!!
```
Bật debug trên R1 để quan sát phản ứng của Router:
```cisco
R1# debug ip ospf adj
OSPF adjacency events debugging is on

R1# debug eigrp packets
EIGRP Packet debugging is on
```
*Hiện tượng xảy ra*:
1. Router R1 in log từ chối gói tin ngay lập tức:
   ```text
   %OSPF-5-ADJCHG: Process 1, Nbr 192.168.2.1 on Serial1/0 from FULL to DOWN, Neighbor Down: Dead timer expired
   EIGRP: Serial1/0: ignored packet from 6.9.6.10, opcode = 5 (authentication failure)
   ```
2. Kiểm tra `show ip route` trên R1: Tuyến đường `192.168.2.0/24` bị xóa khỏi bảng định tuyến ngay lập tức!
3. Khôi phục lại đúng mật khẩu `MatKhau123` trên R2 $\rightarrow$ Adjacency khôi phục lại trạng thái `FULL` sau 10 giây.

---

## ⚠️ LỖI PHỔ BIẾN SINH VIÊN HAY GẶP
1. **Lệch Key ID**: R1 cấu hình `key 1` nhưng R2 cấu hình `key 2`. Hai Router dù có chung password vẫn không bắt tay được vì giá trị Key ID trong gói tin gửi đi không khớp.
2. **Quên lệnh `ip ospf authentication message-digest`**: Đã gõ lệnh `message-digest-key 1 md5 ...` nhưng quên lệnh kích hoạt `authentication message-digest` trên interface khiến OSPF vẫn chạy ở chế độ Null (không xác thực).
3. **Chưa no auto-summary trên RIP/EIGRP**: Khiến các mạng con bị gộp về classful network `192.168.0.0/16`.

---

## 💡 CÂU HỎI GỢI MỞ / MICRO-QUIZ
**Câu hỏi**: *Trong cơ chế xác thực OSPFv2 Cryptographic Authentication (MD5), tại sao trường Sequence Number (Mã số tuần tự) trong OSPF Header lại có vai trò sống còn bên cạnh giá trị băm MD5 Digest 16-byte?*
- A) Để mã hóa toàn bộ dữ liệu gói tin định tuyến OSPF.
- B) Để Router nhận biết và hủy bỏ các gói tin cũ bị kẻ tấn công bắt lại rồi phát lại (Anti-Replay Protection); nếu gói tin mới có Sequence Number nhỏ hơn hoặc bằng giá trị đã nhận trước đó, Router sẽ loại bỏ ngay lập tức.
- C) Để thông báo cho Router láng giềng biết số lượng mạng con (subnets) có trong bảng định tuyến.
- D) Sequence Number chỉ dùng để tính toán thời gian trễ Round-Trip Time (RTT).
*(Đáp án đúng: **B**)*

