"""
Script tạo file Jupyter Notebook hoàn chỉnh: BT_Buoi5_KNN.ipynb
Tham chiếu theo chuẩn mực bài tập thực hành Lab 01 và Lab 02:
  - Tự xây dựng thuật toán KNN từ Scratch (không dùng hộp đen Scikit-Learn).
  - So sánh chi tiết khoảng cách Euclidean vs Manhattan và khảo sát k in {4, 5, 6}.
  - Trực quan hóa hình học đẳng cự (Isometric Contours) và phân tích hiện tượng hòa phiếu (Tie-breaking).
  - Nhúng ảnh Base64 tự động để Notebook hiển thị độc lập không phụ thuộc đường dẫn cục bộ.
"""

import json
import base64
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(base_dir, 'results')


def img_to_base64(filename):
    filepath = os.path.join(results_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return ""


img_dataset_b64 = img_to_base64('01_dataset_visualization.png')
img_point_e_b64 = img_to_base64('02_point_E_demo_k5.png')
img_boundary_b64 = img_to_base64('03_decision_boundary_comparison.png')
img_table_b64 = img_to_base64('04_summary_classification_table.png')

nb = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# BÀI TẬP BUỔI 5: THUẬT TOÁN K-NEAREST NEIGHBORS (K-NN)\n",
    "## MÔN: HỌC MÁY VÀ ỨNG DỤNG HỌC MÁY\n",
    "### Sinh viên: Nguyễn Trung Kiên | MSSV: 102230023 | Khoa Công nghệ Thông tin - Trường Đại học Bách khoa, ĐH Đà Nẵng\n",
    "---\n",
    "> **Phương châm học tập:** *\"Hiểu thấu bản chất mêtric không gian và thuật toán từ Scratch trước khi gọi thư viện. Phân tích sâu sắc ranh giới quyết định và sự đánh đổi Bias-Variance.\"*\n",
    "\n",
    "### Mục tiêu bài tập (Theo tài liệu `KNN_exercises.pdf` - Exercise 01):\n",
    "1. **Số hóa & Khám phá Dữ liệu:** Khai thác tập dữ liệu 2D gồm **31 điểm huấn luyện** thuộc 4 lớp: $\\mathcal{C} = \\{\\text{red triangle}, \\text{blue square}, \\text{green star}, \\text{black heart}\\}$ và **6 điểm kiểm thử chưa gán nhãn** ($A, B, C, D, E, F$).\n",
    "2. **Câu a - Tính toán từng bước:** Lập bảng khoảng cách và phân lớp cho cả 6 điểm dưới **6 cấu hình** ($k \\in \\{4, 5, 6\\}$ với khoảng cách Euclidean và Manhattan).\n",
    "3. **Câu b - Báo cáo phân tích chuyên sâu:** Khảo sát tác động của kích thước láng giềng $k$, sự khác biệt hình học giữa Euclidean và Manhattan, cùng hiện tượng hòa phiếu (Tie-breaking).\n",
    "4. **Câu c - Cài đặt KNN Scratch:** Viết chương trình Python thuần (không dùng scikit-learn) có hiển thị chi tiết bảng láng giềng, tỷ lệ phiếu bầu và chạy thực nghiệm minh họa cho điểm $E$ với $k = 5$."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Khai báo các thư viện cần thiết\n",
    "Sử dụng các thư viện chuẩn trong tính toán khoa học: `numpy`, `matplotlib`, `math`, `collections.Counter`."
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
      "Đã nạp thành công tất cả các thư viện cần thiết!\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.patches as patches\n",
    "from collections import Counter\n",
    "from typing import List, Tuple, Dict, Any\n",
    "\n",
    "print(\"Đã nạp thành công tất cả các thư viện cần thiết!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Số hóa Không gian Dữ liệu từ Hình 1 (Figure 1)\n",
    "Trích xuất chính xác tọa độ của 31 điểm huấn luyện và 6 điểm cần phân loại trên lưới tọa độ $10 \\times 10$."
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
      "Tổng số điểm huấn luyện: 31 điểm.\n",
      "Phân phối các lớp trong tập huấn luyện:\n",
      "  • red triangle: 8 điểm\n",
      "  • blue square: 9 điểm\n",
      "  • green star: 5 điểm\n",
      "  • black heart: 9 điểm\n"
     ]
    }
   ],
   "source": [
    "# Tập 31 điểm huấn luyện\n",
    "TRAINING_DATA = [\n",
    "    # y = 9\n",
    "    (1, 9, 'red triangle'), (3, 9, 'red triangle'), (9, 9, 'blue square'),\n",
    "    # y = 8\n",
    "    (4, 8, 'green star'), (7, 8, 'blue square'),\n",
    "    # y = 7\n",
    "    (1, 7, 'blue square'), (3, 7, 'blue square'), (4, 7, 'red triangle'), (8, 7, 'green star'),\n",
    "    # y = 5\n",
    "    (2, 5, 'black heart'), (3, 5, 'black heart'), (4, 5, 'black heart'),\n",
    "    (6, 5, 'red triangle'), (8, 5, 'blue square'),\n",
    "    # y = 4\n",
    "    (2, 4, 'red triangle'), (4, 4, 'green star'),\n",
    "    # y = 3\n",
    "    (1, 3, 'black heart'), (3, 3, 'black heart'), (5, 3, 'blue square'), (8, 3, 'blue square'),\n",
    "    # y = 2\n",
    "    (1, 2, 'red triangle'), (2, 2, 'black heart'), (4, 2, 'black heart'),\n",
    "    (6, 2, 'red triangle'), (8, 2, 'green star'), (9, 2, 'blue square'),\n",
    "    # y = 1\n",
    "    (1, 1, 'black heart'), (2, 1, 'green star'), (3, 1, 'red triangle'),\n",
    "    (5, 1, 'black heart'), (8, 1, 'blue square'),\n",
    "]\n",
    "\n",
    "# 6 điểm kiểm thử cần phân loại A, B, C, D, E, F\n",
    "UNLABELED_POINTS = {\n",
    "    'A': (2, 8),\n",
    "    'B': (6, 7),\n",
    "    'C': (7, 5),\n",
    "    'D': (2, 3),\n",
    "    'E': (7, 2),\n",
    "    'F': (4, 1)\n",
    "}\n",
    "\n",
    "print(f\"Tổng số điểm huấn luyện: {len(TRAINING_DATA)} điểm.\")\n",
    "counts = Counter([p[2] for p in TRAINING_DATA])\n",
    "print(\"Phân phối các lớp trong tập huấn luyện:\")\n",
    "for cls, cnt in counts.items():\n",
    "    print(f\"  • {cls}: {cnt} điểm\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Trực quan hóa Không gian Dữ liệu Figure 1\n",
    f"![Hình 1](data:image/png;base64,{img_dataset_b64})" if img_dataset_b64 else "*[Đã xuất biểu đồ vào results/01_dataset_visualization.png]*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Cài đặt Thuật toán KNN từ Scratch (Không dùng Scikit-Learn)\n",
    "Hàm tính khoảng cách Euclidean ($L_2$) và Manhattan ($L_1$):\n",
    "- Euclidean: $d_E(p, q) = \\sqrt{(x_p - x_q)^2 + (y_p - y_q)^2}$\n",
    "- Manhattan: $d_M(p, q) = |x_p - x_q| + |y_p - y_q|$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_distance(p1: Tuple[float, float], p2: Tuple[float, float], metric: str = 'euclidean') -> float:\n",
    "    dx = abs(p1[0] - p2[0])\n",
    "    dy = abs(p1[1] - p2[1])\n",
    "    if metric.lower() == 'euclidean':\n",
    "        return math.sqrt(dx ** 2 + dy ** 2)\n",
    "    elif metric.lower() == 'manhattan':\n",
    "        return dx + dy\n",
    "    else:\n",
    "        raise ValueError(f\"Độ đo '{metric}' không hợp lệ.\")\n",
    "\n",
    "class KNNClassifierScratch:\n",
    "    def __init__(self, training_data: List[Tuple[float, float, str]]):\n",
    "        self.training_data = training_data\n",
    "\n",
    "    def predict(self, target_point: Tuple[float, float], k: int = 5, metric: str = 'euclidean', verbose: bool = False):\n",
    "        neighbor_table = []\n",
    "        for x, y, label in self.training_data:\n",
    "            d = calculate_distance(target_point, (x, y), metric=metric)\n",
    "            neighbor_table.append({'coord': (x, y), 'label': label, 'distance': d})\n",
    "        \n",
    "        # Sắp xếp ổn định theo khoảng cách tăng dần\n",
    "        neighbor_table.sort(key=lambda item: (round(item['distance'], 6), item['coord']))\n",
    "        k_nearest = neighbor_table[:k]\n",
    "        \n",
    "        labels = [item['label'] for item in k_nearest]\n",
    "        vote_counts = Counter(labels)\n",
    "        max_votes = max(vote_counts.values())\n",
    "        top_classes = [cls for cls, cnt in vote_counts.items() if cnt == max_votes]\n",
    "        is_tie = len(top_classes) > 1\n",
    "        predicted_label = top_classes[0] if not is_tie else \"TIE: \" + \"/\".join(top_classes)\n",
    "        \n",
    "        if verbose:\n",
    "            print(f\"🎯 ĐIỂM MỤC TIÊU: {target_point} | k = {k} | Độ đo: {metric.upper()}\")\n",
    "            print(f\"{'Hạng':<6}{'Tọa độ':<16}{'Khoảng cách':<14}{'Nhãn thực tế':<15}\")\n",
    "            for i, it in enumerate(k_nearest, 1):\n",
    "                print(f\"{i:<6}{str(it['coord']):<16}{it['distance']:<14.4f}{it['label']:<15}\")\n",
    "            print(f\"=> Phiếu bầu: {dict(vote_counts)} | Kết quả: {predicted_label}\\n\")\n",
    "            \n",
    "        return {\n",
    "            'k_nearest': k_nearest,\n",
    "            'vote_counts': dict(vote_counts),\n",
    "            'top_classes': top_classes,\n",
    "            'is_tie': is_tie,\n",
    "            'predicted_label': predicted_label\n",
    "        }"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Lời giải Câu a: Bảng Tính toán & Phân lớp Chi tiết 6 Điểm qua 6 Cấu hình\n",
    "Thực thi duyệt qua toàn bộ 6 điểm kiểm thử ($A, B, C, D, E, F$) trên 6 cấu hình độc lập."
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
      "=== BẢNG TỔNG HỢP KẾT QUẢ PHÂN LỚP QUA 6 CẤU HÌNH ===\n",
      "Điểm A (2, 8):\n",
      "  • Euclidean: k=4 -> TIE: blue square/red triangle | k=5 -> TIE: blue square/red triangle | k=6 -> red triangle\n",
      "  • Manhattan: k=4 -> TIE: blue square/red triangle | k=5 -> TIE: blue square/red triangle | k=6 -> TIE: blue square/red triangle\n",
      "Điểm B (6, 7):\n",
      "  • Euclidean: k=4 -> red triangle | k=5 -> TIE: red triangle/green star | k=6 -> TIE: red triangle/green star\n",
      "  • Manhattan: k=4 -> red triangle | k=5 -> TIE: red triangle/blue square | k=6 -> TIE: red triangle/blue square/green star\n",
      "Điểm C (7, 5):\n",
      "  • Euclidean: k=4 -> blue square | k=5 -> blue square | k=6 -> blue square\n",
      "  • Manhattan: k=4 -> blue square | k=5 -> blue square | k=6 -> blue square\n",
      "Điểm D (2, 3):\n",
      "  • Euclidean: k=4 -> black heart | k=5 -> black heart | k=6 -> black heart\n",
      "  • Manhattan: k=4 -> black heart | k=5 -> black heart | k=6 -> black heart\n",
      "Điểm E (7, 2):\n",
      "  • Euclidean: k=4 -> blue square | k=5 -> blue square | k=6 -> blue square\n",
      "  • Manhattan: k=4 -> blue square | k=5 -> blue square | k=6 -> blue square\n",
      "Điểm F (4, 1):\n",
      "  • Euclidean: k=4 -> black heart | k=5 -> black heart | k=6 -> black heart\n",
      "  • Manhattan: k=4 -> black heart | k=5 -> black heart | k=6 -> black heart\n"
     ]
    }
   ],
   "source": [
    "clf = KNNClassifierScratch(TRAINING_DATA)\n",
    "print(\"=== BẢNG TỔNG HỢP KẾT QUẢ PHÂN LỚP QUA 6 CẤU HÌNH ===\")\n",
    "for name, coord in UNLABELED_POINTS.items():\n",
    "    print(f\"Điểm {name} {coord}:\")\n",
    "    for metric in ['euclidean', 'manhattan']:\n",
    "        sub_res = []\n",
    "        for k in [4, 5, 6]:\n",
    "            res = clf.predict(coord, k=k, metric=metric, verbose=False)\n",
    "            sub_res.append(f\"k={k} -> {res['predicted_label']}\")\n",
    "        print(f\"  • {metric.capitalize()}: {' | '.join(sub_res)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Bảng Ma trận Tổng hợp Kết quả Phân loại (Consolidated Matrix)\n",
    f"![Bảng tổng hợp](data:image/png;base64,{img_table_b64})" if img_table_b64 else "*[Đã xuất bảng vào results/04_summary_classification_table.png]*",
    "\n\n",
    "| Điểm | Tọa độ | Euclidean $k=4$ | Euclidean $k=5$ | Euclidean $k=6$ | Manhattan $k=4$ | Manhattan $k=5$ | Manhattan $k=6$ |\n",
    "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n",
    "| **A** | $(2, 8)$ | *Tie (Blue/Red)* | *Tie (Blue/Red)* | **Red Triangle** | *Tie (Blue/Red)* | *Tie (Blue/Red)* | *Tie (Blue/Red)* |\n",
    "| **B** | $(6, 7)$ | **Red Triangle** | *Tie (Red/Green)* | *Tie (Red/Green)* | **Red Triangle** | *Tie (Red/Blue)* | *Tie (3-way)* |\n",
    "| **C** | $(7, 5)$ | **Blue Square** | **Blue Square** | **Blue Square** | **Blue Square** | **Blue Square** | **Blue Square** |\n",
    "| **D** | $(2, 3)$ | **Black Heart** | **Black Heart** | **Black Heart** | **Black Heart** | **Black Heart** | **Black Heart** |\n",
    "| **E** | $(7, 2)$ | **Blue Square** | **Blue Square** | **Blue Square** | **Blue Square** | **Blue Square** | **Blue Square** |\n",
    "| **F** | $(4, 1)$ | **Black Heart** | **Black Heart** | **Black Heart** | **Black Heart** | **Black Heart** | **Black Heart** |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Lời giải Câu b: Báo cáo Phân tích So sánh Toàn diện (Comparative Analysis)\n",
    "\n",
    "### 5.1. Tác động của việc thay đổi kích thước láng giềng $k$ ($k = 4, 5, 6$)\n",
    "1. **Tính bất biến tại các vùng cụm mật độ cao (Dense Core Points):**\n",
    "   - Các điểm $C(7, 5)$, $D(2, 3)$, $E(7, 2)$ và $F(4, 1)$ hoàn toàn **không đổi nhãn dự đoán** khi $k$ tăng từ 4 lên 6. Lý do: mật độ các điểm cùng lớp xung quanh chúng áp đảo hoàn toàn.\n",
    "2. **Hiện tượng bất ổn định tại vùng biên giới phân lớp (Boundary Ambiguity):**\n",
    "   - Điểm $A(2, 8)$: Nằm chính giữa 2 cụm Red Triangle (phía trên) và Blue Square (phía dưới). Tại $k=4$ và $k=5$, số phiếu luôn hòa $2 - 2$. Đến $k=6$ trong Euclidean, việc mở rộng bán kính thu nạp thêm điểm $(4, 7)$ (Red Triangle) giúp lớp này giành chiến thắng.\n",
    "   - Điểm $B(6, 7)$: Với $k=4$, Red Triangle chiếm ưu thế ($2$ phiếu). Nhưng khi mở rộng lên $k=5, 6$, các láng giềng khác (Green Star, Blue Square) xuất hiện làm tỷ lệ phiếu bị phân tán và dẫn đến hòa phiếu.\n",
    "   - **Kết luận:** Số $k$ chẵn ($k=4, 6$) làm tăng nguy cơ hòa phiếu rõ rệt. Tuy nhiên, ở bài toán 4 lớp, $k=5$ lẻ vẫn có thể hòa phiếu nếu 2 lớp dẫn đầu cùng đạt $2$ phiếu.\n",
    "\n",
    "### 5.2. Tác động của độ đo khoảng cách (Euclidean vs. Manhattan)\n",
    "1. **Đường đẳng cự (Isometric Shape):**\n",
    "   - Euclidean đo đường chim bay $\\rightarrow$ hình đẳng cự là **hình tròn** $\\sum (x_i - y_i)^2 = R^2$.\n",
    "   - Manhattan đo đường bàn cờ (taxi-cab) $\\rightarrow$ hình đẳng cự là **hình thoi (Diamond)** nghiêng $45^\\circ$ $|x_1 - x_2| + |y_1 - y_2| = R$.\n",
    "2. **Tác động lên việc xếp hạng láng giềng:**\n",
    "   - Một điểm nằm chéo $(1, 1)$ có khoảng cách Euclidean là $\\sqrt{2} \\approx 1.414 < 2.0$, nhưng có khoảng cách Manhattan là $1 + 1 = 2.0$, ngang bằng với điểm thẳng hàng $(2, 0)$. Do đó, Manhattan tạo ra rất nhiều láng giềng đồng hạng khoảng cách, làm tăng khả năng hòa phiếu ngẫu nhiên."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Ma trận Ranh giới Quyết định (Decision Boundaries) qua 6 Cấu hình\n",
    f"![Ranh giới quyết định](data:image/png;base64,{img_boundary_b64})" if img_boundary_b64 else "*[Đã xuất biểu đồ vào results/03_decision_boundary_comparison.png]*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. Lời giải Câu c: Minh họa Thực nghiệm Điểm E với k = 5\n",
    "Yêu cầu đề bài: Thực thi và in ra console chi tiết các bước tính toán trung gian cho điểm $E = (7, 2)$ với $k = 5$ dưới cả 2 độ đo Euclidean và Manhattan."
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
      "🚀 THỰC THI DEMO MINH HỌA CHO ĐIỂM E (7, 2) VỚI K = 5:\n",
      "\n",
      "🎯 ĐIỂM MỤC TIÊU: (7, 2) | k = 5 | Độ đo: EUCLIDEAN\n",
      "Hạng  Tọa độ          Khoảng cách   Nhãn thực tế   \n",
      "1     (6, 2)          1.0000        red triangle   \n",
      "2     (8, 2)          1.0000        green star     \n",
      "3     (8, 1)          1.4142        blue square    \n",
      "4     (8, 3)          1.4142        blue square    \n",
      "5     (9, 2)          2.0000        blue square    \n",
      "=> Phiếu bầu: {'red triangle': 1, 'green star': 1, 'blue square': 3} | Kết quả: blue square\n",
      "\n",
      "🎯 ĐIỂM MỤC TIÊU: (7, 2) | k = 5 | Độ đo: MANHATTAN\n",
      "Hạng  Tọa độ          Khoảng cách   Nhãn thực tế   \n",
      "1     (6, 2)          1.0000        red triangle   \n",
      "2     (8, 2)          1.0000        green star     \n",
      "3     (8, 1)          2.0000        blue square    \n",
      "4     (8, 3)          2.0000        blue square    \n",
      "5     (9, 2)          2.0000        blue square    \n",
      "=> Phiếu bầu: {'red triangle': 1, 'green star': 1, 'blue square': 3} | Kết quả: blue square\n"
     ]
    }
   ],
   "source": [
    "print(\"🚀 THỰC THI DEMO MINH HỌA CHO ĐIỂM E (7, 2) VỚI K = 5:\\n\")\n",
    "target_e = UNLABELED_POINTS['E']\n",
    "clf.predict(target_e, k=5, metric='euclidean', verbose=True)\n",
    "clf.predict(target_e, k=5, metric='manhattan', verbose=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Trực quan hóa Hình học Bán kính Lân cận Điểm E (Hình tròn vs Hình thoi)\n",
    f"![Minh họa điểm E](data:image/png;base64,{img_point_e_b64})" if img_point_e_b64 else "*[Đã xuất biểu đồ vào results/02_point_E_demo_k5.png]*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7. Tổng kết & Bài học Kỹ nghệ (Engineering Takeaways)\n",
    "\n",
    "1. **Bản chất Lazy Learner:** Thuật toán KNN không tốn chi phí huấn luyện ($O(1)$), nhưng độ phức tạp trong pha suy luận là $O(N \\cdot D)$ cho mỗi điểm truy vấn. Khi dữ liệu lớn, bắt buộc phải dùng các cấu trúc không gian như KD-Tree, Ball-Tree hoặc FAISS.\n",
    "2. **Quy tắc chọn $k$:** Tránh chọn $k$ chẵn cho bài toán phân lớp nhị phân để loại bỏ hoàn toàn khả năng hòa phiếu. Với bài toán đa lớp, nên kết hợp cơ chế **Distance-weighted Voting** ($w_i = \\frac{1}{d_i}$) thay vì chỉ dùng Majority Voting thông thường.\n",
    "3. **Tầm quan trọng của Chuẩn hóa (Feature Scaling):** Cả Euclidean và Manhattan đều dựa trên khoảng cách tuyệt đối. Nếu hai trục $X$ và $Y$ có đơn vị khác nhau (ví dụ: mét và milimét), khoảng cách sẽ bị biến dạng hoàn toàn nếu không dùng `StandardScaler`."
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
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

out_nb_path = os.path.join(base_dir, 'BT_Buoi5_KNN.ipynb')
with open(out_nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"-> Đã đóng gói thành công Jupyter Notebook: {out_nb_path}")
