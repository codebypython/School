# 🎓 BỘ CÂU HỎI VÀ ĐÁP ÁN BẢO VỆ ĐỒ ÁN CHUYÊN SÂU — PHẦN 3
## ⚡ ĐỘNG HỌC HUẤN LUYỆN, SỐ LƯỢNG EPOCH & TỐI ƯU HÓA HỘI TỤ (TRAINING DYNAMICS & CONVERGENCE SATURATION)
**Đơn vị nghiên cứu: VisionLab Corp (CORP-01-CV) — Chuẩn Học Thuật Đại Học Bách Khoa (DUT)**

---

### 🎯 CÂU HỎI VÀNG 01: VÌ SAO THIẾT LẬP 15 EPOCHS? Ý NGHĨA KHOA HỌC & RÀNG BUỘC KỸ THUẬT
> **Câu hỏi của Hội đồng phản biện:**  
> *"Tại sao nhóm lại lựa chọn con số chính xác là 15 Epochs cho cả 3 mô hình? Vì sao không chọn ít hơn (ví dụ 5 epochs) để tiết kiệm thời gian, hoặc chọn nhiều hơn (ví dụ 30 - 50 epochs) để mô hình học sâu hơn? Liệu với 15 epochs thì 3 mô hình được lựa chọn (ResNet-50, ConvNeXt-Tiny, Swin-T) đã được huấn luyện triệt để hay chưa?"*

#### 💡 Câu Trả Lời Chuẩn Mực Dành Cho Sinh Viên (Defense Script):

**Kính thưa Thầy/Cô và Hội đồng, quyết định lựa chọn mốc 15 Epochs là một bài toán tối ưu hóa đa mục tiêu có chủ đích khoa học (Controlled Scientific Benchmark), cân bằng giữa 4 yếu tố then chốt:**

---

#### 1. Đánh giá mức độ "Triệt để" riêng biệt cho từng mô hình (Convergence Saturation Analysis)
Không phải mô hình nào cũng có tốc độ học và độ "đói dữ liệu" giống nhau. Con số 15 Epochs đem lại kết luận rất rõ ràng cho 3 trường phái:

* **Với M1: ResNet-50 (ĐÃ ĐỦ & ĐẠT ĐIỂM BÃO HÒA TRIỆT ĐỂ):**
  * ResNet-50 là mạng CNN có **Inductive Bias cực mạnh** (tính cục bộ không gian và bất biến tịnh tiến) kết hợp với trọng số khởi tạo chất lượng cao từ **ImageNet-1K**.
  * Trên thực nghiệm của nhóm, sau 12 - 15 epochs, sai số Val MAE giảm xuống mức **7.38 tháng** ($\sim 0.61$ tuổi) và đường cong Loss trên tập Validation bắt đầu đi ngang (Plateau).
  * Con số 7.38 tháng tiệm cận với **sai số tự nhiên giữa các bác sĩ chẩn đoán hình ảnh độc lập (Inter-observer variability)** vốn dao động từ $6 - 8$ tháng.
  * Nếu tiếp tục train lên 30 hay 50 epochs, ResNet-50 sẽ rơi vào bẫy **Overfitting** (Train Loss tiếp tục giảm nhưng Val MAE tăng lên do mô hình ghi nhớ cả các đốm nhiễu quang học của máy chụp). Do đó, với ResNet-50, **15 epochs là điểm dừng tối ưu hoàn hảo**.

* **Với M2: ConvNeXt-Tiny (ĐÃ ĐỦ ĐỂ ĐẠT ĐIỂM CÂN BẰNG TỐI ƯU):**
  * Tương tự ResNet-50, ConvNeXt vẫn giữ bản chất là mạng tích chập (Convolutional Backbone) với Depthwise 7x7. Tốc độ hội tụ của ConvNeXt rất nhanh và 15 epochs là hoàn toàn đủ để mô hình đạt mức sai số tối ưu ổn định quanh 7 - 9 tháng.

* **Với M3: Swin Transformer v2 (CHƯA TRIỆT ĐỂ NHƯNG CÓ Ý NGHĨA KHOA HỌC CAO):**
  * Swin-T thiếu Inductive Bias của CNN, hoạt động thuần túy dựa trên cơ chế Self-Attention.
  * Ở Epoch 14, Swin-T đạt MAE = 38.56 tháng. Dù Loss đã giảm sâu từ 123 xuống 24, nhưng nếu được cấp thêm 30 - 50 epochs và tập dữ liệu lớn hơn nhiều, Swin-T hoàn toàn có thể giảm thêm sai số.
  * **Tuy nhiên, sự "chưa triệt để" này chính là bằng chứng thực nghiệm quan trọng:** Nó phản ánh khái niệm **Hiệu suất mẫu (Sample Efficiency)**. Khi bị giới hạn cùng một ngân sách tính toán (Fixed Computational Budget = 15 Epochs), mạng CNN chứng minh hiệu suất học vượt trội hơn Vision Transformer trên tập dữ liệu y tế quy mô vừa.

---

#### 2. Vì sao không dùng Ít hơn (ví dụ 3 - 5 epochs)?
* Trong 3 - 5 epoch đầu tiên, mô hình chỉ mới học các đặc trưng cấp thấp (low-level features) như đường biên bao ngoài của bàn tay và phân bố mức xám toàn cục (đó là lý do ở Epoch 1-3 của Swin-T, MAE vẫn ở mức rất cao: $123 \rightarrow 107$ tháng).
* Bộ điều chỉnh tốc độ học **Cosine Annealing Scheduler** cần tối thiểu 10 - 15 epochs để Learning Rate suy giảm mềm mại từ $10^{-4}$ về $10^{-6}$, cho phép mạng "tinh chỉnh vi mô" (fine-tune) các trọng số ở tầng Fully Connected cuối cùng. Nếu dừng ở 5 epochs, mô hình chưa kịp thoát khỏi vùng cực tiểu cục bộ thô.

---

#### 3. Vì sao không dùng Nhiều hơn (ví dụ 30 - 50 epochs)?
Quyết định này xuất phát từ 2 ràng buộc kỹ thuật thực tế:

* **Rủi ro Overfitting (Quá khớp dữ liệu y tế):**  
  Thực nghiệm tại Epoch 15 của Swin-T đã chứng minh rõ điều này: Train Loss tiếp tục giảm từ $24.31 \rightarrow 23.89$, nhưng Val MAE đã bật ngược từ **$38.56 \rightarrow 43.75$ tháng**. Kéo dài số epoch sẽ kích hoạt hiện tượng "thuộc lòng dữ liệu train", làm mất khả năng tổng quát hóa trên bệnh nhi mới.
* **Ràng buộc tài nguyên tính toán (Kaggle Cloud Budget):**  
  * Mỗi epoch của Swin-T mất xấp xỉ **409 giây ($\sim 6.8$ phút)** trên GPU NVIDIA T4.
  * 15 epochs $\times 6.8$ phút $\approx \mathbf{102 \text{ phút}}$ ($\sim 1.7$ giờ).
  * Nếu tăng lên 50 epochs: $50 \times 6.8 \text{ phút} \approx \mathbf{340 \text{ phút}}$ ($\sim \mathbf{5.7 \text{ giờ}}$).
  * Trong khi đó, Kaggle giới hạn trần ngạch GPU miễn phí là **30 giờ / tuần**. Nếu chạy 3 mô hình đối đầu ở mức 50 epochs, dự án sẽ tiêu tốn hơn **$17.1 \text{ giờ}$** (chiếm gần $60\%$ quota tuần), tiềm ẩn nguy cơ cạn kiệt tài nguyên trước khi kịp chạy các tác vụ trích xuất bản đồ nhiệt Grad-CAM, benchmark và kiểm thử độc lập.

---

### 📊 BẢNG TỔNG HỢP HIỆU SUẤT HỌC THEO SỐ LƯỢNG EPOCH

| Số lượng Epochs | Trạng thái của ResNet-50 | Trạng thái của Swin Transformer | Mức độ rủi ro Overfitting | Mức tiêu hao Quota GPU Kaggle (3 mô hình) | Đánh giá khoa học |
|:---:|:---|:---|:---:|:---:|:---|
| **3 - 5 Epochs** | Chưa hội tụ hết, MAE còn cao (~15 - 20m) | Chưa kịp học, MAE rất lớn (>90m) | Cực thấp (Underfitting) | Rất nhẹ (~1.5 giờ) | ❌ Không đạt yêu cầu học thuật |
| **15 Epochs** *(Lựa chọn của đồ án)* | **Đạt điểm bão hòa hoàn hảo (MAE 7.38m)** | **Đạt cực tiểu tối ưu giai đoạn 1 (MAE 38.56m)** | **Cân bằng tối ưu (Chớm overfit tại epoch 15)** | **Hợp lý (~4.5 giờ tổng)** | **✅ Điểm cân bằng Pareto lý tưởng** |
| **30 - 50 Epochs** | Chắc chắn bị Overfitting nặng | Có thể giảm thêm MAE nhưng hội tụ chậm | Rất cao | Nguy cơ cạn quota GPU (>15 giờ) | ⚠️ Lãng phí tài nguyên tính toán |
