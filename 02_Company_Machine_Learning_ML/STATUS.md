# 📊 PROJECT STATUS DASHBOARD — CoreAI Corp (CORP-02-ML)

> **Cập nhật lần cuối**: 2026-09-13 | **Tuần hiện tại**: Tuần 1 (Linear Models & Optimization)  
> **Mentor chuyên trách**: DUT Machine Learning Mentor (`AGENT_PROFILE.md`)

---

## Current Phase: 🔵 PHASE 1 — MATHEMATICAL FOUNDATIONS & REGRESSION (Tuần 1-4)

Tập trung vào Đại số tuyến tính, Gradient Descent và Hồi quy tuyến tính từ Scratch.

---

## Implementation & Lab Progress

### Module 1: Hồi quy & Tối ưu hóa
- [x] Thiết lập môi trường Python 3.11, NumPy, Pandas, Scikit-Learn
- [x] Linear Regression Scratch (Nghịch đảo ma trận OLS: $w = (X^T X)^{-1} X^T y$)
- [ ] Gradient Descent (Batch GD, Stochastic GD, Mini-batch GD)
- [ ] Regularization L1 (Lasso) & L2 (Ridge)

### Module 2: Phân lớp & Cây quyết định
- [x] K-Nearest Neighbors (KNN) Scratch & Production Pipeline (Lab 03 - Exercise 01)
- [ ] Logistic Regression Scratch (Binary Cross-Entropy Loss)
- [ ] Softmax Regression cho Multi-class Classification
- [ ] Decision Tree & Random Forest Classifier

### Module 3: Nâng cao & Học không giám sát
- [x] K-Means Clustering Scratch & Image Segmentation (Lab 01 & Lab 02)
- [ ] Support Vector Machines (Linear & RBF Kernel)
- [ ] PCA giảm chiều dữ liệu
- [ ] Ensemble XGBoost & LightGBM Pipeline

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | Cần chuẩn bị dataset bài tập thực hành tuần 2 (Boston / California Housing) | 🟡 Medium | Sẵn sàng trong `data/` |

---

## Last Session
- **Date**: 2026-09-18
- **Work Done**: Hoàn thành toàn diện bộ bài tập Lab 03 KNN (Exercise 01: Câu a, b, c), chuẩn hóa tài liệu theo format chuẩn Lab 01 & Lab 02 gồm `run_knn.py`, `build_notebook.py`, `BT_Buoi5_KNN.ipynb` (nhúng Base64), `102230023_NguyenTrungKien.ipynb`, `README.md` và các biểu đồ `results/`.
- **Next Priority (P0)**: Hoàn thành bài Lab so sánh tốc độ hội tụ giữa Batch Gradient Descent và Stochastic Gradient Descent trên dữ liệu tổng hợp.
