# ⚡ ĐIỀU LỆ HOẠT ĐỘNG: CÔNG TY HỆ THỐNG & GIẢI THUẬT HIỆU NĂNG CAO (ALGOCORE SYSTEMS CORP)
## Company 07: Algorithms, Data Structures & Systems Engineering

> **Mã Doanh Nghiệp:** `CORP-07-ALGO`  
> **Tên giao dịch:** AlgoCore Systems Corporation  
> **Lĩnh vực chuyên môn:** Cấu trúc Dữ liệu & Giải thuật chuyên sâu (DSA), Thiết kế Thuật toán (CLRS), Kỹ thuật Lập trình Bậc thấp, Quản trị Bộ nhớ, C++20 Standard, Cache Locality & Concurrency.  
> **Cố vấn chuyên môn:** DUT Algorithmic & Systems Mentor (`AGENT_PROFILE.md`)  
> **Tổng Giám Đốc Điều Hành (CEO):** Sinh viên (Role Handmade)

---

## 1. SỨ MỆNH & TẦM NHÌN (MISSION & VISION)

- **Sứ mệnh**: Xây dựng nền móng tư duy kỹ thuật máy tính vững chắc nhất cho sinh viên CNTT Bách Khoa: Đập tan tư duy "giải thuật toán trên giấy", kết nối phân tích tiệm cận Big-O với kiến trúc phần cứng thực tế (Memory Hierarchy, Cache, Pointers, Multithreading).
- **Tiêu chuẩn học thuật**:
  - Lý thuyết thuật toán: Đối chiếu 100% tinh hoa từ **CLRS (Introduction to Algorithms 4th ed, MIT Press)** và **Steven Skiena (The Algorithm Design Manual 3rd ed)**.
  - Tiêu chuẩn mã nguồn: Tuân thủ **C++20 & C++ Core Guidelines** (Bjarne Stroustrup & Herb Sutter), triệt tiêu con trỏ trần (`raw pointer`) gây rò rỉ bộ nhớ, làm chủ RAII và Smart Pointers.

---

## 2. CƠ CẤU TỔ CHỨC CÁC PHÒNG BAN (ORGANIZATION BREAKDOWN)

```
07_Company_Algorithms_and_Systems_ALGO/
├── 📄 COMPANY_CHARTER.md                    # Bản điều lệ này
├── 📄 STATUS.md                             # Bảng theo dõi tiến độ thời gian thực
├── 📁 01_Strategy_and_Curriculum/            # Phòng Chiến Lược & Lộ Trình Đào Tạo
│   ├── 📄 DEPARTMENT_CHARTER.md
│   ├── 📄 AGENT_PROFILE.md                  # Hồ sơ năng lực & Persona DUT Mentor C++
│   └── 📄 ROADMAP_AND_CURRICULUM.md         # Khung chương trình 15 tuần chuẩn hóa
├── 📁 02_Lectures_and_Raw_Materials/        # Phòng Tư Liệu & Barem Thuật Toán
│   └── 📄 DEPARTMENT_CHARTER.md
├── 📁 03_Engineering_Labs_and_Code/         # Phòng Kỹ Thuật, Mã Nguồn & Test Suites
│   └── 📄 DEPARTMENT_CHARTER.md
├── 📁 04_Notion_Digital_Workspace/          # Phòng Số Hóa & Không Gian Notion LMS
│   └── 📄 DEPARTMENT_CHARTER.md
└── 📁 05_Troubleshooting_and_Toolkits/      # Phòng Kiểm Soát Lỗi Bộ Nhớ & Debugging
    └── 📄 DEPARTMENT_CHARTER.md
```

---

## 3. QUY TRÌNH PHỐI HỢP & TÁC NGHIỆM CỦA HỌC VIÊN

1. **Định hướng tuần**: Mở `01_Strategy_and_Curriculum/ROADMAP_AND_CURRICULUM.md` để nắm các chứng minh Big-O và cấu trúc dữ liệu mục tiêu.
2. **Nghiên cứu bản chất**: Đọc các chương tương ứng từ CLRS / CS:APP được chỉ định trong Knowledge Vault.
3. **Thực hành Code & Kiểm thử**: Viết mã nguồn C++20 trong `03_Engineering_Labs_and_Code/`, bắt buộc chạy qua AddressSanitizer (ASan) hoặc Valgrind để đảm bảo 0 byte memory leak.
4. **Active Recall**: Trả lời câu hỏi phản biện cuối mỗi bài lab với Mentor AI.
