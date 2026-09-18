# 📜 ĐIỀU LỆ PHÒNG CHIẾN LƯỢC & LỘ TRÌNH ĐÀO TẠO (STRATEGY & CURRICULUM DEPT)
## Phòng 01 — Công Ty Công Nghệ Thị Giác Máy Tính (CORP-01-CV)

> **Mã Phòng Ban:** `CV-DEPT-01`  
> **Trưởng phòng phụ trách:** Agent `PSD-04` (Pedagogical Scaffolding Designer) & `ACD-01` (Academic Curriculum Director)  
> **Tiêu chuẩn học thuật:** Stanford CS231n / Szeliski Computer Vision 2nd / PyTorch 2.x Deep Vision

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Chiến Lược & Lộ Trình là **bộ não định hình khung đào tạo và kiến trúc kỹ thuật Thị giác máy tính**:
1. **Thiết Kế Khung Chương Trình & Kiến Trúc Hệ Thống Chuẩn**: Định hình giải pháp từ Xử lý ảnh không gian & tần số cổ điển $\rightarrow$ Trích xuất đặc trưng $\rightarrow$ Mạng nơ-ron tích chập CNNs $\rightarrow$ Multimodal Late Fusion & Vision Transformers.
2. **Chiến Lược Tác Chiến Phân Tầng Điện Toán (Hybrid Cloud-Local Strategy)**: 
   - **Định tuyến Tính toán Nặng sang Google Colab**: Tối ưu hóa pipeline để chạy trơn tru trên GPU Tesla T4 (16GB VRAM), thiết kế Two-Stage Transfer Learning và cơ chế ngắt sớm Early Stopping.
   - **Định vị Máy trạm Cục bộ làm Trung Tâm Điều Khiển (Local HQ)**: Giữ vai trò cung cấp tài liệu cốt lõi, chuẩn hóa thiết kế toán học, quản lý dữ liệu đối sánh và vận hành WebApp chẩn đoán lâm sàng.
3. **Loại Bỏ Tư Duy "Hộp Đen" (No-Magic Principle)**: Bắt buộc học viên hiểu rõ toán học giải tích phía sau phép tích chập 2D (Cross-correlation vs Convolution), ma trận Jacobian/Hessian, đạo hàm ngược (Backpropagation trên Tensor 4D).
4. **Đảm Bảo Chuẩn Đầu Ra Kỹ Sư Computer Vision**: Học viên có khả năng tự tay cài đặt mô hình, kiểm soát shape tensor, đối chuẩn kết quả với các bài báo quốc tế và đóng gói sản phẩm hoàn chỉnh.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (PEDAGOGICAL INVARIANTS)

1. **Tuân Thủ Mô Hình 4 Tầng Sư Phạm**:
   - Mọi tuần học bắt buộc phải có: *Tầng 1 (Bản chất quang học & Toán học)* $\rightarrow$ *Tầng 2 (Cài đặt PyTorch/OpenCV hiện đại)* $\rightarrow$ *Tầng 3 (⚠️ Cảnh báo CUDA OOM & Data Leakage)* $\rightarrow$ *Tầng 4 (Bài lab thực nghiệm)*.
2. **Quy Tắc Tensor Shape Rõ Ràng**:
   - Mọi bài giảng lý thuyết và slide phải luôn ghi chú kích thước Tensor `[B, C, H, W]` tại mọi bước biến đổi toán học.
3. **Quy Tắc Tách Biệt Data Pipeline**:
   - Nghiêm cấm áp dụng kỹ thuật Data Augmentation lên tập Validation hoặc Test set.

---

## 🛠️ 3. TOOLCHAIN & SKILLS ROUTE ĐÀO TẠO THỊ GIÁC MÁY TÍNH

| Hạng Mục | Bộ Công Cụ & Thước Đo | Mục Đích Sư Phạm |
| :--- | :--- | :--- |
| **Deep Learning Framework** | PyTorch 2.x, Torchvision, CUDA 12 | Xây dựng mạng nơ-ron và huấn luyện tăng tốc |
| **Xử lý Ảnh & Tăng Cường** | OpenCV (`cv2`), Albumentations | Tiền xử lý ảnh nhanh, tối ưu hóa I/O luồng dữ liệu |
| **Trực quan hóa & Phân tích** | Matplotlib, TensorBoard, Torchinfo | Vẽ đồ thị Loss/Accuracy, hiển thị Feature Maps |
| **Triển khai Mô hình Tối ưu** | ONNX Runtime, TensorRT, Netron | Chuyển đổi mô hình phục vụ suy luận thời gian thực |

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
01_Strategy_and_Curriculum/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 AGENT_PROFILE.md                      # Hồ sơ năng lực Mentor AI Computer Vision
├── 📄 ROADMAP_AND_CURRICULUM.md             # Giáo trình Master 15 tuần Computer Vision
├── 📁 rubrics/                              # Thang điểm đánh giá đồ án thị giác
│   └── vision_capstone_rubric.md            # Tiêu chí chấm đồ án Segmentation & Detection
└── 📁 exam_blueprints/                      # Đề cương kiểm tra định kỳ
    ├── midterm_classical_cv_blueprint.md    # Đề thi giữa kỳ: Xử lý ảnh số & Homography
    └── final_deep_vision_blueprint.md       # Đề thi cuối kỳ: CNNs, YOLO, U-Net
```

---

## 💻 5. MẪU THIẾT KẾ BÀI HỌC 4 TẦNG QUY CHUẨN (GOLD MASTER SYLLABUS UNIT)

```markdown
### Tuần X: [Tên Chủ Đề Thị Giác Máy Tính]
- **Tầng 1 (Toán học & Bản chất Vật lý - Nguồn: Szeliski Ch.X / CS231n)**:
  - Bản chất toán học: Phép biến đổi không gian, ma trận tích chập, Gradient Vector.
  - Phân tích độ phức tạp tính toán FLOPs và số lượng tham số Parameters.
- **Tầng 2 (Cài đặt PyTorch & OpenCV Hiện Đại)**:
  - Tự viết Custom Layer hoặc Training loop hỗ trợ Mixed Precision (`torch.cuda.amp`).
- **Tầng 3 (⚠️ Cảnh báo bẫy sai lầm & Anti-patterns)**:
  - Bẫy quên `model.eval()` và `torch.no_grad()` trong pha đánh giá.
  - Bẫy kênh màu BGR của OpenCV khi chuyển đổi sang Tensor PyTorch RGB.
- **Tầng 4 (Bài tập Lab & Tiêu chí DoD)**:
  - Đề bài: Huấn luyện mô hình đạt Accuracy >= 85% trên tập dữ liệu benchmark, 0 lỗi CUDA OOM.
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU GIÁO TRÌNH (DEFINITION OF READY - DoR)

- [ ] **DoR-1**: Giáo trình bám sát cấu trúc của Stanford CS231n và sách Szeliski Computer Vision 2nd edition.
- [ ] **DoR-2**: Các bài học về CNNs đều có sơ đồ luồng dữ liệu Tensor Shape rõ ràng từ đầu vào đến đầu ra.
- [ ] **DoR-3**: Đã có starter repo bài tập với DataLoader và kịch bản huấn luyện mẫu.
- [ ] **DoR-4**: Không sử dụng các thư viện auto-ml che giấu bản chất kỹ thuật.
- [ ] **DoR-5**: Có câu hỏi phản biện Micro-quiz về Receptive Field hoặc Loss Function (Cross-Entropy vs Dice Loss).

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK GIÁM ĐỊNH LỘ TRÌNH (CURRICULUM TROUBLESHOOTING RUNBOOK)

Khi phát hiện bài giảng chứa công thức sai hoặc bài lab gây sập VRAM GPU học viên:
1. **Phát hiện (Detection)**: Sinh viên phản hồi bài lab Tuần 8 gây lỗi `CUDA out of memory` trên GPU 4GB.
2. **Đình chỉ module (Quarantine)**: Gắn nhãn `⚠️ VRAM BOTTLENECK UNDER REMEDIATION` tại `STATUS.md`.
3. **Hiệu chỉnh bài lab**: Giảm batch size mặc định, bổ sung Gradient Accumulation và kích hoạt AMP.
4. **Kiểm chứng thực nghiệm**: Chạy thử kịch bản huấn luyện trên GPU có đúng 4GB VRAM để đảm bảo an toàn tuyệt đối.
