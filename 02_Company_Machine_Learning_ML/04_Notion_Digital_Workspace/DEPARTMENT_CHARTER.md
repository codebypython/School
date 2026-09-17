# 📜 ĐIỀU LỆ PHÒNG SỐ HÓA & KHÔNG GIAN NOTION (NOTION DIGITAL WORKSPACE DEPT)
## Phòng 04 — Công Ty Trí Tuệ Nhân Tạo & Học Máy (CORP-02-ML)

> **Mã Phòng Ban:** `ML-DEPT-04`  
> **Trưởng phòng phụ trách:** Agent `NKA-05` (Notion Knowledge Architect) & Trợ Lý Vận Hành LMS  
> **Cấp bậc quản trị:** Cấp 2 — Số hóa tri thức, quản lý bảng cơ sở dữ liệu Notion Formula 2.0 và theo dõi tiến độ học tập

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `ML-DEPT-04` chịu trách nhiệm kiến tạo, duy trì và tối ưu hóa không gian làm việc số Notion LMS dành riêng cho bộ môn Machine Learning:
1. **Quản trị Cơ sở dữ liệu Toán học & Thuật toán**: Thiết kế hệ thống database theo dõi tiến độ 15 tuần, công thức toán KaTeX (`$$...$$`), và mã nguồn thực thi tương ứng.
2. **Theo dõi Chênh lệch Hiệu năng (Delta Benchmarking)**: Tích hợp thuộc tính đo đạc tốc độ `From-Scratch (NumPy)` so với `Production (Scikit-Learn)` để sinh viên đánh giá định lượng chi phí tính toán.
3. **Quản lý Bài tập & Đồ án ĐHBK Đà Nẵng**: Đồng bộ hóa danh mục bài tập lớn, tiêu chí chấm điểm (Rubric) và trạng thái nộp bài của sinh viên.

---

## 2. BỘ QUY TẮC BẤT BIẾN (WORKSPACE INVARIANTS & HARD CONSTRAINTS)
1. **Nguyên tắc Toán học Chuẩn KaTeX**: Mọi công thức toán học lưu trữ trên Notion bắt buộc phải sử dụng khối toán KaTeX hiển thị chuẩn, không dùng ảnh chụp màn hình chất lượng thấp.
2. **Nguyên tắc Notion Formula 2.0**: Mọi công thức tính toán tiến độ, tỷ lệ hoàn thành hoặc cảnh báo deadline phải sử dụng cú pháp Formula 2.0 hiện đại (dùng `lets()`, `ifs()`, hàm định dạng số và ngày tháng).
3. **Nguyên tắc Liên kết Quan hệ Hai chiều (Bidirectional Relations)**: Bảng thuật toán (Algorithms DB) bắt buộc liên kết 2 chiều với Bảng bài tập (Labs DB) và Bảng công thức toán (Math Foundations DB).
4. **Nguyên tắc Đồng bộ Offline Markdown**: Toàn bộ cấu trúc Notion bắt buộc phải có một bản sao tương ứng dạng file Markdown `.md` trong thư mục phòng ban để phục vụ việc lưu trữ cục bộ và kiểm soát phiên bản bằng Git.

---

## 3. BỘ LỆNH & CÔNG CỤ ĐỒNG BỘ NOTION (TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Chuyển đổi và kiểm tra cú pháp Markdown trước khi import vào Notion
npx markdown-toc -i NOTION_ML_MACHINE_LEARNING.md

# 2. Đồng bộ các trang Notion thông qua Notion API CLI
notion-cli sync --page-id "ML-CORE-WORKSPACE" --file NOTION_ML_MACHINE_LEARNING.md

# 3. Kiểm tra tính toàn vẹn của các biểu thức KaTeX
python -c "import re; content = open('NOTION_ML_MACHINE_LEARNING.md', encoding='utf-8').read(); katex_blocks = re.findall(r'\$\$(.*?)\$\$', content, re.DOTALL); print(f'Total KaTeX Blocks: {len(katex_blocks)}')"
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
04_Notion_Digital_Workspace/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── NOTION_ML_MACHINE_LEARNING.md      # Không gian Notion tích hợp sẵn sàng kéo thả
├── schemas/                           # Định dạng schema JSON của các Database Notion
│   ├── algorithms_database_schema.json
│   └── lab_submissions_schema.json
└── templates/                         # Mẫu trang ghi chú thuật toán & bài giải chi tiết
    └── ALGORITHM_NOTE_TEMPLATE.md
```

---

## 5. MẪU KHUNG DATABASE NOTION FORMULA 2.0 (GOLD MASTER SCHEMA)

### Công Thức Formula 2.0 Tính Tỷ Lệ Hoàn Thành Thuật Toán & Cảnh Báo Ôn Tập
```javascript
/* NOTION FORMULA 2.0: Thuật toán tính chỉ số Readiness & Cảnh báo Spaced Repetition */
lets(
  /* Đếm số tiêu chí đã hoàn tất */
  mathDone, if(prop("Math Theory Validated"), 1, 0),
  scratchDone, if(prop("NumPy Scratch Implemented"), 1, 0),
  sklearnDone, if(prop("Sklearn Pipeline Ready"), 1, 0),
  quizPassed, if(prop("MicroQuiz Passed"), 1, 0),
  totalScore, mathDone + scratchDone + sklearnDone + quizPassed,
  percentage, (totalScore / 4) * 100,

  /* Tính số ngày kể từ lần review cuối */
  daysSinceReview, dateBetween(now(), prop("Last Reviewed At"), "days"),

  /* Xuất kết quả trực quan */
  ifs(
    percentage == 100 && daysSinceReview > 14,
    "⚠️ Cần ôn tập lại (Đã qua " + daysSinceReview + " ngày)",
    percentage == 100,
    "🟢 Hoàn thành xuất sắc (100%)",
    percentage >= 50,
    "🟡 Đang thực hiện (" + percentage + "%)",
    "🔴 Chưa đạt yêu cầu (" + percentage + "%)"
  )
)
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **Trực quan hóa công thức toán**: Mọi thẻ bài học đều có công thức mất mát và đạo hàm render chuẩn xác trên giao diện Notion.
- [x] **Trường dữ liệu đầy đủ**: Database có tối thiểu 6 trường: `Week`, `Algorithm Name`, `Category (Supervised/Unsupervised)`, `Mathematical Complexity`, `Implementation Status`, `Performance Delta`.
- [x] **Đồng bộ song hành Git-Notion**: Mọi thay đổi trên Notion đều có thể trích xuất ra file `NOTION_ML_MACHINE_LEARNING.md` lưu trữ trong Git.
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ ĐỒNG BỘ NOTION (TROUBLESHOOTING & RUNBOOK)

### Sự cố 1: Công thức KaTeX hiển thị lỗi đỏ (`ParseError`) khi paste vào Notion
- **Hiện tượng**: Khối công thức toán bị báo lỗi cú pháp hoặc không render được dấu ngoặc ma trận.
- **Nguyên nhân**: Dùng sai cú pháp LaTeX (ví dụ thiếu escape ký tự `\begin{bmatrix}` hoặc viết tắt không được KaTeX hỗ trợ).
- **Cách khắc phục**:
  1. Thay thế các lệnh không tương thích bằng cú pháp chuẩn KaTeX:
     ```latex
     \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \quad \text{thay vì} \quad \left( \begin{array} ... \end{array} \right)
     ```
  2. Kiểm tra trước tại trang kiểm thử trực tuyến KaTeX sandbox trước khi đưa vào Notion.

### Sự cố 2: Thuộc tính Rollup hoặc Formula 2.0 hiển thị `Circular Dependency`
- **Hiện tượng**: Bảng cơ sở dữ liệu báo lỗi phụ thuộc vòng tròn giữa 2 cột tính toán.
- **Cách khắc phục**: Tách biệt logic: Một cột thuần túy lưu trữ giá trị nhập liệu cơ bản (Raw Value), cột thứ hai tính toán trung gian, cột thứ ba xuất nhãn cảnh báo trực quan.
