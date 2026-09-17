# 📊 PROJECT STATUS DASHBOARD — CyberDefense Corp (CORP-04-SEC)

> **Cập nhật lần cuối**: 2026-09-17 | **Tuần hiện tại**: Tuần 1 (Classical Cryptography & Symmetric Ciphers)  
> **Mentor chuyên trách**: DUT Cyber Security Mentor (`AGENT_PROFILE.md`)

---

## Current Phase: 🔵 PHASE 1 — CRYPTOGRAPHY FOUNDATIONS & SYMMETRIC ENCRYPTION (Tuần 1-4)

Tập trung vào Mật mã cổ điển, Đại số modulo, Chuẩn mã hóa dữ liệu nâng cao AES và các chế độ khối (Block Cipher Modes).

---

## Implementation & Lab Progress

### Module 1: Mật Mã Đối Xứng & Hàm Băm
- [x] Thiết lập môi trường Python `cryptography` & Wireshark
- [x] Thuật toán AES-128 / AES-256 (Mô phỏng 4 phép biến đổi SubBytes, ShiftRows, MixColumns, AddRoundKey)
- [ ] So sánh thực nghiệm chế độ AES-ECB vs AES-CBC vs AES-GCM
- [ ] Băm SHA-256 và tạo mã xác thực thông điệp HMAC

### Module 2: Mật Mã Bất Đối Xứng & PKI
- [ ] Cài đặt thuật toán RSA từ Scratch (Số nguyên tố lớn, Nghịch đảo modulo Euclid mở rộng)
- [ ] Thiết lập chứng chỉ số X.509 với OpenSSL (Self-signed CA, Server Certificate)
- [ ] Ký số và xác thực chữ ký số trên tài liệu PDF/văn bản

### Module 3: Giao Thức Mạng & Tường Lửa
- [x] Thiết lập cẩm nang môi trường thực hành 100% miễn phí & mã nguồn mở (GNS3 + VMware Workstation Pro + VyOS + pfSense + Alpine Linux)
- [ ] Cấu hình đường hầm IPsec Site-to-Site VPN trên Router Cisco/VyOS
- [ ] Phân tích bắt tay TLS 1.3 trong Wireshark
- [ ] Triển khai Zone-Based Firewall (ZBF) và danh sách kiểm soát truy cập (ACL)

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | Cần chuẩn bị file pcap mẫu cho bài lab Wireshark TLS | 🟡 Medium | Sẵn sàng trong `data/` |

---

## Last Session
- **Date**: 2026-09-17
- **Work Done**: Ban hành cẩm nang `FREE_TOOLKIT_SETUP_AND_TROUBLESHOOTING_GUIDE.md` tại Phòng 05: Hướng dẫn cài đặt VMware Workstation Pro Free, GNS3 VM, OpenSSL, Python Crypto, cùng Ma trận dự đoán và khắc phục sự cố (Troubleshooting Matrix).
- **Next Priority (P0)**: Thực hiện bài Lab mã hóa ảnh bitmap bằng AES-ECB vs AES-CBC để minh họa trực quan lỗ hổng rò rỉ mẫu dữ liệu.
