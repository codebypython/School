# BÁO CÁO ĐỀ CƯƠNG VÀ THIẾT KẾ KỸ THUẬT DỰ ÁN
## ĐỀ TÀI: HỆ THỐNG TỰ ĐỘNG ĐÁNH GIÁ TUỔI XƯƠNG (BONE AGE ASSESSMENT) TỪ ẢNH X-QUANG BÀN TAY TRẺ EM
**Học phần**: Computer Vision (Thị giác Máy tính)  
**Đơn vị đào tạo**: Trường Đại học Bách Khoa — Đại học Đà Nẵng (DUT)  
**Nhóm thực hiện**: 02 Sinh viên | **Thời gian thực hiện**: 04 tuần  
**Môi trường tính toán**: GPU NVIDIA GeForce RTX 3050 Laptop (4GB VRAM) & Google Colab (Tesla T4 16GB)  

---

## TỔNG QUAN ĐIỀU HÀNH (EXECUTIVE SUMMARY)

Dự án **"Hệ thống Tự động Đánh giá Tuổi Xương từ ảnh X-quang Bàn tay Trẻ em" (Pediatric Bone Age Assessment - BAA)** được xây dựng nhằm giải quyết bài toán định lượng mức độ trưởng thành sinh học của hệ xương ở bệnh nhi, phục vụ chẩn đoán các rối loạn nội tiết (dậy thì sớm, chậm tăng trưởng do thiếu hụt hormone tăng trưởng GH, suy tuyến giáp bẩm sinh) và dự báo chiều cao trưởng thành. 

Khác với các đồ án Computer Vision thông thường chỉ dừng lại ở bài toán phân loại bệnh (Classification) đơn thuần, đề tài này tiếp cận một bài toán **Hồi quy Đa phương thức (Multimodal Regression)** phức tạp, kết hợp chặt chẽ giữa:
1. **Xử lý ảnh thị giác cổ điển (Classical Computer Vision)**: Pipeline 5 bước gồm cân bằng lược đồ màu thích ứng cục bộ (CLAHE), lọc nhiễu Gaussian, phân ngưỡng tự động Otsu, biến đổi hình thái học (Morphological Filtering) và định vị vùng quan tâm (ROI Cropping) để làm sạch nền và triệt tiêu chữ cái đánh dấu (L/R marker).
2. **Học sâu đa phương thức (Multimodal Deep Learning)**: Mạng nơ-ron tích chập (CNN Backbone: ResNet-50 / EfficientNet-B4) kết hợp với nhánh mã hóa giới tính phi tuyến (Gender Embedding 32 chiều) thông qua kỹ thuật **Late Fusion**, tối ưu hóa bởi hàm mất mát kháng ngoại lai **Smooth L1 (Huber Loss)**.
3. **Trí tuệ nhân tạo có thể giải thích (Explainable AI - XAI)**: Module **Grad-CAM** cho bài toán hồi quy giúp bác sĩ xác minh mô hình có thực sự "nhìn" vào các trung tâm cốt hóa quan trọng (xương cổ tay, sụn tiếp hợp) hay bị rơi vào bẫy học đường tắt (Shortcut Learning).
4. **Ứng dụng thực tiễn (Clinical Web App)**: Giao diện tương tác Streamlit tích hợp biểu đồ tăng trưởng chuẩn của Tổ chức Y tế Thế giới (WHO Growth Standards), đưa ra cảnh báo lâm sàng tự động.

Toàn bộ giải pháp được thiết kế tối ưu hóa thích ứng hoàn toàn với rào cản phần cứng cục bộ (RTX 3050 4GB) thông qua kỹ thuật Mixed Precision Training (FP16) và cơ chế huấn luyện phân tầng trên đám mây (Google Colab).

---

## CHƯƠNG 1: BỐI CẢNH DỰ ÁN VÀ TÍNH CẤP THIẾT

### 1.1. Ý nghĩa Lâm sàng của Đánh giá Tuổi Xương
Tuổi xương (Bone Age) là chỉ số vàng phản ánh mức độ trưởng thành sinh lý và sinh học thực tế của hệ xương, hoàn toàn khác biệt với **tuổi sinh học/tuổi theo giấy khai sinh (Chronological Age)**:
- **Trường hợp bình thường**: Độ lệch giữa tuổi xương và tuổi thật $|\Delta| = |\text{Bone Age} - \text{Chronological Age}| \le 12 \text{ tháng}$ (1 năm).
- **Tuổi xương phát triển sớm ($\Delta > +12 \text{ tháng}$)**: Báo hiệu tình trạng dậy thì sớm (Precocious Puberty), u tuyến thượng thận, hoặc cường giáp. Hậu quả là sụn tiếp hợp đóng sớm khiến trẻ ngừng phát triển chiều cao trước tuổi trưởng thành.
- **Tuổi xương phát triển muộn ($\Delta < -12 \text{ tháng}$)**: Báo hiệu tình trạng thiếu hormone tăng trưởng (GH Deficiency), suy tuyến giáp bẩm sinh (Hypothyroidism), hội chứng Turner hoặc suy dinh dưỡng mãn tính.

### 1.2. Thách thức trong Quy trình Lâm sàng Truyền thống
Hiện nay, hai phương pháp đọc tuổi xương phổ biến nhất trong y khoa gồm:
1. **Phương pháp Greulich-Pyle (GP)**: Bác sĩ đối chiếu toàn bộ ảnh X-quang của bệnh nhi với tập bản đồ mẫu (GP Atlas xuất bản từ năm 1959) để tìm ảnh giống nhất.
   - *Hạn chế*: Mang tính chủ quan rất lớn, độ biến thiên giữa các bác sĩ (inter-observer variability) và giữa các lần đọc của cùng một bác sĩ (intra-observer variability) dao động từ **0.5 đến 1.5 năm tuổi**.
2. **Phương pháp Tanner-Whitehouse (TW3)**: Bác sĩ phân tích chi tiết 20 vùng giải phẫu (ROIs) gồm 13 xương dài (ngón tay, xương bàn, đầu dưới xương quay/trụ) và 7 xương cổ tay, chấm điểm từng vùng rồi tra bảng quy đổi.
   - *Hạn chế*: Độ chính xác cao hơn nhưng cực kỳ tốn thời gian (mất từ 15–30 phút cho một phim chụp), tạo áp lực quá tải khủng khiếp lên hệ thống chẩn đoán hình ảnh nhi khoa.

### 1.3. Mục tiêu Khoa học và Ứng dụng của Đề tài
- **Mục tiêu kỹ thuật**: Xây dựng mô hình Computer Vision có sai số tuyệt đối trung bình **MAE (Mean Absolute Error) đạt dưới 6.0 tháng tuổi** trên tập kiểm thử độc lập (đạt mức tương đương năng lực của bác sĩ X-quang chuyên khoa).
- **Mục tiêu học thuật**: Minh chứng rõ ràng vai trò của từng phương pháp xử lý ảnh số căn bản (Classical CV) đối với hiệu năng của mạng Deep Learning thông qua chuỗi thực nghiệm Ablation Study có kiểm soát.
- **Mục tiêu triển khai**: Xây dựng bản mẫu phần mềm hoàn chỉnh, cung cấp giao diện trực quan cho bác sĩ kèm bản đồ nhiệt Grad-CAM giải thích quyết định dự đoán.

---

## CHƯƠNG 2: CƠ SỞ KHOA HỌC VÀ MIỀN NGHIỆP VỤ (DOMAIN KNOWLEDGE)

### 2.1. Sinh lý học Quá trình Cốt hóa Nội sụn (Endochondral Ossification)
Hệ xương bàn tay của trẻ em phát triển theo trình tự sinh học nghiêm ngặt:
1. **Giai đoạn sơ sinh (< 12 tháng)**: Phần lớn cấu trúc bàn tay là sụn cản quang kém, chỉ thấy thân xương bàn và thân các đốt ngón tay. Các hạt cốt hóa xương cổ tay bắt đầu xuất hiện tuần tự (xương Cả - Capitate và xương Móc - Hamate xuất hiện đầu tiên khoảng tháng thứ 3–6).
2. **Giai đoạn tiền dậy thì (1 – 10 tuổi)**: Các xương cổ tay lần lượt cốt hóa theo thứ tự: Tháp (Triquetrum) $\to$ Nguyệt (Lunate) $\to$ Thang (Trapezium) $\to$ Thê (Trapezoid) $\to$ Đậu (Pisiform). Các chỏm xương (Epiphyses) ở đầu ngón tay xuất hiện và phát triển về kích thước.
3. **Giai đoạn dậy thì (10 – 16 tuổi)**: Chỏm xương mở rộng bằng bề ngang thân xương, tạo thành các khe hẹp gọi là **đĩa sụn tăng trưởng (Growth Plate)**.
4. **Giai đoạn hoàn thiện (16 – 19 tuổi)**: Các đĩa sụn tiếp hợp cốt hóa hoàn toàn và đóng kín (Fusion). Đầu dưới xương quay (Distal Radius) là cấu trúc cuối cùng đóng sụn tiếp hợp.

```
TIẾN TRÌNH CỐT HÓA BÀN TAY THEO LỨA TUỔI:
[0 - 2 tuổi]  : Cốt hóa các hạt xương cổ tay đầu tiên (Capitate, Hamate)
[3 - 9 tuổi]  : Hoàn thiện 8 xương cổ tay + mở rộng chỏm đốt ngón
[10 - 14 tuổi]: Đĩa sụn tiếp hợp đạt cực đại, biểu hiện khác biệt giới tính rõ rệt
[15 - 19 tuổi]: Sụn tiếp hợp ngón tay đóng kín dần -> Đầu xương quay hợp nhất
```

### 2.2. Hiện tượng Dị hình Giới tính (Sexual Dimorphism)
Trong quá trình phát triển xương, **bé gái luôn cốt hóa sớm hơn bé trai từ 1.5 đến 2 năm**, đặc biệt rõ rệt trong giai đoạn dậy thì:
- Bé gái thường hoàn thành cốt hóa toàn bộ vào khoảng 16 – 17 tuổi.
- Bé trai hoàn thành cốt hóa vào khoảng 18 – 19 tuổi.
- **Hệ quả thiết kế AI**: Nếu chỉ đưa ảnh X-quang vào mạng CNN mà không có thông tin giới tính, mô hình sẽ không thể phân biệt một bức ảnh sụn tiếp hợp bắt đầu đóng là của một bé gái 13 tuổi hay một bé trai 15 tuổi. Do đó, **biến Giới tính (Gender) là một thuộc tính lâm sàng bắt buộc phải tích hợp vào mô hình**.

---

## CHƯƠNG 3: PHÂN TÍCH TẬP DỮ LIỆU RSNA VÀ THỐNG KÊ LƯỢC ĐỒ MÀU (DATASET & HISTOGRAM ANALYSIS)

### 3.1. Cấu trúc Tập Dữ liệu RSNA Pediatric Bone Age
Nghiên cứu sử dụng tập dữ liệu chuẩn mực y khoa từ cuộc thi **RSNA Pediatric Bone Age Challenge**:
- **Quy mô tập huấn luyện**: $12,611$ ảnh X-quang bàn tay trái định dạng PNG.
- **Tập kiểm tra công khai**: $1,425$ ảnh.
- **Metadata**: Đi kèm file CSV gồm 3 trường cốt lõi:
  - `id`: Mã định danh bức ảnh (khớp với tên file ảnh).
  - `boneage`: Nhãn tuổi xương thực tế tính bằng **tháng** ($1 \le \text{boneage} \le 228$).
  - `male`: Biến nhị phân đại diện cho giới tính (`True`: Nam, `False`: Nữ).

### 3.2. Đặc tính Thống kê Dữ liệu (Exploratory Data Analysis - EDA)
1. **Phân bố Giới tính**:
   - Nam (Male): $6,833$ ảnh ($\approx 54.18\%$).
   - Nữ (Female): $5,778$ ảnh ($\approx 45.82\%$).
   - Tỷ lệ giới tính tương đối cân bằng, không xảy ra hiện tượng mất cân bằng lớp nghiêm trọng.
2. **Phân bố Tuổi xương (Target Distribution)**:
   - Giá trị trung bình: $\mu \approx 127.3$ tháng ($\approx 10.6$ tuổi).
   - Độ lệch chuẩn: $\sigma \approx 41.2$ tháng.
   - Khoảng phân vị: $Q_1 \approx 96$ tháng ($8$ tuổi), Median $\approx 132$ tháng ($11$ tuổi), $Q_3 \approx 156$ tháng ($13$ tuổi).
   - Phân bố dạng hình chuông (Bell curve) với đỉnh tập trung mạnh từ 90 đến 160 tháng (giai đoạn tiền dậy thì và dậy thì).
   - **Vùng thưa thớt dữ liệu**: Trẻ sơ sinh $< 24$ tháng và thanh thiếu niên $> 200$ tháng chiếm tỷ lệ nhỏ ($< 3\%$), đặt ra cảnh báo về nguy cơ phương sai dự đoán lớn ở hai cực phân phối.

### 3.3. Phân tích Chuyên sâu Lược đồ Mức xám (Histogram Analysis) & Vấn đề Cản quang
Phân tích lược đồ mức xám (Grayscale Histogram) của ảnh X-quang gốc cho thấy các vấn đề thị giác đặc thù:
1. **Phân bố Bimodal lệch cực độ (Extreme Bimodal Distribution)**:
   - Hơn $50\% - 65\%$ số lượng điểm ảnh tập trung sát giá trị $0$ (dải $[0, 20]$), đại diện cho vùng nền đen xung quanh bàn tay (nơi tia X xuyên thẳng không bị cản).
   - Dải mức xám của vùng bàn tay phân bố rải rác trong khoảng $[40, 230]$, trong đó:
     - Mô mềm (Soft tissue): Cản quang yếu, nằm ở dải mức xám thấp $[40, 90]$.
     - Cấu trúc xương (Cortical & Trabecular bone): Cản quang trung bình đến mạnh, nằm ở dải $[100, 210]$.
     - Dị vật kim loại / Chữ đánh dấu (Marker L/R): Cản quang tuyệt đối, tạo đỉnh nhọn ở dải $[240, 255]$.
2. **Thất bại của Histogram Equalization (HE) toàn cục**:
   - Nếu áp dụng thuật toán cân bằng lược đồ màu truyền thống (Global HE), hàm tích lũy xác suất (CDF) bị chi phối áp đảo bởi lượng pixel nền đen. Hệ quả là dải động bị kéo dãn sai lệch, vùng nền bị đẩy sáng kèm nhiễu hạt khuếch đại, trong khi độ tương phản giữa sụn và xương ở bàn tay bị nén phẳng, làm mất chi tiết ranh giới giải phẫu.
   - **Giải pháp bắt buộc**: Ứng dụng **CLAHE (Contrast Limited Adaptive Histogram Equalization)** nhằm chia nhỏ ảnh thành các ô lưới cục bộ, giới hạn độ dốc biến đổi tương phản (Clip Limit) để bảo tồn các đĩa sụn.

### 3.4. Chiến lược Phân chia Dữ liệu Tránh Thiên vị (Stratified Splitting)
Do sự kết hợp giữa tuổi và giới tính tạo ra các phân nhóm có đặc tính hình thái khác nhau, nhóm áp dụng kỹ thuật **Stratified Shuffle Split** phân tầng theo 2 tiêu chí đồng thời:
- Chia biến liên tục `boneage` thành $12$ bins tương ứng các giai đoạn phát triển: $[0, 12), [12, 24), \dots, [204, 228]$.
- Kết hợp với biến nhị phân `male` để tạo thành $24$ tầng phân loại riêng biệt ($12 \times 2$).
- Tỷ lệ phân bổ:
  - **Tập huấn luyện (Training Set)**: $80\%$ ($\approx 10,089$ ảnh).
  - **Tập kiểm định (Validation Set)**: $10\%$ ($\approx 1,261$ ảnh).
  - **Tập kiểm thử độc lập (Test Set)**: $10\%$ ($\approx 1,261$ ảnh).

---

## CHƯƠNG 4: THIẾT KẾ KIẾN TRÚC KỸ THUẬT HỆ THỐNG

Toàn bộ hệ thống được xây dựng theo một luồng xử lý khép kín, chuẩn hóa từ ảnh thô đến giá trị dự đoán tuổi xương.

```
+-----------------------------------------------------------------------------+
|                           HỆ THỐNG BONE AGE ASSESSMENT                      |
+-----------------------------------------------------------------------------+
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
┌───────────────────────┐                             ┌───────────────────────┐
│ Nhánh Ảnh X-quang     │                             │ Nhánh Lâm sàng        │
│ (Raw X-ray Image)     │                             │ (Patient Gender: M/F) │
└───────────┬───────────┘                             └───────────┬───────────┘
            │                                                     │
            ▼                                                     ▼
┌───────────────────────────────────────────┐         ┌───────────────────────┐
│ PIPELINE CLASSICAL COMPUTER VISION        │         │ GENDER EMBEDDING      │
│ 1. CLAHE (clip=3.0, grid=8x8)             │         │ 1-d -> Linear(32)     │
│ 2. Gaussian Filter (5x5, sigma=0)         │         │ -> BatchNorm1d        │
│ 3. Otsu Auto-Thresholding                 │         │ -> ReLU -> Linear(32) │
│ 4. Morphology Opening & Closing           │         │ -> Vector e_g in R^32 │
│ 5. Max Contour Bounding Box Crop (+2% pad)│         └───────────┬───────────┘
│ 6. Resize 512x512 & Normalize             │                     │
└───────────────────┬───────────────────────┘                     │
                    │                                             │
                    ▼                                             │
┌───────────────────────────────────────────┐                     │
│ CNN BACKBONE (Image Encoder)              │                     │
│ ResNet-50 (Stage 1-4) / EfficientNet-B4   │                     │
│ Global Average Pooling (GAP)              │                     │
│ Output: Feature Vector f_img in R^2048    │                     │
└───────────────────┬───────────────────────┘                     │
                    │                                             │
                    └──────────────────────┬──────────────────────┘
                                           │
                                           ▼
                    ┌───────────────────────────────────────────┐
                    │ LATE FUSION (Feature Concatenation)       │
                    │ z = [ f_img || e_g ] in R^(2048 + 32)     │
                    └──────────────────────┬────────────────────┘
                                           │
                                           ▼
                    ┌───────────────────────────────────────────┐
                    │ MULTI-STAGE REGRESSION HEAD               │
                    │ Linear(2080 -> 1024) + BN + ReLU + Drop   │
                    │ Linear(1024 -> 512)  + BN + ReLU + Drop   │
                    │ Linear(512 -> 1) (Linear Output)          │
                    └──────────────────────┬────────────────────┘
                                           │
                                           ▼
                    ┌───────────────────────────────────────────┐
                    │ PREDICTED BONE AGE y_hat (tháng tuổi)     │
                    │ + GRAD-CAM EXPLAINABILITY HEATMAP         │
                    └───────────────────────────────────────────┘
```

### 4.1. Pipeline Tiền xử lý Ảnh Cổ điển (Classical Computer Vision Pipeline)
Mục tiêu cốt lõi của tiền xử lý cổ điển là **chuẩn hóa độ tương phản** và **cắt bỏ toàn bộ vùng nền nhiễu/ký tự L-R** trước khi đưa vào mạng sâu.

#### Module 1: Cân bằng Lược đồ màu Thích ứng Cục bộ (CLAHE)
- **Nguyên lý toán học**: Ảnh được chia thành lưới $M \times N$ khối chữ nhật nhỏ (Tiles) kích thước $8 \times 8$. Lược đồ mức xám của từng tile được tính toán. Nhằm ngăn chặn khuếch đại nhiễu ở các vùng đồng nhất, một ngưỡng cắt $\beta$ (Clip Limit) được áp dụng:
  $$\beta = \frac{N_{x} \cdot N_{y}}{L} \left(1 + \frac{\alpha}{100}(S_{\max} - 1)\right)$$
  Phần diện tích lược đồ vượt quá $\beta$ được cắt đều và phân phối lại cho toàn bộ các bin khác. Giá trị điểm ảnh sau đó được nội suy song tuyến (Bilinear Interpolation) giữa các tile liền kề nhằm loại bỏ hiện tượng ranh giới khối (blocking artifact).
- **Tham số tối ưu**: $\text{clip\_limit} = 3.0$, $\text{tile\_grid\_size} = (8, 8)$.

#### Module 2: Lọc mượt Gaussian (Gaussian Blur)
- Giảm thiểu nhiễu lượng tử hóa và nhiễu hạt muối tiêu trước khi phân đoạn.
- Áp dụng nhân tích chập 2D:
  $$G(x, y) = \frac{1}{2\pi\sigma^2} \exp\left(-\frac{x^2 + y^2}{2\sigma^2}\right)$$
- Kích thước kernel: $5 \times 5$, $\sigma$ tính toán tự động theo độ rộng cửa sổ.

#### Module 3: Phân ngưỡng Tự động Otsu (Otsu's Thresholding)
- Tách tiền cảnh (bàn tay) khỏi hậu cảnh mà không cần gán cứng giá trị ngưỡng thủ công.
- Thuật toán tối ưu hóa tìm ngưỡng $t^*$ nhằm cực đại hóa phương sai liên lớp $\sigma_B^2(t)$:
  $$\sigma_B^2(t) = \omega_0(t)\omega_1(t)\left[\mu_0(t) - \mu_1(t)\right]^2$$
  Trong đó $\omega_0, \omega_1$ lần lượt là xác suất xuất hiện của nền và đối tượng; $\mu_0, \mu_1$ là giá trị mức xám trung bình của hai vùng tương ứng.

#### Module 4: Biến đổi Hình thái học (Morphological Cleaning)
- Ảnh nhị phân sau Otsu thường chứa các thành phần nhiễu tách rời (nhãn chỉ định Left/Right của máy X-quang, dị vật kim loại, thước đo cản quang) và các lỗ khuyết mô mềm.
- Áp dụng **Phép mở (Morphological Opening)** với phần tử cấu trúc chữ nhật $B_{5 \times 5}$ để xóa bỏ chữ và dị vật:
  $$A \circ B = (A \ominus B) \oplus B$$
- Áp dụng **Phép đóng (Morphological Closing)** để lấp đầy các khoảng khuyết biểu mô bên trong lòng bàn tay:
  $$A \bullet B = (A \oplus B) \ominus B$$

#### Module 5: Trích xuất Đường bao & Định vị Bàn tay (Contour Detection & ROI Crop)
- Sử dụng thuật toán dò biên Suzuki để trích xuất tập hợp các đường bao ngoài: $\mathcal{C} = \{C_1, C_2, \dots, C_k\}$.
- Lựa chọn đường bao có diện tích lớn nhất: $C^* = \arg\max_{C \in \mathcal{C}} \text{Area}(C)$.
- Xác định hộp bao tối thiểu (Bounding Box): $(x, y, w, h)$.
- Mở rộng biên an toàn một lượng đệm $\text{pad} = 0.02 \times \max(w, h)$ nhằm đảm bảo không vô tình cắt xén các mấu lồi đốt ngón xa (Distal Phalanges).
- Cắt và resize vùng bàn tay về kích thước chuẩn ($512 \times 512$ đối với ResNet-50 hoặc $380 \times 380$ đối với EfficientNet-B4).

---

### 4.2. Kiến trúc Mạng Nơ-ron Sâu Đa Phương Thức (Multimodal Deep Learning)

Mô hình được thiết kế theo nguyên lý **Late Fusion**, cho phép trích xuất đặc trưng hình thái học độc lập với đặc trưng lâm sàng trước khi hợp nhất.

#### A. Nhánh Trích xuất Đặc trưng Thị giác (Image Feature Extractor)
1. **Mô hình Cơ sở (Baseline Backbone) — ResNet-50**:
   - Sử dụng cơ chế kết nối tắt phần dư (Residual Skip Connection): $\mathbf{y} = \mathcal{F}(\mathbf{x}, \{W_i\}) + \mathbf{x}$.
   - Giải quyết triệt để vấn đề suy biến gradient (Vanishing Gradient) khi huấn luyện mạng sâu.
   - Trích xuất bản đồ đặc trưng cuối cùng kích thước $C=2048, H=16, W=16$.
   - Tầng **Global Average Pooling (GAP)** chuyển đổi toàn bộ bản đồ đặc trưng thành vector $1\text{D}$ chiều dài $2048$:
     $$f_{\text{img}}^k = \frac{1}{H \times W} \sum_{i=1}^H \sum_{j=1}^W A^k_{i, j}$$
2. **Mô hình Nâng cao (Advanced Backbone) — EfficientNet-B4**:
   - Áp dụng nguyên lý mở rộng đồng bộ (Compound Scaling) cân bằng giữa chiều sâu ($\alpha$), chiều rộng kênh ($\beta$) và độ phân giải ảnh vào ($\gamma$):
     $$\text{depth}: d = \alpha^\phi, \quad \text{width}: w = \beta^\phi, \quad \text{resolution}: r = \gamma^\phi$$
     thỏa mãn điều kiện $\alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$.
   - Khối cấu trúc MBConv (Mobile Inverted Bottleneck Convolution) kết hợp cơ chế chú ý kênh Squeeze-and-Excitation (SE Block).
   - Cho vector đặc trưng đầu ra kích thước $1792$ chiều với số lượng tham số chỉ $\approx 19.3\text{M}$ (nhỏ hơn ResNet-50 có $\approx 25.6\text{M}$ tham số nhưng độ chính xác cao hơn rõ rệt).

#### B. Nhánh Mã hóa Đặc trưng Giới tính (Gender Embedding Branch)
- Nếu chỉ dùng một số thực đơn lẻ ($0.0$ hoặc $1.0$) ghép trực tiếp vào vector ảnh $2048$ chiều, thông tin giới tính sẽ bị "nuốt chửng" hoàn toàn trong quá trình lan truyền tiến và tính toán đạo hàm.
- Giải pháp: Xây dựng một mạng nơ-ron truyền thẳng (MLP) nhỏ để chiếu giá trị nhị phân vào không gian biểu diễn liên tục $32$ chiều:
  $$\mathbf{e}_g = \text{ReLU}\left(\mathbf{W}_2 \cdot \text{ReLU}\left(\text{BatchNorm}(\mathbf{W}_1 \cdot g + \mathbf{b}_1)\right) + \mathbf{b}_2\right)$$
  với $\mathbf{W}_1 \in \mathbb{R}^{32 \times 1}$, $\mathbf{W}_2 \in \mathbb{R}^{32 \times 32}$. Không gian này cho phép mô hình học được mối tương quan phi tuyến giữa giới tính và các trạng thái cốt hóa khác nhau.

#### C. Tầng Hợp nhất và Đầu Hồi quy Đa tầng (Fusion & Regression Head)
- **Cơ chế Late Fusion**: Ghép nối trực tiếp hai vector đặc trưng:
  $$\mathbf{z} = [\mathbf{f}_{\text{img}} \,\|\, \mathbf{e}_g] \in \mathbb{R}^{D + 32}$$
  ($D = 2048$ với ResNet-50; $D = 1792$ với EfficientNet-B4).
- **Khối hồi quy nén dần (Hierarchical Regression Head)**:
  - Tầng 1: $\text{Linear}(D+32 \to 1024) \to \text{BatchNorm1d} \to \text{ReLU} \to \text{Dropout}(p=0.3)$
  - Tầng 2: $\text{Linear}(1024 \to 512) \to \text{BatchNorm1d} \to \text{ReLU} \to \text{Dropout}(p=0.3)$
  - Tầng 3: $\text{Linear}(512 \to 1)$ — Đầu ra tuyến tính trực tiếp là tuổi xương dự đoán $\hat{y}$ (tháng).

---

### 4.3. Hàm Mất mát và Chiến lược Tối ưu hóa (Loss Function & Optimization)

#### A. Hàm Mất mát Kháng Ngoại lai Smooth L1 (Huber Loss)
Trong bài toán hồi quy tuổi xương, dữ liệu y tế luôn tồn tại các ca dị tật bẩm sinh hoặc nhãn bị sai lệch nhẹ (Label Noise).
- Hàm mất mát sai số toàn phương (MSE / $L_2$) có đạo hàm tỷ lệ thuận với độ lỗi ($2|y - \hat{y}|$), dẫn đến việc mô hình bị kéo lệch quá mức bởi các điểm dị biệt (Outliers).
- Hàm mất mát sai số tuyệt đối (MAE / $L_1$) có đạo hàm hằng số, nhưng không khả vi liên tục tại điểm $0$, dễ gây dao động quanh điểm cực tiểu.
- **Lựa chọn tối ưu**: Áp dụng **Smooth L1 Loss (Huber Loss)** với ngưỡng $\delta = 1.0$:
  $$\mathcal{L}_{\delta}(y, \hat{y}) = \begin{cases} 
  \frac{1}{2}(y - \hat{y})^2 & \text{khi } |y - \hat{y}| \le \delta \\
  \delta |y - \hat{y}| - \frac{1}{2}\delta^2 & \text{khi } |y - \hat{y}| > \delta
  \end{cases}$$
  Hàm loss này hoạt động như $L_2$ khi sai số nhỏ (hội tụ êm, khả vi liên tục) và chuyển thành $L_1$ khi sai số lớn (bền vững trước các ca outlier).

#### B. Chiến lược Huấn luyện 2 Giai đoạn (Two-Stage Transfer Learning)
Nhằm bảo vệ trọng số đã được tiền huấn luyện trên ImageNet khỏi hiện tượng phá hủy đặc trưng (Catastrophic Forgetting):
- **Giai đoạn 1 — Warm-up Regression Head (10 Epochs)**:
  - Đóng băng (Freeze) toàn bộ các tầng trọng số của CNN Backbone.
  - Chỉ tính toán gradient và cập nhật cho Gender Encoder và Regression Head.
  - Tốc độ học (Learning Rate): $\eta = 10^{-3}$, Bộ tối ưu hóa: AdamW (`weight_decay=1e-4`).
- **Giai đoạn 2 — Full Fine-tuning (30 Epochs)**:
  - Mở khóa (Unfreeze) toàn bộ mạng nơ-ron.
  - Huấn luyện end-to-end với tốc độ học nhỏ hơn gấp 10 lần: $\eta = 10^{-4}$.
  - Kết hợp bộ điều chỉnh tốc độ học theo chu kỳ Cosine (**Cosine Annealing Learning Rate Scheduler**):
    $$\eta_t = \eta_{\min} + \frac{1}{2}(\eta_{\max} - \eta_{\min})\left(1 + \cos\left(\frac{T_{cur}}{T_{\max}}\pi\right)\right)$$
  - Sử dụng cơ chế ngắt sớm (**Early Stopping**) nếu chỉ số MAE trên tập Validation không cải thiện sau 7 epochs liên tiếp.

#### C. Chiến lược Tăng cường Dữ liệu An toàn Y tế (Medical-Safe Augmentation)
Khác với ảnh tự nhiên thông thường, việc tăng cường ảnh X-quang y tế phải tuân thủ nghiêm ngặt tính hợp lý giải phẫu:
- **Biến đổi hợp lệ**:
  - `HorizontalFlip(p=0.5)`: Hợp lệ do cấu trúc bàn tay đối xứng trục cơ thể.
  - `Rotate(limit=10, p=0.5)`: Mô phỏng góc đặt tay của bệnh nhi bị nghiêng nhẹ khi chụp.
  - `RandomBrightnessContrast(limit=0.1, p=0.3)`: Mô phỏng sự khác biệt nhỏ về cường độ phát tia X giữa các đời máy chụp.
- **Biến đổi cấm**:
  - *Vertical Flip (Lộn ngược)*: Sai lệch giải phẫu lâm sàng.
  - *RandomCrop mạnh*: Nguy cơ làm mất đốt ngón tay hoặc xương cổ tay.
  - *ColorJitter*: Phá hủy thang xám cản quang sinh học.

---

## CHƯƠNG 5: THIẾT KẾ MODULE GIẢI THÍCH MÔ HÌNH (EXPLAINABLE AI - GRAD-CAM)

### 5.1. Cơ sở Toán học Grad-CAM cho Bài toán Hồi quy (Regression Grad-CAM)
Để đảm bảo tính tin cậy y khoa, bác sĩ cần hiểu được căn cứ đưa ra dự đoán của mạng Deep Learning. Thuật toán **Grad-CAM (Gradient-weighted Class Activation Mapping)** được tùy biến cho bài toán hồi quy (đầu ra là một đại lượng vô hướng $\hat{y}$ thay vì lớp phân loại):
1. **Tính trọng số đóng góp của kênh đặc trưng**:
   Tính đạo hàm của giá trị tuổi xương dự đoán $\hat{y}$ theo từng điểm ảnh tại bản đồ kích hoạt $A^k$ ở tầng tích chập cuối cùng:
   $$\alpha_k = \frac{1}{Z} \sum_{i=1}^H \sum_{j=1}^W \frac{\partial \hat{y}}{\partial A^k_{i, j}}$$
   với $Z = H \times W$ là diện tích bản đồ đặc trưng.
2. **Tổng hợp Bản đồ Nhiệt (Heatmap Generation)**:
   Kết hợp tuyến tính các bản đồ đặc trưng với trọng số $\alpha_k$, đi qua hàm kích hoạt $\text{ReLU}$ nhằm chỉ giữ lại các đặc trưng có tác động làm tăng giá trị tuổi xương:
   $$L_{\text{Grad-CAM}} = \text{ReLU}\left(\sum_{k} \alpha_k A^k\right)$$
3. **Phủ bản đồ nhiệt lên ảnh gốc (Overlay Visualization)**:
   Nội suy song tuyến $L_{\text{Grad-CAM}}$ về kích thước gốc của ảnh X-quang, chuẩn hóa về dải $[0, 1]$ và áp dụng bảng màu JET (Đỏ: Vùng chú ý cao nhất $\to$ Xanh: Không chú ý).

### 5.2. Tiêu chuẩn Đánh giá Tính Hợp lệ Lâm sàng (Clinical Sanity Check)
Bản đồ Grad-CAM sẽ được đối chiếu trực tiếp với các tiêu chuẩn của phương pháp Tanner-Whitehouse (TW3):
- **Trường hợp Trẻ nhỏ (< 10 tuổi)**: Vùng nhiệt đỏ rực PHẢI tập trung tại **8 hạt xương cổ tay (Carpal bones)** — đây là nơi diễn ra cốt hóa mạnh nhất ở lứa tuổi này.
- **Trường hợp Trẻ vị thành niên (10 – 16 tuổi)**: Vùng nhiệt PHẢI chuyển dịch lên các **đĩa sụn tiếp hợp ở đầu đốt ngón (Phalangeal Epiphyses)** để theo dõi mức độ đóng sụn.
- **Phát hiện Bẫy học đường tắt (Shortcut Learning Detection)**: Nếu Grad-CAM hiển thị vùng kích hoạt đỏ tại chữ chỉ thị góc ảnh (L/R) hoặc vùng nền đen, chứng tỏ mô hình đang dự đoán dựa trên nhiễu biên chứ không học tri thức giải phẫu $\to$ Hệ thống sẽ đưa ra cảnh báo không tin cậy.

---

## CHƯƠNG 6: THIẾT KẾ ỨNG DỤNG LÂM SÀNG (WEB APP STREAMLIT)

### 6.1. Kiến trúc Tương tác và Trải nghiệm Người dùng (UX/UI)
Hệ thống được đóng gói thành một Web Application tương tác dành cho bác sĩ nhi khoa, xây dựng trên nền tảng **Streamlit**:
- **Cột Trái — Bảng Điều khiển Nhập liệu (Input Console)**:
  - Khung tải ảnh X-quang (hỗ trợ kéo thả các định dạng DICOM/PNG/JPG).
  - Nút chọn Giới tính bệnh nhi (`Male` / `Female`).
  - Hộp nhập Tuổi thực tế theo giấy khai sinh (tháng).
  - Nút kích hoạt chẩn đoán `[🔍 Phân Tích Tuổi Xương]`.
- **Cột Phải — Bảng Kết quả Chẩn đoán (Diagnostic Dashboard)**:
  - Thẻ hiển thị số đo tuổi xương dự đoán (nổi bật, cỡ chữ lớn: `132.5 tháng` $\approx$ `11 tuổi 0.5 tháng`).
  - Chỉ số chênh lệch: $\Delta = \text{Tuổi xương} - \text{Tuổi thật}$.
  - Nhãn trạng thái màu tương ứng:
    - 🟢 **Xanh lá**: $|\Delta| \le 12 \text{ tháng}$ $\to$ "Tốc độ phát triển xương bình thường".
    - 🟡 **Vàng**: $12 < |\Delta| \le 24 \text{ tháng}$ $\to$ "Có dấu hiệu bất thường, đề nghị theo dõi định kỳ".
    - 🔴 **Đỏ**: $|\Delta| > 24 \text{ tháng}$ $\to$ "Bất thường nghiêm trọng! Đề nghị hội chẩn chuyên khoa nội tiết nhi".
  - Hiển thị trực quan cặp ảnh: Ảnh X-quang gốc song song với Ảnh bản đồ nhiệt Grad-CAM.

### 6.2. Tích hợp Biểu đồ Tăng trưởng Chuẩn WHO (WHO Growth Standards Chart)
Hệ thống tích hợp bảng tra cứu và thuật toán tính toán đường cong bách phân vị chiều cao theo tuổi xương dựa trên dữ liệu chuẩn của **Tổ chức Y tế Thế giới (WHO Anthro Standards)**:
- Đồ thị biểu diễn các đường chuẩn độ lệch chuẩn: $Z = -2, -1, 0, +1, +2$.
- Điểm đánh dấu (Marker) tọa độ của bệnh nhi được định vị trực tiếp trên đồ thị.
- Hỗ trợ bác sĩ ngoại suy và dự báo chiều cao tiềm năng khi trẻ trưởng thành (Adult Height Prediction).

---

## CHƯƠNG 7: KẾ HOẠCH THỰC NGHIỆM VÀ ĐÁNH GIÁ (EXPERIMENT PROTOCOL)

### 7.1. Chuỗi Thí nghiệm Đóng góp Thành phần (Ablation Study Matrix)
Để chứng minh một cách khoa học tính cần thiết của từng khối kỹ thuật trước hội đồng phản biện tại DUT, nhóm thiết kế 4 kịch bản thực nghiệm lũy tiến:

| Mã TN | Tên Thí nghiệm | CNN Backbone | Tiền xử lý Ảnh | Biến Giới tính | Hàm Loss | Mục tiêu / Kỳ vọng |
|:---:|:---|:---|:---|:---:|:---:|:---|
| **E0** | Raw Baseline | ResNet-50 | Resize thô (không CLAHE, không Crop) | ❌ Không | MSE ($L_2$) | Thiết lập đường cơ sở tối thiểu. MAE kỳ vọng: $\approx 10 - 12$ tháng. |
| **E1** | + Classical CV | ResNet-50 | **Pipeline 5 bước (CLAHE + Otsu Crop)** | ❌ Không | MSE ($L_2$) | Định lượng đóng góp của xử lý ảnh cổ điển. MAE kỳ vọng: $\approx 8 - 9$ tháng. |
| **E2** | + Gender Fusion | ResNet-50 | Pipeline 5 bước | **✅ Có (Embedding 32-d)** | **Smooth L1** | Đánh giá vai trò của giới tính và hàm loss kháng ngoại lai. MAE kỳ vọng: $\approx 6 - 7$ tháng. |
| **E3** | + EfficientNet | **EfficientNet-B4** | Pipeline 5 bước | ✅ Có (Embedding 32-d) | Smooth L1 | Tối ưu hóa kiến trúc nâng cao. MAE kỳ vọng: $\approx \mathbf{4.5 - 5.5}$ tháng. |

*Ghi chú*: Tất cả các thực nghiệm đều chạy trên cùng một bộ phân chia dữ liệu cố định (`seed=42`), cùng số epoch và cùng tập tham số bộ tối ưu.

### 7.2. Thang đo Đánh giá Hiệu năng (Evaluation Metrics)
1. **Sai số Tuyệt đối Trung bình — MAE (Chỉ số cốt lõi)**:
   $$\text{MAE} = \frac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i| \quad (\text{đơn vị: tháng})$$
2. **Căn bậc hai Sai số Toàn phương Trung bình — RMSE**:
   $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2}$$
3. **Hệ số Xác định — $R^2$ Score**:
   $$R^2 = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2}$$
4. **Đánh giá Sai số Phân tầng (Stratified Error Analysis)**:
   - MAE tính riêng theo từng nhóm tuổi: $0-5$ tuổi, $5-10$ tuổi, $10-15$ tuổi, $15-19$ tuổi.
   - MAE tính riêng theo giới tính: Nam so với Nữ.

---

## CHƯƠNG 8: TỔ CHỨC DỰ ÁN, PHÂN PHỐI PHẦN CỨNG VÀ LỘ TRÌNH TRIỂN KHAI

### 8.1. Cấu hình Hạ tầng Tính toán và Biện pháp Thích ứng Phần cứng
Nhóm sở hữu tài nguyên phần cứng gồm:
- **Máy trạm cá nhân**: Laptop GPU NVIDIA GeForce RTX 3050 (4GB VRAM).
- **Điện toán Đám mây**: Google Colab T4 GPU (16GB VRAM, giới hạn phiên $\approx 12$ giờ/lần).

**Chiến lược tối ưu hóa bộ nhớ GPU (VRAM Optimization Matrix)**:
1. **Huấn luyện với độ chính xác hỗn hợp (Automatic Mixed Precision - AMP)**: Sử dụng kiểu dữ liệu FP16 cho quá trình lan truyền tiến và đạo hàm ngược, giữ FP32 cho cập nhật trọng số (`torch.cuda.amp.autocast()`). Kỹ thuật này giúp giảm **$50\%$ dung lượng VRAM** và tăng tốc độ xử lý lên gấp $2.2$ lần.
2. **Cơ chế Tiền lưu trữ (Data Pre-caching)**: Toàn bộ pipeline tiền xử lý ảnh cổ điển (CLAHE + Otsu Crop) được chạy trước một lần duy nhất trên máy local, lưu kết quả ảnh đã nén thành các tệp nhị phân nén. Quá trình nạp dữ liệu khi huấn luyện không phải tính toán lại bước này, triệt tiêu hiện tượng nghẽn cổ chai CPU.
3. **Phân chia nhiệm vụ theo năng lực phần cứng**:
   - Máy RTX 3050: Phát triển module tiền xử lý OpenCV, chạy kiểm thử cú pháp mã nguồn, debug mô hình với tập dữ liệu nhỏ (`batch_size=8`, ảnh $224 \times 224$), kiểm thử giao diện Streamlit.
   - Google Colab T4: Chạy toàn bộ quá trình huấn luyện chính thức các thực nghiệm E0 $\to$ E3 với độ phân giải đầy đủ ($380 \times 380$ hoặc $512 \times 512$, `batch_size=16 - 32`).

### 8.2. Phân công Trách nhiệm Nhân sự (Role Allocation)

```
+-----------------------------------------------------------------------------+
|                          PHÂN CÔNG VAI TRÒ DỰ ÁN                            |
+-----------------------------------------------------------------------------+
|  SINH VIÊN 1: Data & Classical CV Lead      |  SINH VIÊN 2: Deep Learning & |
|                                             |               Deployment Lead |
+---------------------------------------------+-------------------------------+
| - Quản trị và khai phá dữ liệu RSNA (EDA)   | - Thiết kế kiến trúc nơ-ron   |
| - Xây dựng Pipeline tiền xử lý Classical CV |   Multimodal Late Fusion      |
| - Thiết kế module trích xuất đặc trưng hình | - Xây dựng Training Engine,   |
|   thái học (CLAHE, Otsu, Morphology, Crop)  |   AMP, Checkpoint & Logging   |
| - Xây dựng PyTorch Dataset & Transforms     | - Triển khai Grad-CAM XAI     |
| - Phân tích sai số (Error Analysis)         | - Phát triển Web App Streamlit|
| - Soạn thảo báo cáo kỹ thuật phần dữ liệu   | - Tích hợp WHO Growth Chart   |
+-----------------------------------------------------------------------------+
```

### 8.3. Lộ trình Triển khai 4 Tuần (Sprint Breakdown)

#### Tuần 1: Khởi động, Khai phá Dữ liệu và Xây dựng Pipeline Xử lý Cổ điển
- Hoàn thành báo cáo phân tích lược đồ mức xám (Histogram Analysis) và các thống kê phân bố RSNA.
- Lập trình hoàn chỉnh 5 module Classical CV trong thư mục `src/preprocessing/`.
- Xuất bản bộ ảnh trực quan hóa so sánh Before/After cho từng giai đoạn xử lý.
- Chuẩn bị slide báo cáo tổng quan giai đoạn 1 (20 trang).

#### Tuần 2: Xây dựng Pipeline Dữ liệu và Thiết lập Baseline Thực nghiệm
- Hoàn thành module `BoneAgeDataset`, tích hợp tăng cường dữ liệu an toàn `Albumentations`.
- Chạy tiền xử lý và lưu trữ toàn bộ tập ảnh đã cắt bỏ nền.
- Huấn luyện thí nghiệm cơ sở **E0** (Raw ResNet-50 Baseline).
- Huấn luyện thí nghiệm **E1** (+ Classical CV Preprocessing) để kiểm chứng mức giảm MAE.
- Tích hợp nhánh Gender Embedding và hoàn thành thí nghiệm **E2** (Multimodal ResNet-50).

#### Tuần 3: Tối ưu hóa Mạng Nâng cao và Triển khai Trí tuệ Nhân tạo Giải thích được
- Chuyển đổi sang backbone **EfficientNet-B4**, tinh chỉnh siêu tham số và huấn luyện thực nghiệm **E3**.
- Triển khai thuật toán **Grad-CAM** cho mô hình hồi quy, xuất bản đồ nhiệt đối chiếu với các vùng giải phẫu chuẩn TW3.
- Thực hiện phân tích sai số chuyên sâu: vẽ biểu đồ phân tán (Predicted vs Actual), biểu đồ phần dư (Residuals), và phân tích các trường hợp sai lệch lớn nhất.

#### Tuần 4: Phát triển Ứng dụng Web, Kiểm thử và Hoàn tất Hồ sơ Đồ án
- Lập trình giao diện Web App lâm sàng với Streamlit (`app/streamlit_app.py`).
- Nhúng module tra cứu và vẽ đường cong bách phân vị tăng trưởng theo chuẩn WHO.
- Kiểm thử tích hợp toàn diện từ khâu tải ảnh đến hiển thị Grad-CAM.
- Đóng gói mã nguồn theo chuẩn module hóa khoa học, biên tập video demo và hoàn thiện báo cáo đồ án.

---

## CHƯƠNG 9: PHÂN TÍCH RỦI RO VÀ PHƯƠNG ÁN DỰ PHÒNG (RISK MATRIX)

| # | Rủi ro Kỹ thuật | Xác suất | Tác động | Phương án Giảm thiểu / Giải pháp Dự phòng |
|:-:|:---|:---:|:---:|:---|
| 1 | **Google Colab hết hạn ngạch GPU (Quota Limit)** khi đang huấn luyện dang dở | Cao (60%) | Lớn | - Lưu Checkpoint (`best_model.pth` và `last_checkpoint.pth`) định kỳ sau mỗi epoch lên Google Drive.<br>- Chuẩn bị sẵn 2 tài khoản Google dự phòng.<br>- Kích hoạt Mixed Precision (FP16) để rút ngắn tối đa thời gian huấn luyện. |
| 2 | **Tràn bộ nhớ VRAM trên Laptop RTX 3050 (Out Of Memory - OOM)** | Trung bình (40%) | Trung bình | - Không huấn luyện toàn bộ tập dữ liệu trên máy cá nhân.<br>- Giới hạn kích thước ảnh test cục bộ ở mức $224 \times 224$ và `batch_size = 8`.<br>- Tận dụng lệnh `torch.cuda.empty_cache()` sau các bước đánh giá. |
| 3 | **Mô hình bị hiện tượng Học đường tắt (Shortcut Learning)** | Trung bình (30%) | Rất lớn | - Khâu tiền xử lý Otsu + Contour Crop loại bỏ hoàn toàn các góc chứa chữ L/R.<br>- Giám sát liên tục bằng bản đồ nhiệt Grad-CAM; nếu phát hiện vùng nhiệt rơi vào góc ảnh, lập tức bổ sung bước xóa chữ (Text Inpainting). |
| 4 | **Sai số dự đoán cao ở nhóm trẻ sơ sinh (< 12 tháng)** | Cao (70%) | Trung bình | - Về mặt sinh học, trẻ dưới 1 tuổi chưa xuất hiện nhiều trung tâm cốt hóa nên hình thái X-quang rất khó phân biệt.<br>- Giải pháp: Tách riêng bảng đánh giá sai số cho nhóm này, phân tích nguyên nhân sinh lý học trong báo cáo như một giới hạn tự nhiên của phương pháp X-quang bàn tay. |

---

## KẾT LUẬN VÀ CAM KẾT ĐẦU RA

Bản thiết kế kỹ thuật này cung cấp một khuôn khổ khoa học toàn diện, khả thi và bám sát các yêu cầu thực tế của học phần Computer Vision tại Trường Đại học Bách Khoa — ĐH Đà Nẵng. Dự án không chỉ dừng lại ở việc áp dụng một mô hình Deep Learning có sẵn, mà kết hợp hài hòa và làm nổi bật sức mạnh của **các giải thuật xử lý ảnh cổ điển (Classical CV)**, tính chuẩn mực của **nghiệp vụ y khoa lâm sàng**, và sự minh bạch trong quyết định chẩn đoán thông qua **Explainable AI**.

Toàn bộ kế hoạch đã được tối ưu hóa tương thích với điều kiện phần cứng hiện có của nhóm và cam kết hoàn thành đúng tiến độ đề ra.
