# 🔐 ĐIỀU LỆ HOẠT ĐỘNG: CÔNG TY AN TOÀN THÔNG TIN & TÁC CHIẾN MẠNG (CYBERDEFENSE CORP)
## Company 04: Network Security & Applied Cryptography

> **Mã Doanh Nghiệp:** `CORP-04-SEC`  
> **Tên giao dịch:** CyberDefense & Cryptography Corporation  
> **Lĩnh vực chuyên môn:** Mật mã học ứng dụng (AES, RSA, ECC, SHA-256), Chứng chỉ số X.509/PKI, Giao thức bảo mật TLS 1.3 & IPsec VPN, Danh sách kiểm soát truy cập (ACL), Tường lửa Zone-Based, và Phân tích gói tin Wireshark.  
> **Cố vấn chuyên môn:** Giám Đốc An Toàn Thông Tin & Cố Vấn Học Thuật DUT  
> **Tổng Giám Đốc Điều Hành (CEO):** Sinh viên (Role Handmade)

---

## 1. SỨ MỆNH & TẦM NHÌN (MISSION & VISION)

- **Sứ mệnh**: Trang bị cho sinh viên năng lực bảo vệ toàn diện hệ thống thông tin theo mô hình CIA Triad (Confidentiality, Integrity, Availability). Làm chủ toán mật mã từ gốc, hiểu sâu cấu trúc từng byte trong gói tin mạng và tự tin cấu hình tường lửa, VPN bảo mật cấp doanh nghiệp.
- **Tiêu chuẩn chất lượng**: Đối chiếu và kế thừa 100% tinh hoa từ **Cryptography and Network Security (William Stallings)**, **NIST Special Publications (SP 800-series)**, và **Wireshark Network Analysis (Laura Chappell)**.

---

## 2. CƠ CẤU TỔ CHỨC CÁC PHÒNG BAN (ORGANIZATION BREAKDOWN)

```
04_Company_Network_Security_SEC/
├── 📄 COMPANY_CHARTER.md                    # Bản điều lệ này
├── 📁 01_Strategy_and_Curriculum/            # Phòng Chiến Lược & Giáo Trình 15 Tuần
│   ├── 📄 DEPARTMENT_CHARTER.md
│   └── 📄 ROADMAP_AND_CURRICULUM.md         # Lộ trình 15 tuần chuẩn Stallings/NIST
├── 📁 02_Lectures_and_Raw_Materials/        # Phòng Tư Liệu & Tài Liệu Gốc
│   ├── 📄 DEPARTMENT_CHARTER.md
│   ├── 📄 ACL Samples.pdf                   # Mẫu bài tập và cấu hình ACL
│   ├── 📄 Authentication OSPF.pdf           # Hướng dẫn xác thực OSPF MD5
│   ├── 📄 Authentication EIGRP.pdf          # Hướng dẫn xác thực EIGRP
│   ├── 📄 Authentication RIPv2.pdf          # Hướng dẫn xác thực RIPv2
│   ├── 📄 PPP.pdf                           # Giao thức điểm-nối-điểm & CHAP/PAP
│   └── 🎥 Hướng dẫn GNS3 và Wireshark.mp4   # Video thực hành mô phỏng
├── 📁 03_Engineering_Labs_and_Code/         # Phòng Kỹ Thuật, Code & Thực Nghiệm
│   ├── 📄 DEPARTMENT_CHARTER.md
│   └── 📁 sample for excercise/             # Các bài tập thực hành mẫu
├── 📁 04_Notion_Digital_Workspace/          # Phòng Số Hóa & Không Gian Notion
│   ├── 📄 DEPARTMENT_CHARTER.md
│   └── 📄 NOTION_SEC_SECURITY.md            # Không gian LMS An toàn mạng (Wireshark Log)
└── 📁 05_Troubleshooting_and_Toolkits/      # Phòng Công Cụ & Kiểm Soát Sự Cố
    ├── 📄 DEPARTMENT_CHARTER.md
    ├── 📄 FREE_TOOLKIT_SETUP_AND_TROUBLESHOOTING_GUIDE.md # Cẩm nang cài đặt & fix lỗi 100% Free
    └── 📁 support tools/                    # Công cụ hỗ trợ an ninh mạng
```

---

## 3. QUY TRÌNH PHỐI HỢP & TÁC NGHIỆM CỦA SINH VIÊN

1. **Lý thuyết**: Đọc phần mật mã học và cơ chế giao thức trong `01_Strategy_and_Curriculum/ROADMAP_AND_CURRICULUM.md`.
2. **Thực hành Lab**: Tham chiếu các file PDF cấu hình trong `02_Lectures_and_Raw_Materials/` và làm bài tập trong `03_Engineering_Labs_and_Code/`.
3. **Phân tích Gói tin**: Bắt gói tin bằng Wireshark, chụp màn hình các frame bắt tay 3 bước TCP, TLS Client Hello hoặc IPsec ESP và dán vào `04_Notion_Digital_Workspace/NOTION_SEC_SECURITY.md`.
