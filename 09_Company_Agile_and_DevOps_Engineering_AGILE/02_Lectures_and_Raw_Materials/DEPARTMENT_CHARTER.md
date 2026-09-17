# 📜 ĐIỀU LỆ PHÒNG TƯ LIỆU & USER STORY TEMPLATES (LECTURES & RAW MATERIALS DEPT)
## Phòng 02 — Công Ty Quy Trình Phần Mềm & Kỹ Nghệ Agile/DevOps (CORP-09-AGILE)

> **Mã Phòng Ban:** `AGILE-DEPT-02`  
> **Trưởng phòng phụ trách:** Agent `EKC-03` (Knowledge Curator & Quality Sentinel)  
> **Tiêu chuẩn học liệu:** ER-QVR $\ge 90/100$ | The 2020 Scrum Guide / Pro Git / DORA Research

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Tư Liệu là **thư viện chuẩn mực quy trình Agile và văn hóa kỹ nghệ DevOps**:
1. **Lưu Trữ Văn Bản Định Chuẩn Quốc Tế**: Lưu trữ nguyên văn và bản dịch chuẩn The 2020 Scrum Guide, Tuyên ngôn Agile 2001, các báo cáo khoa học State of DevOps và bộ chỉ số DORA Metrics.
2. **Kho Biểu Mẫu Quy Trình Sản Xuất (Templates Vault)**: Chuẩn hóa mẫu User Story theo tiêu chuẩn INVEST, mẫu Definition of Done (DoD), mẫu Pull Request Template và Issue Templates cho GitHub/GitLab.
3. **Giải Phẫu Cấu Trúc Dữ Liệu Git (Git Internals Vault)**: Lưu trữ các phân tích kỹ thuật về Git Object Database (Blobs, Trees, Commits, Annotated Tags, Packfiles).

---

## ⚖️ 2. BỘ QUY TẮC BẢO TỒN TƯ LIỆU BẤT BIẾN (CURATION INVARIANTS)

1. **Chuẩn Mực Nguồn Cung Cấp (Canonical Source Invariant)**:
   - Mọi tư liệu về Scrum bắt buộc phải lấy từ Scrum.org hoặc Scrum Alliance. Tuyệt đối không lưu các biến thể tùy tiện làm sai lệch bản chất tự quản (Self-managing) của Scrum Team.
2. **Quy Tắc Tiêu Chuẩn INVEST Cho Mọi User Story Mẫu**:
   - Mọi User Story lưu trữ làm mẫu bắt buộc phải thỏa mãn 6 tiêu chí: Independent, Negotiable, Valuable, Estimable, Small, Testable.
3. **Quy Tắc Rõ Ràng Của Acceptance Criteria**:
   - Mọi kịch bản chấp nhận (Acceptance Criteria) phải được viết theo định dạng Gherkin chuẩn: `Given ... When ... Then ...`.

---

## 🛠️ 3. TOOLCHAIN & QUY TRÌNH SỐ HÓA BÀI GIẢNG

1. **Vẽ Sơ Đồ Quy Trình**: Mermaid.js GitGraph, PlantUML State Machine.
2. **Quản Lý Biểu Mẫu Markdown**: GitHub Flavored Markdown (GFM) Task Lists.
3. **Kiểm Duyệt Liên Kết**: Script `holding_system_auditor.py`.

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
02_Lectures_and_Raw_Materials/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 agile_standards/                      # Các tài liệu chuẩn mực thế giới
│   ├── scrum_guide_2020_annotated.md       # Scrum Guide 2020 có chú giải thực chiến
│   └── agile_manifesto_12_principles.md    # 12 nguyên lý phía sau Tuyên ngôn Agile
├── 📁 process_templates/                    # Biểu mẫu quản trị quy trình
│   ├── user_story_invest_template.md       # Mẫu User Story chuẩn Gherkin
│   ├── definition_of_done_checklist.md     # Bảng kiểm tra DoD đa tầng
│   └── pull_request_template.md            # Mẫu mô tả PR có checklist tự kiểm tra
└── 📁 git_internals/                        # Chuyên đề giải phẫu Git
    └── git_dag_and_object_storage.md       # Cơ chế lưu trữ phân tán của Git
```

---

## 💻 5. MẪU TƯ LIỆU BIỂU MẪU QUY TRÌNH CHUẨN (GOLD MASTER USER STORY)

```markdown
# 📋 USER STORY: XÁC THỰC HAI LỚP CHO TÀI KHOẢN QUẢN TRỊ VIÊN (2FA AUTH)
> **Mã số:** `US-SEC-042` | **Story Points:** 5 | **Ưu tiên:** High  
> **Người thẩm định:** Agent `EKC-03` | **Tiêu chuẩn:** INVEST Compliant

### 1. Mô tả Người dùng (User Narrative)
Là một **Quản trị viên hệ thống (System Admin)**,  
Tôi muốn **kích hoạt xác thực 2 lớp (2FA) qua ứng dụng Authenticator (TOTP)**,  
Để **ngăn chặn rủi ro tài khoản bị chiếm đoạt khi lộ mật khẩu**.

### 2. Tiêu chí Chấp nhận (Acceptance Criteria - Gherkin)
- **Kịch bản 1: Quét mã QR thành công**
  - *Given*: Quản trị viên đã đăng nhập và mở trang Cài đặt Bảo mật.
  - *When*: Bấm nút "Kích hoạt 2FA" và nhập đúng mã 6 chữ số từ Google Authenticator.
  - *Then*: Hệ thống kích hoạt 2FA và cung cấp 8 mã dự phòng (Backup Codes).

- **Kịch bản 2: Nhập sai mã OTP**
  - *Given*: Quản trị viên đang ở màn hình xác thực 2FA.
  - *When*: Nhập mã 6 chữ số đã hết hạn hoặc không khớp.
  - *Then*: Hệ thống từ chối đăng nhập và hiển thị thông báo lỗi "Mã xác thực không hợp lệ".
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU TƯ LIỆU (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: Toàn bộ biểu mẫu có thể sao chép và áp dụng ngay vào dự án thực tế.
- [ ] **DoD-2**: User Story mẫu có đầy đủ kịch bản kiểm thử Acceptance Criteria dạng Gherkin.
- [ ] **DoD-3**: Sơ đồ nhánh Git hiển thị trực quan không bị lỗi cú pháp Mermaid GitGraph.
- [ ] **DoD-4**: Đạt điểm đánh giá ER-QVR tối thiểu 90/100.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK KHẮC PHỤC SAI LỆCH QUY TRÌNH (CURATION TROUBLESHOOTING RUNBOOK)

Khi phát hiện biểu mẫu hoặc tư liệu hướng dẫn vi phạm nguyên lý Agile:
1. **Phát hiện**: Phát hiện mẫu User Story quá lớn (Epic) nhưng bị gán làm 1 Story đơn lẻ trong Sprint.
2. **Khóa biểu mẫu**: Đánh dấu nhãn `⚠️ SPLITTING REQUIRED`.
3. **Phân rã User Story**: Áp dụng kỹ thuật phân tách của Mike Cohn (theo Workflow, theo Data type, theo Spike).
4. **Cập nhật kho mẫu**: Đưa ví dụ phân tách vào thư viện mẫu để sinh viên tham khảo.
