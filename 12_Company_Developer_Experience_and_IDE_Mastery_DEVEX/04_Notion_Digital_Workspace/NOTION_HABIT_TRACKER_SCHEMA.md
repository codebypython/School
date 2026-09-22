# 📋 SCHEMA NOTION DATABASE: BẢNG THEO DÕI PHẢN XẠ IDE 14 NGÀY
## Notion Habit & Reflex Tracker for 80/20 IDE Mastery

Bản thiết kế database này dùng để import hoặc tạo trực tiếp trên Notion Workspace của học viên, giúp lượng hóa sự tiến bộ qua từng ngày luyện tập.

---

## 1. THIẾT KẾ CÁC TRƯỜNG THUỘC TÍNH (DATABASE PROPERTIES)

| Tên trường (Property) | Loại dữ liệu (Type) | Cấu hình & Tùy chọn | Mục đích sử dụng |
| :--- | :--- | :--- | :--- |
| **Day ID** | Title | Text (vd: `Day 01: Multi-Window & Alt+Tab`) | Tên bài luyện tập trong lộ trình |
| **Phase / Week** | Select | `Tuần 1: Navigation & Editing`, `Tuần 2: Agentic Workflows` | Phân loại giai đoạn huấn luyện |
| **Status** | Status | `Not Started`, `In Training`, `Mastered (Passed)` | Trạng thái hoàn thành bài tập |
| **Drill Speed (sec)**| Number | Định dạng: `Number` (vd: `8`) | Thời gian hoàn thành bài test tốc độ (giây) |
| **Target Speed (sec)**| Number | Định dạng: `Number` (vd: `10`) | Thời gian chuẩn tối đa để được pass |
| **Mouse-Free Ratio** | Number | Định dạng: `Percent (%)` (vd: `95%`) | Tỉ lệ thời gian không chạm chuột trong buổi code |
| **Key Reflex Checklist** | Multi-select | `Ctrl+P`, `Ctrl+D`, `Alt+Up/Down`, `F12`, `F2`, `Ctrl+I`, `@mentions`, `/grill-me` | Các phím tắt đã thực hiện thành phản xạ |
| **Daily Reflection** | Rich Text | Ghi chú văn bản | Ghi lại những tình huống ngón tay còn lúng túng |
| **Pass Formula** | Formula | Xem công thức mục 2 | Tự động tính điểm đạt/không đạt |

---

## 2. CÔNG THỨC NOTION TÍNH TOÁN TỰ ĐỘNG (NOTION FORMULAS 2.0)

### Công thức tính Trạng thái Nghiệm thu (`Pass Formula`)
Kiểm tra xem học viên có đạt chuẩn kép: Tốc độ nhỏ hơn Target VÀ Tỉ lệ không dùng chuột trên 85%:

```javascript
ifs(
  prop("Status") == "Mastered (Passed)", "🏆 XUẤT SẮC (MASTERED)",
  and(prop("Drill Speed (sec)") <= prop("Target Speed (sec)"), prop("Mouse-Free Ratio") >= 0.85), "✅ ĐẠT CHUẨN (PASS)",
  prop("Status") == "In Training", "⏳ ĐANG RÈN LUYỆN",
  "⚠️ CHƯA ĐẠT CHUẨN"
)
```

---

## 3. CÁC CHẾ ĐỘ HIỂN THỊ ĐỀ XUẤT (RECOMMENDED DATABASE VIEWS)

1. **Board View (Theo Trạng thái)**:
   - Group by: `Status`.
   - Card Preview: None, hiển thị các thuộc tính: `Mouse-Free Ratio`, `Drill Speed (sec)`, `Pass Formula`.
2. **Calendar View (Lịch 14 ngày)**:
   - Hiển thị từng bài drill trải dài trên 14 ngày liên tục, giúp duy trì chuỗi học không bị đứt đoạn (Don't break the chain).
3. **Table View (Master Audit)**:
   - Hiển thị đầy đủ tất cả các cột để đối soát vào cuối mỗi tuần cùng Mentor.
