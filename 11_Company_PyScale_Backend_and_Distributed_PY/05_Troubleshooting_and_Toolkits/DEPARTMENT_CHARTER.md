# 📜 ĐIỀU LỆ PHÒNG KIỂM SOÁT LỖI ASYNCIO & HIỆU NĂNG BACKEND (TROUBLESHOOTING & TOOLKITS DEPT)
## Phòng 05 — Công Ty Hệ Thống Phân Tán & Backend Python (CORP-11-PY)

> **Mã Phòng Ban:** `PY-DEPT-05`  
> **Trưởng phòng phụ trách:** Agent `SMS-02` (Syllabus Sentinel & Technical Auditor)  
> **Thẩm quyền kỹ thuật:** Chẩn đoán lỗi Event Loop Blocked, Điều tra truy vấn chậm N+1 ORM, Cứu hộ hàng đợi Celery & Redis  
> **Bộ công cụ cốt lõi:** `yappi` (AsyncIO Profiler) / `py-spy` / SQLAlchemy Query Echo / Redis CLI & Locust Load Testing

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kiểm Soát Sự Cố Python Backend là **"Trung tâm Cứu hộ và Tối ưu hóa Hệ thống Phân tán"**:
1. **Chẩn Đoán Nghẽn Event Loop Trong FastAPI/AsyncIO**: Cô lập các lời gọi hàm blocking hoặc tác vụ CPU-bound vô tình đặt trong hàm `async def` làm đứng toàn bộ server.
2. **Triệt Tiêu Lỗi Truy Vấn CSDL N+1 Trong SQLAlchemy 2.0**: Bật log truy vấn SQL và công cụ đo đạc để phát hiện các mối quan hệ nạp lười biếng (Lazy Loading) làm bùng nổ số lượng truy vấn xuống PostgreSQL.
3. **Cứu Hộ Hàng Đợi Phân Tán Celery & Redis**: Xử lý tình trạng nghẽn hàng đợi (Queue Backlog), tác vụ bị crash không thể retry (Task Poisoning) và rò rỉ bộ nhớ trong Redis.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN (DEBUGGING INVARIANTS)

1. **Nguyên Tắc Dữ Liệu Thực Nghiệm (Metric-Driven Diagnostics)**:
   - Nghiêm cấm phỏng đoán nguyên nhân nghẽn mà không có số liệu CPU, Memory profile hoặc log query execution time.
2. **Nguyên Tắc Không Tắt Debug Chế Độ Mù**:
   - Khi gặp lỗi `RuntimeWarning: coroutine was never awaited`, bắt buộc phải truy tìm tận gốc nguồn gọi thay vì bỏ qua cảnh báo bằng `filterwarnings`.
3. **Nguyên Tắc Cô Lập Môi Trường (Sandbox Reproduction)**:
   - Sự cố đa tiến trình hoặc hàng đợi phân tán phải được tái lập trong môi trường Docker tách biệt trước khi can thiệp vào mã nguồn.

---

## 🛠️ 3. TOOLCHAIN & SKILLS ROUTE CHẨN ĐOÁN BACKEND

| Sự Cố / Nhu Cầu | Công Cụ Chẩn Đoán | Cú Pháp Thực Thi CLI |
| :--- | :--- | :--- |
| **Nghẽn Event Loop** | AsyncIO Debug Mode / `py-spy` | `PYTHONASYNCIODEBUG=1 uvicorn ...` / `py-spy top --pid <PID>` |
| **N+1 Queries CSDL** | SQLAlchemy Query Echo / SQLTap | `create_async_engine(..., echo=True)` |
| **Tắc nghẽn Celery Queue** | Celery Inspect / Flower Web UI | `celery -A src.workers.celery_app inspect active` |
| **Kiểm thử tải đồng thời** | Locust / wrk | `locust -f load_tests/locustfile.py --headless -u 1000 -r 50` |

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
05_Troubleshooting_and_Toolkits/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 diagnostic_scripts/                   # Kịch bản chẩn đoán tự động
│   ├── check_blocking_calls.py             # Script quét AST tìm lời gọi sync trong async
│   └── inspect_celery_queues.sh            # Script kiểm tra hàng đợi Redis
└── 📁 runbooks/                             # Cẩm nang xử lý sự cố chi tiết
    ├── event_loop_starvation_runbook.md
    └── sqlalchemy_n_plus_one_remediation.md
```

---

## 💻 5. MẪU KHUNG CODE CHẨN ĐOÁN & PROFILING (BOILERPLATE TOOLKIT)

```python
# Middleware chẩn đoán: Tự động đo thời gian xử lý và log các truy vấn chậm
import time
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class PerformanceMonitorMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next) -> Response:
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = f"{process_time:.4f}s"

        if process_time > 0.5:  # Cảnh báo nếu request vượt quá 500ms
            print(
                f"[PERF ALERT] Endpoint {request.url.path} chậm: {process_time:.4f}s"
            )

        return response
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU CHẨN ĐOÁN (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: Phát hiện và xử lý triệt để nguyên nhân gốc rễ (Root Cause Identified).
- [ ] **DoD-2**: Tái lập được lỗi bằng test case kiểm thử tải hoặc test case đơn vị.
- [ ] **DoD-3**: Không còn log cảnh báo `RuntimeWarning` hay `Slow callback` trong terminal.
- [ ] **DoD-4**: Latency P99 của endpoint được cải thiện tối thiểu 50% sau khi sửa.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & CẨM NANG KHẮC PHỤC (TOP 4 RUNBOOKS)

### 🚨 RUNBOOK 1: PHÁT HIỆN HÀM BLOCKING TRONG ASYNCIO BẰNG ASYNCIO DEBUG MODE
* **Triệu chứng**: FastAPI server xử lý các request khác cực kỳ chậm khi có một user gọi vào một endpoint nhất định.
* **Quy trình kích hoạt phát hiện tự động**:
  - Khởi động Uvicorn với biến môi trường debug của AsyncIO:
    ```bash
    PYTHONASYNCIODEBUG=1 uvicorn src.main:app --reload
    ```
  - Hoặc cấu hình trong code:
    ```python
    import asyncio

    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = (
        0.05  # Cảnh báo nếu bất kỳ callback nào chiếm Event Loop > 50ms
    )
```
  - Quan sát log Terminal: Nếu có hàm blocking, AsyncIO sẽ lập tức in ra cảnh báo: `Executing <Handle ...> took 0.450 seconds!` kèm tên file và số dòng gây nghẽn.

---

### 🚨 RUNBOOK 2: PHÁT HIỆN VÀ TRIỆT TIÊU LỖI N+1 QUERIES TRONG SQLALCHEMY 2.0
* **Triệu chứng**: Thời gian phản hồi API danh sách đơn hàng tăng vọt từ 20ms lên 1,500ms khi số lượng đơn hàng tăng lên.
* **Quy trình điều tra**:
  1. *Bước 1 - Bật Engine Echo*:
     ```python
     engine = create_async_engine("postgresql+asyncpg://...", echo=True)
     ```
  2. *Bước 2 - Quan sát log SQL*: Nếu thấy hàng trăm câu lệnh `SELECT ... FROM order_items WHERE order_id = ?` chạy liên tiếp, lỗi N+1 đã xảy ra!
  3. *Bước 3 - Khắc phục bằng Eager Loading*:
     ```python
     # Thay thế câu truy vấn thường bằng selectinload:
     stmt = select(Order).options(selectinload(Order.items)).where(...)
     ```

---

### 🚨 RUNBOOK 3: XỬ LÝ LỖI "COROUTINE WAS NEVER AWAITED"
* **Triệu chứng**: Hàm chạy nhưng không sinh ra kết quả, terminal cảnh báo: `RuntimeWarning: coroutine 'send_notification' was never awaited`.
* **Nguyên nhân**: Gọi hàm `async def` mà quên viết từ khóa `await` phía trước.
* **Khắc phục**:
  - Tìm vị trí gọi hàm và bổ sung `await`:
    ```python
    # SAI: send_notification(user_id)
    # ĐÚNG:
    await send_notification(user_id)
    ```

---

### 🚨 RUNBOOK 4: XỬ LÝ HÀNG ĐỢI CELERY BỊ NGHẼN (TASK TIMEOUT & PURGE)
* **Triệu chứng**: Tác vụ Celery bị tồn đọng hàng nghìn jobs trong Redis, worker không chịu nhận thêm việc mới.
* **Quy trình cứu hộ bằng Celery CLI**:
  ```bash
  # 1. Kiểm tra trạng thái và số lượng worker đang hoạt động
  celery -A src.workers.celery_app status

  # 2. Xem danh sách các tác vụ đang chạy (active tasks)
  celery -A src.workers.celery_app inspect active

  # 3. Trong trường hợp khẩn cấp, xóa sạch hàng đợi bị kẹt (Purge Queue)
  celery -A src.workers.celery_app purge -f
  ```
