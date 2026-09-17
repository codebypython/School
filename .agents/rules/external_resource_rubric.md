# ⚖️ BỘ THƯỚC ĐO THẨM ĐỊNH CHẤT LƯỢNG NGUỒN TRI THỨC NGOẠI SINH
## External Resource Quality Vetting Rubric (ER-QVR) — Thang Điểm 100

> **Cơ quan ban hành:** Academic Operations Crew (AOC) — DUT Semester 7 Hub  
> **Mục đích:** Sàng lọc, đánh giá và chọn lọc các nguồn tài liệu học thuật/kỹ thuật bên ngoài (Sách, Bài báo, Khóa học, Kho mã nguồn, Tài liệu tiêu chuẩn) để xây dựng giáo trình vững chắc cho các môn chưa có giáo trình nội bộ hoàn chỉnh.

---

## 1. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)

1. **"First-Principles Over Hype" (Bản chất hơn trào lưu)**: Mọi kiến thức được lựa chọn phải giải thích tường tận nguyên lý hoạt động, bản chất toán học hoặc cơ chế giao thức từ gốc rễ, không chấp nhận việc học vẹt hoặc chỉ sao chép code.
2. **"Reproducibility First" (Khả năng tái lập là thước đo sự thật)**: Mọi đoạn code, kịch bản cấu hình hoặc phân tích gói tin phải kiểm chứng được (reproducible) trên môi trường thực tế của sinh viên Đại học Bách khoa (DUT).
3. **"Pedagogical Scaffolding" (Bậc thang nhận thức sư phạm)**: Tài liệu phải đi theo lộ trình: *Trực quan hóa (Intuition) $\rightarrow$ Mô hình hóa/Toán học (Formalism) $\rightarrow$ Thực thi/Code (Implementation) $\rightarrow$ Đánh giá/Phản biện (Critical Reflection)*.

---

## 2. BẢNG TIÊU CHÍ ĐÁNH GIÁ CHI TIẾT (100 ĐIỂM)

### Trụ Cột 1: Độ Chuẩn Xác Học Thuật & Nền Tảng Lý Thuyết (25 Điểm)
*Trọng tâm: Nền tảng toán học, tính đúng đắn khoa học và định dạng chuẩn mực.*

| Mức Điểm | Tiêu Chuẩn Đạt Được |
| :---: | :--- |
| **23 – 25 đ** | Chứng minh toán học/cơ chế giao thức đầy đủ, chính xác từng bước; giải thích rõ giả định của bài toán (assumptions); định dạng công thức chuẩn mực (LaTeX/KaTeX); định nghĩa biến số và không gian mẫu rõ ràng. |
| **18 – 22 đ** | Trình bày đúng bản chất lý thuyết nhưng lược bớt một vài bước chứng minh trung gian; công thức rõ ràng, dễ hiểu. |
| **12 – 17 đ** | Chỉ nêu công thức cuối cùng hoặc tóm tắt sơ lược cơ chế; thiếu phân tích chuyên sâu về điều kiện biên (edge cases). |
| **0 – 11 đ** | Lý thuyết có sai sót, hiểu sai bản chất giao thức/thuật toán hoặc chỉ đưa ra phát biểu định tính vô căn cứ. |

---

### Trụ Cột 2: Tính Sư Phạm & Bậc Thang Nhận Thức (20 Điểm)
*Trọng tâm: Khả năng dẫn dắt người học từ chưa biết đến thành thạo.*

| Mức Điểm | Tiêu Chuẩn Đạt Được |
| :---: | :--- |
| **18 – 20 đ** | Bố cục sư phạm hoàn hảo: Đi từ bài toán thực tế $\rightarrow$ Giải pháp trực quan $\rightarrow$ Công thức toán học $\rightarrow$ Minh họa đồ họa/sơ đồ khối $\rightarrow$ Câu hỏi kiểm tra độ hiểu (Active Recall). |
| **14 – 17 đ** | Trình bày mạch lạc, có ví dụ minh họa và sơ đồ; giải thích dễ hiểu nhưng thiếu phần tự kiểm tra năng lực. |
| **10 – 13 đ** | Trình bày theo dạng liệt kê sự thật (fact-dumping), ít liên kết logic giữa các phần; người học phải tự xâu chuỗi. |
| **0 – 9 đ** | Rời rạc, câu chữ tối nghĩa, không có định hướng người đọc. |

---

### Trụ Cột 3: Tính Thực Chiến & Khả Năng Tái Lập (25 Điểm)
*Trọng tâm: Khả năng ứng dụng vào Lab, Code, và Vận hành hệ thống.*

| Mức Điểm | Tiêu Chuẩn Đạt Được |
| :---: | :--- |
| **23 – 25 đ** | Code/Lệnh CLI chuẩn hiện đại (Python 3.10+, PyTorch 2.x, Cisco IOS 15+, Linux RHEL 9/Ubuntu 22+); comment chi tiết từng dòng quan trọng; đi kèm dữ liệu mẫu (Sample Dataset, PCAP file, Topo GNS3/Packet Tracer) có thể clone và chạy thành công 100%. |
| **18 – 22 đ** | Code/Lệnh chính xác, chạy được sau khi cài đặt môi trường cơ bản; có hướng dẫn debug lỗi phổ biến. |
| **12 – 17 đ** | Code ở dạng đoạn mã rời rạc (pseudocode hoặc snippet cắt khúc); cần người học tự bổ sung thêm khung chương trình để chạy được. |
| **0 – 11 đ** | Code lỗi thời, sử dụng thư viện đã deprecated, phụ thuộc vào đường dẫn cứng không tồn tại, hoặc không chạy được. |

---

### Trụ Cột 4: Thẩm Quyền & Độ Tin Cậy Quốc Tế (15 Điểm)
*Trọng tâm: Uy tín của tác giả, nhà xuất bản và tổ chức ban hành.*

| Mức Điểm | Tiêu Chuẩn Đạt Được |
| :---: | :--- |
| **14 – 15 đ** | Giáo trình từ các trường đại học hàng đầu thế giới (Stanford, MIT, Berkeley, CMU); sách của các NXB uy tín (O'Reilly, Springer, MIT Press, Cisco Press); Tiêu chuẩn chính thức (RFC, NIST, IEEE, W3C, Official Framework Docs). |
| **11 – 13 đ** | Giáo trình đại học quốc tế uy tín khác; bài báo bình duyệt (peer-reviewed papers) tại các hội nghị đỉnh cao (CVPR, NeurIPS, USENIX, SIGCOMM); sách của chuyên gia đầu ngành có nhiều trích dẫn. |
| **7 – 10 đ** | Khóa học uy tín trên Coursera/edX (do trường ĐH đứng tên); blog kỹ thuật của các công ty công nghệ lớn (Google AI, Meta AI, AWS Architecture Blog). |
| **0 – 6 đ** | Bài viết blog cá nhân trôi nổi không rõ danh tính tác giả, bài dịch tự phát không kiểm chứng. |

---

### Trụ Cột 5: Tương Thích Ngữ Cảnh Kỹ Sư DUT (15 Điểm)
*Trọng tâm: Phù hợp với năng lực phần cứng, chuẩn đầu ra và môi trường học tập tại ĐHBK Đà Nẵng.*

| Mức Điểm | Tiêu Chuẩn Đạt Được |
| :---: | :--- |
| **14 – 15 đ** | Hoàn toàn tương thích phần cứng sinh viên (GPU 4GB VRAM / Google Colab T4 / RAM 16GB); khớp 100% với đề cương môn học và rubric chấm điểm DUT; tài liệu song ngữ hoặc tiếng Anh kỹ thuật chuẩn mực, thuật ngữ đồng nhất. |
| **11 – 13 đ** | Chạy tốt trên phần cứng cá nhân nhưng cần tinh chỉnh giảm batch size hoặc lượng tử hóa; khớp 80% với chuẩn DUT. |
| **7 – 10 đ** | Yêu cầu tài nguyên tính toán cao (cần GPU lớn hoặc cụm server) gây khó khăn cho việc tự thực hành ở nhà. |
| **0 – 6 đ** | Không phù hợp với điều kiện thực tế của sinh viên; nội dung lệch xa chuẩn đầu ra của ngành. |

---

## 3. PHÂN CẤP CHẤT LƯỢNG NGUỒN (TIER CLASSIFICATION)

Dựa trên tổng điểm ER-QVR (Thang 100), tài liệu được phân thành 4 cấp bậc:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 🏆 TIER A+ (>= 90 Điểm) — NGUỒN KINH ĐIỂN CỐT LÕI (Canonical Core)      │
│ ➔ Bắt buộc đưa vào làm khung xương giáo trình chính của môn học.       │
├─────────────────────────────────────────────────────────────────────────┤
│ ⭐ TIER A  (80 – 89 Điểm) — NGUỒN XUẤT SẮC (Excellent Benchmark)        │
│ ➔ Dùng làm tài liệu đối chiếu, bổ trợ đào sâu và thực hành chính quy.   │
├─────────────────────────────────────────────────────────────────────────┤
│ 📚 TIER B  (70 – 79 Điểm) — NGUỒN BỔ TRỢ (Supplementary Reference)     │
│ ➔ Dùng cho các bài đọc thêm, đồ án mở rộng hoặc tra cứu nhanh.        │
├─────────────────────────────────────────────────────────────────────────┤
│ ❌ REJECTED (< 70 Điểm) — LOẠI BỎ (Substandard / Outdated)              │
│ ➔ Tuyệt đối không đưa vào hệ thống học tập để tránh sai lệch tư duy.    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 4. QUY TẮC BỘ LỌC CỨNG (HARD GATEKEEPER RULES)

Bất kể tài liệu đạt bao nhiêu điểm ở các tiêu chí khác, nếu vi phạm một trong các điều sau, tài liệu sẽ bị **LOẠI BỎ NGAY LẬP TỨC (Điểm = 0)**:

1. **Lỗi thời & Nguy hiểm**: Hướng dẫn sử dụng các giao thức đã bị khuyến cáo cấm sử dụng trong môi trường thực tế (VD: Telnet không mã hóa, DES, MD5 cho chữ ký số, SSLv3, WEP).
2. **Hộp đen (Black-box)**: Code chỉ gọi hàm của bên thứ ba mà hoàn toàn không giải thích tham số, ý nghĩa toán học hoặc logic thuật toán.
3. **Mã nguồn không thể chạy**: Script dính lỗi cú pháp cơ bản hoặc phụ thuộc vào các gói cài đặt đã bị xóa khỏi PyPI/GitHub.
