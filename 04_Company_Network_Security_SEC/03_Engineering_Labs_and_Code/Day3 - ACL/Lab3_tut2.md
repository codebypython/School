### Giai đoạn 1: Chuẩn bị máy ảo trên Oracle VirtualBox

**1.Cài đặt và thiết lập 2 máy ảo Windows Server 2003:**

1. Mở **Oracle VirtualBox**.
2. Import file máy ảo từ Google Drive: Tải máy ảo tại đây.
    
    *(Khóa kích hoạt bản quyền nếu có yêu cầu: `HDXR2-62748-6XG6Y-4BT6T-R6H43`)*.
    
3. Đổi tên máy ảo vừa import thành **`LAN2`**.
4. Chuột phải vào máy `LAN2` → chọn **Clone...**:
    - **Name:** `LAN3`
    - **MAC Address Policy:** Chọn **Generate new MAC addresses for all network adapters**
    - **Clone type:** Chọn **Full clone** → bấm **Clone**.
5. Cấu hình card mạng (tránh xung đột trước khi GNS3 quản lý):
    - Vào **Settings** của máy `LAN2` → chọn mục **Network** → tab **Adapter 1**: tại dòng *Attached to* chọn **Not attached** → bấm **OK**.
    - Thực hiện tương tự cho máy `LAN3`: chuyển Adapter 1 thành **Not attached** → bấm **OK**.
        
        *Xác minh:* Cả 2 máy `LAN2` và `LAN3` đều hiển thị trạng thái *Powered Off* và *Adapter 1: Not attached*.
        

### Giai đoạn 2: Khởi tạo Project và Cắm dây trong GNS3

**1.Đăng ký máy ảo VirtualBox vào GNS3:**

1. Mở GNS3 → tạo Project mới (đặt tên tùy ý).
2. Vào menu **Edit** → **Preferences...** → chọn mục **VirtualBox VMs** ở danh sách bên trái.
3. Thêm máy `LAN2`:
    - Bấm **New** → chọn máy `LAN2` → **Finish**.
    - Chọn máy `LAN2` vừa thêm → bấm **Edit** → chuyển sang tab **Network** → tích chọn ô: **Allow GNS3 to use any configured VirtualBox adapter** → bấm **OK**.
4. Thêm máy `LAN3`:
    - Bấm **New** → chọn máy `LAN3` → **Finish**.
    - Bấm **Edit** máy `LAN3` → chuyển sang tab **Network** → tích chọn ô: **Allow GNS3 to use any configured VirtualBox adapter** → bấm **OK**.
5. Bấm **Apply** → **OK** để lưu lại.
    
    *Xác minh:* Khi vào mục thiết bị đầu cuối (End Devices) trên GNS3, bạn thấy hiển thị 2 node `LAN2` và `LAN3`.
    

**2.Đưa thiết bị ra sơ đồ và cắm dây:**

```
1. Kéo các thiết bị sau vào bảng làm việc:
   * **3 Router:** Đặt tên lần lượt là `west`, `gateway`, `east`.
   * **2 Máy ảo:** `LAN2` và `LAN3`.
2. Sử dụng công cụ nối cáp kết nối trực tiếp các cổng theo bảng sau:
```

| **Thiết bị A** | **Cổng A** | **Thiết bị B** | **Cổng B** | **Loại cáp** |
| --- | --- | --- | --- | --- |
| **west** | `Serial1/0` | **gateway** | `Serial1/0` | Cáp Serial |
| **east** | `Serial1/1` | **gateway** | `Serial1/1` | Cáp Serial |
| **west** | `FastEthernet0/0` | **LAN2** (VirtualBox) | `Ethernet0` | Cáp Ethernet |
| **east** | `FastEthernet0/0` | **LAN3** (VirtualBox) | `Ethernet0` | Cáp Ethernet |

```
3. Nhấn nút **Start (▶)** màu xanh lá trên thanh công cụ để khởi động 3 Router và 2 máy ảo Windows Server.
*Xác minh:* Tất cả các điểm nối chuyển sang chấm màu xanh lá và 2 cửa sổ máy ảo khởi động lên màn hình đăng nhập.
```

### Giai đoạn 3: Cấu hình trên 3 Router (Copy & Paste CLI)

Mở cửa sổ Console của từng router trên GNS3 và chạy các đoạn lệnh sau:

#### 1. Router Gateway

Cisco CLI

```
enable
configure terminal
hostname gateway

interface Serial1/0
 ip address 172.16.3.2 255.255.255.0
 clock rate 64000
 no shutdown
exit

interface Serial1/1
 ip address 172.16.4.2 255.255.255.0
 clock rate 64000
 no shutdown
exit

interface FastEthernet0/0
 ip address 16.19.16.19 255.255.255.0
 no shutdown
exit

router rip
 version 2
 no auto-summary
 network 172.16.0.0
 network 16.0.0.0
exit

end
write memory
```

#### 2. Router East

Cisco CLI

```
enable
configure terminal
hostname east

interface Serial1/1
 ip address 172.16.4.1 255.255.255.0
 no shutdown
exit

interface FastEthernet0/0
 ip address 10.10.3.1 255.255.255.0
 no shutdown
exit

interface Loopback0
 ip address 10.10.4.1 255.255.255.0
 no shutdown
exit

router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 172.16.0.0
exit

end
write memory
```

#### 3. Router West

Cisco CLI

```
enable
configure terminal
hostname west

interface Serial1/0
 ip address 172.16.3.1 255.255.255.0
 no shutdown
exit

interface FastEthernet0/0
 ip address 10.10.2.1 255.255.255.0
 no shutdown
exit

interface Loopback0
 ip address 10.10.1.1 255.255.255.0
 no shutdown
exit

router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 172.16.0.0
exit

no ip access-list extended ACL_LAN2_FILTER
ip access-list extended ACL_LAN2_FILTER
 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq 21
 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq 20
 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 established
 deny ip 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255
 permit ip any any
exit

interface FastEthernet0/0
 ip access-group ACL_LAN2_FILTER in
exit

end
write memory
```

### Giai đoạn 4: Cấu hình trên 2 máy ảo Windows Server 2003

Đăng nhập vào từng máy (menu VirtualBox: **Input** → **Keyboard** → **Insert Ctrl-Alt-Del**):

#### 1. Trên máy ảo `LAN2` (Đóng vai trò Client)

1. Tắt tường lửa: Vào **Start** → **Control Panel** → **Windows Firewall** → chọn **Off (not recommended)** → bấm **OK**.
2. Cài đặt IP:
    - Vào **Start** → **Control Panel** → **Network Connections**.
    - Chuột phải vào **Local Area Connection** → chọn **Properties** → nhấp đúp vào **Internet Protocol (TCP/IP)**.
    - Chọn **Use the following IP address**:
        - **IP address:** `10.10.2.10`
        - **Subnet mask:** `255.255.255.0`
        - **Default gateway:** `10.10.2.1`
    - Bấm **OK** → **Close**.

#### 2. Trên máy ảo `LAN3` (Đóng vai trò Server FTP & Web)

1. Tắt tường lửa: Vào **Start** → **Control Panel** → **Windows Firewall** → chọn **Off (not recommended)** → bấm **OK**.
2. Cài đặt IP:
    - Vào **Start** → **Control Panel** → **Network Connections**.
    - Chuột phải vào **Local Area Connection** → chọn **Properties** → nhấp đúp vào **Internet Protocol (TCP/IP)**.
    - Chọn **Use the following IP address**:
        - **IP address:** `10.10.3.10`
        - **Subnet mask:** `255.255.255.0`
        - **Default gateway:** `10.10.3.1`
    - Bấm **OK** → **Close**.
3. Đảm bảo dịch vụ Web và FTP đang chạy:
    - Mở **Start** → **Administrative Tools** → **Internet Information Services (IIS) Manager**.
    - Bung mục tên Server → kiểm tra hai mục **Web Sites** và **FTP Sites**: Đảm bảo `Default Web Site` và `Default FTP Site` đều đang ở trạng thái **Running** (nếu đang dừng thì chuột phải chọn **Start**).

### Giai đoạn 5: Thực hiện Test nghiệm thu (Lấy số liệu báo cáo)

Toàn bộ các bài test được thực hiện trực tiếp từ máy **LAN2** (`10.10.2.10`):

**1.Kiểm tra thông tuyến nội bộ và Ping ra ngoài mạng khác (Cho phép):**

Mở CMD trên máy **LAN2** và chạy:

1. Ping Gateway cục bộ:

DOS

```
ping 10.10.2.1
```

*Kết quả:* Nhận phản hồi thành công `Reply from 10.10.2.1...`.

2. Ping cổng Loopback LAN 1:

DOS

```
ping 10.10.1.1
```

*Kết quả:* Nhận phản hồi thành công `Reply from 10.10.1.1...`.

3. Ping cổng Loopback LAN 4:

DOS

```
ping 10.10.4.1
```

*Kết quả:* Nhận phản hồi thành công `Reply from 10.10.4.1...`.

4. Ping cổng Internet Gateway:

DOS

```
ping 16.19.16.19
```

*Kết quả:* Nhận phản hồi thành công `Reply from 16.19.16.19...`.

*Xác minh:* Các dải mạng bên ngoài hoạt động bình thường, không bị ACL chặn nhầm.

**2.Kiểm tra Ping sang Server LAN3 (Yêu cầu: Bị chặn):**

Tại cửa sổ CMD của máy **LAN2**, gõ:

DOS

```
ping 10.10.3.10
```

*Xác minh thành công:* Màn hình thông báo `Request timed out.` hoặc `Destination host unreachable.`. Gói tin ICMP giữa LAN 2 và LAN 3 đã bị ACL chặn đúng thiết kế.

**3.Kiểm tra truy cập Web sang Server LAN3 (Yêu cầu: Bị chặn):**

1. Mở trình duyệt **Internet Explorer** trên máy **LAN2**.
2. Nhập địa chỉ: `http://10.10.3.10` rồi nhấn **Enter**.
    
    *Xác minh thành công:* Trình duyệt không tải được trang và hiển thị lỗi: *"The page cannot be displayed"* hoặc *"Internet Explorer cannot display the webpage"*. Cổng HTTP 80 đã bị ACL chặn.
    

**4.Kiểm tra dịch vụ FTP sang Server LAN3 (Yêu cầu: Cho phép):**

Mở lại cửa sổ CMD trên máy **LAN2** và thực hiện:

1. Gõ:

DOS

```
ftp 10.10.3.10
```

1. Nhập User: `anonymous` rồi nhấn **Enter**.
2. Nhập Password: Để trống và nhấn **Enter**.
3. Màn hình hiện thông báo `230 User anonymous logged in.`.
4. Gõ lệnh:

DOS

```
dir
```

Màn hình hiển thị danh sách thư mục và báo `226 Transfer complete.`.

6. Gõ `bye` để thoát khỏi phiên FTP.

*Xác minh thành công:* Dịch vụ FTP truyền dữ liệu thông suốt theo đúng rule cho phép của ACL.

**5.Chụp ảnh bộ đếm gói tin ACL trên Router West:**

Vào console của **Router West**, gõ:

Cisco CLI

```
show ip access-lists
```

*Xác minh thành công:* Dòng `permit tcp ... eq 21/20` tăng số lượng `matches` (khớp gói FTP), dòng `deny ip ...` tăng số lượng `matches` (khớp các gói Ping và Web đã bị chặn), và dòng `permit ip any any` ghi nhận số lượt truy cập ra các mạng ngoài.