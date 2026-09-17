# 📜 ĐIỀU LỆ PHÒNG CHIẾN LƯỢC & LỘ TRÌNH ĐÀO TẠO (STRATEGY & CURRICULUM DEPT)
## Phòng 01 — Công Ty Hệ Thống Phân Tán & Backend Python (CORP-11-PY)

> **Mã Phòng Ban:** `PY-DEPT-01`  
> **Trưởng phòng phụ trách:** Agent `PSD-04` (Pedagogical Scaffolding Designer) & `ACD-01` (Academic Curriculum Director)  
> **Tiêu chuẩn học thuật:** Fluent Python 2nd ed (Ramalho) / Robust Python (Viafore) / FastAPI / SQLAlchemy 2.0 / Celery

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Chiến Lược & Lộ Trình là **bộ não định hình kiến trúc Backend Python phân tán**:
1. **Thiết Kế Khung Chương Trình 15 Tuần Chuẩn**: Dẫn dắt học viên từ CPython Data Model & Generators $\rightarrow$ Concurrency & AsyncIO Deep Dive $\rightarrow$ FastAPI Asynchronous API $\rightarrow$ SQLAlchemy 2.0 Async $\rightarrow$ Distributed Task Queue Celery & Redis $\rightarrow$ Microservices Capstone.
2. **Loại Bỏ Tư Duy "Python Là Ngôn Ngữ Script Đơn Giản"**: Đào tạo sinh viên thành Kỹ sư Backend chuyên nghiệp, nắm vững cơ chế quản lý bộ nhớ của CPython, cơ chế giải phóng tài nguyên của Async Context Managers và kỹ thuật xử lý hàng chục nghìn kết nối đồng thời.
3. **Chuẩn Hóa Bộ Công Cụ Pythonic Hiện Đại**: Sử dụng `poetry` / `uv` cho quản lý dependencies, `ruff` cho linting siêu tốc, `mypy` cho static type check và `pytest` cho kiểm thử tự động.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (PEDAGOGICAL INVARIANTS)

1. **Tuân Thủ Mô Hình 4 Tầng Sư Phạm**:
   - Mọi tuần học bắt buộc phải có: *Tầng 1 (Bản chất CPython/AsyncIO)* $\rightarrow$ *Tầng 2 (Cài đặt FastAPI/SQLAlchemy 2.0)* $\rightarrow$ *Tầng 3 (⚠️ Cảnh báo Blocking Event Loop & N+1 Queries)* $\rightarrow$ *Tầng 4 (Bài lab Microservices)*.
2. **Nguyên Tắc "Bất Đồng Bộ Tuyệt Đối Trong I/O"**:
   - Mọi bài giảng về Backend đều phải giải thích bản chất không đồng bộ của Event Loop, nghiêm cấm trộn lẫn các thư viện blocking vào `async def`.
3. **Quy Tắc Type Hints 100% Theo PEP 484**:
   - Toàn bộ mã nguồn mẫu trong bài giảng bắt buộc phải có đầy đủ Type Annotations và Pydantic v2 schemas.

---

## 🛠️ 3. TOOLCHAIN & SKILLS ROUTE ĐÀO TẠO BACKEND

| Hạng Mục | Công Cụ & Thước Đo | Mục Đích Sư Phạm |
| :--- | :--- | :--- |
| **Quản trị Dependencies** | Poetry, UV | Quản lý lockfile xác định (Deterministic Lockfile) |
| **Kiểm tra Tĩnh & Linter** | Ruff, Mypy Strict | Loại bỏ lỗi cú pháp và cưỡng chế kiểm tra kiểu tĩnh |
| **Khung Kiểm thử Bất đồng bộ** | Pytest, Pytest-Asyncio, HTTPX | Kiểm thử tích hợp Async API và database mock |
| **Môi trường Phân tán** | Docker Compose, LocalStack, Redis CLI | Khởi chạy cụm Microservices, Task Worker, Database |

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
01_Strategy_and_Curriculum/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 AGENT_PROFILE.md                      # Hồ sơ năng lực Mentor AI PyScale Backend
├── 📄 ROADMAP_AND_CURRICULUM.md             # Giáo trình Master 15 tuần Python Backend
├── 📁 rubrics/                              # Thang điểm đánh giá đồ án
│   └── microservices_capstone_rubric.md    # Tiêu chí chấm đồ án phân tán & async API
└── 📁 exam_blueprints/                      # Đề cương kiểm tra định kỳ
    ├── midterm_async_blueprint.md          # Đề thi giữa kỳ: AsyncIO & CPython Internals
    └── final_distributed_blueprint.md      # Đề thi cuối kỳ: FastAPI, Celery & Microservices
```

---

## 💻 5. MẪU THIẾT KẾ BÀI HỌC 4 TẦNG QUY CHUẨN (GOLD MASTER SYLLABUS UNIT)

```markdown
### Tuần X: [Tên Module Backend Phân Tán]
- **Tầng 1 (Bản chất hệ thống & Why? - Nguồn: Fluent Python Ch.X)**:
  - Cơ chế hoạt động của Single-Threaded Event Loop, Macrotask/Microtask, Coroutines.
  - Sự khác biệt về tài nguyên CPU và RAM giữa Threading vs Multiprocessing vs AsyncIO.
- **Tầng 2 (Cài đặt FastAPI & SQLAlchemy 2.0 Async)**:
  - Code mẫu bất đồng bộ chuẩn mực, xử lý kết nối connection pool và transaction.
- **Tầng 3 (⚠️ Cảnh báo bẫy hiệu năng & Anti-patterns)**:
  - Bẫy Blocking Event Loop do gọi hàm đồng bộ trong route handler async.
  - Bẫy rò rỉ kết nối Database do không dùng Async Context Manager (`async with`).
- **Tầng 4 (Bài tập Lab & Tiêu chí DoD)**:
  - Đề bài: Triển khai endpoint xử lý 10,000 concurrent requests qua `locust` không timeout.
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU GIÁO TRÌNH (DEFINITION OF READY - DoR)

- [ ] **DoR-1**: Khung chương trình bám sát sách Fluent Python 2nd edition và tài liệu chính thức của FastAPI.
- [ ] **DoR-2**: Các bài học về ORM đều chỉ rõ cách dùng `selectinload()` và cảnh báo lỗi N+1 Query.
- [ ] **DoR-3**: Đã có starter repo tích hợp sẵn Docker Compose (FastAPI, Postgres, Redis, Celery) để học viên thực hành.
- [ ] **DoR-4**: Toàn bộ code mẫu đã vượt qua `mypy --strict` và `ruff check`.
- [ ] **DoR-5**: Có câu hỏi phản biện Socratic Dialogue kiểm tra kiến thức về GIL (Global Interpreter Lock).

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK GIÁM ĐỊNH LỘ TRÌNH (CURRICULUM TROUBLESHOOTING RUNBOOK)

Khi phát hiện bài giảng chứa code blocking hoặc giáo trình gây quá tải nhận thức:
1. **Phát hiện (Detection)**: Sinh viên hoặc Agent Audit phát hiện hàm `requests.get()` hoặc `time.sleep()` trong coroutine bài giảng.
2. **Đình chỉ module (Quarantine)**: Gắn nhãn `⚠️ EVENT LOOP HAZARD` tại `STATUS.md`.
3. **Hiệu chỉnh khẩn cấp**: Thay thế bằng `httpx.AsyncClient` hoặc `asyncio.sleep()`, bổ sung giải thích về nghẽn luồng.
4. **Kiểm chứng tải**: Chạy benchmark với công cụ `wrk` hoặc `locust` để xác nhận Event Loop không bị block.
