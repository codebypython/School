# 📡 ĐIỀU LỆ HOẠT ĐỘNG: CÔNG TY HẠ TẦNG & QUẢN TRỊ MẠNG DOANH NGHIỆP (ENTERPRISE NETADMIN CORP)
## Company 03: Network Management & Infrastructure Operations

> **Mã Doanh Nghiệp:** `CORP-03-NMA`  
> **Tên giao dịch:** Enterprise NetAdmin & Infrastructure Corporation  
> **Lĩnh vực chuyên môn:** Mô hình FCAPS, Quy hoạch IP/Subnetting, Hạ tầng DHCP/DNS/Routing, Active Directory & LDAP, Dịch vụ Web/Mail/NFS, và Giám sát SNMP/Syslog.  
> **Cố vấn chuyên môn tối cao:** **DUT Network Admin Mentor** (Giảng viên kiêm Chuyên gia kỹ thuật hệ thống mạng DUT)  
> **Tổng Giám Đốc Điều Hành (CEO):** Sinh viên (Role Handmade)

---

## 1. SỨ MỆNH & TẦM NHÌN (MISSION & VISION)

- **Sứ mệnh**: Rèn luyện kỹ sư quản trị hạ tầng mạng có bản lĩnh thực chiến cấp doanh nghiệp. Nắm chắc nguyên lý PDU từ Tầng Ứng dụng tới Tầng Vật lý, tự tin thiết kế mạng Enterprise, cấu hình thiết bị Cisco IOS và quản trị máy chủ Windows Server/Linux RHEL chuẩn mực.
- **Tiêu chuẩn chất lượng**: Đối chiếu và kế thừa 100% tinh hoa từ **Cisco CCNA 200-301 (Wendell Odom)**, **Computer Networking: A Top-Down Approach (Kurose-Ross)**, và chuẩn đào tạo chính quy của Khoa CNTT - ĐHBK Đà Nẵng.

---

## 2. CƠ CẤU TỔ CHỨC CÁC PHÒNG BAN (ORGANIZATION BREAKDOWN)

```
03_Company_Network_Management_NMA/
├── 📄 COMPANY_CHARTER.md                    # Bản điều lệ này
├── 📁 01_Strategy_and_Curriculum/            # Phòng Chiến Lược & Hồ Sơ Mentor
│   ├── 📄 DEPARTMENT_CHARTER.md
│   ├── 📄 ROADMAP_AND_CURRICULUM.md         # Lộ trình 15 tuần học chuẩn ĐHBK Đà Nẵng
│   └── 📄 AGENT_PROFILE.md                  # Hồ sơ chuyên gia DUT Network Admin Mentor
├── 📁 02_Lectures_and_Raw_Materials/        # Phòng Bài Giảng Chuyên Đề & Tư Liệu
│   ├── 📄 DEPARTMENT_CHARTER.md
│   ├── 📄 01_co_so_va_fcaps.md              # Chuyên đề 1: FCAPS & Quy hoạch IP
│   ├── 📄 02_ha_tang_cot_loi_*.md           # Chuyên đề 2: DHCP, DNS, Routing
│   ├── 📄 03_dinh_danh_active_directory_*.md# Chuyên đề 3: Active Directory & LDAP
│   ├── 📄 04_dich_vu_ung_dung_*.md          # Chuyên đề 4: Web, Mail, Storage
│   ├── 📄 05_giam_sat_va_bao_mat.md         # Chuyên đề 5: SNMP, Syslog, Firewall
│   └── 📄 bai_trinh_bay_yeu_cau_1_*.md      # Thiết kế phủ sóng Wifi Cafe
├── 📁 03_Engineering_Labs_and_Code/         # Phòng Kỹ Thuật & Phòng Lab Thực Chiến
│   ├── 📄 DEPARTMENT_CHARTER.md
│   ├── 📄 lab_guidelines_and_topologies.md  # Hướng dẫn bài lab & sơ đồ Topo chuẩn
│   └── 📄 common_pitfalls_and_*.md          # Cẩm nang sửa lỗi cấu hình kinh điển
├── 📁 04_Notion_Digital_Workspace/          # Phòng Số Hóa & Không Gian Notion
│   ├── 📄 DEPARTMENT_CHARTER.md
│   ├── 📄 NOTION_NMA_NETWORK_MANAGEMENT.md  # Không gian LMS môn Quản trị mạng
│   ├── 📄 NOTION_STUDY_WORKSPACE_CAFE_WIFI.md
│   └── 📄 NOTION_IMPORT_NMA_CAFE_WIFI.md
└── 📁 05_Troubleshooting_and_Toolkits/      # Phòng Công Cụ & Phần Mềm Hạ Tầng
    ├── 📄 DEPARTMENT_CHARTER.md
    ├── ⚙️ CiscoPacketTracer822_64bit_setup_signed.exe
    └── 📄 chi phí đi dây, chi phí công thợ, c.txt
```

---

## 3. NGUYÊN TẮC BẤT DI BẤT DỊCH CỦA CÔNG TY (DUT MENTOR DIRECTIVES)

1. **Bắt buộc có Bảng phân bổ IP & Sơ đồ Topo mạng** trước khi gõ bất kỳ dòng lệnh CLI nào.
2. **Tuân thủ quy trình 3 bước**: *Bản chất giao thức (Tại sao?) $\rightarrow$ Lệnh cấu hình (Làm thế nào?) $\rightarrow$ Kiểm thử & Bắt gói tin (Xác thực thế nào?)*.
3. **Mỗi bài lab đều phải chụp màn hình kiểm chứng** kết quả lệnh `show ip interface brief`, `show ip route`, `ping`, hoặc Wireshark.
