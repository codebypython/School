# 📑 BẢN THIẾT KẾ KIẾN TRÚC NOTION TOÀN DIỆN KỲ 7
## Notion 2.0 Relational LMS & Knowledge Architecture Specification

> **Đơn vị thiết kế:** Agent `NKA-05` (Notion Knowledge Architect)  
> **Áp dụng cho:** Toàn bộ 6 môn học Semester 7 (`CV`, `ML`, `NMA`, `Security`, `Japanese`, `PBL6`)  
> **Kế thừa từ:** [NOTION_ADVANCED_FORMULAS.md](file:///d:/User/7th/School/00_Central_Notion_LMS_Hub/NOTION_ADVANCED_FORMULAS.md) & [NOTION_SYSTEM_GUIDE.md](file:///d:/User/7th/School/00_Central_Notion_LMS_Hub/NOTION_SYSTEM_GUIDE.md)

---

## 🧭 I. TỔNG QUAN KIẾN TRÚC: SINGLE SOURCE OF TRUTH

Mô hình quản trị tri thức kỳ 7 được thiết kế theo nguyên lý **"Điều Hành Tập Trung, Thực Thi Chuyên Sâu"**:

```
                              ┌──────────────────────────────────┐
                              │    00_SEMESTER_COMMAND_CENTER    │
                              │  - Master Weekly Tasks Planner   │
                              │  - Urgency Radar (Đếm ngược hạn) │
                              │  - GPA Auto-Grader (Chuẩn DUT)   │
                              │  - External Resource Vault Radar │
                              └─────────────────┬────────────────┘
                                                │ Relation & Rollups
      ┌──────────────┬──────────────┬───────────┴───┬──────────────┬──────────────┐
      ▼              ▼              ▼               ▼              ▼              ▼
┌───────────┐  ┌───────────┐  ┌───────────┐   ┌───────────┐  ┌───────────┐  ┌───────────┐
│ 👁️ CV     │  │ 🧠 ML     │  │ 📡 NMA    │   │ 🔐 SEC    │  │ 🇯🇵 JPN    │  │ 🤖 PBL6   │
│ - Papers  │  │ - Delta   │  │ - Error   │   │ - PCAP Log│  │ - Kanji   │  │ - Sprint  │
│ - Code    │  │ - Scratch │  │ - Topo/IP │   │ - Auth CLI│  │ - 10h KPI │  │ - Exp Log │
└───────────┘  └───────────┘  └───────────┘   └───────────┘  └───────────┘  └───────────┘
```

---

## 🏛️ II. CƠ SỞ DỮ LIỆU MỚI: EXTERNAL RESOURCE VAULT & QUALITY RADAR

Đây là CSDL lưu trữ toàn bộ các nguồn tri thức kinh điển đã qua kiểm định của Agent `EKC-03`.

### 1. Thuộc tính Database (Properties Schema)
- `Tên Tài Liệu` (Title): Tên sách, bài báo hoặc khóa học.
- `Môn Học` (Select): `CV`, `ML`, `NMA`, `Security`, `Japanese`, `PBL6`.
- `Loại Hình` (Select): `Sách Giáo Trình`, `Bài Giảng ĐH`, `Tiêu Chuẩn RFC/NIST`, `Bài Báo Khoa Học`.
- `Tác Giả / Xuất Bản` (Text): Stanford, MIT, Cisco Press, Vũ Hữu Tiệp, Stallings...
- `Điểm ER-QVR` (Number): Thang điểm 0 - 100 theo [ER-QVR Rubric](file:///d:/User/7th/School/.agents/rules/external_resource_rubric.md).
- `Xếp Hạng Chất Lượng` (Formula 2.0): Hiển thị Badge tự động đổi màu sắc.
- `Giá Trị Chắt Lọc` (Text): Các chương quan trọng cần đọc.
- `Link Tài Liệu` (URL): Đường dẫn trực tiếp hoặc file liên kết.

### 2. Mã Formula 2.0 Cột `Xếp Hạng Chất Lượng`
```javascript
let(
  score, prop("Điểm ER-QVR"),
  ifs(
    empty(score), "⚪ Chưa thẩm định",
    score >= 90, style("🏆 HẠNG A+ (KINH ĐIỂN: " + format(score) + "/100)", "green", "green_background", "b"),
    score >= 80, style("⭐ HẠNG A (XUẤT SẮC: " + format(score) + "/100)", "blue", "b"),
    score >= 70, style("📚 HẠNG B (BỔ TRỢ: " + format(score) + "/100)", "yellow"),
    style("⚠️ DƯỚI CHUẨN (" + format(score) + "/100)", "red", "red_background", "b")
  )
)
```

---

## ⚙️ III. BẢN ĐỒ FORMULA 2.0 CHO TỪNG KHÔNG GIAN HỌC TẬP

| Không Gian | Database Đích | Tên Cột Formula | Đoạn Code Cần Dán | Ý Nghĩa Vận Hành |
| :--- | :--- | :--- | :--- | :--- |
| **Command Center** | `DEADLINE & EXAM TRACKER` | `Tình Trạng` | *(Xem Mục 1.1 trong NOTION_ADVANCED_FORMULAS.md)* | Đếm ngược ngày tới hạn; Đỏ rực nếu trễ, Cam nếu hôm nay, Vàng nếu $\le 3$ ngày. |
| **Command Center** | `GPA ESTIMATOR` | `Điểm Chữ` | *(Xem Mục 1.2 trong NOTION_ADVANCED_FORMULAS.md)* | Tự tính điểm tín chỉ ĐHBK Đà Nẵng (40% QT + 60% CK) $\rightarrow$ A, B+, C... |
| **NMA / Security** | `FLASHCARD ACTIVE RECALL` | `Ngày Ôn Tiếp` | *(Xem Mục 2.1 trong NOTION_ADVANCED_FORMULAS.md)* | Thuật toán SuperMemo: Tự nhân chu kỳ theo mức độ tự tin (Chưa thuộc / Tạm / Rất thuộc). |
| **NMA / Security** | `LAB ERROR JOURNAL` | `Attention` | *(Xem Mục 2.2 trong NOTION_ADVANCED_FORMULAS.md)* | Highlight đỏ rực thẻ bài lab nguy hiểm trong Gallery View. |
| **Học Máy (ML)** | `FROM-SCRATCH COMPARISON`| `Tốc Độ (Delta)`| *(Xem Mục 3.1 trong NOTION_ADVANCED_FORMULAS.md)* | Đo mức chênh lệch thời gian chạy (ms) giữa code Numpy tự viết và thư viện Sklearn. |
| **PBL6** | `EXPERIMENT LOG` | `AI Score` | *(Xem Mục 4.1 trong NOTION_ADVANCED_FORMULAS.md)* | Vẽ thanh Progress Bar màu tính điểm RAG (30% Recall + 50% Faithfulness + 20% BERTScore). |
| **PBL6** | `SPRINT BOARD` | `Bottleneck Check` | *(Xem Mục 4.2 trong NOTION_ADVANCED_FORMULAS.md)* | Phát hiện task bị kẹt ở In Progress quá hạn để giải cứu ngay. |
| **Tiếng Nhật N3** | `KANJI MASTER` | `Mastery Badge` | *(Xem Mục 5.1 trong NOTION_ADVANCED_FORMULAS.md)* | Tự động thăng cấp: `🌱 MỚI HỌC` $\rightarrow$ `🔥 ĐANG CÀY` $\rightarrow$ `🏆 MASTERED`. |
| **Tiếng Nhật N3** | `WEEKLY DRILL TRACKER` | `Tổng Giờ` | *(Xem Mục 5.2 trong NOTION_ADVANCED_FORMULAS.md)* | Theo dõi KPI học tập 10 giờ/tuần đổi màu xanh khi hoàn thành. |

---

## 🛠️ IV. QUY TRÌNH 3 BƯỚC NHẬP LIỆU (IMPORT SOP) KHÔNG LỖI

1. **Bước 1: Kéo Thả File Markdown Vào Notion**:
   - Kéo file `.md` môn học tương ứng (VD: `ROADMAP_AND_CURRICULUM.md`) vào Notion Desktop hoặc Web.
   - Notion sẽ tự động chuyển đổi các đề mục `#`, `##` thành Headings và các đoạn code thành Code Blocks chuẩn đẹp.
2. **Bước 2: Chuyển Bảng Thành Cơ Sở Dữ Liệu Động**:
   - Di chuột lên góc phải các bảng tổng hợp $\rightarrow$ Click `···` $\rightarrow$ Chọn **`Turn into database`**.
   - Đổi tên bảng theo đúng chuẩn (VD: `Algorithm Cheatsheet`, `Kanji Master`).
3. **Bước 3: Thiết Lập Cột Formula 2.0**:
   - Click dấu `+` ở góc phải bảng để thêm cột mới $\rightarrow$ Đặt tên cột (VD: `Mastery Badge`) $\rightarrow$ Chọn loại là **`Formula`**.
   - Copy đoạn mã tương ứng từ bảng trên hoặc trong [NOTION_ADVANCED_FORMULAS.md](file:///d:/User/7th/School/00_Central_Notion_LMS_Hub/NOTION_ADVANCED_FORMULAS.md) và dán vào.
   - Chỉnh định dạng hiển thị: Nếu là tiến độ chọn dạng `Bar` hoặc `Ring`.
4. **Bước 4: Thiết Lập Các Góc Nhìn Đỉnh Cao (Smart Views)**:
   - **Board View**: Dùng cho `Sprint Board PBL6` (Group theo `Status: Backlog / In Progress / Review / Done`).
   - **Gallery View**: Dùng cho `Lab Error Journal` (Card Preview chọn `Page Content` để hiện thẳng ảnh chụp lỗi màn hình).
   - **Filtered Table View**: Dùng cho `Flashcard` (Bật bộ lọc `Cần Ôn? = True` để chỉ hiển thị các từ vựng/khái niệm đến hạn phải ôn trong ngày).
