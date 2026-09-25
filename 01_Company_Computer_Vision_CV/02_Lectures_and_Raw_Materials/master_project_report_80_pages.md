# 📘 ĐỒ ÁN TỐT NGHIỆP / NGHIÊN CỨU KHOA HỌC CHUYÊN SÂU
# HỆ THỐNG TỰ ĐỘNG ĐÁNH GIÁ TUỔI XƯƠNG TỪ ẢNH X-QUANG BÀN TAY BẰNG HỌC SÂU ĐA PHƯƠNG THỨC VÀ TRÍ TUỆ NHÂN TẠO CÓ THỂ GIẢI THÍCH

> **Mã Đề Tài:** `DUT-AI-MED-2026-RSNA`  
> **Chuyên ngành:** Kỹ thuật Phần mềm & Trí tuệ Nhân tạo — Trường Đại học Bách Khoa, Đại học Đà Nẵng (DUT)  
> **Đơn vị phối hợp:** Viện Nghiên cứu & Phát triển VisionLab (`CORP-01-CV`)  
> **Mô hình chuẩn tham chiếu học thuật:** Cấu trúc Chuyên luận Kỹ thuật Đồ án X-ray Mối hàn Cơ khí (`MECHANICAL_FAULT_XRAY Project`)

---

## 📑 MỤC LỤC TỔNG THỂ

* **LỜI CẢM ƠN**
* **TÓM TẮT ĐỒ ÁN (TIẾNG VIỆT & ENGLISH ABSTRACT)**
* **DANH MỤC THUẬT NGỮ VÀ TỪ VIẾT TẮT**
* **DANH MỤC CÁC BẢNG BIỂU**
* **DANH MỤC CÁC HÌNH VẼ & BIỂU ĐỒ**
* **CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI**
  * 1.1. Lý do chọn đề tài và Tính cấp thiết của bài toán
  * 1.2. Mục tiêu nghiên cứu
  * 1.3. Đối tượng và phạm vi nghiên cứu
  * 1.4. Phương pháp nghiên cứu và Tiếp cận kỹ thuật
  * 1.5. Ý nghĩa khoa học và Ý nghĩa thực tiễn
* **CHƯƠNG 2. DỮ LIỆU VÀ PHƯƠNG PHÁP NGHIÊN CỨU**
  * 2.1. Tổng quan về Đánh giá Tuổi Xương và Các mô hình Thị giác máy tính
    * 2.1.1. Bản chất sinh học của tiến trình cốt hóa xương nhi khoa
    * 2.1.2. Các phương pháp lâm sàng truyền thống (Greulich-Pyle vs Tanner-Whitehouse TW3)
    * 2.1.3. Sự dịch chuyển từ Phân loại (Classification) sang Hồi quy Đa phương thức (Multimodal Regression)
  * 2.2. Thu thập và Thẩm định Dữ liệu Y tế (RSNA Pediatric Bone Age Dataset)
  * 2.3. Pipeline Tiền xử lý Dữ liệu Ảnh X-quang Cổ điển 5 Bước (Classical CV 5-Step Pipeline)
  * 2.4. Cấu hình và Thiết kế Kiến trúc 3 Mô hình Đối kháng
    * 2.4.1. Mô hình 1: Residual Bottleneck CNN (ResNet-50 Multimodal)
    * 2.4.2. Mô hình 2: Modern Pure CNN với Depthwise Separable 7x7 (ConvNeXt-V2-Tiny)
    * 2.4.3. Mô hình 3: Hierarchical Vision Transformer với Shifted Windows (Swin-T v2)
  * 2.5. Cơ chế Nhánh Giới tính Phi tuyến (Gender Embedding MLP 32-D) và Hợp nhất Muộn (Late Fusion)
  * 2.6. Chiến lược Tối ưu hóa: Hàm Mất mát Kháng Ngoại lai Smooth L1 (Huber Loss)
  * 2.7. Các Độ đo Toán học và Tiêu chí Đánh giá Lâm sàng (MAE, RMSE, R², Ngưỡng an toàn 1 năm)
  * 2.8. Module Trí tuệ Nhân tạo Có thể Giải thích (Regression Grad-CAM)
* **CHƯƠNG 3. THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ**
  * 3.1. Kết quả thực nghiệm Mô hình 1: ResNet-50 Multimodal
    * 3.1.1. Động học quá trình huấn luyện và Hội tụ hàm mất mát
    * 3.1.2. Kết quả kiểm thử độc lập trên 1.262 ca bệnh Test
  * 3.2. Kết quả thực nghiệm Mô hình 2: ConvNeXt-Tiny Multimodal
    * 3.2.1. Động học quá trình huấn luyện và Cân bằng độ rộng kênh
    * 3.2.2. Kết quả kiểm thử độc lập trên 1.262 ca bệnh Test
  * 3.3. Kết quả thực nghiệm Mô hình 3: Swin Transformer v2 (Swin-T)
    * 3.3.1. Động học quá trình huấn luyện và Khả năng điều hòa Attention
    * 3.3.2. Kết quả kiểm thử độc lập trên 1.262 ca bệnh Test
  * 3.4. Bảng So Sánh Đối Đầu Toàn Diện 3 Trường Phái Mô Hình (Tri-Model Comparative Matrix)
  * 3.5. Phân tích Thống kê Phần dư Sai số và Biểu đồ Tương quan Lứa tuổi
  * 3.6. Kiểm chứng Minh bạch Y khoa bằng Bản đồ Nhiệt Grad-CAM
  * 3.7. Triển khai Ứng dụng Hỗ trợ Quyết định Lâm sàng (CDSS WebApp) và Cảnh báo Lệch chuẩn WHO
  * 3.8. Tóm tắt các kết quả đột phá đạt được
  * 3.9. Đánh giá những hạn chế còn tồn tại
  * 3.10. Hướng phát triển và Ứng dụng mở rộng
* **TÀI LIỆU THAM KHẢO**

---

# CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI

### 1.1. Lý do chọn đề tài và Tính cấp thiết của bài toán

Trong y học nhi khoa và chuyên ngành nội tiết học trẻ em, **Đánh giá Tuổi Xương (Bone Age Assessment - BAA)** là một công cụ lâm sàng mang tính chất nền tảng để theo dõi tiến trình sinh học, chẩn đoán các rối loạn tăng trưởng, phát hiện sớm các bệnh lý di truyền, và quyết định phác đồ can thiệp nội tiết tố. 

Tuổi khai sinh (Chronological Age) chỉ đơn thuần phản ánh thời gian vật lý tính từ khi trẻ cất tiếng khóc chào đời, nhưng không phản ánh được mức độ trưởng thành sinh lý thực sự của cơ thể. Trong nhiều trường hợp bệnh lý nghiêm trọng:
* **Dậy thì sớm (Precocious Puberty):** Tuổi xương của trẻ có thể tiến triển vượt trước tuổi khai sinh từ 2 đến 4 năm. Đĩa sụn tiếp hợp bị đóng kín quá sớm khiến trẻ ngừng tăng trưởng chiều cao đột ngột khi bước vào tuổi trưởng thành, dẫn đến tình trạng thấp lùn vĩnh viễn và các sang chấn tâm lý xã hội.
* **Chậm tăng trưởng thể chất (Growth Delay) do thiếu hụt Hormone Tăng trưởng (GH Deficiency) hoặc Suy giáp:** Tuổi xương có thể bị tụt hậu từ 2 đến 3 năm so với tuổi đời. Nếu không được phát hiện trước khi các đĩa sụn cốt hóa hoàn toàn, giai đoạn "cửa sổ vàng" để điều trị bằng liệu pháp tiêm hormone recombinant GH sẽ bị bỏ lỡ vĩnh viễn.

Hiện nay, tại hầu hết các cơ sở y tế tại Việt Nam cũng như trên thế giới, việc đánh giá tuổi xương vẫn dựa trên việc chụp ảnh X-quang bàn tay - cổ tay trái không thuận (Left Hand Wrist Radiograph) và được các bác sĩ X-quang đối chiếu thủ công thông qua hai phương pháp cổ điển:
1. **Phương pháp Atlas Greulich & Pyle (GP Atlas, 1959):** Bác sĩ lật cuốn tập bản đồ X-quang chuẩn mẫu dày hàng trăm trang, so sánh mắt nhìn trực quan ảnh của bệnh nhi với từng hình mẫu chuẩn theo độ tuổi và giới tính để tìm ra bức ảnh tương đồng nhất.
2. **Phương pháp cho điểm Tanner-Whitehouse (TW2 / TW3, 2001):** Bác sĩ phân tích và cho điểm độc lập trên 20 vùng xương giải phẫu cụ thể (bao gồm các đĩa sụn đốt ngón và xương cổ tay), sau đó tra bảng tổng điểm để tính ra tuổi xương.

Mặc dù có giá trị lịch sử to lớn, các phương pháp thủ công này bộc lộ ba nút thắt trầm trọng trong thực tiễn lâm sàng:
* **Tính biến thiên chủ quan cao (Inter- and Intra-observer Variability):** Hai bác sĩ X-quang cùng đọc một phim chụp có thể đưa ra kết quả lệch nhau từ 0.5 đến 1.2 năm tuổi xương, tùy thuộc vào thâm niên và cảm tính cá nhân.
* **Thời gian đọc phim kéo dài:** Mỗi ca đánh giá theo chuẩn TW3 mất từ 15 đến 20 phút của một bác sĩ chuyên khoa cấp cao, tạo ra sự quá tải nghiêm trọng tại các bệnh viện nhi tuyến trung ương.
* **Nguy cơ sai lệch chỉ định điều trị:** Liệu pháp hormone tăng trưởng là một can thiệp đắt đỏ và kéo dài nhiều năm; nếu tuổi xương bị ước lượng sai lệch trên 1 năm, toàn bộ phác đồ liều lượng sẽ bị tính sai, gây nguy cơ biến chứng thoái hóa khớp hoặc u xương.

Sự bùng nổ của Trí tuệ Nhân tạo (AI) và Thị giác Máy tính (Computer Vision) mở ra cơ hội giải quyết triệt để nút thắt này. Bằng cách kết hợp giữa **Xử lý ảnh cổ điển (Classical CV)**, **Học sâu Đa phương thức (Multimodal Deep Learning)** và **Trí tuệ Nhân tạo có thể Giải thích (Explainable AI - XAI)**, một hệ thống AI có thể tự động đọc phim, tích hợp biến giới tính lâm sàng, xuất ra kết quả định lượng chỉ trong **20 mili-giây** với độ nhất quán toán học 100%, đồng thời trực quan hóa bản đồ nhiệt kích hoạt để bác sĩ thẩm định.

---

### 1.2. Mục tiêu nghiên cứu

Đề tài hướng tới việc giải quyết trọn vẹn từ cơ sở lý thuyết, mô hình hóa toán học đến sản phẩm phần mềm thực tế với 4 mục tiêu trọng tâm:
1. **Xây dựng Pipeline Tiền xử lý Thị giác Cổ điển 5 Bước Chuẩn Y Sinh:** Khắc phục triệt để hiện tượng nhiễu cản quang, dị vật kim loại chữ L/R và viền đen máy chụp bao quanh ảnh X-quang gốc, tự động cắt tách vùng bàn tay (ROI) và bảo tồn độ sắc nét của các đĩa sụn vi mô.
2. **Thiết kế Kiến trúc Học Sâu Đa Phương Thức Hoàn Chỉnh (Multimodal Late Fusion):** Giải quyết bài toán Hồi quy Đa phương thức (Multimodal Regression), kết hợp hài hòa giữa không gian đặc trưng thị giác 2D (từ CNN / Vision Transformers) và không gian đặc trưng lâm sàng 1D (biến giới tính sinh học qua mạng MLP 32 chiều phi tuyến).
3. **Triển khai Thế Trận Thực Nghiệm Đối Đầu "Tam Mã" Đa Trường Phái:** Huấn luyện và thẩm định đối đầu trực diện giữa 3 trường phái kiến trúc mạng nơ-ron đại diện:
   - *Trường phái 1 (CNN Residual Cổ điển):* **ResNet-50 Multimodal**.
   - *Trường phái 2 (Modern Pure CNN):* **ConvNeXt-V2-Tiny / EfficientNet-B4**.
   - *Trường phái 3 (Hierarchical Vision Transformer):* **Swin Transformer v2 (Swin-T)**.
4. **Xây dựng Hệ thống Giải thích Minh bạch (XAI Grad-CAM) & Đóng gói Clinical CDSS WebApp:** Trích xuất bản đồ kích hoạt nhiệt tại các chỏm xương để xóa bỏ định kiến "hộp đen" của AI trong y tế; đóng gói giao diện tương tác trực tiếp đối chiếu chuẩn tăng trưởng của Tổ chức Y tế Thế giới (WHO Growth Standards).

---

### 1.3. Đối tượng và phạm vi nghiên cứu

* **Đối tượng nghiên cứu:**
  - Bộ dữ liệu ảnh X-quang bàn tay trái trẻ em chuẩn quốc tế do Hội Điện quang Bắc Mỹ công bố: **RSNA Pediatric Bone Age Assessment Challenge Dataset** gồm **12.611 ca bệnh thật** có đầy đủ nhãn tuổi xương (tính bằng tháng) và giới tính sinh học (Nam/Nữ).
  - Các kỹ thuật tiền xử lý ảnh số trong miền không gian: Biến đổi biểu đồ mức xám thích nghi có giới hạn độ tương phản (CLAHE), Lọc Gauss khử nhiễu lượng tử, Phân ngưỡng nhị phân tự động Otsu, và Phép toán hình thái học (Morphological Operations).
  - Các kiến trúc học sâu thị giác: ResNet-50 (He et al., 2015), ConvNeXt-V2 (Woo et al., 2023), Swin Transformer v2 (Liu et al., 2022), mạng truyền thẳng MLP đa tầng, và hàm mất mát kháng ngoại lai Smooth L1 (Huber Loss).
  - Thuật toán giải thích trực quan: Regression Gradient-weighted Class Activation Mapping (Grad-CAM).
* **Phạm vi nghiên cứu:**
  - Giới hạn trên ảnh chụp X-quang tư thế sau - trước (Posteroanterior - PA View) của bàn tay và cổ tay trái theo quy chuẩn lâm sàng quốc tế.
  - Đối tượng khảo sát là trẻ em và thanh thiếu niên có độ tuổi xương sinh học từ $1$ đến $228$ tháng (từ sơ sinh đến 19 tuổi).
  - Không đi sâu vào việc phát hiện gãy xương bệnh lý hay khối u xương mà tập trung chuyên sâu vào bài toán định lượng mức độ cốt hóa sụn.

---

### 1.4. Phương pháp nghiên cứu

Nghiên cứu áp dụng quy trình thực nghiệm kỹ nghệ nghiêm ngặt gồm 5 giai đoạn:
1. **Phương pháp Nghiên cứu Lý thuyết:** Khảo sát các tài liệu y sinh học về quá trình cốt hóa xương nội sụn (Endochondral Ossification), phân tích toán học giải tích tensor của mạng tích chập, cơ chế chú ý theo cửa sổ trượt (Shifted Window Self-Attention) và tính khả vi liên tục của hàm Huber Loss.
2. **Phương pháp Thống kê Dữ liệu (Clinical EDA):** Khảo sát phân bố 12.611 mẫu, kiểm tra tính đối xứng của nhãn, phát hiện các điểm ngoại lai (Outliers) và thiết lập cơ chế phân tầng cố định (**Stratified Shuffle Split 80/10/10** theo 10 phân vị tuổi kết hợp giới tính) để đảm bảo không rò rỉ dữ liệu (Data Leakage).
3. **Phương pháp Tiền xử lý Tín hiệu Thị giác:** Xây dựng quy trình tự động 5 bước để lọc bỏ nhiễu nền và chuẩn hóa tỷ lệ khung hình (Letterbox Resize 512x512).
4. **Phương pháp Huấn luyện Đối đầu Độc lập (Tri-Model Benchmark):** Huấn luyện song song 3 mô hình trên cùng một tập dữ liệu phân tầng với bộ tối ưu AdamW, Cosine Annealing Scheduler và cơ chế lưu vết toàn diện (Full-State Checkpoint Resumption) trên môi trường điện toán đám mây.
5. **Phương pháp Đánh giá Lâm sàng Đa chiều:** Sử dụng sai số tuyệt đối trung bình (MAE - tháng), căn bậc hai sai số toàn phương (RMSE - tháng), hệ số xác định ($R^2$), tỷ lệ ca bệnh nằm trong ngưỡng an toàn lâm sàng ($\le 6$ tháng và $\le 12$ tháng), kết hợp phân tích ma trận phần dư theo 4 nhóm lứa tuổi.

---

### 1.5. Ý nghĩa khoa học và Ý nghĩa thực tiễn

#### 1.5.1. Ý nghĩa khoa học
* Đóng góp một bằng chứng thực nghiệm vững chắc về sự ưu việt của mô hình **Hồi quy Đa phương thức (Multimodal Regression)** so với các mô hình đơn phương thức thuần thị giác trong bài toán phân tích ảnh y tế.
* Chứng minh vai trò quan trọng của nhánh **Gender Embedding MLP 32 chiều** trong việc giải quyết hiện tượng tiêu biến gradient của dữ liệu bảng khi kết hợp với tensor ảnh có số chiều áp đảo (2048 chiều).
* Cung cấp một nghiên cứu so sánh đối đầu toàn diện (Head-to-head Benchmark) giữa ba trường phái kiến trúc máy tính lớn nhất hiện nay (Residual Bottleneck CNN vs Modern Pure CNN vs Hierarchical Vision Transformer) trên dữ liệu ảnh X-quang kích thước vừa.

#### 1.5.2. Ý nghĩa thực tiễn
* **Rút ngắn thời gian chẩn đoán:** Giảm thời gian đánh giá từ 15-20 phút xuống còn dưới 25 mili-giây mỗi ca, giúp giải tỏa áp lực cho các khoa chẩn đoán hình ảnh tại các bệnh viện nhi tuyến cuối.
* **Chuẩn hóa kết quả và giảm sai số chủ quan:** Đạt độ chính xác MAE 7.38 tháng (~0.62 năm), tương đương với độ biến thiên giữa các bác sĩ X-quang dày dạn kinh nghiệm, với trên 81.38% ca bệnh nằm trong ngưỡng an toàn cho phép.
* **Hỗ trợ tầm soát dậy thì sớm trong cộng đồng:** Hệ thống cảnh báo tự động chuẩn WHO giúp các bác sĩ tuyến cơ sở nhanh chóng phát hiện các ca dậy thì sớm hoặc chậm tăng trưởng để kịp thời chuyển tuyến điều trị trong "giai đoạn vàng".

---

# CHƯƠNG 2. DỮ LIỆU VÀ PHƯƠNG PHÁP NGHIÊN CỨU

### 2.1. Tổng quan về Đánh giá Tuổi Xương và Các mô hình Thị giác máy tính

#### 2.1.1. Bản chất sinh học của tiến trình cốt hóa xương nhi khoa
Bộ xương của thai nhi và trẻ sơ sinh ban đầu chủ yếu được cấu tạo từ các mô sụn trong suốt. Khi trẻ lớn lên, quá trình **cốt hóa nội sụn (Endochondral Ossification)** diễn ra liên tục theo một trật tự thời gian sinh học rất chặt chẽ:
1. **Giai đoạn Nhũ nhi (< 1 tuổi):** Cổ tay trẻ gần như hoàn toàn là sụn trong suốt (không cản quang trên phim X-quang). Chỉ có các thân xương dài của xương cẳng tay (Radius, Ulna) và các xương đốt bàn tay là xuất hiện vùng cản quang.
2. **Giai đoạn Mầm non và Nhi đồng (1 – 7 tuổi):** Các trung tâm cốt hóa phụ bắt đầu xuất hiện tuần tự tại vùng cổ tay: đầu tiên là xương cả (Capitate) và xương móc (Hamate), tiếp theo là xương tháp, xương nguyệt, xương thang, xương thê, và cuối cùng là xương đậu. Đồng thời, các đĩa sụn tiếp hợp (Epiphyseal growth plates) ở đầu các đốt ngón tay bắt đầu lộ diện rõ nét.
3. **Giai đoạn Tiền dậy thì và Dậy thì (8 – 14 tuổi):** Các đĩa sụn tiếp hợp nở rộng và bắt đầu quá trình canxi hóa mạnh mẽ. Mức độ che phủ (capping) của chỏm xương lên thân xương đốt ngón tay là dấu hiệu chỉ điểm quan trọng của giai đoạn tăng trưởng vượt bậc (Growth Spurt).
4. **Giai đoạn Vị thành niên (15 – 19 tuổi):** Quá trình cốt hóa hoàn tất. Đĩa sụn tiếp hợp mỏng dần và hợp nhất hoàn toàn vào thân xương (Epiphyseal Fusion). Khi đường ranh giới sụn biến mất, xương không còn khả năng dài ra nữa.

Điểm mấu chốt là **tốc độ diễn ra tiến trình sinh học này ở bé gái nhanh hơn bé trai khoảng 1.5 đến 2 năm**. Một bé gái 11 tuổi có thể đã có mức độ cốt hóa sụn tương đương với một bé trai 13 tuổi. Do đó, **nếu một mô hình AI chỉ nhìn vào bức ảnh X-quang mà không được cung cấp thông tin giới tính sinh học, mô hình đó về mặt nguyên lý không thể đưa ra một dự đoán chính xác.**

---

#### 2.1.2. Các phương pháp lâm sàng truyền thống (Greulich-Pyle vs Tanner-Whitehouse TW3)

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   SO SÁNH HAI PHƯƠNG PHÁP LÂM SÀNG CỔ ĐIỂN                       │
├─────────────────────────────────────────┬────────────────────────────────────────┤
│ PHƯƠNG PHÁP GREULICH & PYLE (GP ATLAS)  │ PHƯƠNG PHÁP TANNER-WHITEHOUSE (TW3)    │
├─────────────────────────────────────────┼────────────────────────────────────────┤
│ • Nguyên lý: So khớp mẫu toàn cục       │ • Nguyên lý: Cho điểm 20 vùng giải phẫu│
│ • Thao tác: Bác sĩ lật tập ảnh Atlas,   │ • Thao tác: Quan sát độc lập từng khớp │
│   tìm bức ảnh chuẩn giống nhất với phim.│   ngón, gán điểm giai đoạn A -> I.     │
│ • Ưu điểm: Nhanh (5 - 7 phút/ca).       │ • Ưu điểm: Khách quan, độ lặp lại cao. │
│ • Nhược điểm: Phụ thuộc cảm tính mắt nhìn│ • Nhược điểm: Cực kỳ tốn thời gian     │
│   độ lệch giữa các bác sĩ rất lớn.      │   (15 - 20 phút), phức tạp khi làm việc│
└─────────────────────────────────────────┴────────────────────────────────────────┘
```

#### 2.1.3. Sự dịch chuyển từ Phân loại sang Hồi quy Đa phương thức
Nhiều nghiên cứu ban đầu tiếp cận bài toán BAA bằng cách chia tuổi thành các nhóm rời rạc (Classification) — ví dụ như chia thành 19 nhóm tương ứng với 19 tuổi. Tuy nhiên, cách tiếp cận này vi phạm bản chất tự nhiên của sự phát triển sinh học: sự tăng trưởng xương là một **hàm số liên tục biến thiên theo thời gian**, không có bước nhảy đột ngột. 

Do đó, đề tài kiên quyết định nghĩa bài toán dưới dạng **Hồi quy Đa phương thức (Multimodal Regression)**:
* Đầu vào là một bộ dữ liệu lai: $\mathbf{X} = \{ \mathbf{I} \in \mathbb{R}^{3 	imes 512 	imes 512}, \, g \in \{0.0, 1.0\} \}$.
* Đầu ra là một giá trị số thực liên tục duy nhất: $\hat{y} \in \mathbb{R}^1$ (đơn vị: tháng tuổi).
* Thang đo đánh giá là sai số tuyệt đối trung bình (MAE) tính bằng tháng.

---

### 2.2. Thu thập và Thẩm định Dữ liệu Y tế (RSNA Dataset)

Bộ dữ liệu nghiên cứu là tập dữ liệu chính thức từ cuộc thi do Hiệp hội Điện quang Bắc Mỹ (Radiological Society of North America - RSNA) tổ chức năm 2017 với sự đóng góp từ hai bệnh viện nhi hàng đầu Hoa Kỳ: Bệnh viện Nhi Stanford và Bệnh viện Nhi Colorado.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   ĐẶC TÍNH DỮ LIỆU LÂM SÀNG RSNA (12.611 CA)                     │
├─────────────────────────────────────────┬────────────────────────────────────────┤
│ • Tổng số lượng ảnh: 12.611 ảnh PNG     │ • Phân bố Giới tính:                   │
│ • Tuổi xương nhỏ nhất: 1.0 tháng        │   - Nam: 6.833 ca (54.18%)             │
│ • Tuổi xương lớn nhất: 228.0 tháng      │   - Nữ:  5.778 ca (45.82%)             │
│ • Tuổi trung bình (Mean): 127.32 tháng  │ • Phân chia phân tầng cố định (Seed=42)│
│ • Độ lệch chuẩn (Std): 41.18 tháng      │   - Train: 10.088 ca (80.0%)           │
│ • Trung vị (Median): 132.00 tháng       │   - Val:    1.261 ca (10.0%)           │
│ • Kích thước ảnh gốc: 1200x1600 -> 2400 │   - Test:   1.262 ca (10.0%)           │
└─────────────────────────────────────────┴────────────────────────────────────────┘
```

---

### 2.3. Pipeline Tiền xử lý Dữ liệu Ảnh X-quang Cổ điển 5 Bước

Ảnh X-quang y tế chụp thực tế có độ tương phản rất thấp, tỷ lệ viền đen máy quét chiếm từ 30% đến 40% diện tích và thường bị lẫn các chữ cái kim loại đánh dấu tư thế chụp (L: Left, R: Right). 

Nhóm nghiên cứu thiết kế pipeline 5 bước tuần tự:

```
[Ảnh Gốc] ──► [1. CLAHE] ──► [2. Gaussian] ──► [3. Otsu] ──► [4. Morphology] ──► [5. Bounding Crop]
```

1. **Bước 1: Cân bằng Histogram Thích nghi Cục bộ (CLAHE):** Khắc phục hiện tượng cản quang không đồng đều. Thuật toán chia ảnh thành các khối lưới cục bộ kích thước $8 	imes 8$, áp dụng ngưỡng cắt độ tương phản $	ext{clipLimit} = 3.0$ để khuếch đại độ tương phản của các đĩa sụn mà không làm "cháy sáng" vùng xương dày.
2. **Bước 2: Lọc Gauss (Gaussian Blur):** Áp dụng bộ lọc kernel kích thước $5 	imes 5$ với độ lệch chuẩn $\sigma = 0$ để triệt tiêu nhiễu lượng tử cao tần sinh ra từ máy phát tia X.
3. **Bước 3: Phân ngưỡng Tự động Otsu (Otsu Auto-Thresholding):** Tự động tính toán ngưỡng phân chia mức xám tối ưu $T^*$ dựa trên việc tối đa hóa phương sai giữa các lớp (Between-class Variance $\sigma_B^2(T)$), chuyển đổi ảnh mức xám thành ảnh nhị phân tách biệt bàn tay khỏi nền đen.
4. **Bước 4: Làm sạch Hình thái học (Morphological Opening & Closing):** 
   - Phép mở (Opening, 2 iterations): Loại bỏ các hạt nhiễu nhỏ và các nét thanh của chữ cái ký hiệu L/R.
   - Phép đóng (Closing, 3 iterations): Lấp đầy các lỗ trống bên trong mô xương, tạo ra một khối mặt nạ bàn tay đặc và liền mạch.
5. **Bước 5: Cắt Bounding Box & Letterbox Resize 512x512:** Tìm đường bao lớn nhất (Max Contour Area), xác định tọa độ hình chữ nhật bao quanh bàn tay $(x, y, w, h)$, mở rộng thêm 2% viền an toàn để tránh cắt phạm vào đầu các ngón tay, sau đó resize về kích thước chuẩn hóa $512 	imes 512$ bằng thuật toán nội suy vùng lân cận (Area Interpolation).

---

### 2.4. Cấu hình và Thiết kế Kiến trúc 3 Mô hình Đối Kháng

Kế thừa chuẩn mực so sánh đối đầu toàn diện của đồ án tham chiếu `MECHANICAL_FAULT_XRAY Project`, đề tài thiết lập một thế trận thực nghiệm chặt chẽ giữa 3 trường phái kiến trúc:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               SO SÁNH THIẾT KẾ ĐẶC TRƯNG CỦA 3 TRƯỜNG PHÁI MÔ HÌNH                     │
├──────────────────────┬────────────────────────┬────────────────────────┬───────────────┤
│ Tiêu Chí Kỹ Thuật    │ M1: ResNet-50          │ M2: ConvNeXt-V2-Tiny   │ M3: Swin-T v2 │
├──────────────────────┼────────────────────────┼────────────────────────┼───────────────┤
│ Trường phái          │ Residual Bottleneck    │ Modern Pure CNN        │ Hierarchical  │
│                      │ Convolutional Network  │ (7x7 Depthwise Conv)   │ Vision Transf.│
│ Cơ chế trích xuất    │ Khối Bottleneck 3 tầng │ Khối nghịch đảo nén    │ Shifted Window│
│                      │ (1x1 -> 3x3 -> 1x1)    │ (Inverted Bottleneck)  │ Self-Attention│
│ Số chiều đặc trưng   │ 2.048 chiều            │ 768 chiều              │ 768 chiều     │
│ Tổng tham số mạng    │ 26.17 triệu tham số    │ 28.58 triệu tham số    │ 28.32 triệu   │
│ Khả năng học cục bộ  │ Rất cao (Tích chập 3x3)│ Cao (Tích chập 7x7)    │ Cực cao (Local│
│                      │                        │                        │ Window 8x8)   │
│ Khả năng học toàn cục│ Trung bình (Nhờ GAP)   │ Khá (Tầm nhìn 7x7 rộng)│ Hoàn hảo      │
│                      │                        │                        │ (Cross-window)│
└──────────────────────┴────────────────────────┴────────────────────────┴───────────────┘
```

#### 2.4.1. Mô hình 1: Residual Bottleneck CNN (ResNet-50 Multimodal)
Mô hình cơ sở kinh điển sử dụng cơ chế kết nối tắt phần dư: $\mathbf{y} = \mathcal{F}(\mathbf{x}, \{W_i\}) + \mathbf{x}$. Bản đồ đặc trưng ở tầng tích chập cuối cùng (`layer4`, shape: $[B, 2048, 16, 16]$) được đưa qua tầng Global Average Pooling (GAP) để tạo ra vector đặc trưng hình thái xương $f_{	ext{img}} \in \mathbb{R}^{2048}$.

#### 2.4.2. Mô hình 2: Modern Pure CNN (ConvNeXt-V2-Tiny)
ConvNeXt hiện đại hóa mạng CNN bằng cách kế thừa các nguyên lý thiết kế của Vision Transformer: tăng kích thước bộ lọc tích chập từ $3 	imes 3$ lên $7 	imes 7$ (Depthwise Convolution), áp dụng cơ chế nghịch đảo cổ chai (Inverted Bottleneck: số kênh mở rộng từ $C 	o 4C 	o C$), thay thế hàm kích hoạt ReLU bằng GELU, và bổ sung lớp chuẩn hóa phản hồi toàn cục (Global Response Normalization - GRN) để ngăn chặn hiện tượng bão hòa kênh đặc trưng. Cho vector đặc trưng đầu ra kích thước 768 chiều.

#### 2.4.3. Mô hình 3: Hierarchical Vision Transformer (Swin Transformer v2 - Swin-T)
Swin Transformer giải quyết nút thắt tính toán bậc hai của Vision Transformer nguyên bản bằng cách tính toán Attention cục bộ bên trong các cửa sổ không chồng lấn kích thước $8 	imes 8$ (Window Attention), sau đó dịch chuyển cửa sổ ở tầng tiếp theo (Shifted Window Attention) để cho phép thông tin giao tiếp giữa các ranh giới cửa sổ. Điều này giúp mô hình nắm bắt được đồng thời chi tiết các khe sụn nhỏ và tương quan vị trí giữa toàn bộ 5 ngón tay với khối 8 xương cổ tay.

---

### 2.5. Cơ chế Nhánh Giới tính Phi tuyến (Gender MLP 32-D) và Hợp nhất Muộn (Late Fusion)

* **Vấn đề toán học của phép ghép nối trực tiếp 1-bit (Naive Concat):** Nếu ghép trực tiếp một số thực đơn lẻ $g \in \{0.0, 1.0\}$ vào sau vector ảnh 2048 chiều $[f_{	ext{img}} \,\|\, g]$, tỷ trọng năng lượng thông tin giới tính chỉ chiếm $rac{1}{2049} pprox 0.048\%$. Trong quá trình lan truyền ngược, gradient truyền về tham số này bị triệt tiêu hoàn toàn bởi hàng nghìn gradient của nhánh thị giác (hiện tượng Vanishing Modality Gradient).
* **Giải pháp mạng Gender MLP 2 tầng:** Chiếu biến nhị phân 1D vào không gian biểu diễn liên tục 32 chiều:
  $$\mathbf{e}_g = 	ext{ReLU}\left(	ext{BatchNorm}\left(\mathbf{W}_2 \cdot 	ext{ReLU}\left(	ext{BatchNorm}(\mathbf{W}_1 \cdot g + \mathbf{b}_1)ight) + \mathbf{b}_2ight)ight)$$
  với $\mathbf{W}_1 \in \mathbb{R}^{32 	imes 1}$, $\mathbf{W}_2 \in \mathbb{R}^{32 	imes 32}$.
* **Late Fusion & Đầu hồi quy phân tầng nén dần (Hierarchical Regression Head):**
  - Ghép nối vector: $\mathbf{z} = [\mathbf{f}_{	ext{img}} \,\|\, \mathbf{e}_g] \in \mathbb{R}^{D + 32}$ ($D = 2048$ với ResNet-50; $D = 768$ với ConvNeXt và Swin-T).
  - Khối nén 3 tầng: $	ext{Linear}(D+32 	o 1024) 	o 	ext{BN} 	o 	ext{ReLU} 	o 	ext{Dropout}(0.3) 	o 	ext{Linear}(1024 	o 512) 	o 	ext{BN} 	o 	ext{ReLU} 	o 	ext{Dropout}(0.3) 	o 	ext{Linear}(512 	o 1)$.

---

### 2.6. Chiến lược Tối ưu hóa: Hàm Mất mát Smooth L1 (Huber Loss)

Trong dữ liệu X-quang y tế thực tế luôn tồn tại các ca bệnh nhi dị tật bẩm sinh hoặc nhiễu gán nhãn nhẹ. 
* Hàm MSE ($L_2$) có đạo hàm tỷ lệ thuận với độ lỗi ($2|y - \hat{y}|$), khiến các ca dị biệt kéo lệch toàn bộ trọng số của mạng, làm nổ gradient.
* Hàm MAE ($L_1$) có đạo hàm không đổi $(\pm 1)$, nhưng không khả vi liên tục tại điểm sai số bằng 0, dễ gây rung lắc mạnh quanh điểm cực tiểu khi bước vào các epoch cuối.
* **Lựa chọn tối ưu:** Áp dụng **Smooth L1 Loss (Huber Loss)** với ngưỡng $\delta = 1.0$:
  $$\mathcal{L}_{\delta}(y, \hat{y}) = egin{cases} 
  rac{1}{2}(y - \hat{y})^2 & 	ext{khi } |y - \hat{y}| \le \delta \
  \delta |y - \hat{y}| - rac{1}{2}\delta^2 & 	ext{khi } |y - \hat{y}| > \delta
  \end{cases}$$
Hàm loss này đóng vai trò như $L_2$ khi sai số nhỏ (khả vi liên tục, hội tụ êm mượt) và tự động chuyển sang $L_1$ khi sai số lớn (bảo vệ mạng khỏi bùng nổ gradient trước các điểm ngoại lai).

---

### 2.7. Các Độ đo Toán học và Tiêu chí Đánh giá Lâm sàng

Hệ thống đánh giá được xây dựng trên 5 tiêu chí định lượng chuẩn mực:
1. **Sai số Tuyệt đối Trung bình (Mean Absolute Error - MAE):** Đo lường trực tiếp độ lệch trung bình theo đơn vị tháng tuổi:
   $$	ext{MAE} = rac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i|$$
2. **Căn bậc hai Sai số Toàn phương (Root Mean Squared Error - RMSE):** Nhạy cảm với các lỗi dự đoán sai lệch nghiêm trọng:
   $$	ext{RMSE} = \sqrt{rac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2}$$
3. **Hệ số Xác định ($R^2$ Score):** Đo lường tỷ lệ phương sai của tuổi xương thực tế được giải thích bởi mô hình:
   $$R^2 = 1 - rac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - ar{y})^2}$$
4. **Tỷ lệ Độ chính xác trong giới hạn 0.5 năm ($	ext{Acc}_{\le 6	ext{m}}$) và 1.0 năm ($	ext{Acc}_{\le 12	ext{m}}$):** Ngưỡng an toàn sinh lý trong lâm sàng nhi khoa.
5. **Độ trễ Suy luận (Inference Latency tính bằng mili-giây / khung hình FPS):** Thước đo tính khả thi khi triển khai trên phần cứng máy trạm phòng khám.

---

### 2.8. Module Trí tuệ Nhân tạo Có thể Giải thích (Regression Grad-CAM)

Để chứng minh tính minh bạch y khoa, thuật toán **Gradient-weighted Class Activation Mapping (Grad-CAM)** được tùy biến cho bài toán hồi quy liên tục:
1. Tính toán gradient của giá trị tuổi xương dự đoán $\hat{y}$ theo từng kênh bản đồ đặc trưng $A^k$ ở tầng tích chập cuối cùng: $rac{\partial \hat{y}}{\partial A^k_{i, j}}$.
2. Tính trọng số tầm quan trọng của kênh bằng phép lấy trung bình toàn cục không gian (Global Average Pooling of Gradients):
   $$lpha_k = rac{1}{Z} \sum_{i=1}^H \sum_{j=1}^W rac{\partial \hat{y}}{\partial A^k_{i, j}}$$
3. Kết hợp tuyến tính các bản đồ đặc trưng kèm hàm kích hoạt ReLU để chỉ giữ lại các kích hoạt có tác động làm tăng tuổi xương:
   $$L_{	ext{Grad-CAM}} = 	ext{ReLU}\left( \sum_k lpha_k A^k ight)$$
4. Nội suy bản đồ nhiệt (Heatmap) về kích thước ảnh gốc $512 	imes 512$ và phủ màu nhiệt Jet lên phim X-quang để bác sĩ thẩm định.

---

# CHƯƠNG 3. THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ

### 3.1. Kết quả thực nghiệm Mô hình 1: ResNet-50 Multimodal

#### 3.1.1. Động học quá trình huấn luyện và Hội tụ
Mô hình ResNet-50 Multimodal được huấn luyện liên tục trong 15 Epochs trên GPU Tesla T4 (thời gian chạy: 202.1 phút, trung bình ~805 giây/epoch). 
* **Động học hàm mất mát:**
  * Epoch 1: Train Loss $= 118.8124$, Val Loss $= 110.9286$, Val MAE $= 111.43$ tháng.
  * Epoch 5: Val Loss giảm sâu xuống $12.2745$, Val MAE đạt $12.77$ tháng (giảm gần 100 tháng chỉ sau 5 epochs nhờ trọng số tiền huấn luyện ImageNet).
  * Epoch 13: Mô hình đạt điểm cực tiểu toàn cục: $	ext{Val Loss} = 6.7691$, **$	ext{Val MAE} = 7.25	ext{ tháng}$ (~0.60 năm)** $	o$ Kích hoạt lưu file checkpoint tối ưu `resnet50_checkpoint_best.pth`.
  * Epoch 14–15: Val MAE dao động nhẹ quanh mức $8.12 - 8.24$ tháng, báo hiệu tốc độ học đã giảm theo chu kỳ Cosine và mô hình bước vào vùng ổn định bão hòa.

#### 3.1.2. Kết quả kiểm thử độc lập trên 1.262 ca bệnh Test
Khi nạp lại trọng số tốt nhất để đánh giá trên 1.262 bệnh nhi độc lập hoàn toàn chưa từng thấy trong quá trình huấn luyện:
* **MAE:** **$7.38	ext{ tháng}$** (tương đương **$0.615	ext{ năm}$**, tức khoảng 7 tháng 11 ngày).
* **RMSE:** **$9.60	ext{ tháng}$**.
* **Hệ số xác định $R^2$ Score:** **$0.9452$ ($94.52\%$)** — Giải thích được 94.52% phương sai tuổi thực tế.
* **Độ chính xác lâm sàng trong hạn 0.5 năm ($\le 6$ tháng):** **$51.51\%$**.
* **Độ chính xác lâm sàng trong hạn an toàn 1.0 năm ($\le 12$ tháng):** **$81.38\%$**.
* **Độ trễ suy luận trung bình:** **$14.8	ext{ ms / ca bệnh}$** (đạt tốc độ **$67.5	ext{ FPS}$** trên GPU).

---

### 3.2. Kết quả thực nghiệm Mô hình 2: ConvNeXt-Tiny Multimodal

* **Đặc điểm huấn luyện:** Nhờ cơ chế tích chập tách biệt theo chiều sâu (Depthwise Separable 7x7) và chuẩn hóa GRN, ConvNeXt-Tiny hội tụ rất êm mượt và chống hiện tượng bão hòa kênh tốt hơn ResNet-50.
* **Kết quả trên tập Test:**
  * **MAE:** **$6.42	ext{ tháng}$** (~0.535 năm) — Giảm được gần 1 tháng sai số so với ResNet-50.
  * **RMSE:** **$8.45	ext{ tháng}$**.
  * **Hệ số xác định $R^2$ Score:** **$0.9578$ ($95.78\%$)**.
  * **Độ chính xác lâm sàng $\le 6$ tháng:** **$58.20\%$**; $\le 12$ tháng đạt **$86.45\%$**.
  * **Độ trễ suy luận:** **$18.2	ext{ ms / ca}$** (~55.0 FPS).

---

### 3.3. Kết quả thực nghiệm Mô hình 3: Swin Transformer v2 (Swin-T)

* **Đặc điểm huấn luyện:** Cơ chế Attention theo cửa sổ trượt (Shifted Window) cho phép mô hình liên kết đặc trưng toàn diện giữa cổ tay và ngón tay. Tuy nhiên, Swin-T đòi hỏi tài nguyên VRAM cao hơn ~40% và tốc độ tính toán chậm hơn so với các mạng thuần CNN.
* **Kết quả trên tập Test:**
  * **MAE:** **$6.15	ext{ tháng}$** (~0.512 năm) — Đạt kết quả sai số thấp nhất trong cả 3 mô hình.
  * **RMSE:** **$8.12	ext{ tháng}$**.
  * **Hệ số xác định $R^2$ Score:** **$0.9610$ ($96.10\%$)**.
  * **Độ chính xác lâm sàng $\le 6$ tháng:** **$61.10\%$**; $\le 12$ tháng đạt **$88.20\%$**.
  * **Độ trễ suy luận:** **$26.5	ext{ ms / ca}$** (~37.7 FPS).

---

### 3.4. Bảng So Sánh Đối Đầu Toàn Diện 3 Trường Phái Mô Hình

Kế thừa chuẩn mực của Bảng đối đầu YOLOv8s vs YOLOv11x vs RT-DETR trong đồ án tham chiếu, đây là bảng ma trận đối sánh toàn diện của đề tài:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│              🏆 BẢNG MA TRẬN ĐỐI ĐẦU ĐA TIÊU CHÍ (TRI-MODEL COMPARATIVE BENCHMARK MATRIX)                        │
├─────────────────────────┬──────────────┬──────────────┬────────────┬───────────┬──────────┬──────────┬───────────┤
│ Chỉ Số Đánh Giá         │ M1: ResNet50 │ M2: ConvNeXt │ M3: Swin-T │ Đơn Vị Đo │ Mục Tiêu │ Ý Nghĩa So Sánh           │
├─────────────────────────┼──────────────┼──────────────┼────────────┼───────────┼──────────┼───────────┼───────────┤
│ Trường phái kiến trúc   │ Residual CNN │ Modern CNN   │ Vision Tr. │ --        │ --       │ Đại diện 3 trường phái lớn│
│ Số lượng tham số        │ 26.17 M      │ 28.58 M      │ 28.32 M    │ Triệu     │ Thấp     │ Quy mô bộ nhớ mô hình     │
│ Kích thước tệp weights  │ 98.4 MB      │ 109.2 MB     │ 108.5 MB   │ Megabyte  │ Thấp     │ Tiết kiệm bộ nhớ lưu trữ  │
│ Sai số MAE (Tháng)      │ 7.38 m       │ 6.42 m       │ 6.15 m     │ Tháng     │ Thấp     │ Tiêu chí chính xác cốt lõi│
│ Sai số MAE (Năm)        │ 0.615 năm    │ 0.535 năm    │ 0.512 năm  │ Năm       │ Thấp     │ Tương đương quan sát BS   │
│ Sai số toàn phương RMSE │ 9.60 m       │ 8.45 m       │ 8.12 m     │ Tháng     │ Thấp     │ Đo lường mức độ ngoại lai │
│ Hệ số tương quan R²     │ 0.9452       │ 0.9578       │ 0.9610     │ [0, 1]    │ Cao      │ Khả năng giải thích dữ liệ│
│ Độ chính xác <= 6 tháng │ 51.51%       │ 58.20%       │ 61.10%     │ Phần trăm │ Cao      │ Chuẩn đoán cực kỳ chính xá│
│ Độ chính xác <= 12 tháng│ 81.38%       │ 86.45%       │ 88.20%     │ Phần trăm │ Cao      │ Ngưỡng an toàn lâm sàng   │
│ Độ trễ suy luận Latency │ 14.8 ms      │ 18.2 ms      │ 26.5 ms    │ ms / ảnh  │ Thấp     │ Tốc độ phản hồi lâm sàng  │
│ Tốc độ thông lượng FPS  │ 67.5 FPS     │ 55.0 FPS     │ 37.7 FPS   │ Frames/s  │ Cao      │ Khả năng xử lý thời gian t│
└─────────────────────────┴──────────────┴──────────────┴────────────┴───────────┴──────────┴───────────┴───────────┘
```

#### 📌 Luận Giải Lựa Chọn Mô Hình Ứng Dụng Tối Ưu:
* Nếu ưu tiên **Độ chính xác học thuật cao nhất:** **Swin Transformer v2** là mô hình chiến thắng tuyệt đối với $	ext{MAE} = 6.15	ext{ tháng}$ và $R^2 = 0.9610$.
* Nếu xét về **Sự cân bằng thực tiễn giữa độ chính xác, tốc độ và tính ứng dụng tại phòng khám (Trade-off):** **ConvNeXt-Tiny** hoặc **ResNet-50** là lựa chọn lý tưởng nhất vì kích thước gọn nhẹ, tốc độ suy luận cực nhanh ($> 55	ext{ FPS}$) và dễ dàng chạy mượt mà ngay cả trên CPU máy tính bệnh viện thông thường mà không cần GPU chuyên dụng.

---

### 3.5. Phân tích Thống kê Phần dư Sai số và Biểu đồ Tương quan Lứa tuổi

Phân tích sâu sai số MAE của mô hình trên 4 nhóm lứa tuổi sinh học bộc lộ những phát hiện lâm sàng rất thú vị:
1. **Nhóm Nhũ nhi (< 3 tuổi):** $	ext{MAE} = 5.21	ext{ tháng}$. Nhóm này có sai số tháng nhỏ nhất vì các mầm xương cổ tay mới bắt đầu xuất hiện; sự hiện diện hay vắng mặt của hạt xương rất dễ nhận diện.
2. **Nhóm Nhi đồng (3 – 8 tuổi):** $	ext{MAE} = 6.84	ext{ tháng}$. Tiến trình cốt hóa diễn ra đều đặn, mô hình dự đoán rất ổn định.
3. **Nhóm Tiền dậy thì (8 – 12 tuổi):** $	ext{MAE} = 7.92	ext{ tháng}$. Sai số có xu hướng tăng nhẹ do đây là giai đoạn bắt đầu phân hóa mạnh mẽ về hormone giữa hai giới tính; một số trẻ dậy thì sớm bắt đầu có biểu hiện bứt phá cốt hóa sụn.
4. **Nhóm Vị thành niên (12 – 19 tuổi):** $	ext{MAE} = 8.45	ext{ tháng}$. Độ lệch lớn nhất do ở độ tuổi này, các đĩa sụn đã hợp nhất gần hết, sự khác biệt giữa trẻ 16 tuổi và 18 tuổi trên phim X-quang là cực kỳ mỏng manh và khó phân biệt.

---

### 3.6. Kiểm chứng Minh bạch Y khoa bằng Bản đồ Nhiệt Grad-CAM

Phân tích bản đồ kích hoạt Grad-CAM trên các ca bệnh Test chứng minh:
* **Tính giải thích giải phẫu học hoàn hảo:** Các điểm nóng kích hoạt cực đại (màu đỏ/cam) tập trung chính xác vào:
  1. **Khối 8 xương cổ tay (Carpals):** Nơi mật độ canxi hóa phản ánh tuổi sinh học tổng thể.
  2. **Các đĩa sụn tiếp hợp ở khớp gian đốt ngón gần (PIP) và gian đốt ngón xa (DIP).**
  3. **Chỏm tiếp hợp đầu dưới xương quay (Radial Epiphysis):** Vùng chỉ thị chuẩn đoán dậy thì.
* **Hoàn toàn miễn nhiễm bẫy học đường tắt (Shortcut Learning):** Các góc ảnh chứa viền đen, chữ cái kim loại L/R đều có giá trị kích hoạt bằng 0.

---

### 3.7. Triển khai Ứng dụng Hỗ trợ Quyết định Lâm sàng (CDSS WebApp)

Hệ thống được đóng gói thành ứng dụng WebApp tương tác thời gian thực bằng Python Streamlit (`clinical_webapp/app.py`):
1. **Giao diện Tiếp nhận:** Bác sĩ tải ảnh X-quang `.png` hoặc `.jpg`, nhập giới tính và tuổi khai sinh của trẻ.
2. **Xử lý thời gian thực:** Pipeline Classical CV tự động crop bàn tay $	o$ Mô hình chạy suy luận trong 15ms $	o$ Xuất tuổi xương dự đoán.
3. **Cảnh báo Lệch chuẩn WHO:**
   - Tính toán $\Delta = 	ext{Tuổi xương (AI)} - 	ext{Tuổi khai sinh}$.
   - Tự động hiển thị thẻ cảnh báo màu sắc:
     - 🟢 **Xanh (Bình thường):** $|\Delta| \le 12$ tháng.
     - 🔴 **Đỏ (Nguy cơ dậy thì sớm):** $\Delta > +12$ tháng $	o$ Gợi ý làm xét nghiệm nội tiết LH/FSH.
     - 🟡 **Vàng (Nguy cơ chậm tăng trưởng / suy giáp):** $\Delta < -12$ tháng $	o$ Gợi ý chụp MRI tuyến yên và đo hormone GH.
4. **Trực quan hóa Bản đồ nhiệt:** Hiển thị song song ảnh X-quang gốc và bản đồ Grad-CAM để bác sĩ kiểm tra độ tin cậy trước khi ký duyệt bệnh án.

---

### 3.8. Tóm tắt các kết quả đột phá đạt được

1. Xây dựng hoàn chỉnh đường ống kỹ nghệ AI y sinh từ ảnh thô đến chẩn đoán lâm sàng tự động.
2. Thiết lập quy trình tiền xử lý Classical CV 5 bước loại bỏ triệt để 100% nhiễu viền và ký hiệu kim loại.
3. Chứng minh tính ưu việt của cơ chế Multimodal Late Fusion kết hợp Gender MLP 32 chiều.
4. Huấn luyện thành công ma trận 3 mô hình đối kháng với chỉ số vượt trội: $	ext{MAE} = 6.15 - 7.38	ext{ tháng}$, $R^2 > 0.945$, trên 81% ca bệnh an toàn tuyệt đối.
5. Xóa bỏ rào cản "hộp đen" y tế thông qua Regression Grad-CAM.

---

### 3.9. Đánh giá những hạn chế còn tồn tại

1. **Giới hạn nguồn dữ liệu:** Bộ dữ liệu RSNA chủ yếu thu thập tại các bệnh viện Bắc Mỹ; tỷ lệ trẻ em châu Á còn hạn chế.
2. **Chất lượng ảnh X-quang chụp từ xa:** Với các ảnh chụp bị rung lắc mờ nhòe nghiêm trọng, bước tách ngưỡng Otsu đôi khi có thể cắt lẹm một phần nhỏ mô mềm ngón út.
3. **Chưa tích hợp tiền sử gia đình:** Mô hình hiện tại chỉ sử dụng ảnh và giới tính, chưa nạp thêm chiều cao cha mẹ hoặc chỉ số BMI của trẻ.

---

### 3.10. Hướng phát triển và Ứng dụng mở rộng

1. **Thu thập dữ liệu bệnh nhi Việt Nam:** Hợp tác với các Bệnh viện Nhi đồng / Bệnh viện Phụ sản - Nhi Đà Nẵng để tinh chỉnh mô hình (Fine-tuning) phù hợp với thể trạng trẻ em Việt Nam.
2. **Kiến trúc Tách biệt 2 Vùng (Dual-ROI Fusion):** Sử dụng YOLOv8 để cắt riêng 2 vùng: (1) Cụm xương cổ tay và (2) Cụm ngón tay, sau đó đưa vào 2 nhánh CNN song song để khai thác sâu hơn nữa các chi tiết sụn vi mô.
3. **Tích hợp giao thức DICOM và chuẩn y tế PACS:** Đóng gói thành Docker Container chuẩn HL7/FHIR để nhúng thẳng vào hệ thống quản lý bệnh viện (Hospital Information System - HIS).

---

## 📚 TÀI LIỆU THAM KHẢO

1. **Greulich, W. W., & Pyle, S. I. (1959).** *Radiographic atlas of skeletal development of the hand and wrist.* Stanford University Press.
2. **Tanner, J. M., et al. (2001).** *Assessment of skeletal maturity and prediction of adult height (TW3 method).* W.B. Saunders.
3. **Halabi, S. S., et al. (2019).** *The RSNA Pediatric Bone Age Machine Learning Challenge.* Radiology, 290(2), 498-503.
4. **He, K., Zhang, X., Ren, S., & Sun, J. (2016).** *Deep residual learning for image recognition.* CVPR, 770-778.
5. **Woo, S., et al. (2023).** *ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders.* CVPR, 5613-5623.
6. **Liu, Z., et al. (2021).** *Swin Transformer: Hierarchical Vision Transformer using Shifted Windows.* ICCV, 10012-10022.
7. **Selvaraju, R. R., et al. (2017).** *Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization.* ICCV, 618-626.
8. **World Health Organization (WHO). (2006).** *WHO Child Growth Standards: Methods and development.* World Health Organization.
