# 📊 PROJECT STATUS DASHBOARD — CyberDefense Corp (CORP-04-SEC)

> **Cập nhật lần cuối**: 2026-09-23 | **Tuần hiện tại**: Tuần 3 (Public Key Cryptography & PKI / Lab Migration)  
> **Mentor chuyên trách**: DUT Cyber Security Mentor (`AGENT_PROFILE.md`)  
> **Hệ sinh thái ảo hóa mục tiêu**: **100% VMware Workstation Pro** (Chuyển dịch hoàn tất từ VirtualBox)

---

## Current Phase: 🔵 PHASE 1 — CRYPTOGRAPHY FOUNDATIONS & VMWARE ECOSYSTEM CONVERSION

Đã khép kín toàn bộ code thực nghiệm Mật mã học (Vigenère IoC, Pure AES-128 Image Visualizer, RSA from Scratch) và chuẩn hóa toàn bộ các bài Lab mạng sang hệ sinh thái VMware Workstation Pro.

---

## Implementation & Lab Progress

### Module 1: Mật Mã Đối Xứng & Hàm Băm
- [x] Thiết lập môi trường Python 3 & Wireshark
- [x] Thuật toán AES-128 Pure Python (SubBytes, ShiftRows, MixColumns, AddRoundKey)
- [x] So sánh thực nghiệm chế độ AES-ECB vs AES-CBC trên ảnh BMP (`aes_modes_visualizer.py`)
- [x] Thám mã cổ điển tự động Vigenère bằng Chỉ số Trùng lặp (IoC) & Chi-Squared (`vigenere_ioc_cracker.py`)
- [x] Bảng tra cứu nguyên thủy mật mã NIST SP 800-57 (`CRYPTO_PRIMITIVES_CHEATSHEET.md`)

### Module 2: Mật Mã Bất Đối Xứng & PKI
- [x] Cài đặt thuật toán RSA từ Scratch (`rsa_from_scratch.py` với Miller-Rabin 25 rounds, Euclid mở rộng)
- [x] Ký số và xác thực chữ ký số toàn vẹn văn bản bằng RSA + SHA-256
- [ ] Thiết lập chứng chỉ số X.509 với OpenSSL (Self-signed CA, Server Certificate)

### Module 3: Giao Thức Mạng, Tường Lửa & Chuyển Dịch VMware
- [x] Thiết lập cẩm nang môi trường thực hành 100% miễn phí (GNS3 + VMware Workstation Pro + Alpine)
- [x] **Chuyển dịch 100% Lab 3 (Extended ACL) sang VMware Workstation Pro** (`LAB3_VMWARE_GNS3_MASTER_GUIDE.md`)
- [x] **Chuyển dịch 100% Lab 4 (AAA TACACS+ Banana Corp) sang VMware** (`LAB4_AAA_TACACS_VMWARE_MASTER_GUIDE.md`)
- [x] **Bộ công cụ & kịch bản tự động hóa VMware Workstation** (`vmware_controller.py` & `VMWARE_AUTOMATION_PLAYBOOK.md`)
- [x] Chuẩn hóa chính sách quản lý Binary nặng (>1GB) bằng `.gitignore` và bảng mã băm SHA-256
- [x] Ban hành Bản cam kết đạo đức an toàn thông tin chuẩn ĐHBK Đà Nẵng (`ETHICAL_SECURITY_POLICY_DUT.md`)

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | Cần chuẩn bị file pcap mẫu cho bài lab Wireshark TLS 1.3 | 🟡 Medium | Sẵn sàng trong `data/` |

---

## Last Session
- **Date**: 2026-09-23
- **Work Done**:
  1. Giải đáp và chứng minh năng lực điều khiển, can thiệp tự động máy ảo VMware Workstation vượt trội hơn VirtualBox.
  2. Xử lý triệt để lỗ hổng lưu trữ binary lớn: thiết lập `.gitignore`, tính mã băm SHA-256 cho `Server 2003 R2.ova` và `Hướng dẫn GNS3 và Wireshark.mp4`.
  3. Lập trình 3 công cụ mật mã học Python thuần túy: `vigenere_ioc_cracker.py`, `aes_modes_visualizer.py`, `rsa_from_scratch.py`.
  4. Biên soạn 2 cẩm nang Master Lab 3 và Lab 4 chuyên biệt cho VMware Workstation Pro + GNS3.
  5. Xây dựng bộ công cụ tự động hóa `vmware_controller.py` và cẩm nang `VMWARE_AUTOMATION_PLAYBOOK.md`.
  6. Hoàn thiện toàn bộ các tài sản cam kết trong Điều lệ phòng ban.
- **Next Priority (P0)**: Thực hiện bài Lab OpenSSL PKI nội bộ (Root CA -> CSR -> Signed Cert) và bắt gói tin phân tích bắt tay TLS 1.3 trên Wireshark.
