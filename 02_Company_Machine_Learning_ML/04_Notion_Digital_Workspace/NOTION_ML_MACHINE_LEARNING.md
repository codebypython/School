# 🤖 MASTER WORKSPACE: HỌC MÁY VÀ ỨNG DỤNG
# Đại học Bách khoa — Đại học Đà Nẵng | Semester 7

> 🎓 **Mã học phần**: ML-DUT
> 💡 **Phương châm**: "Viết hàm custom từ đầu (from scratch) $\rightarrow$ Đối chiếu thư viện chuẩn."
> 🛠️ **Công cụ cốt lõi**: NumPy, Pandas, Matplotlib, Scikit-Learn
> 🎯 **Trọng tâm**: Hiểu bản chất Toán học (Đạo hàm, Loss Function) & So sánh Hiệu năng.

---

## 🔬 I. LAB & EXPERIMENT TRACKER (Quản lý Bài tập)

> 💡 **Notion**: Convert thành Database $\rightarrow$ Tạo **Board View** grouped by `Status`.

| Tên Lab / Bài Tập | Phân Loại | Kỹ Thuật (Algorithms) | Tập Dữ Liệu (Dataset) | Độ Khó | Ngày Bắt Đầu | Trạng Thái | Link / Ghi Chú |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Lab 3: Phân cụm Iris** | Unsupervised | K-Means, C-Means, PCA | `flower_dataset.csv` | 🟡 TB | YYYY-MM-DD | 🔲 Todo | Viết tay K-Means |
| **Lab 4: Phân đoạn Ảnh** | Unsupervised | K-Means, Fuzzy C-Means | `sample_image.jpg` | 🔴 Khó | YYYY-MM-DD | 🔲 Todo | Xử lý nhiễu ảnh, $e > 50\%$ |
| _Template Lab..._ | _Supervised_ | _Linear Regression_ | _Housing Data_ | 🟢 Dễ | _—_ | 🔲 Todo | _—_ |

---

## ⚖️ II. FROM-SCRATCH VS LIBRARY COMPARISON LOG (Nhật ký Đối chiếu)

> 💡 **Notion**: Convert thành Database $\rightarrow$ **Cột Metric (Số vòng lặp, Quán tính, Runtime) chỉnh thành type `Number`** để dễ sort và so sánh.

| Bài Tập | Thuật Toán | Quán Tính / Loss (Custom) | Quán Tính / Loss (Sklearn) | Vòng lặp (Custom) | Vòng lặp (Sklearn) | Runtime Custom (ms) | Runtime Sklearn (ms) | Nhận Xét / Bài Học Rút Ra |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| Lab 3 | K-Means (Hoa Iris) | — | — | — | — | — | — | Chú ý cách khởi tạo tâm cụm ban đầu. |
| Lab 4 | K-Means (Ảnh 180x180) | 624.44 | 624.48 | 22 | 6 | 110 | 1560 | Numpy vectorization rất nhanh. Sklearn chậm do chạy nhiều `n_init`. |
| Lab 4 | Fuzzy C-Means ($m=2$) | — | N/A | — | N/A | — | N/A | Sklearn không có sẵn FCM. Phân tách được vùng biên mờ! |
| _Template_ | _Algorithm..._ | _—_ | _—_ | _—_ | _—_ | _—_ | _—_ | _Tự đánh giá..._ |

---

## 🧠 III. ALGORITHM & MATH CHEATSHEET (Spaced Repetition)

> 💡 **Notion Formula** cho cột `Cần Ôn?`:
> ```javascript
> if(empty(prop("Lần Ôn")), true, dateAdd(prop("Lần Ôn"), prop("Chu Kỳ"), "days") <= now())
> ```
> 💡 Chỉnh cột `Lần Ôn` $\rightarrow$ type **Date**, cột `Chu Kỳ` $\rightarrow$ type **Number**.

| Thuật Toán / Khái Niệm | Phân Loại | Hàm Mục Tiêu (Loss Function) | Cơ Chế Cập Nhật / Đạo Hàm | Siêu Tham Số (Hyperparams) | Confidence | Lần Ôn | Chu Kỳ | Cần Ôn? | Nhược Điểm |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **K-Means Clustering** | Unsupervised | WCSS / Inertia: $\sum \|x_i - \mu_j\|^2$ | (1) Gán cụm: $argmin \|x_i - \mu_k\|$ <br> (2) Cập nhật tâm: Trung bình cộng. | $K$ (số cụm) | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Bị ảnh hưởng bởi Outliers và khởi tạo ban đầu. |
| **Fuzzy C-Means (FCM)** | Unsupervised | $J_m = \sum \sum u_{ij}^m \|x_i - v_j\|^2$ | $u_{ij} = [ \sum (\frac{\|x_i - v_j\|}{\|x_i - v_k\|})^{\frac{2}{m-1}} ]^{-1}$ | $C$ (số cụm), $m$ (hệ số mờ > 1) | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Tính toán nặng hơn K-Means rất nhiều. |
| **PCA (Phân tích TP chính)** | Dimensionality Reduction | Maximize Variance / Minimize Projection Error | Phân tích giá trị riêng (Eigen Decomposition) của Ma trận Hiệp phương sai (Covariance Matrix). | $n\_components$ | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | Mất diễn giải vật lý (interpretability) của features. |
| **Linear Regression** | Supervised | MSE: $\frac{1}{2N} \sum (y_i - (wx_i + b))^2$ | Gradient Descent: $w := w - \alpha \frac{\partial J}{\partial w}$ | $\alpha$ (Learning Rate) | 🔴 Chưa thuộc | — | 1 | ⚠️ Cần ôn | Chỉ nắm bắt được quan hệ tuyến tính. |
| **Logistic Regression** | Supervised (Classify) | Binary Cross-Entropy (Log-Loss) | $w := w - \alpha \sum (h_\theta(x_i) - y_i)x_i$ | $\alpha$, Threshold (0.5) | 🔴 Chưa thuộc | — | 2 | ⚠️ Cần ôn | Không giải quyết được bài toán XOR. |
| _Template_ | _Select..._ | _Math formula..._ | _Update rule..._ | _Hyperparams..._ | 🔴 | _—_ | 1 | ⚠️ | _..._ |

---

## 💻 IV. ML CODE SNIPPET VAULT (Thư viện Code "Chống Cháy")

> Các đoạn code được đóng gói sẵn để tái sử dụng, tối ưu bằng NumPy (Vectorization) để tránh dùng vòng lặp `for`.

<details>
<summary><b>1️⃣ Tính khoảng cách Euclidean (NumPy Vectorized)</b></summary>

```python
import numpy as np

# Tính khoảng cách từ 1 điểm đến nhiều tâm cụm cùng lúc
def calculate_distances(X, centroids):
    """
    X: ma trận dữ liệu (N, d)
    centroids: ma trận tâm cụm (K, d)
    Returns: ma trận khoảng cách (N, K)
    """
    # Cách 1: Broadcasting (Nhanh và gọn nhất)
    # X[:, np.newaxis, :] có shape (N, 1, d)
    # centroids có shape (K, d) => (1, K, d) khi broadcast
    distances = np.linalg.norm(X[:, np.newaxis, :] - centroids, axis=2)
    return distances
```

</details>

<details>
<summary><b>2️⃣ Khởi tạo tâm cụm ngẫu nhiên (Random Initialization)</b></summary>

```python
def initialize_centroids(X, K):
    """
    Chọn ngẫu nhiên K điểm dữ liệu từ X làm tâm ban đầu.
    """
    np.random.seed(42) # Để kết quả có thể tái lập (reproducible)
    random_indices = np.random.choice(X.shape[0], K, replace=False)
    centroids = X[random_indices]
    return centroids
```

</details>

<details>
<summary><b>3️⃣ Hàm cập nhật tâm cụm (Mean Update)</b></summary>

```python
def update_centroids(X, labels, K):
    """
    Tính trung bình cộng các điểm trong cùng 1 cụm.
    """
    new_centroids = np.zeros((K, X.shape[1]))
    for k in range(K):
        # Lọc ra các điểm thuộc cụm k
        cluster_points = X[labels == k]
        # Xử lý trường hợp cụm rỗng (tránh chia cho 0)
        if len(cluster_points) > 0:
            new_centroids[k] = np.mean(cluster_points, axis=0)
    return new_centroids
```

</details>

<details>
<summary><b>4️⃣ Visualize với Matplotlib (Scatter Plot)</b></summary>

```python
import matplotlib.pyplot as plt

def plot_clusters(X, labels, centroids, title="Clustering Result"):
    plt.figure(figsize=(8, 6))
    
    # Vẽ các điểm dữ liệu, dùng cmap để tạo màu khác nhau cho các labels
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.6, s=50)
    
    # Vẽ tâm cụm (Dấu X màu đỏ)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
    
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    plt.show()
```

</details>

---

## 📝 V. QUICK NOTE & RESOURCES (Ghi chép nhanh)

- [ ] **Data Preprocessing**: Luôn nhớ scale dữ liệu (chuẩn hóa `StandardScaler` hoặc Min-Max) trước khi chạy thuật toán dùng khoảng cách như K-Means, SVM, KNN.
- [ ] **Curse of Dimensionality**: Dữ liệu có số chiều cao làm cho khoảng cách Euclidean mất đi ý nghĩa. Cần giảm chiều bằng PCA trước.
- [ ] **Overfitting vs Underfitting**: 
  - Overfitting: Thuộc lòng (High Variance) $\rightarrow$ Thêm data, Regularization (L1/L2), Dropout.
  - Underfitting: Học kém (High Bias) $\rightarrow$ Mô hình phức tạp hơn, thêm features.
