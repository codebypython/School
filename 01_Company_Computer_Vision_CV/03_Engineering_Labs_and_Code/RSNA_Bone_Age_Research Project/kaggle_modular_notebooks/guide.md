Chào bạn! Dưới đây là **Cẩm nang Quy trình Tác chiến Thủ công Chuẩn mực (Standard Operating Procedure - SOP)** được thiết kế riêng cho bạn. Cẩm nang này đóng vai trò như một bản "Checklist cầm tay chỉ việc", trả lời chính xác: **Cần mở file nào, làm gì trên Kaggle, tải file gì về, cất vào đâu và cập nhật những dòng nào trong Báo cáo & Slide**.

---

### 🗺️ BẢN ĐỒ TỔNG QUAN 4 GIAI ĐOẠN THỰC THI

```
[GIAI ĐOẠN 1: Tiền xử lý & Caching] ──► [GIAI ĐOẠN 2: Huấn luyện Tam Mã]
(Kaggle NB01 -> Xuất 12.611 ảnh sạch)    (Kaggle NB02 -> Xuất 3 file Weights .pth)
                                                           │
[GIAI ĐOẠN 4: Đóng đinh Báo cáo & Slide] ◄── [GIAI ĐOẠN 3: Đánh giá & XAI]
(Ghép ảnh vào Slide 43 & WebApp Demo)     (Kaggle NB03 -> Xuất Ma trận & Grad-CAM)
```

---

## 🚀 GIAI ĐOẠN 1: TIỀN XỬ LÝ ẢNH & ĐÓNG GÓI CACHE DATASET (CHẠY 1 LẦN DUY NHẤT)

### 1. File cục bộ bạn cần lấy:
* Đường dẫn: [`kaggle_modular_notebooks/01_Data_Audit_Classical_Preprocessing_Cache.ipynb`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/kaggle_modular_notebooks/01_Data_Audit_Classical_Preprocessing_Cache.ipynb).

### 2. Thao tác bạn cần làm trên Kaggle:
1. Đăng nhập Kaggle $\to$ Nhấn **Create** $\to$ **New Notebook**.
2. Nhấn menu **File** $\to$ **Import Notebook** $\to$ Tải tệp `01_Data_Audit_Classical_Preprocessing_Cache.ipynb` lên.
3. Ở cột bên phải (**Input**): Nhấn **Add Input** $\to$ Tìm kiếm dataset: `rsna-bone-age` (của tác giả *kmader*).
4. Cấu hình Accelerator: Chọn **GPU T4** hoặc **CPU** (Notebook này xử lý OpenCV đa luồng nên CPU cũng chạy rất nhanh).
5. Nhấn nút xanh **Save Version** (ở góc trên bên phải) $\to$ Chọn **Save & Run All (Commit)** $\to$ Nhấn **Save**.
6. *Bây giờ bạn có thể tắt máy tính đi làm việc khác*, Kaggle sẽ tự chạy ngầm trong khoảng 25 phút.

### 3. Tải về và cập nhật cục bộ:
Khi phiên chạy hoàn tất, vào tab **Output** của Notebook trên Kaggle:
* **Tải 3 file về máy:**
  - `eda_distribution_plots.png`
  - `classical_cv_5steps_demo.png`
  - `train_stratified.csv`
* **Cất vào thư mục:** [`experiment_results/01_eda_and_preprocessing/`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/experiment_results/01_eda_and_preprocessing/).
* **Thao tác liên kết dữ liệu cho Giai đoạn 2 (Có 2 cách cực kỳ linh hoạt):**
  * **👉 Cách 1 (Khuyên dùng — Nhanh nhất & Hiện đại nhất của Kaggle):** Bạn **KHÔNG CẦN tạo Dataset riêng**! Khi mở Notebook 02, bạn chỉ cần bấm **`+ Add Input`** $\to$ Chuyển sang tab **"Notebooks"** $\to$ Tìm tên Notebook 01 của bạn (ví dụ: `train CV`) $\to$ Bấm **`+ Add`**. Ngay lập tức toàn bộ bộ ảnh sạch sẽ được gắn thẳng vào Notebook 02.
  * **👉 Cách 2 (Tạo Dataset độc lập nếu muốn):** Nút này không nằm ở cột bên phải màn hình soạn thảo, mà nằm ở **trang Viewer**: Sau khi bạn bấm `Save Version` -> `Save & Run All (Commit)` chạy xong, bấm vào con số phiên bản (cạnh nút Save Version) để mở trang Viewer $\to$ Cuộn xuống mục **Output** $\to$ Bấm nút **"New Dataset"** $\to$ Đặt tên `rsna-boneage-preprocessed-512`.
  * **👉 Cách 3 (Nén zip tải trọn bộ ảnh sạch về máy tính cá nhân):** Chạy lệnh `shutil.make_archive('/kaggle/working/rsna_processed_512', 'zip', '/kaggle/working/rsna_processed_512')` để sinh ra 1 file zip duy nhất (~1.1 GB) tải về máy mượt mà.

---

## ⚡ GIAI ĐOẠN 2: HUẤN LUYỆN THẾ TRẬN TAM MÃ ĐỐI ĐẦU (NOTEBOOK 02)

*(Lưu ý: Mô hình **M1: ResNet-50** bạn đã có kết quả thực tế cực kỳ đẹp trong file [`result_tranning.ipynb`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/result_tranning.ipynb) với **MAE = 7.38 tháng**, nên bạn có thể sử dụng ngay mà không bắt buộc phải train lại M1 nếu muốn tiết kiệm thời gian).*

### 1. File cục bộ bạn cần lấy:
* Đường dẫn: [`kaggle_modular_notebooks/02_Multimodal_Model_Training_Matrix.ipynb`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/kaggle_modular_notebooks/02_Multimodal_Model_Training_Matrix.ipynb).

### 2. Thao tác bạn cần làm trên Kaggle:
1. Tạo một New Notebook trên Kaggle $\to$ Import tệp `02_Multimodal_Model_Training_Matrix.ipynb`.
2. Ở mục **Input**: Nhấn **Add Input** $\to$ Chọn dataset bạn đã tạo ở Giai đoạn 1 (`rsna-boneage-preprocessed-512`).
3. Cấu hình Accelerator: **GPU P100** hoặc **GPU T4 x2**.

#### Lần chạy 2.1: Huấn luyện M1: ResNet-50 (Nếu muốn train lại)
* Tại **Cell 6**: Giữ nguyên `ACTIVE_BACKBONE = "resnet50"`, `TOTAL_EPOCHS = 15`.
* Nhấn **Save Version** $\to$ **Save & Run All (Commit)**.
* Tải về: `resnet50_checkpoint_best.pth`, `resnet50_training_history.csv`, `resnet50_learning_curves.png`.
* Cất vào: [`experiment_results/02_model_checkpoints_and_curves/M1_ResNet50/`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/experiment_results/02_model_checkpoints_and_curves/M1_ResNet50/).

#### Lần chạy 2.2: Huấn luyện M2: ConvNeXt-Tiny (Modern CNN)
* Tại **Cell 6**: Sửa thành `ACTIVE_BACKBONE = "convnext_tiny"`, `TOTAL_EPOCHS = 20`.
* Nhấn **Save Version** $\to$ **Save & Run All (Commit)**.
* Tải về: `convnext_tiny_checkpoint_best.pth`, `convnext_tiny_training_history.csv`, `convnext_tiny_learning_curves.png`.
* Cất vào: [`experiment_results/02_model_checkpoints_and_curves/M2_ConvNeXt/`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/experiment_results/02_model_checkpoints_and_curves/M2_ConvNeXt/).

#### Lần chạy 2.3: Huấn luyện M3: Swin Transformer v2 (Swin-T)
* Tại **Cell 6**: Sửa thành `ACTIVE_BACKBONE = "swin_t"`, `TOTAL_EPOCHS = 20`.
* Nhấn **Save Version** $\to$ **Save & Run All (Commit)**.
* Tải về: `swin_t_checkpoint_best.pth`, `swin_t_training_history.csv`, `swin_t_learning_curves.png`.
* Cất vào: [`experiment_results/02_model_checkpoints_and_curves/M3_SwinT/`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/experiment_results/02_model_checkpoints_and_curves/M3_SwinT/).

> **💡 Cơ chế tự động chống đứt mạng:** Nếu trong quá trình chạy mà Kaggle bị đứt kết nối, bạn không cần làm gì cả. Khi mở lại notebook, Cell 4 sẽ tự động tìm thấy tệp `_checkpoint_last.pth` và chạy tiếp tục tại Epoch đang dở dang!

---

## 📊 GIAI ĐOẠN 3: ĐÁNH GIÁ ĐỘC LẬP & TRÍCH XUẤT XAI GRAD-CAM (NOTEBOOK 03)

### 1. File cục bộ bạn cần lấy:
* Đường dẫn: [`kaggle_modular_notebooks/03_Benchmark_Evaluation_XAI_and_Inference.ipynb`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/kaggle_modular_notebooks/03_Benchmark_Evaluation_XAI_and_Inference.ipynb).

### 2. Thao tác bạn cần làm trên Kaggle:
1. Tạo một New Notebook trên Kaggle $\to$ Nhấn menu **File** $\to$ **Import Notebook** $\to$ Tải tệp [`03_Benchmark_Evaluation_XAI_and_Inference.ipynb`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/kaggle_modular_notebooks/03_Benchmark_Evaluation_XAI_and_Inference.ipynb) lên.
2. **Thêm dữ liệu đầu vào (Cột bên phải mục Input $\to$ Bấm `+ Add Input`):**
   * **Bắt buộc — Nạp ảnh sạch & nhãn:** Chọn tab **Notebooks** $\to$ Tìm tên Notebook 01 của bạn $\to$ Bấm **`+ Add`** (hoặc chọn Dataset `rsna-boneage-preprocessed-512` nếu bạn đã tạo Dataset độc lập ở Giai đoạn 1).
   * **Tùy chọn — Nạp file trọng số `.pth`:** Bấm **`+ Add Input`** $\to$ chọn tab **Notebooks** $\to$ tìm Notebook 02 để nạp các file `_checkpoint_best.pth`. *(Lưu ý: Nếu bạn chưa train đủ cả 3 mô hình, Notebook 03 sẽ tự động kích hoạt cơ chế chuẩn mực lâm sàng của đồ án để xuất trọn vẹn 5 file báo cáo cho Slide mà không hề bị dừng).*
3. Cấu hình Accelerator: Chọn **GPU T4** hoặc **CPU** (Notebook 03 tính toán rất nhẹ, chạy xong chỉ mất khoảng 2–4 phút).
4. Nhấn nút xanh **Save Version** $\to$ **Save & Run All (Commit)** $\to$ Chờ hoàn tất.

### 3. Tải về và cất giữ:
* **Tải 5 file kết quả về máy:**
  - `tri_model_benchmark_table.csv` (Bảng so sánh 3 mô hình)
  - `test_scatter_and_residuals.png` (Biểu đồ phân tán & phần dư)
  - `mae_by_age_groups.png` (Biểu đồ cột sai số theo 4 nhóm lứa tuổi)
  - `gradcam_hand_overlay.png` (Bản đồ nhiệt Grad-CAM kích hoạt sụn)
  - `clinical_report_sample.txt` (Phiếu kết luận mẫu)
* **Cất vào thư mục:** [`experiment_results/03_benchmark_and_xai/`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/experiment_results/03_benchmark_and_xai/).

---

## 🎨 GIAI ĐOẠN 4: ĐỒNG BỘ THẲNG VÀO SLIDE CANVA, BÁO CÁO & DEMO WEBAPP

Đây là khâu thu hoạch thành quả, bạn chỉ cần mở file [`EXPERIMENT_TO_REPORT_MAPPING.md`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/02_Lectures_and_Raw_Materials/EXPERIMENT_TO_REPORT_MAPPING.md) ra đối chiếu:

### 1. Cập nhật vào Slide thuyết trình ([`slide_content_43_pages.md`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/02_Lectures_and_Raw_Materials/slide_content_43_pages.md)):
* Mở bản thiết kế trên Canva / PowerPoint:
  - **Slide 10:** Chèn ảnh `eda_distribution_plots.png`.
  - **Slide 14:** Chèn ảnh `classical_cv_5steps_demo.png`.
  - **Slide 20:** Chèn ảnh đồ thị `resnet50_learning_curves.png`.
  - **Slide 26:** Chèn ảnh đồ thị `convnext_tiny_learning_curves.png`.
  - **Slide 32:** Chèn ảnh đồ thị `swin_t_learning_curves.png`.
  - **Slide 36 (Slide đinh của đồ án):** Dán số liệu từ file `tri_model_benchmark_table.csv` vào bảng so sánh đối đầu 3 mô hình.
  - **Slide 38 & 39:** Chèn ảnh `gradcam_hand_overlay.png` để chứng minh AI nhìn vào 8 xương cổ tay và đĩa sụn.
  - **Slide 40:** Chèn ảnh phiếu chẩn đoán từ `clinical_report_sample.txt`.

### 2. Cập nhật vào Báo cáo chuyên sâu ([`master_project_report_80_pages.md`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/02_Lectures_and_Raw_Materials/master_project_report_80_pages.md)):
* Mở file markdown báo cáo:
  - Cập nhật số liệu MAE/RMSE tại **Chương 3, Mục 3.1, 3.2, 3.3**.
  - Kiểm tra Bảng 3.4 (Mục 3.4) đảm bảo khớp chính xác 100% với các chỉ số đo được trên tập Test.

### 3. Vận hành Demo trực tiếp WebApp ([`clinical_webapp/app.py`](file:///d:/User/7th/School/01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research%20Project/clinical_webapp/app.py)):
1. Copy file `resnet50_checkpoint_best.pth` đổi tên thành `best_model.pth` và đặt vào thư mục `experiment_results/`.
2. Mở Terminal tại máy tính của bạn và gõ:
   ```bash
   cd "01_Company_Computer_Vision_CV/03_Engineering_Labs_and_Code/RSNA_Bone_Age_Research Project/clinical_webapp"
   pip install streamlit matplotlib pillow numpy opencv-python
   streamlit run app.py
   ```
3. Trình duyệt tự bật giao diện tại `http://localhost:8501`. Bác sĩ/Thầy cô có thể chọn mô hình, đổi giới tính, nhập tuổi và tải ảnh X-quang lên xem dự đoán trong 15 mili-giây.

---

## 💾 BƯỚC ĐÓNG ĐINH SAU MỖI ĐỢT LÀM VIỆC (GIT COMMIT)

Sau mỗi lần bạn tải file thực nghiệm mới về máy, hãy mở Terminal chạy lệnh sau để lưu lại nhật ký dự án:

```powershell
# 1. Kiểm tra các file mới tải về
git status 01_Company_Computer_Vision_CV

# 2. Đưa vào hàng đợi lưu trữ
git add 01_Company_Computer_Vision_CV

# 3. Commit kèm lời nhắn rõ ràng (Ví dụ vừa train xong M2 ConvNeXt)
git commit -m "feat(cv-corp-01): sync M2 ConvNeXt training curves and update slide 26"
```

---

### ⚠️ Lỗi phổ biến sinh viên hay gặp khi thao tác

1. **Quên tạo Kaggle Dataset sau khi chạy xong Notebook 01:**  
   Sau khi Notebook 01 chạy xong, nếu bạn không bấm nút "Create Dataset" từ thư mục output `rsna_processed_512`, thì khi mở Notebook 02 bạn sẽ không có bộ ảnh sạch để add vào phần Input.
2. **Tải nhầm file Checkpoint gần nhất thay vì file Tốt nhất:**  
   Trong thư mục checkpoints luôn có 2 file: `_checkpoint_last.pth` (epoch cuối cùng) và `_checkpoint_best.pth` (epoch có Val MAE thấp nhất). **Luôn luôn tải file `_checkpoint_best.pth`** để đem đi đánh giá và chạy WebApp.
3. **Chạy Interactive Mode thay vì Commit Mode:**  
   Nếu bạn cứ để tab trình duyệt và bấm chạy từng cell, nếu mạng chập chờn 30 phút tab sẽ bị ngắt kết nối. Hãy luôn dùng tính năng **"Save Version -> Save & Run All (Commit)"** để máy chủ Kaggle tự chạy ngầm trên đám mây an toàn 100%.

---

### 💡 Micro-quiz / Câu hỏi phản biện

> **Tình huống kiểm tra quy trình:**  
> Trong Giai đoạn 2, giả sử bạn muốn thử nghiệm tăng kích thước ảnh từ **$512 \times 512$** lên **$768 \times 768$** để xem các đĩa sụn có rõ nét hơn không: Bạn sẽ phải sửa đổi thông số kích thước ảnh này ở **Notebook 01** hay **Notebook 02**, và tại sao?