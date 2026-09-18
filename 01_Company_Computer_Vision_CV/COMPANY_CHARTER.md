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

Toàn bộ công ty vận hành theo cơ chế phân định trách nhiệm rõ ràng giữa Đám mây và Máy trạm cục bộ:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   HỆ THỐNG TÁC CHIẾN HYBRID CLOUD-LOCAL (CORP-01-CV)             │
├─────────────────────────────────────────┬────────────────────────────────────────┤
│ ☁️ CLOUD COMPUTE ENGINE (GOOGLE COLAB)   │ 💻 LOCAL STRATEGIC & MANAGEMENT HQ     │
├─────────────────────────────────────────┼────────────────────────────────────────┤
│ 1. Nạp Dataset trực tiếp qua Kaggle API │ 1. Trung tâm thiết kế & kiến trúc core │
│ 2. Tiền xử lý ảnh (CLAHE + Otsu Crop)   │ 2. Quản trị Báo cáo Kỹ thuật (DOCX/MD) │
│ 3. Huấn luyện Model (GPU T4 16GB VRAM)  │ 3. Quản trị Slide thuyết trình (PPTX)  │
│ 4. Chạy chuỗi thí nghiệm E0 -> E3       │ 4. Quản lý logs & đối sánh kết quả     │
│ 5. Xuất Checkpoints (.pth) & Metrics CSV│ 5. Triển khai Clinical Demo WebApp     │
└─────────────────────────────────────────┴────────────────────────────────────────┘
```

---

## 2. CƠ CẤU TỔ CHỨC CÁC PHÒNG BAN (ORGANIZATION BREAKDOWN)

```
01_Company_Computer_Vision_CV/
├── 📄 COMPANY_CHARTER.md                    # Bản điều lệ này (Đã cập nhật Hybrid Paradigm)
├── 📊 STATUS.md                             # Dashboard theo dõi tiến độ & phân tầng tác vụ
├── 📁 01_Strategy_and_Curriculum/            # Phòng Chiến Lược: Thiết kế kiến trúc & Lộ trình đào tạo
├── 📁 02_Lectures_and_Raw_Materials/        # Phòng Tư Liệu: Quản trị Báo cáo đồ án, Slide & Tư liệu chuẩn
├── 📁 03_Engineering_Labs_and_Code/         # Phòng Kỹ Thuật: Notebooks Colab, Local WebApp & Experiment Logs
│   ├── 📁 RSNA_Bone_Age_Research Project/   # Dự án Tuổi Xương RSNA (Flagship)
│   │   ├── 📄 01_RSNA_Bone_Age_End_to_End_Pipeline.ipynb # Master Notebook chạy trên Colab
│   │   ├── 📁 colab_notebooks/              # Scripts & Notebooks huấn luyện đám mây
│   │   ├── 📁 experiment_results/           # Lưu trữ metrics, biểu đồ & checkpoint tải từ Colab
│   │   └── 📁 clinical_webapp/              # Ứng dụng WebApp tương tác lâm sàng (Streamlit Local)
│   └── 📁 MECHANICAL_FAULT_XRAY Project/    # Đồ án X-ray Mối hàn Nhóm 16 (Dự án tham chiếu chuẩn)
├── 📁 04_Notion_Digital_Workspace/          # Phòng Số Hóa: Đồng bộ bảng kết quả thực nghiệm & Task Sprint
└── 📁 05_Troubleshooting_and_Toolkits/      # Phòng Hỗ Trợ: Cẩm nang xử lý lỗi Colab Runtime & Local Streamlit
```

---

## 3. QUY TRÌNH PHỐI HỢP & TÁC NGHIỆP CỦA SINH VIÊN

1. **Giai đoạn Thiết kế (Local HQ)**: Soạn thảo đề cương, kiến trúc mô hình và pipeline tại `01_Strategy_and_Curriculum/` và `02_Lectures_and_Raw_Materials/`.
2. **Giai đoạn Huấn luyện (Google Colab)**: Đưa notebook lên Google Colab, nạp token Kaggle, kéo dataset về RAM/SSD đám mây, huấn luyện với GPU T4, sau đó tải file checkpoint (`best_model.pth`) và file log kết quả (`history.csv`) về máy.
3. **Giai đoạn Quản lý Kết quả & Báo cáo (Local HQ)**: Nạp các file kết quả vào `experiment_results/`, cập nhật biểu đồ vào Báo cáo đồ án (`project_report.md`) và Slide thuyết trình (`slide_content_20_pages.md`).
4. **Giai đoạn Trình diễn (Local WebApp)**: Tải trọng số tốt nhất vào ứng dụng Streamlit tại `clinical_webapp/` để chạy demo chẩn đoán trực tiếp phục vụ bảo vệ đồ án.

