# 📊 PROJECT STATUS DASHBOARD — AlgoCore Systems Corp (CORP-07-ALGO)

> **Cập nhật lần cuối**: 2026-09-18 | **Tuần hiện tại**: Tuần 1 (Systems Foundations & Modern C++ Memory Model)  
> **Mentor chuyên trách**: DUT Algorithmic & Systems Mentor (`AGENT_PROFILE.md`)

---

## Current Phase: 🔵 PHASE 1 — LOW-LEVEL MECHANICS & LINEAR STRUCTURES (Tuần 1-4)

Tập trung vào quản lý vùng nhớ Stack vs Heap, Con trỏ & Tham chiếu, Smart Pointers (`unique_ptr`, `shared_ptr`), RAII Idiom và triển khai Cấu trúc Dữ liệu Tuyến tính từ đầu (From Scratch).

---

## Implementation & Lab Progress

### Module 1: Kỹ thuật Lập trình Bậc thấp & Quản trị Bộ nhớ
- [x] Thiết lập Toolchain: GCC 13 / Clang 17, CMake 3.25+, AddressSanitizer (ASan)
- [x] Phân biệt Stack Frame vs Heap Allocation, Memory Alignment & Padding
- [ ] Con trỏ trần (`raw pointer`) vs Smart Pointers (`std::unique_ptr`, `std::shared_ptr`, `std::weak_ptr`)
- [ ] Move Semantics (`std::move`, Rvalue References `&&`) & Quy tắc 5 (Rule of 5)
- [ ] Đo đạc Memory Leak bằng Valgrind & ASan

### Module 2: Cấu trúc Dữ liệu Tuyến tính Tự Cài Đặt (From Scratch)
- [ ] Dynamic Array (Tự cài đặt vector với resizing strategy $\times 2$)
- [ ] Singly & Doubly Linked List an toàn bộ nhớ
- [ ] Circular Buffer & Lock-free Queue cơ bản
- [ ] Stack & Monotonic Stack (Bài toán Next Greater Element)

### Module 3: Cây & Đồ thị Nâng cao
- [ ] Binary Search Tree (BST) & Cây Cân bằng (AVL / Red-Black Tree)
- [ ] Trie (Cây tiền tố) ứng dụng trong Autocomplete & IP Routing Table
- [ ] Thuật toán Đồ thị: BFS, DFS, Dijkstra với `std::priority_queue`

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | Sinh viên có thói quen dùng `new/delete` thủ công kiểu C++98 | 🔴 High | Bắt buộc bật cờ biên dịch `-Werror` và audit bằng linter |

---

## Next Priority (P0)
- Hoàn thiện bài lab kiểm thử quản lý bộ nhớ tuần 1 trong `03_Engineering_Labs_and_Code/`.
- Chuẩn hóa bộ template Catch2 / Google Test để sinh viên làm bài theo phong cách TDD.
