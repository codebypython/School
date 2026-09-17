# 📜 ĐIỀU LỆ PHÒNG CHIẾN LƯỢC & KẾ HOẠCH 15 TUẦN (STRATEGY & PLANNING DEPT)
## Phòng 01 — Công Ty Đào Tạo Ngôn Ngữ & Hội Nhập Toàn Cầu (CORP-05-JPN)

> **Mã Phòng Ban:** `JPN-DEPT-01`  
> **Trưởng phòng phụ trách:** Agent `PSD-04` (Pedagogical Scaffolding Designer) & Giám Đốc Đào Tạo Ngôn Ngữ  
> **Cấp bậc quản trị:** Cấp 1 — Định hình lộ trình 15 tuần JLPT N3 & Tiếng Nhật Chuyên ngành Công nghệ Thông tin (IT Nihongo)

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `JPN-DEPT-01` chịu trách nhiệm toàn diện về chiến lược sư phạm, lộ trình 15 tuần và bộ tiêu chuẩn đánh giá năng lực Nhật ngữ cho kỹ sư CNTT:
1. **Lộ Trình Tích Hợp Kép (JLPT N3 + IT Nihongo)**: Kết hợp chặt chẽ giữa việc chuẩn bị cho kỳ thi năng lực tiếng Nhật JLPT N3 (Từ vựng, Ngữ pháp, Đọc hiểu, Nghe hiểu) và kỹ năng giao tiếp công việc thực tế trong dự án phần mềm với khách hàng Nhật Bản (BrSE, Offshore Dev).
2. **Chuẩn Hóa Phương Pháp Giảng Dạy Mimi Kara Oboeru & Shinkanzen Master**: Thiết kế giáo trình dựa trên ngữ cảnh thực tế, phân biệt các cặp ngữ pháp đồng nghĩa dễ gây nhầm lẫn và ứng dụng thuật toán lặp lại ngắt quãng (Spaced Repetition System - SRS).
3. **Quản Lý Barem Đánh Giá Năng Lực**: Thiết lập hệ thống kiểm tra định kỳ (Weekly Drills) và thi thử mô phỏng (Mock Exams) chuẩn theo barem của Hiệp hội Hỗ trợ Quốc tế Nhật Bản (JEES).

---

## 2. BỘ QUY TẮC BẤT BIẾN (PEDAGOGICAL INVARIANTS & HARD CONSTRAINTS)
1. **Nguyên tắc Kanji Trong Ngữ Cảnh (Kanji in Context Invariant)**: Cấm tuyệt đối học chữ Hán (Kanji) đơn lẻ bằng cách chép phạt cơ học. Bắt buộc phải học Kanji kèm âm On/Kun, các từ ghép phổ biến (Jukugo) và đặt trong câu văn cụ thể.
2. **Nguyên tắc Phân Biệt Sắc Thái Ngữ Pháp (Nuance Differentiation)**: Khi giới thiệu bất kỳ mẫu ngữ pháp nào có ý nghĩa tương đương (ví dụ: `わけではない` vs `というわけではない`, `に関して` vs `について`), bắt buộc phải có bảng phân tích so sánh về: Mức độ trang trọng (Politeness), Tính chủ quan/khách quan, và Bối cảnh cấm dùng.
3. **Nguyên tắc Furigana & Hán Tự Chuẩn**: Toàn bộ tài liệu tiếng Nhật phải có Hán tự chuẩn, bổ sung Furigana cho các từ vựng N3 mới và phiên âm Romaji (nếu cần cho người mới bắt đầu).
4. **Nguyên tắc Kiểm Soát Kích Thước File Sách PDF**: Sách giáo trình bản scan lớn (>50MB) bắt buộc phải đưa vào `.gitignore` và quản lý qua tài liệu hướng dẫn tải riêng.

---

## 3. BỘ LỆNH & CÔNG CỤ LUYỆN TẬP TIẾNG NHẬT (TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Phân tích từ vựng và tra cứu từ điển bằng MeCab (Morpheme Analyzer)
echo "昨日はプロジェクトの仕様書を作成しました。" | mecab

# 2. Tạo file Deck thẻ nhớ Anki (.apkg) từ file từ vựng CSV
python scripts/generate_anki_deck.py --input vocab_n3_it.csv --output n3_it_deck.apkg

# 3. Quét kiểm tra các file tài liệu tiếng Nhật mã hóa UTF-8
file -bi *.md
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
01_Strategy_and_Curriculum/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── AGENT_PROFILE.md                   # Chân dung & phong thái Mentor tiếng Nhật
├── ROADMAP_AND_CURRICULUM.md          # Lộ trình 15 tuần chi tiết JLPT N3 & IT Nihongo
├── README.md                          # Sổ tay tổng quan hướng dẫn học tiếng Nhật
└── 00_Dashboard_and_Planning/         # Kế hoạch và bảng phân bổ thời gian hàng tuần
```

---

## 5. MẪU KHUNG HỌC TẬP & MA TRẬN PHÂN BIỆT NGỮ PHÁP (GOLD MASTER BOILERPLATE)

### Ma Trận So Sánh Các Mẫu Ngữ Pháp Chỉ Nguyên Nhân / Lý Do N3 (`~せいで` vs `~おかげで` vs `~せいで`)
```markdown
# 🎌 MA TRẬN PHÂN TÍCH SẮC THÁI NGỮ PHÁP: CHỈ NGUYÊN NHÂN / KẾT QUẢ

| Mẫu Ngữ Pháp | Cấu Trúc Kết Nối | Bản Chất & Sắc Thái Ngữ Nghĩa | Ví Dụ Điển Hình Trong CNTT |
|:---|:---|:---|:---|
| **〜おかげで** | V/A/N (Thể ngắn) + おかげで (Nの) | Kết quả **TÍCH CỰC**, mang hàm ý biết ơn, may mắn. "Nhờ có..." | 先輩がコードレビューをしてくれた**おかげで**、バグを早期発見できた。<br>*(Nhờ tiền bối review code mà phát hiện bug từ sớm.)* |
| **〜せいで** | V/A/N (Thể ngắn) + せいで (Nの) | Kết quả **TIÊU CỰC**, mang hàm ý trách móc, đổ lỗi. "Do tại / Tại vì..." | ネットワークが不安定だった**せいで**、デプロイに失敗してしまった。<br>*(Tại vì mạng chập chờn mà việc deploy bị thất bại.)* |
| **〜によって** | N + によって / による + N | Nguyên nhân mang tính **TRUNG TÍNH, KHÁCH QUAN**, thường dùng trong văn viết/báo cáo kỹ thuật. "Do / Bởi vì..." | サーバーの過負荷**によって**、システムがダウンしました。<br>*(Hệ thống bị sập do tình trạng quá tải máy chủ.)* |
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **Lộ trình 15 tuần đầy đủ**: Mỗi tuần có đủ mục tiêu 4 kỹ năng (Kanji, Từ vựng, Ngữ pháp, IT Drill).
- [x] **Có bảng phân biệt sắc thái**: 100% các cặp ngữ pháp đồng nghĩa đều có bảng so sánh ngữ cảnh.
- [x] **Tích hợp ngữ cảnh CNTT**: Tối thiểu 30% ví dụ mẫu sử dụng thuật ngữ dự án phần mềm thực tế.
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ HỌC TẬP (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: Học trước quên sau, rớt từ vựng Kanji sau 2 tuần
- **Hiện tượng**: Học viên nhớ được chữ Hán trong bài học nhưng sau 10 ngày không nhận diện được mặt chữ khi làm đề đọc hiểu.
- **Quy trình xử lý**:
  1. Chuyển sang phương pháp Spaced Repetition (SRS) với phần mềm Anki.
  2. Thiết lập chu kỳ ôn tập: Ngày 1 $\rightarrow$ Ngày 3 $\rightarrow$ Ngày 7 $\rightarrow$ Ngày 14 $\rightarrow$ Ngày 30.
  3. Luyện đọc đoạn văn ngắn chứa từ vựng thay vì nhìn flashcard từ đơn lập.

### Sự cố 2: Nhầm lẫn kính ngữ (Keigo: Sonkeigo vs Kenjougo) khi giao tiếp với khách hàng
- **Hiện tượng**: Dùng kính ngữ tôn kính (Sonkeigo) cho hành động của bản thân hoặc dùng khiêm nhường ngữ (Kenjougo) cho hành động của đối tác.
- **Quy trình xử lý**:
  1. Vẽ sơ đồ ranh giới: Mình/Công ty mình (Uchi) vs Khách hàng/Đối tác (Soto).
  2. Áp dụng quy tắc ngón tay: Hành động của Uchi $\rightarrow$ Hạ thấp mình bằng Kenjougo (`いたします`, `申します`); Hành động của Soto $\rightarrow$ Nâng cao khách bằng Sonkeigo (`なさいます`, `おっしゃいます`).
