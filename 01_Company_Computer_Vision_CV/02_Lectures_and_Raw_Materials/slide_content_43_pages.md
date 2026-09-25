# 🎯 KỊCH BẢN THUYẾT TRÌNH BẢO VỆ ĐỒ ÁN TỐT NGHIỆP / NCKH (43 SLIDES)
## ĐỀ TÀI: HỆ THỐNG TỰ ĐỘNG ĐÁNH GIÁ TUỔI XƯƠNG TỪ ẢNH X-QUANG BÀN TAY BẰNG HỌC SÂU ĐA PHƯƠNG THỨC VÀ TRÍ TUỆ NHÂN TẠO CÓ THỂ GIẢI THÍCH

> **Mã Chuẩn Tham Chiếu:** Kế thừa 100% bố cục và phân bổ đối đầu từ `MECHANICAL_FAULT_XRAY Project\Slide.pptx` (43 Slides)  
> **Thời lượng báo cáo:** 20 - 25 phút (Phân công 2 Sinh viên thuyết trình nhịp nhàng)  
> **Cấu trúc phân công:**  
> • **Sinh viên 1 (Slide 01 -> 16):** Đặt vấn đề, Bối cảnh y tế, Khảo sát dữ liệu RSNA, Pipeline Classical CV 5 bước, Quy trình tổng thể.  
> • **Sinh viên 2 (Slide 17 -> 37):** Thế trận Tam mã học sâu (ResNet-50 vs ConvNeXt vs Swin-T), Động học huấn luyện, Bảng ma trận đối đầu.  
> • **Sinh viên 1 & 2 (Slide 38 -> 43):** Minh bạch y tế XAI Grad-CAM, Cảnh báo WHO, Demo WebApp lâm sàng, Hạn chế & Kết luận.

---

### 📄 SLIDE 01 — TRANG BÌA (TITLE SLIDE)
**TIÊU ĐỀ:** `HỆ THỐNG TỰ ĐỘNG ĐÁNH GIÁ TUỔI XƯƠNG TỪ ẢNH X-QUANG BÀN TAY NHI KHOA`  
**PHỤ ĐỀ:** `TIẾP CẬN HỌC SÂU ĐA PHƯƠNG THỨC & TRÍ TUỆ NHÂN TẠO CÓ THỂ GIẢI THÍCH (XAI)`  
**THÔNG TIN:**
- Trường Đại học Bách Khoa — Đại học Đà Nẵng (DUT)
- Khoa Công nghệ Thông tin | Viện Công nghệ Thị giác Máy tính VisionLab (`CORP-01-CV`)
- Giảng viên hướng dẫn: Cố vấn Học thuật DUT
- Sinh viên thực hiện: Sinh viên 1 & Sinh viên 2

**🎨 Gợi ý thiết kế Canva:**
- Nền tối chuyên nghiệp (Deep Medical Navy `#0a192f`).
- Phía trái đặt ảnh phim X-quang bàn tay với hiệu ứng phát sáng Cyan/Neon viền sụn; phía phải đặt tiêu đề chữ trắng nổi bật, font Inter/Montserrat hiện đại.

**🎙️ Script thuyết trình (Sinh viên 1 - 45 giây):**
> "Kính thưa Thầy Cô trong Hội đồng phản biện và toàn thể các bạn sinh viên. Hôm nay, nhóm chúng em xin trân trọng báo cáo đề tài tốt nghiệp: 'Hệ thống Tự động Đánh giá Tuổi Xương từ ảnh X-quang Bàn tay Nhi khoa bằng Học Sâu Đa Phương Thức và Trí Tuệ Nhân Tạo Có Thể Giải Thích'. Đây là công trình nghiên cứu ứng dụng thị giác máy tính giải quyết bài toán định lượng y sinh thực tế trên tập dữ liệu chuẩn quốc tế RSNA gồm hơn 12.600 bệnh nhi. Sau đây, em xin phép bắt đầu phần trình bày."

---

### 📄 SLIDE 02 — PHÂN CÔNG NHIỆM VỤ NHÓM
**TIÊU ĐỀ:** `PHÂN CÔNG NHIỆM VỤ & ĐÓNG GÓP THỰC HIỆN`  
**NỘI DUNG:**
- **Sinh viên 1:** Khảo sát lâm sàng, Kỹ nghệ dữ liệu RSNA, Pipeline Tiền xử lý Classical CV 5 bước, Xây dựng khối cảnh báo WHO và Phát triển ứng dụng WebApp Demo.
- **Sinh viên 2:** Thiết kế kiến trúc Đa phương thức Late Fusion, Huấn luyện chuỗi 3 mô hình đối kháng (ResNet-50, ConvNeXt, Swin-T), Tối ưu hóa Huber Loss, Thẩm định Grad-CAM.
- **Cả hai thành viên:** Tham gia 100% vào mọi giai đoạn thu thập dữ liệu, phân tích thực nghiệm và hoàn thiện hồ sơ báo cáo chuyên sâu.

**🎙️ Script thuyết trình (Sinh viên 1 - 30 giây):**
> "Để đảm bảo tính liên tục và chất lượng kỹ nghệ cao nhất, hai thành viên trong nhóm chúng em đã phối hợp chặt chẽ: Bạn đảm nhiệm khối kiến trúc học sâu và ma trận đối đầu các mô hình, còn em tập trung vào kỹ nghệ tiền xử lý dữ liệu, kiểm soát nhiễu ảnh y tế và đóng gói sản phẩm lâm sàng phục vụ người dùng."

---

### 📄 SLIDE 03 — NỘI DUNG CHÍNH (AGENDA)
**TIÊU ĐỀ:** `CẤU TRÚC BÁO CÁO TỔNG THỂ`  
**4 TRỤ CỘT BÁO CÁO:**
1. **GIỚI THIỆU BÀI TOÁN & BỐI CẢNH Y TẾ** (Slide 04 – 06)
2. **DỮ LIỆU LÂM SÀNG & TIỀN XỬ LÝ ẢNH CỔ ĐIỂN** (Slide 07 – 14)
3. **MÔ HÌNH HỌC SÂU ĐỐI ĐẦU & THUẬT TOÁN** (Slide 15 – 34)
4. **KẾT QUẢ ĐẠT ĐƯỢC, XAI & TRIỂN KHAI ỨNG DỤNG** (Slide 35 – 43)

**🎙️ Script thuyết trình (Sinh viên 1 - 25 giây):**
> "Bài báo cáo hôm nay của chúng em được cấu trúc thành 4 phần logic chặt chẽ: Đi từ bài toán lâm sàng, giải pháp làm sạch dữ liệu X-quang, đến thế trận thực nghiệm đối đầu giữa 3 trường phái mô hình lớn nhất hiện nay, và cuối cùng là giải thích quyết định bằng XAI và demo ứng dụng thực tế."

---

### 📄 SLIDE 04 — TITLE DIVIDER 1
**TIÊU ĐỀ:** `PHẦN 1: GIỚI THIỆU BÀI TOÁN & BỐI CẢNH LÂM SÀNG`

---

### 📄 SLIDE 05 — BỐI CẢNH & TẦM QUAN TRỌNG
**TIÊU ĐỀ:** `TẦM QUAN TRỌNG CỦA ĐÁNH GIÁ TUỔI XƯƠNG TRONG NHI KHOA`  
**NỘI DUNG:**
- **Tuổi xương (Bone Age) khác với Tuổi khai sinh:** Phản ánh mức độ trưởng thành sinh lý thực sự của hệ cơ xương.
- **Vai trò chẩn đoán sống còn:**
  - Phát hiện sớm **Dậy thì sớm (Precocious Puberty):** Tuổi xương vượt trước tuổi đời $	o$ Đóng sụn sớm, trẻ bị thấp lùn vĩnh viễn.
  - Phát hiện **Chậm tăng trưởng thể chất (Growth Delay):** Tuổi xương tụt hậu do thiếu hormone tăng trưởng GH hoặc suy giáp $	o$ Cần can thiệp trong "giai đoạn vàng".
- **Áp lực lâm sàng:** Phương pháp thủ công (lật sách Greulich-Pyle Atlas hoặc chấm điểm Tanner-Whitehouse TW3) tốn 15–20 phút/ca, phụ thuộc cảm tính chủ quan, sai số giữa các bác sĩ lên tới 0.5 – 1.2 năm.

**🎙️ Script thuyết trình (Sinh viên 1 - 50 giây):**
> "Kính thưa Thầy Cô, trong y học nhi khoa, tuổi khai sinh không thể hiện được mức độ trưởng thành thực tế. Một đứa trẻ 8 tuổi có thể mang khung xương của một người 11 tuổi nếu bị dậy thì sớm, khiến các đĩa sụn đóng lại sớm và vĩnh viễn không thể cao thêm. Ngược lại, nếu trẻ bị thiếu hormone GH, tuổi xương sẽ bị tụt hậu. Hiện nay, việc lật sách so sánh thủ công tốn rất nhiều thời gian và có độ lệch chủ quan lớn giữa các bác sĩ. Một hệ thống AI định lượng chính xác trong vài mili-giây là nhu cầu cấp thiết của các bệnh viện nhi."

---

### 📄 SLIDE 06 — PHẠM VI & TIẾP CẬN ĐỀ TÀI
**TIÊU ĐỀ:** `PHẠM VI NGHIÊN CỨU & ĐỊNH NGHĨA BÀI TOÁN`  
**NỘI DUNG:**
- **Đối tượng:** Ảnh X-quang tư thế sau - trước (PA) bàn tay và cổ tay trái của trẻ từ 1 đến 228 tháng tuổi.
- **Tiếp cận Đột phá:** Định nghĩa bài toán là **HỒI QUY ĐA PHƯƠNG THỨC (MULTIMODAL REGRESSION)**.
  - Không tiếp cận dạng Phân loại (Classification) rời rạc vì tăng trưởng xương là quá trình sinh học liên tục.
  - Không chỉ dùng ảnh mà bắt buộc phải kết hợp biến **Giới tính lâm sàng** (vì bé gái cốt hóa xương sớm hơn bé trai 1.5 - 2 năm).

**🎙️ Script thuyết trình (Sinh viên 1 - 40 giây):**
> "Điểm sáng tạo cốt lõi của đề tài nằm ở việc định nghĩa bài toán dưới góc độ Hồi quy Đa phương thức. Vì sự phát triển của sụn là một hàm số liên tục biến thiên theo thời gian, và tốc độ cốt hóa của bé gái luôn đi trước bé trai từ 1.5 đến 2 năm, mô hình của chúng em tích hợp song song cả tín hiệu ảnh X-quang 2D và biến giới tính 1D để dự đoán trực tiếp một số thực là số tháng tuổi của bệnh nhi."

---

### 📄 SLIDE 07 — TITLE DIVIDER 2
**TIÊU ĐỀ:** `PHẦN 2: DỮ LIỆU LÂM SÀNG & TIỀN XỬ LÝ ẢNH CỔ ĐIỂN`

---

### 📄 SLIDE 08 — DỮ LIỆU X-RAY BÀN TAY: TIẾN TRÌNH CỐT HÓA
**TIÊU ĐỀ:** `TIẾN TRÌNH CỐT HÓA SINH HỌC TRÊN PHIM X-QUANG`  
**NỘI DUNG:**
- **Vùng 8 xương cổ tay (Carpals):** Xuất hiện tuần tự từ sơ sinh đến 7 tuổi (xương cả, xương móc $	o$ xương đậu).
- **Vùng đĩa sụn tiếp hợp (Epiphyseal Plates):** Nằm giữa chỏm xương và thân đốt ngón tay. Nở rộng ở tuổi dậy thì và khép kín hoàn toàn (hợp nhất xương) khi bước vào tuổi trưởng thành.
- **Nhiệm vụ của AI:** Phải học được sự biến thiên liên tục của khe sụn và độ đậm đặc cản quang của các hạt xương cổ tay.

**🎙️ Script thuyết trình (Sinh viên 1 - 45 giây):**
> "Trên phim X-quang bàn tay, hai vùng giải phẫu mang tính quyết định là cụm 8 xương cổ tay và các đĩa sụn tiếp hợp ở khớp đốt ngón tay. Ở trẻ sơ sinh, cổ tay chỉ là sụn trong suốt; theo thời gian, các hạt xương mới lần lượt xuất hiện và các đĩa sụn dần khép kín lại. Mô hình học sâu phải có năng lực phân giải được sự thay đổi kích thước milimét này qua từng độ tuổi."

---

### 📄 SLIDE 09 — BỘ DỮ LIỆU CHUẨN RSNA PEDIATRIC BONE AGE
**TIÊU ĐỀ:** `BỘ DỮ LIỆU Y TẾ THẬT RSNA BONE AGE CHALLENGE`  
**NỘI DUNG:**
- Nguồn: Hiệp hội Điện quang Bắc Mỹ (RSNA) đóng góp từ Stanford Children's Hospital và Children's Hospital Colorado.
- Quy mô: **12.611 ca bệnh thật** kèm đầy đủ ảnh X-quang, giới tính và tuổi xương chuẩn do hội đồng chuyên gia chẩn đoán.
- Phân phối tuổi: Từ 1 đến 228 tháng ($\mu = 127.32	ext{m} pprox 10.6$ tuổi, $\sigma = 41.18	ext{m}$).

**🎙️ Script thuyết trình (Sinh viên 1 - 35 giây):**
> "Nhóm sử dụng bộ dữ liệu chuẩn quốc tế RSNA gồm 12.611 ca bệnh thật. Dữ liệu trải dài từ trẻ sơ sinh 1 tháng tuổi đến thanh thiếu niên 19 tuổi, với tuổi trung bình là 10.6 tuổi, phản ánh trọn vẹn sự biến thiên sinh học của cộng đồng nhi khoa."

---

### 📄 SLIDE 10 — CƠ CẤU GIỚI TÍNH & PHÂN PHỐI LÂM SÀNG
**TIÊU ĐỀ:** `PHÂN TÍCH THỐNG KÊ LÂM SÀNG (CLINICAL EDA)`  
**NỘI DUNG (BIỂU ĐỒ ĐỐI CHỨNG):**
- Cơ cấu giới tính: **54.18% Nam (6.833 ca)** | **45.82% Nữ (5.778 ca)**.
- Phân phối độ tuổi đối xứng, tiệm cận phân phối chuẩn Gauss, đảm bảo tính đại diện cao cho thuật toán hồi quy.

**🎙️ Script thuyết trình (Sinh viên 1 - 30 giây):**
> "Kết quả khảo sát thống kê cho thấy tỷ lệ giới tính trong tập dữ liệu đạt mức cân bằng lý tưởng: 54% nam và 46% nữ. Đường cong phân bố tuổi xương có dạng hình chuông cân đối, tạo điều kiện thuận lợi để mô hình học không bị thiên lệch về một nhóm tuổi cục bộ."

---

### 📄 SLIDE 11 — PHÂN TẦNG DỮ LIỆU CỐ ĐỊNH CHỐNG RÒ RỈ
**TIÊU ĐỀ:** `CHIẾN LƯỢC PHÂN CHIA PHÂN TẦNG (STRATIFIED SPLIT 80/10/10)`  
**NỘI DUNG:**
- Không chia ngẫu nhiên (Random Split) để tránh rò rỉ phân phối.
- Phân tầng kết hợp 10 phân vị tuổi (Quantiles) $	imes$ Giới tính:
  - **Tập Huấn luyện (Train Set):** **10.088 ca (80.0%)**
  - **Tập Kiểm định (Val Set):** **1.261 ca (10.0%)**
  - **Tập Kiểm thử Độc lập (Test Set):** **1.262 ca (10.0%)**
- Đóng băng danh sách bệnh nhi vào tệp `train_stratified.csv` để cả 3 mô hình cùng được kiểm tra trên một tập dữ liệu chuẩn.

**🎙️ Script thuyết trình (Sinh viên 1 - 40 giây):**
> "Để đảm bảo tính trung thực tuyệt đối trong khoa học, nhóm không chia tập ngẫu nhiên mà thực hiện phân tầng cố định theo 10 phân vị tuổi kết hợp giới tính. Tập Test gồm đúng 1.262 ca bệnh được đóng băng hoàn toàn, đảm bảo cả 3 mô hình sau này đều phải vượt qua cùng một bài kiểm tra độc lập và công bằng."

---

### 📄 SLIDE 12 — THỐNG KÊ CHI TIẾT SỐ LƯỢNG MẪU THEO NHÓM TUỔI
**TIÊU ĐỀ:** `PHÂN BỔ BỆNH NHI THEO 4 GIAI ĐOẠN PHÁT TRIỂN`  
**BẢNG THỐNG KÊ LÂM SÀNG:**
- Nhũ nhi (< 3 tuổi): 782 ca (6.2%)
- Nhi đồng (3 – 8 tuổi): 2.415 ca (19.1%)
- Tiền dậy thì (8 – 12 tuổi): 4.120 ca (32.7%)
- Vị thành niên (12 – 19 tuổi): 5.294 ca (42.0%)

**🎙️ Script thuyết trình (Sinh viên 1 - 35 giây):**
> "Bảng số liệu cho thấy mật độ dữ liệu tập trung cao nhất ở giai đoạn tiền dậy thì và vị thành niên, chiếm gần 75% dữ liệu. Đây chính là giai đoạn các đĩa sụn có biến động mạnh nhất và cũng là nhóm đối tượng có nhu cầu thăm khám nội tiết cao nhất trong thực tế."

---

### 📄 SLIDE 13 — THÁCH THỨC CỦA DỮ LIỆU X-RAY NHI KHOA
**TIÊU ĐỀ:** `3 THÁCH THỨC QUANG HỌC LỚN TRÊN ẢNH X-QUANG GỐC`  
**NỘI DUNG:**
1. **Viền đen máy quét quá lớn:** Chiếm từ 30% đến 40% diện tích ảnh thô, làm lãng phí năng lực tính toán của mạng.
2. **Độ tương phản thấp:** Vùng đĩa sụn tiếp hợp bị chìm trong mô mềm, rất khó quan sát nếu không tăng cường sáng.
3. **Dị vật kim loại & Chữ L/R:** Chữ đánh dấu tay trái/phải cản quang mạnh, dễ khiến mạng bị bẫy học đường tắt (Shortcut Learning).

**🎙️ Script thuyết trình (Sinh viên 1 - 45 giây):**
> "Khi quan sát ảnh X-quang gốc, nhóm phát hiện 3 trở ngại kỹ thuật lớn: Thứ nhất, viền đen máy quét chiếm gần một nửa khung hình. Thứ hai, các đĩa sụn tiếp hợp rất mờ do cản quang kém. Thứ ba, các ký hiệu kim loại chữ L hoặc R có độ sáng rất gắt, nếu không xử lý, mô hình sẽ học 'đường tắt' vào chữ kim loại thay vì nhìn vào sụn xương."

---

### 📄 SLIDE 14 — PIPELINE TIỀN XỬ LÝ ẢNH CỔ ĐIỂN 5 BƯỚC
**TIÊU ĐỀ:** `PIPELINE CHUẨN HÓA THỊ GIÁC CỔ ĐIỂN (CLASSICAL CV)`  
**DÃI 5 BƯỚC XỬ LÝ THỰC TẾ:**
`Ảnh Thô` $	o$ `1. CLAHE (clip=3.0)` $	o$ `2. Gauss 5x5` $	o$ `3. Otsu Auto` $	o$ `4. Morphology Open/Close` $	o$ `5. Bounding Box Crop (512x512)`.
- Kết quả: Xóa sạch chữ L/R, cắt sát bàn tay kèm 2% viền an toàn, làm nổi rõ từng khe sụn khớp ngón.

**🎙️ Script thuyết trình (Sinh viên 1 - 50 giây):**
> "Để khắc phục triệt để các thách thức trên, nhóm xây dựng pipeline tiền xử lý 5 bước: Dùng CLAHE cân bằng sáng cục bộ, lọc Gauss khử nhiễu lượng tử, thuật toán Otsu nhị phân hóa tách bàn tay, phép toán hình thái học xóa tan chữ kim loại, và thuật toán tìm đường bao lớn nhất để cắt đúng vùng bàn tay rồi đưa về chuẩn 512x512. Toàn bộ 12.611 ảnh sạch được xuất sẵn làm bộ đệm cache, giúp việc huấn luyện sau này diễn ra với tốc độ tối đa."

---

### 📄 SLIDE 15 — TITLE DIVIDER 3
**TIÊU ĐỀ:** `PHẦN 3: MÔ HÌNH HỌC SÂU ĐỐI ĐẦU & THUẬT TOÁN`

---

### 📄 SLIDE 16 — QUY TRÌNH HỆ THỐNG TỔNG THỂ (PIPELINE ARCHITECTURE)
**TIÊU ĐỀ:** `SƠ ĐỒ KHỐI VẬN HÀNH HỆ THỐNG ĐA PHƯƠNG THỨC`  
**SƠ ĐỒ CHỮ Y:**
- Nhánh Trái: Ảnh sạch $512 	imes 512 	imes 3 	o$ Visual Backbone (Trích xuất vector $D$ chiều).
- Nhánh Phải: Giới tính $1	ext{D} 	o$ Gender MLP (Chiếu lên vector 32 chiều).
- Trung tâm: Late Fusion ghép nối $[D \,\|\, 32] 	o$ Hierarchical Regression Head 3 tầng $	o$ Tuổi xương dự đoán $\hat{y}$ (tháng).

**🎙️ Script thuyết trình (Sinh viên 2 - 50 giây):**
> "Kính thưa Thầy Cô, từ phần này em xin phép trình bày về thiết kế học sâu của hệ thống. Chúng em tiếp cận theo mô hình phân nhánh hình chữ Y: Nhánh thị giác sử dụng các backbone sâu để trích xuất đặc trưng hình thái xương; nhánh lâm sàng sử dụng mạng MLP nâng biến giới tính lên 32 chiều. Hai dòng thông tin này hợp nhất tại tầng Late Fusion trước khi đi qua đầu hồi quy nén dần 3 bậc để xuất ra số tháng tuổi dự đoán."

---

### 📄 SLIDE 17 — GIỚI THIỆU MÔ HÌNH 1: RESNET-50 MULTIMODAL
**TIÊU ĐỀ:** `MÔ HÌNH 1: RESIDUAL BOTTLENECK CNN (RESNET-50)`  
**NỘI DUNG:**
- Trường phái: Mạng tích chập phần dư kinh điển (He et al., 2015).
- Cơ chế cốt lõi: Residual Skip Connections ($\mathbf{y} = \mathcal{F}(\mathbf{x}) + \mathbf{x}$) giúp dòng gradient truyền thẳng, triệt tiêu hiện tượng tiêu biến đạo hàm.
- Tổng tham số: **26.17 triệu tham số**.
- Vector đặc trưng thị giác xuất ra từ tầng Global Average Pooling: **2.048 chiều**.

**🎙️ Script thuyết trình (Sinh viên 2 - 40 giây):**
> "Đại diện đầu tiên trong thế trận thực nghiệm là ResNet-50. Đây là kiến trúc CNN chuẩn mực nhất trong thị giác máy tính với cấu trúc kết nối tắt phần dư Residual Skip Connections, tạo ra bề mặt mất mát cực kỳ ổn định. Khối Bottleneck cuối cùng trích xuất vector đặc trưng không gian 2.048 chiều rất giàu ngữ nghĩa."

---

### 📄 SLIDE 18 — ĐẶC ĐIỂM KIẾN TRÚC RESNET-50 & LỢI ÍCH
**TIÊU ĐỀ:** `TẠI SAO RESNET-50 LÀ "ĐIỂM RƠI VÀNG" (SWEET SPOT)?`  
**BẢNG SO SÁNH NỘI BỘ DÒNG RESNET:**
- ResNet-18/34: Chỉ có 512 chiều đặc trưng, quá nông cho sụn tiếp hợp.
- **ResNet-50:** Khối Bottleneck ($1	imes1 	o 3	imes3 	o 1	imes1$), 2048D, 25.6M tham số, vừa vặn hoàn hảo với 10.000 ảnh.
- ResNet-101/152: 44.5M – 60.2M tham số, quá nặng, dễ bị Overfitting trên tập dữ liệu y tế cỡ vừa.

**🎙️ Script thuyết trình (Sinh viên 2 - 40 giây):**
> "Một câu hỏi thường gặp là: Tại sao không dùng ResNet-18 hay ResNet-152? Nghiên cứu của chúng em chỉ ra rằng ResNet-18 với 512 chiều là quá nông cho các khe sụn nhỏ; trong khi ResNet-152 với hơn 60 triệu tham số lại bị thừa năng lực và dễ bị học vẹt trên tập 10.000 ảnh. ResNet-50 chính là điểm rơi vàng giữa khả năng biểu diễn và tính khái quát hóa."

---

### 📄 SLIDE 19 — CẤU HÌNH HUẤN LUYỆN RESNET-50
**TIÊU ĐỀ:** `THIẾT LẬP THỰC NGHIỆM HUẤN LUYỆN RESNET-50`  
**THÔNG SỐ HUẤN LUYỆN (CELL 16 NOTEBOOK):**
- Phần cứng: GPU NVIDIA Tesla T4 (14.56 GB VRAM) trên Google Colab.
- Batch Size: 32 | Số Epochs: 15 vòng lặp.
- Hàm mất mát: Smooth L1 (Huber Loss, $\delta = 1.0$) kháng ngoại lai.
- Bộ tối ưu: AdamW ($lr = 1	ext{e-}4$, weight decay = $1	ext{e-}4$).
- Điều lịch học: CosineAnnealingLR ($T_{\max} = 15$) + Mixed Precision (AMP FP16).

**🎙️ Script thuyết trình (Sinh viên 2 - 35 giây):**
> "Mô hình được huấn luyện trên GPU Tesla T4 với 15 Epochs, sử dụng bộ tối ưu AdamW kết hợp lịch hạ tốc độ học theo hàm Cosine. Điểm nhấn là việc áp dụng hàm mất mát Huber Loss để chặn hiện tượng bùng nổ gradient từ các ca bệnh đột biến, và kỹ thuật AMP FP16 giúp tiết kiệm 50% bộ nhớ GPU."

---

### 📄 SLIDE 20 — ĐỘNG HỌC HUẤN LUYỆN RESNET-50
**TIÊU ĐỀ:** `KẾT QUẢ ĐỘNG HỌC HUẤN LUYỆN RESNET-50`  
**ĐƯỜNG CONG THỰC NGHIỆM:**
- Thời gian chạy: **202.1 phút (~3.37 giờ)** (~805s/epoch).
- Động học hội tụ:
  - Epoch 01: $	ext{Val MAE} = 111.43$ tháng.
  - Epoch 05: $	ext{Val MAE} = 12.77$ tháng (lao dốc ngoạn mục nhờ ImageNet pre-training).
  - Epoch 13: Đạt điểm tối ưu **$	ext{Val MAE} = 7.25	ext{ tháng}$ (~0.60 năm)** $	o$ Lưu `checkpoint_best.pth`.

**🎙️ Script thuyết trình (Sinh viên 2 - 45 giây):**
> "Trên màn hình là đồ thị huấn luyện thực tế từ tệp log. Nhờ sức mạnh của bộ trọng số tiền huấn luyện ImageNet, sai số Val MAE giảm cực nhanh từ 111 tháng ở vòng 1 xuống chỉ còn 12 tháng ở vòng 5. Tại vòng thứ 13, mô hình đạt độ chính xác kỷ lục với sai số chỉ 7.25 tháng và kích hoạt lưu giữ checkpoint tốt nhất."

---

### 📄 SLIDE 21 — KẾT QUẢ KIỂM THỬ ĐỘC LẬP RESNET-50
**TIÊU ĐỀ:** `ĐÁNH GIÁ TRÊN TẬP TEST ĐỘC LẬP (1.262 BỆNH NHI)`  
**BẢNG CHỈ SỐ TEST THỰC TẾ:**
- **MAE (Sai số tuyệt đối trung bình):** **$7.38	ext{ tháng}$ (~0.615 năm)**.
- **RMSE (Căn bậc hai sai số toàn phương):** **$9.60	ext{ tháng}$**.
- **Hệ số xác định $R^2$ Score:** **$0.9452$ ($94.52\%$)**.
- **Độ an toàn lâm sàng $\le 12$ tháng:** **$81.38\%$**.

**🎙️ Script thuyết trình (Sinh viên 2 - 40 giây):**
> "Khi đưa mô hình ra kiểm tra trên 1.262 ca bệnh độc lập mà mô hình chưa từng thấy trong lúc học, kết quả đạt được vô cùng ấn tượng: Sai số trung bình MAE chỉ là 7.38 tháng, tương đương 0.61 năm; hệ số R² đạt 94.52%, và hơn 81% ca bệnh có sai số nằm hoàn toàn trong giới hạn an toàn 1 năm của y khoa."

---

### 📄 SLIDE 22 — PHÂN TÍCH PHẦN DƯ SAI SỐ RESNET-50
**TIÊU ĐỀ:** `PHÂN TÍCH PHÂN BỐ PHẦN DƯ SAI SỐ (RESIDUAL ANALYSIS)`  
**NỘI DUNG ĐỒ THỊ:**
- Đồ thị Scatter Plot: Các điểm dữ liệu bám sát đường chéo $45^\circ$, nằm gọn trong dải hành lang an toàn $\pm 12$ tháng.
- Đồ thị Phần dư: Phân phối đối xứng hoàn hảo quanh điểm 0, chứng minh mô hình không bị lệch (unbiased) về phía đoán già hơn hay non hơn.

**🎙️ Script thuyết trình (Sinh viên 2 - 35 giây):**
> "Biểu đồ phân tán cho thấy các điểm chẩn đoán phân bố rất đồng đều dọc theo đường chéo lý tưởng 45 độ. Biểu đồ phần dư đối xứng hoàn hảo quanh trục số 0, chứng minh mô hình không hề bị lệch thiên kiến về việc đoán già hơn hay đoán non hơn tuổi thực."

---

### 📄 SLIDE 23 — GIỚI THIỆU MÔ HÌNH 2: CONVNEXT-V2-TINY
**TIÊU ĐỀ:** `MÔ HÌNH 2: MODERN PURE CNN (CONVNEXT-V2)`  
**NỘI DUNG:**
- Trường phái: Mạng CNN thuần hiện đại (Meta AI, Woo et al., 2023).
- Triết lý thiết kế: Tái cấu trúc tích chập theo chuẩn Transformer.
- Tổng tham số: **28.58 triệu tham số**.
- Vector đặc trưng xuất ra: **768 chiều**.

**🎙️ Script thuyết trình (Sinh viên 2 - 35 giây):**
> "Đại diện thứ hai trong thế trận đối đầu là ConvNeXt-V2-Tiny. Đây là đỉnh cao của kiến trúc CNN hiện đại do Meta AI công bố, được thiết kế lại toàn diện để sở hữu tầm nhìn rộng của Transformer nhưng vẫn giữ được tốc độ và tính ổn định của mạng tích chập."

---

### 📄 SLIDE 24 — ĐẶC ĐIỂM KIẾN TRÚC CONVNEXT & LỢI ÍCH
**TIÊU ĐỀ:** `3 ĐỘT PHÁ CỦA CONVNEXT TRONG PHÂN TÍCH X-RAY`  
**NỘI DUNG:**
1. **Bộ lọc tích chập lớn $7 	imes 7$ (Depthwise Separable):** Mở rộng trường tiếp nhận (Receptive Field) bắt trọn toàn bộ cấu trúc bàn tay.
2. **Khối Nghịch đảo Cổ chai (Inverted Bottleneck):** Mở rộng số kênh $C 	o 4C 	o C$ giúp giữ lại các chi tiết sụn tinh vi.
3. **Chuẩn hóa Phản hồi Toàn cục (GRN):** Chống hiện tượng bão hòa kênh đặc trưng.

**🎙️ Script thuyết trình (Sinh viên 2 - 40 giây):**
> "ConvNeXt mang đến 3 cải tiến vượt bậc: Bộ lọc 7x7 giúp mở rộng tầm nhìn không gian; cấu trúc nghịch đảo cổ chai giúp bảo tồn các nếp gấp sụn siêu nhỏ; và tầng chuẩn hóa GRN giúp ngăn ngừa hiện tượng bão hòa kênh, giúp gradient lưu thông mạnh mẽ hơn."

---

### 📄 SLIDE 25 — CẤU HÌNH HUẤN LUYỆN CONVNEXT-TINY
**TIÊU ĐỀ:** `CẤU HÌNH HUẤN LUYỆN CONVNEXT-TINY`  
**THÔNG SỐ:**
- Batch Size: 32 | Epochs: 20 vòng lặp | Optimizer: AdamW ($lr = 1	ext{e-}4$).
- Regularization: Stochastic Depth (Drop Path Rate = 0.1) chống học vẹt.
- Late Fusion: $768	ext{D (Ảnh)} + 32	ext{D (Giới tính)} 	o 800	ext{D} 	o$ Regression Head.

**🎙️ Script thuyết trình (Sinh viên 2 - 30 giây):**
> "Với ConvNeXt, chúng em bổ sung thêm cơ chế Stochastic Depth để ngắt ngẫu nhiên một số đường dẫn trong quá trình train nhằm chống Overfitting, và ghép nối vector 768 chiều với nhánh giới tính 32 chiều thành vector 800 chiều."

---

### 📄 SLIDE 26 — KẾT QUẢ HUẤN LUYỆN CONVNEXT-TINY
**TIÊU ĐỀ:** `ĐỘNG HỌC HỘI TỤ CỦA CONVNEXT-TINY`  
**NỘI DUNG:**
- Đường cong Loss suy giảm mượt mà và sâu hơn ResNet-50.
- Điểm tối ưu: $	ext{Val MAE} = 6.35	ext{ tháng}$ tại Epoch 17.

**🎙️ Script thuyết trình (Sinh viên 2 - 30 giây):**
> "Nhờ các khối chuẩn hóa hiện đại, đường cong hàm mất mát của ConvNeXt hội tụ êm mượt hơn rõ rệt và đạt mức sai số kiểm định tối ưu 6.35 tháng, vượt trội hơn so với ResNet-50."

---

### 📄 SLIDE 27 — KẾT QUẢ KIỂM THỬ CONVNEXT-TINY
**TIÊU ĐỀ:** `KIỂM THỬ CONVNEXT-TINY TRÊN TẬP TEST (1.262 CA)`  
**CHỈ SỐ TEST SET:**
- **MAE:** **$6.42	ext{ tháng}$ (~0.535 năm)** — Giảm gần 1 tháng so với ResNet-50.
- **RMSE:** **$8.45	ext{ tháng}$**.
- **$R^2$ Score:** **$0.9578$ ($95.78\%$)**.
- **Độ an toàn lâm sàng $\le 12$ tháng:** **$86.45\%$**.

**🎙️ Script thuyết trình (Sinh viên 2 - 35 giây):**
> "Trên tập Test độc lập, ConvNeXt-Tiny đã rút ngắn sai số MAE xuống chỉ còn 6.42 tháng, tức khoảng nửa năm. Hệ số tương quan R² nâng lên 95.78% và tỷ lệ ca bệnh an toàn đạt mức 86.45%."

---

### 📄 SLIDE 28 — SO SÁNH NỘI BỘ: CONVNEXT VS RESNET-50
**TIÊU ĐỀ:** `BƯỚC TIẾN CỦA CONVNEXT SO VỚI RESNET-50`  
**BẢNG ĐỐI CHIẾU:**
- MAE giảm từ $7.38	ext{m} 	o 6.42	ext{m}$ (Cải thiện **$13.0\%$**).
- RMSE giảm từ $9.60	ext{m} 	o 8.45	ext{m}$ (Cải thiện **$12.0\%$**).
- Tốc độ suy luận duy trì mức cực nhanh: **$55.0	ext{ FPS}$**.

**🎙️ Script thuyết trình (Sinh viên 2 - 30 giây):**
> "So với ResNet-50, ConvNeXt cải thiện độ chính xác tới 13% mà vẫn giữ được tốc độ phản hồi cực nhanh 55 khung hình/giây, chứng minh tính ưu việt của tích chập hiện đại."

---

### 📄 SLIDE 29 — GIỚI THIỆU MÔ HÌNH 3: SWIN TRANSFORMER V2 (SWIN-T)
**TIÊU ĐỀ:** `MÔ HÌNH 3: HIERARCHICAL VISION TRANSFORMER (SWIN-T)`  
**NỘI DUNG:**
- Trường phái: Vision Transformer phân cấp (ICCV Best Paper, Liu et al., 2021).
- Cơ chế đột phá: Tự chú ý theo cửa sổ trượt (Shifted Window Self-Attention).
- Tổng tham số: **28.32 triệu tham số**.
- Vector đặc trưng xuất ra: **768 chiều**.

**🎙️ Script thuyết trình (Sinh viên 2 - 40 giây):**
> "Mô hình thứ 3 đại diện cho trường phái Vision Transformer tối tân: Swin Transformer v2. Swin-T phá bỏ giới hạn tính toán của ViT truyền thống bằng cách tính toán Attention bên trong các cửa sổ cục bộ và dịch chuyển cửa sổ giữa các tầng để nắm bắt ngữ cảnh toàn cục."

---

### 📄 SLIDE 30 — ĐẶC ĐIỂM KIẾN TRÚC SWIN-T & LỢI ÍCH
**TIÊU ĐỀ:** `SỨC MẠNH CỦA CƠ CHẾ ATTENTION THEO CỬA SỔ TRƯỢT`  
**NỘI DUNG:**
- **Local Window Attention:** Tính toán tập trung trong cửa sổ $8 	imes 8$, bắt trọn vi cấu trúc của từng đốt ngón tay.
- **Shifted Window Attention:** Dịch chuyển cửa sổ nửa bước, thiết lập mối liên kết ngữ nghĩa giữa **xương cổ tay** và **các ngón tay** ở khoảng cách xa.

**🎙️ Script thuyết trình (Sinh viên 2 - 40 giây):**
> "Cơ chế cửa sổ trượt mang lại lợi thế độc nhất: Nó vừa nhìn rõ từng khe sụn nhỏ trong ô 8x8, vừa liên kết được mối tương quan giữa sự cốt hóa ở cổ tay với sự khép sụn ở ngón tay xa, tạo nên khả năng lập luận không gian toàn diện."

---

### 📄 SLIDE 31 — CẤU HÌNH HUẤN LUYỆN SWIN-T
**TIÊU ĐỀ:** `CẤU HÌNH HUẤN LUYỆN SWIN-T`  
**THÔNG SỐ:**
- Patch Size: $4 	imes 4$ | Window Size: $8 	imes 8$ (Tương thích hoàn hảo ảnh $512 	imes 512$).
- Optimizer: AdamW ($lr = 5	ext{e-}5$, weight decay = $0.05$).
- Cosine Annealing 20 Epochs kèm Warm-up 2 Epochs đầu.

**🎙️ Script thuyết trình (Sinh viên 2 - 30 giây):**
> "Với Swin-T, chúng em sử dụng kích thước cửa sổ 8x8 tương thích chuẩn với ảnh 512x512, áp dụng tốc độ học 5e-5 kèm 2 epoch khởi động warm-up để bảo vệ trọng số attention."

---

### 📄 SLIDE 32 — KẾT QUẢ HUẤN LUYỆN SWIN-T
**TIÊU ĐỀ:** `ĐỘNG HỌC HỘI TỤ CỦA SWIN-T`  
**NỘI DUNG:**
- Val MAE hội tụ về mốc tối ưu: **$6.08	ext{ tháng}$** tại Epoch 18.
- Tiêu tốn VRAM cao hơn ~40% so với ResNet-50.

**🎙️ Script thuyết trình (Sinh viên 2 - 30 giây):**
> "Quá trình huấn luyện Swin-T đòi hỏi nhiều bộ nhớ GPU hơn, nhưng đền đáp lại bằng một đường cong hội tụ sâu nhất, đưa sai số kiểm định xuống chỉ còn 6.08 tháng."

---

### 📄 SLIDE 33 — KẾT QUẢ KIỂM THỬ ĐỘC LẬP SWIN-T
**TIÊU ĐỀ:** `KIỂM THỬ SWIN-T TRÊN TẬP TEST (1.262 CA)`  
**CHỈ SỐ TEST SET:**
- **MAE:** **$6.15	ext{ tháng}$ (~0.512 năm)** — Kỷ lục sai số thấp nhất.
- **RMSE:** **$8.12	ext{ tháng}$**.
- **$R^2$ Score:** **$0.9610$ ($96.10\%$)**.
- **Độ an toàn lâm sàng $\le 12$ tháng:** **$88.20\%$**.

**🎙️ Script thuyết trình (Sinh viên 2 - 35 giây):**
> "Kết quả kiểm thử khẳng định vị thế dẫn đầu về độ chính xác của Swin-T: MAE chỉ còn 6.15 tháng, tương đương 0.51 năm; độ giải thích phương sai R² đạt 96.1% và gần 90% ca bệnh nằm trong ngưỡng an toàn."

---

### 📄 SLIDE 34 — PHÂN TÍCH KIỂM THỬ SWIN-T
**TIÊU ĐỀ:** `PHÂN TÍCH CHI TIẾT ĐỘ CHÍNH XÁC SWIN-T`  
**NỘI DUNG:**
- Đạt độ chính xác trong hạn 6 tháng ($\le 6	ext{m}$) lên tới **$61.10\%$**.
- Giảm thiểu triệt để các ca sai số lớn ở nhóm tuổi vị thành niên.

**🎙️ Script thuyết trình (Sinh viên 2 - 30 giây):**
> "Hơn 61% bệnh nhi được Swin-T dự đoán chính xác trong biên độ nửa năm, đặc biệt mô hình cải thiện vượt bậc ở nhóm trẻ lớn tuổi nhờ khả năng phân tích sự khép kín của đĩa sụn."

---

### 📄 SLIDE 35 — TITLE DIVIDER 4
**TIÊU ĐỀ:** `PHẦN 4: SO SÁNH 3 MÔ HÌNH, XAI & TRIỂN KHAI ỨNG DỤNG`

---

### 📄 SLIDE 36 — BẢNG SO SÁNH ĐỐI ĐẦU TOÀN DIỆN 3 MÔ HÌNH
**TIÊU ĐỀ:** `MA TRẬN ĐỐI SÁNH ĐA TIÊU CHÍ (TRI-MODEL COMPARATIVE MATRIX)`  
**BẢNG ĐỐI ĐẦU CHUẨN:**
| Tiêu Chí Đánh Giá | M1: ResNet-50 | M2: ConvNeXt-Tiny | M3: Swin-T | Mô Hình Tối Ưu |
|:---|:---:|:---:|:---:|:---:|
| **Trường phái** | Residual CNN | Modern Pure CNN | Vision Transformer | -- |
| **Số tham số** | **26.17 M** | 28.58 M | 28.32 M | ResNet-50 (Nhẹ nhất) |
| **Kích thước file** | **98.4 MB** | 109.2 MB | 108.5 MB | ResNet-50 (Gọn nhất) |
| **Test MAE (tháng)**| 7.38 m | 6.42 m | **6.15 m** | **Swin-T (-16.7%)** |
| **Test RMSE (tháng)**| 9.60 m | 8.45 m | **8.12 m** | **Swin-T (-15.4%)** |
| **Hệ số $R^2$** | 0.9452 | 0.9578 | **0.9610** | **Swin-T (Cao nhất)** |
| **Chính xác $\le 12$m**| 81.38% | 86.45% | **88.20%** | **Swin-T (+6.82%)** |
| **Tốc độ thông lượng**| **67.5 FPS** | 55.0 FPS | 37.7 FPS | ResNet-50 (Nhanh nhất)|

**🎙️ Script thuyết trình (Sinh viên 2 - 60 giây):**
> "Kính thưa Hội đồng, đây là bảng tổng kết đối đầu toàn diện giữa 3 trường phái. Nếu xét thuần túy về độ chính xác học thuật, Swin Transformer v2 là quán quân với MAE đạt 6.15 tháng và R² đạt 96.1%. Tuy nhiên, nếu xét về tính ứng dụng và tốc độ phản hồi lâm sàng, ResNet-50 và ConvNeXt-Tiny lại chiếm ưu thế với kích thước tệp nhẹ hơn và tốc độ xử lý nhanh hơn từ 1.5 đến gần 2 lần."

---

### 📄 SLIDE 37 — MÔ HÌNH LỰA CHỌN & PHÂN TÍCH ĐÁNH ĐỔI (TRADE-OFF)
**TIÊU ĐỀ:** `LUẬN GIẢI MÔ HÌNH TỐI ƯU CHO TRIỂN KHAI PHÒNG KHÁM`  
**KẾT LUẬN LỰA CHỌN:**
- **Trong nghiên cứu học thuật:** Chọn **Swin-T** để tối đa hóa độ chính xác ($MAE = 6.15	ext{m}$).
- **Trong triển khai thực tế tại bệnh viện tuyến cơ sở:** Chọn **ConvNeXt-Tiny / ResNet-50** vì có thể chạy mượt mà ngay trên CPU máy trạm thông thường, không đòi hỏi trang bị card đồ họa đắt tiền.

**🎙️ Script thuyết trình (Sinh viên 2 - 40 giây):**
> "Từ bài toán đánh đổi giữa độ chính xác và chi phí phần cứng, nhóm đề xuất giải pháp triển khai linh hoạt: Sử dụng Swin-T cho các trung tâm nghiên cứu y khoa lớn; và đóng gói ConvNeXt hoặc ResNet-50 cho các bệnh viện tuyến cơ sở để các bác sĩ có thể chạy chẩn đoán mượt mà trên chính máy tính văn phòng sẵn có."

---

### 📄 SLIDE 38 — MINH BẠCH HÓA Y TẾ: REGRESSION GRAD-CAM
**TIÊU ĐỀ:** `TRÍ TUỆ NHÂN TẠO CÓ THỂ GIẢI THÍCH (EXPLAINABLE AI)`  
**NGUYÊN LÝ GRAD-CAM:**
- Móc nối (Hook) vào tầng tích chập cuối cùng để lấy đạo hàm riêng của tuổi xương $\hat{y}$ theo từng feature map: $lpha_k = rac{1}{Z} \sum rac{\partial \hat{y}}{\partial A^k}$.
- Tạo bản đồ nhiệt Heatmap trực quan hóa vùng mô hình "nhìn vào".

**🎙️ Script thuyết trình (Sinh viên 1 - 40 giây):**
> "Để mô hình không phải là một 'hộp đen' bí ẩn đối với các bác sĩ, chúng em phát triển thuật toán Regression Grad-CAM. Thuật toán tính toán đạo hàm ngược từ số tháng tuổi dự đoán về bản đồ đặc trưng cuối cùng, xuất ra bản đồ nhiệt chỉ rõ vùng giải phẫu nào đang chi phối quyết định của AI."

---

### 📄 SLIDE 39 — ĐỐI CHIẾU GRAD-CAM THỰC TẾ TRÊN BỆNH NHI
**TIÊU ĐỀ:** `KIỂM CHỨNG GIẢI PHẪU HỌC TRÊN PHIM X-RAY THẬT`  
**HÌNH ẢNH 3 PANEL:** `Ảnh Gốc` $\longleftrightarrow$ `Heatmap Grad-CAM` $\longleftrightarrow$ `Lớp Phủ Overlay`.
- Vùng kích hoạt đỏ rực tập trung vào **8 xương cổ tay** và **đĩa sụn đốt ngón tay**.
- Vùng viền đen và chữ kim loại hoàn toàn không có tín hiệu kích hoạt $	o$ Minh chứng loại bỏ 100% bẫy học đường tắt.

**🎙️ Script thuyết trình (Sinh viên 1 - 45 giây):**
> "Quan sát hình ảnh kiểm chứng thực tế, Thầy Cô có thể thấy vùng màu đỏ kích hoạt cực đại tập trung chính xác vào khối 8 xương cổ tay và các chỏm sụn tiếp hợp ngón tay. Các góc ảnh chứa viền đen và ký tự kim loại hoàn toàn không có màu, chứng minh AI đã học đúng kiến thức giải phẫu học chứ không học vẹt các nhiễu nền bên ngoài."

---

### 📄 SLIDE 40 — HẬU XỬ LÝ LÂM SÀNG & CẢNH BÁO LỆCH CHUẨN WHO
**TIÊU ĐỀ:** `CƠ CHẾ CẢNH BÁO LÂM SÀNG NỘI TIẾT TỰ ĐỘNG`  
**QUY TẮC CẢNH BÁO LÂM SÀNG:**
- $\Delta = 	ext{Tuổi xương (AI)} - 	ext{Tuổi thực (Khai sinh)}$.
- 🟢 **$|\Delta| \le 12$ tháng:** Bình thường (Normal Development).
- 🔴 **$\Delta > +12$ tháng:** Cảnh báo dậy thì sớm $	o$ Khuyến nghị đo hormone LH, FSH.
- 🟡 **$\Delta < -12$ tháng:** Cảnh báo chậm tăng trưởng / suy giáp $	o$ Khuyến nghị đo hormone GH, IGF-1.

**🎙️ Script thuyết trình (Sinh viên 1 - 45 giây):**
> "Kết quả tuổi xương dự đoán được tự động đưa qua module phân tích hậu xử lý. Bằng cách tính độ lệch Delta so với tuổi khai sinh, hệ thống tự động gán nhãn cảnh báo: Nếu lệch trên 1 năm về phía già hơn, hệ thống cảnh báo nguy cơ dậy thì sớm và gợi ý xét nghiệm hormone sinh dục; nếu lệch về phía non hơn, hệ thống cảnh báo nguy cơ thiếu hormone tăng trưởng để bác sĩ kịp thời can thiệp."

---

### 📄 SLIDE 41 — DEMO ỨNG DỤNG LÂM SÀNG (STREAMLIT WEBAPP)
**TIÊU ĐỀ:** `GIAO DIỆN HỆ THỐNG HỖ TRỢ RA QUYẾT ĐỊNH (CDSS DEMO)`  
**CÁC TÍNH NĂNG TRÊN GIAO DIỆN:**
1. Kéo thả ảnh X-quang và chọn giới tính bệnh nhi.
2. Tự động tiền xử lý và suy luận thời gian thực trong 15ms.
3. Xuất thẻ chẩn đoán lâm sàng, độ lệch $\Delta$, và bản đồ nhiệt Grad-CAM kiểm tra chéo.

**🎙️ Script thuyết trình (Sinh viên 1 - 45 giây):**
> "Toàn bộ giải pháp đã được chúng em đóng gói thành ứng dụng WebApp tương tác thời gian thực. Bác sĩ chỉ cần kéo thả bức ảnh X-quang và nhập thông tin cơ bản, hệ thống sẽ tự động cắt ảnh, trả về kết quả dự đoán, bản đồ nhiệt giải thích và phiếu kết luận lâm sàng chỉ trong tích tắc."

---

### 📄 SLIDE 42 — ĐÁNH GIÁ HẠN CHẾ & HƯỚNG PHÁT TRIỂN
**TIÊU ĐỀ:** `ĐÁNH GIÁ HẠN CHẾ & HƯỚNG MỞ RỘNG ĐỀ TÀI`  
**NỘI DUNG:**
- **Hạn chế:** Dữ liệu RSNA chủ yếu là trẻ em Bắc Mỹ; chưa tích hợp thêm chỉ số chiều cao cha mẹ và BMI.
- **Hướng phát triển:** 
  1. Hợp tác thu thập thêm dữ liệu trẻ em Việt Nam để tinh chỉnh mô hình thích nghi thể tạng địa phương.
  2. Ứng dụng mô hình phân tách 2 vùng (Dual-ROI Fusion với YOLOv8) để khai thác sâu hơn nữa các đĩa sụn siêu nhỏ.
  3. Đóng gói Docker Container chuẩn DICOM/PACS nhúng vào hệ thống bệnh viện.

**🎙️ Script thuyết trình (Sinh viên 2 - 40 giây):**
> "Về hướng phát triển tương lai, nhóm đặt mục tiêu mở rộng tập dữ liệu trên trẻ em Việt Nam, đồng thời kết hợp thêm mô hình Object Detection để cắt riêng vùng ngón tay và vùng cổ tay nhằm tiếp tục hạ thấp sai số, hướng tới việc tích hợp chính thức vào hệ thống quản lý bệnh viện PACS."

---

### 📄 SLIDE 43 — KẾT LUẬN & LỜI CẢM ƠN (THANK YOU)
**TIÊU ĐỀ:** `KẾT LUẬN & TRÂN TRỌNG CẢM ƠN`  
**TỔNG KẾT THÀNH TỰU:**
- Hoàn thành trọn vẹn pipeline AI y tế từ tiền xử lý Classical CV đến mô hình đa phương thức.
- Xây dựng thành công ma trận 3 mô hình đối đầu với độ chính xác cao ($MAE = 6.15 - 7.38	ext{m}$, $R^2 > 0.945$).
- Đóng gói ứng dụng chẩn đoán minh bạch hỗ trợ y tế cộng đồng.

**🎙️ Script thuyết trình (Cả hai sinh viên - 30 giây):**
> "Đề tài của chúng em đã chứng minh tiềm năng to lớn của Trí tuệ Nhân tạo trong việc đồng hành và hỗ trợ các y bác sĩ nâng cao chất lượng chăm sóc sức khỏe trẻ em. Chúng em xin trân trọng cảm ơn Thầy Cô trong Hội đồng đã chú ý lắng nghe và rất mong nhận được những ý kiến đóng góp quý báu từ Thầy Cô!"
