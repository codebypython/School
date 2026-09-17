import numpy as np
import pandas as pd
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

np.random.seed(42)

# Tạo dữ liệu 6 loài hoa tương ứng 6 cụm tự nhiên rõ rệt (K = 6 nằm trong khoảng 5 - 7):
# Các đặc trưng số đo kích thước:
# - sepal_length: Chiều dài đài hoa (cm)
# - sepal_width:  Chiều rộng đài hoa (cm)
# - petal_length: Chiều dài cánh hoa (cm)
# - petal_width:  Chiều rộng cánh hoa (cm)
# - stem_length:  Chiều dài cuống/thân hoa (cm)
species_params = {
    'Iris-Setosa':      {'sl': (5.0, 0.35), 'sw': (3.4, 0.38), 'pl': (1.5, 0.17), 'pw': (0.25, 0.10), 'stl': (12.0, 1.2)},
    'Iris-Versicolor':  {'sl': (5.9, 0.52), 'sw': (2.8, 0.31), 'pl': (4.3, 0.47), 'pw': (1.30, 0.20), 'stl': (18.5, 1.5)},
    'Iris-Virginica':   {'sl': (6.6, 0.64), 'sw': (3.0, 0.32), 'pl': (5.6, 0.55), 'pw': (2.00, 0.27), 'stl': (22.0, 2.0)},
    'Mini-Rose':        {'sl': (3.8, 0.40), 'sw': (2.2, 0.25), 'pl': (2.8, 0.35), 'pw': (1.80, 0.22), 'stl': (28.0, 2.5)},
    'Sunflower-Dwarf':  {'sl': (8.2, 0.70), 'sw': (4.1, 0.45), 'pl': (7.8, 0.65), 'pw': (3.20, 0.35), 'stl': (45.0, 3.8)},
    'Tulip-Standard':   {'sl': (7.1, 0.55), 'sw': (2.5, 0.30), 'pl': (6.4, 0.50), 'pw': (2.60, 0.28), 'stl': (32.0, 2.8)},
}

data = []
for sp, p in species_params.items():
    n = 50  # 50 bông hoa mỗi loài -> Tổng cộng 300 mẫu
    sl = np.round(np.random.normal(p['sl'][0], p['sl'][1], n), 2)
    sw = np.round(np.random.normal(p['sw'][0], p['sw'][1], n), 2)
    pl = np.round(np.random.normal(p['pl'][0], p['pl'][1], n), 2)
    pw = np.round(np.random.normal(p['pw'][0], p['pw'][1], n), 2)
    stl = np.round(np.random.normal(p['stl'][0], p['stl'][1], n), 2)
    for i in range(n):
        data.append({
            'flower_id': len(data) + 1,
            'species': sp,
            'sepal_length': float(max(0.5, sl[i])),
            'sepal_width': float(max(0.5, sw[i])),
            'petal_length': float(max(0.5, pl[i])),
            'petal_width': float(max(0.1, pw[i])),
            'stem_length': float(max(1.0, stl[i]))
        })

df = pd.DataFrame(data)
# Xáo trộn ngẫu nhiên dữ liệu để mô phỏng dữ liệu thu thập thực tế
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df['flower_id'] = range(1, len(df) + 1)

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'flower_dataset.csv')
xlsx_path = os.path.join(base_dir, 'flower_dataset.xlsx')

df.to_csv(csv_path, index=False, encoding='utf-8-sig')
df.to_excel(xlsx_path, index=False)

print(f"Đã tạo thành công file CSV: {csv_path}")
print(f"Đã tạo thành công file Excel: {xlsx_path}")
print(f"Kích thước tập dữ liệu: {df.shape[0]} dòng x {df.shape[1]} cột")
print("\n5 dòng đầu tiên của tập dữ liệu:")
print(df.head())
