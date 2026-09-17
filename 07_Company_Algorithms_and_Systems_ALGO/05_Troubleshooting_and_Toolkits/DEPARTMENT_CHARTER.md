# 📜 ĐIỀU LỆ PHÒNG KIỂM SOÁT SỰ CỐ & CÔNG CỤ CHẨN ĐOÁN (TROUBLESHOOTING & TOOLKITS DEPT)
## Phòng 05 — Công Ty Hệ Thống & Giải Thuật Hiệu Năng Cao (CORP-07-ALGO)

> **Mã Phòng Ban:** `ALGO-DEPT-05`  
> **Trưởng phòng phụ trách:** Agent `SMS-02` (Syllabus Sentinel & Technical Auditor)  
> **Thẩm quyền kỹ thuật:** Chẩn đoán lỗi bộ nhớ, Điều tra sự cố crash (SegFault), Giám sát Concurrency & Profiling hiệu năng  
> **Bộ công cụ cốt lõi:** GDB / LLDB / AddressSanitizer / ThreadSanitizer / Valgrind / Linux Perf

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kiểm Soát Sự Cố là **"Bệnh viện Cấp cứu & Phòng Chẩn đoán Hình ảnh"** cho toàn bộ mã nguồn của AlgoCore Systems Corp:
1. **Khắc Phục Sự Cố Hệ Thống Khẩn Cấp**: Hướng dẫn học viên và AI Agent quy trình cô lập nguyên nhân gốc rễ (Root Cause Analysis - RCA) khi chương trình gặp các lỗi chí tử: Segmentation Fault (SIGSEGV), Abort (SIGABRT), Bus Error (SIGBUS).
2. **Quét & Triệt Tiêu Lỗ Hổng Bộ Nhớ**: Vận hành các công cụ Sanitizers phát hiện rò rỉ bộ nhớ (Memory Leak), ghi đè bộ đệm (Buffer Overflow), sử dụng vùng nhớ đã giải phóng (Use-After-Free).
3. **Phát Hiện Tranh Chấp Đa Luồng (Data Race & Deadlock)**: Giám sát các luồng thực thi, phát hiện hiện tượng khóa chết và tranh chấp dữ liệu khi học viên lập trình song song.
4. **Phân Tích Hiệu Năng Tầng Thấp (Hardware Profiling)**: Đo đạc tỷ lệ trượt bộ đệm Cache Miss (L1/L2/L3), dự đoán nhánh sai (Branch Misprediction) và hiện tượng False Sharing.

---

## ⚖️ 2. BỘ NGUYÊN TẮC DEBUGGING BẤT BIẾN (DEBUGGING INVARIANTS)

1. **Nguyên Tắc Bằng Chứng Thực Nghiệm (No Guesswork)**:
   - Nghiêm cấm "sửa mò" (trial-and-error) hoặc thêm lệnh `std::cout` bừa bãi. Bắt buộc phải có dấu vết Stack Trace từ GDB hoặc báo cáo từ AddressSanitizer trước khi sửa code.
2. **Nguyên Tắc Bật Toàn Bộ Cờ Kiểm Soát (Zero Tolerance for Warnings)**:
   - Mã nguồn gặp lỗi trước hết phải được build lại với `-Wall -Wextra -Wpedantic` để loại bỏ các cảnh báo tiềm ẩn lúc biên dịch.
3. **Nguyên Tắc Tái Lập Tối Thiểu (Minimal Reproducible Example - MRE)**:
   - Khi gặp bug thuật toán, phải cô lập thành một test case nhỏ nhất kích hoạt lỗi (1 mảng gồm 2-3 phần tử) thay vì debug trên tập dữ liệu hàng triệu phần tử.

---

## 🛠️ 3. SKILLS ROUTE & TOOLCHAIN CHẨN ĐOÁN CHUẨN

| Loại Sự Cố | Công Cụ Chuyên Dụng | Cờ Biên Dịch / Lệnh CLI Kích Hoạt |
| :--- | :--- | :--- |
| **Tràn bộ đệm, Use-after-free** | AddressSanitizer (ASan) | `-fsanitize=address -fno-omit-frame-pointer -g` |
| **Hành vi bất định (Undefined Behavior)** | UndefinedBehaviorSanitizer (UBSan) | `-fsanitize=undefined -g` |
| **Đua dữ liệu đa luồng (Data Race)** | ThreadSanitizer (TSan) | `-fsanitize=thread -g` *(Không bật chung với ASan)* |
| **Rò rỉ bộ nhớ chi tiết (Memory Leak)** | Valgrind Memcheck | `valgrind --leak-check=full --track-origins=yes ./app` |
| **Crash sập nguồn (Segfault Callstack)** | GDB / LLDB Debugger | `gdb -batch -ex "run" -ex "bt full" --args ./app` |
| **Tối ưu Cache Miss & CPU Cycles** | Linux `perf` / Cachegrind | `perf stat -e cache-misses,cache-references,branches ./app` |

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
05_Troubleshooting_and_Toolkits/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 scripts/                              # Kịch bản tự động hóa chẩn đoán
│   ├── run_asan_check.sh                   # Chạy kiểm tra AddressSanitizer
│   ├── run_valgrind_leak_check.sh          # Quét rò rỉ bộ nhớ tự động
│   └── profile_cache_misses.sh             # Đo lường Cache Locality bằng perf
└── 📁 diagnostic_guides/                    # Sổ tay chẩn đoán chi tiết theo từng lỗi
    ├── sigsegv_triage_guide.md             # Hướng dẫn cứu vãn Segfault
    └── data_race_remediation.md            # Phương pháp khử data race đa luồng
```

---

## 💻 5. MẪU KHUNG CODE CHẨN ĐOÁN & PROFILING (BOILERPLATE TOOLKIT)

```cpp
// Boilerplate: Debugging Diagnostic Harness với High-Resolution Timer & RAII Scoped Profiler
#include <iostream>
#include <chrono>
#include <string_view>

class ScopedTimer {
public:
    explicit ScopedTimer(std::string_view name)
        : m_name(name), m_start(std::chrono::high_resolution_clock::now()) {}

    ~ScopedTimer() {
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - m_start).count();
        std::cout << "[PROFILE] " << m_name << " took " << duration << " us\n";
    }

private:
    std::string_view m_name;
    std::chrono::time_point<std::chrono::high_resolution_clock> m_start;
};
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU CHẨN ĐOÁN (DEFINITION OF DONE - DoD)

Một ca điều tra sự cố được đóng lại khi:
- [ ] **DoD-1**: Đã xác định được Root Cause chính xác qua Stack Trace / Sanitizer log.
- [ ] **DoD-2**: Tạo được 1 file test case độc lập tối thiểu (MRE) tái lập được lỗi trước khi sửa.
- [ ] **DoD-3**: Mã nguồn sau sửa chạy pass 100% test suite với cờ `-fsanitize=address,undefined`.
- [ ] **DoD-4**: Cập nhật bài học vào sổ tay chẩn đoán của phòng ban để tránh tái diễn.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & CẨM NANG KHẮC PHỤC KHẨN CẤP (TOP 5 EMERGENCY RUNBOOKS)

### 🚨 RUNBOOK 1: XỬ LÝ SEGMENTATION FAULT (SIGSEGV)
* **Triệu chứng**: Chương trình đột ngột dừng lại và thông báo: `Segmentation fault (core dumped)`.
* **Nguyên nhân phổ biến**:
  1. Dereference con trỏ `nullptr` hoặc con trỏ rác chưa khởi tạo.
  2. Truy cập mảng ngoài giới hạn (`index >= size`).
  3. Truy cập vùng nhớ đã bị giải phóng (`Use-After-Free`).
* **Quy trình xử lý 3 bước chuẩn hóa của Agent**:
  1. *Bước 1 - Biên dịch với ASan*:
     ```bash
     clang++ -std=c++20 -fsanitize=address -g main.cpp -o main_debug
     ./main_debug
     ```
  2. *Bước 2 - Đọc báo cáo ASan*: Tìm dòng `AddressSanitizer: heap-buffer-overflow` hoặc `SEGV on unknown address 0x000000000000`. ASan sẽ chỉ đích danh tên tệp và số dòng chính xác gây lỗi.
  3. *Bước 3 - Khắc phục*: Thay thế truy cập mảng `arr[i]` bằng `arr.at(i)` để kiểm tra biên, hoặc dùng `std::make_unique` để đảm bảo con trỏ luôn được khởi tạo hợp lệ.

---

### 🚨 RUNBOOK 2: XỬ LÝ RÒ RỈ BỘ NHỚ (MEMORY LEAK TRIAGE)
* **Triệu chứng**: Bộ nhớ RAM tăng liên tục trong Task Manager khi chương trình chạy vòng lặp lâu dài.
* **Quy trình xử lý với Valgrind**:
  ```bash
  valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./main_app
  ```
* **Bảng giải mã phân loại rò rỉ của Valgrind**:
  - `definitely lost`: **Cực kỳ nghiêm trọng!** Không còn con trỏ nào trỏ tới vùng nhớ này $\rightarrow$ Quên giải phóng. Khắc phục bằng cách chuyển toàn bộ sang `std::unique_ptr`.
  - `indirectly lost`: Cấu trúc bị rò rỉ (ví dụ cây hoặc danh sách liên kết bị mất nút gốc).
  - `still reachable`: Tài nguyên chưa kịp giải phóng khi kết thúc chương trình (ít nghiêm trọng nhưng vẫn cần dọn sạch).

---

### 🚨 RUNBOOK 3: XỬ LÝ ĐUA DỮ LIỆU ĐA LUỒNG (DATA RACE IN CONCURRENCY)
* **Triệu chứng**: Kết quả tính toán sai lệch ngẫu nhiên giữa các lần chạy, biến đếm bị mất dữ liệu.
* **Quy trình xử lý với ThreadSanitizer**:
  ```bash
  clang++ -std=c++20 -fsanitize=thread -g concurrent_code.cpp -o thread_app
  ./thread_app
  ```
* **Báo cáo TSan**:
  - TSan sẽ in ra 2 stack trace song song: *Luồng 1 đang ghi dữ liệu tại địa chỉ 0x...* và *Luồng 2 đang đọc dữ liệu tại cùng địa chỉ mà không có đồng bộ*.
* **Khắc phục**:
  - Đặt biến chia sẻ vào vùng khóa: `std::scoped_lock lock(m_mutex);`.
  - Hoặc chuyển biến sang kiểu nguyên tử: `std::atomic<int64_t> m_counter{0};`.

---

### 🚨 RUNBOOK 4: XỬ LÝ TRÀN NGĂN XẾP (STACK OVERFLOW RUNBOOK)
* **Triệu chứng**: Chương trình sập khi gọi hàm đệ quy lớn ($N > 10^5$).
* **Nguyên nhân**: Đệ quy thiếu trường hợp cơ sở (Base Case) hoặc mảng quá lớn cấp phát cục bộ trên Stack (`int big_arr[10000000]`).
* **Khắc phục**:
  - Chuyển mảng lớn sang Heap: `std::vector<int> big_arr(10000000);`.
  - Khử đệ quy bằng cách tự duy trì `std::stack` trên Heap hoặc áp dụng Tail Recursion Optimization.

---

### 🚨 RUNBOOK 5: XỬ LÝ HIỆU NĂNG THẤP DO TRẬT CACHE (CACHE LINE MISS PROFILE)
* **Triệu chứng**: Thuật toán có độ phức tạp lý thuyết là $O(N^2)$ nhưng chạy chậm hơn 10 lần so với thuật toán tương đương.
* **Đo đạc bằng Linux Perf**:
  ```bash
  perf stat -e L1-dcache-load-misses,L1-dcache-loads,instructions,cycles ./benchmark_app
  ```
* **Khắc phục**:
  - Chuyển việc duyệt mảng 2D từ cột-hàng sang hàng-cột (Row-Major traversal).
  - Áp dụng cấu trúc dữ liệu Data-Oriented Design (SoA: Structure of Arrays thay vì AoS: Array of Structures) để tối đa hóa tính cục bộ không gian (Spatial Locality).
