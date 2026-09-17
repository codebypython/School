# 📜 ĐIỀU LỆ PHÒNG SỐ HÓA & KHÔNG GIAN NOTION (NOTION DIGITAL WORKSPACE DEPT)
## Phòng 04 — Công Ty Đào Tạo Ngôn Ngữ & Hội Nhập Toàn Cầu (CORP-05-JPN)

> **Mã Phòng Ban:** `JPN-DEPT-04`  
> **Trưởng phòng phụ trách:** Agent `NKA-05` (Notion Knowledge Architect) & Trợ Lý Vận Hành LMS  
> **Cấp bậc quản trị:** Cấp 2 — Số hóa không gian học tiếng Nhật, quản lý cơ sở dữ liệu Hán tự và cơ chế Gamification rèn luyện

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `JPN-DEPT-04` chịu trách nhiệm kiến tạo, duy trì và tối ưu hóa không gian số Notion LMS dành cho môn Tiếng Nhật N3 & IT Nihongo:
1. **Quản trị Cơ sở dữ liệu Chữ Hán (Kanji Master DB)**: Xây dựng cơ sở dữ liệu 650 chữ Hán N3 kèm bộ thủ, âm On/Kun, âm Hán Việt và công thức cấp huy hiệu tự động (Mastery Badges).
2. **Theo dõi Tiến độ Rèn luyện 15 Tuần (Weekly Drill Tracker)**: Thiết kế bảng theo dõi chỉ số KPI học tập (mục tiêu 10 giờ/tuần), tỷ lệ hoàn thành bài tập ngữ pháp và số lượng flashcard đã ôn luyện.
3. **Quản lý Thư viện Thuật ngữ IT Nhật Bản (IT Nihongo Lexicon)**: Đồng bộ hóa danh mục hơn 500 từ vựng chuyên ngành công nghệ thông tin và mẫu câu giao tiếp dự án phần mềm.

---

## 2. BỘ QUY TẮC BẤT BIẾN (WORKSPACE INVARIANTS & HARD CONSTRAINTS)
1. **Nguyên tắc Gamification & Khích Lệ Tích Cực**: Các bảng theo dõi trên Notion phải tích hợp các trạng thái tiến độ trực quan bằng thanh progress bar và huy hiệu thăng hạng (Novice $\rightarrow$ Intermediate $\rightarrow$ Master).
2. **Nguyên tắc Notion Formula 2.0 Chuẩn Mực**: Các trường tính toán cấp độ và số ngày đến kỳ thi JLPT bắt buộc sử dụng cú pháp Formula 2.0 hiện đại (dùng `lets()`, `ifs()`, `dateBetween()`).
3. **Nguyên tắc Không Bỏ Sót Furigana**: Các từ vựng và ngữ pháp trên Notion phải được trình bày rõ ràng với cách đọc (Hiragana) trong ngoặc hoặc chú thích.
4. **Nguyên tắc Lưu Bản Sao Cục Bộ Git**: Toàn bộ cấu trúc Notion bắt buộc phải có bản sao Markdown đầy đủ `NOTION_JPN_JAPANESE_N3.md` lưu trữ trong git.

---

## 3. BỘ LỆNH & CÔNG CỤ ĐỒNG BỘ NOTION (TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Kiểm tra tính hợp lệ của file Markdown không gian Notion tiếng Nhật
python -c "import re; content = open('NOTION_JPN_JAPANESE_N3.md', encoding='utf-8').read(); print(f'Char Count: {len(content)} | Valid: True')"

# 2. Định dạng lại bảng từ vựng Markdown trước khi nhập vào Notion
npx prettier --write "*.md"

# 3. Quét kiểm tra cú pháp Formula 2.0 trong thư mục
grep -rn "lets(" ./
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
04_Notion_Digital_Workspace/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── NOTION_JPN_JAPANESE_N3.md          # Không gian Notion tích hợp sẵn sàng import
├── schemas/                           # Định dạng schema JSON của các Database tiếng Nhật
│   ├── kanji_master_schema.json
│   └── weekly_drills_schema.json
└── templates/                         # Mẫu trang phân tích ngữ pháp & nhật ký đọc hiểu
    └── GRAMMAR_DRILL_TEMPLATE.md
```

---

## 5. MẪU KHUNG DATABASE NOTION FORMULA 2.0 (GOLD MASTER SCHEMA)

### Công Thức Formula 2.0 Tính Điểm Thuần Thục Chữ Hán (Kanji Mastery Badge)
```javascript
/* NOTION FORMULA 2.0: Tự động cấp Huy hiệu Nắm vững Hán tự dựa trên Spaced Repetition */
lets(
  radicalDone, if(prop("Radicals Identified"), 1, 0),
  onKunDone, if(prop("On/Kun Mastered"), 1, 0),
  hanVietDone, if(prop("Han-Viet Meanings Known"), 1, 0),
  sampleSentenceDone, if(prop("Sample Sentences Created"), 1, 0),
  totalDone, radicalDone + onKunDone + hanVietDone + sampleSentenceDone,

  ifs(
    totalDone == 4,
    "👑 HÁN TỰ BẬC THẦY (Kanji Master)",
    totalDone >= 3,
    "🥈 THUẦN THỤC (Intermediate)",
    totalDone >= 1,
    "🥉 ĐANG HỌC (Novice)",
    "⚪ CHƯA HỌC (Unseen)"
  )
)
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **Trường dữ liệu đầy đủ**: Database Kanji có đủ các trường: `Hán tự`, `Âm Hán Việt`, `Bộ thủ`, `Nghĩa tiếng Việt`, `On/Kun`, `Cấp bậc Huy hiệu Formula 2.0`.
- [x] **File Markdown sẵn sàng import**: Tệp `NOTION_JPN_JAPANESE_N3.md` chứa toàn bộ cấu trúc để kéo thả vào Notion.
- [x] **Theo dõi 15 tuần học**: Có lịch trình chia nhỏ mục tiêu theo từng tuần.
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ ĐỒNG BỘ NOTION (TROUBLESHOOTING & RUNBOOK)

### Sự cố 1: Bảng từ vựng tiếng Nhật bị vỡ cột nghĩa khi copy vào Notion
- **Hiện tượng**: Các ký tự Kanji bị nhảy dòng hoặc cột nghĩa tiếng Việt bị dồn vào cột Furigana.
- **Cách khắc phục**: Chuyển bảng thành file `.csv` có mã hóa UTF-8 with BOM trước khi dùng tính năng "Merge with CSV" trên Notion.

### Sự cố 2: Lỗi công thức Formula 2.0 không hiển thị emoji huy hiệu
- **Cách khắc phục**: Kiểm tra chuỗi emoji trong hàm `ifs()`, đảm bảo ký tự emoji được bọc trong dấu ngoặc kép chuẩn UTF-8 `"👑"`, không dùng ký tự Unicode thoát chuỗi bị lỗi.
