/**
 * @file test_dynamic_array.cpp
 * @brief TDD test suite for algocore::DynamicArray<T> using Catch2 v3.
 *
 * @course  ALGO-DUT | AlgoCore Systems Corp (CORP-07-ALGO)
 * @ref     CLRS 4th ed, Chapter 17 (Amortized Analysis)
 *
 * Build & run:
 *   cmake -B build -S .. -DCMAKE_BUILD_TYPE=Debug -DENABLE_ASAN=ON
 *   cmake --build build -j 4
 *   ctest --test-dir build --output-on-failure -V
 *
 * DoD requirement: 0 bytes leaked when run under AddressSanitizer.
 */

#include <algocore/dynamic_array.hpp>

#include <catch2/catch_test_macros.hpp>
#include <catch2/matchers/catch_matchers_range_equals.hpp>

#include <numeric>   // std::iota
#include <string>
#include <vector>

using algocore::DynamicArray;
using Catch::Matchers::RangeEquals;

// ─────────────────────────────────────────────────────────────────────────────
// Section 1: Construction & Basic Invariants
// ─────────────────────────────────────────────────────────────────────────────
TEST_CASE("DynamicArray — default construction", "[dynamic_array][construction]") {
    DynamicArray<int> arr;
    REQUIRE(arr.empty());
    REQUIRE(arr.size() == 0);
    REQUIRE(arr.capacity() == 2);  // initial capacity per design
}

TEST_CASE("DynamicArray — reserve construction", "[dynamic_array][construction]") {
    DynamicArray<int> arr{16};
    REQUIRE(arr.empty());
    REQUIRE(arr.capacity() == 16);
}

TEST_CASE("DynamicArray — zero capacity reserve rounds up to 1", "[dynamic_array]") {
    DynamicArray<int> arr{0};
    REQUIRE(arr.capacity() >= 1);
}

// ─────────────────────────────────────────────────────────────────────────────
// Section 2: push_back (lvalue & rvalue) + size growth
// ─────────────────────────────────────────────────────────────────────────────
TEST_CASE("DynamicArray — push_back lvalue", "[dynamic_array][push_back]") {
    DynamicArray<int> arr;
    for (int i = 0; i < 10; ++i) {
        arr.push_back(i);
        REQUIRE(arr.size() == static_cast<std::size_t>(i + 1));
        REQUIRE_FALSE(arr.empty());
    }
}

TEST_CASE("DynamicArray — push_back rvalue (move semantics)", "[dynamic_array][push_back]") {
    DynamicArray<std::string> arr;
    std::string s = "hello";
    arr.push_back(std::move(s));  // s should be in moved-from state
    REQUIRE(arr.size() == 1);
    REQUIRE(arr[0] == "hello");
}

TEST_CASE("DynamicArray — capacity doubles on overflow", "[dynamic_array][capacity]") {
    DynamicArray<int> arr;               // capacity = 2
    arr.push_back(1);                    // size=1, cap=2
    arr.push_back(2);                    // size=2, cap=2
    REQUIRE(arr.capacity() == 2);
    arr.push_back(3);                    // triggers realloc → cap=4
    REQUIRE(arr.capacity() == 4);
    REQUIRE(arr.size() == 3);
}

TEST_CASE("DynamicArray — large push_back (100k elements, amortized O(1))",
          "[dynamic_array][stress]") {
    DynamicArray<int> arr;
    constexpr int N = 100'000;
    for (int i = 0; i < N; ++i) arr.push_back(i);
    REQUIRE(arr.size() == static_cast<std::size_t>(N));
    // Spot-check values — ensures no corruption during reallocs
    REQUIRE(arr[0]     == 0);
    REQUIRE(arr[N - 1] == N - 1);
    REQUIRE(arr[N / 2] == N / 2);
}

// ─────────────────────────────────────────────────────────────────────────────
// Section 3: Element access (at, operator[], front, back)
// ─────────────────────────────────────────────────────────────────────────────
TEST_CASE("DynamicArray — at() bounds check throws", "[dynamic_array][access]") {
    DynamicArray<int> arr;
    arr.push_back(42);
    REQUIRE(arr.at(0) == 42);
    REQUIRE_THROWS_AS(arr.at(1), std::out_of_range);
    REQUIRE_THROWS_AS(arr.at(999), std::out_of_range);
}

TEST_CASE("DynamicArray — at() non-const allows mutation", "[dynamic_array][access]") {
    DynamicArray<int> arr;
    arr.push_back(10);
    arr.at(0) = 99;       // non-const reference — must compile and mutate
    REQUIRE(arr[0] == 99);
}

TEST_CASE("DynamicArray — operator[] unchecked access", "[dynamic_array][access]") {
    DynamicArray<int> arr;
    arr.push_back(7);
    arr.push_back(8);
    arr[0] = 100;
    REQUIRE(arr[0] == 100);
    REQUIRE(arr[1] == 8);
}

TEST_CASE("DynamicArray — front() and back()", "[dynamic_array][access]") {
    DynamicArray<int> arr;
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(3);
    REQUIRE(arr.front() == 1);
    REQUIRE(arr.back() == 3);
    arr.back() = 99;    // mutate via back()
    REQUIRE(arr.back() == 99);
}

// ─────────────────────────────────────────────────────────────────────────────
// Section 4: pop_back, clear
// ─────────────────────────────────────────────────────────────────────────────
TEST_CASE("DynamicArray — pop_back", "[dynamic_array][modifiers]") {
    DynamicArray<int> arr;
    arr.push_back(1);
    arr.push_back(2);
    arr.pop_back();
    REQUIRE(arr.size() == 1);
    REQUIRE(arr[0] == 1);
    arr.pop_back();
    REQUIRE(arr.empty());
}

TEST_CASE("DynamicArray — clear resets size but not capacity", "[dynamic_array][modifiers]") {
    DynamicArray<int> arr;
    for (int i = 0; i < 8; ++i) arr.push_back(i);
    const auto cap_before = arr.capacity();
    arr.clear();
    REQUIRE(arr.empty());
    REQUIRE(arr.capacity() == cap_before);  // capacity preserved
}

// ─────────────────────────────────────────────────────────────────────────────
// Section 5: Copy & Move semantics (Rule of 5)
// ─────────────────────────────────────────────────────────────────────────────
TEST_CASE("DynamicArray — copy constructor deep-copies", "[dynamic_array][rule-of-5]") {
    DynamicArray<int> orig;
    orig.push_back(10);
    orig.push_back(20);

    DynamicArray<int> copy{orig};
    REQUIRE(copy.size() == 2);
    REQUIRE(copy[0] == 10);

    copy[0] = 999;            // mutate copy
    REQUIRE(orig[0] == 10);   // original must be unaffected
}

TEST_CASE("DynamicArray — move constructor transfers ownership", "[dynamic_array][rule-of-5]") {
    DynamicArray<int> orig;
    orig.push_back(42);
    DynamicArray<int> moved{std::move(orig)};
    REQUIRE(moved.size() == 1);
    REQUIRE(moved[0] == 42);
}

TEST_CASE("DynamicArray — copy assignment", "[dynamic_array][rule-of-5]") {
    DynamicArray<int> a, b;
    a.push_back(1);
    b.push_back(2);
    b = a;
    REQUIRE(b[0] == 1);
    REQUIRE(a[0] == 1);  // source unchanged
}

TEST_CASE("DynamicArray — self-assignment is safe", "[dynamic_array][rule-of-5]") {
    DynamicArray<int> arr;
    arr.push_back(5);
    arr = arr;  // must not crash or corrupt
    REQUIRE(arr[0] == 5);
}

// ─────────────────────────────────────────────────────────────────────────────
// Section 6: std::span view + iterators
// ─────────────────────────────────────────────────────────────────────────────
TEST_CASE("DynamicArray — as_span() returns correct view", "[dynamic_array][span]") {
    DynamicArray<int> arr;
    for (int i = 0; i < 5; ++i) arr.push_back(i);
    auto sp = arr.as_span();
    REQUIRE(sp.size() == 5);
    REQUIRE(sp[2] == 2);
}

TEST_CASE("DynamicArray — range-for iteration", "[dynamic_array][iterator]") {
    DynamicArray<int> arr;
    for (int i = 1; i <= 5; ++i) arr.push_back(i);

    std::vector<int> collected;
    for (const int& v : arr) collected.push_back(v);

    REQUIRE_THAT(collected, RangeEquals(std::vector<int>{1, 2, 3, 4, 5}));
}

// ─────────────────────────────────────────────────────────────────────────────
// Section 7: emplace_back
// ─────────────────────────────────────────────────────────────────────────────
TEST_CASE("DynamicArray — emplace_back constructs in-place", "[dynamic_array][emplace]") {
    DynamicArray<std::string> arr;
    arr.emplace_back(5, 'x');     // constructs std::string(5, 'x') = "xxxxx"
    REQUIRE(arr.size() == 1);
    REQUIRE(arr[0] == "xxxxx");
}
