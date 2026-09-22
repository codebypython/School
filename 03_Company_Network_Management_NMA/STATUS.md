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
- **Date**: 2026-09-22
- **Work Done**: 
  - Khởi tạo tài liệu Master duy nhất: `Day4/HUONG_DAN_HOAN_CHINH_LAB_4_BANANA_VLSM.md` giải quyết triệt để sự lộn xộn, tích hợp bài giải tự luận chuẩn mực để chép ra giấy, đối chiếu giữa lý thuyết trường (/21, /23, /24) và file thực hành trường (/21, /22, /24).
  - Tái đóng gói và đồng bộ hóa file Packet Tracer `Day4/LAB_4.pkt` tương thích hoàn hảo PT 8.2.2 với đúng bố cục topo, tên thiết bị (`2811 UD CK`, `SWITCH CLASSES`, `Switch LABS`, `Switch OFFICE`, `WRT300N FREE WIFI`, `WRT300N Wireless RADIUS`, `Server CLASSES`, `Server LABS`, `Server RADIUS`, `Smartphone0`, `PC0 LABS`, `Nhan vien 1`, `Nhan vien 2`, `DSL Modem`, `Cloud-PT DSL`, `ISP`, `Google DNS`, `Mail`, `Web`).
  - Xây dựng kịch bản kiểm thử nghiệm thu 7 bước và cẩm nang vấn đáp bảo vệ 10/10.
  - Hạ cấp chữ ký phiên bản thành công cho các tệp `banana collage.pkt`, `Lab 2-Banana College.pkt` (Day 4) và `Lab Cty Banana.pkt` (Day 5: Mô hình OSPF Hà Nội - Đà Nẵng - Sài Gòn) từ bản 9.0.1.0858 xuống bản 8.2.2.0400 tương thích hoàn toàn trên máy sinh viên.
- **Next Priority (P0)**: Sinh viên mở file thực hành trên Cisco Packet Tracer 8.2.2.

