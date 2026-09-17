# 🧪 Lab 1.1 — Kiến Trúc Bộ Nhớ & Con Trỏ (Memory Layout & Pointer Mechanics)
## AlgoCore Systems Corp | CORP-07-ALGO | Tuần 1

> **Tài liệu tham chiếu:** CS:APP 3rd ed — Chapter 3 (Machine-Level Representation of Programs)  
> **Chuẩn biên dịch:** C++20 với AddressSanitizer bắt buộc  
> **Thời gian ước tính:** 2–3 giờ  
> **Definition of Done:** Build sạch + ASan = 0 errors + trả lời đúng Micro-quiz cuối bài

---

## 🎯 Mục tiêu học tập

Sau khi hoàn thành bài lab này, sinh viên có thể:
1. Vẽ chính xác sơ đồ không gian địa chỉ ảo (Virtual Address Space) của một tiến trình.
2. Giải thích tại sao địa chỉ biến Stack **giảm dần** và địa chỉ Heap **tăng dần**.
3. Phân tích chi phí alignment & padding của struct trong C++.
4. Chứng minh sự nguy hiểm của Dangling Pointer thông qua AddressSanitizer output.

---

## 📋 Đề bài

### Phần A — Sơ đồ bộ nhớ tiến trình (30 điểm)

Viết chương trình in địa chỉ và kích thước (bytes) của các thực thể sau, sau đó **vẽ tay** sơ đồ Virtual Address Space tương ứng:

```
┌─────────────────┐  ← Địa chỉ cao (High Address)
│   Stack Frame   │  ← Biến cục bộ, tham số hàm
├─────────────────┤
│       ↓         │
│    (growth)     │
│       ↑         │
├─────────────────┤
│      Heap       │  ← new / malloc
├─────────────────┤
│   BSS Segment   │  ← Biến global chưa khởi tạo
├─────────────────┤
│   Data Segment  │  ← Biến global đã khởi tạo
├─────────────────┤
│   Text Segment  │  ← Mã máy (read-only)
└─────────────────┘  ← Địa chỉ thấp (Low Address 0x0)
```

**Yêu cầu cụ thể:** In ra địa chỉ của:
- Một `int` cục bộ trong `main()`
- Một `int` cục bộ trong một hàm được gọi từ `main()`
- Một biến toàn cục được khởi tạo
- Một biến toàn cục chưa khởi tạo
- Một `int` cấp phát trên Heap bằng `std::make_unique<int>()`

### Phần B — Struct Padding & Alignment (40 điểm)

Dự đoán kích thước của 2 struct sau **trước khi** dùng `sizeof`, sau đó verify:

```cpp
struct Unoptimized {
    char  a;     // 1 byte
    int   b;     // 4 bytes
    char  c;     // 1 byte
    long  d;     // 8 bytes
};

struct Optimized {
    long  d;     // 8 bytes
    int   b;     // 4 bytes
    char  a;     // 1 byte
    char  c;     // 1 byte
};
```

Giải thích tại sao `sizeof(Unoptimized) != sizeof(Optimized)`.

### Phần C — Dangling Pointer Detection (30 điểm)

Hoàn thành hàm `demonstrate_dangling_pointer()` trong `lab1_memory_layout.cpp` để AddressSanitizer bắt được lỗi **stack-use-after-scope**. Chụp lại output của ASan và giải thích từng dòng.

---

## 🛠️ Hướng dẫn biên dịch

```powershell
# Từ thư mục 03_Engineering_Labs_and_Code/
cmake -B build -S . -DCMAKE_BUILD_TYPE=Debug -DENABLE_ASAN=ON
cmake --build build --target lab1_memory_layout -j 4
./build/labs/Week01_Memory_And_Pointers/lab1_memory_layout
```

Hoặc compile trực tiếp (nhanh hơn khi debug):
```powershell
clang++ -std=c++20 -Wall -Wextra -Werror -fsanitize=address,undefined `
        -fno-omit-frame-pointer -g `
        lab1_memory_layout.cpp -o lab1.exe
./lab1.exe
```

---

## ✅ Definition of Done (DoD)

- [ ] **DoD-1:** Biên dịch thành công không có cảnh báo (`-Werror`)
- [ ] **DoD-2:** Output ASan = `0 errors detected` (Phần A & B không có lỗi)
- [ ] **DoD-3:** Phần C trigger đúng `stack-use-after-scope` error từ ASan
- [ ] **DoD-4:** Sơ đồ bộ nhớ vẽ tay nộp kèm (ảnh chụp hoặc file ASCII art)
- [ ] **DoD-5:** Trả lời đúng Micro-quiz bên dưới

---

## 💡 Micro-quiz / Câu hỏi Phản biện

> **Q:** Trên hệ thống 64-bit Linux, tại sao địa chỉ của biến Stack lại **cao hơn** địa chỉ của Heap, và tại sao Stack **tăng xuống dưới** (grow downward) trong khi Heap **tăng lên trên** (grow upward)?  
> Gợi ý: Nghĩ về lý do lịch sử và lợi thế kỹ thuật của thiết kế này khi tiến trình cần cả Stack lẫn Heap cùng tồn tại trong một không gian địa chỉ hạn chế.

### ⚠️ Lỗi phổ biến sinh viên hay gặp

1. **Nhầm địa chỉ biến với giá trị biến:** `int x = 42; &x` là địa chỉ, `x` là giá trị.
2. **Dùng `%p` với `printf` thay vì `std::cout`:** Trên MSVC, format specifier có thể khác.
3. **Quên `reinterpret_cast<void*>` khi in địa chỉ hàm:** Function pointer cần cast đặc biệt.
4. **Giả định địa chỉ Heap nhỏ hơn Stack trên mọi OS:** Trên một số embedded systems, memory map có thể khác hoàn toàn.
