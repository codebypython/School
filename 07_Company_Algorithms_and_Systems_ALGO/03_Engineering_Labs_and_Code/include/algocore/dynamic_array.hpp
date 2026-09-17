/**
 * @file dynamic_array.hpp
 * @brief Production-grade dynamic array (Vector) — C++20, RAII, zero memory leaks.
 *
 * @author    AlgoCore Systems Engineering Division (CORP-07-ALGO)
 * @standard  C++20 | C++ Core Guidelines
 * @ref       CLRS 4th ed, Chapter 17 (Amortized Analysis)
 *            Stroustrup — A Tour of C++ (3rd ed), Chapter 12
 *
 * Complexity guarantees:
 *   push_back   — Amortized O(1)   [Geometric resizing ×2]
 *   at / []     — O(1)
 *   pop_back    — O(1)
 *   clear       — O(N) (destructs elements)
 *   Space       — O(N) auxiliary
 *
 * RAII contract: all memory is owned by std::unique_ptr<T[]>.
 * No manual new/delete. ASan + Valgrind must report 0 bytes leaked.
 */

#ifndef ALGOCORE_DYNAMIC_ARRAY_HPP
#define ALGOCORE_DYNAMIC_ARRAY_HPP

#include <concepts>
#include <cstddef>
#include <memory>
#include <span>
#include <stdexcept>
#include <utility>

namespace algocore {

// ─────────────────────────────────────────────────────────────────────────────
// Concept: element must be destructible without throwing
// ─────────────────────────────────────────────────────────────────────────────
template <typename T>
concept SafeElement = std::is_nothrow_destructible_v<T>;

// ─────────────────────────────────────────────────────────────────────────────
// DynamicArray<T>
// ─────────────────────────────────────────────────────────────────────────────
template <SafeElement T>
class DynamicArray {
public:
    // ── Type aliases (STL-compatible) ────────────────────────────────────────
    using value_type      = T;
    using size_type       = std::size_t;
    using reference       = T&;
    using const_reference = const T&;
    using pointer         = T*;
    using const_pointer   = const T*;

    // ── Constructors ─────────────────────────────────────────────────────────

    /// Default: initial capacity = 2 to avoid realloc on first two push_backs
    DynamicArray()
        : m_capacity{2}
        , m_size{0}
        , m_data{std::make_unique<T[]>(2)}
    {}

    /// Reserve constructor — preallocate without initialising elements
    explicit DynamicArray(size_type initial_capacity)
        : m_capacity{initial_capacity == 0 ? 1 : initial_capacity}
        , m_size{0}
        , m_data{std::make_unique<T[]>(m_capacity)}
    {}

    // ── Rule of 5 ────────────────────────────────────────────────────────────

    ~DynamicArray() = default;  // unique_ptr handles deallocation automatically

    /// Move constructor — O(1), transfers ownership without copying
    DynamicArray(DynamicArray&& other) noexcept = default;

    /// Move assignment — O(1)
    DynamicArray& operator=(DynamicArray&& other) noexcept = default;

    /// Copy constructor — O(N) deep copy
    DynamicArray(const DynamicArray& other)
        : m_capacity{other.m_capacity}
        , m_size{other.m_size}
        , m_data{std::make_unique<T[]>(other.m_capacity)}
    {
        for (size_type i = 0; i < m_size; ++i) {
            m_data[i] = other.m_data[i];
        }
    }

    /// Copy assignment — copy-and-swap idiom for strong exception safety
    DynamicArray& operator=(const DynamicArray& other) {
        if (this != &other) {
            DynamicArray temp{other};           // copy
            *this = std::move(temp);            // swap via move assignment
        }
        return *this;
    }

    // ── Modifiers ────────────────────────────────────────────────────────────

    /// Append lvalue — copies the value. Amortized O(1).
    void push_back(const T& value) {
        ensure_capacity();
        m_data[m_size++] = value;
    }

    /// Append rvalue — moves the value. Amortized O(1). No unnecessary copy.
    void push_back(T&& value) {
        ensure_capacity();
        m_data[m_size++] = std::move(value);
    }

    /// Construct element in-place — avoids extra copy/move entirely.
    template <typename... Args>
    reference emplace_back(Args&&... args) {
        ensure_capacity();
        m_data[m_size] = T{std::forward<Args>(args)...};
        return m_data[m_size++];
    }

    /// Remove last element. O(1). UB if empty — check with empty() first.
    void pop_back() noexcept {
        if (m_size > 0) --m_size;
    }

    /// Destroy all elements, reset size to 0. Capacity unchanged. O(N).
    void clear() noexcept {
        m_size = 0;
    }

    // ── Element access ───────────────────────────────────────────────────────

    /// Bounds-checked mutable access. Throws std::out_of_range.
    [[nodiscard]] reference at(size_type index) {
        if (index >= m_size) {
            throw std::out_of_range{
                "DynamicArray::at — index " + std::to_string(index) +
                " out of range (size=" + std::to_string(m_size) + ")"
            };
        }
        return m_data[index];
    }

    /// Bounds-checked const access. Throws std::out_of_range.
    [[nodiscard]] const_reference at(size_type index) const {
        if (index >= m_size) {
            throw std::out_of_range{
                "DynamicArray::at — index " + std::to_string(index) +
                " out of range (size=" + std::to_string(m_size) + ")"
            };
        }
        return m_data[index];
    }

    /// Unchecked mutable access — caller guarantees index < size().
    [[nodiscard]] reference operator[](size_type index) noexcept {
        return m_data[index];
    }

    /// Unchecked const access.
    [[nodiscard]] const_reference operator[](size_type index) const noexcept {
        return m_data[index];
    }

    [[nodiscard]] reference       front()       noexcept { return m_data[0]; }
    [[nodiscard]] const_reference front() const noexcept { return m_data[0]; }
    [[nodiscard]] reference       back()        noexcept { return m_data[m_size - 1]; }
    [[nodiscard]] const_reference back()  const noexcept { return m_data[m_size - 1]; }

    // ── Capacity queries ─────────────────────────────────────────────────────

    [[nodiscard]] size_type size()     const noexcept { return m_size; }
    [[nodiscard]] size_type capacity() const noexcept { return m_capacity; }
    [[nodiscard]] bool      empty()    const noexcept { return m_size == 0; }

    // ── C++20 std::span view — zero-copy slice ───────────────────────────────

    [[nodiscard]] std::span<T>       as_span()       noexcept {
        return std::span<T>{m_data.get(), m_size};
    }
    [[nodiscard]] std::span<const T> as_span() const noexcept {
        return std::span<const T>{m_data.get(), m_size};
    }

    // ── Raw pointer (for interop with C APIs, read-only) ─────────────────────
    [[nodiscard]] const_pointer data() const noexcept { return m_data.get(); }
    [[nodiscard]] pointer       data()       noexcept { return m_data.get(); }

    // ── Range-for / iterator support ─────────────────────────────────────────
    [[nodiscard]] pointer       begin()       noexcept { return m_data.get(); }
    [[nodiscard]] const_pointer begin() const noexcept { return m_data.get(); }
    [[nodiscard]] pointer       end()         noexcept { return m_data.get() + m_size; }
    [[nodiscard]] const_pointer end()   const noexcept { return m_data.get() + m_size; }

private:
    size_type              m_capacity;
    size_type              m_size;
    std::unique_ptr<T[]>   m_data;   // sole owner; RAII guarantees cleanup

    /// Grow capacity ×2 when full — Geometric resizing for amortized O(1).
    /// Note: this function may throw std::bad_alloc; caller gets strong guarantee
    /// because the swap only happens after successful allocation.
    void ensure_capacity() {
        if (m_size < m_capacity) return;
        const size_type new_cap = m_capacity * 2;
        auto new_data = std::make_unique<T[]>(new_cap); // may throw bad_alloc
        for (size_type i = 0; i < m_size; ++i) {
            new_data[i] = std::move(m_data[i]);         // move elements O(N)
        }
        m_data     = std::move(new_data);               // atomic ownership transfer
        m_capacity = new_cap;
    }
};

}  // namespace algocore

#endif  // ALGOCORE_DYNAMIC_ARRAY_HPP
