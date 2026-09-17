# 📦 Cẩm Nang Quản Lý Môi Trường Ảo (.venv) — VietLawAssist

> **Dự án:** VietLawAssist — PBL6 Machine Learning Training Model Project  
> **Phiên bản Python chuẩn:** `Python 3.11.9 (64-bit)`  
> **Trạng thái:** ✅ Đã khởi tạo và kiểm thử thành công 100% (21/21 thư viện cốt lõi)

---

## 1. Kiến Trúc Môi Trường Ảo (.venv Architecture)

Nhằm tối ưu hóa trải nghiệm lập trình trên cả Workspace Root và thư mục con `Project/`:
- Môi trường gốc thực tế được lưu tại: `Project/.venv/`
- Tại thư mục gốc Workspace tạo một **NTFS Junction** trỏ vào: `.venv/ -> Project/.venv/`
- Cấu hình IDE (`.vscode/settings.json`) đã được cài đặt tự động nhận diện Python interpreter tại `${workspaceFolder}/.venv/Scripts/python.exe`.

```text
d:\User\7th\School\PBL6 - Machine Learning Trainning Model Project\
├── .venv/                         [Junction trỏ vào Project\.venv]
├── .vscode/
│   └── settings.json              [Tự động gắn interpreter và paths]
├── manage_venv.ps1                [Script quản lý cho PowerShell]
├── manage_venv.bat                [Script quản lý cho Command Prompt]
└── Project/
    ├── .venv/                     [Môi trường ảo Python 3.11 thực tế]
    ├── .env                       [Cấu hình môi trường đã khởi tạo]
    ├── requirements.txt           [Danh mục dependencies]
    ├── scripts/
    │   └── check_env.py           [Script chẩn đoán toàn diện môi trường]
    └── tests/
        └── test_smoke.py          [Bộ kiểm thử tự động xác minh môi trường]
```

---

## 2. Cách Kích Hoạt & Sử Dụng

### Cách 1: Sử dụng PowerShell
```powershell
# Kích hoạt môi trường ảo:
.\.venv\Scripts\Activate.ps1

# Hoặc dùng script quản lý:
.\manage_venv.ps1 activate
```
*(Nếu gặp lỗi UnauthorizedAccess về chính sách script, mở PowerShell và gõ: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)*

### Cách 2: Sử dụng Command Prompt (CMD)
```cmd
call .venv\Scripts\activate.bat
```

---

## 3. Các Lệnh Tiện Ích Qua `manage_venv`

| Thao tác | Lệnh PowerShell | Lệnh CMD | Mô tả |
|---|---|---|---|
| **Kiểm tra chẩn đoán** | `.\manage_venv.ps1 check` | `manage_venv.bat check` | Kiểm tra 21 thư viện cốt lõi xem có cài đủ và import được không. |
| **Cài đặt / Cập nhật** | `.\manage_venv.ps1 install` | `manage_venv.bat install` | Nâng cấp pip và cài đặt lại toàn bộ gói từ `requirements.txt`. |
| **Chạy kiểm thử tự động** | `.\manage_venv.ps1 test` | `manage_venv.bat test` | Chạy 4 bài test tự động với `pytest` (Model, NLP, BM25, API). |
| **Khởi chạy Server Backend**| `.\manage_venv.ps1 run-server` | `manage_venv.bat run-server` | Khởi chạy máy chủ FastAPI Uvicorn tại `http://127.0.0.1:8000`. |

---

## 4. Danh Mục Thư Viện Cốt Lõi Đã Cài Đặt

### Tầng Web Backend & API:
- `fastapi==0.115.0`: Khung ứng dụng web asynchronous hiệu năng cao.
- `uvicorn[standard]==0.30.0`: ASGI Web Server với reload tự động.
- `pydantic==2.9.0` & `pydantic-settings==2.5.0`: Validation dữ liệu tốc độ cao qua Rust core.
- `python-dotenv==1.0.1`: Nạp cấu hình từ file `.env`.
- `aiosqlite==0.20.0`: Trình điều khiển SQLite bất đồng bộ.

### Tầng Kỹ Thuật Dữ Liệu & Bóc Tách (Data Engineering):
- `beautifulsoup4==4.12.3`: Phân tích cú pháp DOM HTML từ vbpl.vn và thuvienphapluat.vn.
- `httpx==0.27.0`: Client HTTP bất đồng bộ hỗ trợ HTTP/2.
- `PyMuPDF==1.24.0` (`fitz`): Bóc tách toàn văn PDF văn bản pháp luật chính phủ.
- `lxml==5.3.0`: Trình tăng tốc xử lý XML/HTML.
- `pandas==2.2.0`: Phân tích và quản trị dữ liệu bảng câu hỏi/điều luật.

### Tầng Xử Lý Ngôn Ngữ Tự Nhiên & Tìm Kiếm (NLP & Retrieval):
- `pyvi==0.1.1`: Bộ tách từ tiếng Việt chuẩn xác (Word Segmentation).
- `rank-bm25==0.2.2`: Thuật toán chấm điểm tìm kiếm BM25Okapi Tầng 1.
- `underthesea==6.8.4`: Bộ công cụ NLP tiếng Việt mở rộng.
- `regex==2024.7.24` & `Unidecode==1.3.8`: Xử lý văn bản và chuẩn hóa ký tự.

### Tầng Kiểm Thử & Ghi Log:
- `pytest==8.3.0` & `pytest-asyncio==0.24.0`: Framework kiểm thử tự động.
- `loguru==0.7.2`: Ghi log màu và tự động xoay vòng file log.
- `tqdm==4.66.0`: Thanh hiển thị tiến độ tiến trình.
- `click==8.1.7`: Khung xây dựng CLI.
