# 🛠 Hướng Dẫn Thiết Lập & Khởi Chạy Dự Án VietLawAssist — Agent SA-04

> **Task ID:** S2  
> **Loại output:** 🛠 Hướng dẫn Kỹ thuật Triển khai  
> **Ngày tạo:** 2026-09-09  
> **Dùng cho:** Hướng dẫn chạy đồ án cho giảng viên hướng dẫn, hội đồng phản biện & lập trình viên

---

## 1. Yêu Cầu Môi Trường Phần Cứng & Phần Mềm

### 1.1 Phần Cứng (Hardware Requirements)
- **Hệ điều hành:** Windows 10/11, macOS, hoặc Linux (Ubuntu 20.04+).
- **RAM:** Tối thiểu 4GB (Khuyến nghị 8GB+).
- **Bộ nhớ đĩa trống:** Tối thiểu 2GB.
- **GPU:** Không bắt buộc đối với Phase 1 (BM25 chạy thuần CPU).

### 1.2 Phần Mềm (Software Prerequisites)
- **Python:** Phiên bản `3.10` hoặc `3.11` (Khuyến nghị dùng Python 3.10.x).
- **Trình quản lý gói:** `pip >= 22.0`.
- **PowerShell / Terminal:** PowerShell 7 / Windows Terminal hoặc bash shell.

---

## 2. Quy Trình Cài Đặt Từng Bước (Step-by-Step Installation)

### Bước 1: Điều hướng vào thư mục mã nguồn dự án
Mở PowerShell và di chuyển vào thư mục `Project/`:
```powershell
cd "d:\User\7th\School\PBL6 - Machine Learning Trainning Model Project\Project"
```

### Bước 2: Tạo Môi trường Ảo (Virtual Environment)
Tạo môi trường ảo cách ly để tránh xung đột thư viện:
```powershell
python -m venv venv
```

Kích hoạt môi trường ảo:
- Trên Windows PowerShell:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
  *(Nếu gặp lỗi UnauthorizedAccess về Execution Policy, xem mục 5 bên dưới).*
- Trên Linux / macOS:
  ```bash
  source venv/bin/activate
  ```

### Bước 3: Nâng cấp pip và Cài đặt Thư viện
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```
*Thời gian cài đặt ước tính: 2 - 5 phút tùy tốc độ mạng.*

### Bước 4: Thiết lập Biến Môi trường (`.env`)
Sao chép tệp mẫu `.env.example` thành tệp cấu hình `.env`:
```powershell
Copy-Item .env.example .env
```

Nội dung cấu hình chuẩn trong `.env`:
```env
APP_NAME=VietLawAssist
APP_ENV=development
APP_DEBUG=true
APP_HOST=0.0.0.0
APP_PORT=8000

DATABASE_PATH=data/laws.db

# BM25 Hyperparameters
BM25_K1=1.5
BM25_B=0.75
BM25_DEFAULT_TOP_K=5
```

---

## 3. Khởi Tạo Cơ Sở Dữ Liệu & Nạp Dữ Liệu Mẫu

Khởi tạo bảng SQLite và nạp 30 điều luật mẫu từ `data/sample/sample_articles.json`:
```powershell
python -c "from app.core.database import init_db; init_db()"
```

Output kỳ vọng:
```text
[INFO] Khởi tạo cơ sở dữ liệu SQLite tại data/laws.db thành công.
[INFO] Bảng 'law_articles' đã sẵn sàng.
```

---

## 4. Khởi Chạy Ứng Dụng Backend

Chạy máy chủ phát triển bằng `uvicorn`:
```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Console hiển thị:
```text
INFO:     Will watch for changes in: ['d:\\User\\7th\\School\\...\\Project']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [14520] using WatchFiles
INFO:     Started server process [8324]
INFO:     Waiting for application startup.
INFO:     [Lifespan] Initializing SQLite database and BM25 index...
INFO:     [Lifespan] Loaded 30 articles into BM25 engine.
INFO:     Application startup complete.
```

---

## 5. Kiểm Thử API (Verification & Smoke Test)

### 5.1 Kiểm tra Sức khỏe Hệ thống (Health Check)
Mở một cửa sổ PowerShell mới và thực hiện lệnh:
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/health" -Method Get | ConvertTo-Json
```
**Kết quả mong đợi:**
```json
{
  "status": "healthy",
  "app_name": "VietLawAssist",
  "version": "1.0.0",
  "tier1_status": "ready",
  "total_articles_indexed": 30,
  "timestamp": "2026-09-09T07:15:00"
}
```

### 5.2 Kiểm thử Truy vấn Tìm kiếm BM25 (Retrieve API)
```powershell
$body = @{
    query = "Quyền bất khả xâm phạm về thân thể được quy định thế nào?"
    top_k = 3
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/retrieve" -Method Post -Body $body -ContentType "application/json" | ConvertTo-Json -Depth 4
```
**Kết quả mong đợi:**
```json
{
  "query": "Quyền bất khả xâm phạm về thân thể được quy định thế nào?",
  "total_results": 3,
  "execution_time_ms": 12.5,
  "results": [
    {
      "article_id": "HP2013_D20",
      "law_code": "HP2013",
      "law_name": "Hiến pháp nước Cộng hòa xã hội chủ nghĩa Việt Nam năm 2013",
      "title": "Điều 20. Quyền bất khả xâm phạm về thân thể",
      "score": 14.82,
      "rank": 1
    },
    {
      "article_id": "BLDS2015_D33",
      "law_code": "BLDS2015",
      "title": "Điều 33. Quyền sống, quyền được bảo đảm an toàn về tính mạng, sức khỏe, thân thể",
      "score": 8.45,
      "rank": 2
    }
  ]
}
```

---

## 6. Xử Lý Sự Cố Thường Gặp (Troubleshooting)

| Lỗi | Nguyên nhân | Cách khắc phục |
|---|---|---|
| `File ... cannot be loaded because running scripts is disabled on this system` | Chính sách bảo mật mặc định của PowerShell chặn file script `Activate.ps1`. | Chạy lệnh: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` trong PowerShell. |
| `ERROR: [Errno 10048] error while attempting to bind on address ('127.0.0.1', 8000)` | Cổng 8000 đang bị tiến trình khác chiếm dụng. | Đổi sang cổng khác: `uvicorn app.main:app --port 8080` hoặc tìm tắt PID: `netstat -ano \| findstr :8000` rồi `taskkill /PID <PID> /F`. |
| `ModuleNotFoundError: No module named 'pyvi'` | Chưa kích hoạt đúng môi trường ảo hoặc cài đặt thư viện thất bại. | Đảm bảo tiền tố `(venv)` hiển thị đầu dòng lệnh; chạy lại `pip install pyvi`. |
| `FileNotFoundError: data/laws.db` | Thư mục `data/` chưa được tạo trước khi chạy. | Chạy lệnh `New-Item -ItemType Directory -Force -Path "data"` để tạo thư mục dữ liệu. |
