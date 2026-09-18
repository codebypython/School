# 📜 ĐIỀU LỆ PHÒNG TƯ LIỆU & BÀI GIẢNG GỐC (LECTURES & RAW MATERIALS DEPT)
## Phòng 02 — Công Ty Công Nghệ Thị Giác Máy Tính (CORP-01-CV)

> **Mã Phòng Ban:** `CV-DEPT-02`  
> **Trưởng phòng phụ trách:** Agent `EKC-03` (Knowledge Curator & Quality Sentinel)  
> **Tiêu chuẩn học liệu:** ER-QVR $\ge 90/100$ | Stanford CS231n / Szeliski Computer Vision / DUT Courseware

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Tư Liệu là **trung tâm quản trị hồ sơ học thuật, báo cáo đồ án và thư viện bài giảng gốc**:
1. **Quản Trị Báo Cáo Kỹ Thuật Đồ Án (Project Reports)**: Biên tập, duy trì và cập nhật liên tục bản báo cáo thiết kế kỹ thuật hoàn chỉnh (`project_report.md` và `BÁO-CÁO.docx/pdf`) chuẩn format khoa học của Đại học Bách Khoa Đà Nẵng (DUT).
2. **Quản Trị Kịch Bản & Slide Thuyết Trình (Presentation Slides)**: Quản lý chi tiết nội dung slide từng trang kèm script thuyết trình cho sinh viên (`slide_content_20_pages.md`, `Slide.pptx`, `Slide.pdf`).
3. **Đồng Bộ Dữ Liệu Thực Nghiệm Từ Google Colab Vào Hồ Sơ**: Trích xuất các bảng chỉ số định lượng (MAE, RMSE, $R^2$), biểu đồ hội tụ loss và bản đồ Grad-CAM từ kết quả huấn luyện đám mây để cập nhật thẳng vào các chương báo cáo và slide.
4. **Lưu Trữ Bất Biến Giáo Trình & Bài Báo Khoa Học (Paper Vault)**: Bảo tồn slide bài giảng chính quy của DUT, sách kinh điển (Szeliski, Goodfellow) và các bài báo khoa học bước ngoặt (RSNA Challenge, ResNet, EfficientNet, Swin Transformer).

---

## ⚖️ 2. BỘ QUY TẮC BẢO TỒN TƯ LIỆU BẤT BIẾN (CURATION INVARIANTS)

1. **Chuẩn Mực Công Thức Toán Học (LaTeX Invariant)**:
   - Toàn bộ phương trình tích chập, hàm mất mát (Cross-Entropy, Focal Loss, IoU Loss) bắt buộc viết bằng LaTeX chuẩn:
     $$\mathcal{L}_{CE} = -\sum_{c=1}^{M} y_{o,c} \log(p_{o,c})$$
2. **Quy Tắc Đối Chiếu Nguồn Gốc (Provenance Citation)**:
   - Mọi định lý hoặc thuật toán phải trích dẫn rõ số chương, số trang từ sách Tier A+ trong Knowledge Vault.
3. **Quy Tắc Không "Rác Dữ Liệu"**:
   - Nghiêm cấm lưu trữ các slide nháp không hoàn chỉnh hoặc các tệp media quá khổ trái quy chuẩn Git.

---

## 🛠️ 3. TOOLCHAIN & QUY TRÌNH SỐ HÓA BÀI GIẢNG

1. **Số Hóa Công Thức**: MathJax / KaTeX Markdown Renderer.
2. **Trực Quan Hóa Mạng Nơ-ron**: Netron, Net2Vis, Mermaid.js.
3. **Kiểm Soát Tính Toàn Vẹn**: Script `holding_system_auditor.py`.

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
02_Lectures_and_Raw_Materials/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 slide_content_20_pages.md             # Bản số hóa chi tiết 20 trang slide bài giảng
├── 📄 project_report.md                     # Mẫu báo cáo đồ án thị giác máy tính
├── 📁 paper_summaries/                      # Tóm tắt các bài báo kinh điển
│   ├── resnet_deep_residual_learning.md    # Phân tích cơ chế Skip Connections
│   └── unet_biomedical_segmentation.md     # Phân tích kiến trúc U-Net Encoder-Decoder
└── 📁 math_derivations/                     # Chứng minh toán học thị giác
    └── backprop_conv2d_derivation.md       # Chứng minh đạo hàm ngược trên Tensor Conv2D
```

---

## 💻 5. MẪU TƯ LIỆU CHỨNG MINH HỌC THUẬT (GOLD MASTER MATHEMATICAL DERIVATION)

```markdown
# 📐 BẢN CHỨNG MINH HỌC THUẬT: ĐẠO HÀM NGƯỢC CỦA LỚP TÍCH CHẬP (CONV2D BACKPROPAGATION)
> **Nguồn trích:** Stanford CS231n & Deep Learning (Goodfellow et al., Ch. 9)  
> **Người thẩm định:** Agent `EKC-03` | **Điểm ER-QVR:** 96/100

### 1. Phép tính lan truyền xuôi (Forward Pass)
Cho đầu vào $X \in \mathbb{R}^{H \times W}$, Kernel $K \in \mathbb{R}^{k \times k}$, đầu ra $Y = X * K$:
$$Y_{i,j} = \sum_{m} \sum_{n} X_{i+m, j+n} K_{m,n}$$

### 2. Đạo hàm theo trọng số Kernel ($\frac{\partial \mathcal{L}}{\partial K}$)
$$\frac{\partial \mathcal{L}}{\partial K_{m,n}} = \sum_{i} \sum_{j} \frac{\partial \mathcal{L}}{\partial Y_{i,j}} X_{i+m, j+n}$$
$\implies$ Đạo hàm của Loss theo Kernel chính là phép tích chập giữa đầu vào $X$ và gradient lỗi đầu ra $\frac{\partial \mathcal{L}}{\partial Y}$!
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU TƯ LIỆU (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: Toàn bộ công thức toán học hiển thị chuẩn xác, không lỗi cú pháp LaTeX.
- [ ] **DoD-2**: Trích dẫn tài liệu chính xác từ Szeliski hoặc Stanford CS231n.
- [ ] **DoD-3**: Có sơ đồ trực quan minh họa cơ chế hoạt động của thuật toán thị giác.
- [ ] **DoD-4**: Đạt điểm kiểm định chất lượng ER-QVR tối thiểu 90/100.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK KHẮC PHỤC SAI LỆCH KIẾN THỨC (CURATION TROUBLESHOOTING RUNBOOK)

Khi phát hiện slide hoặc bài viết chứa công thức tích chập hoặc shape tensor không chính xác:
1. **Cô lập tư liệu**: Gắn nhãn `⚠️ MATHEMATICAL ERROR: Re-derivation required`.
2. **Đối chiếu bản in gốc**: Tra cứu trực tiếp trong Szeliski hoặc Goodfellow Deep Learning.
3. **Viết lại chứng minh**: Trình bày từng bước biến đổi đại số tuyến tính chi tiết.
4. **Xác nhận**: Đảm bảo toàn bộ sinh viên tiếp cận công thức toán học chặt chẽ.
