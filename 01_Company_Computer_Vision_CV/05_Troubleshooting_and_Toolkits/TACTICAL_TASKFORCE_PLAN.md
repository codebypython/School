# 🎯 KẾ HOẠCH TÁC CHIẾN: PHÒNG CỨU HỘ KỸ THUẬT & KHẮC PHỤC SỰ CỐ (DEPT 05)
> **Mã biệt đội:** `SQUAD-05-TROUBLESHOOTING`  
> **Nhiệm vụ trọng tâm:** Dự phòng và xử lý tức thời các sự cố phần cứng, tràn RAM GPU và lỗi đứt mạng.

### 📋 Danh mục Tác vụ & Kịch bản Ứng phó:
1. **Sự cố 1: Lỗi `CUDA Out of Memory (OOM)` khi train Swin-T:**
   - *Nguyên nhân:* Kích thước cửa sổ Attention hoặc Batch Size quá lớn so với 16GB VRAM.
   - *Giải pháp tức thời:* Giảm `BATCH_SIZE = 16`, tăng `gradient_accumulation_steps = 2`.
2. **Sự cố 2: Đứt kết nối phiên chạy trên Kaggle giữa chừng:**
   - *Giải pháp tức thời:* Mở lại Notebook 02, bấm chạy bình thường. Cell 4 sẽ tự động phát hiện `_checkpoint_last.pth` và tiếp tục huấn luyện mà không mất mát dữ liệu.
3. **Sự cố 3: Lỗi thiếu thư viện khi chạy Local WebApp:**
   - *Lệnh khắc phục 1 dòng:* `pip install streamlit matplotlib pillow numpy opencv-python torch torchvision`
