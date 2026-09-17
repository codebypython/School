# 📜 ĐIỀU LỆ PHÒNG TƯ LIỆU & BÀI GIẢNG GỐC (LECTURES & RAW MATERIALS DEPT)
## Phòng 02 — Công Ty Hệ Thống & Giải Thuật Hiệu Năng Cao (CORP-07-ALGO)

> **Mã Phòng Ban:** `ALGO-DEPT-02`  
> **Trưởng phòng phụ trách:** Agent `EKC-03` (Knowledge Curator & Quality Sentinel)  
> **Cơ quan thẩm định:** Thước đo ER-QVR 100 Điểm (`00_Corporate_Knowledge_Vault`)  
> **Phạm vi bảo tồn:** Slide bài giảng chính quy, Chứng minh toán học giải tích, Ngân hàng đề thi thuật toán

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Tư Liệu là **thư viện tài liệu gốc và kho lưu trữ chân lý học thuật** của AlgoCore Systems Corp:
1. **Lưu Trữ Slide & Đề Cương Gốc**: Lưu trữ toàn bộ slide bài giảng của trường ĐHBK Đà Nẵng (DUT) và các trường đại học hàng đầu (Stanford CS106B, MIT 6.006).
2. **Chứng Minh Toán Học Chặt Chẽ (Formal Proofs Vault)**: Lưu trữ các chứng minh toán học giải tích tiệm cận (Định lý Thợ - Master Theorem, Phương pháp Thế, Phương pháp Cây Đệ Quy, Phân tích Khấu hao bằng Phương pháp Thế Năng - Potential Method).
3. **Ngân Hàng Câu Hỏi & Bài Toán Phỏng Vấn (Problem Bank)**: Tổng hợp các bài toán thuật toán phân loại theo cấu trúc dữ liệu từ cơ bản đến LeetCode Hard / Codeforces Div 2.

---

## ⚖️ 2. BỘ QUY TẮC BẢO TỒN DỮ LIỆU (CURATION INVARIANTS)

1. **Chuẩn Mực Ký Hiệu Toán Học (LaTeX Invariant)**:
   - Toàn bộ công thức toán học, tiệm cận, phương trình truy hồi bắt buộc phải soạn thảo dưới định dạng LaTeX chuẩn:
     $$T(n) = aT(n/b) + f(n)$$
   - Tuyệt đối không viết công thức dưới dạng text cẩu thả (ví dụ: cấm viết `T(n) = a*T(n/b) + O(n)`).
2. **Quy Tắc Đối Chiếu Nguồn Gốc (Provenance & Citation)**:
   - Mọi định lý hoặc bài tập trong phòng này bắt buộc phải ghi rõ nguồn trích xuất: Số trang, số chương từ sách Tier A+ trong Knowledge Vault (Ví dụ: `CLRS 4th ed, Chapter 4, Page 94`).
3. **Quy Tắc Không "Rác Dữ Liệu" (Zero Clutter)**:
   - Nghiêm cấm lưu các file tải về từ internet không rõ nguồn gốc, file nháp chưa qua thẩm định hoặc slide sao chép thiếu bản quyền.

---

## 📁 3. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
02_Lectures_and_Raw_Materials/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 slides/                               # Slide bài giảng số hóa Markdown/PDF
│   ├── Week01_03_Memory_and_Pointers.md
│   ├── Week04_07_Linear_and_Trees.md
│   └── Week08_11_Graphs_and_DP.md
├── 📁 mathematical_proofs/                  # Chứng minh toán học hình thức
│   ├── master_theorem_proof.md              # Chứng minh 3 trường hợp của Master Theorem
│   ├── amortized_analysis_vector.md         # Chứng minh chi phí O(1) của vector resizing x2
│   └── dijkstra_correctness_proof.md        # Chứng minh tính đúng đắn của Dijkstra
└── 📁 exam_bank/                            # Ngân hàng đề thi thuật toán
    ├── dut_past_exams/                      # Đề thi các năm của ĐHBK Đà Nẵng
    └── bigtech_interview_problems/          # Bài toán phỏng vấn Google, Meta, Amazon
```

---

## 💻 4. MẪU TƯ LIỆU CHỨNG MINH HÌNH THỨC (GOLD MASTER PROOF TEMPLATE)

```markdown
# 📐 BẢN CHỨNG MINH HỌC THUẬT: PHÂN TÍCH KHẤU HAO MẢNG ĐỘNG (DYNAMIC ARRAY AMORTIZATION)
> **Nguồn trích:** CLRS 4th Edition, Chapter 17 (Amortized Analysis), Trang 456  
> **Người thẩm định:** Agent `EKC-03` | **Điểm ER-QVR:** 98/100

### 1. Mô hình bài toán
Xét mảng động có kích thước ban đầu là 1. Khi mảng đầy, ta cấp phát mảng mới có dung lượng gấp đôi ($2 \times$) và sao chép toàn bộ phần tử sang.

### 2. Phương pháp hàm thế năng (The Potential Method)
Định nghĩa hàm thế năng $\Phi(D_i)$ sau thao tác thứ $i$:
$$\Phi(D_i) = 2 \cdot size_i - capacity_i$$

- **Trạng thái ban đầu**: $\Phi(D_0) = 0$.
- **Trạng thái sau khi mảng vừa nhân đôi**: $capacity_i = 2 \cdot size_i \implies \Phi(D_i) = 0$.
- **Trạng thái khi mảng đầy**: $capacity_i = size_i \implies \Phi(D_i) = size_i \ge 0$.

### 3. Tính toán chi phí khấu hao ($\hat{c}_i$)
Chi phí khấu hao của thao tác thứ $i$ được định nghĩa:
$$\hat{c}_i = c_i + \Phi(D_i) - \Phi(D_{i-1})$$

- **Trường hợp 1 (Không cần nhân đôi dung lượng)**: $c_i = 1$
  $$\hat{c}_i = 1 + (2(size_{i-1}+1) - capacity) - (2 \cdot size_{i-1} - capacity) = 3 = O(1)$$
- **Trường hợp 2 (Phải nhân đôi dung lượng)**: $size_{i-1} = capacity_{i-1}$, $c_i = size_{i-1} + 1$
  $$\hat{c}_i = (size_{i-1} + 1) + 0 - (2 \cdot size_{i-1} - size_{i-1}) = 2 = O(1)$$

**Kết luận**: Chi phí khấu hao của mỗi thao tác `push_back` là $O(1)$.
```
