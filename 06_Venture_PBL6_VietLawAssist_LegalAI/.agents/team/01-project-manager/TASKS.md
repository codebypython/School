# 📋 TASKS — Agent 01: Project Manager

> **Cập nhật lần cuối:** 2026-09-09  
> **Giai đoạn hiện tại:** Phase 1 — Thu thập Dữ liệu & Tầng 1

---

## Phase 0: Nghiên cứu & Khám phá (Tuần 0) ✅ HOÀN THÀNH

- [x] Đọc và phân tích toàn bộ Note dự án (Proposal, Kế hoạch, AI Research)
- [x] Xác định 6 vai trò agent cần thiết cho dự án
- [x] Thiết kế cấu trúc thư mục `.agents/` chuẩn hóa
- [x] Phân rã tasks cho từng agent trong giai đoạn nghiên cứu
- [x] Tạo Grand Design Overview tổng hợp từ output các agents
- [x] Review & đánh giá kết quả giai đoạn nghiên cứu

---

## Phase 1: Thu thập Dữ liệu & Tầng 1 (Tuần 1-2)

> **Triết lý output:** 📖 Báo cáo | 🗂 Dữ liệu | 🛠 Hướng dẫn | 💻 Code
> **Thư mục output:** `.agents/outputs/phase1/`

### Sóng 1: Lập kế hoạch & Phân công (PM-01 làm trước)

- [x] **P1.1** 🛠 Cập nhật TASKS.md cho PM-01 (bản thân) ✅
    - Output: `.agents/team/01-project-manager/TASKS.md`
    - DoD: Phase 0 đóng hoàn toàn, Phase 1 có đầy đủ task + DoD + loại output + file path
- [x] **P1.2** 🛠 Cập nhật TASKS.md cho MLR-02 ✅
    - Output: `.agents/team/02-ml-research-agent/TASKS.md`
    - DoD: Phase 1 có 5 task (M1-M5) với DoD chi tiết
- [x] **P1.3** 🛠 Cập nhật TASKS.md cho DE-03 ✅
    - Output: `.agents/team/03-data-engineer-agent/TASKS.md`
    - DoD: Phase 1 có 6 task (D1-D6) với DoD chi tiết
- [x] **P1.4** 🛠 Cập nhật TASKS.md cho SA-04 ✅
    - Output: `.agents/team/04-system-architect-agent/TASKS.md`
    - DoD: Phase 1 có 4 task (S1-S4) với DoD chi tiết
- [x] **P1.5** 🛠 Cập nhật TASKS.md cho EVAL-05 ✅
    - Output: `.agents/team/05-evaluation-agent/TASKS.md`
    - DoD: Phase 1 có 4 task (E1-E4) với DoD chi tiết
- [x] **P1.6** 🛠 Cập nhật TASKS.md cho RW-06 ✅
    - Output: `.agents/team/06-report-writer-agent/TASKS.md`
    - DoD: Phase 1 có 4 task (W1-W4) với DoD chi tiết

### Sóng 2-3: Giám sát & Kiểm soát chất lượng

- [x] **P2** 📖 Review & Đánh giá toàn bộ output Phase 1 ✅
    - Output: 6 files `.agents/team/*/REVIEW.md` cập nhật
    - DoD: Mỗi output được đánh giá đạt/chưa đạt DoD, nhận xét chất lượng, đề xuất bổ sung

### Sóng 4: Bàn giao

- [x] **P3** 📖 Session Handover Report Phase 1 ✅
    - Output: `.agents/outputs/phase1/pm-01_phase1_handover.md`
    - DoD: Tổng kết status tất cả tasks, danh sách outputs, milestones đạt/chưa, hướng Phase 2

---

## Phase 2: Dense Retrieval & Tầng 2 (Tuần 3-4)

- [ ] Phân công Agent-02 PhoBERT + FAISS research
- [ ] Theo dõi Recall@5 comparison Tầng 1 vs Tầng 2
- [ ] Chuẩn bị Báo cáo tiến độ 1 (nộp cho GV)
- [ ] Xác nhận milestone: "Tầng 2 hoạt động"

## Phase 3: RAG Pipeline & Tầng 3 (Tuần 5-6)

- [ ] Phân công Agent-02 setup Qwen2.5-1.5B + quantization
- [ ] Phân công Agent-05 implement ROUGE/BERTScore
- [ ] Xác nhận milestone: "Tầng 3 hoạt động"

## Phase 4: Fine-tuning & Tầng 4 (Tuần 7-8)

- [ ] Phân công Agent-03 tạo dataset 500 cặp Q&A
- [ ] Phân công Agent-02 LoRA fine-tuning trên Colab
- [ ] Xác nhận milestone: "Tầng 4 hoạt động"

## Phase 5: Evaluation & Testing (Tuần 9-10)

- [ ] Phân công Agent-05 full evaluation 4 tầng
- [ ] Phân công Agent-04 load testing (Artillery) + E2E testing (Selenium)
- [ ] Chuẩn bị Báo cáo tiến độ 2 (nộp cho GV)

## Phase 6: Báo cáo & Bảo vệ (Tuần 11-15)

- [ ] Phân công Agent-06 viết báo cáo đồ án
- [ ] Phân công Agent-06 chuẩn bị slide bảo vệ
- [ ] Demo rehearsal
- [ ] Nộp & Bảo vệ
