/**
 * @file lab1_memory_layout.cpp
 * @brief Lab 1.1 — Kiến trúc bộ nhớ & Con trỏ (Memory Layout & Pointer Mechanics)
 *
 * @course  ALGO-DUT | Tuần 1 | AlgoCore Systems Corp (CORP-07-ALGO)
 * @ref     CS:APP 3rd ed, Chapter 3
 *
 * Build (with AddressSanitizer):
 *   clang++ -std=c++20 -Wall -Wextra -Werror \
 *           -fsanitize=address,undefined -fno-omit-frame-pointer -g \
 *           lab1_memory_layout.cpp -o lab1
 *
 * Expected output: Zero ASan errors for Parts A & B.
 *                  Part C deliberately triggers stack-use-after-scope.
 */

#include <cstddef>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <memory>
#include <string>

// ─── Global variables (Data segment — initialised) ───────────────────────────
int g_initialized   = 100;   // .data section
int g_uninitialized;         // .bss  section (zero-initialised by OS)

// ─── Utility: print address and size of an object ────────────────────────────
template <typename T>
void print_addr(const std::string& label, const T& obj) {
    // reinterpret_cast<const void*> is the idiomatic way to print addresses
    std::cout
        << std::setw(38) << std::left << label
        << "  addr = " << std::setw(18) << reinterpret_cast<const void*>(&obj)
        << "  sizeof = " << sizeof(T) << " bytes\n";
}

// ─── Part A: Memory layout exploration ───────────────────────────────────────
void inner_function() {
    int local_in_inner = 999;
    print_addr("inner_function() → local_in_inner", local_in_inner);
}

void part_a_memory_map() {
    std::cout << "\n════════════════════════════════════════════════════════\n";
    std::cout << "  PART A — Virtual Address Space Exploration\n";
    std::cout << "════════════════════════════════════════════════════════\n";

    int local_in_main = 42;

    // Stack variables (addresses should be HIGH and decrease as we go deeper)
    print_addr("main() → local_in_main (Stack)", local_in_main);
    inner_function();  // deeper stack frame → lower address

    // Global variables (Data / BSS segment — addresses are LOW)
    print_addr("g_initialized (Data segment)", g_initialized);
    print_addr("g_uninitialized (BSS segment)", g_uninitialized);

    // Heap (addresses are MEDIUM, grow upward)
    auto heap_int = std::make_unique<int>(777);  // RAII: no delete needed
    print_addr("heap_int (Heap via make_unique)", *heap_int);

    std::cout << "\n📝 Observation:\n"
              << "   Stack addresses > Heap addresses > Data/BSS addresses\n"
              << "   Stack grows DOWNWARD (address decreases with deeper calls)\n"
              << "   Heap grows UPWARD   (address increases with more allocations)\n";
}

// ─── Part B: Struct Padding & Alignment ──────────────────────────────────────
struct Unoptimized {
    char  a;   // 1 byte  + 3 bytes padding
    int   b;   // 4 bytes
    char  c;   // 1 byte  + 7 bytes padding
    long  d;   // 8 bytes
    // Total with padding = 24 bytes (predict before running!)
};

struct Optimized {
    long  d;   // 8 bytes
    int   b;   // 4 bytes
    char  a;   // 1 byte
    char  c;   // 1 byte
    // 2 bytes padding at end
    // Total = 16 bytes
};

void part_b_struct_padding() {
    std::cout << "\n════════════════════════════════════════════════════════\n";
    std::cout << "  PART B — Struct Padding & Memory Alignment\n";
    std::cout << "════════════════════════════════════════════════════════\n";

    Unoptimized u{};
    Optimized   o{};

    std::cout << "sizeof(Unoptimized) = " << sizeof(Unoptimized) << " bytes\n";
    std::cout << "sizeof(Optimized)   = " << sizeof(Optimized)   << " bytes\n";
    std::cout << "Memory saved by reordering: "
              << sizeof(Unoptimized) - sizeof(Optimized) << " bytes ("
              << (sizeof(Unoptimized) - sizeof(Optimized)) * 100 / sizeof(Unoptimized)
              << "% reduction)\n";

    // Print individual member offsets using offsetof
    std::cout << "\nUnoptimized member offsets:\n";
    std::cout << "  &u.a = offset " << offsetof(Unoptimized, a) << "\n";
    std::cout << "  &u.b = offset " << offsetof(Unoptimized, b) << "\n";
    std::cout << "  &u.c = offset " << offsetof(Unoptimized, c) << "\n";
    std::cout << "  &u.d = offset " << offsetof(Unoptimized, d) << "\n";

    std::cout << "\nOptimized member offsets:\n";
    std::cout << "  &o.d = offset " << offsetof(Optimized, d) << "\n";
    std::cout << "  &o.b = offset " << offsetof(Optimized, b) << "\n";
    std::cout << "  &o.a = offset " << offsetof(Optimized, a) << "\n";
    std::cout << "  &o.c = offset " << offsetof(Optimized, c) << "\n";

    // Suppress unused variable warnings
    (void)u; (void)o;
}

// ─── Part C: Dangling Pointer — intentional ASan trigger ─────────────────────
// ⚠️  This function INTENTIONALLY causes a use-after-scope error.
//     Run with -fsanitize=address to see the full ASan report.
//     DO NOT "fix" this — the crash is the deliverable for Part C.
[[maybe_unused]] static void demonstrate_dangling_pointer() {
    std::cout << "\n════════════════════════════════════════════════════════\n";
    std::cout << "  PART C — Dangling Pointer (ASan Intentional Trigger)\n";
    std::cout << "════════════════════════════════════════════════════════\n";

    int* dangling = nullptr;

    {
        int local = 42;
        dangling  = &local;  // points to stack variable
        std::cout << "Inside scope: *dangling = " << *dangling << "\n";
    }  // ← 'local' destroyed here; dangling is now invalid

    // ⚡ UNDEFINED BEHAVIOR — ASan will catch this:
    std::cout << "Outside scope: *dangling = " << *dangling << "\n";
    //                                              ^^^^^^^^ stack-use-after-scope
}

// ─── main ────────────────────────────────────────────────────────────────────
int main() {
    std::cout << "╔══════════════════════════════════════════════════════╗\n";
    std::cout << "║  Lab 1.1 — Memory Layout & Pointer Mechanics         ║\n";
    std::cout << "║  AlgoCore Systems Corp | CORP-07-ALGO | Tuần 1        ║\n";
    std::cout << "╚══════════════════════════════════════════════════════╝\n";

    part_a_memory_map();
    part_b_struct_padding();

    // ── Uncomment Part C to trigger ASan stack-use-after-scope ──────────────
    // demonstrate_dangling_pointer();
    // ────────────────────────────────────────────────────────────────────────

    std::cout << "\n✅ Parts A & B completed. ASan should report 0 errors.\n";
    std::cout << "📌 Uncomment demonstrate_dangling_pointer() for Part C.\n\n";
    return 0;
}
