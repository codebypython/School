# 📜 ĐIỀU LỆ PHÒNG CÔNG CỤ & KIỂM SOÁT SỰ CỐ (TROUBLESHOOTING & TOOLKITS DEPT)
## Phòng 05 — Công Ty Công Nghệ Thị Giác Máy Tính (CORP-01-CV)

> **Mã Phòng Ban:** `CV-DEPT-05`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (Role Handmade) & `PSD-04`

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
- Quản lý các công cụ phụ trợ, script kiểm tra CUDA/GPU, công cụ gán nhãn ảnh (LabelImg, CVAT, Roboflow).
- Lưu trữ nhật ký lỗi kinh điển trong Computer Vision: Lỗi tràn VRAM (CUDA Out of Memory), lỗi kênh màu RGB vs BGR trong OpenCV, lỗi chuẩn hóa ảnh thiếu chia 255.

## 2. TÀI SẢN LƯU TRỮ (STORED ASSETS)
- Các đoạn script chẩn đoán phần cứng (kiểm tra CUDA capability, PyTorch GPU tensor allocation).
- Sổ tay hướng dẫn debug các lỗi biên giới tính toán ma trận và nén mô hình ONNX.

## 3. MỤC ĐÍCH SỬ DỤNG & WORKFLOW
- Khi gặp lỗi `RuntimeError: CUDA out of memory` hoặc ảnh đầu ra bị đổi màu sai lệch, sinh viên tra cứu phòng ban này để tìm hướng giải quyết tức thì.
