# 📜 ĐIỀU LỆ PHÒNG CHIẾN LƯỢC & GIÁO TRÌNH 15 TUẦN (STRATEGY & CURRICULUM DEPT)
## Phòng 01 — Công Ty Trí Tuệ Nhân Tạo & Học Máy (CORP-02-ML)

> **Mã Phòng Ban:** `ML-DEPT-01`  
> **Trưởng phòng phụ trách:** Agent `PSD-04` (Pedagogical Scaffolding Designer) & Giám Đốc Đào Tạo  
> **Cấp bậc quản trị:** Cấp 1 — Định hình triết lý đào tạo, khung chương trình 15 tuần chuẩn DUT & quy chuẩn toán học Machine Learning

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `ML-DEPT-01` chịu trách nhiệm toàn diện về cấu trúc học thuật, thiết kế sư phạm và lộ trình đào tạo 15 tuần môn Học Máy (Machine Learning) theo chuẩn Đại học Bách Khoa - ĐH Đà Nẵng:
1. **Thiết kế lộ trình học tập 4 tầng chuẩn mực**: Mỗi chủ đề thuật toán bắt buộc phải trải qua 4 tầng nhận thức: `Toán học & Cơ sở tối ưu (Loss, Gradient)` $\rightarrow$ `Hiện thực From-Scratch bằng NumPy vectorization` $\rightarrow$ `Hiện thực công nghiệp Scikit-Learn/XGBoost Pipeline` $\rightarrow$ `Đánh giá định lượng & Tránh bẫy Data Leakage`.
2. **Kiểm soát tính chặt chẽ về toán học**: Mọi thuật toán phải có diễn giải đạo hàm, ma trận Hessian (nếu có), điều kiện hội tụ KKT trong SVM, hoặc cơ chế phân tách entropy/Gini trong Decision Trees.
3. **Cân đối giữa Supervised, Unsupervised và Ensemble Learning**: Đảm bảo sinh viên thành thạo từ các mô hình tuyến tính (Linear/Logistic Regression, Ridge/Lasso), mô hình phi tuyến (Kernel SVM, KNN, Random Forest, Gradient Boosting), đến các kỹ thuật giảm chiều dữ liệu (PCA, t-SNE) và gom cụm (K-Means, GMM, DBSCAN).

---

## 2. BỘ QUY TẮC BẤT BIẾN (CURATION INVARIANTS & HARD CONSTRAINTS)
Mọi tài liệu, giáo trình và bài giảng do `ML-DEPT-01` ban hành bắt buộc tuân thủ 5 nguyên tắc bất biến:
1. **Nguyên tắc "Cấm Mớm Lời Giải Một Bước" (Scaffolding Invariant)**: Không bao giờ cung cấp code hoàn chỉnh ngay lập tức khi học viên gặp vướng mắc. Phải dẫn dắt từ trực giác hình học, công thức mất mát (Objective Function), rồi mới đến gradient update.
2. **Nguyên tắc Vectorization Tuyệt đối (No Explicit For-Loops over Samples)**: Trong mọi bài giảng from-scratch bằng NumPy, cấm tuyệt đối sử dụng vòng lặp `for` chạy qua $N$ mẫu dữ liệu để tính toán prediction hoặc gradient. Mọi phép toán bắt buộc phải biểu diễn dưới dạng ma trận $\mathbf{X} \mathbf{w}$ hoặc broadcasting.
3. **Nguyên tắc Chống Rò Rỉ Dữ Liệu (Zero Data Leakage Invariant)**: Mọi thao tác tiền xử lý (StandardScaler, OneHotEncoder, Imputer, PCA) bắt buộc phải tuân theo quy tắc: `fit` chỉ trên tập Train, `transform` trên cả Train và Test/Validation. Nghiêm cấm `fit_transform` trên toàn bộ tập dữ liệu trước khi train_test_split.
4. **Nguyên tắc Metric Đánh Giá Phù Hợp Ngữ Cảnh (Contextual Metric Rule)**: Đối với bài toán mất cân bằng dữ liệu (Imbalanced Data), cấm sử dụng `Accuracy` làm chỉ số chính; bắt buộc phải sử dụng `PR-AUC`, `ROC-AUC`, `Balanced Accuracy` hoặc `F1-Score` kèm Confusion Matrix.
5. **Nguyên tắc Độc lập & Tái lập Kết quả (Reproducibility Rule)**: Mọi thuật toán có tính ngẫu nhiên (kết nạp mẫu, khởi tạo centroid K-Means, bootstrap Random Forest) bắt buộc phải cấu hình `random_state` rõ ràng.

---

## 3. MA TRẬN PHÂN BỔ NĂNG LỰC 15 TUẦN (TOOLCHAIN & SKILLS ROUTE)
```
Tuần 01-02: Đại số tuyến tính, Giải tích đa biến, Xác suất thống kê & NumPy Vectorization.
Tuần 03-04: Linear Regression (OLS, Normal Equation, Batch/Stochastic/Mini-batch GD).
Tuần 05:    Regularization (L1 Lasso, L2 Ridge, ElasticNet) & Trade-off Bias-Variance.
Tuần 06-07: Logistic Regression, Softmax Regression & Tối ưu hàm mất mát Cross-Entropy.
Tuần 08:    Support Vector Machines (Linear SVM, Dual Formulation, Kernel Trick, Soft-Margin).
Tuần 09-10: Decision Trees (ID3, C4.5, CART) & Ensemble Learning (Bagging, Random Forest, AdaBoost, XGBoost).
Tuần 11:    Unsupervised Learning: K-Means, K-Means++, Hierarchical Clustering, DBSCAN.
Tuần 12:    Dimensionality Reduction: PCA (SVD, Eigenvalues), t-SNE, Feature Selection.
Tuần 13:    Evaluation Metrics, Hyperparameter Tuning (GridSearch, Optuna, Stratified K-Fold).
Tuần 14:    End-to-end ML Pipeline, ColumnTransformer & Chống rò rỉ dữ liệu công nghiệp.
Tuần 15:    Giới thiệu Neural Networks (Perceptron, Multi-Layer Perceptron, Backpropagation) & Tổng kết đồ án.
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
01_Strategy_and_Curriculum/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── AGENT_PROFILE.md                   # Hồ sơ Mentor Học thuật ML DUT
├── ROADMAP_AND_CURRICULUM.md          # Khung chương trình 15 tuần chi tiết kèm công thức toán
├── MATH_FOUNDATIONS_SURVIVAL_KIT.md   # Cẩm nang đại số tuyến tính & giải tích vi phân cho ML
└── EVALUATION_RUBRIC_DUT.md           # Barem chấm điểm đồ án và bài thi chuẩn ĐHBK Đà Nẵng
```

---

## 5. MẪU KHUNG CODE THUẬT TOÁN CHUẨN MỰC (GOLD MASTER BOILERPLATE)

### Bộ Lớp Huấn Luyện Tuyến Tính From-Scratch Chuẩn Vector Hóa (`LinearRegressionScratch`)
```python
"""
GOLD MASTER: NUMPY FROM-SCRATCH LINEAR REGRESSION (VECTORIZED)
Tác giả: CORP-02-ML Strategy & Pedagogical Team
Mục tiêu: Mẫu hiện thực chuẩn không dùng for-loop, hỗ trợ L2 Regularization (Ridge).
"""

from typing import Optional
import numpy as np


class RidgeRegressionScratch:
    """Hiện thực Ridge Regression thuần NumPy bằng Gradient Descent vector hóa hoàn toàn."""

    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000, alpha: float = 1.0):
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.alpha = alpha  # Hệ số phạt L2 Regularization
        self.weights: Optional[np.ndarray] = None
        self.bias: float = 0.0
        self.loss_history: list[float] = []

    def fit(self, X: np.ndarray, y: np.ndarray) -> "RidgeRegressionScratch":
        """Huấn luyện mô hình thông qua gradient descent vector hóa."""
        n_samples, n_features = X.shape
        # Khởi tạo trọng số
        self.weights = np.zeros(n_features)
        self.bias = 0.0
        self.loss_history = []

        for _ in range(self.n_iterations):
            # Tầng 1: Tính dự báo qua ma trận (No For-Loops)
            y_predicted = np.dot(X, self.weights) + self.bias
            error = y_predicted - y

            # Tầng 2: Tính hàm mất mát MSE + L2 Penalty
            mse_loss = (1 / (2 * n_samples)) * np.sum(error ** 2)
            l2_penalty = (self.alpha / (2 * n_samples)) * np.sum(self.weights ** 2)
            self.loss_history.append(mse_loss + l2_penalty)

            # Tầng 3: Tính đạo hàm riêng (Gradients)
            dw = (1 / n_samples) * (np.dot(X.T, error) + self.alpha * self.weights)
            db = (1 / n_samples) * np.sum(error)

            # Tầng 4: Cập nhật trọng số
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Dự báo kết quả cho tập dữ liệu mới."""
        if self.weights is None:
            raise ValueError("Mô hình chưa được fit dữ liệu!")
        return np.dot(X, self.weights) + self.bias
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
Một tuần học hoặc học liệu do `ML-DEPT-01` phát hành chỉ đạt chuẩn khi thỏa mãn 4 tiêu chí:
- [x] **Tính đầy đủ về công thức toán**: Mọi bài học thuật toán đều có công thức hàm mục tiêu $J(\mathbf{w})$, đạo hàm riêng $\nabla_{\mathbf{w}} J(\mathbf{w})$, và quy tắc cập nhật tham số.
- [x] **Hai phiên bản code song hành**: Phải có song song bản NumPy From-Scratch để hiểu bản chất và bản Scikit-Learn Pipeline tương ứng để sử dụng thực tế.
- [x] **Cảnh báo lỗi và cạm bẫy**: Mỗi bài học có tối thiểu 2 cảnh báo cạm bẫy kinh điển (ví dụ: bẫy dữ liệu chưa chuẩn hóa trước KNN/SVM, bẫy rò rỉ target encoding).
- [x] **Xác thực tự động bởi Auditor**: Toàn bộ liên kết trong tài liệu hợp lệ 100%, không sinh link gãy.

---

## 7. CẨM NANG KHẮC PHỤC SỰ CỐ SƯ PHẠM (PEDAGOGICAL RUNBOOK)

### Sự cố 1: Sinh viên bị "choáng ngợp toán" (Math Anxiety) ở các tuần đầu
- **Nguyên nhân**: Kiến thức đại số tuyến tính và giải tích vi phân bị hổng, không hình dung được ý nghĩa hình học của gradient.
- **Quy trình xử lý**:
  1. Kích hoạt trực quan hóa 2D/3D: Sử dụng biểu đồ đường đồng mức (Contour Plots) minh họa quá trình Gradient Descent trượt dốc trên mặt cong mất mát hình chén (Convex Bowl).
  2. Bắt đầu từ trường hợp đơn biến: Giải thích đạo hàm cấp 1 với hàm bậc hai $f(w) = w^2 - 4w + 5$ trước khi mở rộng lên đa biến dạng vector $\nabla_{\mathbf{w}} J(\mathbf{w})$.

### Sự cố 2: Lầm tưởng Accuracy cao đồng nghĩa mô hình tốt (Accuracy Paradox)
- **Nguyên nhân**: Bộ dữ liệu mất cân bằng nghiêm trọng (99% âm tính, 1% dương tính); mô hình chỉ cần dự báo toàn âm tính cũng đạt 99% accuracy.
- **Quy trình xử lý**:
  1. Hướng dẫn sinh viên vẽ ma trận nhầm lẫn (Confusion Matrix) với 4 giá trị TP, FP, TN, FN.
  2. Yêu cầu đo đạc `Precision`, `Recall`, và `F1-Score` hoặc `AUC-ROC`.
  3. Áp dụng kỹ thuật cân bằng mẫu: SMOTE oversampling hoặc thiết lập trọng số lớp `class_weight='balanced'` trong Scikit-Learn.
