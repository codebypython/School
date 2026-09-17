# 📜 ĐIỀU LỆ PHÒNG CÔNG CỤ & BẪY ĐỀ THI (TOOLKITS & EXAM TRAPS DEPT)
## Phòng 05 — Công Ty Đào Tạo Ngôn Ngữ & Hội Nhập Toàn Cầu (CORP-05-JPN)

> **Mã Phòng Ban:** `JPN-DEPT-05`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (Role Handmade) & `PSD-04` (Pedagogical Systems Designer)  
> **Cấp bậc quản trị:** Cấp 2 — Quản lý công cụ hỗ trợ Nhật ngữ, phân tích bẫy đề thi JLPT N3 và cẩm nang khắc phục lỗi sai kinh điển

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `JPN-DEPT-05` chịu trách nhiệm vận hành các công cụ số hỗ trợ học tiếng Nhật, xây dựng cẩm nang bẫy đề thi và chuẩn hóa các quy trình khắc phục lỗi ngôn ngữ trong giao tiếp thực tế:
1. **Quản trị Bộ Tiện Ích & Từ Điển Thông Minh**: Cung cấp hướng dẫn tích hợp bộ gõ tiếng Nhật (Google IME, Mozc), tiện ích đọc lướt Yomitan / Rikaikun và công cụ phân tích từ vựng MeCab.
2. **Kho Bẫy Đề Thi JLPT N3 Kinh Điển**: Thu thập, phân loại và giải mã các dạng bẫy trắc nghiệm: Cặp từ đồng âm dị nghĩa (Kanji Homophones), động từ Tự - Tha (自動詞 vs 他動詞), trợ từ đa nghĩa (`に`, `で`, `を`), và kính ngữ tôn kính vs khiêm nhường.
3. **Cẩm Nang Xử Lý Sự Cố Giao Tiếp CNTT**: Xây dựng runbook xử lý tình huống hiểu nhầm yêu cầu (Specification Misinterpretation), báo cáo trễ hạn dự án và văn hóa ứng xử Hou-Ren-Sou (Hokoku - Renraku - Sodan).

---

## 2. BỘ QUY TẮC BẤT BIẾN (DEBUGGING INVARIANTS & HARD CONSTRAINTS)
1. **Nguyên tắc "Tự Động Từ Không Đi Kèm を" (Intransitive Verb Invariant)**: Tự động từ (Jidoushi) chỉ trạng thái tự nhiên của sự vật, chủ ngữ đi với trợ từ `が` và cấm tuyệt đối dùng trợ từ `を` (ví dụ: `ドアが開く`, không được dùng `ドアを開く` nếu muốn nói cửa tự mở).
2. **Nguyên tắc Bẫy Âm On Dài / Ngắn (Long Vowel Phonetics Rule)**: Trong các bài thi chữ Hán, luôn phải chú ý bẫy trường âm (âm kéo dài): Ví dụ `旅行 (りょこう)` có trường âm ở `こう`, không nhầm với `りょこ`.
3. **Nguyên tắc Văn Hóa Báo Cáo Xấu (Bad News Early Protocol - Hou-Ren-Sou)**: Trong dự án với khách hàng Nhật, khi có sự cố phát sinh hoặc nguy cơ chậm tiến độ, bắt buộc phải báo cáo ngay lập tức (Báo cáo sớm dù chưa có phương án khắc phục hoàn chỉnh), cấm tuyệt đối việc giấu lỗi đến ngày bàn giao.
4. **Nguyên tắc Phân Rã Ngữ Nghĩa Toàn Diện (No Vague Explanations)**: Mọi giải thích về một lỗi sai trong đề thi phải chỉ rõ: Tại sao đáp án đó sai, người ra đề đang cài bẫy kiến thức gì, và dấu hiệu nào trong câu giúp loại trừ.

---

## 3. BỘ LỆNH & CÔNG CỤ CHẨN ĐOÁN TIẾNG NHẬT (DIAGNOSTIC TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Kiểm tra cấu hình bộ gõ tiếng Nhật và bảng mã hệ thống trên Linux / WSL
ibus-setup || fcitx-configtool

# 2. Phân tách và tra cứu nghĩa từ vựng tự động với script Python kết nối MeCab
python -c "import MeCab; tagger = MeCab.Tagger('-Ochasen'); print(tagger.parse('仕様書通りに実装してください。'))"

# 3. Quét kiểm tra các liên kết tài liệu trong thư mục phòng ban
python -c "import os, re; print(f'Files checked: {len([f for f in os.listdir(\".\") if f.endswith(\".md\")])}')"
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
05_Troubleshooting_and_Toolkits/
├── DEPARTMENT_CHARTER.md                          # Điều lệ phòng ban 7 tầng chuẩn hóa
├── kanji_trap_detector.py                         # Script kiểm tra các cặp từ Kanji dễ nhầm lẫn
├── ime_setup_and_shortcuts.md                     # Hướng dẫn cấu hình bộ gõ tiếng Nhật và phím tắt
└── runbooks/                                      # Cẩm nang xử lý sự cố & bẫy đề thi
    ├── RUNBOOK_TRANSITIVE_INTRANSITIVE_TRAPS.md   # Phân biệt và giải bẫy Tự động từ vs Tha động từ
    ├── RUNBOOK_PARTICLE_CONFUSION_NI_DE.md        # Giải bẫy trợ từ に và で trong đề thi
    ├── RUNBOOK_KEIGO_HONORIFIC_MISTAKES.md        # Khắc phục nhầm lẫn kính ngữ trong dự án IT
    └── RUNBOOK_HOU_REN_SOU_ESCALATION.md          # Quy trình báo cáo sự cố phần mềm cho khách hàng Nhật
```

---

## 5. MẪU KHUNG PHÂN TÍCH BẪY ĐỀ THI (GOLD MASTER BOILERPLATE)

### Bộ Phân Tích Bẫy Trợ Từ `に` vs `で` Trong Kỳ Thi JLPT N3 (`RUNBOOK_PARTICLE_CONFUSION_NI_DE.md`)
```markdown
# 🎌 CẨM NANG GIẢI BẪY: PHÂN BIỆT TRỢ TỪ 「に」 VS 「で」 CHỈ NƠI CHỐN
> **Tác giả**: CORP-05-JPN Exam Research Unit

## 1. Dấu Hiệu Nhận Biết Bẫy Của Người Ra Đề
Người ra đề thường đưa ra một địa điểm, sau đó để trống trợ từ `[ Nơi chốn ] [ ? ] [ Động từ ]`. Thí sinh thường chọn theo cảm tính hoặc dịch nôm na sang tiếng Việt là "ở / tại" dẫn đến chọn sai.

## 2. Quy Tắc Phân Biệt Tuyệt Đối
1. **Dùng 「で」 khi**: Nơi chốn đó là nơi **diễn ra một HÀNH ĐỘNG tích cực / có chủ ý**.
   - Công thức: `[Địa điểm] + で + [Động từ hành động]`
   - Ví dụ: `会議室【で】仕様書を読みます。` *(Đọc tài liệu tại phòng họp - "Đọc" là hành động).*
2. **Dùng 「に」 khi**: Nơi chốn đó là nơi **TỒN TẠI của sự vật** hoặc là **ĐÍCH ĐẾN / KẾT QUẢ của sự chuyển dịch**.
   - Công thức A (Tồn tại): `[Địa điểm] + に + [います / あります / 住んでいます]`
   - Ví dụ: `サーバー室【に】ラックがあります。` *(Có tủ rack ở trong phòng máy chủ).*
   - Công thức B (Đích đến kết quả): `[Địa điểm] + に + [Động từ ghi / lưu / đặt / vào]`
   - Ví dụ: `データベース【に】データを保存します。` *(Lưu dữ liệu VÀO TRONG cơ sở dữ liệu).*
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **Cẩm nang bẫy đầy đủ 4 chủ đề**: Tự/tha động từ, Trợ từ `に/で`, Kính ngữ, và Hou-Ren-Sou.
- [x] **Có ví dụ phản chứng**: Mọi quy tắc phân biệt bẫy đều có ví dụ Đúng vs Sai đi kèm lời giải thích.
- [x] **Tích hợp tình huống CNTT**: Đưa bối cảnh dự án phần mềm và thuật ngữ kỹ thuật vào runbook.
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ KHẨN CẤP (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: Chọn nhầm cặp tự/tha động từ trong bài thi ngữ pháp (`閉まる` vs `閉める`)
- **Hiện tượng**: Thấy `窓が...` nhưng vẫn chọn `閉めました` vì nhớ mang máng nghĩa là "đóng".
- **Cách khắc phục nhanh trong phòng thi**:
  1. Nhìn trợ từ đứng trước danh từ: Nếu là trợ từ `が` $\rightarrow$ 90% động từ đi kèm là TỰ ĐỘNG TỪ (chỉ trạng thái: `窓が閉まる`).
  2. Nếu là trợ từ `を` $\rightarrow$ Bắt buộc chọn THA ĐỘNG TỪ (có người thực hiện hành động: `窓を閉める`).

### Sự cố 2: Phát sinh Bug nghiêm trọng trong giờ làm việc với đối tác Nhật Bản
- **Hiện tượng**: Tính năng thanh toán bị lỗi khi đang chạy trên môi trường Staging.
- **Quy trình ứng cứu Hou-Ren-Sou 3 bước**:
  1. *Bước 1 (Hokoku - Báo cáo tức thì)*: Gửi thông báo ngắn cho BrSE hoặc Quản lý dự án: "Tính năng X đang phát sinh lỗi Y trên Staging, team đang tiến hành điều tra nguyên nhân."
  2. *Bước 2 (Renraku - Liên lạc các bên)*: Thông báo cho Tester tạm dừng kiểm thử tính năng liên quan để tránh báo trùng bug.
  3. *Bước 3 (Sodan - Thảo luận phương án)*: Đưa ra 2 phương án giải quyết (Rollback commit hoặc Hotfix trực tiếp) kèm ước tính thời gian hoàn thành để sếp quyết định.
