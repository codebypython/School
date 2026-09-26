# 📘 CẨM NANG HƯỚNG DẪN XỬ LÝ ĐỀ THI ẢNH SCAN & TỆP DỮ LIỆU RỜI RẠC
## Dự án: VietLawAssist — PBL6 Khoa CNTT, ĐHBK Đà Nẵng (DUT)

Tài liệu này cung cấp giải pháp kỹ thuật trọn vẹn, chạy **OFFLINE 100% MIỄN PHÍ** trên máy tính của bạn để giải quyết 3 tình huống khó khăn nhất khi thu thập tài liệu học tập:
1. **Tình huống 1**: File PDF là **thuần ảnh scan** hoặc ảnh chụp crop từ điện thoại.
2. **Tình huống 2**: File **Đề bài và File Đáp án rời rạc** nhau (2 file độc lập).
3. **Tình huống 3**: Đề bài và Đáp án nằm **chung 1 file nhưng tách làm 2 phần** (Phần I: Đề, Phần II: Đáp án).

---

## TÌNH HUỐNG 1: XỬ LÝ FILE PDF THUẦN ẢNH SCAN / ẢNH CHỤP CROP

Hệ thống đã tích hợp sẵn module [smart_ocr.py](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/Project/scripts/data_pipeline/smart_ocr.py) kết hợp giữa:
- **PyMuPDF**: Render ảnh độ nét cao (DPI 300) từ các trang PDF.
- **Pillow**: Tự động lọc xám, tăng độ tương phản và làm sắc nét chữ.
- **Tesseract-OCR v5 (vie)**: Đã cài sẵn trên máy bạn (`C:\Program Files\Tesseract-OCR`), nhận diện chữ tiếng Việt có dấu với tốc độ cao mà không tốn phí dịch vụ web.

### 1. Nếu bạn có 1 file PDF scan:
Mở terminal tại thư mục `Project/` và chạy:
```powershell
.\.venv\Scripts\python.exe -m scripts.data_pipeline.manage_pipeline ocr --file "đường_dẫn_tới_file_scan.pdf"
```
*Kết quả*: Hệ thống tự động OCR từng trang và xuất ra file text sạch tại `Project/data/raw/exams/[tên_file]_ocr.txt`.

### 2. Nếu bạn có 1 thư mục chứa nhiều ảnh chụp crop (.png, .jpg):
```powershell
.\.venv\Scripts\python.exe -m scripts.data_pipeline.manage_pipeline ocr --folder "đường_dẫn_tới_thư_mục_ảnh"
```
*Kết quả*: Hệ thống tự động duyệt qua tất cả ảnh, OCR theo thứ tự và gom thành 1 file text tổng hợp duy nhất.

---

## TÌNH HUỐNG 2: ĐỀ BÀI VÀ ĐÁP ÁN NẰM Ở 2 FILE RỜI RẠC

Nhiều trường hợp bạn có:
- File A (`de_thi.txt`): Chứa Câu 1, Câu 2, Câu 3...
- File B (`dap_an.txt`): Chứa Đáp án Câu 1, Đáp án Câu 2, Đáp án Câu 3...

Module [exam_pairer.py](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/Project/scripts/data_pipeline/exam_pairer.py) sẽ tự động bóc tách số thứ tự câu ở cả 2 bên và ghép cặp thông minh theo số câu:

### Lệnh thực thi:
```powershell
.\.venv\Scripts\python.exe -m scripts.data_pipeline.manage_pipeline pair -q "đường_dẫn_file_đề.txt" -a "đường_dẫn_file_đáp_án.txt"
```

### Kết quả tự động tạo ra:
Hệ thống sẽ sinh ra file mới tại `Project/data/raw/exams/` với format 2 mốc neo chuẩn mực:
```text
Câu 1: [Nội dung câu 1 từ file đề]
Đáp án: [Nội dung đáp án câu 1 từ file đáp án]

Câu 2: [Nội dung câu 2 từ file đề]
Đáp án: [Nội dung đáp án câu 2 từ file đáp án]
```

---

## TÌNH HUỐNG 3: ĐỀ THI & ĐÁP ÁN NẰM CHUNG 1 FILE NHƯNG CHIA 2 PHẦN LỚN

Dạng đề thi này thường có cấu trúc:
```text
PHẦN I: ĐỀ BÀI
Câu 1: Ông A và bà B...
Câu 2: Nhận định đúng sai...

PHẦN II: HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN
Câu 1: Căn cứ Điều 644...
Câu 2: Khẳng định trên là Sai...
```

Nếu để nguyên, máy sẽ không biết câu 1 ở phần II là đáp án của câu 1 ở phần I.

### Lệnh tự động chuẩn hóa:
```powershell
.\.venv\Scripts\python.exe -m scripts.data_pipeline.manage_pipeline pair -s "đường_dẫn_file_hai_phần.txt"
```
*Kết quả*: Hệ thống tự động cắt đôi ranh giới giữa Phần I và Phần II, bóc tách từng số câu và ghép thành file Q&A xen kẽ chuẩn barem!

---

## TÌNH HUỐNG 4: ĐỀ THI & ĐÁP ÁN ĐÃ NẰM XEN KẼ SẴN

Nếu file của bạn đã có dạng:
```text
Câu 1: ...
Đáp án: ...

Câu 2: ...
Đáp án: ...
```
Bạn **KHÔNG CẦN CHẠY LỆNH PAIR HAY OCR NÀO CẢ**. Chỉ cần thả trực tiếp file vào thư mục:  
📁 `Project/data/raw/exams/`

---

## TỔNG KẾT: QUY TRÌNH MỘT CHẠM TỪ RAW SANG KAGGLE BUNDLE

Sau khi đã có các file text đề thi sạch trong thư mục `Project/data/raw/exams/`, bạn chỉ cần chạy **đúng 1 lệnh duy nhất**:

```powershell
cd D:\User\7th\School\06_Venture_PBL6_VietLawAssist_LegalAI\Project
.\.venv\Scripts\python.exe -m scripts.data_pipeline.manage_pipeline run-all
```

**Chuỗi xử lý tự động sẽ diễn ra hoàn toàn khép kín**:
1. Bóc tách câu hỏi và đáp án từ kho đề thi thực tế (`crawl-exams`).
2. Gán nhãn Intent tự động (`detect_intent_from_text`).
3. Hòa trộn đề thi thật + dữ liệu synthetic $\rightarrow$ Khử trùng lặp MD5 100% (`curate-sft`).
4. Chạy Citation Guardrail kiểm tra số hiệu điều luật thực định trong SQLite.
5. Phân tầng 80% Train / 20% Val ở cả 2 định dạng Alpaca và ChatML (`split-sft`).
6. Đồng bộ toàn bộ dữ liệu sạch sang `Project/kaggle/dataset/` kèm mã băm MD5 và file cấu hình sẵn sàng nạp lên Kaggle!
