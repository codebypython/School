# 🧪 THƯ VIỆN CÔNG THỨC NOTION 2.0 (ADVANCED FORMULAS)
# Nâng cấp Hệ thống Học tập Semester 7 thành Hệ thống Quản trị (LMS)

Tài liệu này chứa các đoạn code **Notion Formula 2.0** chuyên sâu nhất, được thiết kế may đo riêng cho đặc thù của từng môn học. Với các hàm hiện đại như `let()`, `ifs()`, và `style()`, các Database của bạn giờ đây không chỉ lưu trữ dữ liệu tĩnh, mà còn có khả năng tự động phân tích, cảnh báo và định dạng màu sắc thông minh.

---

## 🏠 1. SEMESTER DASHBOARD (COMMAND CENTER)

### 1.1. Urgency Radar (Radar Cảnh báo Deadline)
*Đích đến: Bảng **DEADLINE & EXAM TRACKER**.*
*Cách hoạt động:* Đếm ngược ngày tới Deadline và tự động thay đổi màu sắc (Đỏ = Quá hạn, Cam = Hôm nay, Xanh = An toàn) để đập vào mắt người dùng.

**Tạo một cột Formula mới tên là `Tình Trạng` và dán code sau:**
```javascript
let(
  days, 
  dateBetween(prop("Ngày"), now(), "days"),
  ifs(
    empty(prop("Ngày")), "⚪ Chưa chốt lịch",
    prop("Trạng Thái") == "Done", style("✅ Đã hoàn thành", "green", "b"),
    days < 0, style("🚨 QUÁ HẠN " + format(abs(days)) + " ngày", "red", "red_background", "b"),
    days == 0, style("🔥 NỘP TRONG HÔM NAY", "orange", "orange_background", "b"),
    days <= 3, style("⚠️ Còn " + format(days) + " ngày", "yellow", "b"),
    style("⏳ Còn " + format(days) + " ngày", "blue")
  )
)
```

### 1.2. GPA Auto-Grader (Tính điểm chữ tự động theo chuẩn DUT)
*Đích đến: Bảng **GPA ESTIMATOR**.*
*Cách hoạt động:* Tự tính điểm Hệ 10 (40% Quá trình + 60% Cuối kỳ) và map sang Hệ chữ (A, B+, C...) theo thang điểm tín chỉ Bách khoa.

**Tại cột Formula `Điểm chữ`, dán code sau:**
```javascript
let(
  finalScore, 
  round((prop("QT (40%)") * 0.4 + prop("CK (60%)") * 0.6) * 10) / 10,
  ifs(
    empty(prop("QT (40%)")) or empty(prop("CK (60%)")), "⏳ Chờ điểm",
    finalScore >= 8.5, style("A (Xuất sắc) - " + format(finalScore), "green", "b"),
    finalScore >= 8.0, style("B+ (Giỏi) - " + format(finalScore), "blue", "b"),
    finalScore >= 7.0, style("B (Khá) - " + format(finalScore), "blue"),
    finalScore >= 6.5, style("C+ (TB Khá) - " + format(finalScore), "yellow", "b"),
    finalScore >= 5.5, style("C (Trung bình) - " + format(finalScore), "yellow"),
    finalScore >= 5.0, style("D+ (TB Yếu) - " + format(finalScore), "orange", "b"),
    finalScore >= 4.0, style("D (Yếu) - " + format(finalScore), "orange"),
    style("F (Trượt) - " + format(finalScore), "red", "red_background", "b")
  )
)
```

---

## 📡 2. QUẢN TRỊ MẠNG (NMA) & AN TOÀN MẠNG (SECURITY)

### 2.1. Dynamic Spaced Repetition (Thuật toán SuperMemo cơ bản)
*Đích đến: Bảng **FLASHCARD & ACTIVE RECALL**.*
*Vấn đề:* Công thức cũ chỉ cộng một số `Chu Kỳ` cố định.
*Giải pháp:* Công thức mới sẽ tự động tính **Ngày Ôn Tiếp Theo (Next Review)** dựa trên trạng thái `Confidence`.

**Tạo một cột Formula mới tên là `Ngày Ôn Tiếp Theo` (Định dạng hiển thị là Date) và dán code:**
```javascript
let(
  multiplier,
  ifs(
    prop("Confidence") == "🔴 Chưa thuộc", 1,
    prop("Confidence") == "🟡 Tạm", 3,
    prop("Confidence") == "🟢 Rất thuộc", 7,
    0
  ),
  if(
    empty(prop("Lần Ôn Gần Nhất")), 
    now(), 
    dateAdd(prop("Lần Ôn Gần Nhất"), prop("Chu Kỳ (Ngày)") * multiplier, "days")
  )
)
```
*(Sau đó, tại cột `Cần Ôn?`, bạn chỉ cần sửa lại thành: `prop("Ngày Ôn Tiếp Theo") <= now()`)*

### 2.2. Error Severity Highlighter (Nhận diện lỗi Nghiêm trọng)
*Đích đến: Bảng **LAB ERROR JOURNAL**.*
*Cách hoạt động:* Highlight đỏ rực toàn bộ thẻ nếu Mức độ là "Nguy hiểm", giúp dễ tìm lỗi khi xem dưới dạng Gallery View.

**Tạo một cột Formula tên `Attention` và dán code:**
```javascript
ifs(
  prop("Mức Độ") == "🚨 Nguy hiểm", style("💥 LỖI TRƯỜNG MẠNG - FIX NGAY!", "red", "red_background", "b"),
  prop("Mức Độ") == "⚠️ Thường gặp", style("👀 Chú ý lần sau", "yellow", "b"),
  style("✅ Lỗi nhẹ", "gray")
)
```

---

## 🧠 3. HỌC MÁY (ML) & COMPUTER VISION (CV)

### 3.1. Performance Delta Calculator (Đo lường mức độ tối ưu thuật toán)
*Đích đến: Bảng **FROM-SCRATCH VS LIBRARY COMPARISON LOG** (Môn ML).*
*Cách hoạt động:* Tự động tính chênh lệch thời gian chạy (Runtime) giữa code Numpy tự viết và thư viện Sklearn, sau đó render ra nhận xét tự động.

**Tạo một cột Formula tên `Tốc độ (Delta)` và dán code:**
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

## 🤖 4. ĐỒ ÁN CHUYÊN NGÀNH (PBL6 - VIETLAWASSIST)

### 4.1. Weighted RAG Score Calculator (Chấm điểm Mô hình AI tự động)
*Đích đến: Bảng **EXPERIMENT LOG**.*
*Cách hoạt động:* Tính điểm tổng hợp cho mô hình theo trọng số (Recall: 30%, Faithfulness: 50%, BERTScore: 20%) và vẽ thanh Progress Bar màu sắc.

**Tạo cột Formula tên `AI Score` (Chỉnh hiển thị dạng Bar/Ring) và dán code:**
```javascript
let(
  score,
  (prop("Recall@5") * 0.3) + (prop("Faithfulness") * 0.5) + (prop("BERTScore") * 0.2),
  score
)
```
*(Notion Tip: Click vào Edit Property của cột `AI Score` $\rightarrow$ Chọn mục `Number format` là `Percent` $\rightarrow$ Chọn `Show as: Bar` $\rightarrow$ Chọn màu sắc theo ý muốn).*

### 4.2. Task Bottleneck Detector (Phát hiện Task bị kẹt)
*Đích đến: Bảng **SPRINT BOARD**.*
*Cách hoạt động:* Quét các task đang ở trạng thái "In Progress" và tính xem nó đã nằm đó bao nhiêu ngày (so sánh với Deadline).

**Tạo cột Formula tên `Bottleneck Check` và dán code:**
```javascript
let(
  daysOpen,
  dateBetween(now(), prop("Deadline"), "days"),
  ifs(
    prop("Status") == "Done", "✅ Xong",
    prop("Status") == "In Progress" and daysOpen > 0, style("🚨 KẸT TASK! Trễ " + format(daysOpen) + " ngày", "red", "red_background", "b"),
    prop("Status") == "In Progress", style("🏃 Đang làm an toàn", "green"),
    "⚪ Nằm chờ"
  )
)
```

---

## 🇯🇵 5. TIẾNG NHẬT (JAPANESE N3)

### 5.1. Kanji Mastery Badge (Hệ thống Huy hiệu Gamification)
*Đích đến: Bảng **KANJI MASTER / VOCAB BUILDER**.*
*Cách hoạt động:* Cấp huy hiệu tự động dựa trên mức độ tự tin và cột `Chu kỳ` ôn tập hiện tại của từ vựng đó.

**Tạo cột Formula tên `Mastery Badge` và dán code:**
```javascript
ifs(
  prop("Confidence") == "🟢 Rất thuộc" and prop("Chu Kỳ") >= 14, style("🏆 MASTERED (Khắc vào não)", "yellow", "yellow_background", "b"),
  prop("Confidence") == "🟡 Tạm" or prop("Chu Kỳ") > 3, style("🔥 ĐANG CÀY", "orange", "b"),
  style("🌱 MỚI HỌC", "gray")
)
```

### 5.2. Study Goal Ring (Trình theo dõi KPI Học Tập 10h/tuần)
*Đích đến: Bảng **WEEKLY DRILL TRACKER**.*
*Cách hoạt động:* Cộng tổng thời gian học Nghe, Đọc, Kanji và đánh giá xem đã đạt mục tiêu (ví dụ 10 giờ) chưa.

**Tại cột Formula `Tổng Giờ` đã có sẵn, hãy thay bằng code sau:**
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

## 💡 HƯỚNG DẪN COPY BỎ TÚI (CHEATSHEET)
1. **Làm sao để hiện background màu nổi bật trong bảng?** 
   $\rightarrow$ Dùng `style("Văn bản", "red", "red_background")`. Các màu hỗ trợ: `blue`, `brown`, `gray`, `green`, `orange`, `pink`, `purple`, `red`, `yellow`.
2. **Làm sao để làm chữ in đậm, in nghiêng?** 
   $\rightarrow$ Thêm argument `"b"` (bold) hoặc `"i"` (italic), `"u"` (underline), `"s"` (strikethrough) vào trong hàm `style()`.
3. **Khai báo biến cục bộ (Local Variables)?**
   $\rightarrow$ Dùng `let(tên_biến, công_thức, kết_quả_trả_về)`. Điều này giúp code gọn hơn rất nhiều thay vì viết lại `prop("...")` hàng chục lần.
