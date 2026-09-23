# 🛡️ TÓM TẮT HỌC THUẬT: XÁC THỰC GIAO THỨC ĐỊNH TUYẾN & WAN PPP
## Tham chiếu: IETF RFC 1994 (CHAP), RFC 2328 (OSPFv2), RFC 7868 (EIGRP)

---

## 1. SO SÁNH CƠ CHẾ XÁC THỰC PAP VS CHAP TRONG GIAO THỨC PPP

| Tiêu chí | Password Authentication Protocol (PAP) | Challenge Handshake Authentication Protocol (CHAP) |
|:---|:---|:---|
| **Số bước bắt tay** | 2 bước: `Request` $\rightarrow$ `Ack/Nak` | 3 bước: `Challenge` $\rightarrow$ `Response` $\rightarrow$ `Success/Failure` |
| **Mức độ an toàn** | 🔴 Kém (Mật khẩu truyền dạng bản rõ Cleartext) | 🟢 Cao (Mật khẩu không bao giờ truyền qua mạng) |
| **Hàm băm sử dụng** | Không sử dụng | Hàm băm một chiều MD5 |
| **Chống tấn công Replay** | 🔴 Không có (dễ bị bắt trộm và phát lại) | 🟢 Có (mỗi lần bắt tay tạo 1 số ngẫu nhiên Nonce mới) |
| **Tần suất xác thực** | Chỉ xác thực 1 lần duy nhất khi link vừa up | Có thể xác thực ngẫu nhiên định kỳ trong suốt phiên kết nối |
| **Quy tắc cấu hình Cisco** | Router gửi khai báo `ppp pap sent-username ...` | `username` phải là **hostname chính xác** của Router đối diện |

---

## 2. MA TRẬN XÁC THỰC CÁC GIAO THỨC ĐỊNH TUYẾN ĐỘNG

| Giao thức | Tầng hoạt động | Cơ chế lưu trữ khóa | Kiểu xác thực hỗ trợ | Lệnh kích hoạt cốt lõi |
|:---|:---:|:---:|:---|:---|
| **RIPv2** | UDP Port 520 | `key chain` | Plaintext (Type 1) hoặc MD5 (Type 2) | `ip rip authentication mode md5`<br>`ip rip authentication key-chain <name>` |
| **OSPFv2** | IP Protocol 89 | Trực tiếp trên Interface hoặc Area | Simple Password (Type 1) hoặc MD5 (Type 2) | `ip ospf authentication message-digest`<br>`ip ospf message-digest-key 1 md5 <pass>` |
| **EIGRP** | IP Protocol 88 | `key chain` | MD5 (Classic mode) hoặc HMAC-SHA-256 (Named mode) | `ip authentication mode eigrp <AS> md5`<br>`ip authentication key-chain eigrp <AS> <name>` |

---

## 3. GIẢI MÃ CÂU HỎI HỌC BÚA CỦA GIẢNG VIÊN (THẦY XUÂN LY)

> **Câu hỏi:** Trong Wireshark, trường `EIGRP_AUTH_TYPE_TEXT = ?`
- Theo định nghĩa trong mã nguồn bộ phân tích giao thức Wireshark (`packet-eigrp.c`) và chuẩn RFC 7868:
  - `EIGRP_AUTH_TYPE_NONE = 0x0000` (Không xác thực)
  - `EIGRP_AUTH_TYPE_TEXT = 0x0001` (Xác thực mật khẩu văn bản thô)
  - `EIGRP_AUTH_TYPE_MD5 = 0x0002` (Xác thực băm mật mã MD5)
  - Khi bắt gói tin EIGRP Hello có xác thực MD5 trong bài lab của Thầy Ly, trường `Authentication TLV -> Auth Type` sẽ mang giá trị hiển thị là **`2`** (`0x0002`).
