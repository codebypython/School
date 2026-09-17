# 📜 ĐIỀU LỆ PHÒNG CHIẾN LƯỢC & LỘ TRÌNH ĐÀO TẠO (STRATEGY & CURRICULUM DEPT)
## Phòng 01 — Công Ty Quy Trình Phần Mềm & Kỹ Nghệ Agile/DevOps (CORP-09-AGILE)

> **Mã Phòng Ban:** `AGILE-DEPT-01`  
> **Trưởng phòng phụ trách:** Agent `PSD-04` (Pedagogical Scaffolding Designer) & `ACD-01` (Academic Curriculum Director)  
> **Tiêu chuẩn học thuật:** The 2020 Scrum Guide (Scrum.org) / Pro Git (Chacon) / Accelerate (DORA Metrics)

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Chiến Lược & Lộ Trình là **bộ não định hình văn hóa làm việc nhóm và kỹ nghệ sản xuất phần mềm**:
1. **Thiết Kế Khung Chương Trình 15 Tuần Chuẩn**: Dẫn dắt học viên từ Agile Manifesto & Khung Scrum 2020 $\rightarrow$ Làm chủ Git Internals & Phân nhánh $\rightarrow$ Văn hóa Code Review & XP $\rightarrow$ Automated Quality Gates & CI/CD $\rightarrow$ Vận hành Sprint thực chiến.
2. **Loại Bỏ Bệnh "Zombie Scrum"**: Đào tạo đúng bản chất tinh gọn của Scrum 2020 (3 Vai trò, 5 Sự kiện, 3 Hiện vật), tập trung vào giá trị phần mềm chạy được thay vì thủ tục giấy tờ hình thức.
3. **Chuẩn Hóa Kỹ Năng DevOps Đầu Ra**: Đảm bảo 100% học viên tốt nghiệp biết viết file cấu hình CI/CD GitHub Actions, tự động chạy linter, format và test coverage.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (PEDAGOGICAL INVARIANTS)

1. **Tuân Thủ Mô Hình 4 Tầng Sư Phạm**:
   - Mọi tuần học bắt buộc phải có: *Tầng 1 (Nguyên lý Agile kinh điển)* $\rightarrow$ *Tầng 2 (Công cụ hiện đại Git/GitHub Actions)* $\rightarrow$ *Tầng 3 (⚠️ Cảnh báo Zombie Scrum & Git traps)* $\rightarrow$ *Tầng 4 (Thực hành Sprint & DoD)*.
2. **Quy Tắc Mô Phỏng Thực Tế (Real-World Simulation Rule)**:
   - Nghiêm cấm dạy lý thuyết Scrum suông trên slide. Mọi khái niệm (Sprint Backlog, Story Points, DoD) bắt buộc phải gắn liền với một bảng Kanban thực tế trên GitHub Projects / Linear.
3. **Quy Tắc Lấy Mã Nguồn Làm Trung Tâm**:
   - Các bài tập về User Story và Acceptance Criteria phải chuyển hóa trực tiếp thành các Automated Tests trong pipeline CI.

---

## 🛠️ 3. TOOLCHAIN & SKILLS ROUTE ĐÀO TẠO AGILE/DEVOPS

| Hạng Mục | Bộ Công Cụ & Thước Đo | Mục Đích Sư Phạm |
| :--- | :--- | :--- |
| **Quản trị Mã nguồn** | Git CLI, GitHub CLI (`gh`), GPG Signing | Phân nhánh GitFlow vs Trunk-based, Rebase sạch |
| **Quản trị Dự án Agile** | GitHub Projects, Linear, Notion Sprint Board | Vận hành Sprint, Backlog Grooming, Burndown Chart |
| **Tự động hóa CI/CD** | GitHub Actions, Act (Local runner), Docker | Xây dựng Pipeline kiểm thử tự động trên Pull Request |
| **Đo lường Hiệu suất** | DORA Metrics (Lead Time, MTTR, CFR) | Đánh giá năng lực chuyển giao phần mềm liên tục |

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
01_Strategy_and_Curriculum/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 AGENT_PROFILE.md                      # Hồ sơ năng lực Mentor AI Agile/DevOps
├── 📄 ROADMAP_AND_CURRICULUM.md             # Giáo trình Master 15 tuần Agile & CI/CD
├── 📁 rubrics/                              # Thang điểm đánh giá Sprint & Teamwork
│   └── sprint_delivery_rubric.md           # Tiêu chí đánh giá chất lượng bàn giao Sprint
└── 📁 exam_blueprints/                      # Đề cương kiểm tra năng lực
    ├── scrum_master_blueprint.md           # Đề thi đánh giá lý thuyết Scrum & Agile
    └── git_devops_practical_exam.md        # Đề thi thực hành giải quyết xung đột Git
```

---

## 💻 5. MẪU THIẾT KẾ BÀI HỌC 4 TẦNG QUY CHUẨN (GOLD MASTER SYLLABUS UNIT)

```markdown
### Tuần X: [Tên Chủ Đề Agile / DevOps]
- **Tầng 1 (Nguyên lý Agile & Bản chất Git - Nguồn: Scrum Guide / Pro Git)**:
  - Bản chất nguyên lý: Phản hồi nhanh với thay đổi hơn là bám sát kế hoạch cứng nhắc.
  - Cấu trúc dữ liệu bên trong Git: Directed Acyclic Graph (DAG), Commit Trees, Reflog.
- **Tầng 2 (Thực hành Công cụ & Kỹ thuật Hiện đại)**:
  - Lệnh CLI thao tác chuẩn, cấu hình GitHub Actions workflow.
- **Tầng 3 (⚠️ Cảnh báo bẫy sai lầm & Anti-patterns)**:
  - Bẫy Zombie Scrum: Daily Standup biến thành buổi báo cáo công việc cho sếp.
  - Bẫy Git: Dùng `git push --force` đè nhánh chung thay vì dùng `--force-with-lease`.
- **Tầng 4 (Bài tập Lab & Tiêu chí DoD)**:
  - Đề bài: Mô phỏng quy trình Sprint 2 tuần, tạo Pull Request và tự động kích hoạt CI pipeline.
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU GIÁO TRÌNH (DEFINITION OF READY - DoR)

- [ ] **DoR-1**: Giáo trình bám sát The 2020 Scrum Guide chính thức từ Ken Schwaber & Jeff Sutherland.
- [ ] **DoR-2**: Các bài tập Git có kịch bản tạo xung đột và video/ảnh minh chứng giải quyết xung đột bằng lệnh.
- [ ] **DoR-3**: Đã có repo template tích hợp sẵn GitHub Actions workflow để học viên fork thực hành.
- [ ] **DoR-4**: Không cổ xúy các nghi thức quan liêu hoặc Waterfall cải trang thành Agile.
- [ ] **DoR-5**: Có câu hỏi gợi mở Micro-quiz về sự khác biệt giữa Definition of Done và Acceptance Criteria.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK GIÁM ĐỊNH LỘ TRÌNH (CURRICULUM TROUBLESHOOTING RUNBOOK)

Khi phát hiện bài giảng có biểu hiện sai lệch về tinh thần Agile hoặc hỏng hóc kịch bản Lab:
1. **Phát hiện (Detection)**: Sinh viên hoặc Agent Audit phát hiện bài lab hướng dẫn bẻ nhánh sai quy chuẩn GitFlow.
2. **Đình chỉ module (Quarantine)**: Gắn nhãn `⚠️ WORKFLOW INCONSISTENCY` tại `STATUS.md`.
3. **Hiệu chỉnh bài lab**: Cập nhật kịch bản lệnh CLI và quy trình Pull Request chuẩn.
4. **Kiểm tra thực nghiệm**: Chạy thử kịch bản lab từ đầu đến cuối trên một repository trống.
