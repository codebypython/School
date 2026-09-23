# 🛡️ TÓM TẮT HỌC THUẬT: KIẾN TRÚC DANH SÁCH KIỂM SOÁT TRUY CẬP (ACL)
## Tham chiếu: Cisco CCNA Security & Tài liệu Giảng viên `ACL Samples.pdf`

---

## 1. PHÂN LOẠI & VỊ TRÍ ĐẶT DANH SÁCH ACL CHUẨN MỰC

| Tiêu chí | Standard ACL (Tiêu chuẩn) | Extended ACL (Mở rộng) |
|:---|:---|:---|
| **Dải số hiệu (Number Ranges)** | `1 – 99` và mở rộng `1300 – 1999` | `100 – 199` và mở rộng `2000 – 2699` |
| **Trường thông tin lọc** | **CHỈ lọc theo IP Nguồn (Source IP)** | **Lọc theo: Source IP, Destination IP, Giao thức L4 (TCP/UDP/ICMP), và Cổng dịch vụ (Port number)** |
| **Quy tắc vàng về vị trí đặt** | **Càng gần ĐÍCH (Destination) càng tốt** | **Càng gần NGUỒN (Source) càng tốt** |
| **Lý do kỹ thuật** | Do không chỉ định được đích đến, nếu đặt gần nguồn sẽ chặn nhầm cả các lưu lượng hợp lệ khác của máy nguồn. | Giúp chặn lưu lượng rác ngay tại cửa ngõ vào mạng, tiết kiệm tối đa băng thông cho đường truyền WAN. |

---

## 2. MA TRẬN CỔNG DỊCH VỤ PHỔ BIẾN KHI VIẾT ACL

```text
Giao thức   Cổng (Port)   Từ khóa Cisco IOS       Lưu ý bảo mật
─────────────────────────────────────────────────────────────────────────────
FTP-DATA    TCP 20        ftp-data                Kênh truyền dữ liệu (BẮT BUỘC MỞ nếu dùng FTP)
FTP         TCP 21        ftp                     Kênh điều khiển lệnh
SSH         TCP 22        - (gõ 22)               Thay thế hoàn toàn cho Telnet không mã hóa
TELNET      TCP 23        telnet                  🔴 Nguy hiểm (truyền rõ mật khẩu)
DNS         UDP/TCP 53    domain                  UDP cho truy vấn máy trạm, TCP cho Zone Transfer
DHCP        UDP 67, 68    bootps, bootpc          Server lắng nghe port 67, Client gửi từ port 68
HTTP        TCP 80        www                     Văn bản rõ
HTTPS       TCP 443       - (gõ 443)              HTTP over TLS/SSL
ICMP        Layer 3       icmp (echo, echo-reply) Kiểm tra kết nối ping và traceroute
```

---

## 3. CÁC QUY TẮC BẤT BIẾN KHI CẤU HÌNH ACL
1. **Thứ tự từ trên xuống dưới (Top-Down Processing)**: Bộ định tuyến duyệt qua từng dòng luật theo thứ tự từ trên xuống dưới. Ngay khi có một dòng khớp (*First Match*), gói tin sẽ được xử lý ngay và bộ định tuyến **dừng kiểm tra** các dòng còn lại.
2. **Luôn đặt các luật chi tiết (Specific rules) lên trước các luật tổng quát (General rules)**.
3. **Implicit Deny Any ở cuối**: Mọi danh sách ACL đều kết thúc bằng một dòng lệnh ngầm định `deny ip any any`. Bắt buộc phải có ít nhất một dòng `permit` nếu không muốn toàn bộ lưu lượng bị chặn sạch.
