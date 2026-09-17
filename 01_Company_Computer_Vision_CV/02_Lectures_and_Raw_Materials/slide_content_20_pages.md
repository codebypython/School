# 🎤 NỘI DUNG CHI TIẾT 20 SLIDE — BONE AGE ASSESSMENT
## Sẵn sàng copy vào Canva | Deadline: Hôm nay 04/09/2026

> **Hướng dẫn sử dụng tài liệu này:**
> - Mỗi slide có: **Tiêu đề**, **Nội dung gạch đầu dòng** (copy trực tiếp vào Canva), **Gợi ý thiết kế**, và **Script thuyết trình** (để 2 bạn tập nói)
> - Bảng màu khuyến nghị: Nền `#0B132B` (xanh đen y tế), Accent `#48CAE4` (cyan neon), Success `#52B788`, Warning `#F4A261`
> - Font: **Montserrat** (tiêu đề) + **Inter** (nội dung)

---

## ═══════════════════════════════════════════
## PHẦN A: BỐI CẢNH & ĐẶT BÀI TOÁN (Slide 1–4)
## ═══════════════════════════════════════════

---

### 📄 SLIDE 1 — TRANG BÌA (Title Slide)

**TIÊU ĐỀ CHÍNH:**
```
HỆ THỐNG TỰ ĐỘNG ĐÁNH GIÁ TUỔI XƯƠNG
TỪ ẢNH X-QUANG BÀN TAY TRẺ EM
```

**TIÊU ĐỀ PHỤ:**
```
Bone Age Assessment using Multimodal Deep Learning
on Pediatric Hand X-ray Radiographs
```

**THÔNG TIN NHÓM:**
```
Học phần: Thị giác Máy tính (Computer Vision)
Trường: Đại học Bách khoa — Đại học Đà Nẵng (DUT)
Giảng viên hướng dẫn: [Tên GV]
Nhóm thực hiện: [Tên SV1] — [Tên SV2]
Học kỳ: 7 | Năm học: 2026–2027
```

**🎨 Gợi ý thiết kế Canva:**
- Nền Dark Mode (#0B132B), bên trái: text trắng nổi bật, bên phải: hình ảnh X-quang bàn tay với hiệu ứng lưới công nghệ (grid overlay, dạng hologram)
- Thêm icon nhỏ: 🦴 + 🤖 + 📊
- Hiệu ứng gradient nhẹ ở góc dưới từ #0B132B → #1C2541

**🎙️ Script thuyết trình (30 giây):**
> "Kính chào Thầy/Cô và các bạn. Hôm nay nhóm chúng em xin trình bày đề tài Hệ thống Tự động Đánh giá Tuổi xương từ ảnh X-quang bàn tay trẻ em. Đây là một bài toán ứng dụng Deep Learning kết hợp xử lý ảnh cổ điển vào lĩnh vực hình ảnh y tế nhi khoa."

---

### 📄 SLIDE 2 — MỤC LỤC (Agenda)

**TIÊU ĐỀ:** `NỘI DUNG TRÌNH BÀY`

**4 KHỐI NỘI DUNG:**

```
01 ─── BỐI CẢNH LÂM SÀNG & ĐẶT BÀI TOÁN
       Tuổi xương là gì? Tại sao cần tự động hóa?
       Điểm sáng tạo: Regression vs Classification

02 ─── PHÂN TÍCH DỮ LIỆU RSNA BONE AGE
       12,611 ảnh X-quang | Phân bố tuổi & giới tính
       Histogram chi tiết | Đặc thù ảnh y tế

03 ─── PHƯƠNG PHÁP ĐỀ XUẤT
       Pipeline xử lý ảnh cổ điển (CLAHE, Otsu)
       Kiến trúc Multimodal CNN (ResNet/EfficientNet + Gender)
       Explainable AI (Grad-CAM)

04 ─── THIẾT KẾ HỆ THỐNG & KẾ HOẠCH
       Giao diện Web App (Streamlit)
       Biểu đồ tăng trưởng WHO
       Lộ trình 4 tuần triển khai
```

**🎨 Gợi ý thiết kế Canva:**
- 4 thẻ (card) xếp dọc hoặc ngang, mỗi thẻ có số `01`–`04` cỡ lớn, tiêu đề đậm + mô tả nhạt
- Thanh tiến trình gradient từ xanh dương → xanh lá ở phía dưới

---

### 📄 SLIDE 3 — BỐI CẢNH LÂM SÀNG (Clinical Background)

**TIÊU ĐỀ:** `TUỔI XƯƠNG LÀ GÌ? TẠI SAO CẦN TỰ ĐỘNG HÓA?`

**CỘT TRÁI — Định nghĩa:**
```
🦴 TUỔI XƯƠNG (Bone Age / Skeletal Age)

• Thước đo mức trưởng thành SINH HỌC
  của hệ xương ở trẻ em

• KHÁC với tuổi theo ngày sinh
  (Chronological Age)

• Đơn vị: THÁNG (1 – 228 tháng ≈ 0 – 19 tuổi)

• Phương pháp đo: Chụp X-quang bàn tay TRÁI
  → So sánh với Atlas mẫu chuẩn
```

**CỘT PHẢI — Ý nghĩa y khoa:**
```
⚕️ ỨNG DỤNG TRONG NHI KHOA

• Chẩn đoán rối loạn NỘI TIẾT:
  → Dậy thì sớm (Precocious Puberty)
  → Suy hormone tăng trưởng (GH Deficiency)
  → Hội chứng Turner

• DỰ BÁO chiều cao trưởng thành

• Hỗ trợ chỉnh hình xương & chỉnh nha
```

**KHUNG NỔI BẬT (highlight box):**
```
⚠️ THÁCH THỨC HIỆN TẠI

Bác sĩ phải so sánh THỦ CÔNG ảnh X-quang với Atlas mẫu
→ Mất 15–30 phút mỗi ca
→ Phụ thuộc kinh nghiệm chủ quan
→ Sai lệch giữa các bác sĩ (Inter-observer Variability)
```

**🎙️ Script thuyết trình (60 giây):**
> "Tuổi xương là một khái niệm y khoa dùng để đo mức trưởng thành sinh học của hệ xương ở trẻ em. Nó khác với tuổi tính theo ngày sinh — ví dụ một em bé 10 tuổi theo lịch nhưng tuổi xương có thể chỉ 8 tuổi, tức là xương phát triển chậm hơn bình thường. Hiện tại, bác sĩ nhi khoa phải so sánh thủ công ảnh X-quang bàn tay trái của trẻ với bộ Atlas mẫu từ năm 1959 — quá trình này mất 15 đến 30 phút và kết quả phụ thuộc vào kinh nghiệm chủ quan. Đề tài của nhóm nhằm tự động hóa quá trình này bằng trí tuệ nhân tạo."

---

### 📄 SLIDE 4 — ĐIỂM SÁNG TẠO: REGRESSION VS CLASSIFICATION

**TIÊU ĐỀ:** `ĐIỂM KHÁC BIỆT: BÀI TOÁN HỒI QUY (REGRESSION)`

**BẢNG SO SÁNH:**

```
┌──────────────────────────────────────────────────────────────────┐
│                 CLASSIFICATION (Đa số nhóm)                      │
├──────────────────────────────────────────────────────────────────┤
│  Input: Ảnh X-quang phổi                                        │
│  Output: Viêm phổi? CÓ / KHÔNG (nhãn rời rạc)                  │
│  Loss: Cross-Entropy                                             │
│  Metric: Accuracy, F1-Score                                      │
│  Hạn chế: Quá phổ biến, ít sáng tạo                            │
└──────────────────────────────────────────────────────────────────┘

                          VS

┌──────────────────────────────────────────────────────────────────┐
│              ⭐ REGRESSION (Đề tài này) ⭐                       │
├──────────────────────────────────────────────────────────────────┤
│  Input: Ảnh X-quang BÀN TAY + Giới tính                         │
│  Output: Tuổi xương = 132.5 THÁNG (giá trị liên tục)           │
│  Loss: Smooth L1 (Huber Loss)                                    │
│  Metric: MAE (Mean Absolute Error) theo tháng                    │
│  Ưu điểm: Độc đáo, đa phương thức, chuẩn lâm sàng             │
└──────────────────────────────────────────────────────────────────┘
```

**TẠI SAO X-QUANG BÀN TAY TRÁI?**
```
🖐️ Bàn tay trái có:
   • 27 xương với nhiều trung tâm cốt hóa độc lập
   • 8 xương cổ tay (Carpals) xuất hiện tuần tự 0–10 tuổi
   • 14 xương đốt ngón với sụn tiếp hợp (Epiphyseal Plates)
   • Đầu dưới xương Quay & Trụ (Distal Radius/Ulna)
   → Chuẩn y tế quốc tế | Liều phơi nhiễm tia X cực thấp
```

**🎙️ Script thuyết trình (60 giây):**
> "Điểm khác biệt cốt lõi của đề tài này so với đa số các nhóm khác: chúng em KHÔNG làm bài toán phân loại thông thường kiểu 'có bệnh hay không'. Thay vào đó, đây là bài toán Hồi quy — dự đoán một giá trị liên tục chính xác đến từng tháng tuổi. Ví dụ, mô hình sẽ dự đoán 'em bé này có tuổi xương bằng 132.5 tháng', không phải đơn giản là 'bình thường hay bất thường'. Ngoài ra, chúng em chọn ảnh X-quang bàn tay thay vì phổi — vì bàn tay chứa tới 27 xương với nhiều trung tâm cốt hóa, là vùng giải phẫu lý tưởng nhất để đánh giá tuổi xương theo chuẩn y tế quốc tế."

---

## ═══════════════════════════════════════════
## PHẦN B: PHÂN TÍCH SÂU DATASET (Slide 5–8)
## ═══════════════════════════════════════════

---

### 📄 SLIDE 5 — TỔNG QUAN DATASET RSNA

**TIÊU ĐỀ:** `BỘ DỮ LIỆU: RSNA PEDIATRIC BONE AGE`

**KHUNG THÔNG TIN CHÍNH:**
```
📦 RSNA Pediatric Bone Age Challenge
    Nguồn: Radiological Society of North America (2017)
    Nền tảng: Kaggle (Public Dataset)

╔═══════════════════════════════════════════════════════╗
║                                                       ║
║   📊 TỔNG QUAN SỐ LIỆU                              ║
║                                                       ║
║   Tổng số ảnh:        14,236 ảnh                     ║
║   ├── Training Set:   12,611 ảnh (có label)          ║
║   ├── Validation Set:  1,425 ảnh                     ║
║   └── Test Set:          200 ảnh                     ║
║                                                       ║
║   Định dạng ảnh:      PNG (mức xám)                  ║
║   Nội dung:           X-quang bàn tay trái (PA view) ║
║   Kích thước ảnh:     Không đồng nhất                ║
║                       (cần Resize về kích thước cố định)║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
```

**CẤU TRÚC DỮ LIỆU CSV:**
```
┌────────────────────────────────────────────────────────┐
│  boneage-training-dataset.csv                          │
├──────────┬────────────┬────────────────────────────────┤
│  Trường  │  Kiểu      │  Mô tả                        │
├──────────┼────────────┼────────────────────────────────┤
│  id      │  Integer   │  Mã ảnh (→ tên file {id}.png) │
│  boneage │  Integer   │  Tuổi xương (đơn vị: THÁNG)   │
│          │            │  Phạm vi: 1 → 228 tháng       │
│  male    │  Boolean   │  True = Nam, False = Nữ        │
└──────────┴────────────┴────────────────────────────────┘

Ví dụ:
│  id   │ boneage │  male │
│ 1377  │   180   │ False │  → Bé gái, tuổi xương 15 năm
│ 1378  │    36   │  True │  → Bé trai, tuổi xương 3 năm
│ 1379  │   132   │  True │  → Bé trai, tuổi xương 11 năm
```

**🎙️ Script thuyết trình (45 giây):**
> "Chúng em sử dụng bộ dữ liệu chuẩn RSNA Pediatric Bone Age từ Kaggle — đây là dataset được Hiệp hội X-quang Bắc Mỹ tổ chức cuộc thi vào năm 2017. Bộ dữ liệu gồm hơn 12,600 ảnh X-quang bàn tay trái đã được dán nhãn tuổi xương chính xác đến từng tháng. Mỗi ảnh đi kèm 2 thông tin quan trọng: tuổi xương tính bằng tháng — từ 1 đến 228 tháng — và giới tính sinh học của trẻ."

---

### 📄 SLIDE 6 — PHÂN TÍCH HISTOGRAM TUỔI XƯƠNG (★ Slide trọng điểm)

**TIÊU ĐỀ:** `PHÂN TÍCH PHÂN BỐ DỮ LIỆU — HISTOGRAM TUỔI XƯƠNG`

**MÔ TẢ BIỂU ĐỒ 1 — Histogram tổng thể:**
```
📊 HISTOGRAM PHÂN BỐ TUỔI XƯƠNG (12,611 mẫu)

 Số lượng
 ảnh
  900 ┤
  800 ┤                          ████
  700 ┤                    ████ █████ ████
  600 ┤              ████ █████ █████ █████ ████
  500 ┤         ████ █████ █████ █████ █████ █████
  400 ┤    ████ █████ █████ █████ █████ █████ █████
  300 ┤████ █████ █████ █████ █████ █████ █████ ████
  200 ┤████ █████ █████ █████ █████ █████ █████ █████ ████
  100 ┤████ █████ █████ █████ █████ █████ █████ █████ █████ ██
    0 ┼────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────
      0   24   48   72   96  120  144  168  192  216  228
                    Tuổi xương (tháng)
      │ 0-2y │ 2-4y │ 4-6y │ 6-8y │8-10y│10-12│12-14│14-16│16-19│
```

**NHẬN XÉT PHÂN TÍCH (text trên slide):**
```
📌 NHẬN XÉT THỐNG KÊ:

1. Phân bố GẦN CHUẨN (Normal-like distribution)
   → Đỉnh tập trung ở khoảng 100–160 tháng (8–13 tuổi)
   → Đây là giai đoạn dậy thì — nhu cầu đánh giá lâm sàng CAO NHẤT

2. Đuôi TRÁI thưa (trẻ < 24 tháng):
   → Ít mẫu sơ sinh → Mô hình có thể DỰ ĐOÁN KÉM ở nhóm này
   → Nguyên nhân y khoa: trẻ sơ sinh ít khi cần chụp X-quang bàn tay

3. Đuôi PHẢI thưa (trẻ > 200 tháng):
   → Trẻ lớn gần trưởng thành → sụn tiếp hợp đã đóng kín
   → Ít biến đổi để mô hình học → Thách thức kỹ thuật

4. Dải giá trị: 1 → 228 tháng (≈ 0.08 → 19 tuổi)
   → Bài toán Regression: dự đoán giá trị LIÊN TỤC trong dải rộng
```

**🎨 Gợi ý thiết kế Canva:**
- Sử dụng biểu đồ histogram thực tế (vẽ bằng Matplotlib, export PNG, chèn vào Canva)
- HOẶC dùng biểu đồ mẫu của Canva với 19 thanh bar, gắn nhãn trục rõ ràng
- Phần nhận xét bên cạnh biểu đồ, đánh số 1-2-3-4, dùng icon 📌 🔍

**🎙️ Script thuyết trình (90 giây — slide QUAN TRỌNG):**
> "Đây là biểu đồ phân bố tuổi xương của toàn bộ 12,611 mẫu trong tập huấn luyện. Trục X là tuổi xương tính bằng tháng, trục Y là số lượng ảnh. 
> 
> Nhóm rút ra 4 nhận xét quan trọng: Thứ nhất, phân bố gần dạng chuẩn, tập trung nhiều nhất ở giai đoạn 8 đến 13 tuổi — đúng với thực tế lâm sàng vì đây là giai đoạn dậy thì, nhu cầu đánh giá tuổi xương cao nhất. 
> 
> Thứ hai, đuôi trái rất thưa — tức là có rất ít ảnh trẻ sơ sinh dưới 2 tuổi. Điều này sẽ là thách thức cho mô hình vì thiếu dữ liệu ở nhóm tuổi này. 
> 
> Thứ ba, dải giá trị rất rộng từ 1 đến 228 tháng — đòi hỏi mô hình Regression phải dự đoán chính xác trên toàn bộ dải, không chỉ ở vùng trung tâm. 
> 
> Thứ tư, phân bố này cho phép chúng em áp dụng chiến lược Stratified Split khi chia dữ liệu để đảm bảo mỗi tập con đều đại diện đầy đủ các lứa tuổi."

---

### 📄 SLIDE 7 — PHÂN TÍCH THEO GIỚI TÍNH (★ Slide trọng điểm)

**TIÊU ĐỀ:** `PHÂN BỐ DỮ LIỆU THEO GIỚI TÍNH & ẢNH HƯỞNG SINH HỌC`

**BIỂU ĐỒ 2 — Pie Chart + Histogram chồng:**
```
┌─────────────────────────┐    ┌──────────────────────────────────┐
│   TỶ LỆ GIỚI TÍNH       │    │  HISTOGRAM CHỒNG THEO GIỚI TÍNH   │
│                          │    │                                    │
│      ┌──────────┐        │    │  ▓▓▓ = Nam (Male)                 │
│     /   54.2%    \       │    │  ░░░ = Nữ (Female)                │
│    │   NAM (Male) │      │    │                                    │
│     \____________/       │    │  Số    ▓▓▓░░░                     │
│     │  45.8%     │       │    │  ảnh ▓▓▓▓░░░░                     │
│     │  NỮ        │       │    │      ▓▓▓▓▓░░░░░                   │
│     │ (Female)   │       │    │      ▓▓▓▓▓▓░░░░░░                 │
│     └────────────┘       │    │      ▓▓▓▓▓▓▓░░░░░░░               │
│                          │    │      ──────────────────→           │
│  Nam: ~6,833 ảnh         │    │         Tuổi xương (tháng)        │
│  Nữ:  ~5,778 ảnh         │    │                                    │
│  → Tỷ lệ CÂN BẰNG TỐT  │    │  → Nữ trưởng thành SỚMHƠN Nam    │
└─────────────────────────┘    └──────────────────────────────────┘
```

**PHÂN TÍCH SINH HỌC (text nổi bật):**
```
🧬 TẠI SAO GIỚI TÍNH LÀ BIẾN BẮT BUỘC?

Sự khác biệt sinh học trong quá trình CỐT HÓA XƯƠNG:

┌───────────────────────────────────────────────────┐
│                                                   │
│  👧 BÉ GÁI:                                      │
│  • Bắt đầu dậy thì: 8–13 tuổi                   │
│  • Hoàn thành cốt hóa: ~16–17 tuổi              │
│  • Xương cổ tay đóng kín SỚM HƠN 1.5–2 năm     │
│                                                   │
│  👦 BÉ TRAI:                                     │
│  • Bắt đầu dậy thì: 9–14 tuổi                   │
│  • Hoàn thành cốt hóa: ~18–19 tuổi              │
│  • Cùng mức cốt hóa → tuổi xương CAO HƠN bé gái │
│                                                   │
│  ⚡ KẾT LUẬN:                                     │
│  → Cùng 1 ảnh X-quang giống nhau nhưng           │
│    tuổi xương bé TRAI ≠ bé GÁI                   │
│  → Nếu BỎ biến giới tính → sai số TĂNG 2–3 tháng│
│                                                   │
└───────────────────────────────────────────────────┘
```

**🎙️ Script thuyết trình (75 giây):**
> "Tiếp theo, nhóm phân tích phân bố theo giới tính. Dataset có khoảng 54% Nam và 46% Nữ — một tỷ lệ khá cân bằng, thuận lợi cho việc huấn luyện mô hình không bị thiên lệch.
> 
> Nhưng quan trọng hơn là sự khác biệt SINH HỌC: bé gái trưởng thành xương sớm hơn bé trai từ 1.5 đến 2 năm, đặc biệt ở giai đoạn dậy thì. Điều này có nghĩa là: cùng một ảnh X-quang có cấu trúc xương giống hệt nhau, tuổi xương của bé trai sẽ khác bé gái. 
> 
> Đây chính là lý do nhóm PHẢI đưa giới tính vào làm biến đầu vào phụ cho mô hình — nếu bỏ qua, sai số sẽ tăng từ 2 đến 3 tháng. Nhóm sẽ chứng minh điều này bằng thực nghiệm Ablation Study: so sánh mô hình CÓ và KHÔNG CÓ biến giới tính."

---

### 📄 SLIDE 8 — MẪU ẢNH X-QUANG & ĐẶC THÙ TÍN HIỆU

**TIÊU ĐỀ:** `ĐẶC THÙ ẢNH X-QUANG BÀN TAY — TÍN HIỆU & THÁCH THỨC`

**GRID 3×2 ẢNH MẪU (mô tả để chèn vào Canva):**
```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│   Trẻ 2 tuổi          Trẻ 8 tuổi          Trẻ 16 tuổi       │
│   ┌──────────┐        ┌──────────┐        ┌──────────┐       │
│   │ Xương cổ  │        │ Xương cổ  │        │ Xương cổ  │      │
│   │ tay: CHƯA │        │ tay: ĐÃ   │        │ tay: ĐÃ   │      │
│   │ XUẤT HIỆN │        │ XUẤT HIỆN │        │ KHÉP KÍN  │      │
│   │           │        │ 6-7/8 xương│       │ 8/8 xương │      │
│   │ Sụn tiếp  │        │           │        │           │      │
│   │ hợp: RẤT  │        │ Sụn tiếp  │        │ Sụn tiếp  │      │
│   │ RỘNG      │        │ hợp: THU  │        │ hợp: ĐÃ   │      │
│   │           │        │ HẸP DẦN   │        │ ĐÓNG KÍN  │      │
│   └──────────┘        └──────────┘        └──────────┘       │
│                                                               │
│   → Ít thông tin       → Nhiều thông tin    → Ít biến đổi    │
│     để phân biệt         nhất để phân tích     còn lại        │
└───────────────────────────────────────────────────────────────┘
```

**ĐẶC THÙ KỸ THUẬT CỦA ẢNH X-QUANG:**
```
📐 BIỂU DIỄN TOÁN HỌC:
   Ảnh X-quang = Ma trận mức xám 2D: X ∈ ℝ^(H × W)
   Giá trị pixel: I(x,y) ∈ [0, 255]

⚡ VẬT LÝ TIA X:
   • Xương (đặc, cản quang cao) → TRẮNG sáng
   • Mô mềm (cản quang thấp)  → XÁM
   • Không khí / Nền           → ĐEN

⚠️ THÁCH THỨC KỸ THUẬT:
   1. Độ tương phản THẤP giữa sụn tiếp hợp & mô mềm
   2. Kích thước ảnh KHÔNG ĐỒNG NHẤT giữa các máy chụp
   3. Nhiễu lâm sàng: chữ L/R, thước kim loại ở góc ảnh
   4. Dải động (Dynamic Range) khác nhau giữa các bệnh viện
```

**🎙️ Script thuyết trình (60 giây):**
> "Đây là 3 ảnh X-quang mẫu ở 3 độ tuổi khác nhau. Ở trẻ 2 tuổi, các xương cổ tay gần như chưa xuất hiện và khe sụn tiếp hợp rất rộng. Đến 8 tuổi, hầu hết xương cổ tay đã xuất hiện và sụn tiếp hợp bắt đầu thu hẹp. Ở 16 tuổi, xương cổ tay đã khép kín hoàn toàn và sụn tiếp hợp gần như đóng kín — đánh dấu sự kết thúc tăng trưởng chiều cao.
> 
> Về mặt kỹ thuật, ảnh X-quang được biểu diễn dưới dạng ma trận mức xám 2 chiều. Thách thức lớn nhất là độ tương phản giữa sụn tiếp hợp — vùng quan trọng nhất — và mô mềm xung quanh rất thấp, đòi hỏi phải tiền xử lý cẩn thận."

---

## ═══════════════════════════════════════════
## PHẦN C: CƠ SỞ LÝ THUYẾT & PHƯƠNG PHÁP (Slide 9–15)
## ═══════════════════════════════════════════

---

### 📄 SLIDE 9 — CHUẨN Y KHOA: GREULICH-PYLE & TANNER-WHITEHOUSE

**TIÊU ĐỀ:** `CƠ SỞ Y KHOA: 2 PHƯƠNG PHÁP ĐÁNH GIÁ CHUẨN`

**BẢNG SO SÁNH 2 CỘT:**
```
┌──────────────────────────┐    ┌──────────────────────────┐
│  GREULICH-PYLE (GP)       │    │  TANNER-WHITEHOUSE (TW3)  │
│  Atlas Matching Method    │    │  Point Scoring Method     │
├──────────────────────────┤    ├──────────────────────────┤
│                           │    │                           │
│  📖 So sánh TOÀN BỘ      │    │  📊 Chấm điểm 20 VÙNG   │
│     bàn tay với Atlas     │    │     xương CỤ THỂ         │
│     mẫu chuẩn            │    │                           │
│                           │    │  13 xương dài (ngón tay,  │
│  ✅ Nhanh (3–5 phút)     │    │  bàn tay, quay, trụ)     │
│  ❌ Chủ quan              │    │  + 7 xương cổ tay         │
│  ❌ Inter-observer        │    │                           │
│     variability CAO       │    │  ✅ Khách quan            │
│                           │    │  ✅ Tái lập cao           │
│  → Phổ biến nhất trong   │    │  ❌ Chậm (15–30 phút)    │
│    thực hành lâm sàng    │    │                           │
│                           │    │  → Ưu tiên trong nghiên  │
│                           │    │    cứu & ca phức tạp     │
└──────────────────────────┘    └──────────────────────────┘
```

**LIÊN HỆ VỚI DEEP LEARNING:**
```
🤖 MẠNG CNN HỌC ĐƯỢC GÌ?

Tầng NÔNG (layers đầu):
  → Học đặc trưng TỔNG THỂ (bàn tay to/nhỏ, tỷ lệ)
  → ≈ Phương pháp Greulich-Pyle (nhìn tổng quan)

Tầng SÂU (layers cuối):
  → Học đặc trưng VI MÔ (mức độ khép kín từng khe sụn)
  → ≈ Phương pháp Tanner-Whitehouse (phân tích chi tiết)

→ CNN tự động KẾT HỢP cả 2 phương pháp!
```

---

### 📄 SLIDE 10 — PIPELINE XỬ LÝ ẢNH CỔ ĐIỂN (Classical CV)

**TIÊU ĐỀ:** `PIPELINE TIỀN XỬ LÝ ẢNH — 5 MODULE XỬ LÝ CỔ ĐIỂN`

**SƠ ĐỒ PIPELINE (dạng mũi tên ngang):**
```
  Ảnh gốc        Module 1         Module 2         Module 3         Module 4         Module 5
  (đa kích    ──▶  CLAHE       ──▶ Gaussian    ──▶ Otsu +       ──▶ Contour     ──▶ Resize &
   thước)        Tăng tương       Blur            Morphology       Crop ROI        Normalize
                 phản cục bộ     Khử nhiễu       Tạo Mask         Định vị         512×512
                                                 bàn tay          bàn tay
```

**CHI TIẾT MODULE 1 — CLAHE:**
```
📌 CLAHE (Contrast Limited Adaptive Histogram Equalization)

Vấn đề:  Ảnh X-quang có độ tương phản THẤP
          → Khó thấy khe sụn tiếp hợp mỏng

Giải pháp: CLAHE xử lý CỤC BỘ thay vì toàn cục
          → Chia ảnh thành lưới 8×8 = 64 tiles
          → Tính Histogram Equalization riêng từng tile
          → Clip Limit = 3.0 (giới hạn tăng tương phản)
          → Nội suy song tuyến để ghép các tile

Kết quả: ✅ Khe sụn tiếp hợp RÕ NÉT
         ✅ Xương cổ tay HIỆN RÕ
         ✅ Vùng mô mềm KHÔNG bị cháy sáng
```

**CHI TIẾT MODULE 3 — Otsu + Morphology:**
```
📌 TÁCH NỀN & ĐỊNH VỊ BÀN TAY

Bước 1: Otsu's Thresholding (Phân ngưỡng tự động)
  → Tối ưu hóa phương sai liên lớp:
    σ²_B(t) = ω₀(t)·ω₁(t)·[μ₀(t) - μ₁(t)]²
  → Tách: Nền đen (0) / Bàn tay sáng (255)

Bước 2: Morphological Opening
  → Erosion → Dilation (kernel 5×5)
  → Xóa nhiễu nhỏ: chữ L/R, thước kim loại

Bước 3: Largest Contour → Bounding Box → Crop
  → Tìm đường bao lớn nhất = bàn tay
  → Cắt chính xác vùng bàn tay (ROI)

MỤC ĐÍCH: Loại bỏ HOÀN TOÀN nhiễu nền
          → Ngăn mô hình bị "Shortcut Learning"
```

**🎙️ Script thuyết trình (90 giây):**
> "Trước khi đưa ảnh vào mạng Deep Learning, nhóm thiết kế pipeline gồm 5 bước xử lý ảnh cổ điển. Bước quan trọng nhất là CLAHE — viết tắt của Contrast Limited Adaptive Histogram Equalization. Khác với cân bằng histogram thông thường xử lý toàn bộ ảnh một lần, CLAHE chia ảnh thành lưới 8 nhân 8 bằng 64 ô nhỏ, tính histogram cục bộ cho từng ô. Kết quả là các khe sụn tiếp hợp — vùng quan trọng nhất để đánh giá tuổi xương — được hiện rõ hơn đáng kể.
> 
> Bước thứ hai là dùng phân ngưỡng Otsu kết hợp phép biến đổi hình thái học để tạo mặt nạ nhị phân tách bàn tay khỏi nền đen, đồng thời loại bỏ các ký tự L-R và thước kim loại ở góc ảnh. Việc này CỰC KỲ quan trọng vì nếu không loại bỏ, mô hình có thể học tắt — nhìn vào chữ thay vì xương."

---

### 📄 SLIDE 11 — TOÁN TỐI ƯU: THIẾT KẾ HÀM MẤT MÁT (Loss Functions)

**TIÊU ĐỀ:** `LỰA CHỌN HÀM MẤT MÁT CHO BÀI TOÁN REGRESSION`

**BẢNG SO SÁNH 3 HÀM LOSS:**
```
┌─────────────────────────────────────────────────────────────┐
│  L2 Loss (MSE)                                              │
│  L = (1/N) Σ(yᵢ - ŷᵢ)²                                    │
│                                                             │
│  ✅ Đạo hàm liên tục, mượt tại mọi điểm                   │
│  ❌ Phạt BẬC HAI với sai số lớn                             │
│  ❌ CỰC KỲ nhạy cảm với outlier (ca dị tật, nhãn sai)     │
│  → Baseline so sánh, KHÔNG phải lựa chọn tối ưu            │
├─────────────────────────────────────────────────────────────┤
│  L1 Loss (MAE)                                              │
│  L = (1/N) Σ|yᵢ - ŷᵢ|                                     │
│                                                             │
│  ✅ BỀN VỮNG với outlier (đạo hàm = hằng số ±1)           │
│  ❌ Đạo hàm KHÔNG LIÊN TỤC tại điểm 0                     │
│  → Tốt nhưng không tối ưu                                  │
├─────────────────────────────────────────────────────────────┤
│  ⭐ Smooth L1 / Huber Loss (LỰA CHỌN CHÍNH)               │
│                                                             │
│  L_δ = { ½(y-ŷ)²            nếu |y-ŷ| ≤ δ                │
│        { δ|y-ŷ| - ½δ²       nếu |y-ŷ| > δ                │
│                                                             │
│  ✅ Kết hợp ưu điểm CẢ HAI:                                │
│     • Mượt như L2 khi sai số nhỏ (quanh 0)                 │
│     • Robust như L1 khi sai số lớn (outlier)               │
│  ✅ δ = 1.0: giá trị mặc định tối ưu                       │
│  → LỰA CHỌN CHÍNH cho đề tài                              │
└─────────────────────────────────────────────────────────────┘
```

**METRIC ĐÁNH GIÁ CHÍNH:**
```
📏 MAE (Mean Absolute Error) — tính theo THÁNG

   MAE = (1/N) Σ |tuổi_thực - tuổi_dự_đoán|

   Benchmark:
   ┌────────────────────────────────────────┐
   │  < 6 tháng    → Tốt (ngang bác sĩ)   │
   │  < 8 tháng    → Chấp nhận được        │
   │  > 12 tháng   → Chưa đạt yêu cầu     │
   │                                        │
   │  RSNA 2017 Winner: MAE ≈ 4.2 tháng    │
   │  Mục tiêu nhóm:    MAE < 6 tháng      │
   └────────────────────────────────────────┘
```

---

### 📄 SLIDE 12 — KIẾN TRÚC MẠNG: CNN BACKBONE (★ Slide trọng điểm)

**TIÊU ĐỀ:** `LỰA CHỌN BACKBONE: RESNET-50 VS EFFICIENTNET-B4`

**BẢNG SO SÁNH KỸ THUẬT:**
```
┌─────────────────────────┬────────────────┬─────────────────┐
│  Thuộc tính              │  ResNet-50     │ EfficientNet-B4 │
│                          │  (BASELINE)    │ (NÂNG CAO)      │
├─────────────────────────┼────────────────┼─────────────────┤
│  Số tầng                 │  50            │  ~350+          │
│  Tham số                 │  25.6M         │  19.3M ⭐       │
│  FLOPs                   │  4.1G          │  4.2G           │
│  Feature vector output   │  2048-d        │  1792-d         │
│  Input khuyến nghị       │  224×224       │  380×380        │
│  Pre-trained             │  ImageNet 1K   │  ImageNet 1K    │
│  MAE dự kiến             │  ~7-8 tháng    │  ~5-6 tháng ⭐  │
│  VRAM cần (batch=16)     │  ~6 GB         │  ~10 GB         │
├─────────────────────────┼────────────────┼─────────────────┤
│  Vai trò trong dự án     │  Experiment    │  Experiment     │
│                          │  E0, E1, E2    │  E3 (Final)     │
└─────────────────────────┴────────────────┴─────────────────┘
```

**RESNET — RESIDUAL BLOCK:**
```
📐 CƠ CHẾ SKIP CONNECTION (Residual Learning)

   Input x ──┬──── Conv → BN → ReLU → Conv → BN ──┬── + ──→ ReLU → Output y
             │                                       │
             └──────── SKIP CONNECTION ──────────────┘

   y = F(x) + x

   Gradient: ∂y/∂x = ∂F/∂x + 1
                              ↑
                     Luôn có +1 → Gradient KHÔNG bao giờ triệt tiêu
                     → Cho phép mạng cực sâu (50, 101, 152 tầng)
```

**EFFICIENTNET — COMPOUND SCALING:**
```
📐 CƠ CHẾ MỞ RỘNG ĐỒNG THỜI (Compound Scaling)

   depth  = α^φ    (tăng số tầng)
   width  = β^φ    (tăng số kênh)
   resolution = γ^φ (tăng kích thước ảnh)

   Ràng buộc: α · β² · γ² ≈ 2

   → Scale đồng thời 3 chiều → Hiệu quả hơn việc
     chỉ tăng 1 chiều (như VGG chỉ tăng depth)
```

---

### 📄 SLIDE 13 — KIẾN TRÚC TỔNG THỂ: MULTIMODAL FUSION (★ Slide trọng điểm)

**TIÊU ĐỀ:** `KIẾN TRÚC ĐỀ XUẤT: MẠNG ĐA PHƯƠNG THỨC (MULTIMODAL FUSION)`

**SƠ ĐỒ KIẾN TRÚC (blueprint chính của dự án):**
```
    ┌────────────────────────────────────────────────────────────────┐
    │              BONE AGE MULTIMODAL REGRESSION MODEL              │
    └───────────────────────────┬────────────────────────────────────┘
                                │
         ┌──────────────────────┴─────────────────────┐
         │                                            │
    IMAGE BRANCH                               GENDER BRANCH
    ┌──────────────┐                          ┌──────────────┐
    │ Input:       │                          │ Input:       │
    │ X-ray Image  │                          │ Gender       │
    │ (B, 3, H, W) │                          │ (B, 1)       │
    └──────┬───────┘                          │  0 = Nữ      │
           │                                  │  1 = Nam      │
    ┌──────▼───────┐                          └──────┬───────┘
    │ CNN Backbone  │                                 │
    │ ResNet-50 /   │                          ┌──────▼───────┐
    │ EfficientNet  │                          │ Linear(1→32) │
    │ [Pre-trained  │                          │ + BatchNorm  │
    │  ImageNet]    │                          │ + ReLU       │
    └──────┬───────┘                          │ Linear(32→32)│
           │                                  │ + ReLU       │
    ┌──────▼───────┐                          └──────┬───────┘
    │ Global Avg   │                                 │
    │ Pooling      │                          Gender Vector
    └──────┬───────┘                          (B, 32)
           │                                         │
    Image Vector                                     │
    (B, 2048) or (B, 1792)                           │
           │                                         │
           └──────────────┬──────────────────────────┘
                          │
                   ┌──────▼───────┐
                   │ CONCATENATION │
                   │ (B, 2080)    │  ← 2048 + 32
                   └──────┬───────┘
                          │
                   ┌──────▼───────┐
                   │ REGRESSION   │
                   │ HEAD         │
                   │              │
                   │ FC(2080→1024)│
                   │ + BN + ReLU  │
                   │ + Dropout 0.3│
                   │              │
                   │ FC(1024→512) │
                   │ + BN + ReLU  │
                   │ + Dropout 0.3│
                   │              │
                   │ FC(512→1)    │
                   │ (Linear, NO  │
                   │  activation) │
                   └──────┬───────┘
                          │
                     Output: ŷ
                  Predicted Bone Age
                 (1 giá trị vô hướng,
                  đơn vị: tháng)
```

**GIẢI THÍCH CHIẾN LƯỢC LATE FUSION:**
```
❓ TẠI SAO LATE FUSION?

• Mỗi modality (ảnh, giới tính) được xử lý RIÊNG BIỆT
  bởi encoder chuyên biệt

• Feature vectors được GHÉP NỐI (Concatenation)
  tại tầng Fully Connected

• ƯU ĐIỂM:
  ✅ Đơn giản, dễ triển khai trong 4 tuần
  ✅ Đã được chứng minh hiệu quả (MAE < 5 tháng)
  ✅ Dễ ablation: bỏ gender branch → đo impact

• Tại sao Gender cần EMBEDDING 32-d thay vì 0/1?
  → Giá trị 0/1 = 1 chiều, quá nhỏ so với 2048 chiều
    của image feature → bị "lấn át"
  → Embedding 32-d cho phép mạng tự học biểu diễn
    PHI TUYẾN phong phú hơn cho ảnh hưởng của giới tính
```

---

### 📄 SLIDE 14 — CHIẾN LƯỢC HUẤN LUYỆN (Training Strategy)

**TIÊU ĐỀ:** `CHIẾN LƯỢC HUẤN LUYỆN: TRANSFER LEARNING 2 GIAI ĐOẠN`

**SƠ ĐỒ 2 GIAI ĐOẠN:**
```
╔══════════════════════════════════════════════════════════════╗
║  GIAI ĐOẠN 1: FREEZE BACKBONE (5–10 epochs)                ║
║                                                              ║
║  ❄️ CNN Backbone: ĐÓNG BĂNG (không cập nhật trọng số)       ║
║  🔥 Gender Branch + Regression Head: HUẤN LUYỆN             ║
║  📌 Learning Rate: 1×10⁻³ (cao)                             ║
║  📌 Mục đích: Hội tụ NHANH phần Regression Head             ║
╠══════════════════════════════════════════════════════════════╣
║  GIAI ĐOẠN 2: UNFREEZE ALL (20–30 epochs)                   ║
║                                                              ║
║  🔥 TOÀN BỘ mạng: HUẤN LUYỆN end-to-end                    ║
║  📌 Learning Rate: 1×10⁻⁴ (thấp hơn 10×)                   ║
║  📌 LR Scheduler: CosineAnnealingLR                         ║
║  📌 Mục đích: Fine-tune backbone cho đặc trưng X-quang      ║
║  📌 Early Stopping: patience = 7 (theo val MAE)             ║
╚══════════════════════════════════════════════════════════════╝
```

**CẤU HÌNH HUẤN LUYỆN (phù hợp RTX 3050 + Colab):**
```
┌──────────────────────────────────────────────┐
│  TRAINING CONFIGURATION                       │
├──────────────┬───────────────┬────────────────┤
│  Tham số      │ RTX 3050 (4GB)│ Colab T4 (16GB)│
├──────────────┼───────────────┼────────────────┤
│  Image Size   │ 224 × 224    │ 380 × 380      │
│  Batch Size   │ 8            │ 16             │
│  AMP (FP16)   │ BẮT BUỘC    │ BẮT BUỘC       │
│  Optimizer    │ AdamW        │ AdamW          │
│  Weight Decay │ 1×10⁻⁴      │ 1×10⁻⁴        │
│  Loss         │ Smooth L1    │ Smooth L1      │
│  Grad Clip    │ max_norm=1.0 │ max_norm=1.0   │
├──────────────┼───────────────┼────────────────┤
│  Vai trò      │ Debug/Test   │ TRAIN CHÍNH    │
└──────────────┴───────────────┴────────────────┘
```

**DATA AUGMENTATION AN TOÀN CHO X-QUANG:**
```
   ✅ CHO PHÉP:                    ❌ KHÔNG CHO PHÉP:
   • Xoay nhẹ ±10°               • ColorJitter mạnh
   • Flip ngang                    • Random Crop mạnh
   • Dịch chuyển ±5%             • Vertical Flip
   • Sáng/tương phản ±10%        • Elastic Distortion
   
   → Tôn trọng tính toàn vẹn GIẢI PHẪU
```

---

### 📄 SLIDE 15 — EXPLAINABLE AI: GRAD-CAM

**TIÊU ĐỀ:** `GIẢI THÍCH MÔ HÌNH: GRAD-CAM — MÔ HÌNH NHÌN VÀO ĐÂU?`

**NGUYÊN LÝ TOÁN HỌC:**
```
📐 GRAD-CAM (Gradient-weighted Class Activation Mapping)

Bước 1: Tính trọng số importance cho feature map thứ k:
         αₖ = (1/Z) Σᵢ Σⱼ ∂ŷ/∂Aᵢⱼᵏ
         (Z = số pixel, ŷ = tuổi xương dự đoán)

Bước 2: Tổng hợp có trọng số + ReLU:
         Heatmap = ReLU( Σₖ αₖ · Aᵏ )
         (ReLU: chỉ giữ ảnh hưởng TÍCH CỰC)

Bước 3: Overlay heatmap lên ảnh X-quang gốc

Cho bài toán REGRESSION:
  → Backprop trực tiếp từ output scalar ŷ
  → Không cần one-hot encoding như Classification
```

**TIÊU CHÍ KIỂM CHỨNG Y KHOA:**
```
┌────────────────────────────────────────────────────────┐
│  VÙNG MÀU ĐỎ (Quan trọng nhất):                       │
│                                                        │
│  ✅ ĐÚNG nếu ở:          ❌ SAI nếu ở:                │
│  • Xương cổ tay           • Nền đen/Không khí         │
│    (Carpals) — trẻ nhỏ    • Chữ L/R góc ảnh           │
│  • Sụn tiếp hợp           • Viền máy quét             │
│    (Epiphyses) — trẻ lớn  • Mô mềm bên ngoài         │
│  • Đầu dưới xương Quay    │                            │
│                            │ → "Shortcut Learning"     │
│  → Mô hình ĐÁNG TIN CẬY   │ → Mô hình BỊ LỖI!        │
└────────────────────────────────────────────────────────┘
```

---

## ═══════════════════════════════════════════
## PHẦN D: THIẾT KẾ HỆ THỐNG & KẾ HOẠCH (Slide 16–20)
## ═══════════════════════════════════════════

---

### 📄 SLIDE 16 — THIẾT KẾ ABLATION STUDY

**TIÊU ĐỀ:** `THIẾT KẾ THÍ NGHIỆM — ABLATION STUDY 4 KỊCH BẢN`

```
┌──────┬─────────────────────┬────────────┬──────────┬─────────┬──────────┬───────────┐
│  Exp │  Tên                │  Backbone  │ Tiền xử  │ Gender  │  Loss    │ MAE mục   │
│      │                     │            │ lý CV    │ Input   │          │ tiêu      │
├──────┼─────────────────────┼────────────┼──────────┼─────────┼──────────┼───────────┤
│  E0  │  Raw Baseline       │  ResNet-50 │  ❌ Không│  ❌ Không│  MSE     │ ~10-12 th │
│  E1  │  + Classical CV     │  ResNet-50 │  ✅ CLAHE│  ❌ Không│  MSE     │ ~8-9 th   │
│      │                     │            │   + Crop │         │          │           │
│  E2  │  + Gender Fusion    │  ResNet-50 │  ✅ CLAHE│  ✅ Có  │ Smooth L1│ ~6-7 th   │
│      │                     │            │   + Crop │ (Concat)│          │           │
│  E3  │  + EfficientNet ⭐  │ Efficient  │  ✅ CLAHE│  ✅ Có  │ Smooth L1│ ~5-6 th ⭐│
│      │                     │  Net-B4    │   + Crop │ (Concat)│          │           │
└──────┴─────────────────────┴────────────┴──────────┴─────────┴──────────┴───────────┘

MỤC ĐÍCH:
   E0 → E1: Chứng minh TIỀN XỬ LÝ Classical CV có tác dụng
   E1 → E2: Chứng minh GIỚI TÍNH là biến quan trọng
   E2 → E3: Chứng minh BACKBONE tốt hơn cho kết quả tốt hơn
   
   → Mỗi bước thêm 1 thành phần → Đo lường ĐÓNG GÓP từng thành phần
```

---

### 📄 SLIDE 17 — THIẾT KẾ WEB APP (Streamlit)

**TIÊU ĐỀ:** `GIAO DIỆN ỨNG DỤNG: WEB APP ĐÁNH GIÁ TUỔI XƯƠNG`

```
┌──────────────────────────────────────────────────────────────────┐
│                  🦴 BONE AGE ASSESSMENT SYSTEM                   │
├─────────────────────────────┬────────────────────────────────────┤
│                              │                                    │
│   📤 TẢI ẢNH X-QUANG        │   📊 KẾT QUẢ DỰ ĐOÁN             │
│                              │                                    │
│   [  Kéo thả ảnh vào đây  ] │   🦴 Tuổi xương: 132.5 tháng     │
│   (.png, .jpg)               │      (≈ 11 năm 0.5 tháng)        │
│                              │                                    │
│   ⚧ Giới tính:              │   📏 Chênh lệch: ▲ +4.5 tháng    │
│   ○ Nam  ● Nữ               │   🟢 Phát triển BÌNH THƯỜNG       │
│                              │                                    │
│   📅 Tuổi thật: [128] tháng │   ┌──────────────────────────┐    │
│                              │   │    🔥 GRAD-CAM Heatmap    │    │
│   [  🔍 ĐÁNH GIÁ  ]        │   │    (Vùng mô hình tập     │    │
│                              │   │     trung phân tích)     │    │
│                              │   └──────────────────────────┘    │
├──────────────────────────────┴────────────────────────────────────┤
│                                                                    │
│   📈 BIỂU ĐỒ TĂNG TRƯỞNG WHO                                    │
│   ┌────────────────────────────────────────────────────────────┐  │
│   │  Chiều   Z=+2 ─────────────────────────                   │  │
│   │  cao     Z=+1 ─────────────────────────                   │  │
│   │  (cm)    Z= 0 ═══════════●═══════════  ← Bệnh nhi       │  │
│   │          Z=-1 ─────────────────────────                   │  │
│   │          Z=-2 ─────────────────────────                   │  │
│   │          ─────┬──────┬──────┬──────┬─────                 │  │
│   │              2y     5y    10y    15y   18y                 │  │
│   └────────────────────────────────────────────────────────────┘  │
│                                                                    │
│   Cảnh báo: 🟢 Bình thường | 🟡 Theo dõi | 🔴 Cần hội chẩn      │
└────────────────────────────────────────────────────────────────────┘
```

**CÔNG NGHỆ:**
```
• Framework:  Streamlit (Python) — deploy nhanh, native PyTorch
• Biểu đồ:   Plotly (tương tác) / Matplotlib (tĩnh)
• WHO Data:   Bảng tăng trưởng chuẩn WHO (public domain)
• Cache:      @st.cache_resource — load model 1 lần duy nhất
```

---

### 📄 SLIDE 18 — BIỂU ĐỒ WHO & GIẢI THÍCH LÂM SÀNG

**TIÊU ĐỀ:** `TÍCH HỢP BIỂU ĐỒ TĂNG TRƯỞNG CHUẨN WHO`

```
📊 Ý NGHĨA LÂM SÀNG CỦA CHÊNH LỆCH (Δ)

   Δ = Tuổi xương — Tuổi thật

   ┌──────────────────────────────────────────────────┐
   │  |Δ| ≤ 12 tháng                                  │
   │  🟢 BÌNH THƯỜNG                                  │
   │  → Phát triển trong giới hạn sinh lý             │
   ├──────────────────────────────────────────────────┤
   │  Δ > +12 tháng (xương phát triển NHANH)         │
   │  🟡 CẢNH BÁO                                     │
   │  → Nguy cơ: Dậy thì sớm, tăng sinh              │
   │    tuyến thượng thận                              │
   ├──────────────────────────────────────────────────┤
   │  Δ < -12 tháng (xương phát triển CHẬM)          │
   │  🔴 NGUY HIỂM                                    │
   │  → Nguy cơ: Suy giáp, suy hormone GH,           │
   │    suy dinh dưỡng nặng                           │
   │  → Đề nghị hội chẩn nội tiết nhi                 │
   └──────────────────────────────────────────────────┘
```

---

### 📄 SLIDE 19 — KẾ HOẠCH TRIỂN KHAI 4 TUẦN

**TIÊU ĐỀ:** `LỘ TRÌNH TRIỂN KHAI — 4 TUẦN (GANTT CHART)`

```
         Tuần 1              Tuần 2              Tuần 3              Tuần 4
   ┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
   │ 🔍 KHỞI ĐỘNG    │ 🏗️ XÂY DỰNG    │ ⚡ TỐI ƯU      │ 🚀 HOÀN THIỆN  │
   │                  │                  │                  │                  │
   │ SV1:            │ SV1:            │ SV1:            │ SV1:            │
   │ • EDA dataset    │ • Dataset loader│ • Thử Loss      │ • Export ONNX   │
   │ • Pipeline CV    │ • Data augment  │ • Error analysis│ • README & docs │
   │ • 7 biểu đồ     │ • Cache images  │ • Biểu đồ KQ   │ • Kiểm thử      │
   │                  │                  │                  │                  │
   │ SV2:            │ SV2:            │ SV2:            │ SV2:            │
   │ • Research model │ • Train baseline│ • EfficientNet  │ • Web App       │
   │ • Slide GĐ1     │ • ResNet-50+    │ • Grad-CAM      │ • WHO chart     │
   │ • Setup Git     │   Gender fusion │ • Kiểm chứng    │ • Video demo    │
   │                  │                  │   y khoa        │                  │
   ├──────────────────┼──────────────────┼──────────────────┼──────────────────┤
   │ 🏁 M1: EDA Done  │ 🏁 M4: Baseline│ 🏁 M6: Best    │ 🏁 M9: Final   │
   │ 🏁 M2: Pipeline │ 🏁 M5: Multi   │ 🏁 M7: Grad-CAM│    Demo Ready   │
   │ 🏁 M3: Slide    │    modal Done   │    Validated    │                  │
   └──────────────────┴──────────────────┴──────────────────┴──────────────────┘
```

**PHÂN CÔNG VAI TRÒ:**
```
   👤 SV1: DATA & CLASSICAL CV LEAD
      Trọng tâm: Dữ liệu, EDA, Tiền xử lý OpenCV, Error Analysis

   👤 SV2: DEEP LEARNING & DEPLOYMENT LEAD
      Trọng tâm: Kiến trúc mạng, Huấn luyện, Grad-CAM, Web App
```

---

### 📄 SLIDE 20 — KẾT LUẬN & Q&A

**TIÊU ĐỀ:** `KẾT LUẬN & TỔNG KẾT`

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🎯 GIÁ TRỊ CỐT LÕI CỦA ĐỀ TÀI                         ║
║                                                              ║
║   1. Bài toán REGRESSION ĐỘC ĐÁO                           ║
║      → Dự đoán tuổi xương chính xác đến từng THÁNG         ║
║      → Khác biệt hoàn toàn với Classification thông thường  ║
║                                                              ║
║   2. Kết hợp TOÀN DIỆN kiến thức CV                         ║
║      → Classical CV: CLAHE, Otsu, Morphology                ║
║      → Toán Tối ưu: Huber Loss, MAE metric                  ║
║      → Deep Learning: Multimodal CNN Fusion                  ║
║      → Explainable AI: Grad-CAM kiểm chứng y khoa          ║
║                                                              ║
║   3. Sản phẩm ỨNG DỤNG THỰC TẾ                             ║
║      → Web App trực quan hỗ trợ bác sĩ nhi khoa            ║
║      → Biểu đồ tăng trưởng WHO tích hợp                    ║
║      → Giải thích quyết định minh bạch bằng Heatmap        ║
║                                                              ║
║   4. Tính nhân văn                                           ║
║      → Phát hiện SỚM rối loạn nội tiết ở trẻ em            ║
║      → Giảm thời gian & chi phí chẩn đoán                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

      Mục tiêu: MAE < 6 tháng | 4 Ablation Experiments
      Dataset: RSNA 12,611 ảnh | Thời gian: 4 tuần

   ─────────────────────────────────────────────────────
   XIN CẢM ƠN QUÝ THẦY/CÔ ĐÃ LẮNG NGHE!
   Nhóm rất mong nhận được góp ý quý báu.

                   ❓ Q & A SESSION
   ─────────────────────────────────────────────────────
```

**🎙️ Script thuyết trình (45 giây):**
> "Tóm lại, đề tài của nhóm có 4 giá trị cốt lõi: Thứ nhất, đây là bài toán Hồi quy độc đáo — dự đoán tuổi xương chính xác đến từng tháng, khác biệt hoàn toàn với các đề tài Phân loại thông thường. Thứ hai, nhóm kết hợp toàn diện kiến thức Computer Vision từ xử lý ảnh cổ điển đến Deep Learning hiện đại và Explainable AI. Thứ ba, sản phẩm cuối có tính ứng dụng thực tế với giao diện Web App hỗ trợ bác sĩ nhi khoa. Và cuối cùng, đề tài mang tính nhân văn — giúp phát hiện sớm rối loạn nội tiết ở trẻ em. Xin chân thành cảm ơn Quý Thầy Cô. Nhóm rất mong nhận được góp ý!"

---

## PHÂN CHIA THUYẾT TRÌNH

| Phần | Slide | Người trình bày | Thời gian |
|:---|:---:|:---:|:---:|
| **A. Bối cảnh & Đặt bài toán** | 1–4 | SV1 | ~4 phút |
| **B. Phân tích Dataset** | 5–8 | SV1 | ~5 phút |
| **C. Cơ sở Lý thuyết & Phương pháp** | 9–15 | SV2 | ~8 phút |
| **D. Thiết kế Hệ thống & Kế hoạch** | 16–20 | SV2 | ~3 phút |
| **Tổng** | 20 slide | 2 người | **~20 phút** |
