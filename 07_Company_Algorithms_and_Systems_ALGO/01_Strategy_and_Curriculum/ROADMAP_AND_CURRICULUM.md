# 🧭 KHUNG GIÁO TRÌNH 15 TUẦN CHUẨN: C++20, THUẬT TOÁN & LẬP TRÌNH HỆ THỐNG
## AlgoCore Systems Corp — Mã môn học: `ALGO-DUT`

> **Đơn vị bảo trợ học thuật:** Khoa Công nghệ Thông tin, Đại học Bách khoa – ĐH Đà Nẵng (DUT)  
> **Tài liệu tham chiếu Tier A+:** CLRS (4th ed, 2022), The Algorithm Design Manual (Skiena 2020), A Tour of C++ (Stroustrup C++20), CS:APP (Bryant & O'Hallaron)  
> **Phương pháp sư phạm:** 4 Tầng Sư Phạm (Lý thuyết kinh điển $\rightarrow$ Cú pháp C++20 hiện đại $\rightarrow$ Bẫy lỗi thời $\rightarrow$ Thực hành Lab TDD)

---

## 📅 PHÂN KỲ LỘ TRÌNH 15 TUẦN

```mermaid
graph TD
    P1["GIAI ĐOẠN 1: QUẢN TRỊ BỘ NHỚ & MODERN C++20 (Tuần 1 - 3)"]
    P2["GIAI ĐOẠN 2: CẤU TRÚC DỮ LIỆU TỪ GỐC RỄ (Tuần 4 - 7)"]
    P3["GIAI ĐOẠN 3: GIẢI THUẬT ĐỒ THỊ & QUY HOẠCH ĐỘNG (Tuần 8 - 11)"]
    P4["GIAI ĐOẠN 4: HIỆU NĂNG PHẦN CỨNG & ĐA LUỒNG (Tuần 12 - 14)"]
    P5["GIAI ĐOẠN 5: CAPSTONE PROJECT IN-MEMORY KV STORE (Tuần 15)"]

    P1 --> P2 --> P3 --> P4 --> P5
```

---

### 🔷 GIAI ĐOẠN 1: QUẢN TRỊ BỘ NHỚ & MODERN C++20 (TUẦN 1 - 3)

#### Tuần 1: Kiến Trúc Bộ Nhớ Máy Tính & Con Trỏ (Memory Layout & Pointer Mechanics)
- **Tầng 1 (Lý thuyết kinh điển - CS:APP Ch.1 & 3)**:
  - Cấu trúc không gian địa chỉ tiến trình (Virtual Address Space): Text, Data, BSS, Heap, Stack.
  - Bản chất biến con trỏ: Kích thước địa chỉ (64-bit = 8 bytes), toán tử dereference `*`, toán tử lấy địa chỉ `&`.
  - Con trỏ số học (Pointer Arithmetic), Mảng 1 chiều và Mối liên hệ với con trỏ.
- **Tầng 2 (Cú pháp hiện đại C++20)**:
  - Sử dụng `std::byte`, `std::span` và `std::string_view` thay vì con trỏ chuỗi kiểu C (`char*`).
  - Phân bổ bộ nhớ động an toàn và kiểm tra cấp phát thất bại.
- **Tầng 3 (⚠️ Bẫy lỗi thời & Anti-patterns)**:
  - Cảnh báo: Sử dụng `malloc`/`free` trong C++ làm bỏ qua Constructor và Destructor.
  - Cảnh báo: Trả về địa chỉ của một biến cục bộ trên Stack (Dangling Pointer trap).
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 1.1`: Viết chương trình in địa chỉ bộ nhớ và kích thước của các biến trên Stack vs Heap để vẽ sơ đồ bộ nhớ tiến trình.
  - Bật cờ AddressSanitizer: `g++ -std=c++20 -fsanitize=address -g lab1.cpp`.

#### Tuần 2: Quản Lý Vòng Đời Tài Nguyên (RAII) & Smart Pointers
- **Tầng 1 (Lý thuyết kinh điển - Stroustrup)**:
  - Triết lý RAII (Resource Acquisition Is Initialization): Ràng buộc vòng đời của tài nguyên với vòng đời của đối tượng.
  - Quyền sở hữu (Ownership semantics): Quyền sở hữu duy nhất (Exclusive) vs Chia sẻ (Shared).
- **Tầng 2 (Cú pháp hiện đại C++20)**:
  - `std::unique_ptr<T>` với `std::make_unique<T>()`.
  - `std::shared_ptr<T>` với `std::make_shared<T>()` và cơ chế Reference Counting.
  - `std::weak_ptr<T>` để phá vỡ chu trình tham chiếu vòng (Circular Reference).
- **Tầng 3 (⚠️ Bẫy lỗi thời)**:
  - Không bao giờ dùng `std::auto_ptr` (đã bị xóa bỏ khỏi chuẩn C++17).
  - Không khởi tạo `std::shared_ptr` bằng con trỏ thô 2 lần gây ra Double Free.
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 1.2`: Cài đặt một lớp quản lý File Descriptor tự động đóng file khi ra khỏi scope bằng RAII và Smart Pointers.

#### Tuần 3: Move Semantics, Rvalue References & Rule of 5
- **Tầng 1 (Lý thuyết)**:
  - Lvalue (đối tượng có tên, có địa chỉ) vs Rvalue (giá trị tạm thời).
  - Chi phí sao chép dữ liệu sâu (Deep Copy) và giải pháp chuyển giao quyền sở hữu (Move).
- **Tầng 2 (Cú pháp C++20)**:
  - Rvalue References (`T&&`), `std::move` và `std::forward`.
  - Quy tắc 5 (Rule of 5): Destructor, Copy Constructor, Copy Assignment, Move Constructor, Move Assignment.
- **Tầng 3 (⚠️ Bẫy lỗi thời)**:
  - Sử dụng đối tượng sau khi đã `std::move` (Use-after-move bug).
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 1.3`: Xây dựng lớp `DynamicBuffer` hỗ trợ Move Semantics hoàn chỉnh, đo đạc tốc độ so sánh giữa Deep Copy vs Move khi truyền $10^7$ phần tử.

---

### 🔷 GIAI ĐOẠN 2: CẤU TRÚC DỮ LIỆU TỰ CÀI ĐẶT TỪ GỐC RỄ (TUẦN 4 - 7)

#### Tuần 4: Mảng Động & Danh Sách Liên Kết An Toàn Bộ Nhớ
- **Tầng 1 (CLRS Ch.10)**:
  - Dynamic Array: Chiến lược tái cấp phát bộ nhớ (Geometric resizing $\times 2$), phân tích chi phí khấu hao (Amortized Analysis $O(1)$).
  - Singly Linked List vs Doubly Linked List: Thêm, xóa nút tại đầu/cuối/vị trí bất kỳ.
- **Tầng 2 (C++20)**:
  - Tự cài đặt `CustomVector<T>` template với bộ cấp phát (Custom Allocator cơ bản).
  - Cài đặt `DoublyLinkedList<T>` sử dụng `std::unique_ptr` hoặc raw pointers có destructor giải phóng triệt để.
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 2.1`: Viết bộ kiểm thử tự động Catch2 chứng minh `CustomVector` không rò rỉ bộ nhớ qua 100,000 lần thêm xóa.

#### Tuần 5: Hàng Đợi (Queue), Ngăn Xếp (Stack) & Monotonic Stack
- **Tầng 1 (CLRS Ch.10 & Skiena Ch.3)**:
  - Ngăn xếp (LIFO), Hàng đợi (FIFO), Hàng đợi vòng (Circular Queue/Buffer).
  - Kỹ thuật Monotonic Stack & Monotonic Queue: Tối ưu bài toán cửa sổ trượt (Sliding Window Maximum) từ $O(N \cdot K)$ xuống $O(N)$.
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 2.2`: Giải bài toán *Daily Temperatures* và *Largest Rectangle in Histogram* sử dụng Monotonic Stack $O(N)$.

#### Tuần 6: Cây Nhị Phân Tìm Kiếm (BST) & Hàng Đợi Ưu Tiên (Binary Heap)
- **Tầng 1 (CLRS Ch.6 & 12)**:
  - Min Heap & Max Heap: Thuật toán `Heapify` ($O(N)$) vs Thêm từng phần tử ($O(N \log N)$).
  - Binary Search Tree: Tính chất BST, Duyệt In-order, Pre-order, Post-order, Xóa nút có 2 con.
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 2.3`: Tự xây dựng `PriorityQueue<T, Compare>` tương thích giao diện `std::priority_queue`.

#### Tuần 7: Cây Cân Bằng (AVL / Red-Black Tree) & Trie (Cây Tiền Tố)
- **Tầng 1 (CLRS Ch.13 & Skiena Ch.3)**:
  - Vấn đề suy biến của BST thành danh sách liên kết $O(N)$.
  - Phép xoay cây (Left Rotate, Right Rotate) và điều kiện cân bằng cây AVL/Red-Black Tree.
  - Cấu trúc Trie: Tìm kiếm từ khóa theo tiền tố trong thời gian $O(L)$ với $L$ là độ dài từ.
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 2.4`: Cài đặt Trie Engine hỗ trợ chức năng gợi ý tìm kiếm (Autocomplete) và tìm kiếm ký tự đại diện (Wildcard search).

---

### 🔷 GIAI ĐOẠN 3: GIẢI THUẬT ĐỒ THỊ & QUY HOẠCH ĐỘNG (TUẦN 8 - 11)

#### Tuần 8: Biểu Diễn Đồ Thị & Duyệt Đồ Thị (BFS / DFS)
- **Tầng 1 (CLRS Ch.22)**:
  - Ma trận kề (Adjacency Matrix) vs Danh sách kề (Adjacency List): So sánh bộ nhớ và thời gian truy vấn.
  - Breadth-First Search (BFS): Tìm đường đi ngắn nhất trên đồ thị không trọng số.
  - Depth-First Search (DFS): Phát hiện chu trình, Sắp xếp tô-pô (Topological Sort).
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 3.1`: Giải bài toán lập lịch tiến trình phụ thuộc (Course Schedule / Build Dependency Graph) bằng Topological Sort.

#### Tuần 9: Đường Đi Ngắn Nhất & Cây Khung Nhỏ Nhất (Shortest Paths & MST)
- **Tầng 1 (CLRS Ch.23 & 24)**:
  - Dijkstra Algorithm: Sử dụng Min-Heap, độ phức tạp $O((V + E) \log V)$.
  - Bellman-Ford: Xử lý cạnh trọng số âm, phát hiện chu trình âm.
  - Cây khung nhỏ nhất (MST): Thuật toán Kruskal với Disjoint Set Union (DSU / Union-Find).
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 3.2`: Mô phỏng thuật toán dẫn đường mạng (OSPF Routing Simulation) tính toán bảng định tuyến ngắn nhất qua Dijkstra.

#### Tuần 10: Quy Hoạch Động 1D & 2D (Dynamic Programming Foundations)
- **Tầng 1 (CLRS Ch.15 & Skiena Ch.8)**:
  - Bản chất DP: Bài toán con gối nhau (Overlapping Subproblems) và Cấu trúc con tối ưu (Optimal Substructure).
  - Top-down (Đệ quy có nhớ - Memoization) vs Bottom-up (Bảng phương án - Tabulation).
  - Bài toán kinh điển: Longest Common Subsequence (LCS), 0/1 Knapsack, Coin Change.
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 3.3`: Tối ưu hóa không gian bộ nhớ của bài toán Knapsack từ ma trận $O(N \times W)$ về mảng 1 chiều $O(W)$.

#### Tuần 11: Quy Hoạch Động Nâng Cao & Bitmask DP
- **Tầng 1 (CLRS & Competitive Programming)**:
  - Bitwise operations: `&`, `|`, `^`, `~`, `<<`, `>>`.
  - Sử dụng số nguyên làm tập hợp trạng thái (Bitmasking).
  - Bài toán Người du lịch (Traveling Salesperson Problem - TSP) từ $O(N!)$ xuống $O(N^2 \cdot 2^N)$.
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 3.4`: Cài đặt thuật toán giải bài toán phân công công việc tối ưu với Bitmask DP.

---

### 🔷 GIAI ĐOẠN 4: HIỆU NĂNG PHẦN CỨNG & ĐA LUỒNG HỆ THỐNG (TUẦN 12 - 14)

#### Tuần 12: Kiến Trúc Bộ Nhớ Cache & Cache Locality
- **Tầng 1 (CS:APP Ch.6)**:
  - Hệ thống phân cấp bộ nhớ (Memory Hierarchy): Registers, L1, L2, L3 Cache, RAM, SSD.
  - Cache Line (thường là 64 bytes), Cache Hit vs Cache Miss.
  - Spatial Locality (Tính cục bộ không gian) vs Temporal Locality (Tính cục bộ thời gian).
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 4.1`: Viết benchmark đo đạc thời gian nhân 2 ma trận lớn $N \times N$: Phương pháp ngây thơ (Duyệt theo cột) vs Phương pháp Tiling / Blocked Matrix Multiplication (Tối ưu hóa Cache).

#### Tuần 13: C++ Concurrency: Luồng, Khóa & Điều Kiện Tranh Chấp (Race Condition)
- **Tầng 1 (CS:APP Ch.12 & Stroustrup Ch.15)**:
  - Quá trình chuyển đổi ngữ cảnh (Context Switching), Phân biệt Process vs Thread.
  - Hiện tượng Data Race và Critical Section.
- **Tầng 2 (C++20)**:
  - `std::thread`, `std::jthread` (C++20 tự động join khi hủy).
  - `std::mutex`, `std::lock_guard`, `std::unique_lock`.
  - Tránh Deadlock bằng `std::scoped_lock` (khóa nhiều mutex cùng lúc theo thứ tự an toàn).
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 4.2`: Xây dựng một Thread-Safe Queue đa luồng sử dụng `std::mutex` và `std::condition_variable`.

#### Tuần 14: Atomic Operations & Mô Hình Bộ Nhớ (Memory Model)
- **Tầng 1 (CS:APP & C++ Standard)**:
  - Khái niệm tính nguyên tử (Atomicity).
  - Hướng dẫn cơ bản về `std::atomic<T>`, các thao tác Compare-and-Swap (CAS).
  - Hiện tượng False Sharing giữa các luồng trên cùng một Cache Line và cách dùng `alignas(64)`.
- **Tầng 4 (Lab Thực hành)**:
  - `Lab 4.3`: Xây dựng bộ đếm hiệu năng cao Atomic Counter không dính False Sharing, đo tốc độ so với Mutex thông thường.

---

### 🔷 GIAI ĐOẠN 5: ĐỒ ÁN CAPSTONE TỐT NGHIỆP HỌC PHẦN (TUẦN 15)

#### Tuần 15: Capstone Project — In-Memory Key-Value Storage Engine
- **Mô tả bài toán**:
  - Xây dựng một Mini In-Memory Database (tương tự Redis core) bằng **C++20** thuần túy.
- **Yêu cầu kỹ thuật khắt khe**:
  1. Sử dụng Custom Hash Table hoặc SkipList / Radix Tree tự cài đặt.
  2. Quản lý bộ nhớ hoàn toàn bằng RAII và Smart Pointers (AddressSanitizer trả về 0 leaks).
  3. Hỗ trợ đa luồng an toàn (Thread-safe Concurrent Reads & Synchronized Writes).
  4. Bộ kiểm thử đơn vị tự động viết bằng Catch2 hoặc Google Test đạt độ bao phủ (Coverage) $\ge 90\%$.
- **Đánh giá & Nghiệm thu (DoD)**:
  - Chạy benchmark đạt tối thiểu 100,000 QPS (Queries Per Second) trên máy tính cá nhân.
