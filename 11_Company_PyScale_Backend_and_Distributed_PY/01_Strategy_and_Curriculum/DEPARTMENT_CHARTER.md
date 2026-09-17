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

## ⚖️ 2. BỘ QUY TẮC SƯ PHẠM BẤT BIẾN (PEDAGOGICAL HARD CONSTRAINTS)

1. **Tuân Thủ Mô Hình 4 Tầng Sư Phạm**:
   - Mọi tuần học bắt buộc phải có: *Tầng 1 (Bản chất CPython/AsyncIO)* $\rightarrow$ *Tầng 2 (Cài đặt FastAPI/SQLAlchemy 2.0)* $\rightarrow$ *Tầng 3 (⚠️ Cảnh báo Blocking Event Loop & N+1 Queries)* $\rightarrow$ *Tầng 4 (Bài lab Microservices)*.
2. **Nguyên Tắc "Bất Đồng Bộ Tuyệt Đối Trong I/O"**:
   - Mọi bài giảng về Backend đều phải giải thích bản chất không đồng bộ của Event Loop, nghiêm cấm trộn lẫn các thư viện blocking vào `async def`.
3. **Quy Tắc Type Hints 100% Theo PEP 484**:
   - Toàn bộ mã nguồn mẫu trong bài giảng bắt buộc phải có đầy đủ Type Annotations và Pydantic v2 schemas.

---

## 🛡️ 3. TIÊU CHÍ NGHIỆM THU GIÁO TRÌNH (DEFINITION OF READY - DoR)

- [ ] **DoR-1**: Khung chương trình bám sát sách Fluent Python 2nd edition và tài liệu chính thức của FastAPI.
- [ ] **DoR-2**: Các bài học về ORM đều chỉ rõ cách dùng `selectinload()` và cảnh báo lỗi N+1 Query.
- [ ] **DoR-3**: Đã có starter repo tích hợp sẵn Docker Compose (FastAPI, Postgres, Redis, Celery) để học viên thực hành.
