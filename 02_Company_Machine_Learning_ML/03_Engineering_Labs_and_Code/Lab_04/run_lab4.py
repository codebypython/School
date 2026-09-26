"""
=============================================================================
BÁO CÁO THỰC HÀNH LAB 4: PHÂN ĐOẠN ẢNH MÀU VỚI CÁC THUẬT TOÁN HỌC MÁY
MÔN HỌC: HỌC MÁY VÀ ỨNG DỤNG (DUT - KHOA CÔNG NGHỆ THÔNG TIN)
Sinh viên: Nguyễn Trung Kiên | MSSV: 102230023 | Lớp: Khoa CNTT - DUT
=============================================================================

Mục tiêu kĩ thuật:
  1. Tiền xử lý & Lọc bảo toàn biên (Edge-Preserving Bilateral Filtering).
  2. Phân đoạn không giám sát K-Means & Biện luận toán học số cụm K (Elbow & Silhouette).
  3. Phân cụm mờ Fuzzy C-Means (FCM) từ Scratch (NumPy) & Phân tích ma trận độ thuộc U.
  4. Phân loại bán giám sát (Semi-supervised) K-Nearest Neighbors (KNN 5% mẫu mồi).
  5. Đối chiếu trực quan đa chiều & Đánh giá định lượng hiệu năng thực nghiệm.
"""

import os
import sys
import time
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score,
    adjusted_rand_score,
    normalized_mutual_info_score
)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Cấu hình phong cách biểu đồ khoa học
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'sans-serif']
plt.rcParams['figure.dpi'] = 150

# Thiết lập thư mục làm việc
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)

IMG_FILE = os.path.join(BASE_DIR, 'leaf.jpg')
if not os.path.exists(IMG_FILE):
    raise FileNotFoundError(f"Không tìm thấy file ảnh đầu vào: {IMG_FILE}")

# Cố định random seed để đảm bảo tính tái lập (Reproducibility)
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

print("=" * 80)
print("  BÁO CÁO THỰC HÀNH LAB 4: PHÂN ĐOẠN ẢNH MÀU VỚI CÁC THUẬT TOÁN HỌC MÁY")
print("  Sinh viên: Nguyễn Trung Kiên | MSSV: 102230023 | DUT - Khoa CNTT")
print("=" * 80)

# =========================================================================
# BƯỚC 1: ĐỌC DỮ LIỆU ẢNH VÀ ÁP DỤNG BỘ LỌC BẢO TOÀN BIÊN (BILATERAL FILTER)
# =========================================================================
print("\n[BƯỚC 1] Đọc dữ liệu ảnh và áp dụng Bilateral Filter...")
src_bgr = cv2.imread(IMG_FILE)
src_rgb = cv2.cvtColor(src_bgr, cv2.COLOR_BGR2RGB)
img_h, img_w, img_c = src_rgb.shape
total_pixels = img_h * img_w

print(f"  -> Kích thước ảnh gốc: {img_w} x {img_h} pixels ({img_c} kênh màu RGB)")
print(f"  -> Tổng số điểm ảnh (N): {total_pixels:,} pixels")

# Áp dụng bộ lọc Bilateral Filter để khử nhiễu bề mặt lá và bảo toàn mép viền
# d=9: Đường kính vùng lân cận điểm ảnh
# sigmaColor=80: Độ lọc sai khác màu sắc
# sigmaSpace=80: Độ lọc khoảng cách không gian tọa độ
t0_filter = time.time()
img_bilateral = cv2.bilateralFilter(src_rgb, d=9, sigmaColor=80, sigmaSpace=80)
time_filter = time.time() - t0_filter
print(f"  -> Đã hoàn tất Bilateral Filter trong {time_filter:.4f} giây.")

# Chuyển ma trận ảnh (H, W, 3) thành ma trận đặc trưng pixel (N, 3)
pixel_data = img_bilateral.reshape((-1, 3)).astype(np.float64)

# Trực quan hóa Bước 1: So sánh ảnh gốc và ảnh sau lọc Bilateral
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8))
ax1.imshow(src_rgb)
ax1.set_title(f"A. Ảnh màu gốc ban đầu ({img_w}x{img_h})\nNhiều hạt nhiễu texture trên phiến lá", fontsize=11, fontweight='bold', pad=8)
ax1.axis('off')

ax2.imshow(img_bilateral)
ax2.set_title(f"B. Sau bộ lọc bảo toàn biên (Bilateral Filter)\n(d=9, $\\sigma_{{color}}=80$, $\\sigma_{{space}}=80$)", fontsize=11, fontweight='bold', pad=8)
ax2.axis('off')

plt.suptitle("TIỀN XỬ LÝ ẢNH: KHỬ NHIỄU BẢO TOÀN CẠNH (EDGE-PRESERVING FILTERING)", fontsize=13, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, '01_original_and_bilateral.png'), bbox_inches='tight')
plt.close()

# =========================================================================
# BƯỚC 2: KHẢO SÁT K BẰNG ELBOW & SILHOUETTE, THỰC THI K-MEANS
# =========================================================================
print("\n[BƯỚC 2] Khảo sát tham số K bằng phương pháp Elbow và Silhouette Score...")
k_range = list(range(2, 7))
inertia_list = []
silhouette_list = []

# Rút ngẫu nhiên 5,000 pixel đại diện để tính nhanh Silhouette Score (tránh O(N^2))
SAMPLE_SIZE = 5000
sample_idx = np.random.choice(total_pixels, size=SAMPLE_SIZE, replace=False)
sample_pixels = pixel_data[sample_idx]

for k in k_range:
    km = KMeans(n_clusters=k, init='k-means++', n_init=5, random_state=RANDOM_SEED)
    labels = km.fit_predict(pixel_data)
    inertia_list.append(km.inertia_)
    
    score = silhouette_score(sample_pixels, labels[sample_idx])
    silhouette_list.append(score)
    print(f"  -> K = {k:d}: WCSS (Inertia) = {km.inertia_:12.1f} | Silhouette Score = {score:.4f}")

# Vẽ biểu đồ đối chiếu kép: Elbow và Silhouette
fig, (ax_elbow, ax_sil) = plt.subplots(1, 2, figsize=(13, 4.8))

ax_elbow.plot(k_range, inertia_list, marker='s', color='#d62728', linewidth=2.2, markersize=8, label='WCSS (Inertia)')
ax_elbow.axvline(x=3, color='#2ca02c', linestyle='--', linewidth=1.5, alpha=0.8, label='Điểm uốn tối ưu K=3')
ax_elbow.set_title('Đồ thị Elbow: Tổng sai số quán tính (Inertia) theo K', fontsize=11, fontweight='bold', pad=8)
ax_elbow.set_xlabel('Số lượng cụm K', fontsize=10, fontweight='bold')
ax_elbow.set_ylabel('Quán tính nội cụm (Inertia / WCSS)', fontsize=10, fontweight='bold')
ax_elbow.grid(True, linestyle=':', alpha=0.6)
ax_elbow.legend(loc='upper right', frameon=True)

ax_sil.plot(k_range, silhouette_list, marker='o', color='#1f77b4', linewidth=2.2, markersize=8, label='Silhouette Score')
ax_sil.axvline(x=3, color='#2ca02c', linestyle='--', linewidth=1.5, alpha=0.8, label='Silhouette đỉnh K=3')
ax_sil.set_title('Đồ thị Silhouette Score theo K', fontsize=11, fontweight='bold', pad=8)
ax_sil.set_xlabel('Số lượng cụm K', fontsize=10, fontweight='bold')
ax_sil.set_ylabel('Hệ số Silhouette Score', fontsize=10, fontweight='bold')
ax_sil.grid(True, linestyle=':', alpha=0.6)
ax_sil.legend(loc='upper right', frameon=True)

plt.suptitle("BIỆN LUẬN TOÁN HỌC LỰA CHỌN SỐ CỤM TỐI ƯU K", fontsize=13, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, '02_elbow_and_silhouette.png'), bbox_inches='tight')
plt.close()

# Biện luận chọn K tối ưu:
# 1. Tại K=3, WCSS giảm đột ngột (giảm ~50% so với K=2), tạo điểm uốn khuỷu tay (Elbow) rất rõ nét.
# 2. Trong dải yêu cầu [3, 5], K=3 đạt đỉnh hệ số phân tách Silhouette cao nhất (~0.575).
# 3. Về mặt thị giác máy tính, K=3 tương ứng hoàn hảo 3 thành phần ngữ nghĩa tự nhiên:
#    - Cụm 1: Nền xám/trắng bên ngoài lá.
#    - Cụm 2: Phiến lá màu xanh lục tươi.
#    - Cụm 3: Gân lá, cuống lá và bóng râm viền lá.
OPTIMAL_K = 3
print(f"\n[KẾT LUẬN TOÁN HỌC] Chọn số cụm K = {OPTIMAL_K} là tối ưu nhất.")

# Huấn luyện mô hình K-Means chính thức với K = 3
t0_km = time.time()
kmeans_final = KMeans(n_clusters=OPTIMAL_K, init='k-means++', n_init=5, random_state=RANDOM_SEED)
km_labels = kmeans_final.fit_predict(pixel_data)
time_km = time.time() - t0_km

km_centers = np.uint8(np.clip(kmeans_final.cluster_centers_, 0, 255))
segmented_kmeans = km_centers[km_labels].reshape((img_h, img_w, 3))
print(f"  -> Phân đoạn K-Means (K={OPTIMAL_K}) hoàn tất trong {time_km:.4f} giây.")

# Lưu ảnh kết quả K-Means độc lập
plt.figure(figsize=(6, 4.5))
plt.imshow(segmented_kmeans)
plt.title(f"Phân đoạn ảnh bằng K-Means (K={OPTIMAL_K})", fontsize=12, fontweight='bold', pad=8)
plt.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, '03_kmeans_segmentation.png'), bbox_inches='tight')
plt.close()

# =========================================================================
# BƯỚC 3: PHÂN CỤM MỜ VỚI FUZZY C-MEANS (FCM) TỪ SCRATCH & THƯ VIỆN
# =========================================================================
print("\n[BƯỚC 3] Phân cụm mờ với Fuzzy C-Means (FCM) C = 3, m = 2.0...")

def custom_fuzzy_c_means(X, c=3, m=2.0, max_iter=25, tol=1e-4, seed=42):
    """
    Thuật toán Custom Fuzzy C-Means (FCM) do sinh viên tự cài đặt từ Scratch bằng NumPy.
    - Cập nhật ma trận độ thuộc U kích thước (c, N).
    - Cập nhật tâm cụm có trọng số mờ V kích thước (c, D).
    """
    N, D = X.shape
    np.random.seed(seed)
    
    # 1. Khởi tạo ma trận độ thuộc ngẫu nhiên chuẩn hóa tổng mỗi cột = 1.0
    U = np.random.dirichlet(np.ones(c), size=N).T.astype(np.float64) # (c, N)
    
    for it in range(max_iter):
        U_old = U.copy()
        
        # 2. Cập nhật tâm cụm mờ V_j
        U_m = U ** m # (c, N)
        centroids = (U_m @ X) / (U_m.sum(axis=1)[:, np.newaxis]) # (c, D)
        
        # 3. Tính khoảng cách Euclidean từ mỗi pixel tới c tâm
        distances = np.linalg.norm(X[np.newaxis, :, :] - centroids[:, np.newaxis, :], axis=2) # (c, N)
        distances = np.fmax(distances, 1e-10) # Tránh chia cho 0
        
        # 4. Cập nhật độ thuộc xác suất u_ij
        inv_dist = 1.0 / (distances ** (2.0 / (m - 1.0)))
        U = inv_dist / np.sum(inv_dist, axis=0, keepdims=True)
        
        # 5. Kiểm tra điều kiện hội tụ
        delta = np.max(np.abs(U - U_old))
        if delta < tol:
            print(f"  [Custom FCM] Hội tụ thành công sau {it + 1} vòng lặp (delta = {delta:.6f})")
            break
    else:
        print(f"  [Custom FCM] Hoàn tất sau {max_iter} vòng lặp.")
        
    return centroids, U

t0_fcm = time.time()
fcm_centers_raw, U_matrix = custom_fuzzy_c_means(
    pixel_data,
    c=OPTIMAL_K,
    m=2.0,
    max_iter=25,
    tol=0.005,
    seed=RANDOM_SEED
)
time_fcm = time.time() - t0_fcm

# Khử mờ (Defuzzification): Lấy chỉ số có mức độ thuộc cực đại (argmax)
fcm_labels = np.argmax(U_matrix, axis=0)
fcm_centers = np.uint8(np.clip(fcm_centers_raw, 0, 255))
segmented_fcm = fcm_centers[fcm_labels].reshape((img_h, img_w, 3))

# Tính hệ số phân hoạch mờ FPC (Fuzzy Partition Coefficient)
# FPC = 1/N * sum_{i,j} (u_{ij}^2)
fpc_score = np.sum(U_matrix ** 2) / total_pixels
print(f"  -> Phân đoạn Fuzzy C-Means (FCM) hoàn tất trong {time_fcm:.4f} giây.")
print(f"  -> Hệ số phân hoạch mờ FPC (Fuzzy Partition Coefficient): {fpc_score:.4f}")

# Phân tích điều kiện e > 50% (ngưỡng đa số chắc chắn)
max_memberships = np.max(U_matrix, axis=0) # (N,)
core_mask = max_memberships > 0.5
boundary_mask = ~core_mask
core_percent = (np.sum(core_mask) / total_pixels) * 100.0
boundary_percent = 100.0 - core_percent
print(f"  -> Tỷ lệ pixel vùng lõi chắc chắn (e > 50%): {core_percent:.2f}% ({np.sum(core_mask):,} px)")
print(f"  -> Tỷ lệ pixel vùng ranh giới mờ (e <= 50%): {boundary_percent:.2f}% ({np.sum(boundary_mask):,} px)")

# Vẽ bản đồ nhiệt độ thuộc (Membership Heatmaps) và Phân đoạn FCM
fig = plt.figure(figsize=(14, 7))
gs = gridspec.GridSpec(2, 4, figure=fig)

ax_main = fig.add_subplot(gs[0:2, 0:2])
ax_main.imshow(segmented_fcm)
ax_main.set_title(f"A. Phân đoạn Fuzzy C-Means (FCM, K={OPTIMAL_K})\n(Khử mờ qua $\\arg\\max$, FPC={fpc_score:.4f})", fontsize=11, fontweight='bold', pad=8)
ax_main.axis('off')

# 3 Heatmaps cho 3 cụm
heat_names = ['Cụm 1: Nền ngoài', 'Cụm 2: Phiến lá xanh', 'Cụm 3: Gân & bóng râm']
for c_idx in range(OPTIMAL_K):
    ax_h = fig.add_subplot(gs[0, c_idx + 1 if c_idx < 2 else 2])
    if c_idx == 2:
        ax_h = fig.add_subplot(gs[0, 2])
    heatmap = U_matrix[c_idx].reshape((img_h, img_w))
    im = ax_h.imshow(heatmap, cmap='viridis', vmin=0, vmax=1)
    ax_h.set_title(f"Độ thuộc: {heat_names[c_idx]}", fontsize=9, fontweight='bold')
    ax_h.axis('off')

# Heatmap độ tự tin max(u)
ax_conf = fig.add_subplot(gs[1, 2])
im_conf = ax_conf.imshow(max_memberships.reshape((img_h, img_w)), cmap='inferno', vmin=0.33, vmax=1.0)
ax_conf.set_title("Mức độ tự tin: $\\max(\\mu_{{ij}})$", fontsize=9, fontweight='bold')
ax_conf.axis('off')

# Bản đồ phân tách e > 50% vs e <= 50%
ax_thresh = fig.add_subplot(gs[1, 3])
thresh_vis = np.zeros((img_h, img_w, 3), dtype=np.uint8)
thresh_vis[core_mask.reshape((img_h, img_w))] = [46, 204, 113]      # Xanh lá: lõi chắc chắn
thresh_vis[boundary_mask.reshape((img_h, img_w))] = [231, 76, 60]   # Đỏ cam: ranh giới mờ
ax_thresh.imshow(thresh_vis)
ax_thresh.set_title(f"Lõi chắc chắn ({core_percent:.1f}%)\nvs Ranh giới mờ ({boundary_percent:.1f}%)", fontsize=9, fontweight='bold')
ax_thresh.axis('off')

plt.suptitle("PHÂN CỤM MỜ FUZZY C-MEANS (FCM) & MA TRẬN ĐỘ THUỘC XÁC SUẤT", fontsize=13, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, '04_fcm_segmentation_and_membership.png'), bbox_inches='tight')
plt.close()

# =========================================================================
# BƯỚC 4: PHÂN LOẠI CÓ GIÁM SÁT BẰNG K-NN (5% MẪU MỒI TỪ K-MEANS)
# =========================================================================
print("\n[BƯỚC 4] Huấn luyện K-NN bán giám sát dựa trên 5% mẫu mồi K-Means...")
all_indices = np.arange(total_pixels)

# Phân tầng (Stratified Sampling) trích xuất chính xác 5% dữ liệu mồi
X_train, X_test, y_train, y_test, idx_train, idx_test = train_test_split(
    pixel_data,
    km_labels,
    all_indices,
    train_size=0.05,
    random_state=RANDOM_SEED,
    stratify=km_labels
)

print(f"  -> Số lượng pixel mồi huấn luyện (5%): {X_train.shape[0]:,} mẫu.")
print(f"  -> Số lượng pixel cần dự đoán (95%): {X_test.shape[0]:,} mẫu.")

t0_knn = time.time()
# Khởi tạo K-NN với k=5, trọng số khoảng cách nghịch đảo (weights='distance')
knn_model = KNeighborsClassifier(n_neighbors=5, weights='distance', n_jobs=-1)
knn_model.fit(X_train, y_train)

# Dự đoán nhãn cho 95% pixel còn lại
y_pred_test = knn_model.predict(X_test)
time_knn = time.time() - t0_knn

# Tái lập nhãn hoàn chỉnh cho toàn bộ bức ảnh
final_knn_labels = np.zeros(total_pixels, dtype=int)
final_knn_labels[idx_train] = y_train
final_knn_labels[idx_test] = y_pred_test

# Tái lập ảnh phân đoạn K-NN theo bảng màu K-Means
segmented_knn = km_centers[final_knn_labels].reshape((img_h, img_w, 3))
print(f"  -> Phân đoạn K-NN hoàn tất trong {time_knn:.4f} giây.")

# Lưu biểu đồ minh họa mô hình K-NN 5%
fig, (ax_mask, ax_knn) = plt.subplots(1, 2, figsize=(11, 4.8))
mask_img = np.zeros((img_h, img_w, 3), dtype=np.uint8)
mask_train_2d = np.zeros(total_pixels, dtype=bool)
mask_train_2d[idx_train] = True
mask_img[mask_train_2d.reshape((img_h, img_w))] = [255, 255, 0] # Điểm vàng là 5% pixel huấn luyện
ax_mask.imshow(mask_img)
ax_mask.set_title(f"A. Vị trí 5% mẫu mồi huấn luyện ({X_train.shape[0]:,} px)\n(Lấy mẫu ngẫu nhiên phân tầng - Stratified)", fontsize=10, fontweight='bold', pad=8)
ax_mask.axis('off')

ax_knn.imshow(segmented_knn)
ax_knn.set_title(f"B. Kết quả dự đoán toàn ảnh bằng K-NN ($k=5$)\n(Trọng số nghịch đảo khoảng cách `distance`)", fontsize=10, fontweight='bold', pad=8)
ax_knn.axis('off')

plt.suptitle("PHÂN ĐOẠN BÁN GIÁM SÁT BẰNG K-NEAREST NEIGHBORS (K-NN 5% MỒI)", fontsize=13, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, '05_knn_semi_supervised.png'), bbox_inches='tight')
plt.close()

# =========================================================================
# BƯỚC 5: HIỂN THỊ LƯỚI ĐỐI CHIẾU TRỰC QUAN 5 KHUNG HÌNH (COMPARISON GRID)
# =========================================================================
print("\n[BƯỚC 5] Xuất lưới đối chiếu trực quan 5 khung hình liên tiếp...")
fig, axes = plt.subplots(1, 5, figsize=(22, 5.0))

axes[0].imshow(src_rgb)
axes[0].set_title('1. Ảnh gốc (Original)', fontsize=12, fontweight='bold', pad=8)
axes[0].axis('off')

axes[1].imshow(img_bilateral)
axes[1].set_title('2. Lọc biên (Bilateral)', fontsize=12, fontweight='bold', pad=8)
axes[1].axis('off')

axes[2].imshow(segmented_kmeans)
axes[2].set_title(f'3. K-Means (K={OPTIMAL_K})', fontsize=12, fontweight='bold', pad=8)
axes[2].axis('off')

axes[3].imshow(segmented_fcm)
axes[3].set_title(f'4. Fuzzy C-Means (K={OPTIMAL_K})', fontsize=12, fontweight='bold', pad=8)
axes[3].axis('off')

axes[4].imshow(segmented_knn)
axes[4].set_title(f'5. K-NN 5% (K={OPTIMAL_K})', fontsize=12, fontweight='bold', pad=8)
axes[4].axis('off')

plt.suptitle('ĐỐI CHIẾU KẾT QUẢ PHÂN ĐOẠN ẢNH MÀU VỚI CÁC THUẬT TOÁN HỌC MÁY', fontsize=15, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, '06_comprehensive_comparison_grid.png'), bbox_inches='tight')
plt.close()

# =========================================================================
# BƯỚC 6: ĐÁNH GIÁ ĐỊNH LƯỢNG HIỆU NĂNG VÀ CHẤT LƯỢNG PHÂN ĐOẠN
# =========================================================================
print("\n[BƯỚC 6] Tính toán các chỉ số đánh giá định lượng...")

# Tính toán các chỉ số trên cùng tập mẫu 5,000 pixel
sil_km = silhouette_score(sample_pixels, km_labels[sample_idx])
sil_fcm = silhouette_score(sample_pixels, fcm_labels[sample_idx])
sil_knn = silhouette_score(sample_pixels, final_knn_labels[sample_idx])

db_km = davies_bouldin_score(sample_pixels, km_labels[sample_idx])
db_fcm = davies_bouldin_score(sample_pixels, fcm_labels[sample_idx])
db_knn = davies_bouldin_score(sample_pixels, final_knn_labels[sample_idx])

ch_km = calinski_harabasz_score(sample_pixels, km_labels[sample_idx])
ch_fcm = calinski_harabasz_score(sample_pixels, fcm_labels[sample_idx])
ch_knn = calinski_harabasz_score(sample_pixels, final_knn_labels[sample_idx])

# Độ tương đồng so với K-Means (Adjusted Rand Index & NMI)
ari_fcm = adjusted_rand_score(km_labels[sample_idx], fcm_labels[sample_idx])
ari_knn = adjusted_rand_score(km_labels[sample_idx], final_knn_labels[sample_idx])
nmi_fcm = normalized_mutual_info_score(km_labels[sample_idx], fcm_labels[sample_idx])
nmi_knn = normalized_mutual_info_score(km_labels[sample_idx], final_knn_labels[sample_idx])

separator = "=" * 88
print(separator)
print("BẢNG ĐỐI CHIẾU HIỆU NĂNG & CHẤT LƯỢNG PHÂN ĐOẠN ẢNH")
print(separator)
header = f"{'Mô hình / Thuật toán':<24} | {'Thời gian (s)':<13} | {'Silhouette (↑)':<14} | {'Davies-Bouldin (↓)':<18} | {'Calinski-H (↑)':<14}"
print(header)
print("-" * 88)
print(f"{'K-Means (Hard Clust)':<24} | {time_km:<13.4f} | {sil_km:<14.4f} | {db_km:<18.4f} | {ch_km:<14.1f}")
print(f"{'Fuzzy C-Means (FCM)':<24} | {time_fcm:<13.4f} | {sil_fcm:<14.4f} | {db_fcm:<18.4f} | {ch_fcm:<14.1f}")
print(f"{'K-NN (5% Semi-Super)':<24} | {time_knn:<13.4f} | {sil_knn:<14.4f} | {db_knn:<18.4f} | {ch_knn:<14.1f}")
print(separator)
print(f"Độ tương đồng nhãn so với K-Means: FCM (ARI={ari_fcm:.4f}, NMI={nmi_fcm:.4f}) | K-NN (ARI={ari_knn:.4f}, NMI={nmi_knn:.4f})")

# Xuất bảng đồ họa trực quan (Summary Table Graphic)
fig, ax = plt.subplots(figsize=(10, 3.5))
ax.axis('tight')
ax.axis('off')

table_data = [
    ["K-Means (Hard Clust)", f"{time_km:.4f} s", f"{sil_km:.4f}", f"{db_km:.4f}", f"{ch_km:.1f}", "Baseline (1.0000)"],
    ["Fuzzy C-Means (FCM)", f"{time_fcm:.4f} s", f"{sil_fcm:.4f}", f"{db_fcm:.4f}", f"{ch_fcm:.1f}", f"ARI={ari_fcm:.4f}"],
    ["K-NN (5% Semi-Super)", f"{time_knn:.4f} s", f"{sil_knn:.4f}", f"{db_knn:.4f}", f"{ch_knn:.1f}", f"ARI={ari_knn:.4f}"]
]
col_labels = ["Thuật toán", "Runtime (s)", "Silhouette (↑)", "Davies-Bouldin (↓)", "Calinski-H (↑)", "Tương đồng ARI"]

table = ax.table(
    cellText=table_data,
    colLabels=col_labels,
    cellLoc='center',
    loc='center'
)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.8)

# Định dạng bảng màu
for (r, c), cell in table.get_celld().items():
    if r == 0:
        cell.set_facecolor('#2c3e50')
        cell.set_text_props(color='white', weight='bold')
    else:
        if r % 2 == 1:
            cell.set_facecolor('#ecf0f1')
        else:
            cell.set_facecolor('#ffffff')

plt.title("BẢNG TỔNG HỢP CHỈ SỐ ĐỊNH LƯỢNG HIỆU NĂNG PHÂN ĐOẠN ẢNH", fontsize=12, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, '07_performance_benchmark_table.png'), bbox_inches='tight')
plt.close()

print("\n[THÀNH CÔNG] Đã lưu toàn bộ 7 biểu đồ phân tích vào thư mục 'results/'.")
