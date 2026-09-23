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
- [x] **Chuyển dịch 100% Lab 3 (Extended ACL) sang VMware Workstation Pro** (`LAB3_VMWARE_GNS3_MASTER_GUIDE.md`, `acl.gns3`, `acl_cloud_vmnet.gns3`)
- [x] **Chuyển dịch 100% Lab 4 (AAA TACACS+ Banana Corp) sang VMware** (`LAB4_AAA_TACACS_VMWARE_MASTER_GUIDE.md`, `TACAS.gns3`, `TACAS_cloud_vmnet.gns3`)
- [x] **Triển khai tự động 3 máy ảo Server 2003 trên VMware SSD** (`Server2003_LAN2`, `Server2003_LAN3`, `TACAS_Server` tại `D:\VMware_SEC_Labs`)
- [x] **Bộ công cụ & kịch bản tự động hóa VMware Workstation** (`vmware_controller.py` & `VMWARE_AUTOMATION_PLAYBOOK.md`)
- [x] **Cẩm nang & kịch bản gỡ cài đặt sạch sẽ VirtualBox** (`VIRTUALBOX_CLEANUP_AND_UNINSTALL_GUIDE.md`, `uninstall_virtualbox_safely.ps1`)
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
  1. Phân tích chi tiết toàn bộ 4 bài Lab thực chiến và lập ma trận phụ thuộc ảo hóa.
  2. Chuyển đổi toàn diện file topology GNS3 (`acl.gns3`, `TACAS.gns3`) từ `virtualbox` sang `vmware` native và cung cấp bản `cloud_vmnet`.
  3. Triển khai vật lý thành công 100% cả 3 máy ảo Server 2003 từ `Server 2003 R2.ova` vào thư mục `D:\VMware_SEC_Labs` bằng `ovftool` (tự động cấu hình VMnet1, VMnet2, VMnet3).
  4. Cập nhật toàn bộ tài liệu Lab 3, Lab 4, Điều lệ phòng ban theo chuẩn VMware Workstation Pro.
  5. Thiết lập cẩm nang và kịch bản PowerShell tự động dọn dẹp sạch card mạng ảo và gỡ bỏ hoàn toàn VirtualBox (`uninstall_virtualbox_safely.ps1`).
- **Next Priority (P0)**: Chạy script `uninstall_virtualbox_safely.ps1` để giải phóng VirtualBox và tiến hành thực nghiệm Lab 3 / Lab 4 trên VMware.
