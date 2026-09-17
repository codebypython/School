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

## ⚖️ 2. BỘ QUY TẮC SƯ PHẠM BẤT BIẾN (PEDAGOGICAL HARD CONSTRAINTS)

1. **Tuân Thủ Mô Hình 4 Tầng Sư Phạm**:
   - Mọi tuần học bắt buộc phải có: *Tầng 1 (Bản chất thiết kế)* $\rightarrow$ *Tầng 2 (Cài đặt hiện đại)* $\rightarrow$ *Tầng 3 (⚠️ Cảnh báo Code Smells)* $\rightarrow$ *Tầng 4 (Bài lab TDD nghiệm thu)*.
2. **Nguyên Tắc "Không Độc Tôn Một Ngôn Ngữ"**:
   - Kiến trúc phần mềm là độc lập với ngôn ngữ. Mọi mẫu thiết kế phải được minh họa trên ít nhất 2 ngôn ngữ khác nhau (ví dụ: Python và TypeScript) để chứng minh tính trừu tượng.
3. **Quy Tắc Văn Hóa TDD Tuyệt Đối**:
   - Mọi bài giảng về tính năng mới đều phải dẫn dắt từ việc viết Unit Test mô tả hành vi mong muốn trước khi viết code logic.

---

## 🛡️ 3. TIÊU CHÍ NGHIỆM THU GIÁO TRÌNH (DEFINITION OF READY - DoR)

- [ ] **DoR-1**: Giáo trình có đối chiếu với sách Tier A+ trong Vault (Dive Into Design Patterns, Khorikov Unit Testing).
- [ ] **DoR-2**: Mỗi mẫu Design Pattern đều có sơ đồ Class Diagram chuẩn mực minh họa.
- [ ] **DoR-3**: Đã có starter repo bài tập TDD với test suite viết sẵn kiểm tra hành vi.
- [ ] **DoR-4**: Có mục phân tích các lỗi sai kinh điển khi lạm dụng pattern (Pattern Over-engineering).
