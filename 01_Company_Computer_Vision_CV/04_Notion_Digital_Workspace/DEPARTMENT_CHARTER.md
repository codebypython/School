# 📜 ĐIỀU LỆ PHÒNG SỐ HÓA & KHÔNG GIAN NOTION (NOTION DIGITAL WORKSPACE DEPT)
## Phòng 04 — Công Ty Công Nghệ Thị Giác Máy Tính (CORP-01-CV)

> **Mã Phòng Ban:** `CV-DEPT-04`  
> **Trưởng phòng phụ trách:** Agent `NKA-05` (Notion Architect & Hub Administrator)  
> **Hệ sinh thái liên kết:** Central Notion LMS Hub (`00_Central_Notion_LMS_Hub`)  
> **Tiêu chuẩn công nghệ:** Notion Formula 2.0 / Paper Tracker / Active Recall Flashcards

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Số Hóa là **trung tâm quản trị học tập số và theo dõi tiến độ thực nghiệm**:
1. **Quản Trị Bảng Theo Dõi Thực Nghiệm Đám Mây (Colab Experiment Tracker DB)**: Số hóa toàn bộ ma trận kết quả huấn luyện từ Google Colab (MAE, RMSE, $R^2$, Epochs, thời gian huấn luyện GPU T4, Checkpoint path) để đồng bộ vào báo cáo khoa học.
2. **Quản Trị Tiến Độ Đọc Paper Khoa Học (Vision Paper Tracker DB)**: Theo dõi tiến độ đọc 20+ papers kinh điển và hiện đại (RSNA Challenge 2019, ResNet, EfficientNet, Swin Transformer), ghi chú phương pháp và mã nguồn tái lập.
3. **Kho Bảng Tra Cứu Số Hóa (Cheat Sheets Vault)**: Số hóa danh mục công thức hình học thị giác, bảng so sánh kiến trúc Backbone và lệnh PyTorch.
4. **Hệ Thống Flashcards Lặp Lại Ngắt Quãng (Vision Math Flashcards)**: Sử dụng Notion Formula 2.0 để tự động lên lịch kiểm tra kiến thức về Receptive Field, Convolution Arithmetic và Loss Functions.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (NOTION INVARIANTS)

1. **Chuẩn Mực Khối Callout Phân Loại**:
   - Sử dụng định dạng callout chuẩn phân loại cấp độ paper (Classical CV, Deep CNN, Transformers).
2. **Quy Chuẩn CSDL Quan Hệ Hai Chiều**:
   - Mọi bản ghi bài báo khoa học bắt buộc liên kết với môn học tương ứng trong Central Notion LMS Hub.
3. **Công Thức Formula 2.0 Chuẩn Xác**:
   - Mọi công thức tính toán tiến độ đọc hoặc Spaced Repetition phải sử dụng chuẩn Formula 2.0 (`lets()`, `ifs()`).

---

## 🛠️ 3. TOOLCHAIN & KỸ NĂNG VẬN HÀNH NOTION LMS

1. **Bộ Công Cụ**: Notion API v2022-06-28, Python Notion SDK.
2. **Template Builder**: Database Views (Board view theo Nhóm mô hình, Table view theo Năm xuất bản).
3. **Kiểm Tra Cú Pháp**: Notion Formula Linter trong Central LMS Hub.

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
04_Notion_Digital_Workspace/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 NOTION_CV_COMPUTER_VISION.md          # File trang chủ Notion môn CV
├── 📄 Computer_Vision_Mastery_Roadmap_OS.md # Bản lộ trình hệ điều hành học tập CV
├── 📁 flashcards_vault/                     # Ngân hàng câu hỏi Active Recall
│   ├── conv_arithmetic_flashcards.md       # Flashcards tính toán Stride, Padding
│   └── object_detection_flashcards.md      # Flashcards mAP, NMS, IoU
└── 📁 page_templates/                       # Mẫu trang ghi chép nghiên cứu
    └── paper_reading_note_template.md      # Mẫu tóm tắt bài báo khoa học 3 bước
```

---

## 💻 5. MẪU THIẾT KẾ SCHEMA CSDL & CÔNG THỨC NOTION 2.0 (GOLD MASTER NOTION)

```markdown
# 📊 CSDL THEO DÕI ĐỌC BÀI BÁO THỊ GIÁC (CV PAPER TRACKER)

### Thuộc tính bảng (Properties Schema):
1. `Paper Title` (Title): Tên bài báo (VD: Deep Residual Learning for Image Recognition).
2. `Category` (Select): Backbone, Detection, Segmentation, Generative, ViT.
3. `Venue & Year` (Text): CVPR, ICCV, ECCV, NeurIPS (Kèm năm).
4. `Status` (Status): To Read, Skimming, Deep Reading, Replicated.
5. `Key Contribution` (Text): Đóng góp cốt lõi của nghiên cứu.
6. `Last Reviewed` (Date): Ngày đọc/ôn tập gần nhất.

### 🧮 Công thức Formula 2.0: Spaced Repetition Scheduling:
```notion
lets(
  interval, if(prop("Status") == "Replicated", 21, if(prop("Status") == "Deep Reading", 7, 2)),
  dateAdd(prop("Last Reviewed"), interval, "days")
)
```
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU KHÔNG GIAN SỐ (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: CSDL thể hiện đúng tiến độ 100% các module của môn Computer Vision.
- [ ] **DoD-2**: Các công thức Spaced Repetition Formula 2.0 hoạt động chính xác không lỗi cú pháp.
- [ ] **DoD-3**: Giao diện trực quan, có view Kanban theo trạng thái bài đọc.
- [ ] **DoD-4**: Tương thích hoàn toàn với schema liên kết của Central Notion LMS Hub.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK ĐỒNG BỘ DỮ LIỆU NOTION (NOTION TROUBLESHOOTING RUNBOOK)

Khi xảy ra lỗi đồng bộ hoặc gãy liên kết CSDL quan hệ:
1. **Cô lập thuộc tính**: Xác định xem lỗi phát sinh từ Formula 2.0 hay do cấu hình database relation.
2. **Khôi phục cấu trúc**: Tra cứu cấu trúc chuẩn trong `00_Central_Notion_LMS_Hub/NOTION_ADVANCED_FORMULAS.md`.
3. **Sửa đổi cú pháp**: Cập nhật công thức theo đúng đặc tả Notion 2.0.
4. **Kiểm chứng toàn vẹn**: Tạo bản ghi thử nghiệm để kiểm tra tiến độ tính toán tự động.
