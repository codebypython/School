# 🧪 HƯỚNG DẪN THAO TÁC KIỂM TRA CHI TIẾT LAB 2
**Học phần**: An Toàn Mạng (CORP-04-SEC - DUT)  
**Nội dung**: Quy trình kiểm tra định tuyến 6 Subnet VLSM và giám sát xác thực PPP CHAP  

---

## 📋 MỤC TIÊU KIỂM TRA (THEO YÊU CẦU THẦY LÝ)
1. **Kiểm tra tiêu chuẩn 1**: Gõ `show ip route` trên từng Router, hiển thị đầy đủ đúng **6 mạng con (Subnets)** theo chuẩn VLSM.
2. **Kiểm tra tiêu chuẩn 2**: Mở các tệp bắt gói tin `.pcapng` của Wireshark, lọc từ khóa `ppp` hoặc `chap`, hiển thị các gói tin xác thực CHAP mang giá trị Hash MD5.
3. **Kiểm tra kết nối toàn diện**: Ping thành công giữa các Router và giữa các mạng LAN.

---

## 🛠️ CÁC BƯỚC THAO TÁC TRÊN CISCO IOS CLI

### Bước 1: Kiểm tra Bảng Định Tuyến Đủ 6 Subnets
Trên Router VN, gõ lệnh:
```cisco
VN# show ip route
```
*Kết quả hiển thị bắt buộc phải đủ 6 mạng con*:
```text
Gateway of last resort is not set

     172.16.0.0/16 is variably subnetted, 6 subnets, 4 masks
C       172.16.0.0/19 is directly connected, FastEthernet0/0
R       172.16.32.0/20 [120/1] via 172.16.56.2, 00:00:18, Serial1/0
R       172.16.48.0/21 [120/1] via 172.16.56.9, 00:00:22, Serial1/1
C       172.16.56.0/30 is directly connected, Serial1/0
R       172.16.56.4/30 [120/1] via 172.16.56.2, 00:00:18, Serial1/0
                       [120/1] via 172.16.56.9, 00:00:22, Serial1/1
C       172.16.56.8/30 is directly connected, Serial1/1
```
> ✅ **ĐÁNH GIÁ ĐẠT 10/10**: Đủ 6 subnets với 4 loại masks (`/19`, `/20`, `/21`, `/30`).

---

### Bước 2: Kiểm tra Đóng gói PPP và Trạng thái CHAP trên Interface
Trên Router VN, kiểm tra cổng `Serial1/0`:
```cisco
VN# show interfaces serial1/0
```
*Kết quả mong đợi*:
```text
Serial1/0 is up, line protocol is up 
  Hardware is M4T
  Internet address is 172.16.56.1/30
  Encapsulation PPP, LCP Open                           <--- PPP LCP đã mở
  Open: IPCP                                            <--- Giao thức mạng IPCP đã đàm phán xong
  Keepalive set (10 sec)
```

---

### Bước 3: Kiểm tra Kết nối Thông tuyến (Ping End-to-End)
Từ Router VN, thực hiện ping đến các Gateway mạng LAN của Lào và Campuchia:
```cisco
VN# ping 172.16.32.1 source fastEthernet 0/0
!!!!!
Success rate is 100 percent (5/5)

VN# ping 172.16.48.1 source fastEthernet 0/0
!!!!!
Success rate is 100 percent (5/5)
```

---

### Bước 4: Giám sát Quá trình Xác thực CHAP bằng Lệnh Debug
Bật tính năng debug trên Router VN:
```cisco
VN# debug ppp authentication
PPP authentication debugging is on
VN# debug ppp negotiation
PPP protocol negotiation debugging is on
```
Ngắt và bật lại cổng `Serial1/0` để kích hoạt lại đàm phán PPP:
```cisco
VN(config)# interface serial1/0
VN(config-if)# shutdown
VN(config-if)# no shutdown
```
*Console Router sẽ in chi tiết 3 bước bắt tay*:
```text
*Mar  1 00:12:05.123: Se1/0 PPP: Using default id 1
*Mar  1 00:12:05.123: Se1/0 PPP: Treating connection as a dedicated line
*Mar  1 00:12:05.127: Se1/0 PPP: Phase is AUTHENTICATING, by this end
*Mar  1 00:12:05.131: Se1/0 CHAP: O CHALLENGE id 1 len 23 from "VN"
*Mar  1 00:12:05.143: Se1/0 CHAP: I CHALLENGE id 1 len 24 from "LAO"
*Mar  1 00:12:05.147: Se1/0 CHAP: O RESPONSE id 1 len 23 from "VN"
*Mar  1 00:12:05.155: Se1/0 CHAP: I RESPONSE id 1 len 24 from "LAO"
*Mar  1 00:12:05.159: Se1/0 CHAP: O SUCCESS id 1 len 4
*Mar  1 00:12:05.163: Se1/0 CHAP: I SUCCESS id 1 len 4
*Mar  1 00:12:05.167: Se1/0 PPP: Phase is FORWARDING, plugin UP
```
> Tắt debug sau khi hoàn tất: `VN# undebug all`

---

## ⚠️ LỖI PHỔ BIẾN SINH VIÊN HAY GẶP
1. **Lệch Hostname và Username**: Ví dụ Router có `hostname LAO` nhưng trên Router VN lại khai `username lao` (chữ thường) hoặc `username Laos`. Cisco IOS phân biệt hoa/thường (Case-sensitive) đối với username trong CHAP $\rightarrow$ Báo lỗi `CHAP authentication failed`.
2. **Sai Clock Rate trên đầu nối DCE**: Cáp Serial kết nối trực tiếp trong bài lab cần 1 đầu làm DCE phát xung nhịp (`clock rate 2016000`). Nếu cả 2 đầu đều là DTE hoặc quên lệnh `clock rate` thì interface sẽ ở trạng thái `down/down`.

---

## 💡 CÂU HỎI GỢI MỞ / MICRO-QUIZ
**Câu hỏi**: *Trong giao thức PPP CHAP (Challenge Handshake Authentication Protocol), vì sao CHAP lại an toàn hơn PAP (Password Authentication Protocol) gấp nhiều lần khi truyền tải qua môi trường WAN công cộng?*
- A) Vì CHAP sử dụng thuật toán mã hóa khóa công khai RSA-2048 để mã hóa toàn bộ dữ liệu người dùng.
- B) Vì mật khẩu gốc (Shared Secret) không bao giờ được truyền qua đường dây cáp mạng; bên xác thực gửi chuỗi ngẫu nhiên (Challenge) và bên được xác thực chỉ gửi lại giá trị băm `MD5(ID + Secret + Challenge)` kèm tên định danh.
- C) Vì CHAP tự động đổi địa chỉ IP của Router mỗi 30 giây để tránh bị theo dõi.
- D) Vì CHAP chỉ hoạt động trên đường truyền cáp quang bảo mật cao.
*(Đáp án đúng: **B**)*

