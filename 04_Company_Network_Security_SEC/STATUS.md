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
- [x] **Chuẩn hóa toàn diện 4 bài Lab (Day1, Day2, Day3, Day4) theo cấu trúc 6 thành phần vàng**:
  - File cấu hình router/client chuẩn (`*_startup-config.cfg`, `.vpc`, `.gns3`)
  - File mô tả tổng quan học thuật (`*_OVERVIEW.md`)
  - Sơ đồ topo mạng mẫu trực quan (`sodo_*.png`)
  - Bản thiết kế tính toán chuẩn phong cách sinh viên làm tay (`*_BAN_THIET_KE_TINH_TOAN_SINH_VIEN.md`)
  - Bản hướng dẫn thao tác kiểm tra chi tiết (`*_HUONG_DAN_KIEM_TRA_CHI_TIET.md`)
  - Xuất và lưu trữ chính xác file `.pcapng` thực nghiệm + Hướng dẫn phân tích Wireshark (`*_WIRESHARK_PCAPNG_ANALYSIS_GUIDE.md`)
- [x] **Xử lý triệt để lỗi Schema GNS3 RFC 4122 & Đồng bộ hóa VMware Workstation Pro**:
  - Sửa toàn bộ UUID phi chuẩn (`img1`, `L001`, `L002`, `L003`) trong `TACAS.gns3` và `TACAS_cloud_vmnet.gns3` về chuẩn Hex RFC 4122.
  - Chuẩn hóa file cấu hình VMX của 3 máy ảo (`Server2003_LAN2`, `Server2003_LAN3`, `TACAS_Server`) trên `D:\VMware_SEC_Labs`, vượt qua 100% kiểm tra `vmrun checkToolsState`.
  - Đồng bộ danh mục thư viện máy ảo VMware Workstation GUI (`inventory.vmls`), đảm bảo toàn bộ server hiển thị đầy đủ trên thanh điều hướng bên trái ("My Computer").
  - Cập nhật đường dẫn `vmrun_path` trong `gns3_gui.ini` và nạp mẫu thiết bị (template) VMware trong `gns3_controller.ini`.
- [x] **Kiểm toán Chuyên sâu & Chuẩn hóa Toàn bộ 4 Bài Lab Mạng (Day 1 -> Day 4)**:
  - Khởi tạo đồ án GNS3 độc lập `day1/day1.gns3` với 2 router c3725 nạp sẵn startup-config và nhãn mạng chi tiết.
  - Khắc phục lỗi cắm sai cổng trong topology Day 3 (`acl.gns3` & `acl_cloud_vmnet.gns3`): sửa West về `f0/0`, Gateway về `f0/1`, East về `s1/0` đồng bộ hoàn hảo với startup-config.
  - Đồng bộ toàn bộ cấu hình chuẩn vào `project-files/dynamips/` cho Day 2, Day 3, Day 4.
  - Tạo cấu hình tự động cho VPCS `Clients` trong `TACAS/project-files/vpcs/` tránh việc sinh viên phải gõ lại IP bằng tay.
  - Chuẩn hóa toàn bộ 4 tài liệu kiểm tra chi tiết (`*_HUONG_DAN_KIEM_TRA_CHI_TIET.md`) với đầy đủ phần *Lỗi phổ biến sinh viên hay gặp* và *Micro-quiz phản biện* theo chuẩn sư phạm DUT.
- [x] Dọn dẹp sạch toàn bộ file rác, file nháp trùng lặp trong thư mục các lab
- [x] Chuẩn hóa chính sách quản lý Binary nặng (>1GB) bằng `.gitignore` và bảng mã băm SHA-256
- [x] Ban hành Bản cam kết đạo đức an toàn thông tin chuẩn ĐHBK Đà Nẵng (`ETHICAL_SECURITY_POLICY_DUT.md`)

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | Cần chuẩn bị file pcap mẫu cho bài lab Wireshark TLS 1.3 | 🟡 Medium | Sẵn sàng trong `data/` |

---

## Last Session
- **Date**: 2026-09-24
- **Completed**:
  1. Khắc phục triệt để lỗi kết nối chéo cáp trong `Day4-Lab4-hoan chinh/Lab4/Lab4.gns3`: Nối chuẩn `TACACSClient` Fa0/0 <-> `Internet` Fa0/0 (2.2.2.0/24), Fa2/0 <-> `TACACSServer` Cloud VMnet1 (10.0.0.0/24), Fa0/1 <-> `Client` Cloud VMnet2 (192.168.1.0/24).
  2. Cấu hình máy chủ Web Internet 2.2.2.2 hoạt động thực thụ trên Router `Internet` (`ip http server`, `ip route 0.0.0.0 0.0.0.0 2.2.2.1`).
  3. Cấu hình hoàn chỉnh Cisco Auth-Proxy (`ip auth-proxy`, `ip http server`, `aaa authorization auth-proxy default group tacacs+ none`) trên `TACACSClient`.
  4. Mở chế độ Console an toàn (`no login`, `privilege level 15` trên `line con 0`), loại bỏ hoàn toàn nguy cơ bị khóa ngoài (lockout).
  5. Quy chuẩn hóa 100% thông số và tài khoản (`ciscobanana123`, `nhanvien` / `123456`, `Administrator` / `123qwe!@#`, `admin` / `AdminPass123!`).
  6. Biên soạn cẩm nang thực hành và kịch bản demo 4 phần hoàn chỉnh tại `TACACS_AUTH_PROXY_MASTER_PLAYBOOK.md`.
- **In Progress**: Hướng dẫn sinh viên chạy nghiệm thu thực tế với giảng viên.
- **Blockers**: Không có.
- **Next**: Demo toàn diện 4 kịch bản kiểm thử (Web Auth-Proxy 2.2.2.2, Show lệnh Router, Phân quyền Telnet, Nhật ký ACS GUI).



