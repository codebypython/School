# 📜 ĐIỀU LỆ PHÒNG KỸ THUẬT, MICROSERVICES & ASYNC APIS (ENGINEERING LABS & CODE DEPT)
## Phòng 03 — Công Ty Hệ Thống Phân Tán & Backend Python (CORP-11-PY)

> **Mã Phòng Ban:** `PY-DEPT-03`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (`HM-00`) & Giám Sát Kỹ Thuật (`SMS-02`)  
> **Cố vấn chuyên môn:** DUT PyScale Backend Mentor (`AGENT_PROFILE.md`)  
> **Tiêu chuẩn chất lượng:** Python 3.11+ / AsyncIO Non-blocking / FastAPI & Pydantic v2 / SQLAlchemy 2.0 Async / Celery

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kỹ Thuật & Microservices là **trung tâm thiết kế backend phân tán hiệu năng cao**:
1. **Phát Triển Asynchronous APIs**: Xây dựng các API bất đồng bộ bằng FastAPI có khả năng xử lý hàng chục nghìn kết nối đồng thời (I/O-bound Concurrency).
2. **Quản Trị Cơ Sở Dữ Liệu Bất Đồng Bộ**: Triển khai tầng truy xuất dữ liệu an toàn qua SQLAlchemy 2.0 AsyncSession, quản lý phiên bản schema qua Alembic.
3. **Xử Lý Tác Vụ Ngầm & Phân Tán (Distributed Task Queue)**: Đóng gói các tác vụ nặng (Background Tasks) qua Celery kết hợp Redis Broker và thiết lập chiến lược Caching phân tán.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (AGENT BẮT BUỘC TUÂN THỦ)

1. **Quy Tắc Bất Biến Về AsyncIO Non-blocking**:
   - **CẤM TUYỆT ĐỐI**: Gọi các hàm blocking I/O đồng bộ (`time.sleep()`, `requests.get()`, `urllib`, `open()` file lớn đồng bộ) bên trong hàm bất đồng bộ `async def`.
   - Bắt buộc sử dụng các thư viện bất đồng bộ tương ứng: `asyncio.sleep()`, `httpx.AsyncClient()`, `aiofiles`.
   - Nếu bắt buộc phải gọi hàm blocking bên thứ ba, phải gói qua: `await asyncio.to_thread(blocking_func, *args)`.
2. **Quy Tắc SQLAlchemy 2.0 & Triệt Tiêu Lỗi N+1**:
   - **CẤM TUYỆT ĐỐI**: Sử dụng cú pháp cũ 1.x (`session.query(Model)`). Bắt buộc dùng cú pháp 2.0: `await session.execute(select(Model))`.
   - Mọi câu truy vấn dữ liệu có quan hệ (1-N, N-N) bắt buộc phải chỉ định chiến lược Eager Loading (`selectinload()` hoặc `joinedload()`) để triệt tiêu hoàn toàn lỗi **N+1 Query Problem**.
3. **Quy Tắc Tham Số Mặc Định (Mutable Default Argument Trap)**:
   - **CẤM TUYỆT ĐỐI**: Đặt danh sách hoặc từ điển rỗng làm giá trị mặc định (`def func(items=[])`). Bắt buộc dùng `items: list[str] | None = None`.

---

## 🛠️ 3. SKILLS ROUTE & TOOLCHAIN ĐIỀU HÀNH CHUẨN

```powershell
# 1. Khởi động môi trường ảo và cài đặt dependencies
poetry install --no-root

# 2. Chạy Linter và kiểm tra định dạng qua Ruff
ruff check .
ruff format --check .

# 3. Kiểm tra kiểu tĩnh nghiêm ngặt qua Mypy
mypy src/ --strict

# 4. Tự động sinh file migration CSDL qua Alembic
alembic revision --autogenerate -m "create_users_and_orders_table"
alembic upgrade head

# 5. Chạy bộ kiểm thử bất đồng bộ với Pytest
pytest -v --cov=src --cov-fail-under=85
```

---

## 📁 4. CẤU TRÚC THƯ MỤC VÀ TÀI SẢN NỘI BỘ QUY CHUẨN

```
03_Engineering_Labs_and_Code/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 microservices_template/               # Khung mẫu Microservice FastAPI chuẩn
│   ├── app/
│   │   ├── api/routes/                      # Endpoints phân tầng
│   │   ├── core/config.py                   # Pydantic Settings
│   │   ├── db/session.py                    # AsyncSession Manager
│   │   └── models/                          # SQLAlchemy 2.0 ORM Models
│   ├── alembic/                             # Migration scripts
│   └── tests/                               # Pytest async test suite
├── 📁 labs/                                 # 15 Bài Lab phân kỳ theo tuần
│   ├── Week01_Python_Data_Model/
│   ├── Week03_AsyncIO_Deep_Dive/
│   ├── Week07_FastAPI_SQLAlchemy_Async/
│   └── Week15_Capstone_Distributed_Order/
└── 📁 docker/                               # Cụm Docker Compose phụ trợ (Postgres, Redis)
    └── docker-compose.yml
```

---

## 💻 5. MẪU KHUNG CODE / TEMPLATE CHUẨN NGHIỆP VỤ (GOLD MASTER FASTAPI & ASYNC ORM)

```python
"""
Order Service API Endpoint - Tuân thủ kiến trúc bất đồng bộ FastAPI & SQLAlchemy 2.0
"""
from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

# Định nghĩa Pydantic Schemas (DTO) với Pydantic v2
class OrderItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: UUID
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)

class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    user_id: UUID
    status: str
    items: list[OrderItemResponse]

router = APIRouter(prefix="/api/v1/orders", tags=["Orders"])

@router.get("/{order_id}", response_model=OrderResponse, status_code=status.HTTP_200_OK)
async def get_order_details(
    order_id: UUID,
    db: Annotated[AsyncSession, Depends(get_async_db_session)]
) -> OrderResponse:
    """Truy xuất chi tiết đơn hàng an toàn, triệt tiêu lỗi N+1 qua selectinload."""
    query = (
        select(Order)
        .where(Order.id == order_id)
        .options(selectinload(Order.items)) # Eager load quan hệ items trong 1 câu truy vấn tối ưu
    )
    result = await db.execute(query)
    order = result.scalar_one_or_none()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Đơn hàng với ID '{order_id}' không tồn tại."
        )

    return OrderResponse.model_validate(order)
```

---

## 🛡️ 6. BỘ TIÊU CHÍ NGHIỆM THU CHẤT LƯỢNG (DEFINITION OF DONE - DoD)

- [ ] **DoD-1 (Zero Blocking Calls)**: Không phát hiện bất kỳ hàm I/O blocking nào trong các coroutines `async def`.
- [ ] **DoD-2 (Strict Mypy Typechecked)**: 100% hàm có Type Hints, vượt qua `mypy src/ --strict` với 0 lỗi.
- [ ] **DoD-3 (Alembic Migrations Sạch)**: Mọi thay đổi schema đều có tệp migration Alembic tương ứng có thể rollback (`downgrade -1`) an toàn.
- [ ] **DoD-4 (Test Coverage $\ge 85\%$)**: Bộ test bất đồng bộ chạy qua `pytest-asyncio` đạt độ bao phủ tối thiểu 85%.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK KHẮC PHỤC SỰ CỐ HỆ THỐNG PHÂN TÁN (DISTRIBUTED SYSTEMS RUNBOOK)

Khi phát hiện sự cố nghẽn Event Loop hoặc cạn kiệt Connection Pool CSDL:
1. **Nghẽn Event Loop (Event Loop Starvation)**:
   - Dấu hiệu: Latency của toàn bộ API tăng vọt đột ngột dù CPU không tải cao.
   - Xử lý: Sử dụng `asyncio.get_event_loop().set_debug(True)` để log các callback chiếm giữ luồng quá 100ms. Chuyển tác vụ tính toán nặng sang `ProcessPoolExecutor` hoặc Celery worker.
2. **Cạn kiệt Connection Pool (Pool Exhaustion)**:
   - Dấu hiệu: Báo lỗi `TimeoutError: QueuePool limit of size 5 overflow 10 reached`.
   - Xử lý: Kiểm tra các endpoint không đóng session; bọc session trong `async with async_session() as session:`; tăng `pool_size` và `max_overflow` trong cấu hình engine nếu cần thiết.
