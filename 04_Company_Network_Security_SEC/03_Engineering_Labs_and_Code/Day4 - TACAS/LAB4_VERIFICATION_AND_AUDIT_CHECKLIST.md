# 📋 KỊCH BẢN KIỂM THỬ NGHIỆM THU & BẢNG BẰNG CHỨNG ĐẠT 10/10 (LAB 4 AAA)
## Dự Án: Xác Thực & Cấp Quyền Truy Cập Mạng Cho Công Ty Banana Corp
> **Mục tiêu:** Cung cấp đầy đủ các kịch bản kiểm thử thực nghiệm, bắt gói tin Wireshark và chụp màn hình nộp bài cho Thầy Nguyễn Thế Xuân Ly.

---

## 🧪 MA TRẬN CÁC KỊCH BẢN KIỂM THỬ (TEST CASES)

| Mã Test | Thử nghiệm | Thao tác thực hiện | Kết quả mong đợi (Bằng chứng chấm điểm) | Ý nghĩa bảo mật |
| :---: | :--- | :--- | :--- | :--- |
| **TC-01** | **Thông tuyến hạ tầng** | Từ Router gõ: `ping 10.0.0.100`<br>Từ Client gõ: `ping 192.168.1.1` | Nhận phản hồi thành công `!!!!!` (100%) và `Reply from 192.168.1.1`. | Hạ tầng L2/L3 sẵn sàng cho truyền thông AAA. |
| **TC-02** | **Xác thực TACACS+ thành công** | Từ Client PC (`192.168.1.10`) gõ: `telnet 192.168.1.1`<br>User: `nhanvien` / Pass: `123456` | Đăng nhập thành công vào dấu nhắc Router `TACACS_Client>`. | Router đã gửi yêu cầu tới ACS và ACS đã phê duyệt danh tính. |
| **TC-03** | **Từ chối xác thực sai mật khẩu** | Từ Client PC gõ: `telnet 192.168.1.1`<br>User: `nhanvien` / Pass: `saimatkhau` | Báo lỗi `Login invalid`, nhắc nhập lại 3 lần rồi ngắt kết nối. | Hệ thống ngăn chặn truy cập trái phép. |
| **TC-04** | **Phân tích bắt gói tin Wireshark** | Bắt gói tin trên cổng `Fa2/1` nối sang Server, lọc filter: `tacacs`. | Thấy các frame TCP port 49, mang nhãn **`TACACS+ Encrypted payload`**. | Chứng minh TACACS+ mã hóa toàn bộ dữ liệu (vượt trội hơn RADIUS). |
| **TC-05** | **Kiểm tra nhật ký trên Cisco ACS** | Mở Firefox máy ảo `http://127.0.0.1:2002` $\rightarrow$ `Reports` $\rightarrow$ `Passed Authentications`. | Xuất hiện dòng log màu xanh ghi nhận: User `nhanvien`, Client `192.168.1.10`, Status **PASS**. | Khả năng kiểm toán (Accounting/Auditing) tập trung của doanh nghiệp. |
| **TC-06** | **Dự phòng Local khi Server sập** | Tạm dừng (Pause) máy ảo `TACACS_Server`, Telnet bằng user: `admin` / `AdminBackupPass!`. | Vẫn đăng nhập thành công vào chế độ đặc quyền `TACACS_Client#`. | Chống khóa (Lockout) Router khi đứt đường truyền AAA. |

---

## 📸 ẢNH CHỤP MẪU CHUẨN BỊ CHO BÁO CÁO NỘP BÀI

### 1. Bằng chứng Telnet từ máy trạm:
```text
C:\> telnet 192.168.1.1
Connecting To 192.168.1.1...Connected.

User Access Verification

Username: nhanvien
Password: 
TACACS_Client>
```

### 2. Bằng chứng Wireshark phân tích gói tin TACACS+:
* Chuột phải đường dây giữa Router và `TACACS_Server` $\rightarrow$ **Start capture**.
* Bộ lọc: `tacacs`.
* Chi tiết frame trong Wireshark:
  ```text
  Frame 12: 106 bytes on wire
  Transmission Control Protocol, Src Port: 49, Dst Port: 1088, Seq: 1, Ack: 1
  TACACS+
      Major version: 12
      Minor version: 0
      Packet type: Authentication (1)
      Sequence number: 2
      Flags: 0x01 (Encrypted)
      Session ID: 0x2b8d4f12
      Length: 42
      Encrypted payload: e8a3d12...
  ```
  *(Nhấn mạnh vào trường `Flags: 0x01 (Encrypted)` để giải thích cho giảng viên).*
