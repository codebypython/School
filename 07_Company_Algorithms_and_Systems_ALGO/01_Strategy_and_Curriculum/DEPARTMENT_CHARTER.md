# 📜 ĐIỀU LỆ PHÒNG CHIẾN LƯỢC & LỘ TRÌNH ĐÀO TẠO (STRATEGY & CURRICULUM DEPT)
## Phòng 01 — Công Ty Hệ Thống & Giải Thuật Hiệu Năng Cao (CORP-07-ALGO)

> **Mã Phòng Ban:** `ALGO-DEPT-01`  
> **Trưởng phòng phụ trách:** Agent `PSD-04` (Pedagogical Scaffolding Designer) & `ACD-01` (Academic Curriculum Director)  
> **Cơ quan giám định:** Hội Đồng AI AOC Tập Đoàn School Holdings  
> **Tiêu chuẩn học thuật:** ACM/IEEE Computing Curricula / CLRS / CS:APP / Stanford CS106B / DUT Standards

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Chiến Lược & Lộ Trình Đào Tạo là **bộ não định hướng học thuật** của AlgoCore Systems Corp:
1. **Thiết kế & Bảo trì Khung Chương trình 15 Tuần**: Đảm bảo lộ trình có tính giàn giáo (Scaffolding), dẫn dắt học viên từ mức độ phần cứng bậc thấp (Memory, Pointers) đến cấu trúc dữ liệu kinh điển và thuật toán đồ thị, quy hoạch động nâng cao.
2. **Kiểm Soát Tính Tiên Tiến Của Tri Thức**: Loại bỏ triệt để các kỹ thuật C++ cổ điển trước C++11, cập nhật 100% sang chuẩn **C++20 & C++ Core Guidelines**.
3. **Thẩm Định Nguồn Học Liệu Theo ER-QVR 100 Điểm**: Mọi bài giảng, bài tập đều phải có nguồn đối chiếu từ các sách Tier A+ trong `00_Corporate_Knowledge_Vault` (CLRS, Skiena, Stroustrup, CS:APP).

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN (PEDAGOGICAL HARD CONSTRAINTS)

Mọi bài học, tài liệu giảng dạy hoặc đề cương do Agent khởi tạo tại phòng ban này **BẮT BUỘC PHẢI THỎA MÃN**:

1. **Tuân Thủ Tuyệt Đối Mô Hình 4 Tầng Sư Phạm**:
   - **Tầng 1 (Bản chất lý thuyết & Why?)**: Xuất xứ toán học, chứng minh Big-O từ CLRS.
   - **Tầng 2 (Cài đặt C++20 How?)**: Mã nguồn hiện đại, RAII, Smart Pointers, Concepts.
   - **Tầng 3 (⚠️ Cảnh báo bẫy lỗi thời & Anti-patterns)**: Chỉ rõ code C++98 cũ hoặc lỗi tràn bộ nhớ mà sinh viên hay mắc phải.
   - **Tầng 4 (Thực hành Lab & Definition of Done)**: Đề bài Lab với bộ test cases cụ thể.
2. **Nguyên Tắc Bậc Thang Nhận Thức (Bloom's Taxonomy Scaffolding)**:
   - Không nhảy cóc: Phải hiểu Stack/Heap và Pointer ở Tuần 1-3 trước khi tự cài đặt Danh sách liên kết và Cây nhị phân ở Tuần 4-7.
3. **Tính Độc Lập Khỏi Thư Viện Cổ Điển**:
   - Nghiêm cấm đưa vào giáo trình các thư viện lỗi thời (`<conio.h>`, `malloc.h`, `<string.h>` kiểu C). Bắt buộc dùng Header chuẩn C++20 (`<span>`, `<string_view>`, `<memory>`, `<concepts>`, `<ranges>`).

---

## 🛠️ 3. SKILLS ROUTE & MA TRẬN CHUYÊN MÔN MENTOR

Khi Agent nhận diện tag `[CORP-07-ALGO]`, Agent phải kích hoạt **DUT Algorithmic & Systems Mentor Persona** với các năng lực:

| Năng Lực Cốt Lõi | Công Cụ & Thước Đo | Mục Đích Sư Phạm |
| :--- | :--- | :--- |
| **Phân tích Tiệm Cận (Asymptotic Analysis)** | Định lý Thợ (Master Theorem), Phân tích Khấu hao (Amortized Analysis) | Chứng minh độ phức tạp toán học trước khi lập trình |
| **Giải Phẫu Bộ Nhớ (Memory Anatomy)** | Sơ đồ Stack Frame, Virtual Address Space, Cache Line | Hiểu tường tận vị trí biến và chu kỳ giải phóng |
| **Phương Pháp Socratic Dialogue** | Bộ câu hỏi gợi mở, truy vấn nguyên nhân gốc rễ (Root Cause) | Không đưa code giải sẵn, giúp học viên tự tìm ra giải pháp |
| **Kiểm Thử Chẩn Đoán (Diagnostic Testing)** | Catch2 assertion analysis, GDB trace inspection | Hướng dẫn học viên tự debug khi dính lỗi Segfault |

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
01_Strategy_and_Curriculum/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 AGENT_PROFILE.md                      # Hồ sơ năng lực chi tiết của Mentor AI
├── 📄 ROADMAP_AND_CURRICULUM.md             # Giáo trình Master 15 tuần hoàn chỉnh
├── 📁 rubrics/                              # Bộ tiêu chí đánh giá bài tập & đồ án
│   ├── lab_evaluation_rubric.md             # Thang điểm chấm bài lab (Chức năng, Memory, Clean Code)
│   └── capstone_kvstore_rubric.md           # Thang điểm đồ án tốt nghiệp In-Memory KV Store
└── 📁 exam_blueprints/                      # Ma trận đề thi trắc nghiệm & tự luận thuật toán
    ├── midterm_exam_blueprint.md            # Đề cương thi giữa kỳ (DSA cơ bản & Memory)
    └── final_exam_blueprint.md              # Đề cương thi cuối kỳ (Đồ thị, DP & Concurrency)
```

---

## 💻 5. MẪU THIẾT KẾ BÀI HỌC 4 TẦNG QUY CHUẨN (GOLD MASTER SYLLABUS UNIT)

Agent khi soạn thảo thêm bài học mới phải bám sát cấu trúc chuẩn hóa sau:

```markdown
### Tuần X: [Tên Chủ Đề Chuyên Môn]
- **Tầng 1 (Lý thuyết kinh điển - Nguồn: CLRS Ch.X)**:
  - Bản chất toán học / Thuật toán: [Giải thích logic, công thức truy hồi, chứng minh Big-O]
  - Phân tích tiệm cận: Best Case $\Omega(...)$, Average $\Theta(...)$, Worst Case $O(...)$.
- **Tầng 2 (Cú pháp & Chuẩn C++20 hiện đại)**:
  - Sử dụng các tính năng: [Liệt kê Smart Pointer, Range, Concept cụ thể].
  - Code mẫu có chú thích giải thích vòng đời tài nguyên.
- **Tầng 3 (⚠️ Cảnh báo bẫy lỗi thời & Anti-patterns)**:
  - Bẫy kinh điển: [Mô tả chi tiết nguyên nhân crash hoặc rò rỉ bộ nhớ].
  - Ví dụ code SAI vs code ĐÚNG.
- **Tầng 4 (Thực hành Lab & Definition of Done)**:
  - Đề bài: [Mô tả yêu cầu chức năng].
  - Tiêu chí nghiệm thu (DoD): Chạy pass test suite, 0 byte memory leak qua AddressSanitizer.
```

---

## 🛡️ 6. BỘ TIÊU CHÍ DUYỆT BÀI GIẢNG & LỘ TRÌNH (DEFINITION OF READY - DoR)

Trước khi một tuần học được phát hành cho học viên:
- [ ] **DoR-1**: Đã đối chiếu tối thiểu 1 tài liệu Tier A+ trong Knowledge Vault.
- [ ] **DoR-2**: Mã nguồn ví dụ đã được biên dịch thử nghiệm trên GCC 13 với `-Werror`.
- [ ] **DoR-3**: Đã có ít nhất 1 bài tập Lab đi kèm bộ test case tự động.
- [ ] **DoR-4**: Có mục cảnh báo bẫy sai lầm kinh điển sinh viên hay gặp.
- [ ] **DoR-5**: Có câu hỏi gợi mở phản biện (Micro-quiz) kiểm tra mức độ thấu hiểu.
