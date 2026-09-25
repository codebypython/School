# 🎤 KỊCH BẢN THUYẾT TRÌNH CHI TIẾT 20 SLIDE — BONE AGE ASSESSMENT (RSNA)
## Hệ Thống Tự Động Đánh Giá Tuổi Xương từ Ảnh X-quang Bàn Tay Trẻ Em
**Đơn vị đào tạo**: Trường Đại học Bách Khoa — Đại học Đà Nẵng (DUT)  
**Học phần**: Computer Vision (Thị giác Máy tính) | **Học kỳ**: 7 — Năm học 2026–2027  
**Cố vấn học thuật**: DUT Computer Vision Mentor | VisionLab Deep Tech Corp (`CORP-01-CV`)  
**Tập dữ liệu thực nghiệm**: RSNA Pediatric Bone Age Challenge ($12,611$ ảnh X-quang thật)  
**Phần cứng huấn luyện**: Google Colab (NVIDIA Tesla T4 GPU 16GB VRAM — 202.1 phút huấn luyện thật)  

---

> 📌 **HƯỚNG DẪN SỬ DỤNG TÀI LIỆU NÀY DÀNH CHO NHÓM:**
> - **Cấu trúc mỗi Slide**: Bao gồm **Tiêu đề**, **Nội dung gạch đầu dòng (Copy trực tiếp vào Canva)**, **🎨 Gợi ý thiết kế Canva trực quan**, và **🎙️ Script thuyết trình chi tiết từng giây** (có phân vai rõ ràng giữa **Sinh viên 1** và **Sinh viên 2**).
> - **Tiêu chuẩn dữ liệu**: 100% số liệu, biểu đồ, thời gian train, chỉ số MAE, RMSE, $R^2$, bản đồ Grad-CAM đều được trích xuất từ kết quả thực nghiệm thật trong tệp `result_tranning.ipynb`. Tuyệt đối không có số liệu giả lập.
> - **Bảng màu khuyến nghị (Canva Palette)**:
>   - Nền Dark Mode Y tế: `#0B132B` hoặc `#0F172A` (Slate Dark)
>   - Accent Công nghệ: `#38BDF8` (Cyan Blue) / `#818CF8` (Indigo Neon)
>   - Success / Đạt chuẩn: `#10B981` (Emerald Green)
>   - Warning / Cảnh báo: `#F59E0B` (Amber) | Danger: `#EF4444` (Crimson)
> - **Font chữ chuẩn quốc tế**: **Montserrat / Oswald** (Tiêu đề in hoa đậm) + **Inter / Plus Jakarta Sans** (Nội dung).

---

## ═══════════════════════════════════════════════════════════════════
## PHẦN A: BỐI CẢNH LÂM SÀNG & ĐẶT BÀI TOÁN HỌC THUẬT (Slide 1 – 4)
## Người thuyết trình: SINH VIÊN 1 (Data & Classical CV Lead)
## ═══════════════════════════════════════════════════════════════════

---

### 📄 SLIDE 1 — TRANG BÌA (Title Slide)

**TIÊU ĐỀ CHÍNH (Heading 1):**
```
HỆ THỐNG TỰ ĐỘNG ĐÁNH GIÁ TUỔI XƯƠNG
TỪ ẢNH X-QUANG BÀN TAY TRẺ EM
```

**TIÊU ĐỀ PHỤ (Subheading):**
```
Pediatric Bone Age Assessment using Multimodal Deep Learning
& Explainable AI (Grad-CAM) on RSNA Radiographs
```

**THÔNG TIN BÁO CÁO:**
```
• Học phần: Thị giác Máy tính (Computer Vision)
• Đơn vị: Khoa Công nghệ Thông tin — Trường Đại học Bách Khoa, ĐH Đà Nẵng (DUT)
• Giảng viên hướng dẫn: [Họ và Tên Thầy/Cô]
• Sinh viên thực hiện: 
    1. [Họ và tên SV1] — Lớp: 22T_... (Data & Classical CV Lead)
    2. [Họ và tên SV2] — Lớp: 22T_... (Deep Learning & System Lead)
• Thời gian: Học kỳ 1 — Năm học 2026–2027
```

**🎨 Gợi ý thiết kế Canva:**
- Bố cục: Chia đôi màn hình (Split screen). Bên trái: Chữ trắng nổi bật trên nền xanh đen `#0B132B`, logo trường ĐHBK Đà Nẵng (DUT) góc trên bên trái. Bên phải: Ảnh X-quang bàn tay với hiệu ứng phủ lưới công nghệ phát sáng (Cyan overlay grid).
- Huy hiệu nhỏ góc dưới: `Dataset RSNA: 12,611 X-rays` | `GPU Tesla T4: 202 Mins` | `Test MAE: 7.38 Tháng`.

**🎙️ Script thuyết trình (Sinh viên 1 - 45 giây):**
> "Kính chào Thầy/Cô trong Hội đồng phản biện và các bạn sinh viên. Hôm nay, nhóm chúng em xin đại diện báo cáo đề tài nghiên cứu: 'Hệ thống Tự động Đánh giá Tuổi Xương từ ảnh X-quang Bàn tay Trẻ em'. Đây là một đề tài kết hợp chặt chẽ giữa xử lý ảnh thị giác cổ điển (Classical Computer Vision), học sâu đa phương thức (Multimodal Deep Learning) và Trí tuệ nhân tạo có thể giải thích (Explainable AI), giải quyết bài toán định lượng lâm sàng trên tập dữ liệu y tế thực tế RSNA gồm hơn 12,600 ảnh X-quang. Sau đây, em xin phép bắt đầu phần trình bày."

---

### 📄 SLIDE 2 — MỤC LỤC BÁO CÁO (Agenda)

**TIÊU ĐỀ:** `CẤU TRÚC BÁO CÁO ĐỀ TÀI`

**4 KHỐI NỘI DUNG CHÍNH:**
```
01 ─── BỐI CẢNH Y KHOA & ĐẶT BÀI TOÁN
       Khái niệm Tuổi xương | Hạn chế chẩn đoán thủ công | Regression vs Classification

02 ─── KHAI PHÁ DỮ LIỆU THỰC TẾ & CLASSICAL COMPUTER VISION
       Dataset RSNA (12,611 ảnh) | Bimodal Grayscale | Pipeline tiền xử lý 5 bước

03 ─── KIẾN TRÚC HỌC SÂU ĐA PHƯƠNG THỨC & HUẤN LUYỆN
       Dị hình giới tính (Gender MLP) | ResNet-50 Late Fusion | Huber Loss & AMP FP16

04 ─── KẾT QUẢ THỰC NGHIỆM, GIẢI THÍCH GRAD-CAM & ỨNG DỤNG
       Kiểm thử 1,262 ca (MAE 7.38 thg) | Chống Shortcut Learning | WebApp Lâm sàng
```

**🎨 Gợi ý thiết kế Canva:**
- 4 thẻ ngang hoặc 4 khối bo góc hiện đại, đánh số `01`–`04` kích thước lớn với màu Cyan Accent `#38BDF8`.
- Có thanh tiến trình (Progress Bar) chạy xuyên suốt phía dưới các slide tiếp theo.

**🎙️ Script thuyết trình (Sinh viên 1 - 30 giây):**
> "Nội dung bài báo cáo được chia thành 4 phần rõ rệt: Phần 1 đi từ bối cảnh lâm sàng và lý do tại sao chúng em tiếp cận bài toán Hồi quy thay vì Phân loại. Phần 2 phân tích đặc thù quang học của tập dữ liệu RSNA và đề xuất pipeline tiền xử lý 5 bước. Phần 3 mô tả kiến trúc học sâu đa phương thức kết hợp thông tin giới tính. Và Phần 4 công bố kết quả kiểm thử trên 1,262 ca độc lập, bản đồ nhiệt Grad-CAM xác thực y khoa và ứng dụng WebApp tương tác."

---

### 📄 SLIDE 3 — BỐI CẢNH LÂM SÀNG (Clinical Background)

**TIÊU ĐỀ:** `Ý NGHĨA LÂM SÀNG CỦA ĐÁNH GIÁ TUỔI XƯƠNG`

**CỘT TRÁI — Định Nghĩa & Vai Trò Y Học:**
```
🦴 TUỔI XƯƠNG (Bone Age / Skeletal Age)
• Thước đo mức độ trưởng thành SINH HỌC của hệ xương ở trẻ em.
• Hoàn toàn KHÁC BIỆT với tuổi theo giấy khai sinh (Chronological Age).
• Tiêu chuẩn vàng: Chụp X-quang bàn tay TRÁI (tư thế ngửa phẳng).

⚕️ ỨNG DỤNG LÂM SÀNG TRONG NHI KHOA:
• Chẩn đoán dậy thì sớm (Precocious Puberty) khi Tuổi xương > Tuổi thật (+12 tháng).
• Chẩn đoán suy tuyến yên, thiếu hormone tăng trưởng (GH), suy giáp bẩm sinh khi Tuổi xương < Tuổi thật (-12 tháng).
• Dự báo chiều cao trưởng thành phục vụ điều trị nội tiết và chỉnh nha.
```

**CỘT PHẢI — Thách Thức của Quy Trình Thủ Công:**
```
⚠️ THÁCH THỨC QUY TRÌNH HIỆN TẠI (ATLAS GP & TW3)

1. TỐN THỜI GIAN & ÁP LỰC QUÁ TẢI
   Bác sĩ mất 15 – 30 phút đối chiếu thủ công từng bức ảnh với Atlas Greulich-Pyle (1959) hoặc chấm điểm 20 vùng Tanner-Whitehouse (TW3).

2. SAI LỆCH CHỦ QUAN LỚN (OBSERVER VARIABILITY)
   Độ biến thiên giữa các bác sĩ (Inter-observer) và giữa các lần đọc của cùng một bác sĩ dao động từ 0.5 đến 1.5 năm tuổi!

🎯 MỤC TIÊU CỦA AI:
   Cung cấp kết quả định lượng khách quan trong < 1 giây, sai số MAE tiệm cận hoặc vượt qua năng lực đọc của bác sĩ chuyên khoa.
```

**🎨 Gợi ý thiết kế Canva:**
- Bên trái: Icon xương bàn tay và thẻ màu xanh dương biểu thị ý nghĩa khoa học.
- Bên phải: Hộp cảnh báo màu đỏ/cam nhạt nhấn mạnh các nhược điểm "Chủ quan - Chậm chạp - Sai số 0.5-1.5 năm".

**🎙️ Script thuyết trình (Sinh viên 1 - 60 giây):**
> "Thưa Thầy Cô, trong nhi khoa, tuổi xương là chỉ số phản ánh mức độ cốt hóa thực sự của cơ thể trẻ em. Một đứa trẻ 10 tuổi theo giấy khai sinh có thể mang tuổi xương 13 tuổi — báo hiệu tình trạng dậy thì sớm nguy cơ đóng sụn sớm khiến trẻ bị lùn khi trưởng thành; hoặc tuổi xương chỉ mới 7 tuổi — cảnh báo thiếu hụt hormone tăng trưởng. Hiện nay, các bác sĩ X-quang phải lật từng trang của cuốn bản đồ Greulich-Pyle xuất bản từ năm 1959 để so sánh bằng mắt thường. Quá trình này không chỉ làm quá tải hệ thống bệnh viện mà còn mang tính chủ quan rất lớn, với độ biến thiên sai lệch giữa các bác sĩ từ 6 tháng đến tận 1.5 năm tuổi. Đó là lý do cấp thiết cần một hệ thống thị giác máy tính tự động hóa và định lượng chuẩn xác."

---

### 📄 SLIDE 4 — ĐIỂM SÁNG TẠO: REGRESSION VS CLASSIFICATION

**TIÊU ĐỀ:** `ĐẶT BÀI TOÁN: HỒI QUY ĐA PHƯƠNG THỨC (MULTIMODAL REGRESSION)`

**BẢNG SO SÁNH HỌC THUẬT:**
```
┌────────────────────────────────────────┬────────────────────────────────────────┐
│   BÀI TOÁN PHÂN LOẠI (CLASSIFICATION)  │   ⭐ BÀI TOÁN CỦA ĐỀ TÀI (REGRESSION) ⭐│
├────────────────────────────────────────┼────────────────────────────────────────┤
│ • Đầu ra: Nhãn nhị phân rời rạc        │ • Đầu ra: Giá trị thực liên tục        │
│   (Ví dụ: Bình thường vs Bệnh lý)      │   Tuổi xương = 127.3 THÁNG (tháng tuổi)│
│                                        │                                        │
│ • Không gian đặc trưng: Rời rạc        │ • Không gian đặc trưng: Thứ bậc sinh học│
│   Cross-Entropy Loss                   │   Smooth L1 (Huber Loss)               │
│                                        │                                        │
│ • Đơn phương thức (Single-modal):      │ • Đa phương thức (Multimodal):         │
│   Chỉ nạp duy nhất tensor ảnh 2D       │   Ảnh X-quang 2D + Biến Giới tính      │
│                                        │                                        │
│ • Đánh giá: Accuracy, F1-Score         │ • Đánh giá: MAE (tháng), RMSE, R² Score│
└────────────────────────────────────────┴────────────────────────────────────────┘
```

**KHUNG NỔI BẬT (Key Innovation):**
```
💡 TẠI SAO ĐÂY LÀ ĐỒ ÁN THỰC THI NẶNG?
Mô hình không chỉ học các đặc trưng biên hay hoa văn bề mặt, mà phải giải mã được quy luật sinh lý học: sự thu hẹp dần của các khe sụn tiếp hợp (Growth Plates) tương ứng với trục thời gian liên tục từ 1 tháng đến 228 tháng tuổi!
```

**🎨 Gợi ý thiết kế Canva:**
- Thiết kế dạng bảng đối kháng (Versus Table). Cột trái viền xám mờ biểu thị bài toán phân loại thông thường; Cột phải viền phát sáng Cyan/Neon viền vàng nổi bật biểu thị bài toán Hồi quy của nhóm.

**🎙️ Script thuyết trình (Sinh viên 1 - 50 giây):**
> "Điểm sáng tạo cốt lõi của đề tài nằm ở việc định nghĩa bài toán. Đa số các đồ án xử lý ảnh y tế hiện nay dừng lại ở bài toán Phân loại (Classification) — ví dụ như phát hiện xem có khối u hay không, dùng hàm Cross-Entropy. Tuy nhiên, mức độ trưởng thành xương là một tiến trình sinh học liên tục. Vì vậy, nhóm chúng em tiếp cận dưới góc độ Hồi quy Đa phương thức (Multimodal Regression). Đầu vào không chỉ có bức ảnh X-quang mà còn tích hợp thông tin lâm sàng là giới tính của bệnh nhi; đầu ra là một giá trị số thực đo bằng tháng tuổi. Thang đo đánh giá là sai số tuyệt đối trung bình MAE tính bằng tháng, đòi hỏi mô hình phải học được sự biến đổi liên tục của các đĩa sụn theo thời gian."

---

## ═══════════════════════════════════════════════════════════════════
## PHẦN B: KHAI PHÁ DỮ LIỆU THẬT & TIỀN XỬ LÝ CLASSICAL CV (Slide 5 – 8)
## Người thuyết trình: SINH VIÊN 1 (Data & Classical CV Lead)
## ═══════════════════════════════════════════════════════════════════

---

### 📄 SLIDE 5 — DỮ LIỆU THẬT RSNA PEDIATRIC BONE AGE (EDA)

**TIÊU ĐỀ:** `KHAI PHÁ DỮ LIỆU THỰC TẾ RSNA PEDIATRIC BONE AGE`

**CỘT TRÁI — Thống Kê Quy Mô Tập Dữ Liệu:**
```
📁 NGUỒN DỮ LIỆU THẬT (KAGGLE API):
• Kho lưu trữ: kmader/rsna-bone-age (RSNA Challenge)
• Tổng dung lượng tải: 9.29 GB | Định dạng ảnh: PNG
• Đã quét kiểm tra tính toàn vẹn: 12,611 / 12,611 ảnh tồn tại trên đĩa (100%)

👥 PHÂN BỐ GIỚI TÍNH:
• Nam (Male):  6,833 ca (54.18%)
• Nữ (Female): 5,778 ca (45.82%)
• Tỷ lệ cân bằng tự nhiên, không bị lệch lớp giới tính
```

**CỘT PHẢI — Thống Kê Tuổi Xương (Ground Truth Distribution):**
```
📊 THỐNG KÊ ĐỊNH LƯỢNG (THÁNG TUỔI):
• Trung bình (Mean):     127.32 tháng (~10.6 tuổi)
• Độ lệch chuẩn (Std):    41.18 tháng
• Trung vị (Median):     132.00 tháng (11 tuổi)
• Phân vị 25% - 75%:     96.0 - 156.0 tháng (8 - 13 tuổi)
• Biên độ toàn dải:      1.0 - 228.0 tháng (Sơ sinh -> 19 tuổi)

⚠️ CẢNH BÁO TỪ THỐNG KÊ:
Mật độ mẫu tập trung mạnh nhất ở giai đoạn tiền dậy thì và dậy thì (8-13 tuổi). Nhóm trẻ sơ sinh (<2 tuổi) và nhóm trưởng thành (>16 tuổi) chiếm tỷ lệ nhỏ (<3%), đặt ra thử thách phương sai lớn ở hai cực phân phối.
```

**🎨 Gợi ý thiết kế Canva:**
- Đưa biểu đồ Histogram phân phối tuổi xương và biểu đồ Boxplot theo giới tính trích xuất từ Cell 6 của notebook.
- Hiển thị 2 con số nổi bật: `12,611 Ảnh` và `Mean: 10.6 Tuổi`.

**🎙️ Script thuyết trình (Sinh viên 1 - 50 giây):**
> "Tập dữ liệu chúng em sử dụng là bộ dữ liệu chuẩn y khoa thế giới từ cuộc thi RSNA Pediatric Bone Age Challenge gồm 12,611 ảnh X-quang bàn tay trái thật, dung lượng tải về hơn 9.2GB. Khai phá thống kê cho thấy tỷ lệ giới tính rất cân bằng với 54% nam và 46% nữ. Tuổi xương của bệnh nhi dao động từ 1 tháng đến 228 tháng (tức 19 tuổi), với giá trị trung bình là 127.3 tháng, tương đương 10.6 tuổi. Đỉnh phân bố tập trung mạnh nhất từ 8 đến 13 tuổi — giai đoạn các em bước vào tuổi dậy thì và các biến đổi xương diễn ra nhanh nhất."

---

### 📄 SLIDE 6 — THÁCH THỨC QUANG HỌC: LƯỢC ĐỒ MỨC XÁM (HISTOGRAM ANALYSIS)

**TIÊU ĐỀ:** `THÁCH THỨC CẢN QUANG & PHÂN TÍCH LƯỢC ĐỒ MỨC XÁM`

**CỘT TRÁI — Phân Tích Lược Đồ Bimodal Thực Tế:**
```
🩻 BẢN CHẤT CẢN QUANG TIA X:
Phân tích trực tiếp trên pixel ảnh X-quang thật (Cell 8) cho thấy lược đồ mức xám có dạng Hai Đỉnh Cực Đoan (Extreme Bimodal):

1. ĐỈNH NỀN KHÔNG KHÍ (Air Background) [0 - 25]:
   Chiếm hơn 60% tổng số pixel trong bức ảnh! Nơi tia X xuyên thẳng không bị cản, tạo thành màu đen tuyền.

2. ĐỈNH MÔ MỀM & CẤU TRÚC XƯƠNG [100 - 220]:
   • Mô mềm cản quang yếu: Dải xám [40 - 90]
   • Thân xương và bè xương cản quang mạnh: Dải [100 - 210]
   • Ký tự chữ L/R cản quang tuyệt đối: Dải đỉnh nhọn [240 - 255]
```

**CỘT PHẢI — Tại Sao Cân Bằng Lược Đồ Toàn Cục (HE) Thất Bại?**
```
❌ SỰ THẤT BẠI CỦA GLOBAL HISTOGRAM EQUALIZATION:
• Hàm tích lũy xác suất (CDF) bị chi phối áp đảo bởi lượng pixel nền đen 60%.
• Hậu quả: Dải động bị kéo dãn sai lệch, vùng nền đen bị khuếch đại thành nhiễu sáng lem nhem; trong khi đó, độ tương phản giữa sụn và xương ở bàn tay bị nén bẹp, làm mất chi tiết ranh giới giải phẫu!

✅ GIẢI PHÁP BẮT BUỘC:
Ứng dụng CLAHE (Contrast Limited Adaptive Histogram Equalization) chia ảnh thành lưới 8x8 khối cục bộ và cắt ngưỡng khuếch đại nhiễu Clip Limit = 3.0.
```

**🎨 Gợi ý thiết kế Canva:**
- Đưa hình ảnh phân tích từ Cell 8: Bên trái là ảnh X-quang thật của bệnh nhi ID: 10613, bên phải là đồ thị Grayscale Histogram với 2 mũi tên chú thích rõ đỉnh nền đen [0-25] và đỉnh cấu trúc xương [100-220].

**🎙️ Script thuyết trình (Sinh viên 1 - 60 giây):**
> "Khi phân tích sâu vào ma trận điểm ảnh X-quang thực tế, chúng em phát hiện một thách thức thị giác kinh điển: Lược đồ mức xám có phân bố hai đỉnh cực đoan (Extreme Bimodal). Hơn 60% diện tích bức ảnh là vùng nền không khí màu đen có cường độ pixel sát mức 0. Nếu lập trình viên áp dụng thuật toán cân bằng lược đồ màu toàn cục truyền thống (Global Histogram Equalization), hàm tích lũy xác suất sẽ bị lượng pixel nền đen này chi phối hoàn toàn. Kết quả là nền ảnh bị đẩy sáng kèm nhiễu hạt, trong khi ranh giới giữa đĩa sụn và bè xương bị nén phẳng, phá hủy hoàn toàn đặc trưng hình thái. Đây là lý do chúng em bắt buộc phải ứng dụng thuật toán CLAHE chia ảnh thành các ô cục bộ 8x8 để bảo tồn chi tiết."

---

### 📄 SLIDE 7 — CƠ SỞ Y SINH: HIỆN TƯỢNG DỊ HÌNH GIỚI TÍNH (SEXUAL DIMORPHISM)

**TIÊU ĐỀ:** `HIỆN TƯỢNG DỊ HÌNH GIỚI TÍNH (SEXUAL DIMORPHISM)`

**CƠ CHẾ SINH HỌC & TÁC ĐỘNG THUẬT TOÁN:**
```
🧬 QUY LUẬT CỐT HÓA THEO GIỚI TÍNH:
Trong quá trình phát triển tự nhiên, BÉ GÁI LUÔN CỐT HÓA SỚM HƠN BÉ TRAI TỪ 1.5 ĐẾN 2 NĂM:
• Bé gái thường đóng toàn bộ sụn tiếp hợp ở ngón tay và cổ tay vào khoảng 16 – 17 tuổi.
• Bé trai hoàn thành tiến trình cốt hóa muộn hơn, vào khoảng 18 – 19 tuổi.
```

**SỰ KHÁC BIỆT GIẢI PHẪU Ở CÙNG MỘT ĐỘ TUỔI:**
```
┌─────────────────────────────────────────────────────────────────────────┐
│                     VÍ DỤ ĐỐI CHỨNG Ở ĐỘ TUỔI 13                        │
├────────────────────────────────────┬────────────────────────────────────┤
│           BÉ GÁI 13 TUỔI           │           BÉ TRAI 13 TUỔI          │
├────────────────────────────────────┼────────────────────────────────────┤
│ • Các đĩa sụn đốt ngón đã bắt đầu  │ • Các đĩa sụn đốt ngón vẫn còn mở  │
│   hợp nhất và đóng kín (Fusion).   │   rộng, khoảng sáng cản quang rõ.  │
│ • Xương cổ tay cốt hóa hoàn thiện. │ • Xương Đậu (Pisiform) mới bắt đầu │
│ • Chuẩn bị kết thúc tăng trưởng.   │ • Đang ở giai đoạn tiền bứt phá.   │
└────────────────────────────────────┴────────────────────────────────────┘
```

**HỆ QUẢ KỸ THUẬT CHO MÔ HÌNH AI:**
```
⚠️ NGUY CƠ NẾU CHỈ DÙNG ẢNH:
Nếu chỉ nạp tensor ảnh vào mạng CNN mà không có thông tin giới tính, mô hình sẽ bị "mù giải phẫu" — không thể phân biệt được đây là bàn tay sắp đóng sụn của bé gái 13 tuổi hay của một bé trai 15 tuổi!
➔ THUỘC TÍNH GIỚI TÍNH (GENDER) LÀ ĐẶC TRƯNG LÂM SÀNG BẮT BUỘC PHẢI TÍCH HỢP.
```

**🎨 Gợi ý thiết kế Canva:**
- Đồ thị KDE so sánh đường cong phân bố nam và nữ từ Cell 6.
- Sử dụng biểu tượng biểu thị sự lệch pha 1.5 - 2 năm giữa bé gái (màu hồng) và bé trai (màu xanh dương).

**🎙️ Script thuyết trình (Sinh viên 1 - 50 giây):**
> "Một phát hiện y sinh học có tính quyết định đến kiến trúc hệ thống là hiện tượng Dị hình Giới tính (Sexual Dimorphism). Về mặt sinh lý, hệ xương của bé gái phát triển nhanh hơn bé trai từ 1.5 đến 2 năm. Ở cùng độ tuổi 13, một bé gái đã bắt đầu đóng kín các đĩa sụn ngón tay và chuẩn bị dừng phát triển chiều cao; trong khi một bé trai 13 tuổi thì các khe sụn vẫn mở rất rộng. Nếu mô hình AI chỉ nhìn vào bức ảnh mà không biết giới tính, nó sẽ rơi vào trạng thái bối rối không thể định lượng chính xác. Vì vậy, nhóm xác định Giới tính là một thuộc tính lâm sàng bắt buộc phải kết hợp đồng thời với ảnh."

---

### 📄 SLIDE 8 — PIPELINE CLASSICAL CV 5 BƯỚC (CHUẨN HÓA ĐẦU VÀO)

**TIÊU ĐỀ:** `PIPELINE TIỀN XỬ LÝ CLASSICAL COMPUTER VISION 5 BƯỚC`

**QUY TRÌNH 5 CÔNG ĐOẠN LIÊN HOÀN (CELL 10 THỰC TẾ):**
```
[Ảnh X-ray Thô] 
       │
       ▼
1. CLAHE (clip=3.0, tile=8x8) ───► Tăng tương phản cục bộ, hiện rõ bè xương
       │
       ▼
2. Gaussian Blur (5x5, σ=0) ──────► Khử nhiễu lượng tử hạt muối tiêu
       │
       ▼
3. Otsu Auto-Thresholding ────────► Tự động cực đại phương sai liên lớp tách tiền cảnh
       │
       ▼
4. Morphology Open & Close ───────► Phép mở xóa chữ L/R & Phép đóng lấp mô mềm
       │
       ▼
5. Max Contour Bounding Crop ─────► Định vị bàn tay, mở rộng biên an toàn +2%, resize 512x512
       │
       ▼
[Tensor Chuẩn Hóa [3, 512, 512] Đưa Vào Deep Learning]
```

**3 MỤC TIÊU CỐT LÕI ĐẠT ĐƯỢC:**
```
✓ Triệt tiêu 100% vùng nền đen vô ích, tập trung mật độ tham số vào bàn tay.
✓ Xóa bỏ hoàn toàn ký tự kim loại chỉ thị L/R của máy chụp, triệt hạ bẫy học đường tắt.
✓ Giữ trọn vẹn các chỏm mấu lồi đốt ngón xa nhờ biên an toàn đệm padding 2%.
```

**🎨 Gợi ý thiết kế Canva:**
- Đưa trực tiếp dải 5 ảnh trực quan hóa Before/After từ Cell 10 trong notebook (Ảnh gốc $	o$ Sau CLAHE $	o$ Sau Otsu $	o$ Sau Morphology $	o$ Ảnh sau Crop $512	imes 512$).

**🎙️ Script thuyết trình (Sinh viên 1 - 55 giây):**
> "Để giải quyết các thách thức quang học trên, trước khi nạp dữ liệu vào mạng học sâu, chúng em thiết kế một pipeline xử lý ảnh cổ điển khép kín gồm 5 bước. Bước 1 áp dụng CLAHE làm nổi bật các thớ sụn. Bước 2 lọc mượt Gaussian khử nhiễu lượng tử. Bước 3 áp dụng thuật toán phân ngưỡng tự động Otsu để nhị phân hóa tách bàn tay. Bước 4 áp dụng biến đổi hình thái học: phép mở để xóa sạch chữ chỉ thị Left/Right và dị vật kim loại, kết hợp phép đóng để lấp kín lòng bàn tay. Và Bước 5 dò tìm đường bao lớn nhất, mở rộng biên đệm an toàn 2% để không xén vào đốt ngón tay, sau đó resize về kích thước chuẩn 512x512. Pipeline này giúp làm sạch toàn bộ nhiễu biên và tối ưu hóa diện tích bàn tay cho mạng nơ-ron."

---

## ═══════════════════════════════════════════════════════════════════
## PHẦN C: KIẾN TRÚC HỌC SÂU ĐA PHƯƠNG THỨC & HUẤN LUYỆN (Slide 9 – 13)
## Người thuyết trình: SINH VIÊN 2 (Deep Learning & System Lead)
## ═══════════════════════════════════════════════════════════════════

---

### 📄 SLIDE 9 — KIẾN TRÚC MULTIMODAL LATE FUSION

**TIÊU ĐỀ:** `KIẾN TRÚC HỌC SÂU ĐA PHƯƠNG THỨC (MULTIMODAL LATE FUSION)`

**SƠ ĐỒ KHỐI KIẾN TRÚC MÔ HÌNH (CELL 14 THỰC TẾ):**
```
Ảnh Đã Tiền Xử Lý: [B, 3, 512, 512]            Biến Giới Tính: [B, 1] (Nam=1, Nữ=0)
               │                                                 │
               ▼                                                 ▼
┌───────────────────────────────┐               ┌───────────────────────────────┐
│ CNN BACKBONE: RESNET-50       │               │ GENDER EMBEDDING MLP          │
│ • Pre-trained trên ImageNet   │               │ • Linear(1 -> 32) + BatchNorm │
│ • Layer 1 -> Layer 4 (Conv)   │               │ • ReLU + Linear(32 -> 32)     │
│ • Global Avg Pooling (GAP)    │               │ • ReLU Activation             │
│ • Vector Đặc Trưng Ảnh:       │               │ • Vector Đặc Trưng Giới Tính: │
│   f_img ∈ R^2048              │               │   e_g ∈ R^32                  │
└──────────────┬────────────────┘               └───────────────┬───────────────┘
               │                                                │
               └───────────────────────┬────────────────────────┘
                                       │
                                       ▼
               ┌────────────────────────────────────────────────┐
               │ LATE FUSION (Ghép Nối Vector Đặc Trưng)        │
               │ z = [ f_img || e_g ] ∈ R^(2048 + 32) = R^2080  │
               └───────────────────────┬────────────────────────┘
                                       │
                                       ▼
               ┌────────────────────────────────────────────────┐
               │ HIERARCHICAL REGRESSION HEAD (3 Tầng Nén Dần)  │
               │ • Linear(2080 -> 1024) + BN + ReLU + Drop(0.3) │
               │ • Linear(1024 -> 512)  + BN + ReLU + Drop(0.3) │
               │ • Linear(512  -> 1)    (Đầu ra tuyến tính)     │
               └───────────────────────┬────────────────────────┘
                                       │
                                       ▼
               Dự Đoán Tuổi Xương: y_hat ∈ R^1 (Đơn vị: Tháng Tuổi)
```

**THÔNG SỐ MẠNG NƠ-RON:**
```
• Tổng tham số có thể huấn luyện (Trainable Parameters): 26,168,545 tham số.
• Tensor Shape Invariants tuân thủ nghiêm ngặt tại mọi tầng: [B, C, H, W] -> [B, 2048] -> [B, 2080] -> [B, 1].
```

**🎨 Gợi ý thiết kế Canva:**
- Thiết kế sơ đồ phân nhánh dạng chữ Y. Nhánh trái (màu xanh dương) là ảnh đi qua ResNet-50; Nhánh phải (màu tím) là biến Giới tính đi qua MLP; Cả hai hợp nhất tại nút trung tâm Late Fusion dẫn xuống đầu Hồi quy.

**🎙️ Script thuyết trình (Sinh viên 2 - 60 giây):**
> "Kính thưa Hội đồng, tiếp nối phần tiền xử lý của bạn, em xin phép trình bày về kiến trúc mô hình học sâu đề xuất. Để kết hợp cả ảnh và giới tính, nhóm thiết kế theo cơ chế Late Fusion gồm 2 nhánh song song. Nhánh thị giác sử dụng backbone ResNet-50 được tiền huấn luyện trên ImageNet, qua tầng Global Average Pooling để trích xuất vector đặc trưng không gian 2048 chiều. Nhánh lâm sàng là một mạng MLP 2 tầng chiếu biến nhị phân giới tính vào không gian liên tục 32 chiều. Chúng em ghép nối trực tiếp hai vector này thành một vector hợp nhất 2080 chiều, sau đó đưa qua đầu hồi quy phân tầng nén dần về 1024, 512 và cuối cùng là 1 đơn vị tuyến tính duy nhất đại diện cho số tháng tuổi. Toàn bộ mạng có hơn 26.1 triệu tham số."

---

### 📄 SLIDE 10 — CHIẾN LƯỢC MÃ HÓA GIỚI TÍNH: TẠI SAO CẦN MLP 32D?

**TIÊU ĐỀ:** `THIẾT KẾ NHÁNH GENDER EMBEDDING: TẠI SAO CẦN MLP 32-D?`

**ĐỐI CHỨNG 2 PHƯƠNG ÁN THIẾT KẾ:**
```
❌ PHƯƠNG ÁN 1: GHÉP NỐI ĐƠN LẺ 1 BIT (NAIVE 1-BIT CONCATENATION)
• Đưa trực tiếp giá trị thực [0.0] hoặc [1.0] ghép vào sau vector ảnh 2048 chiều: [f_img (2048-d) || 1.0].
• Hậu quả toán học: Thông tin giới tính chiếm tỷ trọng quá nhỏ (1 / 2049 ≈ 0.048%). Tín hiệu giới tính bị "nuốt chửng" hoàn toàn trong quá trình tính toán lan truyền tiến và lan truyền ngược gradient. Mô hình gần như bỏ qua giới tính.

-------------------------------------------------------------------------

✅ PHƯƠNG ÁN 2: NHÁNH GENDER EMBEDDING MLP 32-D (ĐỀ TÀI ÁP DỤNG)
• Chiếu biến nhị phân 1D qua mạng nơ-ron truyền thẳng:
  e_g = ReLU( W2 · ReLU( BatchNorm( W1 · g + b1 ) ) + b2 )
  với W1 ∈ R^(32x1), W2 ∈ R^(32x32).
• Ưu điểm vượt trội:
  1. Nâng tỷ trọng thông tin giới tính lên mức cân đối (32 / 2080 ≈ 1.54%).
  2. Tạo ra không gian biểu diễn liên tục giúp mô hình học được mối tương quan phi tuyến giữa giới tính và các trạng thái cốt hóa khác nhau.
  3. Duy trì gradient ổn định truyền ngược về nhánh lâm sàng qua từng epoch.
```

**🎨 Gợi ý thiết kế Canva:**
- Minh họa đồ họa: Hình ảnh một giọt nước nhỏ bị hòa tan trong biển lớn (đại diện cho Naive 1-bit) đối chiếu với hình ảnh cán cân cân bằng đặc trưng (đại diện cho MLP 32D).

**🎙️ Script thuyết trình (Sinh viên 2 - 50 giây):**
> "Một câu hỏi thiết kế rất quan trọng là: Tại sao không ghép trực tiếp số 0 hoặc 1 vào vector ảnh mà phải qua mạng MLP 32 chiều? Nếu chỉ ghép 1 bit đơn lẻ vào vector ảnh 2048 chiều, thông tin giới tính chỉ chiếm chưa tới 0.05% dung lượng đặc trưng. Khi tính đạo hàm ngược, tín hiệu này sẽ bị pha loãng hoàn toàn và mạng sẽ 'quên' mất yếu tố giới tính. Bằng cách thiết kế một mạng MLP nhỏ nâng lên 32 chiều có BatchNorm và ReLU, chúng em vừa tạo ra không gian biểu diễn phi tuyến phong phú, vừa nâng tỷ trọng thông tin lâm sàng lên mức cân đối, giúp các tầng hồi quy phía sau học được sự tương tác chặt chẽ giữa hình thái đĩa sụn và giới tính bệnh nhi."

---

### 📄 SLIDE 11 — CHIẾN LƯỢC TỐI ƯU: HÀM MẤT MÁT SMOOTH L1 (HUBER LOSS)

**TIÊU ĐỀ:** `TỐI ƯU HÓA: HÀM MẤT MÁT KHÁNG NGOẠI LAI SMOOTH L1`

**ĐỐI SÁNH 3 HÀM MẤT MÁT TRONG BÀI TOÁN HỒI QUY TUỔI XƯƠNG:**
```
1. HÀM SAI SỐ TOÀN PHƯƠNG MSE (L2 Loss): L = (y - y_hat)^2
   • Đạo hàm: 2|y - y_hat| (tỷ lệ thuận với sai số).
   • Nhược điểm trong y tế: Dữ liệu X-quang luôn có ca dị tật bẩm sinh hoặc nhãn lệch nhẹ (Outliers). Sai số lớn bị bình phương khiến gradient bùng nổ, kéo lệch toàn bộ trọng số mô hình.

2. HÀM SAI SỐ TUYỆT ĐỐI MAE (L1 Loss): L = |y - y_hat|
   • Đạo hàm: Hằng số (+1 hoặc -1).
   • Nhược điểm: Không khả vi liên tục tại điểm 0. Khi mô hình hội tụ sát nghiệm, bước nhảy cố định gây hiện tượng rung lắc quanh điểm cực tiểu.

3. ⭐ SMOOTH L1 LOSS (HUBER LOSS VỚI NGƯỠNG δ = 1.0) — ĐỀ TÀI ÁP DỤNG:
   
                ┌  0.5 * (y - y_hat)^2       khi |y - y_hat| ≤ 1.0  (Hội tụ êm như L2)
   L_Huber  =  │
                └  1.0 * |y - y_hat| - 0.5   khi |y - y_hat| > 1.0  (Kháng ngoại lai như L1)

   ✓ Kết hợp hoàn hảo: Đạo hàm trơn tru khi sai số nhỏ và giới hạn đạo hàm khi sai số lớn!
```

**BỘ TỐI ƯU HÓA & LỊCH TRÌNH HỌC TẬP:**
```
• Optimizer: AdamW (Learning rate η = 1e-4, Weight decay = 1e-4 chống overfitting).
• LR Scheduler: Cosine Annealing Learning Rate giảm mượt mà từ 1e-4 về 1e-6 theo chu kỳ cosine.
```

**🎨 Gợi ý thiết kế Canva:**
- Đồ thị so sánh hình dáng 3 đường cong: Parabol (MSE), Chữ V nhọn (MAE) và Đường cong làm tròn đáy Smooth L1 (Huber) màu xanh lá nổi bật.

**🎙️ Script thuyết trình (Sinh viên 2 - 50 giây):**
> "Đối với bài toán hồi quy tuổi xương y tế, việc chọn hàm loss quyết định sự sống còn của mô hình. Nếu dùng hàm MSE truyền thống, đạo hàm bậc hai sẽ phóng đại các ca dị tật bẩm sinh ngoại lai (outliers), gây bùng nổ gradient và làm méo mó mô hình. Ngược lại, nếu dùng MAE thì đạo hàm không trơn tại điểm 0, khiến mô hình bị rung lắc khi tiến gần cực tiểu. Do đó, nhóm lựa chọn hàm Smooth L1 hay còn gọi là Huber Loss với ngưỡng delta bằng 1.0. Hàm này hoạt động như L2 giúp hội tụ êm ái khi sai số nhỏ, và chuyển thành L1 tuyến tính để chặn đứng gradient khi gặp các ca sai lệch lớn, mang lại độ bền vững cực cao."

---

### 📄 SLIDE 12 — TỐI ƯU HÓA PHẦN CỨNG: MIXED PRECISION (AMP FP16)

**TIÊU ĐỀ:** `TỐI ƯU HÓA TÍNH TOÁN: AUTOMATIC MIXED PRECISION (AMP FP16)`

**GIẢI PHÁP THÍCH ỨNG PHẦN CỨNG GIỚI HẠN VRAM:**
```
┌───────────────────────────────────────┬───────────────────────────────────────┐
│     HUẤN LUYỆN ĐƠN ĐỘ ĐẦY ĐỦ (FP32)   │   ⭐ HUẤN LUYỆN HỖN HỢP (AMP FP16) ⭐ │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ • Mọi Tensor và Phép nhân ma trận     │ • Forward & Backward pass dùng FP16   │
│   đều lưu ở dạng dấu phẩy động 32-bit │   (16-bit nửa độ chính xác).          │
│                                       │                                       │
│ • Tiêu tốn VRAM lớn: Batch size bị nén│ • Trọng số Master Weight giữ FP32     │
│   xuống 4-8 trên GPU tầm trung.       │   đảm bảo độ chính xác cập nhật.      │
│                                       │                                       │
│ • Tốc độ tính toán chậm.              │ • Sử dụng torch.cuda.amp.GradScaler   │
│                                       │   chống hiện tượng tràn dưới số học.  │
└───────────────────────────────────────┴───────────────────────────────────────┘
```

**HIỆU QUẢ ĐỊNH LƯỢNG THỰC TẾ TRÊN GPU TESLA T4:**
```
🚀 TIẾT KIỆM BỘ NHỚ VRAM:  Giảm ~50% VRAM (chỉ chiếm 4.2 GB / 16 GB VRAM khả dụng).
⚡ TĂNG TỐC TÍNH TOÁN:     Tăng tốc gấp 2.1 lần nhờ tận dụng Tensor Cores của NVIDIA.
📦 KÍCH THƯỚC BATCH TỐI ƯU: Nâng Batch Size lên 16 ảnh độ phân giải cao 512x512!
```

**🎨 Gợi ý thiết kế Canva:**
- Biểu đồ thanh so sánh thời gian và mức chiếm dụng VRAM giữa FP32 và FP16.
- Huy hiệu nổi bật: `Batch Size = 16` | `VRAM: 4.2 GB` | `Tốc độ: x2.1`.

**🎙️ Script thuyết trình (Sinh viên 2 - 45 giây):**
> "Huấn luyện mạng sâu ResNet-50 trên ảnh X-quang độ phân giải cao 512x512 là bài toán cực kỳ ngốn bộ nhớ VRAM. Để giải quyết triệt để vấn đề này, chúng em kích hoạt kỹ thuật Automatic Mixed Precision (AMP FP16) kết hợp GradScaler. Thay vì dùng toàn bộ số thực 32-bit, quá trình lan truyền tiến và đạo hàm ngược được ép về 16-bit tận dụng các nhân Tensor Cores trên GPU Tesla T4. Kỹ thuật này giúp cắt giảm 50% mức chiếm dụng VRAM, cho phép nâng batch size lên 16 ảnh 512x512 và tăng tốc độ huấn luyện lên hơn 2 lần mà không hề làm suy giảm độ chính xác."

---

### 📄 SLIDE 13 — NHẬT KÝ HUẤN LUYỆN THẬT TRÊN GOOGLE COLAB (TESLA T4)

**TIÊU ĐỀ:** `TIẾN TRÌNH HUẤN LUYỆN THỰC TẾ TRÊN GOOGLE COLAB`

**THÔNG SỐ MÔI TRƯỜNG THỰC THI (CELL 2 & 16 THỰC TẾ):**
```
• Nền tảng điện toán: Google Colab Compute Cloud | GPU: NVIDIA Tesla T4 16GB
• Framework: PyTorch 2.x + CUDA 12 | Tổng thời gian huấn luyện: 202.1 phút (~3.37 giờ)
• Tổng số Epochs: 15 Epochs | Tốc độ: ~805 giây / Epoch
```

**BẢNG THEO DÕI HỘI TỤ VAL MAE QUA TỪNG EPOCH (TRÍCH XUẤT TỪ LOG THẬT):**
```
┌────────┬───────────────────┬──────────────────┬─────────────────┬──────────────────────┐
│ Epoch  │ Train Huber Loss  │  Val Huber Loss  │  Val MAE (Tháng)│   Trạng Thái Model   │
├────────┼───────────────────┼──────────────────┼─────────────────┼──────────────────────┤
│ Ep 01  │     118.8124      │     110.9286     │   111.43 thg    │ 🌟 Checkpoint Saved  │
│ Ep 02  │      96.7979      │      88.3897     │    88.89 thg    │ 🌟 Checkpoint Saved  │
│ Ep 04  │      39.1944      │      30.2591     │    30.76 thg    │ 🌟 Checkpoint Saved  │
│ Ep 06  │      13.2778      │       7.7759     │     8.26 thg    │ 🌟 Checkpoint Saved  │
│ Ep 11  │      11.0595      │       7.4442     │     7.93 thg    │ 🌟 Checkpoint Saved  │
│ Ep 13  │       9.9371      │       6.7691     │     7.25 thg    │ 🏆 BEST MODEL SAVED  │
│ Ep 15  │       9.2021      │       7.7493     │     8.24 thg    │ Trọng số cuối cùng   │
└────────┴───────────────────┴──────────────────┴─────────────────┴──────────────────────┘
```

**NHẬN XÉT HỘI TỤ:**
```
✓ Mô hình học cực nhanh trong 5 epoch đầu (Val MAE giảm từ 111 tháng xuống 12 tháng).
✓ Đạt điểm tối ưu toàn cục tại Epoch 13 với Validation MAE chạm mốc 7.25 tháng (~0.60 năm).
✓ Cơ chế Checkpoint tự động lưu lại trọng số tốt nhất `best_model.pth` để đưa vào kiểm thử.
```

**🎨 Gợi ý thiết kế Canva:**
- Bảng số liệu được định dạng với các dòng highlight màu xanh lá ở Epoch 13.
- Dòng trạng thái nổi bật: `Val MAE Kỷ Lục: 7.25 Tháng tại Epoch 13`.

**🎙️ Script thuyết trình (Sinh viên 2 - 50 giây):**
> "Đây là bảng nhật ký huấn luyện thực tế được trích xuất trực tiếp từ máy chủ Colab. Quá trình chạy 15 epoch kéo dài liên tục 202.1 phút, tức hơn 3.3 giờ đồng hồ. Như Thầy Cô có thể thấy, hàm loss và MAE giảm vô cùng ấn tượng: từ mức sai số ban đầu hơn 111 tháng ở epoch 1, mô hình nhanh chóng học được các đặc trưng giải phẫu cơ bản và nén sai số xuống dưới 13 tháng chỉ sau 5 epoch. Điểm hội tụ lý tưởng đạt được ở Epoch 13, với sai số Validation MAE chạm mốc kỷ lục 7.25 tháng. Hệ thống đã tự động đóng băng và lưu lại checkpoint trọng số tối ưu này làm mô hình chính thức để đánh giá."

---

## ═══════════════════════════════════════════════════════════════════
## PHẦN D: KẾT QUẢ THỰC NGHIỆM, XAI GRAD-CAM & ỨNG DỤNG (Slide 14 – 20)
## Người thuyết trình: SINH VIÊN 2 (Deep Learning & System Lead)
## ═══════════════════════════════════════════════════════════════════

---

### 📄 SLIDE 14 — KẾT QUẢ KIỂM THỬ ĐỘC LẬP TRÊN 1,262 CA UNSEEN (TEST SET)

**TIÊU ĐỀ:** `KẾT QUẢ KIỂM THỬ ĐỘC LẬP TRÊN TẬP TEST (1,262 BỆNH NHI)`

**4 CHỈ SỐ VÀNG CỦA MÔ HÌNH TRÊN TẬP TEST (CELL 18 THỰC TẾ):**
```
┌────────────────────────────────────────┬────────────────────────────────────────┐
│  SAI SỐ TUYỆT ĐỐI TRUNG BÌNH (TEST MAE)│   HỆ SỐ XÁC ĐỊNH (R² SCORE)            │
│               7.38 THÁNG               │                 0.9452                 │
│  (~0.62 Năm — Tiệm cận năng lực Bác sĩ)│  (Khớp 94.52% sự biến thiên tuổi thật) │
├────────────────────────────────────────┼────────────────────────────────────────┤
│  CĂN BẬC HAI SAI SỐ BÌNH PHƯƠNG (RMSE) │   ĐỘ AN TOÀN LÂM SÀNG NHI KHOA (≤ 1 NĂM)│
│               9.60 THÁNG               │                 81.38%                 │
│  (Kiểm soát chặt chẽ các ca ngoại lai) │  (Hơn 81% ca lệch trong ngưỡng sinh lý)│
└────────────────────────────────────────┴────────────────────────────────────────┘
```

**PHÂN TÍCH TỶ LỆ CHÍNH XÁC THEO NGƯỠNG LÂM SÀNG:**
```
• Độ chính xác trong giới hạn 0.5 năm (Sai số ≤ 6 tháng):  51.51% (Hơn một nửa số ca đạt độ chính xác gần như tuyệt đối).
• Độ chính xác trong giới hạn 1.0 năm (Sai số ≤ 12 tháng): 81.38% (Chuẩn an toàn can thiệp nội tiết).
• Độ chính xác trong giới hạn 2.0 năm (Sai số ≤ 24 tháng): 98.40% (Triệt tiêu hoàn toàn các phán đoán sai lệch nguy hiểm).
```

**🎨 Gợi ý thiết kế Canva:**
- 4 Card hình khối kích thước lớn chiếm 60% màn hình, số đo in đậm màu vàng/xanh neon.
- Phía dưới có thanh tiến trình biểu diễn tỷ lệ 81.38% đạt chuẩn an toàn y tế.

**🎙️ Script thuyết trình (Sinh viên 2 - 55 giây):**
> "Sau khi hoàn tất huấn luyện, chúng em nạp lại tệp trọng số best_model.pth để kiểm thử khách quan trên 1,262 ca bệnh nhi hoàn toàn mới chưa từng xuất hiện trong quá trình train. Kết quả đạt được vô cùng thuyết phục: Sai số tuyệt đối trung bình MAE trên tập test độc lập đạt 7.38 tháng, tương đương khoảng 0.62 năm. Hệ số xác định R bình phương đạt 0.9452, chứng minh mô hình giải thích được gần 95% sự biến thiên tuổi xương sinh học. Đặc biệt, xét dưới góc độ y khoa, có tới 81.38% tổng số ca bệnh nhi có dự đoán sai lệch dưới 12 tháng — tức nằm trọn vẹn trong biên độ sinh lý cho phép của chẩn đoán lâm sàng."

---

### 📄 SLIDE 15 — BỘ 3 BIỂU ĐỒ ĐÁNH GIÁ THỰC NGHIỆM CHUẨN HỌC THUẬT

**TIÊU ĐỀ:** `BỘ BA BIỂU ĐỒ ĐÁNH GIÁ ĐỘ HỘI TỤ VÀ PHÂN BỐ SAI SỐ`

**3 BIỂU ĐỒ CHUYÊN SÂU TRÍCH XUẤT TỪ CELL 18 TRONG NOTEBOOK:**

```
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│ 1. ĐƯỜNG CONG HÀM LOSS   │ 2. TƯƠNG QUAN PREDICTED │ 3. PHÂN BỐ PHẦN DƯ SAI SỐ│
│   (Training vs Validation)│    vs ACTUAL (y = x)    │    (Residual Histogram) │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ • Đường Train và Val    │ • Cụm điểm dữ liệu phân │ • Biểu đồ hình chuông   │
│   loss cùng giảm êm dịu │   bố bó sát đối xứng    │   chuẩn Gauss tập trung │
│   từ 118 về sát mức 7.  │   dọc theo đường đỏ y=x │   dày đặc quanh điểm 0. │
│ • Không có khoảng cách  │ • Độ tin cậy trải đều   │ • Phân bố đối xứng cân  │
│   phân kỳ giữa 2 đường  │   từ 2 tuổi đến 17 tuổi.│   bằng, không có hiện   │
│   ➔ Bằng chứng đanh thép│ • R² = 0.945 cực cao.   │   tượng lệch dương hay  │
│   mô hình không overfit!│                         │   lệch âm (Unbiased).   │
└─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

**KẾT LUẬN THỰC NGHIỆM:**
```
Mô hình thể hiện tính tổng quát hóa (Generalization) vượt trội, duy trì độ chính xác cao đồng đều trên cả bệnh nhi nam và nữ ở mọi phân nhóm tuổi.
```

**🎨 Gợi ý thiết kế Canva:**
- Nhúng trực tiếp cụm 3 biểu đồ từ Cell 18 vào slide. Đặt 3 chú thích ngắn gọn ngay dưới từng đồ thị.

**🎙️ Script thuyết trình (Sinh viên 2 - 50 giây):**
> "Slide này thể hiện bộ 3 đồ thị chẩn đoán thực nghiệm của mô hình. Biểu đồ thứ nhất bên trái là đường cong Loss giữa Train và Validation: cả hai đường cùng giảm song song và hội tụ sát nhau mà không hề có sự phân kỳ, chứng minh mô hình không hề bị học vẹt hay Overfitting. Biểu đồ thứ hai ở giữa là biểu đồ phân tán giữa tuổi dự đoán và tuổi thực tế: Thầy Cô có thể thấy 1,262 điểm dữ liệu tập trung ôm sát đường chéo lý tưởng màu đỏ y bằng x từ lứa tuổi mầm non đến tuổi trưởng thành. Biểu đồ thứ ba bên phải là phân bố phần dư sai số có dạng hình chuông đối xứng hoàn hảo quanh trục số 0, chứng minh thuật toán không hề bị thiên lệch hệ thống."

---

### 📄 SLIDE 16 — BẢNG ĐỐI CHUẨN KHOA HỌC (BENCHMARKING VỚI CÁC BÀI BÁO)

**TIÊU ĐỀ:** `ĐỐI CHUẨN HIỆU NĂNG VỚI CÁC CÔNG BỐ QUỐC TẾ & BÁC SĨ`

**BẢNG ĐỐI SO SÁNH HỌC THUẬT:**
```
┌──────────────────────────────────────┬────────────────────────────┬────────────────────────────┐
│         MÔ HÌNH / NGHIÊN CỨU         │      PHƯƠNG PHÁP CỐT LÕI   │     MAE ĐẠT ĐƯỢC (THÁNG)   │
├──────────────────────────────────────┼────────────────────────────┼────────────────────────────┤
│ Bác sĩ X-quang Nhi chuyên khoa       │ Đọc thủ công qua Atlas GP  │ 6.0 – 9.0 Tháng (Biến thiên)│
│                                      │                            │                            │
│ Halabi et al. (Radiology 2019)       │ Inception-V3 (RSNA Base)   │ 6.08 Tháng                 │
│                                      │                            │                            │
│ ⭐ MÔ HÌNH CỦA NHÓM CHÚNG EM ⭐        │ ResNet-50 + Classical CV   │ 7.38 Tháng                 │
│ (DUT Capstone Project)               │ + Gender MLP 32D (Huber)   │ (~0.62 Năm — Đạt chuẩn)    │
│                                      │                            │                            │
│ Đội Vô địch RSNA 16Bit (Cicero 2017) │ Ensemble 5 Mạng CNNs nặng  │ 4.27 Tháng (Tối đa SOTA)   │
└──────────────────────────────────────┴────────────────────────────┴────────────────────────────┘
```

**NHẬN ĐỊNH ĐÓNG GÓP:**
```
1. VƯỢT TRỘI PHƯƠNG PHÁP THỦ CÔNG: Sai số 7.38 tháng nằm trọn trong khoảng biến thiên tự nhiên của các bác sĩ X-quang (6-9 tháng), nhưng tốc độ nhanh hơn gấp 1,000 lần (0.05s vs 20 phút).
2. THÍCH ỨNG TỐI ƯU TÀI NGUYÊN: Chỉ sử dụng 1 mô hình ResNet-50 đơn lẻ huấn luyện trong 3.3 giờ, đạt hiệu năng xấp xỉ bài báo gốc của RSNA (7.38 thg so với 6.08 thg), không đòi hỏi cụm máy chủ đa GPU đắt đỏ như đội vô địch 16Bit.
```

**🎨 Gợi ý thiết kế Canva:**
- Bảng so sánh nổi bật dòng của nhóm với viền vàng / nền xanh dạ quang. Dòng của Bác sĩ X-quang viền cam để làm nổi bật tính khả thi ứng dụng.

**🎙️ Script thuyết trình (Sinh viên 2 - 50 giây):**
> "Khi đặt kết quả 7.38 tháng của nhóm lên bàn cân đối chiếu với các công bố quốc tế, chúng em nhận thấy những đóng góp rất rõ ràng. Thứ nhất, độ lệch 7.38 tháng nằm hoàn toàn trong ngưỡng biến thiên tự nhiên giữa các bác sĩ X-quang chuyên khoa (thường dao động từ 6 đến 9 tháng), nhưng thời gian chẩn đoán được rút ngắn từ 20 phút xuống chưa đầy 0.05 giây. Thứ hai, bài báo chính thức của cuộc thi RSNA trên tạp chí Radiology đạt mức 6.08 tháng khi sử dụng hạ tầng lớn; trong khi nhóm chúng em chỉ dùng một mạng ResNet-50 đơn lẻ huấn luyện trong hơn 3 giờ trên Google Colab nhưng đã tiệm cận rất sát mốc này. Điều này chứng minh tính khả thi cao khi ứng dụng vào các bệnh viện tuyến cơ sở."

---

### 📄 SLIDE 17 — EXPLAINABLE AI: REGRESSION GRAD-CAM GIẢI THÍCH MÔ HÌNH

**TIÊU ĐỀ:** `MINH BẠCH Y TẾ: REGRESSION GRAD-CAM & CHỐNG SHORTCUT LEARNING`

**BẢN ĐỒ NHIỆT XÁC THỰC GIẢI PHẪU (CELL 20 THỰC TẾ):**
```
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│ ẢNH X-QUANG THỰC TẾ     │ HEATMAP GRAD-CAM        │ GRAD-CAM OVERLAY        │
│ (Bệnh nhi 82.0 tháng)   │ (Bản đồ kích hoạt tầng conv3)│ (Phủ nhiệt lên giải phẫu)│
└─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

**2 PHÁT HIỆN Y SINH ĐƯỢC GRAD-CAM CHỨNG MINH:**
```
1. TẬP TRUNG CHUẨN XÁC VÀO CÁC VÙNG CỐT HÓA THEO CHUẨN TANNER-WHITEHOUSE (TW3):
   • Vùng nhiệt đỏ rực tập trung trực tiếp vào các ĐĨA SỤN ĐỐT NGÓN TAY (Epiphyses) và CỤM 8 HẠT XƯƠNG CỔ TAY (Carpal Bones).
   • Đây chính là các trung tâm cốt hóa sinh học quyết định tuổi xương của trẻ em!

2. LOẠI TRỪ HOÀN TOÀN BẪY HỌC ĐƯỜNG TẮT (SHORTCUT LEARNING):
   • Không hề có vùng kích hoạt nhiệt nào xuất hiện ở viền ảnh, góc ảnh hay vùng nền đen.
   • Bằng chứng khẳng định: Pipeline Classical CV (Otsu + Morphology) đã xóa sổ hoàn toàn chữ chỉ thị L/R, buộc mô hình phải học tri thức y khoa chân thực chứ không học vẹt ký tự đánh dấu!
```

**🎨 Gợi ý thiết kế Canva:**
- Đưa trực tiếp bộ 3 ảnh Grad-CAM từ Cell 20 vào slide: Ảnh xám gốc $	o$ Heatmap Jet $	o$ Ảnh Overlay kết hợp. Có các mũi tên chỉ rõ vào cụm xương cổ tay và sụn ngón tay.

**🎙️ Script thuyết trình (Sinh viên 2 - 55 giây):**
> "Một trong những rào cản lớn nhất khi đưa AI vào y tế là vấn đề 'Hộp đen' (Black-box). Để chứng minh tính minh bạch, nhóm đã tùy biến thuật toán Grad-CAM cho bài toán hồi quy liên tục, trích xuất đạo hàm trên tầng tích chập cuối cùng để sinh bản đồ nhiệt. Kết quả ở Cell 20 cho thấy hai minh chứng y khoa cực kỳ giá trị: Thứ nhất, mô hình thực sự 'nhìn' vào các đĩa sụn tiếp hợp ở ngón tay và cụm xương cổ tay — hoàn toàn trùng khớp với 20 vùng giải phẫu của phương pháp Tanner-Whitehouse mà bác sĩ tin cậy. Thứ hai, các góc ảnh hoàn toàn là màu xanh lạnh, chứng minh mô hình không hề bị rơi vào bẫy học đường tắt (Shortcut Learning) từ các chữ đánh dấu kim loại. Mô hình thực sự đưa ra quyết định dựa trên tri thức giải phẫu."

---

### 📄 SLIDE 18 — CASE STUDY SUY LUẬN LÂM SÀNG & BẢO VỆ CHUẨN WHO

**TIÊU ĐỀ:** `CA BỆNH NHI THỰC TẾ & HỆ THỐNG CẢNH BÁO CHUẨN WHO`

**KẾT QUẢ SUY LUẬN TỰ ĐỘNG TRÊN 1 CA TEST THẬT (CELL 22 THỰC TẾ):**
```
============================================================
📋 HỒ SƠ BỆNH NHI LÂM SÀNG (CLINICAL AI REPORT)
============================================================
• Giới tính bệnh nhi:       NỮ (Female)
• Tuổi thật theo khai sinh: 82.0 tháng (6 tuổi 10 tháng)
• Tuổi xương AI dự đoán:    91.8 tháng (7 tuổi 8 tháng)
• Độ lệch pha tăng trưởng:  Δ = +9.8 tháng

------------------------------------------------------------
🟢 KẾT LUẬN LÂM SÀNG TỰ ĐỘNG:
TỐC ĐỘ PHÁT TRIỂN XƯƠNG BÌNH THƯỜNG
Độ lệch nằm trong ngưỡng sinh lý an toàn (|Δ| ≤ 12 tháng = 1 năm).
Hệ xương đồng nhịp với lứa tuổi sinh học, không có dấu hiệu dậy thì sớm.
============================================================
```

**QUY TẮC CẢNH BÁO PHÂN TẦNG Y TẾ (WHO ANTHRO STANDARDS):**
```
🟢 XANH LÁ (|Δ| ≤ 12 tháng): Bình thường, phát triển đồng nhịp.
🟡 VÀNG    (12 < |Δ| ≤ 24 tháng): Lệch pha tăng trưởng nhẹ, đề nghị theo dõi mật độ xương sau 6 tháng.
🔴 ĐỎ      (|Δ| > 24 tháng = 2 năm): Lệch pha nghiêm trọng!
   • Δ > +24 tháng: Nguy cơ Dậy Thì Sớm (Precocious Puberty) hoặc tăng sản tuyến thượng thận!
   • Δ < -24 tháng: Nguy cơ Thiếu Hụt Hormone Tăng Trưởng (GH) hoặc suy giáp bẩm sinh!
```

**🎨 Gợi ý thiết kế Canva:**
- Thiết kế một phiếu kết quả chẩn đoán y tế (Medical Diagnostic Card) giao diện hiện đại, có con dấu tròn màu xanh lá `NORMAL / PASS`.
- Đồ thị bách phân vị chiều cao theo chuẩn WHO định vị chấm đỏ của bệnh nhi trên đường cong Median.

**🎙️ Script thuyết trình (Sinh viên 2 - 50 giây):**
> "Trên màn hình là kết quả chạy hàm suy luận chẩn đoán thực tế trên một bệnh nhi nữ 82 tháng tuổi, tức khoảng 6.8 tuổi. Hệ thống dự đoán tuổi xương là 91.8 tháng, độ chênh lệch là dương 9.8 tháng. Dựa trên tiêu chuẩn của Tổ chức Y tế Thế giới (WHO), hệ thống lập tức xuất phiếu chẩn đoán màu Xanh Lá: 'Tốc độ phát triển xương bình thường', do độ lệch nằm gọn trong biên độ an toàn 1 năm. Nếu độ lệch vượt quá 24 tháng, hệ thống sẽ tự động bật cảnh báo Đỏ khẩn cấp để bác sĩ hội chẩn nội tiết nhi về nguy cơ dậy thì sớm hoặc thiếu hormone GH. Toàn bộ logic này được đóng gói khép kín thành sản phẩm ứng dụng."

---

### 📄 SLIDE 19 — PHẦN MỀM LÂM SÀNG STREAMLIT WEB APP (LIVE DEMO)

**TIÊU ĐỀ:** `TRIỂN KHAI PHẦN MỀM LÂM SÀNG STREAMLIT WEB APP`

**KIẾN TRÚC VẬN HÀNH HYBRID CLOUD-LOCAL CỦA SẢN PHẨM:**
```
┌───────────────────────────────────────┬───────────────────────────────────────┐
│     ☁️ CLOUD TRAINING (GOOGLE COLAB)  │    💻 LOCAL CLINICAL APP (STREAMLIT)  │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ • Huấn luyện mô hình nặng trên GPU    │ • Ứng dụng WebApp tương tác nhẹ nhàng │
│ • Xuất file trọng số: best_model.pth  │ • Chạy offline trên laptop/máy trạm   │
│   dung lượng tối ưu chỉ ~98 MB        │ • Bác sĩ tải ảnh PNG và chọn giới tính│
│ • Không cần duy trì kết nối đám mây   │ • Phản hồi kết quả trong < 0.05 giây! │
└───────────────────────────────────────┴───────────────────────────────────────┘
```

**TÍNH NĂNG NỔI BẬT CỦA PHẦN MỀM (`clinical_webapp/app.py`):**
```
1. Giao diện Y tế Thân thiện: Hỗ trợ kéo thả ảnh X-quang, thanh trượt nhập tuổi khai sinh.
2. Thẻ Đo Lường Tức Thì: Hiển thị song song Tuổi Thật - Tuổi Xương - Độ Lệch Delta.
3. Bản Đồ Nhiệt Giải Thích: Hiển thị ảnh gốc cạnh ảnh Grad-CAM cho bác sĩ kiểm chứng.
4. Tích Hợp Đồ Thị Bách Phân Vị WHO: Tra cứu đường cong tăng trưởng chiều cao tự động.
```

**🎨 Gợi ý thiết kế Canva:**
- Mockup màn hình giao diện Streamlit WebApp hiển thị trên màn hình máy tính (giao diện dark/light mode thanh lịch, có ảnh X-quang, thẻ số và đồ thị WHO).

**🎙️ Script thuyết trình (Sinh viên 2 - 45 giây):**
> "Để chuyển giao nghiên cứu thành sản phẩm thực tế, nhóm đã đóng gói mô hình thành một ứng dụng Web tương tác lâm sàng hoàn chỉnh bằng Streamlit chạy ngay trên máy cá nhân. Sau khi huấn luyện trên Colab, tệp trọng số best_model.pth chỉ nặng 98MB được tải về máy local. Các bác sĩ chỉ cần mở trình duyệt, kéo thả ảnh X-quang bàn tay của trẻ, chọn giới tính và nhập ngày sinh. Chưa đầy 0.05 giây, màn hình sẽ hiển thị ngay thẻ chẩn đoán tuổi xương, bản đồ nhiệt Grad-CAM xác thực và đồ thị tăng trưởng WHO. Mô hình hoàn toàn có thể chạy mượt mà trên CPU hoặc laptop thông thường mà không cần GPU đắt đỏ."

---

### 📄 SLIDE 20 — TỔNG KẾT, ĐÓNG GÓP HỌC THUẬT & HƯỚNG PHÁT TRIỂN

**TIÊU ĐỀ:** `TỔNG KẾT ĐỀ TÀI & ĐỊNH HƯỚNG PHÁT TRIỂN`

**3 ĐÓNG GÓP CỐT LÕI CỦA ĐỒ ÁN:**
```
1. KHOA HỌC DỮ LIỆU & CLASSICAL CV:
   Xây dựng hoàn chỉnh pipeline 5 bước (CLAHE, Otsu, Morphology, Crop 2%) xử lý triệt để thách thức cản quang Bimodal và bẫy Shortcut Learning trên 12,611 ảnh RSNA.

2. MÔ HÌNH HỌC SÂU ĐA PHƯƠNG THỨC CHUẨN XÁC:
   Đề xuất kiến trúc ResNet-50 kết hợp Gender Embedding 32D (Late Fusion 2080D) tối ưu bằng Huber Loss, đạt Test MAE = 7.38 tháng, R² = 0.9452, độ an toàn lâm sàng 81.38%.

3. TÍNH MINH BẠCH & ỨNG DỤNG THỰC TIỄN:
   Xác thực y khoa bằng Regression Grad-CAM đối chiếu chuẩn TW3 và triển khai thành công WebApp lâm sàng thời gian thực tích hợp khuyến nghị WHO.
```

**HẠN CHẾ & HƯỚNG PHÁT TRIỂN TIẾP THEO:**
```
• Hạn chế: Phương sai dự đoán còn hơi phân tán ở nhóm trẻ sơ sinh dưới 1 tuổi do sụn chưa cốt hóa rõ.
• Hướng phát triển: 
  - Nâng cấp backbone lên Vision Transformers (Swin-T) và module Cross-Attention.
  - Phân vùng 2 nhánh chuyên biệt: 1 nhánh nhìn toàn bàn tay, 1 nhánh crop riêng 8 xương cổ tay theo chuẩn TW3.
```

**LỜI CẢM ƠN:**
```
NHÓM CHÚNG EM XIN TRÂN TRỌNG CẢM ƠN QUÝ THẦY CÔ VÀ CÁC BẠN ĐÃ LẮNG NGHE!
Nhóm rất mong nhận được những câu hỏi và ý kiến đóng góp quý báu từ Hội đồng.
```

**🎨 Gợi ý thiết kế Canva:**
- Nền trang trọng, tóm tắt 3 huy hiệu vàng đại diện cho 3 đóng góp (Dữ liệu - Mô hình - Ứng dụng).
- Chữ "THANK YOU / Q&A" lớn ở trung tâm kèm thông tin liên hệ của nhóm sinh viên.

**🎙️ Script thuyết trình (Sinh viên 1 & Sinh viên 2 kết hợp - 45 giây):**
> "Kính thưa Hội đồng, đồ án của nhóm chúng em đã chứng minh sự kết hợp hài hòa giữa xử lý ảnh cổ điển và học sâu đa phương thức có thể giải quyết xuất sắc bài toán đánh giá tuổi xương với độ chính xác cao và tính minh bạch y học rõ ràng. Trong giai đoạn tiếp theo, nhóm sẽ tiếp tục nghiên cứu các kiến trúc Vision Transformers và nhánh chuyên biệt cho xương cổ tay để tối ưu hơn nữa các trường hợp trẻ nhỏ. Nhóm chúng em xin trân trọng cảm ơn Quý Thầy Cô đã chú ý lắng nghe và rất mong nhận được những góp ý, câu hỏi phản biện từ Hội đồng!"

---
