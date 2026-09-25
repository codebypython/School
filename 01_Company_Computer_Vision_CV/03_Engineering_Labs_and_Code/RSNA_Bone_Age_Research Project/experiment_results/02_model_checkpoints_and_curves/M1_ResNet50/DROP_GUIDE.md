# 📥 DROPBOX 02-M1: MÔ HÌNH RESNET-50 MULTIMODAL (BASELINE)
> **Mã nguồn phát sinh:** `02_Multimodal_Model_Training_Matrix.ipynb` (`ACTIVE_BACKBONE = "resnet50"`)  
> **Bộ phận thụ hưởng:** Phòng Kỹ Thuật & Phòng Tư Liệu

### 📋 Danh mục File thả vào đây:
1. `resnet50_checkpoint_best.pth`: Trọng số tối ưu nhất đạt Val MAE kỷ lục (ở Epoch 13 đạt 7.25 tháng).
   - 👉 **Áp dụng vào WebApp:** Copy đổi tên thành `best_model.pth` để WebApp chạy suy luận thật.
2. `resnet50_training_history.csv`: File log quá trình huấn luyện 15 epochs.
   - 👉 **Áp dụng vào Báo cáo:** Chương 3, Mục 3.1.1 (Bảng 3.1: Động học hội tụ qua từng Epoch).
3. `resnet50_learning_curves.png`: Đồ thị đường cong Train Loss / Val Loss và Val MAE qua 15 Epochs.
   - 👉 **Áp dụng vào Báo cáo:** Chương 3, Mục 3.1.1 (Hình 3.1).
   - 👉 **Áp dụng vào Slide:** Slide 20 (Kết quả động học huấn luyện ResNet-50).
