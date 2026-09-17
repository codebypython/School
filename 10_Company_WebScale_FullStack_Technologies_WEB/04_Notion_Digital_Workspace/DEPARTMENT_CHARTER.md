# 📜 ĐIỀU LỆ PHÒNG SỐ HÓA & KHÔNG GIAN NOTION LMS (NOTION DIGITAL WORKSPACE DEPT)
## Phòng 04 — Công Ty Công Nghệ Web Full-Stack & Hệ Sinh Thái JS/TS (CORP-10-WEB)

> **Mã Phòng Ban:** `WEB-DEPT-04`  
> **Trưởng phòng phụ trách:** Agent `NKA-05` (Notion Architect & Hub Administrator)  
> **Hệ sinh thái liên kết:** Central Notion LMS Hub (`00_Central_Notion_LMS_Hub`)  
> **Tiêu chuẩn công nghệ:** Notion Formula 2.0 / Web Project Kanban / Active Recall Flashcards

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Số Hóa là **trung tâm quản trị học tập số** cho kỹ sư Web Full-Stack:
1. **Quản Trị Tiến Độ Dự Án Full-Stack (Full-Stack Roadmap DB)**: Theo dõi tiến độ hoàn thành các module từ JavaScript cơ bản đến Next.js và NestJS.
2. **Kho Bảng Tra Cứu Số Hóa (Cheat Sheets Vault)**: Số hóa danh mục TypeScript Utility Types, React Hooks lifecycle, và bảng mã trạng thái HTTP.
3. **Hệ Thống Flashcards Lặp Lại Ngắt Quãng (Web Core Flashcards)**: Sử dụng Notion Formula 2.0 để tự động lên lịch kiểm tra kiến thức về Event Loop, Closures, và CSS Box Model.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (NOTION INVARIANTS)

1. **Chuẩn Mực Khối Mã Lệnh (Code Block Invariant)**:
   - Toàn bộ code snippet trong trang Notion bắt buộc phải được khai báo đúng ngôn ngữ (TypeScript hoặc TSX).
2. **Quy Chuẩn CSDL Quan Hệ Hai Chiều**:
   - Mọi dự án Full-Stack phải có thuộc tính quan hệ trỏ về `Subjects Database` của Central LMS Hub.
3. **Công Thức Formula 2.0 Chuẩn Xác**:
   - Mọi công thức tính toán tiến độ hoặc Spaced Repetition phải sử dụng chuẩn Formula 2.0.

---

## 🛠️ 3. TOOLCHAIN & KỸ NĂNG VẬN HÀNH NOTION LMS

1. **Bộ Công Cụ**: Notion API v2022-06-28, TypeScript Notion SDK.
2. **Kiểm Tra Cú Pháp**: Notion Formula Linter trong Central LMS Hub.
3. **Môi Trường Sandbox**: Workspace Notion riêng biệt cho WebScale Corp.

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
04_Notion_Digital_Workspace/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 NOTION_WEBSCALE_TRACKER_SCHEMA.md     # Cấu trúc CSDL theo dõi tiến độ Web
├── 📁 flashcards_vault/                     # Ngân hàng câu hỏi Active Recall
│   ├── typescript_types_flashcards.md      # Flashcards Generics & Utility Types
│   └── react_hooks_lifecycle_flashcards.md # Flashcards React Lifecycle & State
└── 📁 page_templates/                       # Mẫu trang kỹ thuật Notion
    ├── api_specification_template.md       # Mẫu đặc tả REST/GraphQL API
    └── frontend_component_spec_template.md # Mẫu tài liệu thiết kế UI Component
```

---

## 💻 5. MẪU THIẾT KẾ SCHEMA CSDL & CÔNG THỨC NOTION 2.0 (GOLD MASTER NOTION)

```markdown
# 📊 CSDL QUẢN LÝ TIẾN ĐỘ BÀI LAB WEB (WEBSCALE LAB TRACKER)

### Thuộc tính bảng (Properties Schema):
1. `Lab Name` (Title): Tên bài lab (VD: 01. Event Loop & Macrotasks).
2. `Tech Stack` (Multi-select): TypeScript, React, Next.js, NestJS, Tailwind.
3. `Test Coverage` (Number): Phần trăm kiểm thử đạt được.
4. `Status` (Status): Not Started, Coding, Reviewing, Completed.
5. `Last Reviewed` (Date): Ngày ôn tập gần nhất.

### 🧮 Công thức Formula 2.0: Spaced Repetition Scheduling:
```notion
lets(
  interval, if(prop("Status") == "Completed", 14, if(prop("Status") == "Reviewing", 3, 1)),
  dateAdd(prop("Last Reviewed"), interval, "days")
)
```
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU KHÔNG GIAN SỐ (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: CSDL thể hiện đúng tiến độ 100% các bài lab của WebScale Full-Stack.
- [ ] **DoD-2**: Các công thức Spaced Repetition Formula 2.0 hoạt động chính xác không lỗi cú pháp.
- [ ] **DoD-3**: Giao diện trực quan, có view Kanban theo trạng thái bài tập.
- [ ] **DoD-4**: Tương thích hoàn toàn với schema liên kết của Central Notion LMS Hub.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK ĐỒNG BỘ DỮ LIỆU NOTION (NOTION TROUBLESHOOTING RUNBOOK)

Khi xảy ra lỗi đồng bộ hoặc gãy liên kết CSDL quan hệ:
1. **Cô lập thuộc tính**: Xác định xem lỗi phát sinh từ Formula 2.0 hay do cấu hình database relation.
2. **Khôi phục cấu trúc**: Tra cứu cấu trúc chuẩn trong `00_Central_Notion_LMS_Hub/NOTION_ADVANCED_FORMULAS.md`.
3. **Sửa đổi cú pháp**: Cập nhật công thức theo đúng đặc tả Notion 2.0.
4. **Kiểm chứng toàn vẹn**: Tạo bản ghi thử nghiệm để kiểm tra tiến độ tính toán tự động.
