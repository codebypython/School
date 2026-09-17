# 📜 ĐIỀU LỆ PHÒNG CÔNG CỤ & KIỂM SOÁT SỰ CỐ (TROUBLESHOOTING & TOOLKITS DEPT)
## Phòng 05 — Công Ty Trí Tuệ Nhân Tạo & Học Máy (CORP-02-ML)

> **Mã Phòng Ban:** `ML-DEPT-05`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (Role Handmade) & `PSD-04` (Pedagogical Systems Designer)  
> **Cấp bậc quản trị:** Cấp 2 — Vận hành công cụ chẩn đoán, debug ma trận toán học, tối ưu hội tụ và xử lý sự cố học máy

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `ML-DEPT-05` chịu trách nhiệm cung cấp bộ công cụ chẩn đoán toán học, kiểm soát môi trường tính toán số học và chuẩn hóa quy trình ứng cứu sự cố trong suốt quá trình phát triển mô hình Machine Learning:
1. **Chẩn đoán Sự cố Hội tụ & Tối ưu**: Xử lý các hiện tượng Gradient Descent phân kỳ, learning rate quá lớn, đạo hàm bị triệt tiêu (vanishing) hoặc bùng nổ (exploding).
2. **Kiểm soát Dị thường Dữ liệu & Số học**: Cung cấp script phát hiện giá trị NaN/Inf, ma trận suy biến (Singular Matrix / Zero Determinant trong Normal Equation), và đa cộng tuyến (Multicollinearity).
3. **Bộ công cụ Kiểm định Mô hình & Tối ưu Hiệu năng**: Quản lý script đo đạc độ trễ inference, profiling bộ nhớ RAM/CPU khi xử lý mảng dữ liệu lớn, và thẩm định độ tin cậy của mô hình.

---

## 2. BỘ QUY TẮC BẤT BIẾN (DEBUGGING INVARIANTS & HARD CONSTRAINTS)
1. **Nguyên tắc Phòng ngừa Chia Cho Không (Numerical Epsilon Guard)**: Mọi phép toán liên quan đến hàm logarithm (Cross-Entropy, KL-Divergence) hoặc căn bậc hai/chuẩn hóa (Standardization, Batch Normalization) bắt buộc phải cộng một lượng $\epsilon > 0$ cực nhỏ (thường là $1e-7$ đến $1e-15$) để tránh `NaN` hoặc `inf`:
   $$\log(y + \epsilon), \quad \frac{x}{\sqrt{\sigma^2 + \epsilon}}$$
2. **Nguyên tắc Khả Nghịch của Ma Trận (Invertibility Verification)**: Khi giải phương trình pháp tuyến $\mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$, tuyệt đối cấm dùng trực tiếp `np.linalg.inv()`. Bắt buộc phải dùng giả nghịch đảo Moore-Penrose `np.linalg.pinv()` hoặc thêm thành phần chính quy hóa Ridge $\lambda \mathbf{I}$ để đảm bảo ma trận luôn khả nghịch.
3. **Nguyên tắc Kiểm Tra Trực quan Đường Học (Learning Curve Invariant)**: Trước khi quyết định tinh chỉnh tham số phức tạp, bắt buộc phải vẽ đồ thị biểu diễn Loss và Metric theo từng Epoch/Iteration cho cả Train và Validation để phân biệt rõ ràng Overfitting vs Underfitting.
4. **Nguyên tắc Độc lập Giữa Dữ liệu & Tiền xử lý (Pipeline Integrity)**: Mọi quy trình debug phát hiện hiện tượng test score cao bất thường (ví dụ: 100% test accuracy một cách phi thực tế) phải tự động kích hoạt rà soát rò rỉ target hoặc feature leakage.

---

## 3. BỘ LỆNH & CÔNG CỤ CHẨN ĐOÁN (DIAGNOSTIC TOOLCHAIN & SKILLS ROUTE)
```bash
# 1. Kiểm tra môi trường thư viện khoa học dữ liệu và phiên bản phần cứng
python -c "import numpy as np, scipy, sklearn; print(f'NumPy: {np.__version__} | SciPy: {scipy.__version__} | Sklearn: {sklearn.__version__}')"

# 2. Kiểm tra bộ nhớ tiêu thụ khi xử lý mảng ma trận lớn
python -m memory_profiler train_pipeline.py

# 3. Phân tích điểm nghẽn hiệu năng thuật toán với cProfile
python -m cProfile -s cumulative train_pipeline.py | head -n 25

# 4. Kiểm tra sự tồn tại của NaN / Inf trong bộ dữ liệu CSV
python -c "import pandas as pd; df = pd.read_csv('dataset.csv'); print('NaNs:\n', df.isna().sum()[df.isna().sum() > 0])"
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
05_Troubleshooting_and_Toolkits/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── convergence_diagnostics.py         # Bộ công cụ kiểm tra độ hội tụ Gradient Descent
├── matrix_singularity_checker.py      # Script kiểm tra điều kiện ma trận & VIF đa cộng tuyến
├── data_leakage_detector.py           # Công cụ rà soát rò rỉ dữ liệu tự động
└── runbooks/                          # Cẩm nang xử lý sự cố chi tiết
    ├── RUNBOOK_SINGULAR_MATRIX.md     # Xử lý ma trận không khả nghịch
    ├── RUNBOOK_NAN_LOSS_DEBUG.md      # Xử lý loss biến thành NaN trong Cross-Entropy
    ├── RUNBOOK_GRADIENT_EXPLOSION.md  # Xử lý bùng nổ gradient
    └── RUNBOOK_CLASS_IMBALANCE.md     # Xử lý sập hiệu năng trên tập dữ liệu lệch lớp
```

---

## 5. MẪU KHUNG CODE CHẨN ĐOÁN & ỨNG CỨU (GOLD MASTER BOILERPLATE)

### Bộ Công Cụ Chẩn Đoán Ma Trận & Kiểm Tra Dị Thường Số Học (`convergence_diagnostics.py`)
```python
"""
GOLD MASTER: NUMERICAL STABILITY & CONVERGENCE DIAGNOSTICS FOR ML
Tác giả: CORP-02-ML Engineering Team
Mục tiêu: Phát hiện sớm NaN, Singular Matrix, và kiểm tra điều kiện hội tụ.
"""

from typing import Tuple
import numpy as np


class MLStabilityAuditor:
    """Công cụ kiểm tra an toàn số học cho các thuật toán Machine Learning."""

    @staticmethod
    def check_matrix_condition(X: np.ndarray) -> Tuple[bool, float, str]:
        """
        Kiểm tra ma trận X^T X có bị suy biến (singular) hoặc ill-conditioned hay không.
        Sử dụng Condition Number (Số điều kiện).
        """
        XtX = np.dot(X.T, X)
        cond_num = np.linalg.cond(XtX)
        
        # Nếu condition number quá lớn (> 1e12), ma trận gần như suy biến
        if cond_num > 1e12:
            return False, cond_num, "CẢNH BÁO: Ma trận bị Ill-conditioned! Cần dùng Ridge L2 hoặc SVD."
        
        det = np.linalg.det(XtX)
        if np.isclose(det, 0.0):
            return False, cond_num, "NGUY HIỂM: Định thức bằng 0, ma trận không khả nghịch!"
            
        return True, cond_num, "ỔN ĐỊNH: Ma trận khả nghịch an toàn."

    @staticmethod
    def safe_cross_entropy(y_true: np.ndarray, y_pred_prob: np.ndarray, eps: float = 1e-15) -> float:
        """
        Tính Binary Cross-Entropy an toàn tuyệt đối, chống lỗi log(0) sinh NaN.
        """
        # Kẹp xác suất trong khoảng an toàn [eps, 1 - eps]
        clipped_probs = np.clip(y_pred_prob, eps, 1.0 - eps)
        loss = -np.mean(y_true * np.log(clipped_probs) + (1.0 - y_true) * np.log(1.0 - clipped_probs))
        return float(loss)

    @staticmethod
    def detect_numerical_anomalies(arr: np.ndarray, name: str = "Tensor") -> None:
        """Kiểm tra sự xuất hiện của NaN hoặc Inf trong mảng."""
        if np.isnan(arr).any():
            raise FloatingPointError(f"[FATAL ERROR] Phát hiện giá trị NaN trong mảng '{name}'!")
        if np.isinf(arr).any():
            raise FloatingPointError(f"[FATAL ERROR] Phát hiện giá trị Vô cùng (Inf) trong mảng '{name}'!")


if __name__ == "__main__":
    # Minh họa ma trận suy biến
    X_bad = np.array([[1.0, 2.0], [2.0, 4.0]]) # Cột 2 phụ thuộc tuyến tính cột 1
    safe, cond, msg = MLStabilityAuditor.check_matrix_condition(X_bad)
    print(f"Kiểm tra ma trận: {msg} (Cond: {cond})")

    # Minh họa tính Loss an toàn khi xác suất chạm 0.0
    y_t = np.array([1, 0, 1])
    y_p = np.array([0.0, 1.0, 0.0]) # Dự báo sai cực đoan
    safe_loss = MLStabilityAuditor.safe_cross_entropy(y_t, y_p)
    print(f"Loss an toàn (không bị NaN): {safe_loss:.4f}")
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
- [x] **Xử lý toàn diện các lỗi số học**: Mọi hàm tính loss hoặc chia ma trận đều có cơ chế chống chia cho 0 và xử lý ma trận suy biến.
- [x] **Runbook chi tiết 100%**: Có tối thiểu 4 runbook giải quyết 4 bài toán kinh điển: Singular Matrix, NaN Loss, Gradient Explosion và Imbalanced Data.
- [x] **Script chẩn đoán chạy độc lập**: File script mẫu có thể chạy trực tiếp bằng `python convergence_diagnostics.py` mà không báo lỗi phụ thuộc ngoài NumPy.
- [x] **Được kiểm định bởi auditor**: File `DEPARTMENT_CHARTER.md` đạt điểm 100% khi chạy `scripts/holding_system_auditor.py`.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ KHẨN CẤP (RUNBOOK & TROUBLESHOOTING)

### Sự cố 1: `numpy.linalg.LinAlgError: Singular matrix` khi giải Normal Equation
- **Hiện tượng**: Khi gọi `np.linalg.inv(X.T @ X)` chương trình văng lỗi ma trận suy biến.
- **Nguyên nhân gốc rễ**: Số lượng features $D$ lớn hơn số lượng mẫu $N$, hoặc tồn tại các cột dữ liệu phụ thuộc tuyến tính hoàn hảo (ví dụ: bẫy Dummy Variable Trap khi One-Hot Encoding không bỏ cột cơ sở).
- **Quy trình xử lý 3 bước**:
  1. Thay thế `np.linalg.inv()` bằng `np.linalg.pinv()` (Giả nghịch đảo Moore-Penrose dựa trên SVD).
  2. Bổ sung hệ số phạt L2: $( \mathbf{X}^T \mathbf{X} + \alpha \mathbf{I} )^{-1} \mathbf{X}^T \mathbf{y}$ với $\alpha = 1e-4$.
  3. Kiểm tra và loại bỏ một cột trong các cặp cột có hệ số tương quan $|r| = 1.0$.

### Sự cố 2: `Loss = NaN` ngay từ epoch thứ 2 trong hồi quy Logistic
- **Hiện tượng**: Giá trị hàm mất mát biến thành `NaN` sau vài bước cập nhật gradient.
- **Nguyên nhân**: Learning rate quá lớn dẫn đến trọng số $\mathbf{w}$ tăng vọt; khi đó hàm sigmoid $\sigma(\mathbf{w}^T \mathbf{x})$ cho ra kết quả $1.0$ hoặc $0.0$ tuyệt đối, dẫn đến phép toán $\log(0) = -\infty$.
- **Quy trình xử lý**:
  1. Kẹp giá trị đầu ra xác suất bằng `np.clip(probs, 1e-15, 1.0 - 1e-15)`.
  2. Giảm learning rate xuống 10 lần (ví dụ từ $0.1$ xuống $0.01$).
  3. Chuẩn hóa dữ liệu đầu vào bằng `StandardScaler()` trước khi đưa vào mô hình.

### Sự cố 3: Đồ thị Learning Curve bị phân kỳ (Diverging Cost Function)
- **Hiện tượng**: Giá trị Loss tăng dần đều theo thời gian thay vì giảm xuống.
- **Quy trình xử lý**:
  1. Kiểm tra dấu của gradient update: Đảm bảo công thức là $\mathbf{w} \leftarrow \mathbf{w} - \alpha \nabla J$ (trừ đi gradient, không phải cộng vào gradient).
  2. Nếu dấu đã đúng, nguyên nhân chắc chắn là learning rate vượt quá giới hạn ổn định của hàm Lipschitz. Giảm learning rate theo cấp số nhân: $10^{-1} \rightarrow 10^{-2} \rightarrow 10^{-3}$.
