# 🔍 HƯỚNG DẪN THAO TÁC KIỂM TRA & PHÂN TÍCH WIRESHARK PCAPNG (LAB 2)
**Học phần**: An Toàn Mạng (CORP-04-SEC - DUT)  
**Tài nguyên kiểm tra**: Các tệp `VN-LAO.pcapng`, `LAO-CAM.pcapng`, `VN-CAM.pcapng` (lưu tại thư mục `Day2 - PPP/`)  

---

## 🎯 MỤC ĐÍCH PHÂN TÍCH
Chứng minh trên thực tế dòng lưu lượng mạng:
1. Giao thức PPP đàm phán Link Control Protocol (LCP) thành công.
2. Chu trình bắt tay 3 bước của CHAP (Challenge Handshake Authentication Protocol):
   - **Code 1 (Challenge)**: Gửi số ngẫu nhiên 16 bytes.
   - **Code 2 (Response)**: Gửi chuỗi băm MD5 16 bytes.
   - **Code 3 (Success)**: Phê chuẩn kết nối.
3. Không hề có mật khẩu `Sinch@u` xuất hiện trong bất kỳ trường dữ liệu nào của gói tin.

---

## 🔬 PHÂN TÍCH CHI TIẾT TỆP TIN `VN-LAO.pcapng`

Khởi động Wireshark, mở tệp `Day2 - PPP/VN-LAO.pcapng`.

### 1. Bộ lọc hiển thị (Display Filter)
Gõ vào ô filter trên cùng:
```text
chap
```
*(Nếu muốn xem toàn bộ đàm phán PPP LCP và IPCP, gõ `ppp`)*

---

### 2. Phân tích Chuỗi Gói Tin Bắt Tay CHAP

```
  Frame 10 (LAO -> VN) : CHAP Challenge (Code 1, Name='LAO')
  Frame 11 (VN -> LAO) : CHAP Challenge (Code 1, Name='VN')
  Frame 12 (VN -> LAO) : CHAP Response  (Code 2, Name='VN', Hash MD5)
  Frame 13 (LAO -> VN) : CHAP Response  (Code 2, Name='LAO', Hash MD5)
  Frame 14 (LAO -> VN) : CHAP Success   (Code 3)
  Frame 15 (VN -> LAO) : CHAP Success   (Code 3)
```

#### A. Gói tin số 10 (Frame 10): Router LAO gửi Thử Thách (Challenge)
* Mở rộng `Point-to-Point Protocol` $\rightarrow$ `PPP Challenge Handshake Authentication Protocol`:
  ```text
  PPP Challenge Handshake Authentication Protocol
      Code: Challenge (1)                  <--- Code 1: Thử thách
      Identifier: 1                        <--- Phiên ID 1
      Length: 24 bytes
      Data
          Value Size: 16
          Value: 25a74b8c93ac4ac5519c1209a8f86333  <--- Chuỗi số ngẫu nhiên Challenge R
          Name: LAO                                 <--- Tên định danh của LAO
  ```
  > LAO yêu cầu: *"Tôi là LAO. Đây là số ngẫu nhiên $R$ của tôi. Hãy dùng mật khẩu bí mật của bạn để băm nó lại và gửi trả cho tôi!"*

#### B. Gói tin số 12 (Frame 12): Router VN gửi Phản Hồi (Response)
* Mở rộng `PPP Challenge Handshake Authentication Protocol`:
  ```text
  PPP Challenge Handshake Authentication Protocol
      Code: Response (2)                   <--- Code 2: Phản hồi
      Identifier: 1                        <--- Khớp với Identifier của Challenge
      Length: 23 bytes
      Data
          Value Size: 16
          Value: c1f330fed4a61786efce812adee89d0e  <--- Giá trị băm MD5
          Name: VN                                  <--- Định danh Router VN
  ```
* **Minh chứng công thức tính toán**:
  $$\text{Value} = \text{MD5}(0x01 \parallel \text{"Sinch@u"} \parallel 0x25a74b8c93ac4ac5519c1209a8f86333) = \mathbf{c1f330fed4a61786efce812adee89d0e}$$

#### C. Gói tin số 14 (Frame 14): Router LAO gửi Thông Báo Thành Công (Success)
* Mở rộng `PPP Challenge Handshake Authentication Protocol`:
  ```text
  PPP Challenge Handshake Authentication Protocol
      Code: Success (3)                    <--- Code 3: Xác thực thành công!
      Identifier: 1
      Length: 4 bytes
  ```
  > LAO tính toán trong bộ nhớ thấy mã băm khớp 100% $\rightarrow$ Chấp thuận cho phép VN kết nối, mở tiếp tầng Network Control Protocol (IPCP) để truyền dữ liệu IP.

---

## 🔬 KIỂM TRA ĐỐI CHIẾU TRÊN CÁC TUYẾN CÒN LẠI
1. Mở `LAO-CAM.pcapng` $\rightarrow$ Filter `chap` $\rightarrow$ Thấy quá trình bắt tay đối ứng giữa `LAO` và `CAM`.
2. Mở `VN-CAM.pcapng` $\rightarrow$ Filter `chap` $\rightarrow$ Thấy quá trình bắt tay đối ứng giữa `VN` và `CAM`.

> **KẾT LUẬN NGHIỆM THU**: Toàn bộ mạng WAN tam giác 3 quốc gia đạt chuẩn bảo mật kênh truyền PPP CHAP, chống nghe lén mật khẩu và chống tấn công phát lại.
