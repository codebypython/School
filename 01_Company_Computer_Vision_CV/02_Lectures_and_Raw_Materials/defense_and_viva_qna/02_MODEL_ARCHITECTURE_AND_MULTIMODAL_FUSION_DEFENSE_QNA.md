# 🎓 BỘ CÂU HỎI VÀ ĐÁP ÁN BẢO VỆ ĐỒ ÁN CHUYÊN SÂU — PHẦN 2
## 🧠 KIẾN TRÚC MÔ HÌNH ĐỐI ĐẦU & DUNG HỢP ĐA PHƯƠNG THỨC (TRI-MODEL COMPARISON & MULTIMODAL FUSION)
**Đơn vị nghiên cứu: VisionLab Corp (CORP-01-CV) — Chuẩn Học Thuật Đại Học Bách Khoa (DUT)**

---

### 🎯 CÂU HỎI VÀNG 01: VÌ SAO SWIN TRANSFORMER LẠI ĐẠT MAE 38.56 THÁNG TRONG KHI RESNET-50 ĐẠT 7.38 THÁNG?
> **Câu hỏi của Hội đồng phản biện:**  
> *"Theo xu hướng AI hiện nay, Vision Transformer (ViT / Swin-T) được coi là kiến trúc tối tân vượt trội hơn CNN cổ điển (ResNet). Tuy nhiên, trong kết quả thực nghiệm 15 epochs của nhóm, Swin Transformer v2 chỉ đạt MAE = 38.56 tháng (~3.2 tuổi), trong khi ResNet-50 đạt kết quả vượt bậc MAE = 7.38 tháng (~0.61 tuổi). Nhóm hãy giải thích bản chất toán học và kiến trúc sâu xa của hiện tượng này?"*

#### 💡 Câu Trả Lời Chuẩn Mực Dành Cho Sinh Viên (Defense Script):

**Kính thưa Thầy/Cô và Hội đồng, đây là một trong những phát hiện thực nghiệm đắt giá nhất của đề tài, phản ánh chính xác bản chất học máy giữa hai trường phái mạng:**

#### 1. Sự hiện diện và thiếu hụt của "Định kiến quy nạp" (Inductive Bias)
* **ResNet-50 (Trường phái CNN):** Mạng CNN sở hữu hai định kiến quy nạp cấu trúc cực mạnh được cài đặt cứng vào các bộ lọc tích chập (Convolutional Kernels):
  1. *Tính cục bộ không gian (Spatial Locality):* Các pixel lân cận có mối tương quan hình thái cao.
  2. *Tính bất biến tịnh tiến (Translation Invariance):* Một đĩa sụn hay bè xương dù nằm ở vị trí nào trên bàn tay cũng được nhận diện bởi cùng một bộ lọc chia sẻ trọng số (weight sharing).
  $\rightarrow$ Nhờ Inductive Bias mạnh mẽ này, ResNet-50 có thể khái quát hóa các đặc trưng giải phẫu cực nhanh chỉ sau một vài epoch đầu tiên ngay cả trên tập dữ liệu y tế quy mô vừa (~10.000 ca).
* **Swin Transformer (Trường phái Self-Attention):** Mạng Transformer hoàn toàn **không có Inductive Bias cục bộ**. Nó đối xử với mọi patch ảnh ban đầu một cách bình đẳng và phải tự học mối quan hệ tương quan giữa các vùng thông qua ma trận chú ý (Self-Attention Matrix $\text{softmax}(QK^T/\sqrt{d})V$).
  $\rightarrow$ Do đó, Vision Transformer nổi tiếng là kiến trúc **cực kỳ "đói dữ liệu" (Data-Hungry)**. Với tập dữ liệu y tế thực tế chỉ có 10.088 ảnh huấn luyện và giới hạn 15 epochs, Swin-T mới chỉ bắt đầu học được phân bố vĩ mô toàn cục (Loss giảm từ 123 xuống 24) chứ chưa đủ chu kỳ để tinh chỉnh vào các viền sụn tí hon.

#### 2. Đặc thù của bài toán Hồi quy Tuổi xương Lâm sàng
* Các mốc cốt hóa lâm sàng (theo phương pháp Tanner-Whitehouse TW3) nằm ở các chi tiết giải phẫu cực nhỏ: độ hẹp của khe sụn tiếp hợp ở các đốt ngón tay xa (distal phalanges) và đường viền của 8 xương cổ tay (carpal bones), chỉ chiếm kích thước vài pixel.
* Swin-T chia ảnh thành các patch $4 \times 4$ và tính attention trong các cửa sổ cục bộ $7 \times 7$. Khi chuyển qua các tầng sau, cơ chế Shifted Window gom cụm các đặc trưng toàn thể rất tốt cho bài toán phân loại tổng quát (Classification), nhưng đối với bài toán hồi quy liên tục đòi hỏi chi tiết biên vi mô (micro-edge regression), Swin-T cần ít nhất 50 - 100 epochs kèm các kỹ thuật tiền huấn luyện tự giám sát (như SimMIM hoặc Masked Autoencoder) mới phát huy tối đa sức mạnh.

#### 3. Kết luận mang tính học thuật cao
* **Bài học kinh nghiệm thực tiễn:** Trong kỹ thuật thị giác máy tính y tế, *không phải mô hình nào mới hơn, phức tạp hơn cũng mang lại hiệu năng cao hơn*. Khi tài nguyên huấn luyện và dữ liệu bị giới hạn trong môi trường bệnh viện, các kiến trúc CNN tối ưu hóa như ResNet-50 hoặc ConvNeXt vẫn là lựa chọn hàng đầu về tính thực tiễn và độ chính xác.

---

### 🎯 CÂU HỎI VÀNG 02: BẢN CHẤT LỖI `Exception ignored in: _MultiProcessingDataLoaderIter.__del__`
> **Câu hỏi của Hội đồng phản biện:**  
> *"Trong nhật ký huấn luyện của nhóm xuất hiện các cảnh báo ngoại lệ đỏ liên quan đến `_MultiProcessingDataLoaderIter.__del__` và `AssertionError: can only test a child process`. Điều này có làm sai lệch quá trình cập nhật gradient hay làm hỏng trọng số mô hình không?"*

#### 💡 Câu Trả Lời Chuẩn Mực Dành Cho Sinh Viên:
* **Khẳng định:** Hoàn toàn **KHÔNG** ảnh hưởng đến trọng số mô hình, gradient hay độ chính xác tính toán.
* **Bản chất kỹ thuật:** Đây là một hiện tượng tương thích đã được xác nhận (known behavior) giữa **Python 3.12** và cơ chế giải phóng tiến trình con (multiprocessing worker shutdown) trong **PyTorch DataLoader** khi thiết lập `num_workers > 0`:
  1. Khi một Epoch kết thúc, đối tượng lặp `DataLoaderIter` bị hủy, bộ thu gom rác (Garbage Collector) của CPython gọi phương thức hủy `__del__()` để đóng các worker.
  2. Tại thời điểm này, tiến trình cha kiểm tra trạng thái worker thông qua `w.is_alive()`. Trong cơ chế bảo vệ tiến trình chặt chẽ của Python 3.12 (`process.py:160`), hàm này yêu cầu xác thực PID của cha (`assert self._parent_pid == os.getpid()`). Do tiến trình con đã đóng trước đó nên phép assert này vấp ngoại lệ.
  3. Từ khóa **`Exception ignored in...`** chứng minh rằng Python đã cô lập ngoại lệ này trong hàm hủy ngầm và bỏ qua an toàn, vòng lặp huấn luyện chính vẫn tiếp tục chạy mượt mà từ Epoch 1 đến Epoch 15 và lưu file checkpoint bình thường.
