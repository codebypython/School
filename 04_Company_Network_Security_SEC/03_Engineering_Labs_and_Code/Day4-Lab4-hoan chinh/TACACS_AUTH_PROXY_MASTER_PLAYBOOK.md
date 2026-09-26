# 🍌 CẨM NANG TOÀN DIỆN VÀ KHẮC PHỤC TRIỆT ĐỂ LAB 4: AAA TACACS+ AUTH-PROXY (BANANA CORP)
**Mã Học Phần**: CORP-04-SEC (An Toàn Mạng - DUT)  
**Tiêu chuẩn**: DUT Network Security Engineering Lab  
**Thư mục làm việc chuẩn**: `Day4-Lab4-hoan chinh/Lab4`  

---

## 🎯 1. GIẢI MÃ CHÍNH XÁC 3 VẤN ĐỀ BẠN ĐANG GẶP PHẢI

### Vấn đề 1: Tại sao Console `TACACSClient` vẫn bị chặn hỏi Username / Password?
* **Bản chất kỹ thuật**: Trong Cisco IOS, khi lệnh `aaa new-model` được kích hoạt, hệ điều hành sẽ **hoàn toàn phớt lờ lệnh `no login`** trên cổng `line con 0`! IOS tự động ép `line con 0` phải dùng danh sách xác thực `default`.
* **Khắc phục triệt để**: Phải tạo một danh sách riêng biệt `CONSOLE_BYPASS` với phương thức `none`:
  ```cisco
  aaa authentication login CONSOLE_BYPASS none
  aaa authorization exec CONSOLE_BYPASS none
  line con 0
   login authentication CONSOLE_BYPASS
   authorization exec CONSOLE_BYPASS
   privilege level 15
  ```
  *(Đã được nạp trực tiếp vào file cấu hình. Khi khởi động lại Router, bạn bấm Console sẽ vào thẳng ngay `TACACSClient#` mà không bị hỏi bất kỳ chữ nào!).*

---

### Vấn đề 2: Tại sao ping 10.0.0.1 từ CMD máy ảo bị Request timed out?
* **Bản chất kỹ thuật**: 
  1. Trong cấu hình cũ lưu ở bộ nhớ tạm RAM của Router, cổng kết nối sang máy ảo chưa có dòng `no shutdown` $\implies$ Cổng mạng bị đóng (Administratively down).
  2. Chúng tôi đã chuyển cổng kết nối sang **`FastEthernet0/1`** (cổng tích hợp trực tiếp trên mainboard slot 0 của c3725, độ ổn định 100%, không bị lỗi duplex/speed).
  3. Cần đảm bảo Router trên GNS3 đã được **bật (nút Play xanh)** thì máy ảo mới ping thấy được.

---

### Vấn đề 3: Tại sao giao diện `User Setup` trên ảnh thực tế KHÔNG CÓ mục `TACACS+ Settings`?
* Nhìn vào 2 ảnh chụp màn hình bạn gửi: Bạn đang ở trang `User Setup` của user `Administrator`. Các mục hiển thị gồm: `Password Authentication`, `CiscoSecure PAP`, `Group Assigned`, `Callback`, `Client IP Address Assignment`, `Account Disable`. Hoàn toàn không thấy mục `TACACS+ Settings`!
* **Bản chất**: Trong Cisco Secure ACS 4.2:
  👉 **ĐỐI VỚI BÀI TOÁN XÁC THỰC WEB AUTH-PROXY, BẠN HOÀN TOÀN KHÔNG CẦN MỤC `TACACS+ Settings`!**
  - Khi trình duyệt truy cập `http://2.2.2.2/`, Router chỉ gửi yêu cầu hỏi ACS: *"Tài khoản Administrator với mật khẩu này có khớp trong CSDL `ACS Internal Database` không?"*
  - Do đó, trên màn hình thực tế (như ảnh bạn chụp), bạn **CHỈ CẦN**:
    1. Nhập **Password**: `123qwe!@#`
    2. Nhập **Confirm Password**: `123qwe!@#`
    3. Bấm **`Submit`** ở ngay dưới!
  - Thế là xong 100%! Không cần tìm kiếm mục `TACACS+ Settings` phức tạp nào cả!

---

### Vấn đề 4: Tại sao Router `Internet` dùng c3725 (2.2.2.2) mà máy ảo trên VMnet1 vẫn truy cập được?
* **Đây chính là bản chất của Router (Bộ định tuyến)**:
  - Máy ảo của bạn nằm ở dải mạng nội bộ: `10.0.0.0/24` (nối vào cổng `Fa0/1` của Router qua `VMnet1`).
  - Web Server `Internet` nằm ở dải mạng bên ngoài: `2.2.2.0/24` (nối vào cổng `Fa0/0` của Router).
  - Hai dải mạng này **KHÔNG CẦN VÀ KHÔNG ĐƯỢC PHÉP cắm chung vào VMnet1** (vì cắm chung sẽ gây xung đột dải mạng Broadcast).
  - Khi từ máy ảo bạn gõ `http://2.2.2.2/`, gói tin sẽ gửi đến Default Gateway là Router (`10.0.0.1`). Router chặn lại hiện pop-up xác thực $\rightarrow$ Sau khi xác thực đúng, Router tự động **chuyển tiếp (Routing)** gói tin sang cổng `Fa0/0` để mở trang web `2.2.2.2`!

---

## 📋 2. BẢNG QUY CHUẨN THÔNG SỐ TOÀN HỆ THỐNG

| Thông số / Thiết bị | Giá trị chuẩn | Ghi chú |
|:---|:---|:---|
| **TACACS+ Secret Key** | **`ciscobanana123`** | Khóa bí mật đồng bộ giữa Router và ACS |
| **IP Router Gateway** | `10.0.0.1` (Fa0/1) \| `2.2.2.1` (Fa0/0) | Cổng nối máy ảo và cổng nối Internet |
| **IP Máy ảo Server 2003** | `10.0.0.100` (Subnet mask `255.255.255.0`, Gateway `10.0.0.1`) | Máy ảo `TACACS_Server_Banana` trên `VMnet1` |
| **IP Trang Web Internet** | **`http://2.2.2.2/`** | Web server trên Router `Internet` |
| **User Quản trị** | `Administrator` \| Pass: `123qwe!@#` | Tạo trong ACS `User Setup` |
| **User Nhân viên** | `nhanvien` \| Pass: `123456` | Tạo trong ACS `User Setup` |
| **User Cục bộ dự phòng** | `admin` \| Pass: `AdminPass123!` | Lưu sẵn trong Router (phòng khi mất điện) |

---

## 🛠️ 3. QUY TRÌNH THỰC HIỆN TUẦN TỰ (ĐẢM BẢO CHẠY NGAY LẬP TỨC)

### BƯỚC 1: KHỞI ĐỘNG GNS3 VÀ TẢI CẤU HÌNH SẠCH
1. Mở phần mềm **GNS3**, mở dự án `Lab4.gns3`:  
   👉 `Day4-Lab4-hoan chinh\Lab4\Lab4.gns3`
2. Nhấp chuột phải vào `TACACSClient` $\rightarrow$ chọn **Stop** (nếu đang chạy), sau đó chuột phải chọn **Start** (hoặc nhấn nút Play xanh).
3. Chuột phải vào `TACACSClient` $\rightarrow$ chọn **Console**.  
   👉 **KẾT QUẢ**: Màn hình hiện thẳng dấu nhắc:
   ```text
   TACACSClient#
   ```
   *(Không bị hỏi mật khẩu hay khóa ngoài nữa!).*

---

### BƯỚC 2: BẬT MÁY ẢO `TACACS_Server_Banana` & KIỂM TRA MẠNG
1. Trong VMware Workstation Pro, bật máy ảo **`TACACS_Server_Banana`**.
2. Trên máy ảo, mở CMD gõ:
   ```cmd
   ping 10.0.0.1
   ```
   👉 **KẾT QUẢ BẮT BUỘC**:
   ```text
   Reply from 10.0.0.1: bytes=32 time<1ms TTL=255
   ```
   *(Đạt 100% kết nối thông suốt giữa máy ảo và Router).*

---

### BƯỚC 3: THAO TÁC TRÊN GIAO DIỆN WEB ACS (CHUẨN TỪNG NÚT BẤM)
Mở Firefox trên máy ảo vào link ACS (hoặc click icon `CiscoSecure ACS Admin` ngoài Desktop):

#### 3.1. Khai báo Router trong `Network Configuration`:
1. Click menu bên trái: **`Network Configuration`**.
2. Tại bảng **AAA Clients**, click nút **`Add Entry`** (hoặc bấm vào dòng `TACACSClient` nếu đã có):
   - **AAA Client Hostname**: Gõ `TACACSClient`
   - **AAA Client IP Address**: Gõ `10.0.0.1`
   - **Key**: Gõ `ciscobanana123`
   - **Authenticate Using**: Chọn chấm tròn 🔘 **`TACACS+ (Cisco IOS)`**
3. Cuộn xuống đáy trang, bấm nút: **`Submit + Restart`**.

#### 3.2. Cấu hình tài khoản trong `User Setup` (Đúng giao diện thực tế như ảnh của bạn):
1. Click menu bên trái: **`User Setup`**.
2. Ô User: Gõ **`Administrator`** $\rightarrow$ bấm **`Add/Edit`**:
   - Mục **Password Authentication**: Giữ nguyên `ACS Internal Database`.
   - Mục **Password**: Gõ `123qwe!@#`
   - Mục **Confirm Password**: Gõ `123qwe!@#`
   - Bấm nút **`Submit`** ngay dưới (như trên ảnh của bạn).
3. Quay lại ô User: Gõ **`nhanvien`** $\rightarrow$ bấm **`Add/Edit`**:
   - Mục **Password**: Gõ `123456`
   - Mục **Confirm Password**: Gõ `123456`
   - Bấm nút **`Submit`**.

---

## 🎬 4. KỊCH BẢN DEMO BẢO VỆ ĐỒ ÁN TRƯỚC MẶT THẦY

### 🌟 Demo 1: Truy Cập Web Internet 2.2.2.2 Qua Auth-Proxy (Yêu cầu cốt lõi)
1. Trên máy ảo Windows Server 2003, mở trình duyệt **Mozilla Firefox**.
2. Gõ địa chỉ: 👉 **`http://2.2.2.2/`**
3. **Hiện tượng chính xác diễn ra:**
   - Trình duyệt nảy ra ngay hộp thoại pop-up:  
     👉 **`Authentication Required: Enter username and password for "Cisco Systems"`**!
4. **Thử nghiệm nhập sai mật khẩu (Test Case Fail):**
   - Username: `nhanvien`, Password: `sai_mat_khau_123` $\rightarrow$ Bấm OK.
   - Kết quả: Bị từ chối (401 Unauthorized), tiến trình kết thúc, không được xem trang web.
5. **Thử nghiệm nhập đúng mật khẩu (Test Case Pass):**
   - Username: `Administrator`, Password: `123qwe!@#` (hoặc `nhanvien` / `123456`) $\rightarrow$ Bấm OK.
   - Kết quả: Trình duyệt thông báo **`Cisco Systems - Authentication Successful!`** và trang web của máy chủ `2.2.2.2` hiện ra trọn vẹn!

### 🌟 Demo 2: Show Lệnh Xác Thực Trên Console Router
Mở Console `TACACSClient` trên GNS3 gõ:
```cisco
! Xem nhật ký phiên Auth-Proxy vừa đăng nhập
TACACSClient# show ip auth-proxy cache
! Kết quả: Hiển thị IP nguồn 10.0.0.100, giao thức HTTP, thời gian đếm lùi session.

! Xem trạng thái kết nối tới máy chủ TACACS+
TACACSClient# show tacacs
! Kết quả: alive: 10.0.0.100/49, packets in/out tăng đều.
```

### 🌟 Demo 3: Show Nhật Ký Kiểm Toán Trên Web ACS
Vào menu bên trái của ACS: **`Reports and Activity`** $\rightarrow$ **`Passed Authentications`** $\rightarrow$ mở file log ngày hôm nay để thầy thấy rõ thời điểm đăng nhập của user `Administrator` / `nhanvien` vừa thực hiện thành công.

---

### ⚠️ Lỗi phổ biến sinh viên hay gặp
1. **Quên bật nút Start trên GNS3**: Nếu 2 Router trên GNS3 có chấm đỏ (đang tắt), máy ảo sẽ không thể ping thấy `10.0.0.1`.
2. **Khóa bí mật không khớp**: Chữ `ciscobanana123` phải viết thường hoàn toàn, không có dấu cách ở đầu/cuối.
3. **Gõ sai cổng trên thanh URL**: Phải gõ đúng giao thức HTTP chuẩn `http://2.2.2.2/` (không gõ `https`).

---

### 💡 Micro-quiz / Câu hỏi phản biện
**Câu hỏi**: *"Cơ chế Authentication Proxy (Auth-Proxy) trên Router Cisco khác gì so với Proxy Server truyền thống (như Squid hay Nginx)?"*  

**Gợi ý trả lời**:  
*"Thưa thầy, Proxy Server truyền thống hoạt động ở tầng ứng dụng (Layer 7 Application Proxy), trực tiếp nhận yêu cầu từ client rồi tự mình tạo kết nối mới ra server ngoài để lấy dữ liệu về. Trong khi đó, Cisco Auth-Proxy là cơ chế bảo mật trên thiết bị định tuyến (Router): nó chỉ tạm thời chặn gói tin ở tầng mạng để yêu cầu người dùng xác thực danh tính qua AAA (TACACS+/RADIUS). Sau khi xác thực thành công, Router tự động sinh ra một luật truy cập động (Dynamic ACL) mở đường cho lưu lượng IP của người dùng đi xuyên qua router ở tốc độ phần cứng mà không phải xử lý đóng gói proxy tầng 7."*
