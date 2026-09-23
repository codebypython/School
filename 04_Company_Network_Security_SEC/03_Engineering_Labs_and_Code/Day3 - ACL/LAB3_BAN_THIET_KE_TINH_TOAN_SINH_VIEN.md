# 📝 BẢN THIẾT KẾ & TÍNH TOÁN KỸ THUẬT (NHÁP TAY SINH VIÊN BÁCH KHOA)
**Học phần**: An Toàn Mạng & Mật Mã Học Ứng Dụng (CORP-04-SEC - DUT)  
**Bài thực hành**: Lab 3 - Danh Sách Kiểm Soát Truy Cập Mở Rộng (Extended ACL FTP/HTTP/Ping)  
**Người thực hiện**: Sinh viên Khoa CNTT - ĐHBK Đà Nẵng  

---

### [PHẦN 1] TÍNH TOÁN WILDCARD MASK (MẶT NẠ ĐẢO)

* **Công thức chuẩn**:
  $$\text{Wildcard Mask} = 255.255.255.255 - \text{Subnet Mask}$$

1. **Mạng LAN 2**: `10.10.2.0 /24`
   * Subnet Mask: `255.255.255.0`
   * Phép trừ từng octet:
     $$\begin{matrix} 255 & . & 255 & . & 255 & . & 255 \\ - & & & & & & \\ 255 & . & 255 & . & 255 & . & 0 \\ \hline \mathbf{0} & . & \mathbf{0} & . & \mathbf{0} & . & \mathbf{255} \end{matrix}$$
   * $\implies$ Wildcard Mask: `0.0.0.255` (Ý nghĩa: 3 octet đầu phải khớp chính xác tuyệt đối, octet cuối tùy ý từ 0-255).

2. **Mạng LAN 3**: `10.10.3.0 /24`
   * Subnet Mask: `255.255.255.0`
   * $\implies$ Wildcard Mask: `0.0.0.255`

---

### [PHẦN 2] BIỆN LUẬN VỊ TRÍ ĐẶT ACL & CHIỀU LỌC (INBOUND vs OUTBOUND)

```
        LAN 2                     ROUTER WEST                      ROUTER GATEWAY
 [Server 10.10.2.2] ────> (Fa0/0 [IN] ────> S1/0 [OUT]) ────────> (S1/0 ────> ...)
                            │
               VỊ TRÍ TỐI ƯU NHẤT: Fa0/0 INBOUND!
               - Lọc gói tin ngay khi vừa chạm vào Router.
               - Gói tin bị drop ngay, không tiêu tốn tài nguyên định tuyến CPU và băng thông WAN.
```

* **Quy tắc vàng môn Mạng máy tính**:
  * Standard ACL (chỉ lọc IP nguồn): Đặt **càng gần đích càng tốt** (để tránh chặn nhầm đường đi tới các đích khác).
  * **Extended ACL** (lọc cả nguồn, đích, port): Đặt **CÀNG GẦN NGUỒN CÀNG TỐT** (để tiêu diệt gói tin rác ngay tại biên mạng!).
* **Lựa chọn thi công**:
  * Lưu lượng từ LAN 2 sang LAN 3: Đặt trên **Router West**, cổng `FastEthernet0/0`, chiều **`IN`**.
  * Lưu lượng từ LAN 3 sang LAN 2: Đặt trên **Router East**, cổng `FastEthernet0/0`, chiều **`IN`**.

---

### [PHẦN 3] GIẢI BÀI TOÁN GIAO THỨC FTP & CƠ CHẾ 2 KÊNH (ACTIVE vs PASSIVE)

Giao thức FTP (RFC 959) rất đặc biệt vì sử dụng **2 kết nối TCP đồng thời**:
1. **Kênh điều khiển (Control Connection)**:
   * Client mở port ngẫu nhiên $N \ge 1024 \rightarrow$ Server TCP port `21`.
   * Gửi lệnh: `USER`, `PASS`, `LIST`, `RETR`...
   * Cần dòng lệnh: `permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp`
2. **Kênh dữ liệu (Data Connection - Active FTP)**:
   * Khi truyền danh sách file (`dir`) hoặc tải file (`get`), Server khởi tạo kết nối từ TCP port `20` về Client port $N+1$.
   * Cần dòng lệnh: `permit tcp 10.10.2.0 0.0.0.255 eq ftp-data 10.10.3.0 0.0.0.255`
3. **Từ khóa `established`**:
   * Kiểm tra cờ TCP ACK hoặc RST (chỉ gói tin phản hồi của phiên đã mở từ trước mới được đi qua).
   * Cần dòng lệnh: `permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 established`

---

### [PHẦN 4] BẢNG MA TRẬN QUY TẮC ACL 102 (THỨ TỰ ƯU TIÊN TỪ TRÊN XUỐNG DƯỚI)

> *Lưu ý sống còn*: Router duyệt ACL tuần tự từ trên xuống dưới (Top-to-Bottom), gặp dòng đầu tiên khớp (First Match) sẽ thực thi ngay và bỏ qua toàn bộ các dòng bên dưới. Do đó **phải đưa dòng cho phép chi tiết lên trước dòng cấm tổng quát**!

| Thứ tự | Action | Protocol | Source IP / Wildcard | Dest IP / Wildcard | Port / Condition | Mục đích |
|:---:|:---:|:---:|:---|:---|:---|:---|
| **1** | `permit` | `tcp` | `10.10.2.0 0.0.0.255` | `10.10.3.0 0.0.0.255` | `eq ftp` (21) | Cho phép kết nối điều khiển FTP |
| **2** | `permit` | `tcp` | `10.10.2.0 0.0.0.255` | `10.10.3.0 0.0.0.255` | `eq ftp-data` (20) | Cho phép truyền file FTP |
| **3** | `permit` | `tcp` | `10.10.2.0 0.0.0.255` | `10.10.3.0 0.0.0.255` | `established` | Cho phép gói tin phản hồi phiên TCP |
| **4** | **`deny`** | **`ip`** | `10.10.2.0 0.0.0.255` | `10.10.3.0 0.0.0.255` | any | **Chặn toàn bộ IP còn lại** (HTTP 80, Ping ICMP) |
| **5** | `permit` | `ip` | `any` | `any` | any | Cho phép mọi kết nối khác (Internet 8.8.8.8) |
