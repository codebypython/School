# ⚡ KẾ HOẠCH TÁC CHIẾN 4 TUẦN: CÔNG TY HỌC MÁY (COREAI SOLUTIONS)
## 4-Week Tactical Execution Plan — Machine Learning (ML)

> **Mã Doanh Nghiệp:** `CORP-02-ML`  
> **Cố vấn chuyên môn:** Giám Đốc Khoa Học Dữ Liệu (`PSD-04`)  
> **Người thực thi:** Kỹ Sư Trưởng Handmade (`HM-00` / Bạn)

---

## 🎯 MỤC TIÊU THÁNG 1
Làm chủ từ bản chất giải tích đạo hàm đến lập trình from-scratch bằng Numpy cho 4 thuật toán nền tảng: Gradient Descent, Hồi quy tuyến tính, Logistic Regression và SVM; liên kết đo đạc hiệu năng vào Notion Delta Log.

---

## 📅 LỘ TRÌNH CHI TIẾT TỪNG TUẦN

### Tuần 1: Giải Tích Tối Ưu Hóa & Thuật Toán Gradient Descent
- **Lý thuyết**: Đạo hàm riêng $\nabla f(\mathbf{x})$, Ma trận Hessian, Khái niệm hàm lồi (Convex function), Tốc độ học (Learning rate $\alpha$), Hiện tượng nổ gradient.
- **Thực hành (Lab)**:
  - Tự lập trình class `CustomOptimizer` cài đặt 3 thuật toán:
    1. Batch Gradient Descent (BGD).
    2. Stochastic Gradient Descent (SGD).
    3. Mini-batch Gradient Descent có tích hợp Momentum.
  - Vẽ đồ thị contour và quỹ đạo hội tụ trên hàm phi lồi Rosenbrock $f(x, y) = (1-x)^2 + 100(y-x^2)^2$.
- **Sản phẩm bàn giao**: Notebook `03_Engineering_Labs_and_Code/W1_Gradient_Descent_from_Scratch.ipynb`.
- **KPI nghiệm thu**: Thuật toán tìm được nghiệm cực tiểu toàn cục $(1, 1)$ với sai số $< 10^{-4}$.

---

### Tuần 2: Hồi Quy Tuyến Tính (Linear Regression) & Điều Chuẩn L1/L2
- **Lý thuyết**: Hàm mất mát MSE, Đạo hàm theo ma trận $\frac{\partial \mathcal{L}}{\partial \mathbf{w}}$, Nghiệm giải tích Normal Equation $\mathbf{w}^* = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$, Điều chuẩn Ridge (L2: $\lambda \|\mathbf{w}\|_2^2$) và Lasso (L1: $\lambda \|\mathbf{w}\|_1$).
- **Thực hành (Lab)**:
  - Tự viết class `CustomLinearRegression` và `CustomRidgeRegression` bằng Numpy.
  - Xử lý bài toán ma trận suy biến bằng mã giả đảo `np.linalg.pinv` hoặc SVD decomposition.
  - So sánh tốc độ chạy và MSE với `sklearn.linear_model.Ridge` trên tập dữ liệu Boston Housing.
- **Sản phẩm bàn giao**: Notebook `03_Engineering_Labs_and_Code/W2_Linear_and_Ridge_Regression.ipynb`.
- **KPI nghiệm thu**: Ghi nhận số liệu vào Notion `FROM-SCRATCH VS SKLEARN COMPARISON LOG`, công thức `Tốc độ (Delta)` tính toán chính xác.

---

### Tuần 3: Hồi Quy Logistic & Softmax Phân Loại Nhị Phân / Đa Lớp
- **Lý thuyết**: Hàm kích hoạt Sigmoid $\sigma(z) = \frac{1}{1+e^{-z}}$, Hàm mất mát Binary Cross-Entropy (BCE) chứng minh từ nguyên lý ước lượng hợp lý cực đại MLE, Ranh giới quyết định (Decision Boundary).
- **Thực hành (Lab)**:
  - Tự viết class `CustomLogisticRegression` bằng Numpy:
    - Hàm kích hoạt `_sigmoid(z)`.
    - Vòng lặp cập nhật trọng số theo BCE Loss Gradient.
    - Hàm dự đoán xác suất và nhãn nhị phân ($0$ hoặc $1$).
  - Huấn luyện trên tập dữ liệu ung thư vú `load_breast_cancer` của Scikit-Learn.
- **Sản phẩm bàn giao**: Notebook `03_Engineering_Labs_and_Code/W3_Logistic_Regression_Cancer.ipynb`.
- **KPI nghiệm thu**: Độ chính xác Test Accuracy $\ge 95\%$, vẽ được đường biên phân loại trực quan.

---

### Tuần 4: Máy Vector Hỗ Trợ (SVM) Tối Ưu Biên Cực Đại
- **Lý thuyết**: Khái niệm lề cực đại (Maximum Margin), Siêu phẳng phân tách $\mathbf{w}^T\mathbf{x}+b=0$, Bài toán tối ưu ràng buộc với nhân tử Lagrange, Điểm hỗ trợ (Support Vectors), Kernel Trick (RBF).
- **Thực hành (Lab)**:
  - Sử dụng thư viện giải bài toán quy hoạch lồi `cvxopt` để giải phương trình đối ngẫu Lagrange:
    $$\max_{\boldsymbol{\alpha}} \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j \mathbf{x}_i^T\mathbf{x}_j \quad \text{s.t.} \quad 0 \le \alpha_i \le C$$
  - Tìm ra các điểm có $\alpha_i > 10^{-4}$ (chính là Support Vectors), tính vector pháp tuyến $\mathbf{w}$ và hệ số chặn $b$.
- **Sản phẩm bàn giao**: Notebook `03_Engineering_Labs_and_Code/W4_Custom_SVM_Dual.ipynb`.
- **KPI nghiệm thu**: Tìm chính xác các điểm Support Vectors khớp với `sklearn.svm.SVC(kernel='linear')`.
