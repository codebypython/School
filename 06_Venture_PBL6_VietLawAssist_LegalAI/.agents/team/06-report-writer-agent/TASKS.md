# 📋 TASKS — Agent 06: Report Writer Agent

> **Cập nhật lần cuối:** 2026-09-09  
> **Giai đoạn hiện tại:** Phase 1 — Documentation Foundation  
> **Phân công bởi:** PM-01 (Project Manager)

---

## Phase 0: Nghiên cứu & Khám phá (Tuần 0) ✅ HOÀN THÀNH

- [x] Đọc Proposal — nắm scope, structure, rubric alignment
- [x] Đọc Kế hoạch triển khai PBL6 — nắm yêu cầu GV và rubric chấm
- [x] Thiết kế cấu trúc báo cáo đồ án (7 chương)
- [x] Map từng chương với agent cung cấp input
- [x] Viết phần báo cáo structure cho Grand Design Overview

---

## Phase 1: Documentation Foundation (Tuần 1-2)

> **Triết lý:** Phân tích rubric + chuẩn bị template + ghi chép tiến độ — đặt nền móng cho báo cáo cuối kỳ.  
> **Thư mục output:** `.agents/outputs/phase1/`

### Sóng 1 — Phân tích & Chiến lược (không phụ thuộc agent khác)

- [x] **W1** 📖 Phân tích Rubric DUT & Chiến lược ghi điểm ✅
    - Output: `.agents/outputs/phase1/rw-06_rubric_analysis.md`
    - Nội dung bắt buộc:
        1. Trích nguyên văn 5 tiêu chí rubric DUT (từ Note kế hoạch triển khai)
        2. Mỗi tiêu chí: phân tích cách ghi điểm tối đa, "hội đồng muốn thấy gì?"
        3. **Tính cấp thiết (1đ):** PLĐC bắt buộc cho ~100% SV → nhu cầu rõ ràng
        4. **Kết quả nhiệm vụ (3đ):** Cần demo live, 4 tầng hoạt động, kiểm thử đầy đủ
        5. **Am hiểu giải pháp (2đ):** Trả lời được "tại sao BM25?", "tại sao LoRA?"
        6. **Chất lượng báo cáo (2đ):** Cấu trúc chặt chẽ, trích dẫn, hình ảnh minh họa
        7. **Thuyết trình & Demo (2đ):** Slide gọn, demo mượt, tương tác tốt
        8. Ma trận mapping: Tiêu chí rubric ↔ Agent phụ trách ↔ Output cần có
        9. Điểm quá trình (40%) vs Điểm bảo vệ (60%): chiến lược phân bổ effort
    - DoD: File .md, trích rubric nguyên văn, phân tích 5 tiêu chí, ma trận mapping

### Sóng 2 — Template & Tài liệu

- [x] **W2** 🛠 Template báo cáo đồ án (outline chi tiết) ✅
    - Output: `.agents/outputs/phase1/rw-06_report_template.md`
    - Nội dung:
        1. Outline 7 chương, mỗi chương ghi:
            - Tên chương + tên các mục con
            - Nguồn input: agent nào cung cấp nội dung
            - Ước tính số trang
            - Ghi chú: nội dung chính cần viết, hình ảnh/bảng biểu cần có
        2. Format báo cáo: font, cỡ chữ, margin theo quy chuẩn DUT
        3. Cách trích dẫn: số thứ tự [1], [2]... hay APA?
        4. Danh mục bảng biểu, danh mục hình ảnh cần có
    - DoD: File .md, 7 chương với outline chi tiết, format specifications

- [x] **W4** 🗂 Tổng hợp References & Sources ✅
    - Output: `.agents/outputs/phase1/rw-06_references.md`
    - Nội dung:
        1. **NLP & Vietnamese Processing:** Papers PhoBERT (VinAI 2020), Underthesea docs
        2. **Information Retrieval:** Robertson & Zaragoza (2009), Manning "Intro to IR" (2008)
        3. **RAG & LLM:** Lewis et al. (2020) "Retrieval-Augmented Generation", Qwen2.5 Technical Report
        4. **Fine-tuning:** Hu et al. (2021) "LoRA", Dettmers et al. (2023) "QLoRA"
        5. **Legal AI:** Các công trình NLP pháp luật tiếng Việt (nếu có)
        6. **Tools & Libraries:** FastAPI docs, rank-bm25 GitHub, rouge-score, bert-score
        7. Mỗi reference: tác giả, năm, tên, link URL (nếu có)
    - DoD: File .md, chia 6+ nhóm, mỗi nhóm 3-5 references, format APA hoặc IEEE nhất quán

### Sóng 3 — Ghi chép tiến độ

- [x] **W3** 📖 Weekly Progress Log — Tuần 1-2 ✅
    - Output: `.agents/outputs/phase1/rw-06_weekly_log_w1.md`
    - Nội dung:
        1. Tổng quan tuần: mục tiêu → kết quả đạt được
        2. Danh sách output đã tạo: file path + mô tả ngắn
        3. Quyết định kỹ thuật đã đưa ra: tokenizer nào, schema gì, kiến trúc gì
        4. Vướng mắc gặp phải (nếu có)
        5. Kế hoạch tuần tới (Phase 2 preview)
    - DoD: File .md, ghi nhận đầy đủ progress, có thể gửi cho GV Phạm Công Thắng
    - Phụ thuộc: Tổng hợp từ output tất cả agents Phase 1

---

## Phase 4: Báo cáo Tiến độ 1 (Tuần 4)

- [ ] Tổng hợp progress từ tất cả agents (Phase 1-2)
- [ ] Viết báo cáo tiến độ 1: Corpus ready + Tầng 1-2 hoạt động
- [ ] Format theo mẫu GV yêu cầu
- [ ] Nộp cho GV Phạm Công Thắng

## Phase 5: Báo cáo Tiến độ 2 (Tuần 10)

- [ ] Tổng hợp progress từ tất cả agents (Phase 3-5)
- [ ] Viết báo cáo tiến độ 2: Tầng 3-4 hoạt động + Evaluation results
- [ ] Format theo mẫu GV yêu cầu

## Phase 6: Báo cáo Đồ án (Tuần 11-13)

- [ ] Viết Chương 1: Tổng quan (từ Proposal + PM-01 input)
- [ ] Viết Chương 2: Cơ sở lý thuyết (từ MLR-02 research output)
- [ ] Viết Chương 3: Thiết kế hệ thống (từ SA-04 architecture output)
- [ ] Viết Chương 4: Thu thập & xử lý dữ liệu (từ DE-03 data output)
- [ ] Viết Chương 5: Thực nghiệm & đánh giá (từ EVAL-05 metrics output)
- [ ] Viết Chương 6: Kiểm thử (từ SA-04 testing output)
- [ ] Viết Chương 7: Kết luận & hướng phát triển
- [ ] Tạo bảng biểu, đồ thị minh họa
- [ ] Review toàn bộ báo cáo (consistency, trích dẫn, format)

## Phase 7: Slide & Demo Prep (Tuần 14)

- [ ] Thiết kế slide bảo vệ (15-20 slides)
- [ ] Slide 1-3: Giới thiệu, vấn đề, giải pháp
- [ ] Slide 4-7: Kiến trúc 4 tầng (diagrams)
- [ ] Slide 8-10: Demo flow (screenshots)
- [ ] Slide 11-14: Kết quả thực nghiệm (bảng, biểu đồ)
- [ ] Slide 15: Kết luận & hướng phát triển
- [ ] Chuẩn bị demo script (câu hỏi PLĐC mẫu)
