# 📜 ĐIỀU LỆ PHÒNG KỸ THUẬT, CODE & THỰC NGHIỆM (ENGINEERING LABS & CODE DEPT)
## Phòng 03 — Công Ty Trí Tuệ Nhân Tạo & Học Máy Cốt Lõi (CORP-02-ML)

> **Mã Phòng Ban:** `ML-DEPT-03`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (`HM-00`) & Giám Sát Kỹ Thuật (`SMS-02`)  
> **Cố vấn chuyên môn:** DUT Machine Learning Mentor (`AGENT_PROFILE.md`)  
> **Tiêu chuẩn chất lượng:** Scikit-Learn Pipeline / NumPy Vectorization / Zero Data Leakage / K-Fold Cross-Validation

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kỹ Thuật & Thực Nghiệm là **trung tâm toán học giải tích và mô hình hóa học máy**:
1. **Lập Trình Thuật Toán Từ Đầu (From Scratch)**: Tự cài đặt các thuật toán cốt lõi (Gradient Descent, Linear/Logistic Regression, K-Means, Fuzzy C-Means, SVM) bằng NumPy thuần túy để hiểu thấu đáo ma trận đạo hàm và hội tụ.
2. **Xây Dựng Sklearn Production Pipeline**: Đóng gói quy trình xử lý dữ liệu (Imputation $\rightarrow$ Scaling $\rightarrow$ Feature Selection $\rightarrow$ Estimator) bằng `sklearn.pipeline.Pipeline` ngăn chặn rò rỉ dữ liệu.
3. **Đánh Giá Mô Hình Toàn Diện**: So sánh hiệu năng giữa mô hình tuyến tính, mô hình cây (Random Forest, XGBoost, LightGBM) qua Stratified K-Fold và kiểm định thống kê.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (AGENT BẮT BUỘC TUÂN THỦ)

1. **Quy Tắc Vector Hóa Bằng NumPy (Vectorization Invariant)**:
   - **CẤM TUYỆT ĐỐI**: Sử dụng vòng lặp `for` của Python để tính toán khoảng cách Euclidean, nhân ma trận hoặc cập nhật trọng số Gradient Descent.
   - **BẮT BUỘC**: Sử dụng các phép toán mảng đa chiều của NumPy (`np.dot`, `np.linalg.norm`, Broadcasting) để tối ưu hóa tốc độ thực thi C-speed.
2. **Quy Tắc Chống Rò Rỉ Dữ Liệu (Zero Data Leakage Invariant)**:
   - **CẤM TUYỆT ĐỐI**: Gọi `fit()` hoặc `fit_transform()` của Scaler/Encoder trên toàn bộ tập dữ liệu trước khi chia `train_test_split()`.
   - **BẮT BUỘC**: Chỉ gọi `fit_transform()` trên Training Set, và chỉ dùng `transform()` trên Test Set / Validation Set.
3. **Quy Tắc Đánh Giá Dữ Liệu Mất Cân Bằng (Imbalanced Data Evaluation)**:
   - **CẤM TUYỆT ĐỐI**: Chỉ dùng một chỉ số Accuracy (Độ chính xác thô) để đánh giá mô hình phân loại khi các lớp mất cân bằng tỷ lệ.
   - **BẮT BUỘC**: Phải cung cấp đầy đủ: Confusion Matrix, Precision, Recall, F1-Score, và ROC-AUC / PR-AUC Curve.
4. **Quy Tắc Cố Định Ngẫu Nhiên (Random State Invariant)**:
   - Mọi phép chia tập dữ liệu hoặc khởi tạo thuật toán (KMeans, Train-Test Split, RandomForest) bắt buộc phải truyền `random_state=42`.

---

## 🛠️ 3. SKILLS ROUTE & TOOLCHAIN ĐIỀU HÀNH CHUẨN

### 3.1 Toolchain Yêu Cầu
- **Data Manipulation**: NumPy $\ge 1.24$, Pandas $\ge 2.0$, Polars.
- **Machine Learning Core**: Scikit-Learn $\ge 1.3$, SciPy, XGBoost, LightGBM.
- **Visualization**: Matplotlib, Seaborn.
- **Notebook & Environment**: JupyterLab, Python 3.10+.

### 3.2 Bộ Lệnh CLI Tác Nghiệp Chuẩn

```powershell
# 1. Chạy notebook kiểm thử tự động không cần mở giao diện trình duyệt
jupyter nbconvert --to notebook --execute --inplace Lab_01_KMeans_Flower/BT_Buoi3_KMeans_Flower.ipynb

# 2. Xuất báo cáo đồ thị và metrics sang file HTML sạch
jupyter nbconvert --to html --no-input Lab_01_KMeans_Flower/BT_Buoi3_KMeans_Flower.ipynb

# 3. Chạy script tối ưu hóa Hyperparameters với Optuna/GridSearch
python run_pipeline_optimization.py --cv 5 --scoring f1_macro
```

---

## 💻 4. MẪU KHUNG CODE / TEMPLATE CHUẨN NGHIỆP VỤ (GOLD MASTER SKLEARN PIPELINE)

Mẫu chuẩn mực **Pipeline tiền xử lý + Huấn luyện + Đánh giá chống Data Leakage**:

```python
"""
Scikit-Learn Master Pipeline Template - Tuân thủ Zero Data Leakage & K-Fold Validation
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


def build_robust_ml_pipeline(
    df: pd.DataFrame,
    target_column: str,
    numerical_cols: list[str],
    categorical_cols: list[str]
) -> None:
    # 1. Tách biệt Features và Target
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # 2. Phân chia Train/Test ngay từ đầu - BẢO VỆ CHỐNG DATA LEAKAGE
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Xây dựng bộ tiền xử lý chuyên biệt cho từng loại cột
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

    # 4. Đóng gói Model vào Pipeline duy nhất
    full_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42, max_depth=8))
    ])

    # 5. Đánh giá qua Stratified 5-Fold Cross Validation trên tập Train
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_results = cross_validate(
        full_pipeline, X_train, y_train, cv=cv,
        scoring=['accuracy', 'f1_macro', 'roc_auc_ovr'],
        return_train_score=False
    )

    print(f"CV F1-Macro Mean: {cv_results['test_f1_macro'].mean():.4f} +/- {cv_results['test_f1_macro'].std():.4f}")

    # 6. Fit trên toàn bộ Train và kiểm chứng trên Test Set biệt lập
    full_pipeline.fit(X_train, y_train)
    y_pred = full_pipeline.predict(X_test)

    print("\n--- BÁO CÁO ĐÁNH GIÁ TRÊN TEST SET ĐỘC LẬP ---")
    print(classification_report(y_test, y_pred, digits=4))
```

---

## 🛡️ 5. BỘ TIÊU CHÍ NGHIỆM THU CHẤT LƯỢNG (DEFINITION OF DONE - DoD)

- [ ] **DoD-1 (Zero Data Leakage)**: Không có phép tính thống kê nào (mean, median, scaling parameters) từ Test Set lọt vào Train Set.
- [ ] **DoD-2 (Vectorized Code)**: 100% các phép tính ma trận không dùng vòng lặp `for` lồng nhau.
- [ ] **DoD-3 (Generalization Verification)**: Chênh lệch F1-Score giữa Train và Test không vượt quá 5% (không bị Overfitting nặng).
- [ ] **DoD-4 (Visualized Results)**: Có đồ thị Confusion Matrix và biểu đồ ROC/PR curve minh chứng kết quả.

---

## 🚑 6. CẨM NANG XỬ LÝ SỰ CỐ HỌC MÁY (TOP 3 RUNBOOKS)

### 🚨 RUNBOOK 1: XỬ LÝ QUÁ KHỚP DỮ LIỆU (OVERFITTING TRIAGE)
* **Triệu chứng**: Điểm trên tập Train đạt 99% nhưng trên tập Test chỉ đạt 72%.
* **Kỹ thuật điều trị**:
  1. Thêm chuẩn hóa trọng số L1/L2 Regularization (ví dụ tăng tham số `C` hoặc `alpha`).
  2. Giảm độ sâu của cây (`max_depth=5` trong Decision Tree/Random Forest).
  3. Áp dụng Feature Selection (loại bỏ các biến tương quan cao hoặc biến nhiễu).

### 🚨 RUNBOOK 2: XỬ LÝ LỖI ĐA CỘNG TUYẾN (MULTICOLLINEARITY)
* **Triệu chứng**: Mô hình Linear Regression cho ra hệ số trọng số $\mathbf{w}$ quá lớn và dấu bị đảo ngược bất thường.
* **Khắc phục**: Tính toán Variance Inflation Factor (VIF). Nếu $\text{VIF} > 5$, loại bỏ một trong hai biến tương quan hoặc chuyển sang dùng Ridge/Lasso Regression.
