# 📜 ĐIỀU LỆ PHÒNG TƯ LIỆU & PEP STANDARDS (LECTURES & RAW MATERIALS DEPT)
## Phòng 02 — Công Ty Hệ Thống Phân Tán & Backend Python (CORP-11-PY)

> **Mã Phòng Ban:** `PY-DEPT-02`  
> **Trưởng phòng phụ trách:** Agent `EKC-03` (Knowledge Curator & Quality Sentinel)  
> **Tiêu chuẩn học liệu:** ER-QVR $\ge 90/100$ | PEP Standards / Fluent Python 2nd / Architecture Patterns with Python

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Tư Liệu là **thư viện chuẩn mực Pythonic và tài liệu hệ thống phân tán**:
1. **Lưu Trữ & Phân Tích Các PEP Quan Trọng (Python Enhancement Proposals)**: Phân tích sâu PEP 484 (Type Hints), PEP 492 (async/await), PEP 557 (Data Classes), PEP 604 (Union Operators) và PEP 695 (Type Parameter Syntax).
2. **Kho Lưu Trữ Bài Giảng Về CPython Internals**: Lưu trữ tài liệu về GIL, Bộ đếm tham chiếu (Reference Counting), Bộ thu gom rác thế hệ (Generational GC) và Bytecode Disassembly (`dis` module).
3. **Mô Hình Kiến Trúc Phân Tán Mẫu**: Các bản đặc tả thiết kế Microservices, Event-Driven Architecture với Kafka/RabbitMQ và kiến trúc CQRS.

---

## ⚖️ 2. BỘ QUY TẮC BẢO TỒN TƯ LIỆU BẤT BIẾN (CURATION INVARIANTS)

1. **Chuẩn Mực Nguồn Học Liệu (Source Invariant)**:
   - Mọi tư liệu phải có nguồn gốc từ sách Tier A+ trong Knowledge Vault hoặc tài liệu chính thức của Python Software Foundation (docs.python.org).
2. **Quy Tắc Code Tương Thích Python Hiện Đại**:
   - Nghiêm cấm đưa vào tư liệu cú pháp Python 2 hoặc Python cũ trước 3.10 (ví dụ: dùng `typing.List` thay vì `list`, dùng cú pháp cũ thay cho `match-case`).
3. **Quy Tắc Trình Bày Rõ Ràng Cơ Chế Bộ Nhớ**:
   - Mọi ví dụ về Data Model phải có sơ đồ mô tả cách đối tượng được lưu trong Heap và con trỏ PyObject trong CPython.

---

## 🛠️ 3. TOOLCHAIN & QUY TRÌNH SỐ HÓA BÀI GIẢNG

1. **Trực quan hóa Cơ Chế Bộ Nhớ**: Graphviz, Mermaid.js (vẽ cấu trúc PyObject và Reference Graph).
2. **Phân tích Bytecode**: Module `dis`, Python AST explorer.
3. **Định dạng & Kiểm duyệt**: Ruff formatter, Markdown link checker qua `holding_system_auditor.py`.

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
02_Lectures_and_Raw_Materials/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 pep_standards/                        # Các bản phân tích PEP quan trọng
│   ├── pep_492_coroutine_syntax.md         # Phân tích cú pháp async/await
│   └── pep_604_modern_union_types.md       # Cú pháp Union hiện đại với |
├── 📁 cpython_internals/                    # Tài liệu giải phẫu nhân CPython
│   ├── gil_and_multithreading_limits.md    # Bản chất GIL và giới hạn đa luồng
│   └── garbage_collection_deep_dive.md     # Cơ chế thu gom rác thế hệ
└── 📁 distributed_blueprints/               # Bản vẽ kiến trúc hệ thống phân tán
    ├── event_driven_celery_redis.md        # Kiến trúc hàng đợi công việc Celery
    └── async_connection_pooling.md         # Quản lý Connection Pool cho cơ sở dữ liệu
```

---

## 💻 5. MẪU TƯ LIỆU CHỨNG MINH HỌC THUẬT (GOLD MASTER CPYTHON ANALYSIS)

```markdown
# 🔬 GIẢI PHẪU CPYTHON: TẠI SAO DICTIONARY NHANH $O(1)$ VÀ COMPACT TỪ PYTHON 3.6?
> **Nguồn trích:** Fluent Python 2nd ed, Chapter 3 & Raymond Hettinger's Compact Dict Proposal  
> **Người thẩm định:** Agent `EKC-03` | **Điểm ER-QVR:** 96/100

### 1. Vấn đề của Dictionary Cổ Điển (Pre-3.6)
Trước Python 3.6, dict sử dụng mảng sparse entries lớn chứa trực tiếp (hash, key, value), gây lãng phí bộ nhớ tới 33-50% do các ô trống.

### 2. Kiến trúc Compact Dict Hiện Đại
Tách biệt thành 2 mảng:
- `indices`: Mảng số nguyên nhỏ thưa thớt (Sparse Array of int8/int16) lưu chỉ mục.
- `entries`: Mảng đặc (Dense Array) lưu các tuple `(hash, key, value)` theo đúng thứ tự chèn.
$\implies$ Giảm 30-40% bộ nhớ RAM và tự động bảo toàn thứ tự chèn (Insertion Order)!
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU TƯ LIỆU (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: Mọi bài viết về ngôn ngữ đều ghi rõ phiên bản Python áp dụng (tối thiểu Python 3.11+).
- [ ] **DoD-2**: Trích dẫn tài liệu chính xác từ docs.python.org hoặc sách Tier A+.
- [ ] **DoD-3**: Có ví dụ minh họa trực tiếp bằng mã nguồn có thể thực thi độc lập.
- [ ] **DoD-4**: Đạt điểm đánh giá ER-QVR tối thiểu 90/100.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK KHẮC PHỤC SAI LỆCH KIẾN THỨC (CURATION TROUBLESHOOTING RUNBOOK)

Khi phát hiện tư liệu chứa thông tin lỗi thời về CPython hoặc PEP:
1. **Cô lập tư liệu**: Gắn nhãn `⚠️ DEPRECATED SPECIFICATION: Python 3.12+ Update Needed`.
2. **Đối chiếu Release Notes**: Tra cứu Python What's New cho phiên bản tương ứng.
3. **Cập nhật nội dung**: Viết rõ thay đổi cú pháp và cơ chế mới.
4. **Xác nhận**: Đảm bảo toàn bộ code ví dụ chạy thử nghiệm thành công trên Python 3.11+.
