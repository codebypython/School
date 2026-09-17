# 📜 ĐIỀU LỆ PHÒNG SỐ HÓA & KHÔNG GIAN NOTION LMS (NOTION DIGITAL WORKSPACE DEPT)
## Phòng 04 — Công Ty Hệ Thống Phân Tán & Backend Python (CORP-11-PY)

> **Mã Phòng Ban:** `PY-DEPT-04`  
> **Trưởng phòng phụ trách:** Agent `NKA-05` (Notion Architect & Hub Administrator)  
> **Hệ sinh thái liên kết:** Central Notion LMS Hub (`00_Central_Notion_LMS_Hub`)  
> **Tiêu chuẩn công nghệ:** Notion Formula 2.0 / Python Backend Tracker / Active Recall Flashcards

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Số Hóa là **cầu nối không gian quản trị học tập số** cho kỹ sư PyScale Backend:
1. **Quản Lý Tiến Độ Dự Án Microservices (Project Tracker DB)**: Theo dõi tiến độ triển khai các service (Auth, Order, Payment, Worker) và kiểm soát tiêu chí nghiệm thu DoD.
2. **Kho Bảng Tra Cứu Số Hóa (Cheat Sheets Vault)**: Số hóa danh mục Python Data Model Dunder Methods, cú pháp SQLAlchemy 2.0 và lệnh Alembic Migration.
3. **Hệ Thống Flashcards Lặp Lại Ngắt Quãng (AsyncIO & GIL Flashcards)**: Sử dụng Notion Formula 2.0 để tự động lên lịch kiểm tra kiến thức về Event Loop và concurrency.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (NOTION INVARIANTS)

1. **Chuẩn Mực Khối Mã Lệnh (Code Block Invariant)**:
   - Toàn bộ khối code Python trong trang Notion phải có cú pháp đúng PEP 8 và có khai báo type annotations.
2. **Quy Chuẩn CSDL Quan Hệ Hai Chiều**:
   - Mọi task Microservices phải liên kết với User Story tương ứng trong Central Notion LMS Hub.
3. **Công Thức Formula 2.0 Không Có Lỗi Runtime**:
   - Mọi công thức tính toán ngày ôn tập hoặc đo lường tiến độ hoàn thành phải dùng cú pháp Formula 2.0 (`lets()`, `ifs()`).

---

## 🛠️ 3. TOOLCHAIN & KỸ NĂNG VẬN HÀNH NOTION LMS

1. **Bộ Công Cụ**: Notion API v2022-06-28, Python Notion-Client SDK.
2. **Kiểm Tra Cú Pháp**: Notion Formula Linter trong Central LMS Hub.
3. **Môi Trường Sandbox**: Workspace Notion riêng biệt cho PyScale Corp.

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
04_Notion_Digital_Workspace/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 NOTION_PYSCALE_TRACKER_SCHEMA.md      # Cấu trúc CSDL theo dõi tiến độ Backend
├── 📁 flashcards_vault/                     # Ngân hàng câu hỏi Active Recall
│   ├── python_data_model_flashcards.md     # Flashcards Dunder Methods
│   └── asyncio_concurrency_flashcards.md   # Flashcards Event Loop & Coroutines
└── 📁 page_templates/                       # Mẫu trang kỹ thuật Notion
    ├── microservice_api_doc_template.md    # Mẫu đặc tả API nội bộ
    └── incident_postmortem_template.md     # Mẫu báo cáo sự cố backend phân tán
```

---

## 💻 5. MẪU THIẾT KẾ SCHEMA CSDL & CÔNG THỨC NOTION 2.0 (GOLD MASTER NOTION)

```markdown
# 📊 CSDL QUẢN LÝ TIẾN ĐỘ MICROSERVICES (PYSCALE SERVICES DB)

### Thuộc tính bảng (Properties Schema):
1. `Service Name` (Title): Tên dịch vụ (Auth Service, Order Service).
2. `Architecture Type` (Select): Async REST API, Background Worker, Event Consumer.
3. `Test Coverage` (Number): Phần trăm kiểm thử đạt được.
4. `Status` (Status): Spec, In Development, Staging, Production.
5. `Last Security Audit` (Date): Ngày quét bảo mật gần nhất.

### 🧮 Công thức Formula 2.0: Readiness Gate Status:
```notion
lets(
  isReady, prop("Test Coverage") >= 85 and prop("Status") == "Staging",
  if(isReady, "🟢 READY FOR DEPLOY", "🔴 BLOCKED: INSUFFICIENT QUALITY")
)
```
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU KHÔNG GIAN SỐ (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: CSDL thể hiện đúng tiến độ 100% các bài lab của PyScale Backend.
- [ ] **DoD-2**: Các công thức Spaced Repetition Formula 2.0 hoạt động chính xác không lỗi cú pháp.
- [ ] **DoD-3**: Giao diện trực quan, có view Kanban theo trạng thái các microservices.
- [ ] **DoD-4**: Tương thích hoàn toàn với schema liên kết của Central Notion LMS Hub.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK ĐỒNG BỘ DỮ LIỆU NOTION (NOTION TROUBLESHOOTING RUNBOOK)

Khi xảy ra lỗi đồng bộ hoặc gãy liên kết CSDL quan hệ:
1. **Cô lập thuộc tính**: Kiểm tra lỗi xảy ra ở tầng Formula hay tầng Relation.
2. **Khôi phục cấu trúc**: Tra cứu cấu trúc chuẩn trong `00_Central_Notion_LMS_Hub/NOTION_ADVANCED_FORMULAS.md`.
3. **Sửa đổi cú pháp**: Cập nhật công thức theo đúng đặc tả Notion 2.0.
4. **Kiểm chứng toàn vẹn**: Tạo bản ghi thử nghiệm để kiểm tra tiến độ tính toán tự động.
