# 👁️ ĐIỀU LỆ HOẠT ĐỘNG: CÔNG TY CÔNG NGHỆ THỊ GIÁC MÁY TÍNH (VISIONLAB DEEP TECH CORP)
## Company 01: Computer Vision & Visual Perception Technologies

> **Mã Doanh Nghiệp:** `CORP-01-CV`  
> **Tên giao dịch:** VisionLab Deep Tech Corporation  
> **Lĩnh vực chuyên môn:** Xử lý ảnh số, Thị giác máy tính cổ điển, Deep Learning Backbones, Object Detection, Semantic Segmentation và Edge AI.  
> **Cố vấn chuyên môn:** Giám Đốc Nghiên Cứu CV & Cố Vấn Học Thuật DUT  
> **Tổng Giám Đốc Điều Hành (CEO):** Sinh viên (Role Handmade)

---

## 1. SỨ MỆNH & TẦM NHÌN (MISSION & VISION)

- **Sứ mệnh**: Đào tạo và phát triển năng lực nghiên cứu - ứng dụng công nghệ Thị giác Máy tính chuẩn quốc tế cho kỹ sư CNTT Bách Khoa, nắm chắc từ toán học giải tích tensor không gian đến các mô hình mạng nơ-ron tích chập và Vision Transformers hiện đại.
- **Tiêu chuẩn chất lượng**: Đối chiếu và kế thừa 100% tinh hoa từ **Stanford CS231n / Michigan EECS 498-007** và giáo trình kinh điển của **Richard Szeliski (2022)**.

### 🌟 1.1. MÔ HÌNH TÁC CHIẾN PHÂN TẦNG ĐIỆN TOÁN (HYBRID CLOUD-LOCAL PARADIGM)

Toàn bộ công ty vận hành theo cơ chế phân định trách nhiệm rõ ràng giữa Đám mây và Máy trạm cục bộ, kế thừa chuẩn mực học thuật và thực nghiệm từ đồ án xuất sắc `MECHANICAL_FAULT_XRAY Project`:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   HỆ THỐNG TÁC CHIẾN HYBRID CLOUD-LOCAL (CORP-01-CV)             │
├─────────────────────────────────────────┬────────────────────────────────────────┤
│ ☁️ CLOUD COMPUTE ENGINE (KAGGLE/COLAB)   │ 💻 LOCAL STRATEGIC & MANAGEMENT HQ     │
├─────────────────────────────────────────┼────────────────────────────────────────┤
│ 1. Cấu trúc Mô-đun 3 Notebooks độc lập: │ 1. Trung tâm kiến trúc & đặc tả core   │
│    - NB01: Data Audit & Cache Clean 512 │ 2. Báo cáo Chuyên sâu (86 trang chuẩn  │
│    - NB02: Tri-Model Training Matrix    │    mực cấu trúc như MECHANICAL_FAULT)  │
│    - NB03: Benchmark Eval, XAI & Infer  │ 3. Bộ Slide Thuyết trình 43 trang mẫu  │
│ 2. Thế trận Tam mã Đa phương thức:      │ 4. Quản lý nhật ký thực nghiệm đối đầu │
│    - M1: ResNet-50 Baseline (2048D)     │    (ResNet-50 vs ConvNeXt vs Swin-T)   │
│    - M2: ConvNeXt-V2 / EfficientNet-B4  │ 5. Vận hành Clinical WebApp Demo       │
│    - M3: Swin Transformer v2 (Swin-T)   │    (Streamlit có cảnh báo WHO)         │
│ 3. Cơ chế Full-State Checkpoint & Resume│ 6. Thẩm định mô hình toán & XAI GradCAM│
└─────────────────────────────────────────┴────────────────────────────────────────┘
```

---

## 2. CƠ CẤU TỔ CHỨC CÁC PHÒNG BAN (ORGANIZATION BREAKDOWN)

```
01_Company_Computer_Vision_CV/
├── 📄 COMPANY_CHARTER.md                    # Bản điều lệ doanh nghiệp (Chuẩn hóa Siêu Kế Hoạch)
├── 📊 STATUS.md                             # Dashboard theo dõi tiến độ & phân tầng tác vụ
├── 📁 01_Strategy_and_Curriculum/            # Phòng Chiến Lược: Thiết kế kiến trúc & Lộ trình đào tạo
├── 📁 02_Lectures_and_Raw_Materials/        # Phòng Tư Liệu: Báo cáo 86 trang & Bộ Slide 43 trang
│   ├── 📄 master_project_report_80_pages.md # Báo cáo chuyên sâu chuẩn mực (Tương đương BÁO-CÁO.docx)
│   └── 📄 slide_content_43_pages.md         # Kịch bản 43 slide thuyết trình (Tương đương Slide.pptx)
├── 📁 03_Engineering_Labs_and_Code/         # Phòng Kỹ Thuật: Hệ thống Code & Mô hình thực nghiệm
│   ├── 📁 RSNA_Bone_Age_Research Project/   # Dự án Tuổi Xương RSNA (Flagship)
│   │   ├── 📁 kaggle_modular_notebooks/     # Hệ thống 3 Notebooks độc lập chuẩn Kaggle Grandmaster
│   │   │   ├── 📄 01_Data_Audit_Classical_Preprocessing_Cache.ipynb
│   │   │   ├── 📄 02_Multimodal_Model_Training_Matrix.ipynb
│   │   │   └── 📄 03_Benchmark_Evaluation_XAI_and_Inference.ipynb
│   │   ├── 📄 result_tranning.ipynb         # Kết quả huấn luyện thực tế ResNet-50 (MAE=7.38m)
│   │   ├── 📁 experiment_results/           # Lưu trữ weights (.pth), logs (.csv) & biểu đồ
│   │   └── 📁 clinical_webapp/              # WebApp chẩn đoán lâm sàng tương tác thời gian thực
│   └── 📁 MECHANICAL_FAULT_XRAY Project/    # Đồ án X-ray Mối hàn Nhóm 16 (Dự án tham chiếu chuẩn)
├── 📁 04_Notion_Digital_Workspace/          # Phòng Số Hóa: Đồng bộ bảng kết quả thực nghiệm & Task Sprint
└── 📁 05_Troubleshooting_and_Toolkits/      # Phòng Hỗ Trợ: Cẩm nang xử lý lỗi GPU, Checkpoints & WebApp
```

---

## 3. QUY TRÌNH PHỐI HỢP & TÁC NGHIỆP CỦA SINH VIÊN

1. **Giai đoạn Thiết kế (Local HQ)**: Soạn thảo đề cương, kiến trúc mô hình và pipeline tại `01_Strategy_and_Curriculum/` và `02_Lectures_and_Raw_Materials/`.
2. **Giai đoạn Tiền xử lý & Caching (Kaggle NB01)**: Khảo sát lâm sàng EDA, chạy Classical CV 5 bước, cố định Stratified Split 80/10/10 và đóng gói Dataset sạch 512x512.
3. **Giai đoạn Huấn luyện Đối đầu (Kaggle NB02)**: Chạy song song 3 mô hình (ResNet-50, ConvNeXt/EfficientNet, Swin-T) với Huber Loss, Mixed Precision FP16 và cơ chế Resume Checkpoint.
4. **Giai đoạn Đánh giá & XAI (Kaggle NB03)**: Thẩm định trên 1.262 ca Test độc lập, trích xuất Grad-CAM, tổng hợp ma trận so sánh.
5. **Giai đoạn Báo cáo & Triển khai (Local HQ)**: Cập nhật số liệu thực vào Báo cáo 86 trang, Slide 43 trang và khởi chạy WebApp Demo bảo vệ trước Hội đồng.

