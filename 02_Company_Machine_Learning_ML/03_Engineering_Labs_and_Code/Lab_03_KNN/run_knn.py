"""
HỌC MÁY VÀ ỨNG DỤNG HỌC MÁY - BÀI TẬP THỰC HÀNH BUỔI 5
CHỦ ĐỀ: THUẬT TOÁN K-NEAREST NEIGHBORS (K-NN) TỪ SCRATCH
Sinh viên: Nguyễn Trung Kiên | MSSV: 102230023
Khoa Công nghệ Thông tin - Trường Đại học Bách khoa, ĐH Đà Nẵng (DUT)

Nội dung:
- Giải quyết toàn diện Exercise 01 từ file tài liệu KNN_exercises.pdf
- Khảo sát 6 điểm chưa gán nhãn (A, B, C, D, E, F) trên 6 cấu hình
- So sánh tác động của kích thước láng giềng k in {4, 5, 6} và độ đo (Euclidean vs Manhattan)
- Trực quan hóa và xuất kết quả phân tích chất lượng cao vào thư mục results/
"""

import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import Counter
from typing import List, Tuple, Dict, Any

# Đảm bảo hiển thị Unicode/tiếng Việt trên Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Thiết lập thư mục kết quả
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)

# Cấu hình Matplotlib hiển thị tiếng Việt và font rõ nét
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Segoe UI']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# ==========================================
# 1. SỐ HÓA DỮ LIỆU TỪ HÌNH 1 (FIGURE 1)
# ==========================================
# 31 điểm dữ liệu huấn luyện thuộc 4 lớp
TRAINING_DATA: List[Tuple[float, float, str]] = [
    # y = 9
    (1, 9, 'red triangle'), (3, 9, 'red triangle'), (9, 9, 'blue square'),
    # y = 8
    (4, 8, 'green star'), (7, 8, 'blue square'),
    # y = 7
    (1, 7, 'blue square'), (3, 7, 'blue square'), (4, 7, 'red triangle'), (8, 7, 'green star'),
    # y = 5
    (2, 5, 'black heart'), (3, 5, 'black heart'), (4, 5, 'black heart'),
    (6, 5, 'red triangle'), (8, 5, 'blue square'),
    # y = 4
    (2, 4, 'red triangle'), (4, 4, 'green star'),
    # y = 3
    (1, 3, 'black heart'), (3, 3, 'black heart'), (5, 3, 'blue square'), (8, 3, 'blue square'),
    # y = 2
    (1, 2, 'red triangle'), (2, 2, 'black heart'), (4, 2, 'black heart'),
    (6, 2, 'red triangle'), (8, 2, 'green star'), (9, 2, 'blue square'),
    # y = 1
    (1, 1, 'black heart'), (2, 1, 'green star'), (3, 1, 'red triangle'),
    (5, 1, 'black heart'), (8, 1, 'blue square'),
]

# 6 điểm kiểm thử chưa có nhãn cần phân loại
UNLABELED_POINTS: Dict[str, Tuple[float, float]] = {
    'A': (2, 8),
    'B': (6, 7),
    'C': (7, 5),
    'D': (2, 3),
    'E': (7, 2),
    'F': (4, 1)
}

# Cấu hình màu sắc và ký hiệu hiển thị
CLASS_CONFIG = {
    'red triangle': {'color': '#E63946', 'marker': '^', 'label_vn': 'Tam giác đỏ (Red Triangle)', 'size': 120},
    'blue square': {'color': '#1D3557', 'marker': 's', 'label_vn': 'Vuông xanh (Blue Square)', 'size': 120},
    'green star': {'color': '#2A9D8F', 'marker': '*', 'label_vn': 'Ngôi sao xanh (Green Star)', 'size': 160},
    'black heart': {'color': '#111111', 'marker': 'o', 'label_vn': 'Trái tim đen (Black Heart)', 'size': 110},
}


# ==========================================
# 2. HÀM TÍNH KHOẢNG CÁCH THUẦN TOÁN HỌC
# ==========================================
def euclidean_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Khoảng cách Euclidean L2 norm."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def manhattan_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Khoảng cách Manhattan L1 norm."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# ==========================================
# 3. LỚP THUẬT TOÁN KNN CUSTOM TỪ SCRATCH
# ==========================================
class KNNClassifierScratch:
    def __init__(self, training_data: List[Tuple[float, float, str]]):
        self.training_data = training_data

    def get_sorted_neighbors(self, target_point: Tuple[float, float], metric: str = 'euclidean') -> List[Dict[str, Any]]:
        """Tính toán và sắp xếp tất cả các láng giềng theo khoảng cách tăng dần."""
        dist_fn = euclidean_distance if metric.lower() == 'euclidean' else manhattan_distance
        neighbor_table = []
        for x, y, label in self.training_data:
            d = dist_fn(target_point, (x, y))
            neighbor_table.append({
                'coord': (x, y),
                'label': label,
                'distance': d
            })
        # Sắp xếp ổn định (stable sort): nếu khoảng cách bằng nhau, tie-break theo tọa độ x, y
        neighbor_table.sort(key=lambda item: (round(item['distance'], 6), item['coord']))
        return neighbor_table

    def predict(self, target_point: Tuple[float, float], k: int = 5, metric: str = 'euclidean') -> Dict[str, Any]:
        """Phân loại điểm mục tiêu với số lượng k láng giềng và độ đo khoảng cách cho trước."""
        neighbors = self.get_sorted_neighbors(target_point, metric=metric)
        k_nearest = neighbors[:k]

        # Đếm số phiếu theo từng lớp
        labels = [item['label'] for item in k_nearest]
        vote_counts = Counter(labels)

        # Xác định lớp chiến thắng hoặc hòa phiếu
        max_votes = max(vote_counts.values())
        top_classes = [cls for cls, count in vote_counts.items() if count == max_votes]

        is_tie = len(top_classes) > 1
        predicted_label = top_classes[0] if not is_tie else "TIE: " + "/".join(top_classes)

        return {
            'target_point': target_point,
            'k': k,
            'metric': metric,
            'neighbors': neighbors,
            'k_nearest': k_nearest,
            'vote_counts': dict(vote_counts),
            'top_classes': top_classes,
            'is_tie': is_tie,
            'predicted_label': predicted_label
        }


# ==========================================
# 4. THỰC HIỆN TOÀN BỘ 6 CẤU HÌNH CHO 6 ĐIỂM
# ==========================================
def solve_all_exercise_settings(clf: KNNClassifierScratch) -> Dict[str, Dict[str, Any]]:
    results = {}
    metrics = ['euclidean', 'manhattan']
    k_values = [4, 5, 6]

    for p_name, p_coord in UNLABELED_POINTS.items():
        results[p_name] = {}
        for metric in metrics:
            results[p_name][metric] = {}
            for k in k_values:
                res = clf.predict(p_coord, k=k, metric=metric)
                results[p_name][metric][k] = res
    return results


# ==========================================
# 5. CÁC HÀM TRỰC QUAN HÓA & XUẤT ẢNH
# ==========================================
def plot_dataset_overview():
    """Hình 1: Trực quan hóa toàn bộ 31 điểm huấn luyện và 6 điểm cần phân loại."""
    fig, ax = plt.subplots(figsize=(9, 9))

    # Vẽ lưới nền 0..10
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 10.5)
    ax.set_xticks(range(11))
    ax.set_yticks(range(11))
    ax.grid(True, linestyle='-', color='#CCCCCC', alpha=0.8)

    # Vẽ các điểm huấn luyện theo từng lớp
    for cls_name, cfg in CLASS_CONFIG.items():
        pts = [(x, y) for x, y, l in TRAINING_DATA if l == cls_name]
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        ax.scatter(xs, ys, c=cfg['color'], marker=cfg['marker'], s=cfg['size'],
                   label=cfg['label_vn'], zorder=3, edgecolors='black', linewidths=0.8)

    # Vẽ các điểm chưa gán nhãn A, B, C, D, E, F
    for name, (x, y) in UNLABELED_POINTS.items():
        ax.scatter(x, y, s=400, c='#222222', marker='o', zorder=4, edgecolors='#FFFFFF', linewidths=1.5)
        ax.text(x, y, name, color='white', weight='bold', fontsize=12,
                ha='center', va='center', zorder=5)

    ax.set_title("HÌNH 1: KHÔNG GIAN DỮ LIỆU HUẤN LUYỆN & 6 ĐIỂM CẦN PHÂN LỚP\n(Exercise 01 - Figure 1: Data for k-NN Classification)",
                 fontsize=12, pad=15, weight='bold')
    ax.set_xlabel("Trục X (Đặc trưng 1)", fontsize=11, labelpad=8)
    ax.set_ylabel("Trục Y (Đặc trưng 2)", fontsize=11, labelpad=8)
    ax.legend(loc='upper right', framealpha=0.95, fontsize=9.5)

    out_path = os.path.join(RESULTS_DIR, '01_dataset_visualization.png')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
    print(f"-> Đã lưu biểu đồ: {out_path}")


def plot_point_e_demo(clf: KNNClassifierScratch):
    """Hình 2: Minh họa hình học chuyên sâu cho điểm E (7, 2) với k = 5."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7.5))

    target = UNLABELED_POINTS['E'] # (7, 2)
    res_euc = clf.predict(target, k=5, metric='euclidean')
    res_man = clf.predict(target, k=5, metric='manhattan')

    for ax, res, title, metric in [(ax1, res_euc, "A. Khoảng cách Euclidean (k = 5)", 'euclidean'),
                                   (ax2, res_man, "B. Khoảng cách Manhattan (k = 5)", 'manhattan')]:
        ax.set_xlim(3.5, 10.5)
        ax.set_ylim(-0.5, 6.5)
        ax.set_xticks(range(4, 11))
        ax.set_yticks(range(0, 7))
        ax.grid(True, linestyle=':', color='#BBBBBB')

        # Vẽ các điểm train
        for cls_name, cfg in CLASS_CONFIG.items():
            pts = [(x, y) for x, y, l in TRAINING_DATA if l == cls_name]
            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]
            ax.scatter(xs, ys, c=cfg['color'], marker=cfg['marker'], s=cfg['size'],
                       label=cfg['label_vn'], zorder=3, edgecolors='black', linewidths=0.6, alpha=0.45)

        # Làm nổi bật 5 láng giềng gần nhất
        k_pts = res['k_nearest']
        for rank, item in enumerate(k_pts, 1):
            coord = item['coord']
            label = item['label']
            cfg = CLASS_CONFIG[label]
            ax.scatter(coord[0], coord[1], c=cfg['color'], marker=cfg['marker'], s=cfg['size'] * 2.2,
                       zorder=4, edgecolors='gold', linewidths=2.5)
            # Nối đường ngắm từ E đến láng giềng
            ax.plot([target[0], coord[0]], [target[1], coord[1]], 'k--', alpha=0.5, linewidth=1.2, zorder=2)
            ax.text(coord[0] + 0.12, coord[1] + 0.12, f"#{rank} (d={item['distance']:.2f})",
                    fontsize=8.5, weight='bold', color='#111111', zorder=6,
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFFFEE', alpha=0.8, edgecolor='none'))

        # Vẽ đường biên đẳng cự lân cận lớn nhất (bán kính r = 2.0)
        max_r = k_pts[-1]['distance']
        if metric == 'euclidean':
            # Euclidean contour: đường tròn
            circle = patches.Circle(target, radius=max_r, fill=True, facecolor='#457B9D', alpha=0.12,
                                    edgecolor='#1D3557', linestyle='--', linewidth=1.8, zorder=1)
            ax.add_patch(circle)
            ax.text(target[0], target[1] - max_r - 0.35, f"Bán kính Euclidean R = {max_r:.2f} (Hình tròn)",
                    ha='center', fontsize=9, color='#1D3557', weight='bold')
        else:
            # Manhattan contour: hình thoi nghiêng 45 độ
            diamond_x = [target[0] + max_r, target[0], target[0] - max_r, target[0], target[0] + max_r]
            diamond_y = [target[1], target[1] + max_r, target[1], target[1] - max_r, target[1]]
            ax.plot(diamond_x, diamond_y, color='#E76F51', linestyle='--', linewidth=2.0, zorder=1)
            ax.fill(diamond_x, diamond_y, color='#E76F51', alpha=0.10, zorder=1)
            ax.text(target[0], target[1] - max_r - 0.35, f"Bán kính Manhattan R = {max_r:.1f} (Hình thoi)",
                    ha='center', fontsize=9, color='#E76F51', weight='bold')

        # Vẽ điểm E
        ax.scatter(target[0], target[1], s=500, c='black', marker='o', zorder=5, edgecolors='gold', linewidths=2.5)
        ax.text(target[0], target[1], 'E', color='white', weight='bold', fontsize=13, ha='center', va='center', zorder=6)

        # Chú thích kết quả bỏ phiếu
        votes_str = "\n".join([f"• {k}: {v} phiếu" for k, v in res['vote_counts'].items()])
        info_text = f"Kết quả bỏ phiếu (k = 5):\n{votes_str}\n\n=> DỰ ĐOÁN: BLUE SQUARE (3/5)"
        ax.text(0.04, 0.96, info_text, transform=ax.transAxes, verticalalignment='top',
                fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#F8F9FA', edgecolor='#2B2D42', alpha=0.95))

        ax.set_title(title, fontsize=12, pad=10, weight='bold')
        ax.set_xlabel("Tọa độ X", fontsize=10)
        ax.set_ylabel("Tọa độ Y", fontsize=10)

    fig.suptitle("MINH HỌA TOÁN HỌC: PHÂN LỚP ĐIỂM E (7, 2) VỚI K = 5 TỪ SCRATCH\n(So sánh Đẳng cự Euclidean vs Manhattan)",
                 fontsize=14, weight='bold', y=0.98)
    plt.tight_layout()
    out_path = os.path.join(RESULTS_DIR, '02_point_E_demo_k5.png')
    plt.savefig(out_path)
    plt.close()
    print(f"-> Đã lưu biểu đồ: {out_path}")


def plot_decision_boundary_comparison(clf: KNNClassifierScratch):
    """Hình 3: Lưới ranh giới phân loại (Decision Boundaries) toàn bộ không gian 10x10."""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    label_to_id = {'red triangle': 0, 'blue square': 1, 'green star': 2, 'black heart': 3}
    cmap_colors = ['#FFAAA6', '#A8DADC', '#B7E4C7', '#D3D3D3']
    from matplotlib.colors import ListedColormap
    custom_cmap = ListedColormap(cmap_colors)

    # Tạo lưới phân giải 80x80
    grid_x, grid_y = np.meshgrid(np.linspace(0, 10, 80), np.linspace(0, 10, 80))
    grid_points = np.c_[grid_x.ravel(), grid_y.ravel()]

    configs = [
        ('euclidean', 4, axes[0, 0]), ('euclidean', 5, axes[0, 1]), ('euclidean', 6, axes[0, 2]),
        ('manhattan', 4, axes[1, 0]), ('manhattan', 5, axes[1, 1]), ('manhattan', 6, axes[1, 2])
    ]

    for metric, k, ax in configs:
        preds = []
        for pt in grid_points:
            res = clf.predict((pt[0], pt[1]), k=k, metric=metric)
            # Nếu hòa phiếu, gán cho lớp có láng giềng gần nhất đầu tiên
            top_label = res['k_nearest'][0]['label'] if res['is_tie'] else res['top_classes'][0]
            preds.append(label_to_id[top_label])

        z = np.array(preds).reshape(grid_x.shape)
        ax.contourf(grid_x, grid_y, z, levels=[-0.5, 0.5, 1.5, 2.5, 3.5], cmap=custom_cmap, alpha=0.55)

        # Vẽ các điểm train
        for cls_name, cfg in CLASS_CONFIG.items():
            pts = [(x, y) for x, y, l in TRAINING_DATA if l == cls_name]
            ax.scatter([p[0] for p in pts], [p[1] for p in pts], c=cfg['color'], marker=cfg['marker'],
                       s=35, edgecolors='black', linewidths=0.4, alpha=0.8)

        # Vẽ 6 điểm chưa gán nhãn
        for name, (x, y) in UNLABELED_POINTS.items():
            ax.scatter(x, y, s=120, c='black', marker='o', edgecolors='white', linewidths=1.0)
            ax.text(x, y, name, color='white', weight='bold', fontsize=7.5, ha='center', va='center')

        ax.set_title(f"{metric.capitalize()} | k = {k}", fontsize=11, weight='bold')
        ax.set_xticks(range(0, 11, 2))
        ax.set_yticks(range(0, 11, 2))
        ax.grid(True, linestyle=':', alpha=0.5)

    fig.suptitle("MA TRẬN BIÊN QUYẾT ĐỊNH (DECISION BOUNDARIES) CỦA KNN QUA 6 CẤU HÌNH",
                 fontsize=14, weight='bold', y=0.98)
    plt.tight_layout()
    out_path = os.path.join(RESULTS_DIR, '03_decision_boundary_comparison.png')
    plt.savefig(out_path)
    plt.close()
    print(f"-> Đã lưu biểu đồ: {out_path}")


def plot_summary_table(results: Dict[str, Dict[str, Any]]):
    """Hình 4: Bảng ma trận tổng hợp kết quả phân lớp của 6 điểm."""
    fig, ax = plt.subplots(figsize=(13, 4.5))
    ax.axis('off')

    columns = [
        "Điểm\n(Point)", "Tọa độ\n(x, y)",
        "Euclidean\nk = 4", "Euclidean\nk = 5", "Euclidean\nk = 6",
        "Manhattan\nk = 4", "Manhattan\nk = 5", "Manhattan\nk = 6"
    ]

    table_data = []
    cell_colors = []

    for name in ['A', 'B', 'C', 'D', 'E', 'F']:
        coord = UNLABELED_POINTS[name]
        row = [name, f"({coord[0]}, {coord[1]})"]
        color_row = ['#F8F9FA', '#F8F9FA']

        for metric in ['euclidean', 'manhattan']:
            for k in [4, 5, 6]:
                res = results[name][metric][k]
                pred = res['predicted_label']
                if res['is_tie']:
                    text = f"TIE\n({', '.join([c.split()[0] for c in res['top_classes']])})"
                    color = '#FFE5D9' # Cam nhạt cảnh báo hòa phiếu
                else:
                    text = pred.title()
                    color = '#D8F3DC' if 'blue' in pred or 'black' in pred else '#FFF3B0'
                row.append(text)
                color_row.append(color)

        table_data.append(row)
        cell_colors.append(color_row)

    table = ax.table(cellText=table_data, cellColours=cell_colors, colLabels=columns,
                     loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.0, 2.0)

    # Định dạng header
    for (i, j), cell in table.get_celld().items():
        if i == 0:
            cell.set_facecolor('#1D3557')
            cell.set_text_props(color='white', weight='bold')
            cell.set_height(0.12)
        cell.set_edgecolor('#ADB5BD')

    ax.set_title("BẢNG TỔNG HỢP KẾT QUẢ PHÂN LỚP 6 ĐIỂM TEST QUA 6 CẤU HÌNH (CONSOLIDATED MATRIX)",
                 fontsize=12, weight='bold', pad=20)

    plt.tight_layout()
    out_path = os.path.join(RESULTS_DIR, '04_summary_classification_table.png')
    plt.savefig(out_path)
    plt.close()
    print(f"-> Đã lưu bảng tổng hợp: {out_path}")


# ==========================================
# 6. HÀM MAIN THỰC THI TOÀN BỘ BÀI LAB
# ==========================================
def main():
    print("=" * 80)
    print("HỌC MÁY VÀ ỨNG DỤNG HỌC MÁY - BÀI TẬP THỰC HÀNH BUỔI 5: K-NN TỪ SCRATCH")
    print("Sinh viên: Nguyễn Trung Kiên | MSSV: 102230023 | Lớp: Khoa CNTT - DUT")
    print("=" * 80)

    clf = KNNClassifierScratch(TRAINING_DATA)

    # 1. Sinh các biểu đồ
    print("\n[BƯỚC 1/3] Trực quan hóa dữ liệu và xuất biểu đồ...")
    plot_dataset_overview()
    plot_point_e_demo(clf)
    plot_decision_boundary_comparison(clf)

    # 2. Tính toán toàn bộ cấu hình
    print("\n[BƯỚC 2/3] Thực thi tính toán phân lớp toàn bộ 6 cấu hình cho 6 điểm...")
    results = solve_all_exercise_settings(clf)
    plot_summary_table(results)

    # 3. Minh họa Demo điểm E với k = 5 (Yêu cầu câu c)
    print("\n[BƯỚC 3/3] Thực thi Demonstration cho Điểm E với k = 5:")
    print("--------------------------------------------------------------------------------")
    target_e = UNLABELED_POINTS['E']
    clf.predict(target_e, k=5, metric='euclidean')
    clf.predict(target_e, k=5, metric='manhattan')

    print("=" * 80)
    print("HOÀN THÀNH TẤT CẢ CÁC BƯỚC THỰC THI THÀNH CÔNG! HÃY KIỂM TRA THƯ MỤC results/")
    print("=" * 80)


if __name__ == '__main__':
    main()
