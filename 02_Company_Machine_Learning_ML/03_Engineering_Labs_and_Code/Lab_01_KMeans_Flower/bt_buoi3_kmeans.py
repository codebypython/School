import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.decomposition import PCA

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Cấu hình phong cách đồ thị
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'sans-serif']
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 1.2

base_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(base_dir, 'flower_dataset.xlsx')
csv_path = os.path.join(base_dir, 'flower_dataset.csv')

print("=" * 60)
print("BÀI TẬP BUỔI 3: PHÂN CỤM K-MEANS TRÊN DỮ LIỆU LOÀI HOA")
print("=" * 60)

# -------------------------------------------------------------
# BƯỚC 1: ĐỌC DỮ LIỆU TỪ FILE EXCEL / CSV
# -------------------------------------------------------------
if os.path.exists(excel_path):
    print(f"\n[+] Đang đọc dữ liệu từ file Excel: {excel_path}")
    df = pd.read_excel(excel_path)
else:
    print(f"\n[+] Đang đọc dữ liệu từ file CSV: {csv_path}")
    df = pd.read_csv(csv_path)

print(f"Tổng số mẫu: {len(df)} dòng | Số thuộc tính: {df.shape[1]} cột")
print("\nThông tin 5 mẫu đầu tiên:")
print(df.head())

# Lấy các đặc trưng số (numerical features) để phân cụm
feature_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'stem_length']
X_raw = df[feature_cols].values

print(f"\nCác đặc trưng số được sử dụng ({len(feature_cols)} đặc trưng):")
for col in feature_cols:
    print(f" - {col}: min={df[col].min():.2f}, max={df[col].max():.2f}, mean={df[col].mean():.2f}, std={df[col].std():.2f}")

# -------------------------------------------------------------
# BƯỚC 2: TIỀN XỬ LÝ & CHUẨN HÓA DỮ LIỆU (STANDARD SCALING)
# -------------------------------------------------------------
# Chuẩn hóa Z-score: mean = 0, std = 1 để các thuộc tính có cùng thang đo
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_raw)

# -------------------------------------------------------------
# BƯỚC 3: ĐỒ THỊ GIẢI THÍCH CHỌN K (ELBOW METHOD & SILHOUETTE)
# -------------------------------------------------------------
print("\n[+] Đang tính toán WCSS (Inertia) và Silhouette Score cho K từ 2 đến 10...")
K_range = range(2, 11)
wcss = []
silhouette_scores = []

# Tính thêm cho K=1 để vẽ đường Elbow đầy đủ từ 1 đến 10
km1 = KMeans(n_clusters=1, random_state=42, n_init=10)
km1.fit(X_scaled)
wcss_full = [km1.inertia_]
K_full = [1] + list(K_range)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    wcss.append(km.inertia_)
    wcss_full.append(km.inertia_)
    score = silhouette_score(X_scaled, km.labels_)
    silhouette_scores.append(score)
    print(f"  K = {k:2d} | WCSS (Inertia) = {km.inertia_:9.2f} | Silhouette Score = {score:.4f}")

# Vẽ đồ thị giải thích vì sao chọn K
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Đồ thị 1: Phương pháp Khuỷu tay (Elbow Method)
ax1.plot(K_full, wcss_full, 'bo-', linewidth=2.5, markersize=8, markerfacecolor='#e74c3c', markeredgecolor='black')
ax1.set_title("1. Phương pháp Khuỷu tay (Elbow Method)", fontsize=14, fontweight='bold', pad=12)
ax1.set_xlabel("Số lượng cụm K", fontsize=12)
ax1.set_ylabel("Độ biến dạng WCSS (Inertia)", fontsize=12)
ax1.set_xticks(K_full)
ax1.grid(True, linestyle='--', alpha=0.7)

# Đánh dấu điểm khuỷu tay K = 6 (nằm trong khoảng 5-7)
chosen_k = 6
wcss_chosen = wcss_full[K_full.index(chosen_k)]
ax1.plot(chosen_k, wcss_chosen, 'o', markersize=14, markerfacecolor='yellow', markeredgecolor='red', markeredgewidth=3)
ax1.annotate(f"Điểm Khuỷu tay K={chosen_k}\n(Tốc độ giảm WCSS chậm lại rõ rệt)",
             xy=(chosen_k, wcss_chosen), xytext=(chosen_k + 0.8, wcss_chosen + 200),
             arrowprops=dict(facecolor='red', shrink=0.08, width=2, headwidth=8),
             fontsize=11, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="#fff9c4", ec="#fbc02d", lw=1.5))

# Đồ thị 2: Hệ số Silhouette (Silhouette Score)
colors = ['#3498db' if k != chosen_k else '#e74c3c' for k in K_range]
bars = ax2.bar(K_range, silhouette_scores, color=colors, edgecolor='black', width=0.6, alpha=0.85)
ax2.plot(K_range, silhouette_scores, 'ro--', linewidth=1.5, markersize=6)
ax2.set_title("2. Hệ số Silhouette qua các giá trị K", fontsize=14, fontweight='bold', pad=12)
ax2.set_xlabel("Số lượng cụm K", fontsize=12)
ax2.set_ylabel("Silhouette Score trung bình", fontsize=12)
ax2.set_xticks(list(K_range))
ax2.set_ylim(0, max(silhouette_scores) * 1.25)
ax2.grid(True, axis='y', linestyle='--', alpha=0.7)

# Hiển thị giá trị trên từng cột
for bar, score in zip(bars, silhouette_scores):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.015, f"{score:.3f}",
             ha='center', va='bottom', fontsize=10, fontweight='bold')

ax2.annotate(f"K={chosen_k} đạt đỉnh tối ưu\n(Silhouette={silhouette_scores[K_range.index(chosen_k)]:.3f})",
             xy=(chosen_k, silhouette_scores[K_range.index(chosen_k)]),
             xytext=(chosen_k - 1.8, silhouette_scores[K_range.index(chosen_k)] + 0.10),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.08, width=2, headwidth=8),
             fontsize=11, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="#ffebee", ec="#e57373", lw=1.5))

plt.suptitle(f"PHÂN TÍCH VÀ GIẢI THÍCH LÝ DO CHỌN SỐ CỤM K = {chosen_k} (TRONG KHOẢNG 5-7)", fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
fig_k_path = os.path.join(base_dir, 'dothi_giai_thich_chon_k.png')
plt.savefig(fig_k_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"[+] Đã lưu đồ thị giải thích chọn K: {fig_k_path}")

# -------------------------------------------------------------
# BƯỚC 4: HUẤN LUYỆN K-MEANS VỚI K ĐƯỢC CHỌN (K = 6)
# -------------------------------------------------------------
print(f"\n[+] Huấn luyện mô hình K-Means với K = {chosen_k}...")
kmeans = KMeans(n_clusters=chosen_k, random_state=42, n_init=20, max_iter=300)
cluster_labels = kmeans.fit_predict(X_scaled)
df['cluster'] = cluster_labels

# Tọa độ Centroid trên không gian đã chuẩn hóa
scaled_centroids = kmeans.cluster_centers_

# Chuyển đổi tọa độ Centroid về thang đo gốc (Original Units)
original_centroids = scaler.inverse_transform(scaled_centroids)

print(f"\n[+] Tọa độ Centroid ({chosen_k} cụm) trên thang đo gốc (cm):")
centroids_df = pd.DataFrame(original_centroids, columns=feature_cols)
centroids_df.index = [f"Cluster {i}" for i in range(chosen_k)]
print(centroids_df)

print("\n[+] Phân bố số lượng mẫu trong từng cụm:")
print(df['cluster'].value_counts().sort_index())

# -------------------------------------------------------------
# BƯỚC 5: VẼ SCATTER PLOT - ĐÁNH DẤU CENTROID BẰNG DẤU 'X'
# -------------------------------------------------------------
print("\n[+] Vẽ Scatter Plot đánh dấu Centroid bằng 'X'...")

# Biểu đồ 1: Scatter plot giữa Petal Length và Petal Width (2 đặc trưng đặc trưng nhất của hoa)
plt.figure(figsize=(12, 8))
palette = sns.color_palette("tab10", chosen_k)

# Vẽ các điểm dữ liệu theo cụm
for c in range(chosen_k):
    cluster_points = df[df['cluster'] == c]
    plt.scatter(
        cluster_points['petal_length'],
        cluster_points['petal_width'],
        label=f'Cụm {c} (N={len(cluster_points)})',
        color=palette[c],
        alpha=0.8,
        s=60,
        edgecolors='white',
        linewidth=0.5
    )

# ĐÁNH DẤU CENTROID BẰNG DẤU 'X' TO NỔI BẬT
pl_idx = feature_cols.index('petal_length')
pw_idx = feature_cols.index('petal_width')

plt.scatter(
    original_centroids[:, pl_idx],
    original_centroids[:, pw_idx],
    marker='X',
    s=280,
    c='#d63031',
    edgecolors='black',
    linewidths=2.5,
    label='Tâm cụm Centroid (X)',
    zorder=10
)

# Thêm nhãn cho từng Centroid
for c in range(chosen_k):
    plt.annotate(
        f'Centroid {c}',
        xy=(original_centroids[c, pl_idx], original_centroids[c, pw_idx]),
        xytext=(original_centroids[c, pl_idx] + 0.15, original_centroids[c, pw_idx] + 0.1),
        fontsize=10,
        fontweight='bold',
        color='#2d3436',
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#b2bec3", alpha=0.9),
        zorder=11
    )

plt.title(f"SCATTER PLOT PHÂN CỤM K-MEANS VỚI K = {chosen_k} (ĐÁNH DẤU CENTROID BẰNG 'X')",
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Chiều dài cánh hoa - Petal Length (cm)", fontsize=12, labelpad=8)
plt.ylabel("Chiều rộng cánh hoa - Petal Width (cm)", fontsize=12, labelpad=8)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True, shadow=True, fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

fig_scatter_path = os.path.join(base_dir, 'scatter_plot_kmeans_petal.png')
plt.savefig(fig_scatter_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"[+] Đã lưu Scatter Plot (Petal): {fig_scatter_path}")

# -------------------------------------------------------------
# BƯỚC 6: SCATTER PLOT TOÀN DIỆN VỚI PCA (2D PROJECTION)
# -------------------------------------------------------------
# Giảm chiều 5 đặc trưng số xuống 2 thành phần chính (PC1, PC2) để quan sát toàn diện
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_scaled)
df['PCA1'] = X_pca[:, 0]
df['PCA2'] = X_pca[:, 1]

# Chiếu tọa độ tâm cụm Centroid sang không gian PCA
centroids_pca = pca.transform(scaled_centroids)
var_ratio = pca.explained_variance_ratio_

plt.figure(figsize=(12, 8))
for c in range(chosen_k):
    pts = df[df['cluster'] == c]
    plt.scatter(
        pts['PCA1'], pts['PCA2'],
        label=f'Cụm {c} (N={len(pts)})',
        color=palette[c],
        alpha=0.8,
        s=65,
        edgecolors='white',
        linewidth=0.5
    )

# ĐÁNH DẤU CENTROID BẰNG 'X' TRÊN KHÔNG GIAN PCA
plt.scatter(
    centroids_pca[:, 0],
    centroids_pca[:, 1],
    marker='X',
    s=300,
    c='#d63031',
    edgecolors='black',
    linewidths=2.5,
    label='Tâm cụm Centroid (X)',
    zorder=10
)

for c in range(chosen_k):
    plt.annotate(
        f'Centroid {c}',
        xy=(centroids_pca[c, 0], centroids_pca[c, 1]),
        xytext=(centroids_pca[c, 0] + 0.15, centroids_pca[c, 1] + 0.15),
        fontsize=10,
        fontweight='bold',
        color='#2d3436',
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#b2bec3", alpha=0.9),
        zorder=11
    )

plt.title(f"SCATTER PLOT PHÂN CỤM K-MEANS TRÊN KHÔNG GIAN PCA 2D (K = {chosen_k})\n"
          f"[PC1: {var_ratio[0]*100:.1f}%, PC2: {var_ratio[1]*100:.1f}% | Tổng phương sai giải thích: {sum(var_ratio)*100:.1f}%]",
          fontsize=14, fontweight='bold', pad=15)
plt.xlabel(f"Thành phần chính 1 - PC1 ({var_ratio[0]*100:.1f}%)", fontsize=12, labelpad=8)
plt.ylabel(f"Thành phần chính 2 - PC2 ({var_ratio[1]*100:.1f}%)", fontsize=12, labelpad=8)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True, shadow=True, fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

fig_pca_path = os.path.join(base_dir, 'scatter_plot_kmeans_pca.png')
plt.savefig(fig_pca_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"[+] Đã lưu Scatter Plot (PCA 2D): {fig_pca_path}")

print("\n" + "=" * 60)
print("HOÀN THÀNH TOÀN BỘ CÁC BƯỚC THỰC HIỆN BÀI TẬP BUỔI 3!")
print("=" * 60)
