# 📖 Phân tích Rubric DUT & Chiến lược Ghi điểm — Agent RW-06

> **Task ID:** W1  
> **Loại output:** 📖 Báo cáo Kiến thức  
> **Ngày tạo:** 2026-09-09  
> **Dùng cho:** Chiến lược tổng thể — đảm bảo mọi task đều phục vụ rubric 10 điểm

---

## 1. Rubric DUT — Trích nguyên văn

Nguồn: [Kế hoạch triển khai PBL6 Đồ án chuyên ngành](file:///d:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/).md)

### Cấu trúc điểm:
- **Điểm quá trình: 40%** — GV hướng dẫn (Phạm Công Thắng) chấm
- **Điểm bảo vệ: 60%** — Hội đồng chấm chéo

### 5 Tiêu chí — Tổng 10 điểm:

| STT | Tiêu chí | Điểm | Mô tả chi tiết (nguyên văn) |
|:---:|----------|:----:|----------------------------|
| **1** | Tính cấp thiết và khả năng ứng dụng của đề tài | **1 điểm** | Đề tài phản ánh nhu cầu thực tế, phù hợp với xu hướng công nghệ. Có tiềm năng triển khai trong thực tiễn hoặc mở rộng nghiên cứu. |
| **2** | Kết quả giải quyết các nhiệm vụ của đồ án | **3 điểm** | Hoàn thành đúng và đủ các yêu cầu đề ra. Sản phẩm hoạt động tốt, có tính khả thi. Thể hiện sự sáng tạo và chủ động. |
| **3** | Mức độ am hiểu về các giải pháp thông qua trả lời câu hỏi | **2 điểm** | Nắm vững nguyên lý hoạt động và phương pháp giải quyết. Trả lời rõ ràng, thuyết phục các câu hỏi chuyên môn. |
| **4** | Chất lượng của quyển báo cáo | **2 điểm** | Nội dung chặt chẽ, trình bày khoa học, có hệ thống. Văn phong rõ ràng, dễ hiểu. Hình ảnh minh họa phù hợp, trích dẫn đúng quy chuẩn. |
| **5** | Kỹ năng thuyết trình slide và demo sản phẩm | **2 điểm** | Slide gọn gàng, súc tích, thể hiện được ý chính. Trình bày tự tin, có sự tương tác tốt. Demo sản phẩm mượt mà, thể hiện đầy đủ chức năng. |

---

## 2. Phân tích từng Tiêu chí — Hội đồng muốn thấy gì?

### 2.1 Tính cấp thiết (1 điểm) — DỄ ĐẠT MAX

**Hội đồng muốn thấy:**
- Đề tài giải quyết vấn đề thực tế, không phải bài tập đơn giản
- Có xu hướng công nghệ (AI, NLP, LLM đang hot)

**Cách ghi điểm tối đa:**
- PLĐC là môn bắt buộc cho ~100% sinh viên ĐH Việt Nam → nhu cầu THỰC TẾ rõ ràng
- AI hỗ trợ pháp luật là xu hướng toàn cầu (ChatLaw, LegalBERT, ...)
- So sánh 4 phương pháp ML → có tính NGHIÊN CỨU, không chỉ ứng dụng

**Agent phụ trách:** PM-01 (viết Chương 1 — Tổng quan)

### 2.2 Kết quả nhiệm vụ (3 điểm) — QUAN TRỌNG NHẤT

**Hội đồng muốn thấy:**
- Hệ thống chạy THẬT, không chỉ slide
- Có ít nhất 1 phương pháp so sánh (yêu cầu PBL6)
- Kiểm thử đầy đủ (Artillery + Selenium)
- Server tự cấu hình (Ubuntu + Nginx)

**Cách ghi điểm tối đa:**
- Demo LIVE: nhập câu hỏi PLĐC → hiển thị 4 kết quả side-by-side
- 4 tầng hoạt động ≫ yêu cầu "ít nhất 1 phương pháp so sánh"
- Artillery load test report + Selenium E2E report → chứng minh kiểm thử
- Docker + Ubuntu + Nginx → đầy đủ quy trình triển khai

**Agent phụ trách:** SA-04 (code + deploy), MLR-02 (ML pipeline), DE-03 (data)

**Breakdown ghi điểm:**
| Sub-criteria | Điểm | Output cần có |
|-------------|:----:|--------------|
| Hoàn thành đúng yêu cầu | 1.0 | 4 tầng ML hoạt động |
| Sản phẩm hoạt động tốt | 1.0 | Demo live, API response <10s |
| Sáng tạo và chủ động | 1.0 | 7 custom metrics, comparison dashboard |

### 2.3 Am hiểu giải pháp (2 điểm) — CẦN CHUẨN BỊ KỸ

**Hội đồng sẽ hỏi (dự đoán):**
1. "BM25 hoạt động thế nào? Giải thích công thức."
2. "Tại sao dùng PhoBERT mà không dùng multilingual-BERT?"
3. "LoRA khác gì full fine-tuning?"
4. "Recall@5 nghĩa là gì? Tại sao chọn K=5?"
5. "Qwen2.5 có bao nhiêu parameters? Sao fit được RTX 3050?"

**Cách ghi điểm tối đa:**
- Mỗi câu hỏi trên → đã có báo cáo kiến thức từ MLR-02 và EVAL-05
- Nắm rõ CÔNG THỨC + VÍ DỤ CỤ THỂ (không chỉ nói chung chung)
- Bảng so sánh 4 tầng với số liệu thực nghiệm → chứng minh hiểu WHY

**Agent phụ trách:** MLR-02 (lý thuyết ML), EVAL-05 (metrics)

### 2.4 Chất lượng báo cáo (2 điểm)

**Hội đồng muốn thấy:**
- Cấu trúc chặt chẽ, logic (Chương 1 → 2 → ... → 7)
- Hình ảnh minh họa RÕ RÀNG (sơ đồ kiến trúc, biểu đồ metrics)
- Trích dẫn đúng (paper, docs, không trích wikipedia)
- Văn phong học thuật (không viết kiểu blog)

**Cách ghi điểm tối đa:**
- Sử dụng template báo cáo chuẩn DUT (W2)
- Mọi sơ đồ đã có trong Grand Design → copy + refine
- Reference list đầy đủ (W4) — ít nhất 15-20 references
- Bảng biểu metrics (bảng so sánh 4 tầng) → visual impact mạnh

**Agent phụ trách:** RW-06 (viết), tất cả agents (cung cấp input)

### 2.5 Thuyết trình & Demo (2 điểm)

**Hội đồng muốn thấy:**
- Slide gọn (15-20 slides), không nhồi chữ
- Demo MƯỢT — không lỗi, không chờ quá lâu
- Tương tác: trả lời câu hỏi tự tin, không đọc slide

**Cách ghi điểm tối đa:**
- Chuẩn bị 5 câu hỏi demo → test trước 10 lần
- Slide: sơ đồ kiến trúc (1 slide), bảng so sánh (1 slide), demo flow (3 slides)
- Dự phòng: nếu server die → có video demo backup

**Agent phụ trách:** RW-06 (slide), SA-04 (demo)

---

## 3. Ma trận Mapping: Rubric ↔ Agents ↔ Outputs Phase 1

| Tiêu chí | Điểm | Agents chính | Output Phase 1 phục vụ |
|----------|:----:|:------------:|------------------------|
| **Cấp thiết (1đ)** | 1/1 | PM-01, RW-06 | Grand Design §I (đã có) |
| **Kết quả (3đ)** | 2.5-3 | SA-04, DE-03, MLR-02 | Code backend (đã có), sample data (D5), BM25 service (đã có) |
| **Am hiểu (2đ)** | 1.8-2 | MLR-02, EVAL-05 | BM25 theory (M1), Tokenizer comparison (M2), IR Metrics (E1) |
| **Báo cáo (2đ)** | 1.8-2 | RW-06 | Report template (W2), References (W4), Weekly log (W3) |
| **Demo (2đ)** | 1.8-2 | SA-04, RW-06 | Setup guide (S2), /api/health + /api/retrieve (đã có) |

---

## 4. Chiến lược Phân bổ Effort — Điểm quá trình (40%) vs Bảo vệ (60%)

### Điểm quá trình (40%) — GV Phạm Công Thắng chấm

- **Nộp báo cáo tiến độ đúng hạn** (2 đợt) → quan trọng nhất
- Thể hiện **quy trình làm việc có hệ thống** (TASKS.md, REVIEW.md, weekly log)
- Commit code đều đặn lên GitHub → GV thấy tiến độ thực

### Điểm bảo vệ (60%) — Hội đồng chấm chéo

- **Demo phải chạy LIVE** → dành 1 tuần cuối chỉ để test demo
- **Trả lời câu hỏi tự tin** → ôn lại tất cả báo cáo kiến thức (M1, M2, E1)
- **Slide ấn tượng** → sơ đồ 4 tầng + bảng metrics là highlight

### Quy tắc phân bổ effort:

```
Phase 1-5 (Tuần 1-10):  70% effort vào KẾT QUẢ (code + data + metrics)
                         20% effort vào AM HIỂU (báo cáo kiến thức)
                         10% effort vào TÀI LIỆU (ghi chép progress)

Phase 6-7 (Tuần 11-15): 50% effort vào BÁO CÁO (quyển báo cáo 7 chương)
                         30% effort vào SLIDE + DEMO (test, polish)
                         20% effort vào ÔN TẬP (câu hỏi bảo vệ)
```

---

## 5. Yêu cầu Bắt buộc từ PBL6 (Checklist)

Trích từ kế hoạch DUT — PHẢI CÓ trong đồ án:

- [x] ✅ Ứng dụng triển khai mô hình học máy trên web (FastAPI + React)
- [ ] API triển khai trên server tự cấu hình (Ubuntu + Nginx)
- [ ] Có quy trình cài đặt OS, cấu hình webserver
- [x] ✅ Ít nhất 1 phương pháp đối sánh (ta có 4 tầng!)
- [ ] Giải thích lý do sử dụng mô hình ML (lý thuyết + thực nghiệm)
- [ ] Quy trình kiểm thử (phần mềm + phần cứng + mạng)
- [ ] Báo cáo kết quả kiểm thử
- [ ] Tất cả quy trình/kết quả có trong báo cáo cuối cùng
