# 🗝️ CẨM NANG NGUYÊN THỦY MẬT MÃ (CRYPTO PRIMITIVES CHEATSHEET)
## Phòng 01: Strategy & Curriculum — `CORP-04-SEC`
> **Tiêu chuẩn đối chiếu:** NIST Special Publication 800-57 Part 1 Rev. 5 & BSI TR-02102-1  
> **Cố vấn chuyên trách:** DUT Cyber Security Mentor

---

## 1. BẢNG SO SÁNH ĐỘ DÀI KHÓA TƯƠNG ĐƯƠNG (SECURITY BITS EQUIVALENCE)

Theo khuyến nghị bảo mật NIST, mức độ an toàn (Security Strength in bits) giữa các họ mật mã được quy đổi như sau:

| Mức Bảo Mật (Bits) | Mã Khối Đối Xứng (Symmetric) | Khóa Công Khai RSA / DH | Đường Cong Elliptic (ECC) | Hàm Băm Toàn Vẹn (Hash) | Trạng Thái Sử Dụng Đến 2030+ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **80 bits** | 2TDEA (2-Key 3DES) | 1024 bits | 160 bits | SHA-1 | 🔴 **CẤM DÙNG (Legacy / Insecure)** |
| **112 bits** | 3TDEA (3-Key 3DES) | 2048 bits | 224 bits | SHA-224 | 🟡 **Khuyến nghị ngưng dùng sau 2030** |
| **128 bits** | **AES-128** | **3072 bits** | **256 bits (P-256 / Ed25519)** | **SHA-256 / SHA3-256** | 🟢 **Chuẩn Doanh nghiệp Tiêu chuẩn** |
| **192 bits** | **AES-192** | 7688 bits | 384 bits (P-384) | SHA-384 / SHA3-384 | 🟢 **Bảo mật Cấp Chính phủ** |
| **256 bits** | **AES-256** | **15360 bits** | **521 bits (P-521)** | **SHA-512 / SHA3-512** | 🛡️ **Kháng Máy Tính Lượng Tử (Post-Quantum Ready)** |

---

## 2. MA TRẬN CÁC CHẾ ĐỘ MÃ KHỐI (BLOCK CIPHER MODES)

| Chế độ | Viết tắt | Cơ chế hoạt động | Ưu điểm | Nhược điểm / Lỗ hổng | Ứng dụng thực tế |
|:---|:---:|:---|:---|:---|:---|
| **Electronic Codebook** | **ECB** | Mã hóa từng block 128-bit độc lập | Song song hóa, đơn giản | 🔴 **Rò rỉ mẫu dữ liệu cấu trúc (ECB Penguin)** | **CẤM DÙNG** |
| **Cipher Block Chaining** | **CBC** | Khối sau XOR với bản mã trước + IV ngẫu nhiên | Xóa bỏ rò rỉ mẫu | ⚠️ Dễ dính tấn công Padding Oracle (Lucky Thirteen) | IPsec IKEv1, TLS 1.2 (cũ) |
| **Counter Mode** | **CTR** | Mã hóa bộ đếm (Nonce + Counter) thành keystream | Song song hóa cực nhanh, truy cập ngẫu nhiên | 🔴 Lặp Nonce là mất toàn bộ dữ liệu bí mật | Đường truyền tốc độ cao, CPU crypto |
| **Galois/Counter Mode** | **GCM** | CTR mode kết hợp bộ xác thực Galois MAC | **AEAD (Vừa mã hóa vừa bảo vệ toàn vẹn)** | Nhạy cảm với lặp Nonce | **TLS 1.3, IPsec IKEv2, SSHv2, WPA3** |

---

## 3. CÁC HÀM BĂM (ONE-WAY HASH FUNCTIONS) & MAC

- **MD5 (128 bits)**: 🔴 Đã bị bẻ gãy va chạm hoàn toàn (Collision Attack trong vài giây). Tuyệt đối không dùng cho chữ ký số. Chỉ dùng tạm cho checksum file không nhạy cảm hoặc lab cổ điển.
- **SHA-1 (160 bits)**: 🔴 Google & CWI Amsterdam đã công bố cuộc tấn công va chạm SHAttered năm 2017. Bị cấm trên toàn bộ trình duyệt web.
- **SHA-2 (SHA-256, SHA-384, SHA-512)**: 🟢 Cấu trúc Merkle-Damgård. Hiện tại an toàn tuyệt đối, là xương sống của TLS, Bitcoin, DNSSEC và chứng chỉ số X.509.
- **HMAC (Hash-based Message Authentication Code)**: Cơ chế kết hợp khóa bí mật $K$ và hàm băm:
  $$\text{HMAC}(K, M) = H\Big((K \oplus \text{opad}) \parallel H\big((K \oplus \text{ipad}) \parallel M\big)\Big)$$
  Chống tấn công mở rộng chiều dài (Length Extension Attack).
