# 📊 PROJECT STATUS DASHBOARD — VisionLab Corp (CORP-01-CV)

> **Cập nhật lần cuối**: 2026-09-18 | **Giai đoạn**: Triển khai Dự án RSNA Bone Age (Hybrid Cloud-Local)  
> **Mentor chuyên trách**: DUT Computer Vision Mentor (`AGENT_PROFILE.md`)  
> **Mô hình Vận hành**: **Google Colab (Compute Cloud)** $\longleftrightarrow$ **Local Workstation (Strategic HQ & WebApp)**

---

## 🏛️ Sứ Mệnh & Phân Tầng Trách Nhiệm Hiện Tại

| Phân Vùng | Trọng Tâm Nhiệm Vụ | Hiện Trạng & Tài Sản Quản Lý |
|:---|:---|:---|
| ☁️ **Google Colab (Compute Engine)** | - Tải trực tiếp dataset 10GB qua Kaggle Token (`KGAT_...`)<br>- Tiền xử lý ảnh (CLAHE + Otsu Bounding Crop)<br>- Huấn luyện mô hình nặng: ResNet-50, EfficientNet-B4, Swin-T<br>- Xuất checkpoint (`best_model.pth`) & file log (`history.csv`) | - Đã cấu hình Kaggle CLI 2.2.4 & token<br>- Notebook master: `01_RSNA_Bone_Age_End_to_End_Pipeline.ipynb` |
| 💻 **Local Workstation (Strategic HQ)** | - Cung cấp thiết kế, tài liệu kỹ thuật cốt lõi, cẩm nang hướng dẫn<br>- Quản lý hồ sơ Báo cáo đồ án (`project_report.md`) & Slide (`slide_content_20_pages.md`)<br>- Lưu trữ và đối chiếu kết quả thực nghiệm kéo về từ Colab<br>- Phát triển & vận hành chương trình Demo lâm sàng (`Streamlit WebApp`) | - Báo cáo kỹ thuật 438 dòng chuẩn DUT<br>- Kịch bản 20 slide thuyết trình<br>- Folder `experiment_results/` & `clinical_webapp/` |

---

## 📈 Tiến Độ Triển Khai Thực Nghiệm (Ablation Matrix)

- [x] **Thiết kế Kiến trúc Hệ thống**: Hoàn thành pipeline 5 bước Classical CV + Late Fusion Multimodal + Huber Loss.
- [x] **Cấu hình Xác thực Dữ liệu**: Thiết lập thành công Kaggle Token trên hệ thống (`KGAT_647e2aba908b47705fadfd3ea663af4f`).
- [ ] **E0 (Baseline)**: Huấn luyện ResNet-50 thô trên Colab.
- [ ] **E1 (Classical CV)**: Huấn luyện ResNet-50 với ảnh đã qua CLAHE + Otsu Crop.
- [ ] **E2 (Multimodal)**: Huấn luyện ResNet-50 + Gender Embedding 32D + Huber Loss.
- [ ] **E3 (SOTA Backbone)**: Huấn luyện EfficientNet-B4 / Swin-T + Explainable AI (Grad-CAM).
- [ ] **Đồng bộ Checkpoint về Local**: Kéo `best_model.pth` về `experiment_results/`.
- [ ] **Khởi chạy Local WebApp**: Chạy `streamlit run app.py` phục vụ bảo vệ đồ án.

---

## 🎯 Next Priority (P0)
1. **Colab Execution**: Đưa `01_RSNA_Bone_Age_End_to_End_Pipeline.ipynb` lên Google Colab, nạp token và chạy huấn luyện chuỗi mô hình E0 $\to$ E3.
2. **Local Asset Management**: Xây dựng cấu trúc thư mục chuẩn trong `03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research Project`:
   - `colab_notebooks/`: Chứa file ipynb tối ưu hóa cho Colab.
   - `experiment_results/`: Chứa file checkpoint `.pth`, metrics `.csv`, và biểu đồ loss/MAE kéo từ Colab về.
   - `clinical_webapp/`: Chứa mã nguồn Streamlit WebApp tương tác lâm sàng chạy offline trên máy local.
3. **Cập nhật Báo cáo & Slide**: Đưa các số liệu MAE/RMSE thực nghiệm thực tế vào báo cáo và slide bài giảng.


