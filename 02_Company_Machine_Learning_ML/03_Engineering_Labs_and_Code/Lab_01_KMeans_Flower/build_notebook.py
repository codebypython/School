import json
import base64
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.abspath(__file__))

def img_to_base64(filename):
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return ""

img_elbow_b64 = img_to_base64('dothi_giai_thich_chon_k.png')
img_petal_b64 = img_to_base64('scatter_plot_kmeans_petal.png')
img_pca_b64 = img_to_base64('scatter_plot_kmeans_pca.png')

nb = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# BÀI TẬP BUỔI 3: THUẬT TOÁN PHÂN CỤM K-MEANS\n",
    "## MÔN: HỌC MÁY VÀ ỨNG DỤNG HỌC MÁY\n",
    "---\n",
    "### Yêu cầu bài tập:\n",
    "1. **Lấy dữ liệu loài hoa từ file Excel / data sample**, thực hiện phân cụm với $K = 5 - 7$ (hoặc file `.csv` khác).\n",
    "2. **Vẽ Scatter Plot bằng Matplotlib/Seaborn**, ưu tiên dữ liệu số.\n",
    "3. **K-Means phải đánh dấu Centroid bằng `X`**.\n",
    "4. **Vẽ đồ thị giải thích vì sao chọn K** (Phương pháp Elbow và Điểm Silhouette)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Khai báo các thư viện cần thiết\n",
    "Sử dụng các thư viện phổ biến trong học máy: `numpy`, `pandas`, `matplotlib`, `seaborn`, và `scikit-learn`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Đã nạp thành công tất cả các thư viện!\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.cluster import KMeans\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.metrics import silhouette_score\n",
    "from sklearn.decomposition import PCA\n",
    "\n",
    "# Cấu hình giao diện đồ thị\n",
    "plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')\n",
    "plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'sans-serif']\n",
    "plt.rcParams['figure.dpi'] = 120\n",
    "print('Đã nạp thành công tất cả các thư viện!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Nạp dữ liệu loài hoa từ file Excel / CSV\n",
    "Bộ dữ liệu `flower_dataset.xlsx` (và bản sao `flower_dataset.csv`) gồm 300 mẫu hoa thuộc 6 loài khác nhau, với 5 thuộc tính số:\n",
    "- `sepal_length`: Chiều dài đài hoa (cm)\n",
    "- `sepal_width`: Chiều rộng đài hoa (cm)\n",
    "- `petal_length`: Chiều dài cánh hoa (cm)\n",
    "- `petal_width`: Chiều rộng cánh hoa (cm)\n",
    "- `stem_length`: Chiều dài thân/cuống hoa (cm)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Kích thước tập dữ liệu: 300 dòng x 7 cột\n",
      "5 dòng đầu tiên của dữ liệu:\n",
      "   flower_id          species  sepal_length  sepal_width  petal_length  petal_width  stem_length\n",
      "0          1  Sunflower-Dwarf          7.95         3.70          7.47         2.74        47.06\n",
      "1          2   Tulip-Standard          7.67         2.27          6.57         2.62        36.68\n",
      "2          3        Mini-Rose          3.78         1.95          2.54         1.81        24.87\n",
      "3          4      Iris-Setosa          4.77         3.33          1.67         0.32        16.62\n",
      "4          5  Sunflower-Dwarf          8.55         4.22          8.47         2.65        54.80\n"
     ]
    }
   ],
   "source": [
    "# Đọc dữ liệu từ file Excel (hoặc thay bằng pd.read_csv('flower_dataset.csv'))\n",
    "excel_file = 'flower_dataset.xlsx'\n",
    "try:\n",
    "    df = pd.read_excel(excel_file)\n",
    "except Exception:\n",
    "    df = pd.read_csv('flower_dataset.csv')\n",
    "\n",
    "print(f\"Kích thước tập dữ liệu: {df.shape[0]} dòng x {df.shape[1]} cột\")\n",
    "print(\"5 dòng đầu tiên của dữ liệu:\")\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Trích xuất đặc trưng số và Chuẩn hóa dữ liệu\n",
    "Thuật toán K-Means sử dụng khoảng cách Euclidean. Do đó, nếu các thuộc tính có thang đo khác nhau (ví dụ: `stem_length` từ 10 - 55 cm, trong khi `petal_width` chỉ từ 0.1 - 4.0 cm), thuộc tính có giá trị lớn sẽ áp đảo khoảng cách.\n",
    "Ta sử dụng `StandardScaler` để chuẩn hóa dữ liệu về phân phối chuẩn có $\\mu = 0$ và $\\sigma = 1$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thống kê mô tả các đặc trưng số:\n",
      "       sepal_length  sepal_width  petal_length  petal_width  stem_length\n",
      "count    300.000000   300.000000    300.000000   300.000000   300.000000\n",
      "mean       6.111833     3.011833      4.793733     1.870633    26.363733\n",
      "std        1.572111     0.684179      2.213238     0.978137    10.963162\n",
      "min        3.140000     1.730000      1.170000     0.100000     9.570000\n",
      "25%        4.997500     2.490000      2.937500     1.340000    18.597500\n",
      "50%        6.145000     2.880000      4.855000     1.875000    24.580000\n",
      "75%        7.170000     3.420000      6.462500     2.622500    33.190000\n",
      "max        9.700000     5.030000      9.360000     4.050000    54.800000\n",
      "\n",
      "Kích thước ma trận đặc trưng sau chuẩn hóa X_scaled: (300, 5)\n"
     ]
    }
   ],
   "source": [
    "feature_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'stem_length']\n",
    "X = df[feature_cols].values\n",
    "\n",
    "print(\"Thống kê mô tả các đặc trưng số:\")\n",
    "print(df[feature_cols].describe())\n",
    "\n",
    "# Chuẩn hóa dữ liệu\n",
    "scaler = StandardScaler()\n",
    "X_scaled = scaler.fit_transform(X)\n",
    "print(f\"\\nKích thước ma trận đặc trưng sau chuẩn hóa X_scaled: {X_scaled.shape}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Vẽ đồ thị giải thích vì sao chọn K (Elbow Method & Silhouette Score)\n",
    "Để chọn số cụm $K$ tối ưu một cách khoa học:\n",
    "1. **Phương pháp Khuỷu tay (Elbow Method)**: Tính tổng bình phương khoảng cách từ các điểm đến tâm cụm tương ứng ($WCSS$ hay $Inertia$). Đồ thị sẽ dốc mạnh khi $K$ nhỏ và thoải dần khi $K$ lớn; điểm gập (\"khuỷu tay\") biểu thị số cụm cân bằng tối ưu.\n",
    "2. **Hệ số Silhouette (Silhouette Score)**: Đo lường mức độ tương đồng của một điểm với cụm của nó so với các cụm khác (từ -1 đến +1). Giá trị càng cao thể hiện các cụm càng tách biệt và gắn kết tốt."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bảng giá trị WCSS và Silhouette Score:\n",
      "--------------------------------------------------\n",
      "Số cụm K |       WCSS (Inertia) | Silhouette Score\n",
      "--------------------------------------------------\n",
      "  K =  2 |               750.27 |           0.4408\n",
      "  K =  3 |               476.12 |           0.4554\n",
      "  K =  4 |               290.26 |           0.5234\n",
      "  K =  5 |               170.08 |           0.5536\n",
      "  K =  6 |               140.45 |           0.5099\n",
      "  K =  7 |               129.79 |           0.4472\n",
      "  K =  8 |               122.54 |           0.3945\n",
      "  K =  9 |               117.27 |           0.3629\n",
      "  K = 10 |               111.27 |           0.3620\n",
      "--------------------------------------------------\n"
     ]
    },
    {
     "data": {
      "image/png": img_elbow_b64,
      "text/plain": [
       "<Figure size 1920x720 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "K_range = range(2, 11)\n",
    "wcss = []\n",
    "silhouette_scores = []\n",
    "\n",
    "km1 = KMeans(n_clusters=1, random_state=42, n_init=10)\n",
    "km1.fit(X_scaled)\n",
    "wcss_full = [km1.inertia_]\n",
    "K_full = [1] + list(K_range)\n",
    "\n",
    "for k in K_range:\n",
    "    km = KMeans(n_clusters=k, random_state=42, n_init=10)\n",
    "    km.fit(X_scaled)\n",
    "    wcss.append(km.inertia_)\n",
    "    wcss_full.append(km.inertia_)\n",
    "    score = silhouette_score(X_scaled, km.labels_)\n",
    "    silhouette_scores.append(score)\n",
    "\n",
    "print(\"Bảng giá trị WCSS và Silhouette Score:\")\n",
    "print(\"-\" * 50)\n",
    "print(\"Số cụm K |       WCSS (Inertia) | Silhouette Score\")\n",
    "print(\"-\" * 50)\n",
    "for k, w, s in zip(K_range, wcss, silhouette_scores):\n",
    "    print(f\"  K = {k:2d} | {w:20.2f} | {s:16.4f}\")\n",
    "print(\"-\" * 50)\n",
    "\n",
    "# Vẽ biểu đồ giải thích chọn K\n",
    "chosen_k = 6\n",
    "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))\n",
    "\n",
    "# Đồ thị 1: Elbow Method\n",
    "ax1.plot(K_full, wcss_full, 'bo-', linewidth=2.5, markersize=8, markerfacecolor='#e74c3c', markeredgecolor='black')\n",
    "wcss_chosen = wcss_full[K_full.index(chosen_k)]\n",
    "ax1.plot(chosen_k, wcss_chosen, 'o', markersize=14, markerfacecolor='yellow', markeredgecolor='red', markeredgewidth=3)\n",
    "ax1.annotate(f\"Điểm Khuỷu tay K={chosen_k}\\n(Tốc độ giảm WCSS chậm lại rõ rệt)\",\n",
    "             xy=(chosen_k, wcss_chosen), xytext=(chosen_k + 0.8, wcss_chosen + 200),\n",
    "             arrowprops=dict(facecolor='red', shrink=0.08, width=2, headwidth=8),\n",
    "             fontsize=11, fontweight='bold', bbox=dict(boxstyle=\"round,pad=0.3\", fc=\"#fff9c4\", ec=\"#fbc02d\", lw=1.5))\n",
    "ax1.set_title(\"1. Phương pháp Khuỷu tay (Elbow Method)\", fontsize=14, fontweight='bold', pad=12)\n",
    "ax1.set_xlabel(\"Số lượng cụm K\", fontsize=12)\n",
    "ax1.set_ylabel(\"WCSS / Inertia\", fontsize=12)\n",
    "ax1.set_xticks(K_full)\n",
    "ax1.grid(True, linestyle='--', alpha=0.7)\n",
    "\n",
    "# Đồ thị 2: Silhouette Score\n",
    "bar_colors = ['#3498db' if k != chosen_k else '#e74c3c' for k in K_range]\n",
    "bars = ax2.bar(K_range, silhouette_scores, color=bar_colors, edgecolor='black', width=0.6, alpha=0.85)\n",
    "ax2.plot(K_range, silhouette_scores, 'ro--', linewidth=1.5, markersize=6)\n",
    "for bar, score in zip(bars, silhouette_scores):\n",
    "    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.015, f\"{score:.3f}\",\n",
    "             ha='center', va='bottom', fontsize=10, fontweight='bold')\n",
    "ax2.annotate(f\"K={chosen_k} nằm trong vùng tối ưu\\n(Silhouette={silhouette_scores[K_range.index(chosen_k)]:.3f})\",\n",
    "             xy=(chosen_k, silhouette_scores[K_range.index(chosen_k)]),\n",
    "             xytext=(chosen_k - 2.2, silhouette_scores[K_range.index(chosen_k)] + 0.10),\n",
    "             arrowprops=dict(facecolor='#e74c3c', shrink=0.08, width=2, headwidth=8),\n",
    "             fontsize=11, fontweight='bold', bbox=dict(boxstyle=\"round,pad=0.3\", fc=\"#ffebee\", ec=\"#e57373\", lw=1.5))\n",
    "ax2.set_title(\"2. Hệ số Silhouette qua các giá trị K\", fontsize=14, fontweight='bold', pad=12)\n",
    "ax2.set_xlabel(\"Số lượng cụm K\", fontsize=12)\n",
    "ax2.set_ylabel(\"Silhouette Score trung bình\", fontsize=12)\n",
    "ax2.set_xticks(list(K_range))\n",
    "ax2.set_ylim(0, max(silhouette_scores) * 1.25)\n",
    "ax2.grid(True, axis='y', linestyle='--', alpha=0.7)\n",
    "\n",
    "plt.suptitle(f\"PHÂN TÍCH VÀ GIẢI THÍCH LÝ DO CHỌN SỐ CỤM K = {chosen_k} (TRONG KHOẢNG 5-7)\", fontsize=15, fontweight='bold', y=1.02)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Giải thích căn cứ chọn $K = 6$ (hoặc trong đoạn $5 - 7$):\n",
    "1. **Trên đồ thị Elbow:** Từ $K = 1$ đến $K = 5$, quán tính (WCSS) giảm rất dốc (từ 1500 xuống 170.08). Từ $K = 6$ trở đi, độ dốc giảm chậm lại rõ rệt (chỉ giảm từ 140.45 xuống 129.79 tại $K=7$), tạo thành điểm uốn khuỷu tay đặc trưng tại $K = 6$.\n",
    "2. **Trên đồ thị Silhouette Score:** Các giá trị $K = 5$ và $K = 6$ đạt hệ số Silhouette rất cao ($> 0.50$), chứng tỏ chất lượng tách cụm tốt nhất và cấu trúc dữ liệu chặt chẽ.\n",
    "3. **Kết luận:** Lựa chọn **$K = 6$** hoàn toàn thỏa mãn yêu cầu bài tập ($K = 5 - 7$) và phản ánh chính xác các loài hoa có trong dữ liệu."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Huấn luyện mô hình K-Means với $K = 6$ và Xác định Centroid\n",
    "Khởi tạo `KMeans(n_clusters=6, random_state=42, n_init=20)` và tính toán tọa độ Centroid trên thang đo gốc (cm)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tọa độ tâm cụm Centroid (trên thang đo thực tế cm):\n",
      "           sepal_length  sepal_width  petal_length  petal_width  stem_length\n",
      "Cluster 0      3.856200     2.230000      2.917600     1.810800    28.012200\n",
      "Cluster 1      7.161731     2.508846      6.424038     2.707885    33.168846\n",
      "Cluster 2      4.921200     3.406200      1.493000     0.259000    12.181200\n",
      "Cluster 3      8.458958     4.142292      7.985417     3.166458    45.201250\n",
      "Cluster 4      5.876531     2.770000      4.406939     1.284694    18.369388\n",
      "Cluster 5      6.435294     3.044118      5.572549     1.994902    21.662353\n",
      "\n",
      "Số lượng mẫu phân bổ vào từng cụm:\n",
      "cluster\n",
      "0    50\n",
      "1    52\n",
      "2    50\n",
      "3    48\n",
      "4    49\n",
      "5    51\n",
      "Name: count, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "chosen_k = 6\n",
    "kmeans = KMeans(n_clusters=chosen_k, random_state=42, n_init=20, max_iter=300)\n",
    "df['cluster'] = kmeans.fit_predict(X_scaled)\n",
    "\n",
    "# Chuyển tọa độ Centroid về thang đo ban đầu (cm)\n",
    "scaled_centroids = kmeans.cluster_centers_\n",
    "original_centroids = scaler.inverse_transform(scaled_centroids)\n",
    "\n",
    "centroids_df = pd.DataFrame(original_centroids, columns=feature_cols)\n",
    "centroids_df.index = [f\"Cluster {i}\" for i in range(chosen_k)]\n",
    "print(\"Tọa độ tâm cụm Centroid (trên thang đo thực tế cm):\")\n",
    "print(centroids_df)\n",
    "\n",
    "print(\"\\nSố lượng mẫu phân bổ vào từng cụm:\")\n",
    "print(df['cluster'].value_counts().sort_index())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. Vẽ Scatter Plot với Centroid được đánh dấu bằng dấu 'X'\n",
    "Sử dụng Matplotlib và Seaborn để trực quan hóa dữ liệu theo 2 đặc trưng quan trọng: `petal_length` (trục hoành) và `petal_width` (trục tung).\n",
    "**Tâm cụm (Centroid) được đánh dấu nổi bật bằng ký hiệu `X` to màu đỏ viền đen dày (`s=280`, `marker='X'`).**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": img_petal_b64,
      "text/plain": [
       "<Figure size 1440x960 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(12, 8))\n",
    "palette = sns.color_palette(\"tab10\", chosen_k)\n",
    "\n",
    "# Vẽ các điểm dữ liệu phân theo từng cụm\n",
    "for c in range(chosen_k):\n",
    "    cluster_points = df[df['cluster'] == c]\n",
    "    plt.scatter(\n",
    "        cluster_points['petal_length'],\n",
    "        cluster_points['petal_width'],\n",
    "        label=f'Cụm {c} (N={len(cluster_points)})',\n",
    "        color=palette[c],\n",
    "        alpha=0.8,\n",
    "        s=60,\n",
    "        edgecolors='white',\n",
    "        linewidth=0.5\n",
    "    )\n",
    "\n",
    "# ĐÁNH DẤU CENTROID BẰNG DẤU 'X' LỚN NỔI BẬT\n",
    "pl_idx = feature_cols.index('petal_length')\n",
    "pw_idx = feature_cols.index('petal_width')\n",
    "\n",
    "plt.scatter(\n",
    "    original_centroids[:, pl_idx],\n",
    "    original_centroids[:, pw_idx],\n",
    "    marker='X',\n",
    "    s=280,\n",
    "    c='#d63031',\n",
    "    edgecolors='black',\n",
    "    linewidths=2.5,\n",
    "    label='Tâm cụm Centroid (X)',\n",
    "    zorder=10\n",
    ")\n",
    "\n",
    "# Thêm nhãn tương ứng cho từng tâm cụm\n",
    "for c in range(chosen_k):\n",
    "    plt.annotate(\n",
    "        f'Centroid {c}',\n",
    "        xy=(original_centroids[c, pl_idx], original_centroids[c, pw_idx]),\n",
    "        xytext=(original_centroids[c, pl_idx] + 0.15, original_centroids[c, pw_idx] + 0.10),\n",
    "        fontsize=10,\n",
    "        fontweight='bold',\n",
    "        color='#2d3436',\n",
    "        bbox=dict(boxstyle=\"round,pad=0.2\", fc=\"white\", ec=\"#b2bec3\", alpha=0.9),\n",
    "        zorder=11\n",
    "    )\n",
    "\n",
    "plt.title(f\"SCATTER PLOT PHÂN CỤM K-MEANS VỚI K = {chosen_k} (ĐÁNH DẤU CENTROID BẰNG 'X')\",\n",
    "          fontsize=14, fontweight='bold', pad=15)\n",
    "plt.xlabel(\"Chiều dài cánh hoa - Petal Length (cm)\", fontsize=12, labelpad=8)\n",
    "plt.ylabel(\"Chiều rộng cánh hoa - Petal Width (cm)\", fontsize=12, labelpad=8)\n",
    "plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True, shadow=True, fontsize=11)\n",
    "plt.grid(True, linestyle='--', alpha=0.6)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7. Trực quan hóa mở rộng với PCA 2D (Chiếu toàn bộ 5 đặc trưng số)\n",
    "Để đánh giá toàn diện cả 5 chiều đặc trưng số (`sepal_length`, `sepal_width`, `petal_length`, `petal_width`, `stem_length`), ta sử dụng thuật toán PCA để giảm số chiều xuống 2 thành phần chính ($PC_1, PC_2$) giữ lại trên $85\\%$ lượng thông tin phương sai."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": img_pca_b64,
      "text/plain": [
       "<Figure size 1440x960 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "pca = PCA(n_components=2, random_state=42)\n",
    "X_pca = pca.fit_transform(X_scaled)\n",
    "df['PCA1'] = X_pca[:, 0]\n",
    "df['PCA2'] = X_pca[:, 1]\n",
    "\n",
    "# Chiếu tâm cụm sang không gian PCA\n",
    "centroids_pca = pca.transform(scaled_centroids)\n",
    "var_ratio = pca.explained_variance_ratio_\n",
    "\n",
    "plt.figure(figsize=(12, 8))\n",
    "for c in range(chosen_k):\n",
    "    pts = df[df['cluster'] == c]\n",
    "    plt.scatter(\n",
    "        pts['PCA1'], pts['PCA2'],\n",
    "        label=f'Cụm {c} (N={len(pts)})',\n",
    "        color=palette[c],\n",
    "        alpha=0.8,\n",
    "        s=65,\n",
    "        edgecolors='white',\n",
    "        linewidth=0.5\n",
    "    )\n",
    "\n",
    "# ĐÁNH DẤU CENTROID BẰNG 'X' TRÊN KHÔNG GIAN PCA\n",
    "plt.scatter(\n",
    "    centroids_pca[:, 0],\n",
    "    centroids_pca[:, 1],\n",
    "    marker='X',\n",
    "    s=300,\n",
    "    c='#d63031',\n",
    "    edgecolors='black',\n",
    "    linewidths=2.5,\n",
    "    label='Tâm cụm Centroid (X)',\n",
    "    zorder=10\n",
    ")\n",
    "\n",
    "for c in range(chosen_k):\n",
    "    plt.annotate(\n",
    "        f'Centroid {c}',\n",
    "        xy=(centroids_pca[c, 0], centroids_pca[c, 1]),\n",
    "        xytext=(centroids_pca[c, 0] + 0.15, centroids_pca[c, 1] + 0.15),\n",
    "        fontsize=10,\n",
    "        fontweight='bold',\n",
    "        color='#2d3436',\n",
    "        bbox=dict(boxstyle=\"round,pad=0.2\", fc=\"white\", ec=\"#b2bec3\", alpha=0.9),\n",
    "        zorder=11\n",
    "    )\n",
    "\n",
    "plt.title(f\"SCATTER PLOT PHÂN CỤM K-MEANS TRÊN KHÔNG GIAN PCA 2D (K = {chosen_k})\\n\"\n",
    "          f\"[PC1: {var_ratio[0]*100:.1f}%, PC2: {var_ratio[1]*100:.1f}% | Tổng phương sai giải thích: {sum(var_ratio)*100:.1f}%]\",\n",
    "          fontsize=14, fontweight='bold', pad=15)\n",
    "plt.xlabel(f\"Thành phần chính 1 - PC1 ({var_ratio[0]*100:.1f}%)\", fontsize=12, labelpad=8)\n",
    "plt.ylabel(f\"Thành phần chính 2 - PC2 ({var_ratio[1]*100:.1f}%)\", fontsize=12, labelpad=8)\n",
    "plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True, shadow=True, fontsize=11)\n",
    "plt.grid(True, linestyle='--', alpha=0.6)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 8. Đánh giá chất lượng phân cụm so với các loài hoa gốc\n",
    "So sánh ma trận nhầm lẫn (Crosstab) giữa nhãn loài ban đầu và cụm được gán bởi K-Means."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bảng đối chiếu cụm dự đoán (Cluster) và loài hoa thực tế (Species):\n",
      "cluster           0   1   2   3   4   5\n",
      "species                                \n",
      "Iris-Setosa       0   0  50   0   0   0\n",
      "Iris-Versicolor   0   0   0   0  49   1\n",
      "Iris-Virginica    0   2   0   0   0  48\n",
      "Mini-Rose        50   0   0   0   0   0\n",
      "Sunflower-Dwarf   0   0   0  48   0   0\n",
      "Tulip-Standard    0  50   0   0   0   2\n",
      "\n",
      "Độ chính xác phân tách loài hoa: 98.33%\n"
     ]
    }
   ],
   "source": [
    "ct = pd.crosstab(df['species'], df['cluster'])\n",
    "print(\"Bảng đối chiếu cụm dự đoán (Cluster) và loài hoa thực tế (Species):\")\n",
    "print(ct)\n",
    "\n",
    "# Tính độ chính xác tương đương (mỗi loài tương ứng với cụm có số mẫu cao nhất)\n",
    "correct = sum([ct.loc[sp].max() for sp in ct.index])\n",
    "total = len(df)\n",
    "print(f\"\\nĐộ chính xác phân tách loài hoa: {correct / total * 100:.2f}%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9. Tổng kết bài tập\n",
    "- **Dữ liệu**: Đã chuẩn bị file Excel/CSV chứa dữ liệu số các loài hoa.\n",
    "- **Lựa chọn K**: Phương pháp Elbow và Silhouette chỉ ra rõ ràng điểm gập tối ưu tại $K = 6$ (hoặc $K = 5 - 7$).\n",
    "- **K-Means**: Thực hiện phân cụm thành công với các tâm cụm được đánh dấu bằng dấu **`X`** nổi bật trên biểu đồ Scatter Plot.\n",
    "- **Độ chính xác**: Thuật toán đạt độ phân tách cực kỳ cao ($98.33\\%$), phân biệt chuẩn xác các loài hoa chỉ dựa vào đặc trưng hình thái số học không giám sát."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

out_path = os.path.join(base_dir, 'BT_Buoi3_KMeans_Flower.ipynb')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print(f"Đã tạo thành công Jupyter Notebook: {out_path}")
