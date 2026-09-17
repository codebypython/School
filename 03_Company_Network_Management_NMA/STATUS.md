# 📊 PROJECT STATUS DASHBOARD — NetAdmin Corp (CORP-03-NMA)

> **Cập nhật lần cuối**: 2026-09-13 | **Tuần hiện tại**: Tuần 1 (Network Fundamentals & Topo Planning)  
> **Mentor chuyên trách**: DUT Network Admin Mentor (`01_Strategy_and_Curriculum/AGENT_PROFILE.md`)

---

## Current Phase: 🔵 PHASE 1 — INFRASTRUCTURE & CORE SERVICES (Tuần 1-4)

Tập trung vào quy hoạch IP, Subnetting VLSM, cấu hình định tuyến cơ bản và dịch vụ lõi DHCP/DNS.

---

## Implementation & Lab Progress

### Module 1: Cơ Sở Hạ Tầng & Dịch Vụ Mạng Cốt Lõi
- [x] Quy hoạch Bảng phân bổ IP & Topo mạng doanh nghiệp mẫu
- [x] Cấu hình DHCP Server (DORA, Scope, Reservation, Relay Agent)
- [ ] Cấu hình DNS Server (Forward/Reverse Lookup, MX, CNAME, Root Hints)
- [ ] Định tuyến tĩnh & Inter-VLAN Routing (Router-on-a-stick / SVI)

### Module 2: Định Danh & Thư Mục (Directory Services)
- [ ] Cài đặt Windows Server 2022 Active Directory Domain Services (AD DS)
- [ ] Thiết kế Organizational Units (OU), User/Group & Group Policy Objects (GPO)
- [ ] Tích hợp máy trạm Windows 10/11 và Ubuntu Linux vào Domain

### Module 3: Dịch Vụ Ứng Dụng & Giám Sát
- [ ] Triển khai Web Server IIS / Nginx (SSL/TLS HTTPS)
- [ ] File Server SMB/NFS & Phân quyền ma trận NTFS vs Share Permissions
- [ ] Giám sát mạng với SNMPv3, Syslog Server & Bắt gói tin Wireshark

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | File máy ảo Windows Server 2022 dung lượng lớn | 🟡 Medium | Cần dọn dẹp dung lượng ổ đĩa trước khi clone |

---

## Last Session
- **Date**: 2026-09-15
- **Work Done**: 
  - Hoàn thiện bản thiết kế chính thức Lab Day 1 và xuất bản tệp tài liệu Word kỹ thuật đơn sắc chuẩn mực: `Day1/Bao_Cao_Thiet_Ke_Cafe_Wifi_Lab_1.docx` (đầy đủ các bước tính toán hình học, vùng phủ Wi-Fi 6, quy hoạch IP/DHCP, tính toán băng thông 800 Mbps, phân bổ tần số chống nhiễu, bóc tách dự toán BoQ 18.288.000 VNĐ và lệnh Cisco IOS).
  - Phân tích chi tiết 4 hình ảnh tính toán bài Lab 4 Trường Cao Đẳng Banana, tái thiết kế lại toàn bộ quy hoạch mạng VLSM chuẩn mực (/21, /23, /24) và xuất bản `Day4/Bao_Cao_Thiet_Ke_VLSM_Lab_4_Banana.docx`.
  - Biên soạn và xuất bản **Giáo trình Sư phạm Chuyên sâu VLSM & Thiết kế Lab 4**: `Day4/Giao_Trinh_Su_Pham_Chuyen_Sau_VLSM_Lab_4.docx` (~51 KB).
  - Xây dựng **Biểu mẫu Chuẩn Tính toán & Thiết kế Phân hoạch Mạng VLSM (Master Template)** tại `03_Engineering_Labs_and_Code/VLSM_CALCULATION_AND_DESIGN_TEMPLATE.md`.
  - **Khắc phục triệt để lỗi không mở được file Packet Tracer Lab 4**: Điều tra phát hiện `LAB_4.pkt` gốc được lưu bằng Cisco Packet Tracer 9.0.0.0810 trong khi máy tính cài đặt Cisco Packet Tracer 8.2.2.0400. Đã giải mã nhị phân, hạ cấp phiên bản tương thích và tạo các phiên bản hoàn chỉnh: `LAB_4.pkt` (tương thích PT 8.2.2), `LAB_4_v822_Goc.pkt`, `LAB_4_v822_Pure_VLSM.pkt` và backup an toàn `LAB_4_orig_v9.pkt`. Đã kiểm thử khởi động mượt mà trên Packet Tracer 8.2.2.
- **Next Priority (P0)**: Sinh viên mở file `LAB_4.pkt` đã chuyển đổi trên máy và kiểm tra mô phỏng trực tiếp.
