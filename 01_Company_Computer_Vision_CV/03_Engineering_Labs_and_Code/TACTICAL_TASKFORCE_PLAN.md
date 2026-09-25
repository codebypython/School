# 🎯 KẾ HOẠCH TÁC CHIẾN: PHÒNG KỸ THUẬT & HỆ THỐNG HUẤN LUYỆN (DEPT 03)
> **Mã biệt đội:** `SQUAD-03-ENGINEERING`  
> **Nhiệm vụ trọng tâm:** Quản trị bộ 3 Kaggle Notebooks, kiểm soát checkpoint `.pth` và duy trì WebApp Streamlit.

### 📋 Danh mục Tác vụ Cụ thể:
1. **Bảo trì Bộ 3 Kaggle Notebooks (`kaggle_modular_notebooks/`):**
   - Đảm bảo tính tương thích trên cả Kaggle GPU (Tesla T4 / P100) và Google Colab.
   - Kiểm tra cơ chế `load_full_checkpoint()` để đảm bảo tự động phục hồi mượt mà khi bị ngắt kết nối.
2. **Quản lý Thư viện Checkpoint (`experiment_results/`):**
   - Đảm bảo các thư mục con `M1_ResNet50/`, `M2_ConvNeXt/`, `M3_SwinT/` luôn có tệp `DROP_GUIDE.md` hướng dẫn.
3. **Vận hành Local WebApp (`clinical_webapp/app.py`):**
   - Kiểm tra khả năng chạy offline trên máy trạm nội bộ: `streamlit run app.py`.
   - Đảm bảo logic cảnh báo WHO và lớp phủ Grad-CAM hiển thị mượt mà khi demo trước Hội đồng.
