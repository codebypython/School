# 📜 ĐIỀU LỆ PHÒNG SỐ HÓA & KHÔNG GIAN NOTION LMS (NOTION DIGITAL WORKSPACE DEPT)
## Phòng 04 — Công Ty Hệ Thống & Giải Thuật Hiệu Năng Cao (CORP-07-ALGO)

> **Mã Phòng Ban:** `ALGO-DEPT-04`  
> **Trưởng phòng phụ trách:** Agent `NKA-05` (Notion Architect & Hub Administrator)  
> **Hệ sinh thái liên kết:** Central Notion LMS Hub (`00_Central_Notion_LMS_Hub`)  
> **Tiêu chuẩn công nghệ:** Notion Formula 2.0 / Relational Database Schema / Spaced Repetition

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Số Hóa là **cầu nối không gian số** giữa mã nguồn local và nền tảng quản trị học tập Notion LMS:
1. **Thiết Kế CSDL Thuật Toán (DSA Problem Tracker DB)**: Xây dựng cơ sở dữ liệu quan hệ quản lý tiến độ giải bài tập LeetCode, Codeforces, phân loại theo Tags (Array, Tree, Graph, DP) và mức độ khó (Easy, Medium, Hard).
2. **Hệ Thống Lặp Lại Ngắt Quãng (Spaced Repetition Flashcards)**: Tự động tính toán ngày ôn tập tiếp theo (Next Review Date) dựa trên thuật toán SuperMemo SM-2 nhúng trong Notion Formula 2.0.
3. **Đồng Bộ Dữ Liệu 1-Click (Markdown to Notion Ready)**: Đảm bảo toàn bộ tài liệu trong phòng này có thể import trực tiếp vào Notion mà không bị vỡ định dạng bảng, callout hay khối code.

---

## ⚖️ 2. BỘ QUY TẮC ĐỊNH DẠNG NOTION BẤT BIẾN (NOTION FORMAT INVARIANTS)

1. **Chuẩn Hóa Khối Trích Dẫn & Callouts**:
   - Sử dụng cú pháp Callout chuẩn của Notion Markdown:
     ```markdown
     > 💡 **Khái niệm cốt lõi**: Định nghĩa ngắn gọn...
     > ⚠️ **Bẫy thuật toán**: Lưu ý trường hợp biên...
     ```
2. **Quy Chuẩn CSDL Quan Hệ (Relations & Rollups)**:
   - Mọi Database bài tập trong công ty bắt buộc phải có thuộc tính quan hệ trỏ về `Core Subjects Database` của Holding.
3. **Cú Pháp Notion Formula 2.0**:
   - Toàn bộ công thức tính toán ngày ôn tập hoặc thanh tiến độ (Progress Bar) phải tuân thủ chuẩn Formula 2.0 của Notion (hỗ trợ `lets()`, `map()`, `filter()`).

---

## 📁 3. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
04_Notion_Digital_Workspace/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 NOTION_DSA_TRACKER_SCHEMA.md          # Đặc tả CSDL bài tập thuật toán Notion
├── 📄 NOTION_SPACED_REPETITION_FORMULAS.md   # Thư viện công thức Formula 2.0
├── 📁 flashcards_vault/                     # Ngân hàng Flashcards Active Recall
│   ├── Memory_Pointers_Flashcards.md
│   ├── Trees_Graphs_Flashcards.md
│   └── Dynamic_Programming_Flashcards.md
└── 📁 page_templates/                       # Các template trang Notion sẵn sàng import
    ├── leetcode_solution_template.md        # Mẫu ghi chép lời giải thuật toán 1 bài
    └── algorithm_system_cheat_sheet.md      # Bảng tra cứu Big-O trực quan
```

---

## 💻 4. MẪU THIẾT KẾ SCHEMA CSDL & CÔNG THỨC NOTION 2.0 (GOLD MASTER NOTION)

```markdown
# 📊 CSDL THEO DÕI THUẬT TOÁN (ALGOCORE PROBLEM TRACKER)

### Thuộc tính bảng (Properties Schema):
1. `Problem Name` (Title): Tên bài toán (VD: 001. Two Sum).
2. `Platform` (Select): LeetCode, Codeforces, VNOI, DUT Judge.
3. `Difficulty` (Select): Easy 🟢, Medium 🟡, Hard 🔴.
4. `Data Structure Tag` (Multi-select): Array, Hash Table, Two Pointers, DP, Graph.
5. `Status` (Status): Not Started, In Progress, Mastered, Need Review.
6. `Confidence Level` (Number 1-5): Đánh giá độ tự tin khi giải.
7. `Last Solved Date` (Date): Ngày giải gần nhất.

### 🧮 Công thức Formula 2.0: Tự động tính ngày ôn tập tiếp theo (Next Review):
```notion
lets(
  days,
  if(prop("Confidence Level") == 5, 14,
  if(prop("Confidence Level") == 4, 7,
  if(prop("Confidence Level") == 3, 3, 1))),
  dateAdd(prop("Last Solved Date"), days, "days")
)
```

### 📊 Công thức Formula 2.0: Thanh tiến độ trực quan (Visual Progress Bar):
```notion
lets(
  percent, prop("Confidence Level") / 5,
  fill, repeat("🟩", round(percent * 10)),
  empty, repeat("⬜", 10 - round(percent * 10)),
  fill + empty + " " + format(round(percent * 100)) + "%"
)
```
```
