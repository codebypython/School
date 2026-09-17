# 📜 ĐIỀU LỆ PHÒNG TƯ LIỆU & BÀI GIẢNG GỐC (LECTURES & RAW MATERIALS DEPT)
## Phòng 02 — Công Ty Trí Tuệ Nhân Tạo & Học Máy (CORP-02-ML)

> **Mã Phòng Ban:** `ML-DEPT-02`  
> **Trưởng phòng phụ trách:** Agent `SMS-02` (Syllabus & Material Sentinel) & Thư Ký Khoa Học Dữ Liệu  
> **Cấp bậc quản trị:** Cấp 2 — Thu thập, thẩm định chất lượng học liệu theo chuẩn ER-QVR, phân rã slide và chuẩn hóa tri thức gốc

---

## 1. CHỨC NĂNG & NHIỆM VỤ (FUNCTION & MANDATE)
Phòng `ML-DEPT-02` chịu trách nhiệm thu nhận, kiểm định, số hóa và lập chỉ mục toàn bộ tài liệu giảng dạy, slide bài giảng từ giảng viên ĐHBK Đà Nẵng, cùng các giáo trình kinh điển quốc tế về Machine Learning:
1. **Tiếp nhận & Chuẩn hóa Slide Bài giảng**: Phân rã các slide dạng `.pdf`, `.pptx` thành các bản tóm tắt tri thức Markdown theo cấu trúc mô-đun tuần tự 15 tuần.
2. **Đối chiếu giáo trình kinh điển (ER-QVR Standard)**: Thẩm định và đối chiếu nội dung bài giảng với các nguồn tài liệu học thuật uy tín hàng đầu: *Pattern Recognition and Machine Learning* (Christopher Bishop), *The Elements of Statistical Learning* (Hastie, Tibshirani, Friedman), và *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (Aurélien Géron).
3. **Phát hiện & Bù đắp Khoảng trống Tri thức (Knowledge Gap Bridging)**: Tự động phát hiện các công thức toán hoặc bước suy dẫn bị giảng viên giản lược trên lớp để xây dựng phụ lục chứng minh toán học chi tiết.

---

## 2. BỘ QUY TẮC BẤT BIẾN (CURATION INVARIANTS & HARD CONSTRAINTS)
Mọi tài liệu lưu trữ và tóm tắt trong `ML-DEPT-02` bắt buộc phải tuân thủ 5 nguyên tắc:
1. **Nguyên tắc Thẩm định ER-QVR $\ge 80/100$**: Mọi nguồn tài liệu tham khảo ngoại vi (bài blog, video Youtube, tài liệu mạng) phải được chấm điểm theo thang rubric 100 điểm ER-QVR. Nguồn dưới 80 điểm tuyệt đối không được đưa vào kho tài liệu tham khảo chính thống.
2. **Nguyên tắc Bảo tồn Nguyên tác (Source Integrity)**: Slide gốc của giảng viên DUT phải được lưu trữ nguyên bản, không chỉnh sửa trực tiếp vào file nguồn. Mọi bổ sung, đính chính chỉ được thực hiện thông qua file tóm tắt Markdown kèm liên kết tham chiếu.
3. **Nguyên tắc Chuẩn hóa Ký hiệu Toán học (Mathematical Notation Consistency)**: Ký hiệu toán học phải thống nhất trên toàn bộ hệ thống: Ma trận biểu diễn bằng chữ in hoa đậm $\mathbf{X} \in \mathbb{R}^{N \times D}$, vector cột in thường đậm $\mathbf{w} \in \mathbb{R}^{D}$, scalar in nghiêng $y \in \mathbb{R}$.
4. **Nguyên tắc Loại trừ File Quá khổ (File Size Control)**: File slide bài giảng hoặc sách PDF có kích thước vượt quá 50MB bắt buộc phải nén hoặc phân rã thành từng chương trước khi commit vào git.
5. **Nguyên tắc Ghi nhận Bản quyền & Nguồn gốc (Attribution Invariant)**: Mọi định lý, hình ảnh minh họa trích dẫn từ sách ngoài hoặc nghiên cứu khoa học phải ghi rõ tác giả, năm xuất bản và trang tham chiếu.

---

## 3. BỘ LỆNH & QUY TRÌNH XỬ LÝ TÀI LIỆU (TOOLCHAIN & INGESTION PIPELINE)
```bash
# 1. Trích xuất text và công thức từ slide PDF bài giảng ML
pdftotext -layout week04_linear_regression.pdf week04_extracted.txt

# 2. Quét kích thước các file trong phòng ban để đảm bảo không vi phạm giới hạn git
find . -type f -size +40M -exec ls -lh {} \;

# 3. Kiểm tra tính hợp lệ của các liên kết Markdown trong thư mục bài giảng
markdown-link-check week*.md

# 4. Tìm kiếm nhanh một công thức hoặc định lý toán học trong kho học liệu
grep -rn "Lagrangian" ./summaries/
```

---

## 4. CẤU TRÚC THƯ MỤC & TÀI SẢN PHÒNG BAN (DEPARTMENT ASSETS)
```
02_Lectures_and_Raw_Materials/
├── DEPARTMENT_CHARTER.md              # Điều lệ phòng ban 7 tầng chuẩn hóa
├── slides/                            # Lưu trữ slide bài giảng gốc của giảng viên DUT
│   ├── Week01_Introduction_Math.pdf
│   ├── Week03_Linear_Regression.pdf
│   └── ...
├── textbook_references/               # Danh mục trích dẫn giáo trình kinh điển (Bishop, Hastie)
│   └── TEXTBOOK_MAPPING.md
└── lecture_summaries/                 # Bản tóm tắt học thuật Markdown chuẩn ER-QVR
    ├── Summary_Week03_Regression.md
    ├── Summary_Week06_Logistic_Loss.md
    └── Summary_Week08_SVM_Dual.md
```

---

## 5. MẪU TƯ LIỆU TÓM TẮT CHUẨN ER-QVR (GOLD MASTER BLUEPRINT)

### Bản Tóm Tắt Khái Niệm Hàm Mất Mát Cross-Entropy Cho Phân Lớp Logistic (`Summary_Week06_Logistic_Loss.md`)
```markdown
# 📘 TÓM TẮT HỌC THUẬT: HÀM MẤT MÁT BINARY CROSS-ENTROPY (LOG-LOSS)
> **Nguồn trích dẫn chính**: Bishop PRML (Chương 4), Hastie ESL (Chương 4).  
> **Điểm thẩm định ER-QVR**: 98/100 (Uy tín học thuật tuyệt đối).

## 1. Bản chất Xác suất (Likelihood Formulation)
Giả thiết nhãn $y \in \{0, 1\}$ tuân theo phân phối Bernoulli với xác suất:
$$P(y|\mathbf{x}; \mathbf{w}) = \hat{y}^y (1 - \hat{y})^{1 - y}$$
trong đó $\hat{y} = \sigma(\mathbf{w}^T \mathbf{x}) = \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}}}$.

Hàm Likelihood trên toàn bộ $N$ quan sát độc lập cùng phân phối (i.i.d):
$$L(\mathbf{w}) = \prod_{i=1}^{N} \hat{y}_i^{y_i} (1 - \hat{y}_i)^{1 - y_i}$$

## 2. Cực đại hóa Hợp lý $\rightarrow$ Cực tiểu hóa Mất mát (NLL)
Lấy logarithm tự nhiên và đổi dấu để chuyển từ bài toán Maximize Likelihood sang Minimize Negative Log-Likelihood:
$$J(\mathbf{w}) = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \ln(\hat{y}_i) + (1 - y_i) \ln(1 - \hat{y}_i) \right]$$

## 3. Đạo hàm Gradient Vector Hóa
Nhờ tính chất đặc biệt của hàm Sigmoid $\sigma'(z) = \sigma(z)(1 - \sigma(z))$, đạo hàm riêng của $J(\mathbf{w})$ thu gọn lại thành dạng cực kỳ thanh lịch:
$$\nabla_{\mathbf{w}} J(\mathbf{w}) = \frac{1}{N} \mathbf{X}^T (\hat{\mathbf{y}} - \mathbf{y})$$
*Nhận xét sư phạm*: Hình thức đạo hàm này giống hệt đạo hàm của Linear Regression với MSE, nhưng $\hat{\mathbf{y}}$ ở đây là xác suất phi tuyến qua hàm sigmoid!
```

---

## 6. TIÊU CHÍ NGHIỆM THU (DEFINITION OF DONE - DOD)
Tài liệu của phòng `ML-DEPT-02` chỉ được nghiệm thu khi đạt các tiêu chuẩn:
- [x] **100% Slide có bản tóm tắt tương ứng**: Mỗi tệp slide nạp vào đều phải có một bản tóm tắt markdown chuẩn hóa tương ứng trong `lecture_summaries/`.
- [x] **Kiểm định nguồn gốc nghiêm ngặt**: Không đưa tài liệu không rõ xuất xứ, không kiểm chứng vào kho lưu trữ học thuật.
- [x] **Trực quan hóa công thức toán**: Mọi công thức đều được render chuẩn xác bằng KaTeX/LaTeX, không bị lỗi cú pháp hiển thị.
- [x] **Auditor thông qua**: Điểm kiểm định Schema đạt 100% không cảnh báo.

---

## 7. QUY TRÌNH XỬ LÝ SỰ CỐ TÀI LIỆU (TROUBLESHOOTING & RUNBOOK)

### Sự cố 1: Slide giảng viên chứa công thức toán mâu thuẫn hoặc thiếu bước suy dẫn
- **Hiện tượng**: Giảng viên viết tắt từ hàm mục tiêu nhảy thẳng sang công thức cập nhật mà không chứng minh đạo hàm, khiến sinh viên hoang mang.
- **Quy trình xử lý**:
  1. Thư ký học thuật gắn nhãn `[NEEDS_MATHEMATICAL_DERIVATION]` vào mục tương ứng.
  2. Tra cứu chứng minh chuẩn trong sách của Bishop PRML hoặc Christopher Bishop.
  3. Viết phụ lục chứng minh chi tiết từng bước (Step-by-step Derivation) bổ sung vào tệp tóm tắt tương ứng.

### Sự cố 2: File slide bài giảng quá nặng (>100MB) gây nghẽn Git Push
- **Hiện tượng**: Git từ chối nhận commit do vi phạm hạn mức 100MB của GitHub.
- **Quy trình xử lý**:
  1. Tách hình ảnh độ phân giải cao hoặc nén PDF bằng công cụ Ghostscript:
     ```bash
     gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=compressed.pdf original.pdf
     ```
  2. Nếu vẫn lớn hơn 50MB, đưa tệp PDF vào `.gitignore` và chỉ lưu bản tóm tắt Markdown chi tiết trong kho mã nguồn.
