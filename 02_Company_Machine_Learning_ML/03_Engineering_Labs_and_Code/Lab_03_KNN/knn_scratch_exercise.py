"""
Lab 03: K-Nearest Neighbors (KNN) - Exercise 01 Solution
Cài đặt thuật toán KNN từ Scratch (Không dùng thư viện scikit-learn)
Khoa Công nghệ Thông tin - Trường Đại học Bách khoa, ĐH Đà Nẵng (DUT)
"""

import math
import sys
from collections import Counter
from typing import List, Tuple, Dict, Any

# Đảm bảo hiển thị tiếng Việt và ký tự Unicode trên Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ==========================================
# 1. TẬP DỮ LIỆU HUẤN LUYỆN (TRAINING DATA)
# ==========================================
# Trích xuất từ Hình 1 (Figure 1): 31 điểm huấn luyện thuộc 4 lớp
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

# Tọa độ các điểm kiểm thử chưa có nhãn A, B, C, D, E, F
UNLABELED_POINTS: Dict[str, Tuple[float, float]] = {
    'A': (2, 8),
    'B': (6, 7),
    'C': (7, 5),
    'D': (2, 3),
    'E': (7, 2),
    'F': (4, 1)
}


# ==========================================
# 2. CÁC ĐỘ ĐO KHOẢNG CÁCH (DISTANCE METRICS)
# ==========================================
def calculate_distance(p1: Tuple[float, float], p2: Tuple[float, float], metric: str = 'euclidean') -> float:
    """Tính khoảng cách Euclidean hoặc Manhattan giữa 2 điểm p1 và p2."""
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    if metric.lower() == 'euclidean':
        return math.sqrt(dx ** 2 + dy ** 2)
    elif metric.lower() == 'manhattan':
        return dx + dy
    else:
        raise ValueError(f"Độ đo '{metric}' không được hỗ trợ. Vui lòng chọn 'euclidean' hoặc 'manhattan'.")


# ==========================================
# 3. THUẬT TOÁN KNN TỪ SCRATCH
# ==========================================
class KNNClassifierScratch:
    def __init__(self, training_data: List[Tuple[float, float, str]]):
        self.training_data = training_data

    def predict(self, target_point: Tuple[float, float], k: int = 5, metric: str = 'euclidean', verbose: bool = True) -> Dict[str, Any]:
        """
        Phân loại điểm mục tiêu bằng thuật toán KNN.
        Trả về dictionary chứa toàn bộ bảng khoảng cách, k láng giềng, kết quả bỏ phiếu và nhãn dự đoán.
        """
        # Bước 1: Tính khoảng cách từ điểm mục tiêu đến tất cả điểm huấn luyện
        neighbor_table = []
        for x, y, label in self.training_data:
            d = calculate_distance(target_point, (x, y), metric=metric)
            neighbor_table.append({
                'coord': (x, y),
                'label': label,
                'distance': d
            })

        # Bước 2: Sắp xếp các điểm theo khoảng cách tăng dần
        # Quy tắc tie-break phụ: nếu khoảng cách bằng nhau, sắp xếp theo tọa độ (x, y) để đảm bảo tính xác định
        neighbor_table.sort(key=lambda item: (round(item['distance'], 6), item['coord']))

        # Bước 3: Lấy K láng giềng gần nhất
        k_nearest = neighbor_table[:k]

        # Bước 4: Đếm số phiếu bầu (Majority Voting)
        labels = [item['label'] for item in k_nearest]
        vote_counts = Counter(labels)

        # Kiểm tra hòa phiếu (Tie)
        max_votes = max(vote_counts.values())
        top_classes = [cls for cls, count in vote_counts.items() if count == max_votes]

        # Nhãn dự đoán chính
        predicted_label = top_classes[0] if len(top_classes) == 1 else " / ".join(top_classes) + " (HÒA PHIẾU)"

        if verbose:
            print("=" * 70)
            print(f"🎯 KẾT QUẢ PHÂN LỚP KNN TỪ SCRATCH")
            print(f"- Điểm mục tiêu: {target_point}")
            print(f"- Siêu tham số k: {k}")
            print(f"- Độ đo khoảng cách: {metric.upper()}")
            print("-" * 70)
            print("📋 BẢNG K LÁNG GIỀNG GẦN NHẤT:")
            print(f"{'Thứ hạng':<10}{'Tọa độ (x, y)':<18}{'Khoảng cách':<15}{'Nhãn thực tế':<15}")
            for idx, item in enumerate(k_nearest, start=1):
                coord_str = f"({item['coord'][0]}, {item['coord'][1]})"
                print(f"{idx:<10}{coord_str:<18}{item['distance']:<15.4f}{item['label']:<15}")
            print("-" * 70)
            print(f"📊 PHÂN PHỐI PHIẾU BẦU (VOTE DISTRIBUTION):")
            for cls, count in vote_counts.items():
                print(f"  • {cls:<15}: {count} phiếu")
            print("-" * 70)
            print(f"🏆 NHÃN DỰ ĐOÁN CUỐI CÙNG: {predicted_label}")
            print("=" * 70 + "\n")

        return {
            'target_point': target_point,
            'k': k,
            'metric': metric,
            'k_nearest': k_nearest,
            'vote_counts': dict(vote_counts),
            'predicted_label': predicted_label
        }


# ==========================================
# 4. CHẠY DEMO ĐIỂM E VỚI K = 5 (YÊU CẦU CÂU C)
# ==========================================
if __name__ == '__main__':
    clf = KNNClassifierScratch(TRAINING_DATA)
    point_name = 'E'
    point_coord = UNLABELED_POINTS[point_name]

    print(f"🚀 THỰC THI DEMO KIỂM THỬ CHO ĐIỂM {point_name} {point_coord} VỚI K = 5:\n")
    # Demo 1: Euclidean k = 5
    clf.predict(point_coord, k=5, metric='euclidean', verbose=True)

    # Demo 2: Manhattan k = 5
    clf.predict(point_coord, k=5, metric='manhattan', verbose=True)
