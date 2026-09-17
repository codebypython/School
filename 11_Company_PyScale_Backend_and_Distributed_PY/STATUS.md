# 📊 PROJECT STATUS DASHBOARD — PyScale Corp (CORP-11-PY)

> **Cập nhật lần cuối**: 2026-09-18 | **Tuần hiện tại**: Tuần 1 (Python Data Model & Dunder Methods)  
> **Mentor chuyên trách**: DUT PyScale Backend Mentor (`AGENT_PROFILE.md`)

---

## Current Phase: 🔵 PHASE 1 — PYTHONIC INTERNALS & DATA MODEL (Tuần 1-6)

Tập trung mổ xẻ cơ chế CPython, Python Data Model (`__dunder__`), Generator, Decorator, Metaclass và làm chủ lập trình đồng thời AsyncIO.

---

## Implementation & Lab Progress

### Module 1: Python Data Model & Kỹ Thuật Nâng Cao
- [x] Thiết lập môi trường Python 3.11+, Poetry / UV, Ruff linter, Pytest
- [x] Python Data Model: Sequence, Mapping & Numeric Protocols (`__getitem__`, `__len__`, `__repr__`)
- [ ] Iterators, Generators, `yield from` & Memory-Efficient Streaming
- [ ] Decorators tham số hóa, Closures trong Python, `functools.wraps`
- [ ] Type Hints PEP 484, Pydantic v2 validation & Mypy Strict Mode

### Module 2: Lập Trình Bất Đồng Bộ (AsyncIO Deep Dive)
- [ ] CPython GIL (Global Interpreter Lock): Khi nào dùng Multithreading, Multiprocessing, AsyncIO
- [ ] AsyncIO Event Loop, Coroutines, Tasks, `asyncio.gather`, `asyncio.TaskGroup` (Python 3.11)
- [ ] Xử lý I/O bất đồng bộ: HTTP requests với `httpx` / `aiohttp`

### Module 3: Enterprise FastAPI & Distributed Architecture
- [ ] FastAPI Dependency Injection & Async Route Handlers
- [ ] SQLAlchemy 2.0 Async ORM & Alembic Database Migrations
- [ ] Distributed Task Queue: Celery Workers + Redis Broker & Caching

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | Sinh viên gọi hàm đồng bộ blocking (`time.sleep` hoặc `requests.get`) bên trong `async def` | 🔴 High | Bắt buộc kiểm tra linter phát hiện blocking calls trong async context |

---

## Next Priority (P0)
- Tạo starter repo bài tập Python Data Model và AsyncIO Web Crawler trong `03_Engineering_Labs_and_Code/`.
