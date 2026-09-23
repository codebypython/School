# 🧪 HƯỚNG DẪN THAO TÁC KIỂM TRA CHI TIẾT LAB 3
**Học phần**: An Toàn Mạng (CORP-04-SEC - DUT)  
**Nội dung**: Quy trình kiểm tra chính xác 3 dịch vụ: Ping (ICMP), Web (HTTP), FTP theo chuẩn Barem Thầy Lý  

---

## 📋 MỤC TIÊU NGHIỆM THU THEO BAREM ĐIỂM
1. **Kiểm tra 1 (Dịch vụ Ping)**: Từ LAN 2 không ping được sang LAN 3 (Bị chặn ✅). Từ LAN 2 ping ra Internet 8.8.8.8 thành công (Cho phép ✅).
2. **Kiểm tra 2 (Dịch vụ Web)**: Từ LAN 2 mở trình duyệt đến Server LAN 3 (`http://10.10.3.2`) báo không kết nối được (Bị chặn ✅).
3. **Kiểm tra 3 (Dịch vụ FTP)**: Từ LAN 2 kết nối FTP sang Server LAN 3 (`ftp 10.10.3.2`) thành công, đăng nhập được, chạy lệnh `dir`, `get 1 file` và `quit` (Cho phép ✅).
4. **Kiểm tra 4 (Router Audit)**: Lệnh `show ip access-lists` trên Router hiển thị bộ đếm số gói tin (Matches counter) tăng tương ứng.

---

## 🛠️ CÁC BƯỚC THAO TÁC TRÊN MÁY ẢO VMWARE (WINDOWS SERVER 2003 LAN 2)

Đăng nhập vào máy ảo **Server2003_LAN2** (Mật khẩu: `123qwe!@#`).

### Bước 1: Kiểm thử Dịch Vụ Ping (ICMP)
1. Mở `Start` $\rightarrow$ `Run` $\rightarrow$ Gõ `cmd` $\rightarrow$ Nhấn Enter.
2. Thử Ping sang Server LAN 3:
   ```cmd
   ping 10.10.3.2
   ```
   *Kết quả thực tế bắt buộc*:
   ```text
   Pinging 10.10.3.2 with 32 bytes of data:
   Destination host unreachable. (hoặc Request timed out.)
   Destination host unreachable.
   Destination host unreachable.
   Destination host unreachable.

   Ping statistics for 10.10.3.2:
       Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
   ```
   > ✅ **KẾT LUẬN**: ICMP bị chặn chính xác bởi dòng `deny ip 10.10.2.0 ... 10.10.3.0`!

3. Thử Ping ra địa chỉ Internet ngoài:
   ```cmd
   ping 8.8.8.8
   ```
   *Kết quả thực tế*:
   ```text
   Reply from 8.8.8.8: bytes=32 time=25ms TTL=253
   Reply from 8.8.8.8: bytes=32 time=22ms TTL=253
   ```
   > ✅ **KẾT LUẬN**: Các kết nối khác ngoài LAN 3 vẫn thông suốt qua dòng `permit ip any any`!

---

### Bước 2: Kiểm thử Dịch Vụ Web (HTTP Port 80)
1. Trên máy ảo LAN 2, mở trình duyệt Internet Explorer (hoặc Firefox).
2. Nhập URL:
   ```text
   http://10.10.3.2
   ```
3. Nhấn Enter và quan sát.
   *Kết quả thực tế bắt buộc*:
   ```text
   The page cannot be displayed
   The website is not responding or connection was refused.
   ```
   > ✅ **KẾT LUẬN**: Gói tin TCP SYN gửi đến cổng 80 bị Router West drop ngay lập tức!

---

### Bước 3: Kiểm thử Dịch Vụ Truyền File (FTP Port 21 & 20)
1. Tại cửa sổ Command Prompt (`cmd`) trên máy ảo LAN 2, gõ:
   ```cmd
   ftp 10.10.3.2
   ```
2. Màn hình console kết nối thành công và yêu cầu đăng nhập:
   ```text
   Connected to 10.10.3.2.
   220 Microsoft FTP Service
   User (10.10.3.2:(none)): Administrator
   331 Password required for Administrator.
   Password:
   230 User logged in.
   ```
   *(Nhập mật khẩu: `123qwe!@#`)*

3. Thực thi kiểm tra các thao tác truyền dữ liệu:
   ```cmd
   ftp> dir
   ```
   *Console hiển thị danh sách tệp trên Server LAN 3*:
   ```text
   200 PORT command successful.
   150 Opening ASCII mode data connection for /bin/ls.
   -rwxrwxrwx   1 owner    group            1024 Sep 23 10:00 tai_lieu_an_toan_mang.txt
   226 Transfer complete.
   ```
4. Tải 1 tệp tin về máy:
   ```cmd
   ftp> get tai_lieu_an_toan_mang.txt
   ```
   *Console báo thành công*:
   ```text
   200 PORT command successful.
   150 Opening BINARY mode data connection for tai_lieu_an_toan_mang.txt.
   226 Transfer complete.
   ftp: 1024 bytes received in 0.05Seconds 20.48Kbytes/sec.
   ```
5. Thoát FTP:
   ```cmd
   ftp> quit
   221 Goodbye.
   ```
6. Gõ lại lệnh `dir` trên CMD cục bộ của máy ảo LAN 2 $\rightarrow$ Xác nhận tệp `tai_lieu_an_toan_mang.txt` đã xuất hiện trên máy cục bộ!
   > ✅ **KẾT LUẬN ĐẠT 10/10**: Cả kênh điều khiển TCP 21 và kênh dữ liệu TCP 20 hoạt động hoàn hảo!

---

### Bước 4: Kiểm tra Bộ Đếm Match Counter trên Router West
Truy cập vào console Router West, gõ lệnh:
```cisco
West# show ip access-lists 102
```
*Kết quả hiển thị minh chứng các dòng lệnh đã được thực thi*:
```text
Extended IP access list 102
    10 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp (42 matches)
    20 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 eq ftp-data (16 matches)
    30 permit tcp 10.10.2.0 0.0.0.255 eq ftp-data 10.10.3.0 0.0.0.255 (8 matches)
    40 permit tcp 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 established (64 matches)
    50 deny ip 10.10.2.0 0.0.0.255 10.10.3.0 0.0.0.255 (18 matches)
    60 permit ip any any (120 matches)
```
> Có `(matches)` ở dòng FTP, dòng deny IP, và dòng permit any any $\implies$ **Chứng nhận hệ thống lọc ACL đạt chuẩn tuyệt đối!**
