# 📜 ĐIỀU LỆ PHÒNG RÈN LUYỆN 5 KHỐI KỸ NĂNG (SKILL DIVISIONS & DRILLS DEPT)
## Phòng 03 — Công Ty Đào Tạo Ngôn Ngữ & Hội Nhập Toàn Cầu (CORP-05-JPN)

> **Mã Phòng Ban:** `JPN-DEPT-03`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (`HM-00`) & Giám Sát Sư Phạm (`PSD-04`)  
> **Cố vấn chuyên môn:** DUT Japanese Mentor (`AGENT_PROFILE.md`)  
> **Tiêu chuẩn chất lượng:** JLPT N3 Benchmark / 214 Bộ Thủ Hán Tự / Phản Xạ Shadowing / Shinkanzen Master

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng Rèn Luyện Kỹ Năng là **võ đường ngôn ngữ thực chiến** của Global Nihongo Engineering Institute:
1. **Rèn Luyện 5 Trụ Cột Kỹ Năng JLPT N3**: Phân rã bài tập chuyên sâu theo từng kỹ năng: Chữ Hán (Kanji), Từ vựng (Vocabulary), Ngữ pháp (Grammar), Đọc hiểu (Reading), và Nghe hiểu (Listening/Shadowing).
2. **Kỹ Thuật Chiết Tự Hán Tự (Kanji Decomposition)**: Giải mã chữ Hán theo 214 Bộ thủ kết hợp âm Hán Việt để nhớ mặt chữ sâu sắc và lâu dài, tránh học vẹt nét chữ rời rạc.
3. **Luyện Nghe Nói Đuổi (Shadowing Engine)**: Huấn luyện cơ miệng và thính giác bắt kịp ngữ điệu, tốc độ nói tự nhiên của người bản xứ và từ vựng chuyên ngành công nghệ thông tin (IT Nihongo).

---

## 2. BỘ QUY TẮC BẤT BIẾN (HARD CONSTRAINTS & DRILL INVARIANTS)
1. **Quy Tắc Chiết Tự Hán Tự Bắt Buộc (Kanji Radical Invariant)**:
   - **BẮT BUỘC**: Mọi chữ Hán mới khi được giảng dạy hoặc đưa vào flashcard phải có:
     1. Âm Hán Việt in hoa.
     2. Phân tích cấu tạo bộ thủ (Ví dụ: `休` = Bộ Nhân `亻` đứng cạnh Bộ Mộc `木` $\rightarrow$ Người tựa vào cây để *Nghỉ ngơi*).
     3. Cặp âm On-yomi và Kun-yomi kèm ví dụ từ vựng ghép.
2. **Quy Tắc Học Từ Vựng Theo Cụm (Collocation Rule)**:
   - **CẤM TUYỆT ĐỐI**: Học thuộc lòng từ vựng đơn lẻ, cô lập.
   - **BẮT BUỘC**: Học theo cụm cố định gồm `[Danh từ] + [Trợ từ] + [Động từ]` (Ví dụ: thay vì học mỗi từ `薬` (thuốc), bắt buộc học `薬を飲む` - uống thuốc).
3. **Quy Tắc Ngữ Pháp Tương Phản (Contrastive Grammar Invariant)**:
   - **CẤM TUYỆT ĐỐI**: Giải thích một mẫu ngữ pháp mà không đặt cạnh mẫu ngữ pháp tương tự dễ nhầm lẫn.
   - **BẮT BUỘC**: Phân tích sắc thái phân biệt (Nuance Discrimination) giữa các cặp kinh điển:
     - `〜ために` (Mục đích có chủ ý) vs `〜ように` (Mục đích hướng tới trạng thái không thể kiểm soát).
     - `〜わけではない` (Phủ định một phần) vs `〜はずがない` (Phủ định khả năng xảy ra tuyệt đối).
4. **Quy Tắc Đọc Hiểu Bắt Từ Khóa (Signal Words Rule)**:
   - Khi giải thích bài đọc hiểu, bắt buộc phải chỉ ra các từ nối chuyển ý (接続詞): `しかし` (tuy nhiên), `つまり` (tóm lại), `したがって` (do đó), vì luận điểm chính của tác giả luôn nằm ngay sau các từ này.

---

## 3. BỘ LỆNH & SKILLS ROUTE TÁC NGHIỆP CHUẨN (TOOLCHAIN)
- **Bộ sách cốt lõi**: Shinkanzen Master N3 (4 cuốn), Mimi Kara Oboeru N3, Shin Nihongo 500 Mon.
- **Phần mềm bổ trợ**: Anki Spaced Repetition (Deck N3 Tango & Kanji), Mazii Dictionary, Yomitan.
- **Luyện nghe phản xạ**: Audio CD Mimi Kara Oboeru N3 (Tốc độ 1.0x $\rightarrow$ 1.2x).

```bash
# 1. Chạy script tạo nhanh flashcard Anki từ danh sách từ vựng IT
python scripts/build_anki_vocab.py --source kanji_n3.txt --tags "N3,IT"

# 2. Kiểm tra độ chuẩn xác của âm Hán Việt và bộ thủ trong bài tập
python scripts/validate_kanji_drills.py --dir ./drills/
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
03_Skill_Divisions_and_Drills/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── 01_Kanji_Divisions/                # Rèn luyện chữ Hán chiết tự theo bộ thủ
├── 02_Vocabulary_Collocations/        # Rèn luyện từ vựng theo cụm từ thực tế
├── 03_Grammar_Nuances/                # Rèn luyện ngữ pháp tương phản
├── 04_Reading_Speed_Drills/           # Rèn luyện đọc hiểu bắt từ khóa chuyển ý
└── 05_Listening_Shadowing_Engine/     # Rèn luyện phản xạ nghe nói đuổi IT
```

---

## 5. MẪU KHUNG CODE / GOLD MASTER BOILERPLATE (GRAMMAR CONTRASTIVE ANALYSIS)
```markdown
### 📚 Phân biệt chuyên sâu: 〜ために vs 〜ように

#### 1. Mẫu: `V-る / Nの + ために` (Để / Nhằm mục đích...)
- **Bản chất**: Hành động mang tính **ý chí kiểm soát tuyệt đối** của chủ ngữ. Cả 2 vế trước và sau đều là hành vi chủ động.
- **Công thức**: 
  - Động từ ý chí (V-る): `家を買うために、貯金しています。` (Để mua nhà [hành động chủ ý], tôi đang tiết kiệm tiền).
- **Cấm kỵ**: Vế trước KHÔNG ĐƯỢC là động từ chỉ khả năng (`可能動詞`) hoặc trạng thái (`見えない`, `分からない`).

#### 2. Mẫu: `V-る / V-ない + ように` (Để sao cho / Hướng tới trạng thái...)
- **Bản chất**: Không mang tính ý chí trực tiếp, mà hướng tới một **mục tiêu, trạng thái hoặc sự biến đổi tự nhiên**.
- **Công thức**:
  - Động từ khả năng hoặc thể phủ định: `日本語が上手に話せるように、毎日練習しています。` (Để có thể nói giỏi tiếng Nhật [trạng thái khả năng], tôi luyện tập mỗi ngày).
  - Tránh xảy ra rủi ro: `風邪をひかないように、暖かくしてください。` (Để không bị cảm lạnh, hãy mặc ấm vào).

#### 💡 Bảng Tóm Tắt Ghi Nhớ Nhanh:
| Tiêu chí | `〜ために` | `〜ように` |
| :--- | :--- | :--- |
| **Bản chất vế trước** | Hành động có chủ ý (Mua, đi, học) | Trạng thái / Khả năng / Phủ định (Có thể, Hiểu, Không bị) |
| **Chủ ngữ 2 vế** | Bắt buộc là cùng 1 chủ ngữ | Có thể là 2 chủ ngữ khác nhau |
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [ ] **DoD-1 (Kanji Chiết Tự 100%)**: 100% chữ Hán trong bài đều có phân tích bộ thủ và âm Hán Việt.
- [ ] **DoD-2 (Ngữ Pháp Có Ví Dụ 2 Chiều)**: Mọi mẫu ngữ pháp đều có câu ví dụ khẳng định và tình huống cấm kỵ (phân biệt sắc thái).
- [ ] **DoD-3 (Drill Pass $\ge 80\%$)**: Làm bài kiểm tra trắc nghiệm Shin Nihongo 500 Mon đạt điểm tối thiểu 80%.
- [ ] **DoD-4 (Shadowing Verified)**: Đã luyện đọc đuổi theo file audio mà không vấp quá 2 lần.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ HỌC TẬP (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: Không kịp giờ làm bài thi phần Đọc hiểu (Reading Time Out)
- **Triệu chứng**: Thí sinh đọc tỉ mỉ từng từ khiến hết giờ làm bài mà vẫn còn 2 bài đọc dài chưa giải quyết.
- **Cách khắc phục**:
  1. Thay đổi chiến thuật: Đọc câu hỏi trước, xác định từ khóa (Keyword) trong câu hỏi.
  2. Dùng kỹ thuật Skimming/Scanning: Chỉ quét đoạn văn chứa từ khóa và đọc kỹ câu trước/sau từ khóa đó.
  3. Bỏ qua các từ vựng mới không ảnh hưởng đến mạch logic toàn bài.

### Sự cố 2: Lúng túng trước các câu hỏi Đọc hiểu có liên từ chuyển ý
- **Triệu chứng**: Chọn đáp án ở vế đầu câu thay vì vế sau của liên từ `しかし` hoặc `だが`.
- **Cách khắc phục**: Ghi nhớ nguyên tắc: "Ý của tác giả luôn nằm sau liên từ tương phản (Ý A nhưng THỰC RA LÀ Ý B)".
