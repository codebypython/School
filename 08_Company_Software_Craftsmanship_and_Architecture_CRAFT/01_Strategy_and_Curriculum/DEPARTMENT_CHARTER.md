# 📜 ĐIỀU LỆ PHÒNG CHIẾN LƯỢC & LỘ TRÌNH ĐÀO TẠO (STRATEGY & CURRICULUM DEPT)
## Phòng 01 — Công Ty Thiết Kế Phần Mềm & Kiến Trúc Hướng Đối Tượng (CORP-08-CRAFT)

> **Mã Phòng Ban:** `CRAFT-DEPT-01`  
> **Trưởng phòng phụ trách:** Agent `PSD-04` (Pedagogical Scaffolding Designer) & `ACD-01` (Academic Curriculum Director)  
> **Tiêu chuẩn học thuật:** Gang of Four (GoF) / Refactoring (Fowler) / Unit Testing (Khorikov) / Clean Architecture (Martin)

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Chiến Lược & Lộ Trình là **bộ não định hình kiến trúc phần mềm và kỹ nghệ thủ công**:
1. **Thiết Kế Khung Chương Trình 15 Tuần Chuẩn**: Dẫn dắt học viên từ 4 Trụ cột OOP thực chiến $\rightarrow$ Bộ nguyên lý SOLID & GRASP $\rightarrow$ 23 GoF Design Patterns $\rightarrow$ Lightweight UML $\rightarrow$ TDD & Clean Architecture.
2. **Thanh Lọc Các Kỹ Thuật Lỗi Thời**: Loại bỏ các anti-patterns cổ điển (Singleton bừa bãi, kế thừa quá sâu, biểu đồ UML cồng kềnh kiểu Thác nước), thay thế bằng các mẫu thiết kế hiện đại đa ngôn ngữ (Python, C++, TypeScript).
3. **Đảm Bảo Chuẩn Đầu Ra Kỹ Sư Kiến Trúc**: Đào tạo khả năng phân rã bài toán nghiệp vụ phức tạp thành các module có tính gắn kết cao (High Cohesion) và ít phụ thuộc (Low Coupling).

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (PEDAGOGICAL INVARIANTS)

1. **Tuân Thủ Mô Hình 4 Tầng Sư Phạm**:
   - Mọi tuần học bắt buộc phải có: *Tầng 1 (Bản chất thiết kế)* $\rightarrow$ *Tầng 2 (Cài đặt hiện đại)* $\rightarrow$ *Tầng 3 (⚠️ Cảnh báo Code Smells)* $\rightarrow$ *Tầng 4 (Bài lab TDD nghiệm thu)*.
2. **Nguyên Tắc "Không Độc Tôn Một Ngôn Ngữ"**:
   - Kiến trúc phần mềm là độc lập với ngôn ngữ. Mọi mẫu thiết kế phải được minh họa trên ít nhất 2 ngôn ngữ khác nhau (ví dụ: Python và TypeScript) để chứng minh tính trừu tượng.
3. **Quy Tắc Văn Hóa TDD Tuyệt Đối**:
   - Mọi bài giảng về tính năng mới đều phải dẫn dắt từ việc viết Unit Test mô tả hành vi mong muốn trước khi viết code logic.

---

## 🛠️ 3. TOOLCHAIN & SKILLS ROUTE ĐÀO TẠO KIẾN TRÚC

| Lĩnh Vực | Bộ Công Cụ & Thước Đo | Mục Đích Tác Nghiệp |
| :--- | :--- | :--- |
| **Mô hình hóa Kiến trúc** | PlantUML, Mermaid.js, C4 Model | Trực quan hóa Class/Sequence diagrams tinh gọn |
| **Khung Kiểm thử TDD** | Pytest (Python), Vitest / Jest (TS), Catch2 (C++) | Viết test kiểm chứng hành vi (Behavior-Driven) |
| **Phân tích Tĩnh Code Smell** | SonarQube, Ruff, ESLint, Mypy Strict | Đo lường độ phức tạp Cyclomatic, phát hiện Code Smells |
| **Tái cấu trúc (Refactoring)** | IDE Automated Refactoring (Extract, Inline, Move) | Tái cấu trúc từng bước nhỏ bảo tồn hành vi |

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
01_Strategy_and_Curriculum/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 AGENT_PROFILE.md                      # Hồ sơ năng lực Mentor AI Craftsmanship
├── 📄 ROADMAP_AND_CURRICULUM.md             # Giáo trình Master 15 tuần OOP/Design Patterns
├── 📁 rubrics/                              # Tiêu chí chấm đồ án kiến trúc
│   └── clean_architecture_rubric.md        # Thang điểm đánh giá Clean Architecture & TDD
└── 📁 exam_blueprints/                      # Đề cương kiểm tra năng lực OOAD
    ├── midterm_architecture_blueprint.md   # Đề thi giữa kỳ: SOLID & Refactoring
    └── final_capstone_blueprint.md         # Đề thi cuối kỳ: Design Patterns & Clean Architecture
```

---

## 💻 5. MẪU THIẾT KẾ BÀI HỌC 4 TẦNG QUY CHUẨN (GOLD MASTER SYLLABUS UNIT)

```markdown
### Tuần X: [Tên Mẫu Thiết Kế / Nguyên Lý Kiến Trúc]
- **Tầng 1 (Bản chất thiết kế & Why? - Nguồn: GoF / Fowler)**:
  - Vấn đề thực tế phát sinh khi hệ thống mở rộng (Coupling, Rigidity, Fragility).
  - Bản chất nguyên lý: Trừu tượng hóa hành vi thay vì cài đặt cụ thể.
- **Tầng 2 (Cài đặt Đa ngôn ngữ Python & TypeScript)**:
  - Code mẫu tuân thủ Protocol / Interface rõ ràng, không phụ thuộc framework bên ngoài.
- **Tầng 3 (⚠️ Cảnh báo Code Smell & Anti-patterns)**:
  - Lạm dụng pattern: Patternitis (Áp dụng pattern khi bài toán chưa đủ phức tạp).
  - So sánh giải pháp Sai (Vi phạm SRP/OCP) vs giải pháp Đúng.
- **Tầng 4 (Bài tập Lab TDD & Tiêu chí DoD)**:
  - Đề bài: Viết Unit Test trước, triển khai code sau, đạt Coverage >= 85%.
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU GIÁO TRÌNH (DEFINITION OF READY - DoR)

- [ ] **DoR-1**: Giáo trình có đối chiếu với sách Tier A+ trong Vault (Dive Into Design Patterns, Khorikov Unit Testing).
- [ ] **DoR-2**: Mỗi mẫu Design Pattern đều có sơ đồ Class Diagram chuẩn mực minh họa.
- [ ] **DoR-3**: Đã có starter repo bài tập TDD với test suite viết sẵn kiểm tra hành vi.
- [ ] **DoR-4**: Có mục phân tích các lỗi sai kinh điển khi lạm dụng pattern (Pattern Over-engineering).
- [ ] **DoR-5**: Có câu hỏi phản biện Socratic Dialogue kiểm tra tư duy đánh đổi thiết kế (Trade-offs).

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK GIÁM ĐỊNH LỘ TRÌNH (CURRICULUM TROUBLESHOOTING RUNBOOK)

Khi phát hiện bài giảng hoặc bài lab có dấu hiệu phản mẫu (Anti-pattern) hoặc quá tải nhận thức:
1. **Phát hiện (Detection)**: Sinh viên hoặc Agent Audit phát hiện code mẫu dùng Singleton gây khó khăn cho Unit Testing.
2. **Đình chỉ module (Quarantine)**: Gắn nhãn `⚠️ CODE SMELL UNDER REMEDIATION` tại `STATUS.md`.
3. **Tái cấu trúc (Remediate)**: Chuyển đổi sang Dependency Injection với Factory / IoC Container.
4. **Kiểm chứng (Verification)**: Chạy test suite để đảm bảo test coverage không giảm và tính đóng gói được khôi phục.
