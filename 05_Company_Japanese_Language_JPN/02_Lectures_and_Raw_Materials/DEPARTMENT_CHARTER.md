# 📜 ĐIỀU LỆ PHÒNG GIÁO TRÌNH GỐC & SÁCH (ORIGINAL TEXTBOOKS & BOOKS DEPT)
## Phòng 02 — Công Ty Đào Tạo Ngôn Ngữ & Hội Nhập Toàn Cầu (CORP-05-JPN)

> **Mã Phòng Ban:** `JPN-DEPT-02`  
> **Trưởng phòng phụ trách:** Agent `SMS-02` (Syllabus & Material Sentinel) & Thư Ký Học Thuật Tiếng Nhật  
> **Cấp bậc quản trị:** Cấp 2 — Thu thập, thẩm định ER-QVR và số hóa kho giáo trình kinh điển luyện thi JLPT N3 & IT Nihongo

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `JPN-DEPT-02` chịu trách nhiệm lưu trữ, số hóa, lập chỉ mục và kiểm soát chất lượng toàn bộ giáo trình, sách giáo khoa tiếng Nhật chuẩn quốc tế:
1. **Quản Lý Bộ Giáo Trình N3 Kinh Điển**:
   - *Shinkanzen Master N3* (Từ vựng, Ngữ pháp, Đọc hiểu, Nghe hiểu): Giáo trình chuyên sâu phân tích ngữ cảnh, sắc thái từ và bẫy đề thi.
   - *Mimi Kara Oboeru N3*: Học ngữ pháp và từ vựng qua phản xạ âm thanh và câu ví dụ ngữ cảnh.
   - *Nihongo Soumatome N3*: Hệ thống hóa kiến thức trọng tâm theo kế hoạch 6 tuần.
2. **Biên Soạn Tài Liệu Tiếng Nhật Chuyên Ngành CNTT**: Lưu trữ sách thuật ngữ IT (IT用語), mẫu email thương mại (Business Mail) và mẫu đặc tả yêu cầu phần mềm (Specification Documents).
3. **Thẩm Định Bản Quyền & Kích Thước Tệp**: Đảm bảo các file PDF không vi phạm giới hạn commit git và tuân thủ các quy định học thuật.

---

## 2. BỘ QUY TẮC BẤT BIẾN (CURATION INVARIANTS & HARD CONSTRAINTS)
1. **Nguyên tắc Quản Lý File PDF Sách Quá Khổ**: Sách PDF scan dung lượng lớn (>50MB) bắt buộc phải đưa vào `.gitignore`. Cung cấp file `books/README.md` lưu trữ liên kết tải ngoài kèm mã băm SHA-256 để xác thực tệp.
2. **Nguyên tắc Nguồn Gốc Xuất Bản Chuẩn Nhật Bản (Authentic Japanese Sources)**: Mọi giáo trình phải có nguồn gốc từ các nhà xuất bản uy tín của Nhật Bản: 3A Corporation (3A Network), ALC Press, hoặc Ask Publishing.
3. **Nguyên tắc Chuẩn Mã Hóa UTF-8**: Mọi tệp Markdown, tệp text trích xuất từ sách tiếng Nhật bắt buộc lưu dưới định dạng UTF-8 để không bị lỗi font Hán tự (Mojibake).
4. **Nguyên tắc Tách Rời Bài Giảng & Lời Giải (Spaced Self-Testing)**: Các bài tập trong sách khi được số hóa thành đề thi online phải tách riêng phần câu hỏi và phần đáp án giải thích chi tiết.

---

## 3. BỘ LỆNH & TOOLCHAIN XỬ LÝ HỌC LIỆU (TOOLCHAIN & INGESTION PIPELINE)
```bash
# 1. Kiểm tra mã băm SHA-256 xác thực các tệp sách PDF
sha256sum books/*.pdf > books/checksums.sha256

# 2. Tìm kiếm nhanh mẫu ngữ pháp hoặc từ vựng trong kho tóm tắt sách
grep -rn "わけではない" ./summaries/

# 3. Kiểm tra các file sách có kích thước vượt quá giới hạn Git
find books/ -type f -size +40M -exec ls -lh {} \;
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
02_Lectures_and_Raw_Materials/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── books/                             # Thư mục chứa sách điện tử & README tải sách
│   ├── README.md                      # Hướng dẫn tải bộ sách Shinkanzen & Mimi Kara Oboeru
│   └── checksums.sha256               # Mã băm xác thực tính toàn vẹn của sách
└── summaries/                         # Bản tóm tắt học thuật Markdown chuẩn ER-QVR
    ├── SUMMARY_SHINKANZEN_GRAMMAR.md
    └── SUMMARY_IT_VOCABULARY_INDEX.md
```

---

## 5. MẪU TƯ LIỆU HỌC THUẬT CHUẨN ER-QVR (GOLD MASTER BLUEPRINT)

### Bản Tóm Tắt Mẫu Email Thương Mại Chuẩn IT Doanh Nghiệp Nhật (`SUMMARY_IT_VOCABULARY_INDEX.md`)
```markdown
# 🎌 TÀI LIỆU HỌC THUẬT: MẪU EMAIL THÔNG BÁO TIẾN ĐỘ DỰ ÁN (PROJECT PROGRESS REPORT)
> **Nguồn trích dẫn**: Business Japanese for IT Engineers (3A Corporation) | Điểm ER-QVR: 97/100

## 1. Tiêu Đề Email Chuẩn (Email Subject Line)
`【進捗報告】DUT-System開発プロジェクト_20260918_NguyenVanA`  
*(Bắt buộc có tag định danh dự án, ngày tháng và họ tên người gửi)*

## 2. Thân Bài Email (Email Body with Business Keigo)
```text
ABC株式会社
システム開発部
佐藤部長

いつも大変お世話になっております。
DUTオフショア開発チームのグエンでございます。

標題の件につきまして、今週の開発進捗状況をご報告いたします。

【今週の実績】
1. ユーザー認証機能（JWT/OAuth2）の実装：完了（100%）
2. データベースマイグレーションの実施：完了（100%）

【課題および相談事項】
外部APIのレスポンス遅延が確認されたため、現在キャッシュ（Redis）の導入を検討しております。
仕様変更の必要性について、来週月曜日の定例会にてご相談させていただければ幸いです。

お忙しいところ恐れ入りますが、ご確認のほどよろしくお願い申し上げます。

--------------------------------------------------
Nguyen Van A (グエン・ヴァン・A)
DUT School Holdings - IT Offshoring Division
Email: nguyen.a@corp.dut.edu.vn
--------------------------------------------------
```
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **File sách lớn được quản lý qua README**: Không tồn tại file PDF >50MB trong git tree.
- [x] **Trích xuất mục lục đầy đủ**: Danh mục các bài học trong Shinkanzen Master được lập chỉ mục rõ ràng.
- [x] **Tích hợp mẫu email và hội thoại IT**: Có bài học thực tế về giao tiếp văn phòng với khách hàng Nhật.
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ TÀI LIỆU (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: Lỗi hiển thị font chữ tiếng Nhật biến thành ký tự lạ (Mojibake: ???)
- **Hiện tượng**: Mở file Markdown hoặc text tiếng Nhật trên Windows bị lỗi hiển thị toàn dấu hỏi chấm hoặc ký tự rác.
- **Nguyên nhân**: File được lưu với bảng mã Shift-JIS hoặc CP932 của Windows cũ thay vì chuẩn UTF-8 toàn cầu.
- **Quy trình xử lý**:
  1. Mở file bằng VS Code hoặc Notepad++, chọn "Reopen with Encoding" $\rightarrow$ `Shift_JIS`.
  2. Chọn "Save with Encoding" $\rightarrow$ `UTF-8 with BOM` hoặc `UTF-8`.
  3. Chạy lệnh `iconv -f SHIFT_JIS -t UTF-8 input.txt > output_utf8.txt` nếu dùng dòng lệnh Linux/WSL.

### Sự cố 2: Tệp sách PDF bị hỏng liên kết tải về
- **Hiện tượng**: Link lưu trữ Google Drive của sách bị hết hạn hoặc quyền truy cập bị chặn.
- **Cách khắc phục**: Thư ký học thuật định kỳ kiểm tra link tải hàng tháng và duy trì ít nhất 2 nguồn lưu trữ dự phòng (Mirror links) trong `books/README.md`.
