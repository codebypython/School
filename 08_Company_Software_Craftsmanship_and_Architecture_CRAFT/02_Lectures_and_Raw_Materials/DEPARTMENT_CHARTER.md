# 📜 ĐIỀU LỆ PHÒNG TƯ LIỆU & CA THIẾT KẾ MẪU (LECTURES & RAW MATERIALS DEPT)
## Phòng 02 — Công Ty Thiết Kế Phần Mềm & Kiến Trúc Hướng Đối Tượng (CORP-08-CRAFT)

> **Mã Phòng Ban:** `CRAFT-DEPT-02`  
> **Trưởng phòng phụ trách:** Agent `EKC-03` (Knowledge Curator & Quality Sentinel)  
> **Tiêu chuẩn học liệu:** ER-QVR $\ge 90/100$ | GoF / Fowler Refactoring / Clean Architecture Case Studies

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Tư Liệu là **thư viện nghiên cứu ca điển hình (Case Studies) và tài sản kiến trúc chuẩn mực**:
1. **Lưu Trữ Bài Giảng & Nghiên Cứu Tình Huống Thực Tế**: Phân tích sự tiến hóa của kiến trúc phần mềm trong các hệ thống quy mô lớn (Hệ thống thanh toán, E-Commerce, Microservices).
2. **Kho Lưu Trữ 23 Mẫu Thiết Kế GoF Thực Nghiệm**: Minh họa trực quan sơ đồ tương tác UML và mã nguồn cài đặt mẫu bằng Python/TypeScript/C++.
3. **Danh Mục 24 Code Smells & Biện Pháp Tái Cấu Trúc**: Hệ thống hóa các mùi mã nguồn theo Martin Fowler kèm ví dụ Before / After rõ ràng.

---

## ⚖️ 2. BỘ QUY TẮC BẢO TỒN TƯ LIỆU BẤT BIẾN (CURATION INVARIANTS)

1. **Chuẩn Mực Sơ Đồ UML Hiện Đại (UML Invariant)**:
   - Toàn bộ sơ đồ lớp (Class Diagram) và sơ đồ tuần tự (Sequence Diagram) bắt buộc viết bằng Mermaid.js hoặc PlantUML để có thể render trực tiếp trong Markdown.
2. **Quy Tắc Đối Chiếu Nguồn Gốc (Citation Provenance)**:
   - Mọi case study bắt buộc ghi rõ xuất xứ từ sách Tier A+ trong Knowledge Vault (Ví dụ: `Dive Into Design Patterns, Chapter 4, Observer Pattern`).
3. **Quy Tắc Code Tự Giải Thích (Self-Documenting Code)**:
   - Code mẫu trong tư liệu phải đạt chuẩn Clean Code: đặt tên biến theo Ubiquitous Language, không cần comment thừa giải thích cú pháp.

---

## 🛠️ 3. TOOLCHAIN & QUY TRÌNH SỐ HÓA CA THIẾT KẾ

1. **Vẽ Sơ Đồ**: Mermaid.js, PlantUML CLI, draw.io (xuất SVG).
2. **Định Dạng Mã Nguồn**: Prettier (TypeScript), Black/Ruff (Python), Clang-Format (C++).
3. **Lưu Trữ & Kiểm Duyệt**: Markdown AST Checker qua `holding_system_auditor.py`.

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
02_Lectures_and_Raw_Materials/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 case_studies/                         # Các ca phân tích thiết kế thực tế
│   ├── payment_gateway_architecture.md     # Ca thiết kế cổng thanh toán đa nhà cung cấp
│   └── notification_engine_pubsub.md       # Ca thiết kế động cơ thông báo Publisher-Subscriber
├── 📁 uml_blueprints/                       # Bộ sơ đồ UML chuẩn hóa
│   ├── creational_patterns_uml.md          # Sơ đồ Factory, Builder, Prototype
│   ├── structural_patterns_uml.md          # Sơ đồ Adapter, Decorator, Composite
│   └── behavioral_patterns_uml.md          # Sơ đồ Strategy, Observer, Command
└── 📁 code_smell_catalog/                   # Danh mục 24 Code Smells phân tích chuyên sâu
    ├── bloaters_smells.md                   # Long Method, Large Class, Primitive Obsession
    └── couplers_smells.md                   # Feature Envy, Inappropriate Intimacy
```

---

## 💻 5. MẪU TƯ LIỆU CA THIẾT KẾ MẪU (GOLD MASTER CASE STUDY TEMPLATE)

```markdown
# 🏛️ CA THIẾT KẾ HỆ THỐNG: CỔNG THANH TOÁN ĐA PHƯƠNG THỨC (PAYMENT GATEWAY ENGINE)
> **Mẫu áp dụng:** Strategy Pattern kết hợp Abstract Factory & Adapter Pattern  
> **Nguồn trích:** Dive Into Design Patterns & Clean Architecture Ch. 18

### 1. Bối cảnh Nghiệp vụ (Business Context)
Hệ thống thương mại điện tử cần tích hợp nhiều cổng thanh toán: MoMo, VNPay, Stripe, PayPal. Mỗi cổng có API, chữ ký mã hóa và định dạng phản hồi hoàn toàn khác nhau.

### 2. Vấn đề của Thiết kế Sai (The Anti-Pattern)
Sử dụng chuỗi `if-elif-else` dài 500 dòng trong controller để kiểm tra loại thanh toán, gây vi phạm nghiêm trọng nguyên lý Open/Closed (OCP).

### 3. Giải pháp Kiến trúc Chuẩn (Clean Strategy & Adapter)
- Định nghĩa `PaymentGateway` interface với phương thức `process_payment(request: PaymentRequest) -> PaymentResult`.
- Mỗi nhà cung cấp là một Adapter riêng biệt triển khai interface này.
- Sử dụng `PaymentGatewayFactory` để khởi tạo adapter phù hợp qua Dependency Injection.
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU TƯ LIỆU (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: Toàn bộ sơ đồ UML hiển thị đúng cú pháp Mermaid/PlantUML, không vỡ layout.
- [ ] **DoD-2**: Ghi rõ nguồn trích xuất học thuật đạt chuẩn ER-QVR $\ge 90/100$.
- [ ] **DoD-3**: Có phân tích so sánh trực quan Trước và Sau khi tái cấu trúc (Before vs After).
- [ ] **DoD-4**: Mã nguồn ví dụ đã qua linter và format tự động.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK KHẮC PHỤC SAI LỆCH THIẾT KẾ (CURATION TROUBLESHOOTING RUNBOOK)

Khi phát hiện ca thiết kế hoặc sơ đồ UML bị lỗi logic hoặc truyền tải sai lệch mẫu GoF:
1. **Cô lập ca thiết kế**: Gắn cờ cảnh báo `⚠️ REVIEW NEEDED: Inaccurate Pattern Mapping`.
2. **Đối chiếu kinh điển**: Kiểm tra lại định nghĩa nguyên bản trong GoF Design Patterns hoặc Fowler Refactoring.
3. **Hiệu chỉnh sơ đồ & code**: Viết lại ví dụ phản trực giác thành ví dụ thực chiến mạch lạc.
4. **Xác nhận**: Đảm bảo toàn bộ liên kết nội bộ trong bài giảng hoạt động chính xác.
