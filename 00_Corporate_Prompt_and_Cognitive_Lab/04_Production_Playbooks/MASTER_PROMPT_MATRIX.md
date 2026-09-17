# 🎛️ MA TRẬN ĐIỀU PHỐI PROMPT THỰC CHIẾN (MASTER PROMPT MATRIX)
## Decision Matrix for Model Selection x Domain Architecture x Task Type

> **Mã văn kiện:** `PLB-MATRIX-01` | **Khối chuyên trách:** `04_Production_Playbooks`  
> **Áp dụng cho:** Sinh viên (Handmade CEO) và Hệ thống Điều phối Agent Tập đoàn

---

## 1. MA TRẬN LỰA CHỌN MÔ HÌNH NỀN TẢNG (MODEL ROUTING MATRIX)

| Chuyên Môn / Môn Học | Loại Nhiệm Vụ Cụ Thể | Mô Hình Khuyên Dùng Số 1 | Mô Hình Dự Phòng Số 2 | Lý Do Kỹ Thuật |
|:---|:---|:---:|:---:|:---|
| **CORP-01-CV** (Thị giác máy tính) | Viết model PyTorch, Debug shape | **Claude 3.5/3.7 Sonnet** | **Gemini 3.1 Pro** | Claude kiểm soát chặt chẽ tensor dimensions và assert statements. |
| **CORP-01-CV** (Thị giác máy tính) | Đọc hiểu đồ thị, Sơ đồ CNN | **Gemini 3.1 Pro** | **Gemini 3.8 Flash** | Thế mạnh xử lý ảnh trực tiếp (Multimodal Native Grounding). |
| **CORP-02-ML** (Học máy) | Đạo hàm toán học, Chứng minh OLS | **Claude Opus / Sonnet** | **Gemini 3.1 Pro** | Khả năng Extended Thinking suy luận công thức LaTeX chuẩn xác. |
| **CORP-02-ML** (Học máy) | Thử nghiệm nhanh, Tuning tham số | **Gemini 3.8 Flash** | **Claude Sonnet** | Tốc độ sinh mã cực nhanh, chi phí token thấp. |
| **CORP-03-NMA** (Quản trị mạng) | Quy hoạch IP, Viết script PowerShell | **Claude 3.5/3.7 Sonnet** | **Gemini 3.1 Pro** | Cú pháp CLI và PowerShell chặt chẽ, không bị ảo giác tham số. |
| **CORP-04-SEC** (An toàn mạng) | Phân tích RFC, Luồng bắt tay TLS | **Claude 3.5/3.7 Sonnet** | **Gemini 3.1 Pro** | Phân tích logic máy trạng thái giao thức cực kỳ sắc bén. |
| **CORP-05-JPN** (Tiếng Nhật IT) | Chiết tự Kanji, So sánh sắc thái | **Gemini 3.1 Pro** | **Claude Sonnet** | Kho ngữ liệu tiếng Nhật khổng lồ của Google DeepMind. |
| **VENTURE-06** (AI Pháp lý PBL6) | Giải đề thi chuẩn Barem JSON | **Claude 3.5/3.7 Sonnet** | **Gemini 3.1 Pro** | Ép kiểu dữ liệu cấu trúc và bám sát tam đoạn luận pháp lý tuyệt đối. |

---

## 2. QUY TRÌNH 3 BƯỚC KHỞI TẠO CA LÀM VIỆC TỐI ƯU

Khi bạn muốn bắt đầu một công việc với chất lượng cao nhất:

1. **Bước 1 (Chọn Model)**: Mở phần mềm chat / IDE và chọn mô hình theo cột **"Mô hình Khuyên Dùng"** ở bảng trên.
2. **Bước 2 (Lấy Prompt Engine Chuyên Dụng)**:
   - Nếu dùng **Gemini**: Mở file Engine tương ứng trong `00_Corporate_Prompt_and_Cognitive_Lab/02_Domain_Cognitive_Engines/`, copy khối **Gemini Engine**.
   - Nếu dùng **Claude**: Mở file Engine tương ứng, copy khối **Claude Engine (XML Tags)**.
3. **Bước 3 (Điền Working Memory Snapshot)**: Điền thông tin tuần học, nhiệm vụ cụ thể vào các trường `[ ... ]` hoặc `<...>` $\longrightarrow$ Nhấn Gửi để kích hoạt Agent với hiệu năng cao nhất.
