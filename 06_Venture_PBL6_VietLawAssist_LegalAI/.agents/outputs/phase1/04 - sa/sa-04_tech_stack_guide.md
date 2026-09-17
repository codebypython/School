# 🛠 Cẩm Nang Kỹ Thuật: FastAPI + SQLite + Pydantic v2 — Agent SA-04

> **Task ID:** S4  
> **Loại output:** 🛠 Hướng dẫn Công nghệ & Chuẩn Thiết kế Mã nguồn  
> **Ngày tạo:** 2026-09-09  
> **Dùng cho:** Chương 3.2 Báo cáo đồ án + Sổ tay lập trình viên VietLawAssist

---

## 1. FastAPI: Khung Ứng Dụng Web Hiện Đại

VietLawAssist lựa chọn **FastAPI** thay vì Flask hay Django bởi các đặc tính kỹ thuật vượt trội:
- **Tốc độ cao:** Dựa trên Starlette và Pydantic, hiệu năng xấp xỉ NodeJS và Go.
- **Bất đồng bộ bản địa (Native Async/Await):** Giúp hệ sinh thái phục vụ hàng nghìn truy vấn đồng thời mà không bị nghẽn (non-blocking I/O).
- **Tự động sinh tài liệu chuẩn:** Tự động tạo Swagger UI tại `/docs` và ReDoc tại `/redoc`.

### 1.1 Quản Lý Vòng Đời Ứng Dụng với `lifespan`
Thay thế các decorator cũ (`@app.on_event("startup")`), FastAPI khuyến nghị sử dụng `asynccontextmanager`:

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.services.bm25_service import get_bm25_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- KHỞI ĐỘNG (STARTUP) ---
    print("[Lifespan] Đang nạp chỉ mục BM25 vào bộ nhớ RAM...")
    bm25_service = get_bm25_service()
    bm25_service.initialize_index()
    yield
    # --- TẮT MÁY CHỦ (SHUTDOWN) ---
    print("[Lifespan] Đang giải phóng tài nguyên và đóng kết nối DB...")
    bm25_service.close()

app = FastAPI(title="VietLawAssist API", lifespan=lifespan)
```

### 1.2 Cơ Chế Tiêm Phụ Thuộc (Dependency Injection - `Depends`)
Dependency Injection giúp tách biệt việc khởi tạo tài nguyên khỏi logic điều hướng (clean separation):

```python
from fastapi import APIRouter, Depends
from app.services.bm25_service import BM25Service, get_bm25_service

router = APIRouter(prefix="/api", tags=["Retrieval"])

@router.post("/retrieve")
async def retrieve_articles(
    request: SearchRequest,
    bm25_svc: BM25Service = Depends(get_bm25_service)
):
    results = bm25_svc.search(query=request.query, top_k=request.top_k)
    return results
```

---

## 2. SQLite: Hệ Quản Trị Cơ Sở Dữ Liệu Cục Bộ Tối Ưu

### 2.1 Cấu Hình Kết Nối Đa Luồng An Toàn (Thread Safety)
Trong môi trường FastAPI với nhiều worker hoặc thread, kết nối SQLite mặc định sẽ báo lỗi `ProgrammingError: SQLite objects created in a thread can only be used in that same thread`.

**Giải pháp kỹ thuật của VietLawAssist:**
```python
import sqlite3

def get_connection(db_path: str = "data/laws.db") -> sqlite3.Connection:
    conn = sqlite3.connect(
        db_path,
        check_same_thread=False,     # Cho phép truy cập từ nhiều thread an toàn khi đọc
        timeout=10.0                 # Timeout đợi lock (tránh "database is locked")
    )
    # Trả về dữ liệu dạng dictionary thay vì tuple chỉ số
    conn.row_factory = sqlite3.Row
    # Kích hoạt chế độ ghi chép trước (WAL - Write-Ahead Logging) cho hiệu năng cao
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA synchronous = NORMAL;")
    return conn
```

### 2.2 Phòng Chống Tấn Công SQL Injection
Tuyệt đối **KHÔNG** nối chuỗi (`f"SELECT * FROM laws WHERE law_code = '{code}'"`). Luôn sử dụng Parameterized Queries (`?` placeholder):

```python
# CHUẨN AN TOÀN
cursor.execute(
    "SELECT * FROM law_articles WHERE law_code = ? AND article_number = ?",
    (law_code, article_num)
)
```

---

## 3. Pydantic v2: Kiểm Định & Tuần Tự Hóa Dữ Liệu (Validation & Serialization)

VietLawAssist áp dụng **Pydantic v2**, được viết lại hoàn toàn bằng Rust với tốc độ kiểm tra nhanh gấp 5 - 15 lần phiên bản v1.

### 3.1 Khai Báo Model với `Field` & Metadata Tự Sinh
```python
from pydantic import BaseModel, Field, ConfigDict

class SearchRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    query: str = Field(
        ...,
        min_length=2,
        max_length=500,
        description="Câu hỏi hoặc cụm từ tra cứu pháp luật",
        examples=["Độ tuổi kết hôn của nam và nữ"]
    )
    top_k: int = Field(
        default=5,
        ge=1,
        le=50,
        description="Số lượng điều luật liên quan muốn lấy về"
    )
```

### 3.2 Tùy Biến Trình Kiểm Tra (`field_validator`)
Tự động làm sạch văn bản ngay khi dữ liệu được nạp vào schema:
```python
import unicodedata
from pydantic import field_validator

class LawArticleCreate(BaseModel):
    title: str
    content: str

    @field_validator("title", "content", mode="before")
    @classmethod
    def normalize_vietnamese(cls, value: str) -> str:
        if isinstance(value, str):
            # Tự động chuẩn hóa NFC và loại bỏ khoảng trắng thừa
            return unicodedata.normalize("NFC", value).strip()
        return value
```

### 3.3 Chuyển Đổi Dữ Liệu Trong Pydantic v2
- **Chuyển thành Dictionary:** `model.model_dump()` (thay thế `.dict()` của v1).
- **Chuyển thành JSON:** `model.model_dump_json()` (thay thế `.json()` của v1).
- **Khởi tạo từ Dictionary:** `LawArticleCreate.model_validate(raw_dict)` (thay thế `.parse_obj()` của v1).

---

## 4. Tài Liệu Tham Khảo Chính Thức (Official Documentation Links)

1. **FastAPI Documentation:** [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)  
   - Advanced Dependencies: [https://fastapi.tiangolo.com/tutorial/dependencies/](https://fastapi.tiangolo.com/tutorial/dependencies/)
   - Lifespan Events: [https://fastapi.tiangolo.com/advanced/events/](https://fastapi.tiangolo.com/advanced/events/)
2. **Pydantic v2 Documentation & Migration Guide:** [https://docs.pydantic.dev/latest/](https://docs.pydantic.dev/latest/)
3. **Python SQLite3 Standard Library:** [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
4. **Uvicorn ASGI Web Server:** [https://www.uvicorn.org/](https://www.uvicorn.org/)
