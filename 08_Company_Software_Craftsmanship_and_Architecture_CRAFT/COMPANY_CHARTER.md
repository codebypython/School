# 📐 ĐIỀU LỆ HOẠT ĐỘNG: CÔNG TY THIẾT KẾ PHẦN MỀM & KIẾN TRÚC HƯỚNG ĐỐI TƯỢNG (SOFTWARECRAFT CORP)
## Company 08: Software Craftsmanship, Architecture, OOAD & TDD

> **Mã Doanh Nghiệp:** `CORP-08-CRAFT`  
> **Tên giao dịch:** SoftwareCraft Architecture Corporation  
> **Lĩnh vực chuyên môn:** Lập trình Hướng đối tượng nâng cao (OOP), Phân tích & Thiết kế Hướng đối tượng (OOAD), Nguyên lý SOLID & GRASP, 23 Design Patterns (GoF), Phát triển Hướng Kiểm thử (TDD), Refactoring & Clean Architecture.  
> **Cố vấn chuyên môn:** DUT Software Craftsmanship & Architecture Mentor (`AGENT_PROFILE.md`)  
> **Tổng Giám Đốc Điều Hành (CEO):** Sinh viên (Role Handmade)

---

## 1. SỨ MỆNH & TẦM NHÌN (MISSION & VISION)

- **Sứ mệnh**: Đào tạo kỹ sư phần mềm đạt trình độ **"Thợ thủ công phần mềm" (Software Craftsman)**: Biết mô hình hóa bài toán nghiệp vụ phức tạp, thiết kế hệ thống module hóa cao (Low Coupling, High Cohesion), kiểm thử tự động toàn diện qua TDD và tự tin tái cấu trúc mã nguồn liên tục mà không sợ vỡ hệ thống.
- **Tiêu chuẩn học thuật**:
  - Đối chiếu nguyên lý từ **Design Patterns (GoF 1994)** kết hợp phiên bản cập nhật trực quan **Dive Into Design Patterns (2020+)**.
  - Tiêu chuẩn kiểm thử hiện đại: Áp dụng triết lý từ **Unit Testing Principles, Practices, and Patterns (Vladimir Khorikov, 2020)** và **Refactoring 2nd ed (Martin Fowler, 2018)**.

---

## 2. CƠ CẤU TỔ CHỨC CÁC PHÒNG BAN (ORGANIZATION BREAKDOWN)

```
08_Company_Software_Craftsmanship_and_Architecture_CRAFT/
├── 📄 COMPANY_CHARTER.md                    # Bản điều lệ này
├── 📄 STATUS.md                             # Bảng theo dõi tiến độ thời gian thực
├── 📁 01_Strategy_and_Curriculum/            # Phòng Chiến Lược & Lộ Trình Đào Tạo
│   ├── 📄 DEPARTMENT_CHARTER.md
│   ├── 📄 AGENT_PROFILE.md                  # Hồ sơ năng lực & Persona DUT Mentor OOP/TDD
│   └── 📄 ROADMAP_AND_CURRICULUM.md         # Khung chương trình 15 tuần chuẩn hóa
├── 📁 02_Lectures_and_Raw_Materials/        # Phòng Tư Liệu & Ca Thiết Kế Mẫu
│   └── 📄 DEPARTMENT_CHARTER.md
├── 📁 03_Engineering_Labs_and_Code/         # Phòng Kỹ Thuật, TDD Starters & Refactoring
│   └── 📄 DEPARTMENT_CHARTER.md
├── 📁 04_Notion_Digital_Workspace/          # Phòng Số Hóa & Không Gian Notion LMS
│   └── 📄 DEPARTMENT_CHARTER.md
└── 📁 05_Troubleshooting_and_Toolkits/      # Phòng Kiểm Soát Code Smells & Linter
    └── 📄 DEPARTMENT_CHARTER.md
```

---

## 3. QUY TRÌNH PHỐI HỢP & TÁC NGHIỆM CỦA HỌC VIÊN

1. **Phân tích yêu cầu**: Nhận User Scenarios, phác thảo Domain Model và Lightweight Class Diagram.
2. **Viết Test trước (Red Phase)**: Viết các Unit Test kiểm chứng hành vi mong muốn trước khi viết code logic.
3. **Viết Code tối thiểu (Green Phase)**: Viết code để pass toàn bộ test case.
4. **Tái cấu trúc (Refactor Phase)**: Áp dụng SOLID, khử trừ Code Smells, chuẩn hóa tên gọi và tách hàm/lớp an toàn.
