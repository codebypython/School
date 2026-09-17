# 📜 ĐIỀU LỆ PHÒNG SỐ HÓA & KHÔNG GIAN NOTION LMS (NOTION DIGITAL WORKSPACE DEPT)
## Phòng 04 — Công Ty Thiết Kế Phần Mềm & Kiến Trúc Hướng Đối Tượng (CORP-08-CRAFT)

> **Mã Phòng Ban:** `CRAFT-DEPT-04`  
> **Trưởng phòng phụ trách:** Agent `NKA-05` (Notion Architect & Hub Administrator)  
> **Hệ sinh thái liên kết:** Central Notion LMS Hub (`00_Central_Notion_LMS_Hub`)  
> **Tiêu chuẩn công nghệ:** Notion Formula 2.0 / Relational Architecture DB / Active Recall Flashcards

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Số Hóa là **trung tâm quản trị học tập số** về kiến trúc phần mềm và kỹ nghệ phần mềm:
1. **Thiết Kế CSDL Quản Trị Mẫu Thiết Kế (Design Patterns Catalog DB)**: Hệ thống hóa 23 GoF patterns, phân loại theo nhóm (Creational, Structural, Behavioral) kèm độ phức tạp và mức độ phổ biến.
2. **Cơ Sở Dữ Liệu 24 Code Smells & Biện Pháp Refactoring**: Lưu trữ danh mục mùi mã nguồn, dấu hiệu nhận diện và phương pháp tái cấu trúc tương ứng.
3. **Bộ Flashcards Spaced Repetition Ôn Tập SOLID**: Ứng dụng Formula 2.0 để tự động lên lịch nhắc bài ôn tập nguyên lý kiến trúc cho sinh viên.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (NOTION INVARIANTS)

1. **Chuẩn Mực Khối Callout Phân Loại**:
   - Sử dụng màu sắc và icon chuẩn cho từng nhóm pattern:
     ```markdown
     > 🟢 **Creational Pattern**: Tập trung vào cơ chế khởi tạo đối tượng...
     > 🔵 **Structural Pattern**: Tập trung vào cách lắp ghép các lớp và đối tượng...
     > 🟣 **Behavioral Pattern**: Tập trung vào phân công trách nhiệm và giao tiếp...
     ```
2. **Quy Chuẩn Liên Kết CSDL Hai Chiều (Bidirectional Relations)**:
   - Mọi bản ghi Pattern bắt buộc liên kết với bản ghi Code Smell mà nó giải quyết.
3. **Cú Pháp Notion Formula 2.0 Chuẩn Xác**:
   - Mọi công thức tính độ thông thạo (Mastery Score) phải dùng cú pháp hàm mới (`lets()`, `map()`).

---

## 🛠️ 3. TOOLCHAIN & KỸ NĂNG VẬN HÀNH NOTION LMS

1. **Bộ Công Cụ**: Notion API v2022-06-28, Notion Markdown Exporter/Importer.
2. **Template Builder**: Hệ thống Database Views (Board view theo Nhóm, Table view theo Mức độ khó).
3. **Kiểm Tra Tính Toàn Vẹn**: Validator script trong `00_Central_Notion_LMS_Hub`.

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
04_Notion_Digital_Workspace/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 NOTION_CRAFT_CATALOG_SCHEMA.md        # Đặc tả cấu trúc Database Design Patterns
├── 📁 flashcards_vault/                     # Ngân hàng câu hỏi Active Recall
│   ├── solid_principles_flashcards.md      # Flashcards 5 nguyên lý SOLID
│   └── gof_patterns_flashcards.md          # Flashcards 23 GoF Patterns
└── 📁 page_templates/                       # Mẫu trang ghi chép thiết kế
    ├── architectural_decision_record.md     # Mẫu ADR (Architectural Decision Record)
    └── refactoring_session_log.md           # Mẫu ghi nhận buổi tái cấu trúc mã nguồn
```

---

## 💻 5. MẪU THIẾT KẾ SCHEMA CSDL & CÔNG THỨC NOTION 2.0 (GOLD MASTER NOTION)

```markdown
# 📊 CSDL QUẢN LÝ MẪU THIẾT KẾ (DESIGN PATTERNS REPOSITORY)

### Thuộc tính bảng (Properties Schema):
1. `Pattern Name` (Title): Tên mẫu (VD: Observer, Factory Method, Strategy).
2. `Category` (Select): Creational 🟢, Structural 🔵, Behavioral 🟣.
3. `Complexity` (Select): Low (1/3), Medium (2/3), High (3/3).
4. `Code Smells Solved` (Relation): Liên kết tới Database Code Smells.
5. `Confidence Level` (Number 1-5): Đánh giá mức độ thông thạo.
6. `Last Reviewed` (Date): Ngày ôn tập gần nhất.

### 🧮 Công thức Formula 2.0: Spaced Repetition Scheduling:
```notion
lets(
  interval, if(prop("Confidence Level") >= 4, 14, if(prop("Confidence Level") == 3, 5, 1)),
  dateAdd(prop("Last Reviewed"), interval, "days")
)
```
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU KHÔNG GIAN SỐ (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: CSDL thể hiện đầy đủ 23 GoF Patterns với quan hệ đa chiều chính xác.
- [ ] **DoD-2**: Formula 2.0 tính toán ngày ôn tập không có lỗi runtime.
- [ ] **DoD-3**: Hỗ trợ view Kanban phân loại theo tình trạng nắm vững kiến thức.
- [ ] **DoD-4**: Tương thích hoàn toàn với chuẩn đồng bộ của Central Notion LMS Hub.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK ĐỒNG BỘ DỮ LIỆU NOTION (NOTION TROUBLESHOOTING RUNBOOK)

Khi xảy ra lỗi đồng bộ hoặc gãy liên kết CSDL quan hệ:
1. **Cô lập thuộc tính lỗi**: Kiểm tra xem lỗi do Formula syntax hay do relation bị đứt gãy.
2. **Khôi phục cấu trúc**: Đối chiếu với `00_Central_Notion_LMS_Hub/NOTION_INTEGRATION_MASTER_SPEC.md`.
3. **Kiểm tra công thức**: Thay thế các hàm deprecated bằng cú pháp Formula 2.0 chuẩn.
4. **Kiểm thử nghiệm thu**: Tạo thử 1 bản ghi mẫu để xác thực các Rollups hiển thị chính xác.
