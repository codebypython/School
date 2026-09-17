# 🖱️ CẨM NANG HƯỚNG DẪN THAO TÁC NOTION THỰC CHIẾN CHI TIẾT ĐẾN TỪNG CLICK
## Standard Operating Procedure (SOP) — Notion 2.0 LMS Manual Execution Guide

> **Dành riêng cho:** Kỹ Sư Trưởng Handmade (`HM-00` / Bạn) — Người trực tiếp xây dựng và làm chủ hệ thống Notion  
> **Đơn vị ban hành:** Trung Tâm Công Nghệ Số Notion (`00_Central_Notion_LMS_Hub`)  
> **Mục tiêu:** Cung cấp hướng dẫn thao tác tỉ mỉ từ cú pháp gõ phím, vị trí click chuột, cách tạo bảng, liên kết quan hệ (Relation/Rollup), cấu hình công thức Formula 2.0 đến thiết lập giao diện Dashboard đỉnh cao.

---

## 🧭 MỤC LỤC HƯỚNG DẪN
1. [Bản Thiết Kế Bố Cục Trang Chủ (Dashboard Layout & Visual Architecture)](#-chương-1-giải-phẫu-bố-cục-trang-chủ-dashboard-layout)
2. [Hướng Dẫn Tạo Cơ Sở Dữ Liệu & Thuộc Tính Từng Bước (Database & Property Setup)](#-chương-2-hướng-dẫn-tạo-cơ-sở-dữ-liệu--thuộc-tính-chuẩn)
3. [Cẩm Nang Cài Đặt Công Thức Formula 2.0 Không Bao Giờ Lỗi](#-chương-3-cẩm-nang-cài-đặt-formula-20-không-bao-giờ-lỗi)
4. [Kỹ Thuật Thiết Lập Liên Kết Hai Chiều: Relations & Rollups Masterclass](#-chương-4-kỹ-thuật-liên-kết-hai-chiều-relations--rollups)
5. [Nghệ Thuật Cấu Hình 4 Góc Nhìn Thông Minh (Smart Views, Filters, Sorts & Grouping)](#-chương-5-nghệ-thuật-cấu-hình-các-góc-nhìn-thông-minh)
6. [Quy Trình Xây Dựng 6 Không Gian Môn Học Chuyên Biệt](#-chương-6-quy-trình-xây-dựng-không-gian-cho-từng-công-ty-môn-học)
7. [Cẩm Nang Xử Lý Lỗi Thường Gặp (Troubleshooting Guide)](#-chương-7-cẩm-nang-xử-lý-sự-cố-notion-thường-gặp)

---

## 🏛️ CHƯƠNG 1: GIẢI PHẪU BỐ CỤC TRANG CHỦ (DASHBOARD LAYOUT)

Trang chủ điều hành `00_SEMESTER_COMMAND_CENTER` được thiết kế theo tỷ lệ vàng:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [Banner Cover: Minimal Dark Tech / Bách Khoa Đà Nẵng]                                  │
│ Icon: 🎓 | Title: SEMESTER 7 COMMAND CENTER — DUT ACADEMIC HUB                         │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 💡 Callout Block: "Chào buổi sáng Kỹ sư! Kiểm tra Radar Deadline & ôn 15p Flashcards."  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [Quick Navigation Synced Block]: [CV Corp] | [ML Corp] | [NMA Corp] | [SEC] | [JPN]... │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│ 👈 CỘT TRÁI (Tỷ lệ 60% — Điều Hành & Tiến Độ)│ 👉 CỘT PHẢI (Tỷ lệ 40% — Cảnh Báo & Lối Tắt)│
│                                           │                                            │
│ 1. Master Weekly Planner (Board View)     │ 1. Urgency Radar (Deadline đếm ngược)      │
│    - Kéo thả task: To-do ➔ Doing ➔ Done   │    - Đỏ rực nếu trễ hạn, Vàng nếu <= 3 ngày│
│ 2. Spaced Repetition Daily Queue          │ 2. GPA Estimator (Dự phóng điểm chữ A/B+)  │
│    - Lọc các thẻ Flashcard đến hạn hôm nay│ 3. Quick Links & External Resource Vault   │
│ 3. Weekly Reflection & Study Hours Ring   │ 4. Error Journal Radar (Ảnh lỗi cần fix)   │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

### Thao Tác Tạo Bố Cục Từng Bước:
1. **Tạo Trang Mới**: Trong Notion, bấm `+ Add a page` ở thanh bên trái (Sidebar).
2. **Đặt Icon & Cover**:
   - Rê chuột lên tiêu đề $\rightarrow$ Bấm `Add icon` $\rightarrow$ Chọn biểu tượng `🎓`.
   - Bấm `Add cover` $\rightarrow$ Chọn `Change cover` $\rightarrow$ Tab `Unsplash` $\rightarrow$ Gõ từ khóa `minimal technology` hoặc `server room`.
3. **Mở Rộng Toàn Màn Hình (Full Width)**:
   - Nhìn lên góc trên cùng bên phải màn hình Notion $\rightarrow$ Bấm vào dấu `···` (Options).
   - Bật công tắc **`Full width`** (Thanh màu xanh). Chữ và bảng sẽ tràn đều ra hai bên, giao diện rộng rãi và chuyên nghiệp.
4. **Tạo Callout Chào Buổi Sáng**:
   - Gõ phím `/callout` $\rightarrow$ Bấm `Enter`.
   - Đổi icon thành `💡`. Nhập dòng chữ: `⚡ Kỷ luật là cây cầu nối giữa mục tiêu và thành tựu. Hôm nay bạn làm chủ kiến thức!`.
   - Đổi màu nền: Bấm vào dấu `⋮⋮` cạnh khối Callout $\rightarrow$ `Color` $\rightarrow$ Chọn `Blue background`.
5. **Chia 2 Cột (Two Columns Layout)**:
   - Gõ `/2col` $\rightarrow$ Notion lập tức chia trang thành 2 cột song song.
   - Kéo thanh ranh giới ở giữa sao cho cột trái chiếm khoảng 60% và cột phải chiếm khoảng 40%.

---

## 📊 CHƯƠNG 2: HƯỚNG DẪN TẠO CƠ SỞ DỮ LIỆU & THUỘC TÍNH CHUẨN

### 1. Tạo Database Inline (Bảng Nằm Trong Trang)
- **Thao tác**: Nhấp chuột vào vị trí muốn đặt bảng $\rightarrow$ Gõ `/database inline` $\rightarrow$ Bấm `Enter`.
- **Đặt tên bảng**: Nhấp vào dòng chữ *Untitled* $\rightarrow$ Đặt tên (Ví dụ: `DEADLINE & EXAM TRACKER`).

### 2. Thiết Lập Danh Sách Cột (Properties Schema)
Dưới đây là bảng thông số chuẩn cho bảng **DEADLINE & EXAM TRACKER**:

| Tên Cột | Loại Dữ Liệu (Property Type) | Thao Tác Cài Đặt Chi Tiết |
| :--- | :---: | :--- |
| **Nhiệm Vụ / Kỳ Thi** | `Title` | Cột mặc định đầu tiên. Nhấp đúp vào tiêu đề để đổi tên. |
| **Môn Học** | `Select` | Click dấu `+` $\rightarrow$ Chọn `Select` $\rightarrow$ Tạo 6 nhãn màu: `CV` (Tím), `ML` (Xanh dương), `NMA` (Cam), `SEC` (Đỏ), `JPN` (Hồng), `PBL6` (Xanh lá). |
| **Ngày Hạn** | `Date` | Click dấu `+` $\rightarrow$ Chọn `Date`. Khi nhập liệu, bấm vào ô để chọn ngày và giờ cụ thể. |
| **Trạng Thái** | `Status` | Click dấu `+` $\rightarrow$ Chọn `Status`. Mặc định có 3 nhóm: `To-do`, `In progress`, `Done`. |
| **Mức Độ Quan Trọng** | `Select` | Click dấu `+` $\rightarrow$ Chọn `Select` $\rightarrow$ Tạo 3 nhãn: `🚨 Tối Khẩn`, `⚠️ Quan Trọng`, `☕ Bình Thường`. |
| **Tình Trạng (Radar)**| `Formula` | Click dấu `+` $\rightarrow$ Chọn `Formula` $\rightarrow$ Dán đoạn mã ở Chương 3. |

---

## ⚡ CHƯƠNG 3: CẨM NANG CÀI ĐẶT FORMULA 2.0 KHÔNG BAO GIỜ LỖI

### 1. Quy Trình 4 Bước Dán Công Thức Formula 2.0
1. **Bước 1**: Nhấp chuột trái vào tiêu đề cột `Tình Trạng` $\rightarrow$ Chọn **`Edit property`**.
2. **Bước 2**: Tại mục `Type`, đảm bảo đã chọn **`Formula`**.
3. **Bước 3**: Nhấp vào khung **`Edit`** (khung chứa công thức) $\rightarrow$ Một hộp thoại soạn thảo code sẽ hiện ra.
4. **Bước 4**: Xóa sạch ký tự cũ, copy chính xác đoạn mã dưới đây và dán (Ctrl+V) vào:

```javascript
let(
  days, 
  dateBetween(prop("Ngày Hạn"), now(), "days"),
  ifs(
    empty(prop("Ngày Hạn")), "⚪ Chưa chốt lịch",
    prop("Trạng Thái") == "Done", style("✅ Đã hoàn thành", "green", "b"),
    days < 0, style("🚨 QUÁ HẠN " + format(abs(days)) + " ngày", "red", "red_background", "b"),
    days == 0, style("🔥 NỘP TRONG HÔM NAY", "orange", "orange_background", "b"),
    days <= 3, style("⚠️ Còn " + format(days) + " ngày", "yellow", "b"),
    style("⏳ Còn " + format(days) + " ngày", "blue")
  )
)
```

> [!TIP]
> **Cách sửa lỗi "Property not found"**: Công thức trên sử dụng `prop("Ngày Hạn")` và `prop("Trạng Thái")`. Tên cột trong bảng của bạn **phải khớp chính xác từng dấu cách và chữ hoa/thường** với tên trong ngoặc kép. Nếu bảng của bạn đặt tên cột là `Ngày` thì phải sửa thành `prop("Ngày")`.

---

### 2. Cài Đặt Công Thức Hiển Thị Thanh Tiến Độ (Progress Bar / Ring)
Áp dụng cho cột `AI Score` trong bảng **EXPERIMENT LOG (PBL6)**:

1. Tạo cột `AI Score` với loại `Formula`.
2. Dán đoạn mã:
   ```javascript
   let(
     score,
     (prop("Recall@5") * 0.3) + (prop("Faithfulness") * 0.5) + (prop("BERTScore") * 0.2),
     round(score * 100) / 100
   )
   ```
3. **Thao tác biến số thập phân thành Thanh Progress Bar màu sắc**:
   - Nhấp vào tiêu đề cột `AI Score` $\rightarrow$ `Edit property`.
   - Tại mục `Number format`: Chọn **`Percent`**.
   - Tại mục `Show as`: Bấm vào nút **`Bar`** (Thanh ngang) hoặc **`Ring`** (Vòng tròn).
   - Tại mục `Color`: Chọn màu bạn thích (Ví dụ: `Green` hoặc `Purple`).
   - Tại mục `Divide by`: Đặt là `1` (vì giá trị từ 0 đến 1 tương ứng 0% - 100%).

---

## 🔗 CHƯƠNG 4: KỸ THUẬT LIÊN KẾT HAI CHIỀU: RELATIONS & ROLLUPS

Đây là "vũ khí tối thượng" giúp biến các bảng rời rạc thành một mạng lưới quản trị thông minh:

```
[Bảng A: DANH MỤC MÔN HỌC] ◄──(Relation 2 Chiều)──► [Bảng B: MASTER TASKS]
            │                                                 │
            └──────(Rollup: Tự động đếm số task đã Done)──────┘
```

### 1. Hướng Dẫn Tạo Cột Relation (Liên Kết Bảng)
Giả sử bạn muốn liên kết mỗi Task trong `MASTER TASKS` với một môn học trong `COURSE DIRECTORY`:

1. Mở bảng `MASTER TASKS`.
2. Bấm dấu `+` ở cột cuối cùng để thêm thuộc tính mới $\rightarrow$ Chọn **`Relation`**.
3. Một ô tìm kiếm hiện ra: Gõ tên bảng **`COURSE DIRECTORY`** $\rightarrow$ Bấm chọn bảng đó.
4. **Bật liên kết 2 chiều (Cực kỳ quan trọng)**:
   - Gạt công tắc **`Show on COURSE DIRECTORY`** sang trạng thái BẬT (Màu xanh).
   - Đặt tên cột hiển thị bên bảng kia (Ví dụ: `Danh Sách Tasks`).
5. Bấm nút **`Add relation`** màu xanh.
6. **Kết quả**: Khi tạo task mới, bạn chỉ cần nhấp vào ô Relation này để chọn môn học tương ứng.

---

### 2. Hướng Dẫn Tạo Cột Rollup (Tính Toán Tự Động Từ Bảng Liên Kết)
Giả sử tại bảng `COURSE DIRECTORY`, bạn muốn tự động hiển thị **% Task Đã Hoàn Thành** của môn đó:

1. Mở bảng `COURSE DIRECTORY`.
2. Bấm dấu `+` thêm cột mới $\rightarrow$ Chọn loại **`Rollup`**.
3. Nhấp chuột vào cột Rollup vừa tạo $\rightarrow$ Bấm **`Edit property`**:
   - Mục `Relation`: Chọn cột liên kết `Danh Sách Tasks` (đã tạo ở bước trên).
   - Mục `Property`: Chọn thuộc tính `Trạng Thái` (Status).
   - Mục `Calculate`: Cuộn xuống dưới cùng $\rightarrow$ Chọn **`Percent per group`** $\rightarrow$ **`Complete`** (Hoặc `Percent checked`).
4. Tại mục `Show as`: Chọn **`Bar`** $\rightarrow$ Chọn màu `Blue`.
5. **Kết quả kỳ diệu**: Mỗi khi bạn tích hoàn thành 1 task ở bảng kia, thanh tiến độ của môn học bên bảng này sẽ tự động tăng lên (Ví dụ: 3/5 task $\rightarrow$ 60%)!

---

## 👁️ CHƯƠNG 5: NGHỆ THUẬT CẤU HÌNH CÁC GÓC NHÌN THÔNG MINH (SMART VIEWS)

Một database có thể xem dưới nhiều góc nhìn khác nhau mà không cần tạo lại bảng dữ liệu.

### 1. Tạo Kanban Board View (Góc Nhìn Kéo Thả Trạng Thái)
Rất phù hợp cho `Sprint Board PBL6` hoặc `Master Tasks`:

1. Nhìn lên góc trên bên trái của Database (cạnh tab *Table*) $\rightarrow$ Bấm vào dấu `+` (Add view).
2. Chọn loại **`Board`**.
3. Đặt tên View: Nhập `🏃 Đang Làm (Kanban)`.
4. Bấm **`Done`**.
5. **Cấu hình phân nhóm (Grouping)**:
   - Nhấp vào biểu tượng `···` của Database $\rightarrow$ Chọn **`Group`**.
   - Mục `Group by`: Chọn `Trạng Thái` (Status).
   - Các cột sẽ hiện ra: `To-do`, `In Progress`, `Done`. Bạn có thể dùng chuột kéo thả task từ cột này sang cột khác!

---

### 2. Tạo Gallery View (Góc Nhìn Thẻ Ảnh Màn Hình)
Dành riêng cho **`LAB ERROR JOURNAL`** môn Quản Trị Mạng và An Toàn Mạng:

1. Bấm dấu `+` cạnh các tab của Database $\rightarrow$ Chọn **`Gallery`**.
2. Đặt tên View: Nhập `📸 Nhật Ký Ảnh Lỗi`.
3. **Cấu hình hiển thị ảnh chụp màn hình**:
   - Bấm vào biểu tượng `···` của Database $\rightarrow$ Chọn **`Layout`** $\rightarrow$ Nhấp vào mục `Gallery`.
   - Mục **`Card preview`**: Đổi từ *None* sang **`Page content`**.
   - Mục **`Card size`**: Chọn **`Medium`**.
   - Bật công tắc **`Fit image`** (để ảnh không bị méo hoặc cắt góc).
4. **Cách sử dụng**: Khi gặp lỗi terminal hay Wireshark $\rightarrow$ Chụp ảnh màn hình (Windows + Shift + S) $\rightarrow$ Mở row tương ứng thành 1 trang riêng $\rightarrow$ Bấm Ctrl + V dán ảnh thẳng vào thân bài viết $\rightarrow$ Ảnh chụp sẽ tự động hiện lên mặt trước của thẻ Gallery!

---

### 3. Tạo Filtered View: Hộp Ôn Luyện Hàng Ngày (Spaced Repetition Queue)
Dành cho Database **`FLASHCARD & ACTIVE RECALL`**:

1. Bấm dấu `+` tạo 1 View dạng `Table` $\rightarrow$ Đặt tên: `⚠️ CẦN ÔN HÔM NAY`.
2. **Cấu hình Bộ lọc (Filter)**:
   - Nhìn lên góc phải thanh công cụ của Database $\rightarrow$ Bấm vào chữ **`Filter`**.
   - Chọn thuộc tính **`Cần Ôn?`**.
   - Thiết lập điều kiện: **`Is checked`** (hoặc `Equals True`).
3. **Kết quả**: View này sẽ ẩn toàn bộ hàng trăm khái niệm đã thuộc, chỉ hiển thị đúng những thẻ đã đến hạn chu kỳ cần não bộ kích hoạt lại!

---

## 🛠️ CHƯƠNG 6: QUY TRÌNH XÂY DỰNG KHÔNG GIAN CHO TỪNG CÔNG TY MÔN HỌC

Sau khi hoàn thành Dashboard tổng, bạn tiến hành setup 6 trang môn học theo vị trí tương ứng:

### 1. Không Gian `02_Company_Machine_Learning_ML`
- Mở tệp: `02_Company_Machine_Learning_ML/04_Notion_Digital_Workspace/NOTION_ML_MACHINE_LEARNING.md`.
- Copy toàn bộ nội dung $\rightarrow$ Tạo page mới trong Notion $\rightarrow$ Dán vào.
- Chuyển bảng `FROM-SCRATCH VS SKLEARN COMPARISON LOG` thành Database.
- Tạo cột Formula `Tốc độ (Delta)` và dán mã:
  ```javascript
  let(
    diff, 
    prop("Runtime Custom (ms)") - prop("Runtime Sklearn (ms)"),
    ifs(
      empty(prop("Runtime Custom (ms)")) or empty(prop("Runtime Sklearn (ms)")), "⚪ Chờ đo đạc",
      diff < 0, style("🚀 Tự code NHANH HƠN " + format(abs(diff)) + "ms", "green", "b"),
      diff == 0, style("⚖️ Ngang bằng", "gray", "b"),
      style("🐢 Sklearn tối ưu hơn " + format(diff) + "ms", "red", "b")
    )
  )
  ```

---

### 2. Không Gian `03_Company_Network_Management_NMA`
- Mở tệp: `03_Company_Network_Management_NMA/04_Notion_Digital_Workspace/NOTION_NMA_NETWORK_MANAGEMENT.md`.
- Tại bảng `LAB ERROR JOURNAL`, tạo cột Formula `Attention` và dán mã:
  ```javascript
  ifs(
    prop("Mức Độ") == "🚨 Nguy hiểm", style("💥 LỖI TRƯỜNG MẠNG - FIX NGAY!", "red", "red_background", "b"),
    prop("Mức Độ") == "⚠️ Thường gặp", style("👀 Chú ý lần sau", "yellow", "b"),
    style("✅ Lỗi nhẹ", "gray")
  )
  ```
- Tạo View `Gallery` như hướng dẫn ở Chương 5.

---

### 3. Không Gian `05_Company_Japanese_Language_JPN`
- Mở tệp: `05_Company_Japanese_Language_JPN/04_Notion_Digital_Workspace/NOTION_JPN_JAPANESE_N3.md`.
- Tại bảng `KANJI MASTER`, tạo cột Formula `Mastery Badge` và dán mã:
  ```javascript
  ifs(
    prop("Confidence") == "🟢 Rất thuộc" and prop("Chu Kỳ") >= 14, style("🏆 MASTERED (Khắc vào não)", "yellow", "yellow_background", "b"),
    prop("Confidence") == "🟡 Tạm" or prop("Chu Kỳ") > 3, style("🔥 ĐANG CÀY", "orange", "b"),
    style("🌱 MỚI HỌC", "gray")
  )
  ```
- Tại bảng `WEEKLY DRILL TRACKER`, tạo cột Formula `Tổng Giờ` và dán mã:
  ```javascript
  let(
    total,
    prop("Kanji Ôn") + prop("Đọc Hiểu") + prop("Nghe") + prop("Memrise"),
    ifs(
      total >= 10, style(format(total) + "h / 10h 🎯 ĐẠT KPI!", "green", "green_background", "b"),
      style(format(total) + "h / 10h 🏃 Cố lên!", "red", "b")
    )
  )
  ```

---

## 🚨 CHƯƠNG 7: CẨM NANG XỬ LÝ SỰ CỐ NOTION THƯỜNG GẶP

| Hiện Tượng Lỗi | Nguyên Nhân Gốc Rễ | Thao Tác Khắc Phục Tức Thì |
| :--- | :--- | :--- |
| **Lỗi: `Type mismatch: expected Text but got Number`** | Dùng dấu cộng `+` ghép trực tiếp chữ với số trong Formula mà không chuyển đổi kiểu dữ liệu. | Dùng hàm `format(biến_số)` bọc quanh biến số trước khi cộng chuỗi (Ví dụ: `"Còn " + format(days) + " ngày"`). |
| **Lỗi: Bảng dán vào bị vỡ hàng ngang trên điện thoại** | Bật quá nhiều cột không cần thiết trên cùng một góc nhìn Table. | Bấm vào biểu tượng `···` của Database $\rightarrow$ Chọn `Properties` $\rightarrow$ Tắt bớt con mắt `👁️` của những cột phụ, chỉ để lại 3-4 cột quan trọng nhất. |
| **Lỗi: Không tìm thấy trang để tạo Relation** | Tên trang đích quá dài hoặc đặt trong một Không gian Workspace khác. | Gõ chính xác từng từ khóa đầu tiên của trang đích vào ô tìm kiếm Relation; đảm bảo cả 2 trang đều nằm trong cùng 1 tài khoản Workspace Notion. |
| **Lỗi: Công thức báo "Circular Reference"** | Cột A tham chiếu đến cột B, trong khi cột B lại tham chiếu ngược lại cột A. | Kiểm tra lại logic tính toán; tách biệt cột nhập liệu thô (Input Number/Date) và cột hiển thị kết quả (Formula). |

---

## 🎯 CHECKLIST 5 PHÚT MỖI NGÀY DÀNH CHO BẠN (DAILY CHECKLIST)
- [ ] **07:00**: Mở View `⚠️ CẦN ÔN HÔM NAY` trên Notion điện thoại hoặc máy tính $\rightarrow$ Ôn sạch các thẻ đến hạn.
- [ ] **12:00**: Kéo task buổi sáng từ `In Progress` sang `Done` trên `Master Weekly Planner`.
- [ ] **17:00**: Nếu làm lab bị lỗi, dành 2 phút dán ảnh màn hình vào `Lab Error Journal`.
- [ ] **21:30**: Kiểm tra cột `Urgency Radar` xem ngày mai có deadline nộp bài nào gấp không để chuẩn bị.
