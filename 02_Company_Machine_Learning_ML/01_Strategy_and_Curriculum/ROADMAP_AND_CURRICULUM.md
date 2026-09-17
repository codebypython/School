# 🧠 GIÁO TRÌNH & LỘ TRÌNH 15 TUẦN: HỌC MÁY VÀ ỨNG DỤNG
## Machine Learning & Practical Applications — DUT Standard Curriculum

> **Chuyên ngành:** Kỹ sư Công nghệ Thông tin — Đại học Bách khoa, ĐH Đà Nẵng (DUT)  
> **Đơn vị thiết kế:** Agent `PSD-04` (Pedagogical Scaffolding Designer)  
> **Nguồn đối chiếu Tier A+:** [Machine Learning Cơ Bản](file:///d:/User/7th/School/00_Corporate_Knowledge_Vault/EXTERNAL_KNOWLEDGE_VAULT.md#2--học-máy-và-ứng-dụng-machine-learning) (Vũ Hữu Tiệp), *PRML* (Christopher Bishop), *Hands-On ML 3rd ed* (Aurélien Géron), *CS229* (Andrew Ng).

---

## 🧭 TỔNG QUAN CHIẾN LƯỢC SƯ PHẠM 4 TẦNG

Mọi chủ đề trong giáo trình này đều được thiết kế nhất quán qua 4 tầng tiếp cận:
1. **Tầng 1: Bản chất Toán học & Hàm Mục tiêu (Why?)**: Chứng minh đạo hàm, hàm mất mát (loss function), và điều kiện tối ưu lồi từ gốc rễ.
2. **Tầng 2: Thuật toán & Mã nguồn From-Scratch (How?)**: Tự tay code thuật toán bằng thư viện `numpy` (không gọi thư viện đen) để thấu suốt luồng tính toán ma trận.
3. **Tầng 3: Ứng dụng Công nghiệp & Thư viện Sklearn (Production)**: Triển khai pipeline chuẩn với `scikit-learn`, tối ưu siêu tham số bằng `GridSearchCV`.
4. **Tầng 4: ⚠️ Lỗi phổ biến sinh viên hay gặp & Micro-quiz (Reflection)**: Cảnh báo bẫy dữ liệu, rò rỉ thông tin (data leakage) và câu hỏi phản biện bảo vệ.

---

## 📅 LỊCH TRÌNH 15 TUẦN CHI TIẾT

| Tuần | Chuyên Đề Trọng Tâm | Thuật Toán Cốt Lõi | Nguồn Đối Chiếu Tier A+ | Bài Tập Thực Chiến (Lab / Code) |
| :---: | :--- | :--- | :--- | :--- |
| **W1** | **Toán Học Cho ML & Tối Ưu Hóa** | Đạo hàm riêng, Ma trận Hessian, Gradient Descent, Momentum | Vũ Hữu Tiệp (Chương 1-2); Andrew Ng CS229 Note 1 | Code thuật toán Gradient Descent 1D & 2D bằng Numpy |
| **W2** | **Hồi Quy Tuyến Tính (Linear Regression)** | OLS (Ordinary Least Squares), L1 Lasso, L2 Ridge | Vũ Hữu Tiệp (Chương 3, 13); Géron (Chương 4) | Tự giải phương trình nghiệm giải tích $\mathbf{w} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$ |
| **W3** | **Hồi Quy Logistic & Softmax** | Cross-Entropy Loss, Sigmoid, Softmax Regression | Vũ Hữu Tiệp (Chương 10, 11); Bishop (Chương 4) | Code Logistic Regression nhị phân phân loại ung thư vú |
| **W4** | **Máy Vector Hỗ Trợ (SVM)** | Hard/Soft Margin, Dual Formulation, Kernel Trick (RBF) | Vũ Hữu Tiệp (Chương 19-22); Bishop (Chương 7) | Lập trình giải bài toán đối ngẫu SVM bằng thư viện `cvxopt` |
| **W5** | **Cây Quyết Định (Decision Trees)** | Information Gain, Gini Impurity, Thuật toán CART | Géron (Chương 6); Bishop (Chương 14.4) | Tự viết hàm tính Entropy và chia nhánh dữ liệu bằng Python |
| **W6** | **Ensemble Learning: Bagging** | Bootstrap Aggregating, Out-of-Bag (OOB) Error, Random Forest | Géron (Chương 7) | Xây dựng Random Forest từ các Decision Trees tự code |
| **W7** | **Ensemble Learning: Boosting** | AdaBoost, Gradient Boosting, XGBoost, LightGBM | Géron (Chương 7); Bishop (Chương 14.3) | Huấn luyện và tinh chỉnh XGBoost trên dữ liệu mất cân bằng |
| **W8** | **Đánh Giá Mô Hình & Đánh Giá Giữa Kỳ** | K-Fold CV, ROC-AUC, PR-Curve, Bias-Variance Tradeoff | Géron (Chương 2, 3); Bishop (Chương 1.3) | Viết hàm tự vẽ ROC-Curve và tính chỉ số AUC từ scratch |
| **W9** | **Phân Cụm 1: K-Means & Fuzzy C-Means** | K-Means++, Fuzzy Partition Matrix $U$, C-Means | Vũ Hữu Tiệp (Chương 4); Bishop (Chương 9.1) | **[Lab Buổi 3]**: Phân cụm hoa Iris & Phân vùng màu ảnh |
| **W10** | **Phân Cụm 2: GMM & Thuật Toán EM** | Gaussian Mixture Models, Thuật toán EM (E-step, M-step) | Bishop (Chương 9.2-9.4); Murphy ML | So sánh phân cụm hình elip giữa K-Means và GMM |
| **W11** | **Giảm Chiều: PCA & t-SNE** | Eigenvectors, Covariance Matrix, SVD, PCA, t-SNE | Vũ Hữu Tiệp (Chương 27); Géron (Chương 8) | Tự code PCA bằng Numpy; Trực quan hóa không gian 2D |
| **W12** | **Mạng Nơ-ron Nhân Tạo Cơ Bản (MLP)** | Perceptron, Multi-Layer Perceptron, Backpropagation | Vũ Hữu Tiệp (Chương 14-16); Goodfellow (Chương 6) | Tự tính đạo hàm Backpropagation bằng tay trên mạng 2 lớp |
| **W13** | **Feature Engineering & Pipeline Công Nghiệp**| One-Hot/Target Encoding, Imputation, Sklearn Pipeline | Géron (Chương 2) | Xây dựng hoàn chỉnh 1 Pipeline end-to-end có ColumnTransformer |
| **W14** | **Giải Thích Mô Hình Học Máy (XAI)** | Feature Importance, SHAP (Shapley values), LIME | Géron (Chương 7); Molnar (Interpretable ML) | Giải thích quyết định của mô hình Black-box bằng thư viện SHAP |
| **W15** | **Tổng Kết Học Phần & Báo Cáo Đồ Án Cuối Kỳ** | Tổng kết toàn diện, Bảo vệ Capstone Project | DUT Rubric Chuẩn (10 điểm) | Nghiệm thu báo cáo, đo lường chênh lệch Custom vs Sklearn |

---

## 🔬 CHI TIẾT TỪNG MODULE BÀI HỌC CỐT LÕI

### MODULE 1: NỀN TẢNG HỒI QUY & PHÂN LOẠI TUYẾN TÍNH (TUẦN 1 - 3)

#### 1. Bản chất Toán học (Mathematical Formalism)
- **Hồi quy Tuyến tính (Linear Regression)**:
  - Giả thiết mô hình: $\hat{y} = \mathbf{w}^T \mathbf{x} + b = \bar{\mathbf{w}}^T \bar{\mathbf{x}}$ (với $\bar{\mathbf{w}} = [b, \mathbf{w}]^T$, $\bar{\mathbf{x}} = [1, \mathbf{x}]^T$).
  - Hàm mất mát MSE (Mean Squared Error):
    $$\mathcal{L}(\mathbf{w}) = \frac{1}{2N} \|\mathbf{y} - \mathbf{X}\mathbf{w}\|_2^2$$
  - Đạo hàm theo trọng số $\mathbf{w}$:
    $$\frac{\partial \mathcal{L}}{\partial \mathbf{w}} = \frac{1}{N} \mathbf{X}^T (\mathbf{X}\mathbf{w} - \mathbf{y})$$
  - Nghiệm giải tích chính xác (Normal Equation): $\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$ (Điều kiện: $\mathbf{X}^T\mathbf{X}$ khả nghịch).
- **Hồi quy Logistic (Logistic Regression)**:
  - Hàm kích hoạt Sigmoid đưa giá trị về khoảng $(0, 1)$: $\sigma(z) = \frac{1}{1 + e^{-z}}$.
  - Xác suất hậu nghiệm: $P(y=1|\mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x})$.
  - Hàm mất mát Binary Cross-Entropy (từ nguyên lý MLE):
    $$\mathcal{L}_{BCE}(\mathbf{w}) = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]$$

#### 2. Code Mẫu From-Scratch (Numpy)
```python
import numpy as np

class CustomLinearRegression:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Gradient Descent Loop
        for _ in range(self.epochs):
            y_pred = np.dot(X, self.weights) + self.bias
            # Tính gradient
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)
            # Cập nhật tham số
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
```

#### 3. ⚠️ Lỗi Phổ Biến Sinh Viên Hay Gặp
1. **Quên chuẩn hóa dữ liệu (Feature Scaling) trước khi chạy Gradient Descent**: Nếu thuộc tính $X_1$ có giá trị hàng nghìn còn $X_2$ chỉ có giá trị thập phân, mặt phẳng hàm mất mát sẽ bị kéo giãn thành hình elip rất dẹt, khiến Gradient Descent dao động hình zigzag và hội tụ cực kỳ chậm. Luôn dùng `StandardScaler`!
2. **Nghịch đảo ma trận suy biến trong Normal Equation**: Khi số đặc trưng $d > N$ số mẫu, hoặc có 2 cột tương quan tuyến tính hoàn hảo (Multicollinearity), ma trận $\mathbf{X}^T\mathbf{X}$ không khả nghịch. Khắc phục: Dùng mã giả đảo `np.linalg.pinv` hoặc thêm số hạng điều chuẩn L2 (Ridge Regression).
3. **Hiểu nhầm Logistic Regression là bài toán hồi quy**: Tên có chữ "Regression" nhưng đây là thuật toán **Phân loại (Classification)**!

#### 4. 💡 Micro-quiz Phản Biện
> *"Tại sao trong Logistic Regression người ta không dùng hàm mất mát MSE mà bắt buộc phải dùng Binary Cross-Entropy?"*  
> **Gợi ý trả lời**: Nếu kết hợp hàm kích hoạt phi tuyến Sigmoid với hàm MSE, hàm mất mát sinh ra sẽ là hàm **không lồi (Non-convex)**, chứa rất nhiều điểm cực tiểu cục bộ (Local Minima), khiến Gradient Descent bị mắc kẹt. Binary Cross-Entropy đảm bảo hàm mất mát luôn là hàm lồi (Convex), chỉ có duy nhất một điểm cực tiểu toàn cục.

---

### MODULE 2: MÁY VECTOR HỖ TRỢ (SVM) & MÔ HÌNH CÂY (TUẦN 4 - 7)

#### 1. Bản chất Toán học (Mathematical Formalism)
- **SVM Tối ưu Biên Cực Đại (Maximum Margin)**:
  - Khoảng cách từ điểm dữ liệu gần nhất tới siêu phẳng: $\gamma = \frac{1}{\|\mathbf{w}\|_2}$.
  - Bài toán quy hoạch toàn phương nguyên thủy (Primal Problem):
    $$\min_{\mathbf{w}, b} \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^N \xi_i \quad \text{s.t.} \quad y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0$$
  - Bài toán đối ngẫu Lagrange (Dual Problem):
    $$\max_{\boldsymbol{\alpha}} \sum_{i=1}^N \alpha_i - \frac{1}{2} \sum_{i,j=1}^N \alpha_i \alpha_j y_i y_j K(\mathbf{x}_i, \mathbf{x}_j) \quad \text{s.t.} \quad 0 \le \alpha_i \le C, \quad \sum_{i=1}^N \alpha_i y_i = 0$$
  - Điểm hỗ trợ (Support Vectors): Là các điểm có $\alpha_i > 0$. Chỉ các điểm này mới quyết định vị trí siêu phẳng phân tách!
- **Cây Quyết Định (Decision Tree) & Tiêu chuẩn Phân nhánh**:
  - Gini Impurity: $I_G(D) = 1 - \sum_{i=1}^C p_i^2$.
  - Entropy & Information Gain:
    $$H(D) = -\sum_{i=1}^C p_i \log_2(p_i), \quad IG(D, A) = H(D) - \sum_{v \in Values(A)} \frac{|D_v|}{|D|} H(D_v)$$

#### 2. ⚠️ Lỗi Phổ Biến Sinh Viên Hay Gặp
1. **Để cây quyết định phát triển không giới hạn (Overfitting)**: Cây phân nhánh cho đến khi mọi lá đều có Gini = 0 $\rightarrow$ Học vẹt nhiễu của tập Train, khi Test thì độ chính xác giảm thảm hại. Luôn đặt `max_depth`, `min_samples_split`, hoặc dùng kỹ thuật Pruning!
2. **Không điều chỉnh tham số $C$ và $\gamma$ trong RBF Kernel SVM**: $C$ quá lớn $\rightarrow$ phạt lỗi quá nặng dẫn đến Overfit; $\gamma$ quá lớn $\rightarrow$ phạm vi ảnh hưởng của mỗi điểm quá hẹp, tạo ra các "hòn đảo" phân loại quanh từng điểm dữ liệu.

---

### MODULE 3: HỌC KHÔNG GIÁM SÁT — K-MEANS, C-MEANS & GIẢM CHIỀU (TUẦN 9 - 11)
*(Tích hợp trọn vẹn tài liệu Buổi 3 và Buổi 4 trong workspace của sinh viên)*

#### 1. Bản chất Toán học (Mathematical Formalism)
- **K-Means Clustering**:
  - Hàm mục tiêu méo mó (Distortion Function / Inertia):
    $$J(\mathbf{U}, \mathbf{M}) = \sum_{i=1}^N \sum_{k=1}^K u_{ik} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|_2^2 \quad \text{với} \quad u_{ik} \in \{0, 1\}, \sum_{k=1}^K u_{ik} = 1$$
  - Hai bước luân phiên:
    1. **Assignment (Gán cụm)**: $u_{ik} = 1$ nếu $k = \arg\min_j \|\mathbf{x}_i - \boldsymbol{\mu}_j\|_2^2$.
    2. **Update (Cập nhật tâm)**: $\boldsymbol{\mu}_k = \frac{\sum_{i=1}^N u_{ik} \mathbf{x}_i}{\sum_{i=1}^N u_{ik}}$.
- **Fuzzy C-Means (FCM - Phân cụm mờ)**:
  - Cho phép mỗi điểm thuộc về cụm với một độ thuộc (membership degree) $u_{ik} \in [0, 1]$:
    $$J_m = \sum_{i=1}^N \sum_{k=1}^C u_{ik}^m \|\mathbf{x}_i - \mathbf{c}_k\|^2 \quad (m > 1 \text{ là trọng số làm mờ - Fuzzifier})$$
  - Công thức cập nhật độ thuộc:
    $$u_{ik} = \frac{1}{\sum_{j=1}^C \left( \frac{\|\mathbf{x}_i - \mathbf{c}_k\|}{\|\mathbf{x}_i - \mathbf{c}_j\|} \right)^{\frac{2}{m - 1}}}$$

#### 2. Kết nối Lab Buổi 3 & Buổi 4 Của Sinh Viên
- **Buổi 3 (`BT_Buoi3_KMeans_Flower.ipynb`)**:
  - Phân cụm tập dữ liệu hoa dựa trên độ dài/rộng cánh hoa.
  - Vẽ đồ thị Elbow Method (Inertia giảm dần theo $K$) để chọn $K=3$ tối ưu.
- **Buổi 4 (`run_segmentation.py` & `102230023_NguyenTrungKien.ipynb`)**:
  - Phân vùng ảnh màu (Image Segmentation) bằng K-Means: Biến đổi ảnh từ shape $(H, W, 3)$ thành ma trận điểm ảnh $(H \times W, 3)$.
  - Thay thế màu của mỗi điểm ảnh bằng màu của tâm cụm tương ứng để nén dải màu và tách vật thể khỏi nền.

#### 3. ⚠️ Lỗi Phổ Biến Sinh Viên Hay Gặp
1. **Khởi tạo tâm cụm ngẫu nhiên dính Local Minima**: K-Means rất nhạy cảm với vị trí khởi tạo ban đầu. Luôn sử dụng thuật toán khởi tạo **K-Means++** (chọn tâm tiếp theo cách xa các tâm đã chọn với xác suất tỷ lệ với bình phương khoảng cách).
2. **K-Means thất bại trên cụm phi cầu hoặc cụm có mật độ khác nhau**: K-Means ngầm giả định các cụm có dạng hình cầu đồng nhất. Với dữ liệu dạng hình cung/hình trăng khuyết, phải dùng DBSCAN hoặc Spectral Clustering.

---

## 💻 NOTION INTEGRATION: BẢNG SO SÁNH CUSTOM VS SKLEARN

Để nhập vào Database Notion môn Học máy theo chuẩn [NOTION_ADVANCED_FORMULAS.md](file:///d:/User/7th/School/00_Central_Notion_LMS_Hub/NOTION_ADVANCED_FORMULAS.md#31-performance-delta-calculator-đo-lường-mức-độ-tối-ưu-thuật-toán):

| Thuật Toán | Tập Dữ Liệu | Số Vòng Lặp | Runtime Custom (ms) | Runtime Sklearn (ms) | Tốc Độ (Delta Formula) | Độ Khớp Kết Quả (%) |
| :--- | :--- | :---: | :---: | :---: | :--- | :---: |
| **Linear Regression** | Boston Housing (506 samples) | 1,000 | 12.4 | 1.8 | `🐢 Sklearn tối ưu hơn 10.6ms` | 99.98% |
| **Logistic Regression** | Breast Cancer (569 samples) | 500 | 28.6 | 4.2 | `🐢 Sklearn tối ưu hơn 24.4ms` | 99.12% |
| **K-Means Clustering** | Flower Dataset (150 samples) | 25 | 8.1 | 2.5 | `🐢 Sklearn tối ưu hơn 5.6ms` | 100.00% |
| **PCA (From Scratch)** | Iris (150 samples, 4 features) | Giải tích | 1.1 | 0.9 | `⚖️ Ngang bằng` | 100.00% |
