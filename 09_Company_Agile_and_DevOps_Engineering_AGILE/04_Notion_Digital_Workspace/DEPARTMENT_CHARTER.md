# 📜 ĐIỀU LỆ PHÒNG SỐ HÓA & SCRUM KANBAN BOARD NOTION (NOTION DIGITAL WORKSPACE DEPT)
## Phòng 04 — Công Ty Quy Trình Phần Mềm & Kỹ Nghệ Agile/DevOps (CORP-09-AGILE)

> **Mã Phòng Ban:** `AGILE-DEPT-04`  
> **Trưởng phòng phụ trách:** Agent `NKA-05` (Notion Architect & Hub Administrator)  
> **Hệ sinh thái liên kết:** Central Notion LMS Hub (`00_Central_Notion_LMS_Hub`)  
> **Tiêu chuẩn công nghệ:** Notion Formula 2.0 / Agile Sprint Board / Velocity Tracking

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Số Hóa là **trung tâm quản trị vận hành Sprint số hóa**:
1. **Quản Trị Hệ Thống Scrum Board & Backlog DB**: Vận hành bảng Kanban động theo dõi Product Backlog, Sprint Backlog và Epics liên kết hai chiều.
2. **Tự Động Tính Toán Tốc Độ Đội Ngũ (Velocity Calculator)**: Nhúng công thức Notion Formula 2.0 để tự động đo lường số Story Points hoàn thành qua từng Sprint.
3. **Lưu Trữ Biên Bản Cải Tiến (Sprint Retrospectives)**: Chuẩn hóa quy trình ghi chép đánh giá cải tiến liên tục (What went well, What didn't go well, Action items).

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (NOTION INVARIANTS)

1. **Chuẩn Mực Trạng Thái Kanban**:
   - Mọi User Story trong Sprint phải có 1 trong 4 trạng thái: `To Do`, `In Progress`, `In Review / Testing`, `Done`.
2. **Quy Chuẩn Bất Biến Về Story Points**:
   - Story Points bắt buộc chọn theo dãy số Fibonacci: 1, 2, 3, 5, 8, 13. Tuyệt đối không dùng số lẻ tùy tiện (như 4, 7).
3. **Công Thức Formula 2.0 Không Lỗi Cú Pháp**:
   - Toàn bộ thanh tiến độ Burndown và chỉ số hoàn thành phải dùng cú pháp Formula 2.0 (`lets()`, `round()`).

---

## 🛠️ 3. TOOLCHAIN & KỸ NĂNG VẬN HÀNH NOTION LMS

1. **Bộ Công Cụ**: Notion API v2022-06-28, GitHub Notion Integration Sync.
2. **Template Builder**: Sprint Board Views (Timeline view, Board view theo Assignee, Table view theo Epic).
3. **Kiểm Duyệt Toàn Vẹn**: Validator script trong `00_Central_Notion_LMS_Hub`.

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
04_Notion_Digital_Workspace/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 NOTION_AGILE_SPRINT_SCHEMA.md         # Đặc tả cấu trúc CSDL Sprint Board
├── 📁 retro_vault/                          # Ngân hàng biên bản Retrospective
│   ├── sprint_retro_mad_sad_glad.md        # Mẫu Retro Mad-Sad-Glad
│   └── sprint_retro_4ls_template.md        # Mẫu Retro 4Ls (Liked, Learned, Lacked, Longed for)
└── 📁 page_templates/                       # Mẫu trang quản trị dự án
    ├── sprint_planning_agenda.md           # Mẫu chương trình họp lập kế hoạch Sprint
    └── definition_of_done_board_card.md    # Thẻ kiểm tra DoD trên Kanban card
```

---

## 💻 5. MẪU THIẾT KẾ SCHEMA CSDL & CÔNG THỨC NOTION 2.0 (GOLD MASTER NOTION)

```markdown
# 📊 CSDL QUẢN LÝ USER STORIES (AGILE SPRINT BOARD)

### Thuộc tính bảng (Properties Schema):
1. `Story Title` (Title): Tên User Story (VD: US-01: Authentication Flow).
2. `Story Points` (Select): 1, 2, 3, 5, 8, 13.
3. `Epic` (Relation): Liên kết tới Database Epics.
4. `Status` (Status): To Do ⚪, In Progress 🔵, In Review 🟡, Done 🟢.
5. `Assignee` (Person): Kỹ sư phụ trách.
6. `PR Link` (URL): Đường dẫn Pull Request tương ứng trên GitHub.

### 🧮 Công thức Formula 2.0: Tự động tính điểm hoàn thành:
```notion
lets(
  isDone, prop("Status") == "Done",
  pts, toNumber(prop("Story Points")),
  if(isDone, pts, 0)
)
```
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU KHÔNG GIAN SỐ (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: CSDL Sprint Board kết nối thông suốt với Central Notion LMS Hub.
- [ ] **DoD-2**: Formula 2.0 tính toán tổng số Story Points và Velocity chính xác 100%.
- [ ] **DoD-3**: Hỗ trợ bộ lọc xem nhanh các Task đang bị kẹt (Blocked).
- [ ] **DoD-4**: Có đầy đủ template biên bản Sprint Review và Retrospective.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK ĐỒNG BỘ DỮ LIỆU NOTION (NOTION TROUBLESHOOTING RUNBOOK)

Khi xảy ra lỗi đồng bộ bảng Kanban hoặc công thức Formula 2.0 bị gãy:
1. **Xác định lỗi**: Kiểm tra xem lỗi do phân quyền GitHub Webhook hay do cú pháp Notion Formula.
2. **Khôi phục cấu trúc**: Tra cứu đặc tả chuẩn trong `00_Central_Notion_LMS_Hub/NOTION_INTEGRATION_MASTER_SPEC.md`.
3. **Cập nhật công thức**: Sửa lại cú pháp hàm trong bảng thuộc tính.
4. **Kiểm tra hiển thị**: Tạo thử 1 User Story mẫu với 5 Story Points để kiểm tra tính toán tổng tự động.
