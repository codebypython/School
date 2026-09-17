"""
BÀI TẬP BUỔI 4: PHÂN ĐOẠN HÌNH ẢNH (IMAGE SEGMENTATION)
MÔN: HỌC MÁY VÀ ỨNG DỤNG HỌC MÁY

Trọng tâm bài làm (Tinh thần tự học & Tư duy thuật toán của sinh viên):
  1. Tự xây dựng hàm Custom K-Means từ đầu và SO SÁNH trực tiếp với thư viện Scikit-Learn.
  2. Tự xây dựng hàm Custom Fuzzy C-Means (FCM) từ đầu để thực hiện phân cụm mềm.
  3. Tính toán chi tiết ma trận xác suất độ thuộc (% từng cụm) của từng điểm ảnh.
  4. Phân tích điều kiện e > 50% (ngưỡng đa số tuyệt đối) để tách biệt vùng chắc chắn và vùng ranh giới mờ.
  5. Đúc kết nhận xét đối chiếu giữa hàm tự viết (custom) và hàm thư viện có sẵn.
"""

import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Cấu hình phong cách hiển thị
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'sans-serif']
plt.rcParams['figure.dpi'] = 150

base_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(base_dir, 'results')
os.makedirs(results_dir, exist_ok=True)

img_path = os.path.join(base_dir, 'sample_image.jpg')
if not os.path.exists(img_path):
    raise FileNotFoundError(f"Không tìm thấy file ảnh: {img_path}")

print("=" * 75)
print("BÀI TẬP BUỔI 4: TỰ XÂY DỰNG HÀM PHÂN ĐOẠN ẢNH VÀ SO SÁNH VỚI THƯ VIỆN")
print("=" * 75)

# =========================================================================
# BƯỚC 1: ĐỌC VÀ TIỀN XỬ LÝ ẢNH
# =========================================================================
print("\n[+] BƯỚC 1: Đọc và tiền xử lý ảnh đầu vào...")
pil_img = Image.open(img_path).convert('RGB')
img_rgb = np.array(pil_img)
H, W, C = img_rgb.shape
print(f" - Kích thước ảnh: {H} x {W} pixels ({C} kênh màu RGB)")
print(f" - Tổng số điểm ảnh (N): {H * W} mẫu dữ liệu")

# Chuẩn hóa về [0, 1] và duỗi thành (N, 3)
X = img_rgb.reshape(-1, 3).astype(np.float32) / 255.0
print(f" - Kích thước ma trận đặc trưng X: {X.shape[0]} mẫu x {X.shape[1]} đặc trưng (R, G, B)")

# Lưu ảnh gốc
plt.figure(figsize=(5, 5))
plt.imshow(img_rgb)
plt.title(f"Ảnh gốc đầu vào ({H}x{W})", fontsize=12, fontweight='bold', pad=10)
plt.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(results_dir, '01_original_image.png'), bbox_inches='tight')
plt.close()

# =========================================================================
# BƯỚC 2: TỰ XÂY DỰNG HÀM CUSTOM K-MEANS VÀ SO SÁNH VỚI SCIKIT-LEARN
# =========================================================================
print("\n[+] BƯỚC 2: Xây dựng hàm Custom K-Means & So sánh với Scikit-Learn...")

def custom_kmeans(X, k=4, max_iter=100, tol=1e-4, seed=42):
    """
    HÀM CUSTOM K-MEANS DO SINH VIÊN TỰ XÂY DỰNG TỪ ĐẦU (FROM SCRATCH):
    Tư duy giải quyết bài toán:
      1. Khởi tạo ngẫu nhiên k tâm cụm từ tập dữ liệu.
      2. Bước E (Expectation): Tính khoảng cách Euclidean từ mỗi điểm tới k tâm,
         gán điểm đó vào tâm gần nhất (argmin).
      3. Bước M (Maximization): Cập nhật tâm mới bằng trung bình cộng tọa độ (mean).
      4. Kiểm tra điều kiện dừng: nếu tâm cụm dịch chuyển nhỏ hơn ngưỡng tol thì dừng.
    """
    np.random.seed(seed)
    N, D = X.shape
    
    # 1. Khởi tạo k tâm cụm ngẫu nhiên
    init_idx = np.random.choice(N, k, replace=False)
    centroids = X[init_idx].copy()
    
    for it in range(max_iter):
        # 2. Tính khoảng cách Euclidean: khoảng cách giữa X (N, 3) và centroids (k, 3)
        # Sử dụng NumPy broadcasting: (N, 1, 3) - (1, k, 3) -> (N, k, 3)
        distances = np.linalg.norm(X[:, np.newaxis, :] - centroids[np.newaxis, :, :], axis=2)
        
        # Gán cụm: chọn cụm có khoảng cách nhỏ nhất
        labels = np.argmin(distances, axis=1)
        
        # 3. Cập nhật tâm cụm mới bằng trung bình cộng các điểm trong cụm
        new_centroids = np.array([
            X[labels == j].mean(axis=0) if np.sum(labels == j) > 0 else centroids[j]
            for j in range(k)
        ])
        
        # 4. Kiểm tra hội tụ (độ dịch chuyển của tâm cụm)
        shift = np.linalg.norm(new_centroids - centroids)
        centroids = new_centroids
        if shift < tol:
            it_converged = it + 1
            break
    else:
        it_converged = max_iter

    # Tính tổng bình phương sai số nội cụm WCSS (Inertia)
    wcss = np.sum((X - centroids[labels]) ** 2)
    return centroids, labels, it_converged, wcss

# 1. Chạy hàm Custom K-Means
K = 4
t0 = time.time()
custom_centers, custom_labels, custom_iters, custom_wcss = custom_kmeans(X, k=K, max_iter=100, seed=42)
time_custom = time.time() - t0

# 2. Chạy thư viện Scikit-Learn KMeans
t0 = time.time()
sk_kmeans = KMeans(n_clusters=K, random_state=42, n_init=10, max_iter=300)
sk_labels = sk_kmeans.fit_predict(X)
time_sklearn = time.time() - t0
sk_centers = sk_kmeans.cluster_centers_
sk_iters = sk_kmeans.n_iter_
sk_wcss = sk_kmeans.inertia_

# 3. In bảng so sánh trực tiếp giữa Custom và Thư viện
print("\n--- BẢNG ĐỐI CHIẾU: HÀM CUSTOM K-MEANS vs THƯ VIỆN SCIKIT-LEARN ---")
print(f"{'Tiêu chí so sánh':<32} | {'Hàm Custom tự viết':<20} | {'Thư viện Scikit-Learn':<20}")
print("-" * 78)
print(f"{'Thời gian thực thi (Runtime)':<32} | {time_custom*1000:16.2f} ms | {time_sklearn*1000:16.2f} ms")
print(f"{'Số vòng lặp hội tụ':<32} | {custom_iters:17d}  | {sk_iters:17d}")
print(f"{'Quán tính nội cụm (WCSS / Inertia)':<32} | {custom_wcss:17.2f}  | {sk_wcss:17.2f}")
print("-" * 78)

# Tái tạo ảnh phân đoạn từ 2 phương pháp
custom_seg_img = (custom_centers[custom_labels].reshape(H, W, 3) * 255).astype(np.uint8)
sk_seg_img = (sk_centers[sk_labels].reshape(H, W, 3) * 255).astype(np.uint8)

# Vẽ đồ thị so sánh Custom K-Means vs Sklearn K-Means
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
ax1.imshow(custom_seg_img)
ax1.set_title(f"A. Phân đoạn bằng hàm Custom K-Means\n(WCSS={custom_wcss:.1f}, {custom_iters} vòng lặp)", fontsize=11, fontweight='bold', pad=10)
ax1.axis('off')

ax2.imshow(sk_seg_img)
ax2.set_title(f"B. Phân đoạn bằng thư viện Scikit-Learn\n(Inertia={sk_wcss:.1f}, {sk_iters} vòng lặp)", fontsize=11, fontweight='bold', pad=10)
ax2.axis('off')

plt.suptitle("SO SÁNH KẾT QUẢ PHÂN ĐOẠN: CUSTOM K-MEANS vs SCIKIT-LEARN", fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(results_dir, '02_compare_custom_vs_sklearn_kmeans.png'), bbox_inches='tight')
plt.close()

# =========================================================================
# BƯỚC 3: TỰ XÂY DỰNG HÀM CUSTOM FUZZY C-MEANS (FCM)
# =========================================================================
print("\n[+] BƯỚC 3: Xây dựng hàm Custom Fuzzy C-Means (C = 4, m = 2.0)...")

def custom_fuzzy_c_means(X, c=4, m=2.0, max_iter=100, tol=1e-4, seed=42):
    """
    HÀM CUSTOM FUZZY C-MEANS (FCM) DO SINH VIÊN TỰ XÂY DỰNG:
    Tư duy giải quyết bài toán:
      1. Khởi tạo ngẫu nhiên ma trận độ thuộc U kích thước (c, N) sao cho tổng mỗi cột bằng 1.0 (100%).
      2. Cập nhật tâm cụm bằng trung bình có trọng số mũ m:
         V_j = (sum_i u_ij^m * x_i) / (sum_i u_ij^m)
      3. Tính ma trận khoảng cách Euclidean từ mỗi pixel tới c tâm: d_ij = ||x_i - V_j||.
      4. Cập nhật ma trận độ thuộc theo công thức mờ:
         u_ij = 1 / sum_k (d_ij / d_ik)^(2/(m-1))
      5. Kiểm tra hội tụ: max|U_new - U_old| < tol.
    """
    N, D = X.shape
    np.random.seed(seed)
    
    # 1. Khởi tạo ma trận độ thuộc ngẫu nhiên (c, N) bằng phân phối Dirichlet
    U = np.random.dirichlet(np.ones(c), size=N).T
    
    for it in range(max_iter):
        U_old = U.copy()
        
        # 2. Cập nhật tâm cụm có trọng số mờ mũ m
        U_m = U ** m  # Shape: (c, N)
        centroids = (U_m @ X) / (U_m.sum(axis=1)[:, np.newaxis])  # Shape: (c, D)
        
        # 3. Tính khoảng cách Euclidean
        distances = np.linalg.norm(X[np.newaxis, :, :] - centroids[:, np.newaxis, :], axis=2)
        distances = np.fmax(distances, 1e-10)  # Tránh chia cho 0
        
        # 4. Cập nhật độ thuộc mờ
        inv_dist = 1.0 / (distances ** (2.0 / (m - 1.0)))
        U = inv_dist / np.sum(inv_dist, axis=0, keepdims=True)
        
        # 5. Kiểm tra hội tụ
        delta = np.max(np.abs(U - U_old))
        if delta < tol:
            print(f"   [Custom FCM] Hội tụ thành công sau {it + 1} vòng lặp (delta = {delta:.6f})")
            break
    else:
        print(f"   [Custom FCM] Dừng sau tối đa {max_iter} vòng lặp.")
        
    return centroids, U

t0 = time.time()
fcm_centers, U_fcm = custom_fuzzy_c_means(X, c=K, m=2.0, max_iter=100, tol=1e-4, seed=42)
time_fcm = time.time() - t0

# Chuyển U_fcm về dạng (N, c) để mỗi hàng tương ứng với 1 pixel
membership = U_fcm.T  # Shape: (N, 4)

# Khử mờ (Defuzzification) để tái tạo ảnh: gán mỗi pixel về cụm có độ thuộc lớn nhất (argmax)
fcm_dominant_labels = np.argmax(membership, axis=1)
fcm_seg_img = (fcm_centers[fcm_dominant_labels].reshape(H, W, 3) * 255).astype(np.uint8)

# Lưu ảnh FCM
plt.figure(figsize=(5, 5))
plt.imshow(fcm_seg_img)
plt.title(f"Phân đoạn Fuzzy C-Means (C = {K} cụm mềm khử về argmax)", fontsize=11, fontweight='bold', pad=10)
plt.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(results_dir, '03_fcm_segmentation.png'), bbox_inches='tight')
plt.close()

# =========================================================================
# BƯỚC 4: TÍNH % ĐỘ THUỘC & PHÂN TÍCH NGƯỠNG ĐỘ THUỘC e > 50%
# =========================================================================
print("\n[+] BƯỚC 4: Tính % độ thuộc và Phân tích ngưỡng e > 50%...")

# 1. Bảng minh họa chi tiết cho các điểm ảnh đại diện
sample_indices = [
    H // 4 * W + W // 4,       # Vùng nền sáng
    H // 2 * W + W // 2,       # Vùng quả táo đỏ
    H // 5 * W + int(W * 0.7), # Vùng lá xanh
    int(H * 0.8) * W + W // 2, # Vùng mặt bàn gỗ
    int(H * 0.45) * W + int(W * 0.3), # Ranh giới quả táo - phông nền
]
sample_names = ["Góc nền trên-trái", "Thân quả táo (Đỏ)", "Lá cây (Xanh)", "Mặt bàn gỗ", "Ranh giới quả táo - nền"]

print("\n--- BẢNG MINH HỌA XÁC SUẤT ĐỘ THUỘC (%) CỦA CÁC ĐIỂM ẢNH ĐẠI DIỆN ---")
print(f"{'Điểm ảnh đại diện':<26} | {'Cụm 1 (%)':<10} | {'Cụm 2 (%)':<10} | {'Cụm 3 (%)':<10} | {'Cụm 4 (%)':<10} | {'Tổng (%)':<8} | {'Phân loại'}")
print("-" * 105)

for name, idx in zip(sample_names, sample_indices):
    probs = membership[idx] * 100
    max_p = np.max(probs)
    status = "Chắc chắn (e > 50%)" if max_p > 50.0 else "Ranh giới mờ (e <= 50%)"
    print(f"{name:<26} | {probs[0]:9.2f}% | {probs[1]:9.2f}% | {probs[2]:9.2f}% | {probs[3]:9.2f}% | {np.sum(probs):7.2f}% | {status}")

# 2. Phân loại pixel theo điều kiện e > 50%
max_membership = np.max(membership, axis=1)
mask_certain = (max_membership > 0.5).reshape(H, W)
mask_uncertain = (~mask_certain)

certain_count = int(np.sum(mask_certain))
uncertain_count = int(np.sum(mask_uncertain))
total_pixels = H * W

certain_pct = (certain_count / total_pixels) * 100
uncertain_pct = (uncertain_count / total_pixels) * 100

print("\n--- THỐNG KÊ TOÀN DIỆN VỀ NGƯỠNG ĐỘ THUỘC e > 50% ---")
print(f" * Số pixel chắc chắn (e > 50%):         {certain_count:6d} pixels ({certain_pct:.2f}% diện tích ảnh)")
print(f" * Số pixel ranh giới mờ (e <= 50%):     {uncertain_count:6d} pixels ({uncertain_pct:.2f}% diện tích ảnh)")

# =========================================================================
# BƯỚC 5: TRỰC QUAN HÓA BẢN ĐỒ NHIỆT VÀ BẢNG ĐỐI CHIẾU TỔNG HỢP
# =========================================================================
print("\n[+] BƯỚC 5: Xuất các đồ thị trực quan hóa...")

# 1. Vẽ 4 Heatmaps biểu diễn % độ thuộc của từng cụm
fig, axes = plt.subplots(1, 4, figsize=(18, 4.5))
for k in range(4):
    u_k = (membership[:, k].reshape(H, W) * 100)
    im = axes[k].imshow(u_k, cmap='inferno', vmin=0, vmax=100)
    axes[k].set_title(f"Độ thuộc Cụm {k + 1} (%)\n[Tâm: RGB={np.round(fcm_centers[k]*255).astype(int)}]", fontsize=11, fontweight='bold')
    axes[k].axis('off')
    cbar = fig.colorbar(im, ax=axes[k], fraction=0.046, pad=0.04)
    cbar.ax.set_ylabel('% độ thuộc', fontsize=9)
plt.suptitle("BẢN ĐỒ NHIỆT ĐỘ THUỘC (MEMBERSHIP HEATMAPS) CỦA 4 CỤM THEO FUZZY C-MEANS", fontsize=13, fontweight='bold', y=1.05)
plt.tight_layout()
plt.savefig(os.path.join(results_dir, '04_membership_heatmaps.png'), bbox_inches='tight')
plt.close()

# 2. Vẽ phân tách vùng e > 50% và vùng e <= 50%
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

certain_visual = img_rgb.copy()
certain_visual[~mask_certain] = [30, 30, 30] # Che tối vùng không chắc chắn
ax1.imshow(certain_visual)
ax1.set_title(f"Vùng điểm ảnh xác định chắc chắn (e > 50%)\n[Chiếm {certain_pct:.1f}% diện tích ảnh]", fontsize=12, fontweight='bold', pad=10)
ax1.axis('off')

uncertain_visual = np.zeros_like(img_rgb)
uncertain_visual[mask_uncertain] = [255, 60, 0] # Tô màu cam đỏ nổi bật cho pixel ranh giới
import cv2
uncertain_overlay = cv2.addWeighted(img_rgb, 0.6, uncertain_visual, 0.8, 0)
ax2.imshow(uncertain_overlay)
ax2.set_title(f"Vùng ranh giới / chuyển tiếp mờ (e <= 50%)\n[Chiếm {uncertain_pct:.1f}% - Màu cam đỏ nổi bật]", fontsize=12, fontweight='bold', pad=10)
ax2.axis('off')

plt.suptitle("PHÂN TÍCH VÙNG ĐIỂM ẢNH THEO NGƯỠNG ĐỘ THUỘC e > 50%", fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(results_dir, '05_threshold_above_50.png'), bbox_inches='tight')
plt.close()

# 3. Biểu đồ tổng hợp so sánh 6 khung hình toàn diện
fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# 1: Ảnh gốc
axes[0, 0].imshow(img_rgb)
axes[0, 0].set_title("1. Ảnh gốc ban đầu (Input Image)", fontsize=11, fontweight='bold')
axes[0, 0].axis('off')

# 2: Custom K-Means
axes[0, 1].imshow(custom_seg_img)
axes[0, 1].set_title(f"2. Phân đoạn Custom K-Means (K = {K})\n[Hàm tự code - Phân cụm cứng]", fontsize=11, fontweight='bold')
axes[0, 1].axis('off')

# 3: Custom FCM
axes[0, 2].imshow(fcm_seg_img)
axes[0, 2].set_title(f"3. Phân đoạn Custom FCM (C = {K})\n[Hàm tự code - Khử mờ argmax]", fontsize=11, fontweight='bold')
axes[0, 2].axis('off')

# 4: Heatmap Max Membership
max_u_img = (max_membership.reshape(H, W) * 100)
im4 = axes[1, 0].imshow(max_u_img, cmap='viridis', vmin=25, vmax=100)
axes[1, 0].set_title("4. Mức độ tự tin cao nhất max(μ) (%)\n[Vàng: Rất chắc chắn, Xanh: Ranh giới]", fontsize=11, fontweight='bold')
axes[1, 0].axis('off')
fig.colorbar(im4, ax=axes[1, 0], fraction=0.046, pad=0.04)

# 5: Vùng e > 50%
axes[1, 1].imshow(certain_visual)
axes[1, 1].set_title(f"5. Vùng nhận diện chắc chắn (e > 50%)\n[Chiếm {certain_pct:.1f}% diện tích]", fontsize=11, fontweight='bold')
axes[1, 1].axis('off')

# 6: Vùng e <= 50%
axes[1, 2].imshow(uncertain_overlay)
axes[1, 2].set_title(f"6. Vùng ranh giới / tranh chấp mờ (e <= 50%)\n[Chiếm {uncertain_pct:.1f}% diện tích]", fontsize=11, fontweight='bold')
axes[1, 2].axis('off')

# 4. Biểu đồ Scatter Plot không gian màu 2D (Red vs Green) với Centroid 'X'
print("\n[+] BƯỚC 6: Trực quan hóa không gian phân cụm pixel (Scatter Plot 2D với Centroid 'X')...")
np.random.seed(42)
sample_size = 2000
sample_idx = np.random.choice(X.shape[0], sample_size, replace=False)
X_sample = X[sample_idx]
labels_sample = fcm_dominant_labels[sample_idx]

plt.figure(figsize=(9, 6))
colors = ['#e74c3c', '#3498db', '#2ecc71', '#9b59b6']
for i in range(K):
    pts = X_sample[labels_sample == i]
    plt.scatter(pts[:, 0], pts[:, 1], c=colors[i], label=f'Cụm {i + 1} ({len(pts)} mẫu)', alpha=0.45, s=30)

# Vẽ Tâm cụm (Centroids) bằng dấu X lớn nổi bật đúng như hình minh họa lý thuyết trong slide của thầy
plt.scatter(fcm_centers[:, 0], fcm_centers[:, 1], s=350, c='black', marker='X', edgecolors='white', linewidths=2.5,
            label="Tâm cụm Centroid ('X')", zorder=10)

plt.title("PHÂN BỐ ĐIỂM ẢNH TRONG KHÔNG GIAN MÀU 2D (KÊNH RED vs GREEN)\n[Đánh dấu tâm cụm Centroid bằng chữ 'X' lớn theo lý thuyết]",
          fontsize=12, fontweight='bold', pad=12)
plt.xlabel("Cường độ chuẩn hóa kênh Đỏ (Red)", fontsize=11)
plt.ylabel("Cường độ chuẩn hóa kênh Xanh (Green)", fontsize=11)
plt.legend(frameon=True, shadow=True, loc='best')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(results_dir, '07_color_space_scatter.png'), bbox_inches='tight')
plt.close()

print(f"\n[+] ĐÃ HOÀN TẤT VÀ LƯU TẤT CẢ BIỂU ĐỒ VÀO: {results_dir}")
print("=" * 75)
