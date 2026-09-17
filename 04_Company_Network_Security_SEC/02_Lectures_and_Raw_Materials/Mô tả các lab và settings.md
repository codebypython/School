## Bài đăng 1

Nguyễn Thế Xuân Ly8/12 11:13 AM[Chuẩn bị] Cho buổi họcChào các em,Nhớ mang theo laptop, sạc và ổ cắm điện nối dài để làm bài tập nhé.see more2 Heart reactions.21 Fire reaction.Reply

---

## Bài đăng 2

Nguyễn Thế Xuân Ly8/27 7:27 AMEdited[EIGRP] Authentication & Wireshark(1) RFC 7868 (EIGRP Document)(2) Wireshark EIGRP_AUTH_TYPE_TEXT = ?see moreReply

---

## Bài đăng 3

Nguyễn Thế Xuân Ly8/27 7:47 AM[PPP] CHAP Authentication* Hướng dẫn kiểm tra:(1) Gõ lệnh show ip route trên các Router, nếu hiển thị đủ 6 mạng con (subnet) theo thiết kế VLSM là đúng(2) Mở các file pcap của Wireshark, gõ ppp, nếu hiển thị các tài khoản xác thực CHAP (có giá trị hash) là đúng.see moreReply

---

## Bài đăng 4

Nguyễn Thế Xuân Ly8/27 7:32 AMDanh sách kiểm soát Truy cập (Access Control Lists) 1. Sử dụng GNS3 để dựng cơ sở hạ tầng như sơ đồ trên. Giao thức định tuyến sử dụng là RIPv22. Triển khai Access Control List (ACL) thực hiện các yêu cầu sau:- Cho phép FTP giữa LAN2 và LAN3- Chặn các kết nối giữa LAN2 và LAN3- Cho phép các kết nối khác3. Chú ý: các dịch vụ như Web/ FTP có thể dùng IIS trên Server 2003 đối với LAN2 và 3. Các LAN1 và 4 có thể dùng cổng loopback.see moreNguyễn Thế Xuân Ly9/3 7:13 AMEditedGắn thêm 2 server vào LAN 2 và LAN 3 để kiểm tra chặn/ cho phép các dịch vụ tiêu biểu là Ping (ICMP), Web (HTTP) và Truyền file tin cậy (FTP)Chú ý: gán IP phù hợp cho mỗi server theo từng mạng con (subnet) tương ứng của LAN 2 và LAN 3Giả sử rằng đã cấu hình thành công ACL thì từ LAN 2 PC và LAN 3 PC sẽ:không ping được các server ở LAN 2 & 3 (chặn IP sẽ chặn ICMP)không truy cập được các server ở LAN 2 & 3 bằng dịch vụ Web (chặn IP sẽ chặn HTTP)truy cập được các server ở LAN 2 & 3 bằng dịch vụ FTP (vì ACL cho phép). Cách kiểm tra FTP như sau:Desktop --> Command Run --> ftp IP của Server --> bị chặn sẽ báo còn nếu không bị chặn sẽ yêu cầu nhập username và password (có thể dùng tài khoản Administrator). Giả sử rằng đã đăng nhập được bằng FTP vào server LAN 2 và LAN 3 thì gõ các lệnh sau để kiểm tradir //hiển thị nội dung thư mụcget 1 file bất kỳ //tải 1 file bất kỳ vềSau khi get xong thì gõ lệnh quit để thoátGõ lại lệnh dir sẽ thấy file đó đã có ở PCsee moreNguyễn Thế Xuân Ly9/6 1:07 PMEditedMáy ảo Server 2003 cho ai cần:  [4. VM](https://dutudn-my.sharepoint.com/:f:/g/personal/ntxly_dut_udn_vn/IgBS8mA-cbgBQ6RcJwsKd4XaAYXAGjhQq1mxLBrLFlKB0OI?e=WlOAhX) //Giả sử đã cài đặt VMWare Workstation Pro thì sau khi tải máy ảo (file .ova) về, chỉ cần kích đúp chuột vào file là tự động import. Mật khẩu Administrator: 123qwe!@#see more1 Heart reaction.Reply

** Danh mục liên kết & tệp trong bài:**
* [4. VM](https://dutudn-my.sharepoint.com/:f:/g/personal/ntxly_dut_udn_vn/IgBS8mA-cbgBQ6RcJwsKd4XaAYXAGjhQq1mxLBrLFlKB0OI?e=WlOAhX)


---

## Bài đăng 5

Nguyễn Thế Xuân LyYesterday 10:54 PMYêu cầu triển khai AAA (TACACS) cho công ty BananaCác nhân viên công ty Banana muốn truy cập Internet phải được xác thực (Authentication) và cấp quyền Authorization bởi hệ thống TACACS gồm TACACS_Client (Router/ Switch) và TACACS_Server (Server 2003).Sơ đồ triển khai:  Chú ý 1: để cài đặt phần mềm TACACS trên Server 2003 thì cần cài đặt các phần mềm (thư mục Tài liệu học tập --> TACACS) theo thứ tự sau: 1. Cài Java Runtime (jre-6u13-windows-i586-p-s.exe)2. Giải nén ACSv4.2.124 FULL-K9.zip và chọn setup.exe để cài đặt3. Cài Firefox 2.0.exe để thao tác dễ dàng hơn so với IE6 Chú ý 2: nếu chưa có máy ảo VMWare (XP Client & Server 2003) thì có thể import file .ova (trong thư mục Tài liệu học tập --> TACACS) see moreReply