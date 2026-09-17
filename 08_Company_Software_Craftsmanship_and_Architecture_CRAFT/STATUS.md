# 📊 PROJECT STATUS DASHBOARD — SoftwareCraft Corp (CORP-08-CRAFT)

> **Cập nhật lần cuối**: 2026-09-18 | **Tuần hiện tại**: Tuần 1 (Advanced OOP & Clean Abstractions)  
> **Mentor chuyên trách**: DUT Software Craftsmanship & Architecture Mentor (`AGENT_PROFILE.md`)

---

## Current Phase: 🔵 PHASE 1 — OBJECT-ORIENTED EXCELLENCE & SOLID (Tuần 1-6)

Tập trung mổ xẻ 4 trụ cột OOP, thanh lọc tư duy kế thừa sâu, áp dụng nguyên lý Composition over Inheritance và thành thạo bộ nguyên lý SOLID qua mã nguồn thực tế.

---

## Implementation & Lab Progress

### Module 1: OOP Nâng Cao & Tư Duy Hướng Đối Tượng Bản Chất
- [x] Thiết lập bộ công cụ kiểm thử: Pytest (Python), Jest / Vitest (TS), Catch2 (C++)
- [x] 4 Trụ cột OOP: Đóng gói dữ liệu bảo vệ Invariant, Đa hình không phụ thuộc cấu trúc
- [ ] Triệt tiêu "Lớp Thần Thánh" (God Class) & Lạm dụng Getter/Setter (Tell, Don't Ask principle)
- [ ] Composition vs Inheritance: Phân rã bài toán và chứng minh vì sao Composition linh hoạt hơn

### Module 2: Bộ Nguyên Lý SOLID & GRASP Thực Chiến
- [ ] SRP: Tách bạch nghiệp vụ, lưu trữ và hiển thị
- [ ] OCP: Mở rộng tính năng bằng Strategy / Polymorphism không sửa code cũ
- [ ] LSP: Bẫy vi phạm kinh điển Hình chữ nhật vs Hình vuông (Rectangle vs Square)
- [ ] ISP: Phân tách Interface cồng kềnh thành các Role Interfaces tinh gọn
- [ ] DIP: Đảo ngược phụ thuộc qua Abstractions / Dependency Injection

### Module 3: 23 Design Patterns Hiện Đại & TDD
- [ ] Nhóm Khởi tạo (Creational): Factory Method, Abstract Factory, Builder
- [ ] Nhóm Cấu trúc (Structural): Adapter, Decorator, Facade, Composite
- [ ] Nhóm Hành vi (Behavioral): Strategy, Observer, Command, State
- [ ] Vòng lặp TDD (Red-Green-Refactor) & Kỹ thuật Test Doubles (Mocks, Stubs, Fakes)

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | Sinh viên thường viết code trước rồi mới bổ sung Unit Test sau | 🔴 High | Yêu cầu commit Git theo đúng chu trình: Red commit $\rightarrow$ Green commit $\rightarrow$ Refactor commit |

---

## Next Priority (P0)
- Thiết lập starter repo bài tập TDD Tuần 1 (Hệ thống quản lý tài khoản ngân hàng bảo toàn Invariant) trong `03_Engineering_Labs_and_Code/`.
