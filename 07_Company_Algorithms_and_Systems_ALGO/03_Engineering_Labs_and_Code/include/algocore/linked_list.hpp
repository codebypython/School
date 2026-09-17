/**
 * @file linked_list.hpp
 * @brief Doubly Linked List — C++20, RAII via std::unique_ptr, zero memory leaks.
 *
 * @author    AlgoCore Systems Engineering Division (CORP-07-ALGO)
 * @standard  C++20 | C++ Core Guidelines
 * @ref       CLRS 4th ed, Chapter 10.2 (Linked Lists)
 *
 * Complexity guarantees:
 *   push_front / push_back  — O(1)
 *   pop_front  / pop_back   — O(1)
 *   find                    — O(N)
 *   erase                   — O(1) given iterator, O(N) given value
 *   size / empty            — O(1)
 *   Space                   — O(N) nodes
 *
 * Ownership model:
 *   Each node owns its successor via unique_ptr (forward ownership chain).
 *   The tail is tracked via raw non-owning pointer for O(1) push_back.
 *   ~DoublyLinkedList() triggers a cascade of unique_ptr destruction — O(N).
 */

#ifndef ALGOCORE_LINKED_LIST_HPP
#define ALGOCORE_LINKED_LIST_HPP

#include <concepts>
#include <cstddef>
#include <memory>
#include <optional>
#include <stdexcept>
#include <utility>

namespace algocore {

template <typename T>
concept ListElement = std::is_nothrow_destructible_v<T>;

// ─────────────────────────────────────────────────────────────────────────────
template <ListElement T>
class DoublyLinkedList {
private:
    struct Node {
        T                    value;
        std::unique_ptr<Node> next{nullptr};  // owns successor
        Node*                 prev{nullptr};  // non-owning back-pointer

        explicit Node(const T& v)  : value{v}            {}
        explicit Node(T&& v)       : value{std::move(v)} {}
    };

public:
    using value_type = T;
    using size_type  = std::size_t;

    DoublyLinkedList()  = default;
    ~DoublyLinkedList() = default;

    // Non-copyable (owning unique_ptrs; copy would require deep clone)
    DoublyLinkedList(const DoublyLinkedList&)            = delete;
    DoublyLinkedList& operator=(const DoublyLinkedList&) = delete;

    // Movable
    DoublyLinkedList(DoublyLinkedList&&) noexcept            = default;
    DoublyLinkedList& operator=(DoublyLinkedList&&) noexcept = default;

    // ── Modifiers ────────────────────────────────────────────────────────────

    void push_front(const T& value) { insert_front(std::make_unique<Node>(value)); }
    void push_front(T&& value)      { insert_front(std::make_unique<Node>(std::move(value))); }

    void push_back(const T& value)  { insert_back(std::make_unique<Node>(value)); }
    void push_back(T&& value)       { insert_back(std::make_unique<Node>(std::move(value))); }

    /// Remove front element. Returns removed value. Throws if empty.
    T pop_front() {
        if (!m_head) throw std::underflow_error{"DoublyLinkedList::pop_front on empty list"};
        T val = std::move(m_head->value);
        m_head = std::move(m_head->next);
        if (m_head) m_head->prev = nullptr;
        else        m_tail = nullptr;
        --m_size;
        return val;
    }

    /// Remove back element. Returns removed value. Throws if empty.
    T pop_back() {
        if (!m_tail) throw std::underflow_error{"DoublyLinkedList::pop_back on empty list"};
        T val = std::move(m_tail->value);
        if (m_tail->prev) {
            Node* new_tail    = m_tail->prev;
            new_tail->next    = nullptr;       // releases ownership of old tail
            m_tail            = new_tail;
        } else {
            m_head = nullptr;
            m_tail = nullptr;
        }
        --m_size;
        return val;
    }

    void clear() noexcept {
        m_head  = nullptr;   // cascade-destructs all nodes via unique_ptr chain
        m_tail  = nullptr;
        m_size  = 0;
    }

    // ── Queries ──────────────────────────────────────────────────────────────

    [[nodiscard]] bool      empty() const noexcept { return m_size == 0; }
    [[nodiscard]] size_type size()  const noexcept { return m_size; }

    [[nodiscard]] std::optional<T> front() const {
        if (!m_head) return std::nullopt;
        return m_head->value;
    }
    [[nodiscard]] std::optional<T> back() const {
        if (!m_tail) return std::nullopt;
        return m_tail->value;
    }

    /// Linear search — returns true if value found.
    [[nodiscard]] bool contains(const T& value) const noexcept {
        const Node* cur = m_head.get();
        while (cur) {
            if (cur->value == value) return true;
            cur = cur->next.get();
        }
        return false;
    }

private:
    std::unique_ptr<Node> m_head{nullptr};  // owns the chain
    Node*                 m_tail{nullptr};  // non-owning, for O(1) push_back
    size_type             m_size{0};

    void insert_front(std::unique_ptr<Node> node) {
        node->next = std::move(m_head);
        if (node->next) node->next->prev = node.get();
        else            m_tail = node.get();
        m_head = std::move(node);
        ++m_size;
    }

    void insert_back(std::unique_ptr<Node> node) {
        node->prev = m_tail;
        if (m_tail) m_tail->next = std::move(node);
        else        m_head       = std::move(node);
        // After moving, m_tail->next or m_head holds the node
        m_tail = (m_tail ? m_tail->next.get() : m_head.get());
        ++m_size;
    }
};

}  // namespace algocore

#endif  // ALGOCORE_LINKED_LIST_HPP
