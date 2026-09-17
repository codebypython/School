# 📜 ĐIỀU LỆ PHÒNG KỸ THUẬT, MÃ NGUỒN & TEST SUITES (ENGINEERING LABS & CODE DEPT)
## Phòng 03 — Công Ty Hệ Thống & Giải Thuật Hiệu Năng Cao (CORP-07-ALGO)

> **Mã Phòng Ban:** `ALGO-DEPT-03`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (`HM-00`) & Giám Sát Kỹ Thuật (`SMS-02`)  
> **Cố vấn chuyên môn:** DUT Algorithmic & Systems Mentor (`AGENT_PROFILE.md`)  
> **Tiêu chuẩn chất lượng:** C++20 ISO Standard / Zero Memory Leaks / Modern CMake / TDD Catch2

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kỹ Thuật & Thực Nghiệm là **trung tâm tác chiến mã nguồn** của AlgoCore Systems Corp:
1. **Lưu trữ & Vận hành Mã nguồn C++20**: Phát triển các thư viện cấu trúc dữ liệu tự viết từ đầu (From Scratch), các thuật toán tối ưu hóa theo CLRS và các bài toán lập trình hệ thống.
2. **Thiết kế Bộ Test Tự Động (TDD Harness)**: Xây dựng sẵn các test suites bao phủ toàn diện các trường hợp biên (Edge Cases: mảng rỗng, 1 phần tử, giá trị cực đại, chu trình đồ thị).
3. **Đo đạc Hiệu năng Thực tế (Benchmarking)**: So sánh lý thuyết tiệm cận $O(N)$ với thời gian thực thi chu kỳ CPU, tác động của bộ nhớ đệm Cache Locality.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (AGENT BẮT BUỘC TUÂN THỦ)

Mọi Agent hoặc Kỹ sư khi tạo, sửa, hoặc đánh giá mã nguồn trong phòng ban này **PHẢI TUÂN THỦ 100% CÁC QUY TẮC SAU**:

1. **Chuẩn Ngôn Ngữ**: Bắt buộc sử dụng **C++20** (`-std=c++20`). Tuyệt đối không dùng các cấu trúc cú pháp cũ bị deprecated trong C++11/C++14.
2. **Quy Tắc Quản Trị Bộ Nhớ (Memory Safety)**:
   - **CẤM TUYỆT ĐỐI**: Sử dụng `malloc()`, `free()`, hoặc `new`/`delete` trần trụi (Raw Owning Pointers).
   - **BẮT BUỘC**: Sử dụng Smart Pointers (`std::unique_ptr`, `std::shared_ptr`) kết hợp hàm khởi tạo an toàn `std::make_unique()`, `std::make_shared()`.
   - **RAII Bất Biến**: Mọi tài nguyên hệ thống (con trỏ bộ nhớ, socket, file descriptor, mutex lock) phải được gói trong lớp quản lý vòng đời RAII.
3. **Quy Tắc Cờ Biên Dịch Nghiêm Ngặt (Compiler Flags)**:
   - Mọi bản build kiểm thử bắt buộc phải bật cờ:
     ```bash
     -Wall -Wextra -Wpedantic -Wconversion -Wshadow -Werror
     ```
   - Chế độ kiểm tra an toàn bộ nhớ lúc chạy:
     ```bash
     -fsanitize=address,undefined -fno-omit-frame-pointer -g
     ```
4. **Quy Tắc Không Gian Tên (Namespaces)**:
   - **CẤM TUYỆT ĐỐI**: Viết `using namespace std;` trong các tệp tiêu đề (`.h`, `.hpp`) hoặc ở phạm vi toàn cục (Global Scope).
5. **Quy Tắc Độ Phức Tạp Thuật Toán (Complexity Annotations)**:
   - Mọi hàm giải thuật hoặc phương thức cấu trúc dữ liệu phải có Header Docstring ghi rõ:
     - **Time Complexity**: Trường hợp tốt nhất, trung bình, xấu nhất ($O$, $\Omega$, $\Theta$).
     - **Space Complexity**: Bộ nhớ phụ trợ (Auxiliary Space $O$).

---

## 🛠️ 3. SKILLS ROUTE & TOOLCHAIN ĐIỀU HÀNH CHUẨN

Agent khi nhận lệnh triển khai bài lab tại thư mục này phải sử dụng đúng bộ công cụ và lệnh CLI sau:

### 3.1 Toolchain Yêu Cầu
- **Trình biên dịch**: GCC 13+ / Clang 17+ / MSVC 2022 v19.38+.
- **Hệ thống Build**: CMake $\ge 3.25$.
- **Khung Kiểm thử**: Catch2 v3 hoặc Google Test (gTest).
- **Phân tích Động**: AddressSanitizer (ASan), UndefinedBehaviorSanitizer (UBSan), Valgrind.

### 3.2 Bộ Lệnh CLI Tác Nghiệp Chuẩn

```powershell
# 1. Cấu hình dự án bằng CMake với AddressSanitizer được kích hoạt
cmake -B build -S . -DCMAKE_BUILD_TYPE=Debug -DENABLE_ASAN=ON

# 2. Biên dịch toàn bộ mã nguồn và test suite
cmake --build build --config Debug -j 4

# 3. Chạy toàn bộ Test Suite qua CTest với hiển thị chi tiết
ctest --test-dir build --output-on-failure -V

# 4. Biên dịch độc lập 1 bài lab bằng Clang/GCC kèm ASan (dành cho file đơn lẻ)
clang++ -std=c++20 -Wall -Wextra -Werror -fsanitize=address,undefined -g Lab1_Memory_Layout.cpp -o Lab1_Memory_Layout.exe
./Lab1_Memory_Layout.exe
```

---

## 📁 4. CẤU TRÚC THƯ MỤC VÀ TÀI SẢN NỘI BỘ QUY CHUẨN

```
03_Engineering_Labs_and_Code/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ phòng ban này
├── 📄 CMakeLists.txt                        # Master CMake cấu hình toàn bộ Labs & Tests
├── 📁 cmake/                                # Modules hỗ trợ (Sanitizers.cmake, Warnings.cmake)
├── 📁 include/algocore/                     # Thư viện Headers cấu trúc dữ liệu tự viết (.hpp)
│   ├── memory_arena.hpp                     # Custom Allocator / Arena Memory
│   ├── dynamic_array.hpp                    # Vector tự viết from scratch
│   ├── linked_list.hpp                      # Doubly Linked List an toàn RAII
│   ├── bst_tree.hpp                         # Binary Search Tree & AVL Tree
│   └── graph_engine.hpp                     # Graph Adjacency List & Algorithms
├── 📁 src/                                  # Triển khai mã nguồn chi tiết (.cpp)
├── 📁 labs/                                 # 15 Bài Lab phân kỳ theo tuần học
│   ├── Week01_Memory_And_Pointers/
│   │   ├── README.md                        # Đặc tả yêu cầu bài lab & đề bài
│   │   ├── solution.cpp                     # Mã nguồn giải pháp của học viên
│   │   └── benchmark.cpp                    # Đo lường thời gian thực thi
│   ├── Week02_Smart_Pointers_RAII/
│   ├── Week03_Move_Semantics/
│   └── Week15_Capstone_KVStore/             # Đồ án In-Memory Key-Value Storage Engine
└── 📁 tests/                                # Test suites viết bằng Catch2 / Google Test
    ├── test_dynamic_array.cpp
    ├── test_bst_tree.cpp
    └── test_graph_algorithms.cpp
```

---

## 💻 5. MẪU KHUNG CODE / TEMPLATE CHUẨN NGHIỆP VỤ (GOLD MASTER BOILERPLATE)

Mọi bài lab C++20 khi sinh ra phải tuân thủ cấu trúc mẫu chuẩn mực sau:

```cpp
/**
 * @file safe_dynamic_array.hpp
 * @brief Cấu trúc mảng động tự cài đặt tuân thủ C++20 & an toàn bộ nhớ RAII.
 * @author AlgoCore Systems Engineering Division
 * @complexity Time: PushBack Amortized O(1), Access O(1) | Space: O(N)
 */

#ifndef ALGOCORE_SAFE_DYNAMIC_ARRAY_HPP
#define ALGOCORE_SAFE_DYNAMIC_ARRAY_HPP

#include <memory>
#include <stdexcept>
#include <concepts>
#include <span>
#include <cstddef>

namespace algocore {

template <typename T>
requires std::is_nothrow_destructible_v<T>
class DynamicArray {
private:
    std::size_t m_capacity{0};
    std::size_t m_size{0};
    std::unique_ptr<T[]> m_data{nullptr};

    void reallocate(std::size_t new_capacity) {
        // Cấp phát mảng mới bằng std::make_unique để quản lý bộ nhớ tự động
        auto new_data = std::make_unique<T[]>(new_capacity);
        for (std::size_t i = 0; i < m_size; ++i) {
            new_data[i] = std::move(m_data[i]); // Sử dụng Move Semantics tối ưu hiệu năng
        }
        m_data = std::move(new_data);
        m_capacity = new_capacity;
    }

public:
    DynamicArray() : m_capacity(2), m_size(0), m_data(std::make_unique<T[]>(2)) {}

    // Rule of 5: Đảm bảo quản lý tài nguyên hoàn hảo
    ~DynamicArray() = default;
    DynamicArray(DynamicArray&&) noexcept = default;
    DynamicArray& operator=(DynamicArray&&) noexcept = default;
    DynamicArray(const DynamicArray& other) : m_capacity(other.m_capacity), m_size(other.m_size), m_data(std::make_unique<T[]>(other.m_capacity)) {
        for (std::size_t i = 0; i < m_size; ++i) m_data[i] = other.m_data[i];
    }
    DynamicArray& operator=(const DynamicArray& other) {
        if (this != &other) {
            auto temp = other;
            *this = std::move(temp);
        }
        return *this;
    }

    void push_back(const T& value) {
        if (m_size >= m_capacity) {
            reallocate(m_capacity * 2); // Chiến lược Geometric Resizing x2
        }
        m_data[m_size++] = value;
    }

    [[nodiscard]] const T& at(std::size_t index) const {
        if (index >= m_size) {
            throw std::out_of_range("Index out of range in DynamicArray::at");
        }
        return m_data[index];
    }

    [[nodiscard]] std::size_t size() const noexcept { return m_size; }
    [[nodiscard]] std::size_t capacity() const noexcept { return m_capacity; }
    [[nodiscard]] bool empty() const noexcept { return m_size == 0; }
    
    // View dạng span hiện đại của C++20 không tốn chi phí sao chép
    [[nodiscard]] std::span<const T> as_span() const noexcept {
        return std::span<const T>(m_data.get(), m_size);
    }
};

} // namespace algocore

#endif // ALGOCORE_SAFE_DYNAMIC_ARRAY_HPP
```

---

## 🛡️ 6. BỘ TIÊU CHÍ NGHIỆM THU CHẤT LƯỢNG (DEFINITION OF DONE - DoD)

Một bài lab / module code chỉ được công nhận hoàn thành khi thỏa mãn **6 Tiêu chí Bắt buộc**:
- [ ] **DoD-1 (Biên dịch Không Cảnh báo)**: Biên dịch thành công với `-Wall -Wextra -Werror` trên ít nhất GCC 13 hoặc Clang 17.
- [ ] **DoD-2 (Zero Memory Leaks)**: Chạy toàn bộ test cases qua **AddressSanitizer (`-fsanitize=address`)** xuất ra `0 byte leaked`, không có `heap-use-after-free` hay `heap-buffer-overflow`.
- [ ] **DoD-3 (Test Coverage $\ge 85\%$)**: Có test suite kiểm thử đơn vị bao phủ toàn bộ luồng logic chính và các trường hợp lỗi biên.
- [ ] **DoD-4 (Quy chuẩn C++20)**: Sử dụng Smart Pointers, không tồn tại `new/delete` thủ công trong code nghiệp vụ.
- [ ] **DoD-5 (Docstring & Big-O)**: Có ghi chú rõ ràng Time/Space Complexity cho từng giải thuật.
- [ ] **DoD-6 (Format Chuẩn)**: Đã chạy qua `clang-format -i --style=Google` trước khi hoàn tất.

---

## 🚑 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK KHẨN CẤP

Khi Agent hoặc học viên gặp lỗi trong quá trình thực thi:
1. **Lỗi Segmentation Fault (Crash chương trình)**:
   - *Bước 1*: Bật cờ `-g -fsanitize=address` và chạy lại để ASan chỉ đích danh số dòng và hàm gây lỗi.
   - *Bước 2*: Nếu không có ASan, chạy qua GDB: `gdb ./program` $\rightarrow$ gõ `run` $\rightarrow$ khi crash gõ `bt` (backtrace) để xem call stack.
2. **Lỗi Memory Leak**:
   - Chạy với Valgrind: `valgrind --leak-check=full --show-leak-kinds=all ./program`.
   - Tìm vị trí `definitely lost` hoặc `indirectly lost` để thay bằng Smart Pointers.
3. **Lỗi Undefined Behavior (Toán tử dịch bit, truy xuất ngoài biên)**:
   - Bật cờ `-fsanitize=undefined` để trình biên dịch phát hiện ngay lập tức lúc runtime.
