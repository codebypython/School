# 🎓 KẾ HOẠCH TRIỂN KHAI & RUBRIC ĐÁNH GIÁ ĐỒ ÁN PBL6
## KHOA CÔNG NGHỆ THÔNG TIN — TRƯỜNG ĐẠI HỌC BÁCH KHOA, ĐẠI HỌC ĐÀ NẴNG (DUT)
> **Học phần:** PBL6 — Đồ án chuyên ngành 1  
> **Khóa sinh viên:** K2023 | **Quy mô:** ~100 Sinh viên  
> **Căn cứ:** Kế hoạch chính thức của Bộ môn và Khoa CNTT — ĐHBK Đà Nẵng (Phụ trách: Thầy Phạm Công Thắng)

---

## 1. DANH SÁCH GIẢNG VIÊN HƯỚNG DẪN & NHÓM HỌC PHẦN

| STT | Nhóm HP | SLSV | Giảng viên hướng dẫn | Ghi chú |
| :-: | :---: | :---: | :--- | :--- |
| 1 | 23.16A | 20 | TS. Phạm Minh Tuấn | |
| 2 | 23.16B | 20 | ThS. Phạm Công Thắng | Phụ trách chung tiến độ |
| 3 | 23.16C | 20 | TS. Võ Đức Hoàng | |
| 4 | 23.99B | 20 | TS. Ninh Khánh Duy | ThS. Lê Minh Trí |
| 5 | 23.99C | 20 | TS. Nguyễn Văn Hiệu | Đồng Ngọc Nguyên Thịnh, Mai Văn Hà |
| **Tổng** | | **100** | | |

---

## 2. YÊU CẦU NỘI DUNG & CHUẨN ĐẦU RA KIẾN THỨC CỦA ĐỒ ÁN

Đồ án chuyên ngành PBL6 yêu cầu sinh viên phát triển các hệ thống thông minh, tổng hợp kiến thức chuyên ngành CNTT: **Học máy & Ứng dụng**, **Quản trị mạng & Máy chủ**, và **Kiểm thử phần mềm**.

### 2.1. Yêu cầu Kiến thức Chuyên môn
- **Học máy (Machine Learning / NLP):** Phân tích, lựa chọn mô hình học máy phù hợp với bài toán thực tiễn; giải thích được cơ sở lý thuyết và kết quả thực nghiệm.
- **Quản trị hệ thống (System Administration):** Thiết lập và cấu hình Server tự quản trị (cài đặt Hệ điều hành, cấu hình Web server, Reverse Proxy, bảo mật).
- **Kiểm thử hệ thống (Software & Load Testing):** Đề xuất và triển khai quy trình kiểm thử trước khi vận hành (kiểm thử phần mềm, phần cứng, mạng và kiểm thử chịu tải).

### 2.2. Công nghệ, Ngôn ngữ & Công cụ Quy định
- **Ngôn ngữ lập trình:** Python (hoặc C/C++, Java, Node.js...).
- **Thư viện Học máy:** PyTorch, HuggingFace, Transformers, PEFT/LoRA, scikit-learn, rank_bm25, FAISS.
- **Web Server & Hệ điều hành:** Ubuntu Server, Nginx, FastAPI / Gunicorn.
- **Công cụ kiểm thử bắt buộc:** Artillery (kiểm thử chịu tải mạng/server), Selenium / PyTest (kiểm thử chức năng phần mềm).

### 2.3. Yêu cầu Kỹ thuật Bắt buộc của Sản phẩm
1. Phải có ứng dụng hoàn chỉnh (Web App / Mobile / Desktop) kết nối với REST API đã triển khai trên server tự cấu hình.
2. **Bắt buộc có tối thiểu 01 phương pháp đối sánh (Baseline Comparison)** để chứng minh tính vượt trội của giải pháp đề xuất.
3. Giải thích được lý do (cả lý thuyết và thực nghiệm) việc áp dụng mô hình.
4. Triển khai quy trình kiểm thử toàn diện và có số liệu báo cáo rõ ràng.
5. Toàn bộ quy trình và kết quả triển khai phải có mặt trong Quyển Báo cáo Đồ án cuối cùng.

---

## 3. KẾ HOẠCH TIẾN ĐỘ 15 TUẦN & NỘP BÁO CÁO

| Giai đoạn | Thời gian | Nhiệm vụ trọng tâm | Yêu cầu nghiệm thu |
| :--- | :---: | :--- | :--- |
| **Giai đoạn 1** | Tuần 01 – 02 | Nhận đề tài, khảo sát bài toán, xác định tên đề tài chính thức | Đăng ký tên đề tài với GVHD (chậm nhất cuối tuần 4) |
| **Giai đoạn 2** | Tuần 03 – 13 | Triển khai nghiên cứu, huấn luyện mô hình, xây dựng hệ thống, kiểm thử | **Nộp Báo cáo tiến độ Đợt 1 & Đợt 2 cho Thầy Thắng** (có xác nhận khối lượng của GVHD) |
| **Giai đoạn 3** | Tuần 14 – 15 | Hoàn thiện phần mềm, viết quyển báo cáo, chuẩn bị Slide | Tổng duyệt sản phẩm, nộp quyển và chuẩn bị bảo vệ |

---

## 4. CƠ CẤU ĐIỂM SỐ & NGUYÊN TẮC ĐÁNH GIÁ

- **Điểm Quá trình (40%):** Giảng viên hướng dẫn đánh giá dựa trên thái độ, tiến độ và chất lượng qua các buổi gặp. *(Không nộp báo cáo tiến độ xem như không thực hiện đồ án).*
- **Điểm Bảo vệ Cuối kỳ (60%):** Hội đồng phản biện chấm thi theo **nguyên tắc chấm chéo** thông qua thuyết trình Slide, Demo trực tiếp sản phẩm và trả lời câu hỏi chuyên môn. *(Yêu cầu chữ ký xác nhận của GVHD trước khi ra Hội đồng).*

---

## 5. RUBRIC ĐÁNH GIÁ ĐỒ ÁN PBL6 (THANG ĐIỂM 10)

| STT | Tiêu chí đánh giá | Thang điểm | Mô tả chuẩn đầu ra chi tiết |
| :-: | :--- | :---: | :--- |
| **#1** | **Tính cấp thiết và khả năng ứng dụng của đề tài** | **1.0 điểm** | • Đề tài phản ánh đúng nhu cầu thực tế, phù hợp với xu hướng công nghệ hiện đại.<br>• Có tiềm năng ứng dụng thực tiễn cao hoặc mở rộng nghiên cứu khoa học. |
| **#2** | **Kết quả giải quyết các nhiệm vụ của đồ án** | **3.0 điểm** | • Hoàn thành đúng và đủ 100% các yêu cầu nhiệm vụ đề ra.<br>• Sản phẩm hoạt động ổn định, trơn tru, có tính khả thi cao.<br>• Thể hiện tính sáng tạo và tinh thần chủ động trong quá trình thực hiện. |
| **#3** | **Mức độ am hiểu về các giải pháp thông qua trả lời câu hỏi Hội đồng** | **2.0 điểm** | • Nắm vững nguyên lý hoạt động, bản chất toán học và cơ chế của thuật toán.<br>• Trả lời rõ ràng, mạch lạc, thuyết phục các câu hỏi chuyên môn sâu của Hội đồng. |
| **#4** | **Chất lượng của quyển báo cáo** | **2.0 điểm** | • Cấu trúc nội dung chặt chẽ, trình bày khoa học, văn phong kỹ thuật chuẩn xác.<br>• Hình ảnh minh họa, sơ đồ kiến trúc, bảng biểu rõ ràng, trích dẫn đúng quy chuẩn học thuật. |
| **#5** | **Kỹ năng thuyết trình slide và demo sản phẩm** | **2.0 điểm** | • Slide gọn gàng, súc tích, làm nổi bật được đóng góp kỹ thuật cốt lõi.<br>• Trình bày tự tin, tương tác tốt; Demo sản phẩm mượt mà, đầy đủ các chức năng. |
| | **TỔNG CỘNG** | **10.0 điểm** | **Mục tiêu của dự án: Đạt điểm tối đa 10/10** |
