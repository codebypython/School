# 🏛️ VIETLAWASSIST — HỆ THỐNG TRỢ LÝ THÔNG MINH ÔN THI PHÁP LUẬT ĐẠI CƯƠNG
> **Đồ Án Chuyên Ngành PBL6 | Khoa Công Nghệ Thông Tin — Trường Đại học Bách Khoa, Đại học Đà Nẵng (DUT)**  
> **Mã Doanh Nghiệp:** `VENTURE-06-PBL6` | **Mã Học Phần:** PBL6 (Semester 7)  
> **Bảng Trạng Thái Tiến Độ Realtime:** [👉 Xem STATUS.md](./STATUS.md)

---

## 📌 MASTER SITEMAP — DANH MỤC HỒ SƠ DỰ ÁN

Toàn bộ tài liệu của đồ án đã được cấu trúc thành các Khối chuyên trách, phục vụ tra cứu chính xác theo từng đối tượng:

### 1. Ban Chiến Lược, Đề Xuất & Học Thuật ([`01_Strategy_and_Proposal/`](./01_Strategy_and_Proposal/))
Dành cho Giảng viên hướng dẫn, Hội đồng phản biện và Ban điều hành đồ án:
- [📄 `01_PROJECT_PROPOSAL.md`](./01_Strategy_and_Proposal/01_PROJECT_PROPOSAL.md) — Bản thuyết minh đề xuất đồ án chi tiết (Full Proposal).
- [📄 `02_DUT_RUBRICS_AND_SCHEDULE.md`](./01_Strategy_and_Proposal/02_DUT_RUBRICS_AND_SCHEDULE.md) — Kế hoạch tiến độ 15 tuần & Rubric 5 tiêu chí (Thang điểm 10) của Khoa CNTT DUT.
- [📄 `03_CURRICULUM_AND_KNOWLEDGE_MAP.md`](./01_Strategy_and_Proposal/03_CURRICULUM_AND_KNOWLEDGE_MAP.md) — Bản đồ tri thức nền tảng & nguồn tài liệu học thuật kinh điển.
- [📄 `04_AI_AGENT_GOVERNANCE_REPORT.md`](./01_Strategy_and_Proposal/04_AI_AGENT_GOVERNANCE_REPORT.md) — Báo cáo nghiên cứu khoa học về quản trị AI Agent trong ngành IT.
- [📄 `DEPARTMENT_CHARTER.md`](./01_Strategy_and_Proposal/DEPARTMENT_CHARTER.md) — Điều lệ quản trị hồ sơ học thuật.

### 2. Ban Nghiệp Vụ Pháp Lý & Đặc Tả Kỹ Thuật ([`02_Domain_and_Specifications/`](./02_Domain_and_Specifications/))
Dành cho Kỹ sư ML, System Architect, Prompt Engineer và AI Agent tác nghiệp:
- [📄 `01_PROJECT_CONCEPT.md`](./02_Domain_and_Specifications/01_PROJECT_CONCEPT.md) — Diễn giải ý tưởng, nỗi đau sinh viên và mô hình giải pháp sư phạm.
- [📄 `02_TECHNICAL_SPECIFICATIONS.md`](./02_Domain_and_Specifications/02_TECHNICAL_SPECIFICATIONS.md) — Đặc tả kỹ thuật: Kiến trúc 4 tầng ML, CSDL SQLite, FAISS, VRAM budget $\le 3.5\text{GB}$.
- [📄 `03_EXAM_BAREM_TEMPLATES.md`](./02_Domain_and_Specifications/03_EXAM_BAREM_TEMPLATES.md) — Khung barem chuẩn hóa 5 dạng đề thi PLĐC, JSON Schemas và ví dụ mẫu.
- [📄 `04_PROJECT_ROADMAP.md`](./02_Domain_and_Specifications/04_PROJECT_ROADMAP.md) — Lộ trình kỹ thuật 15 tuần & các mốc kiểm thử đối sánh.
- [📄 `DEPARTMENT_CHARTER.md`](./02_Domain_and_Specifications/DEPARTMENT_CHARTER.md) — Điều lệ quản trị nghiệp vụ & đặc tả.

### 3. Ban Kỹ Thuật & Sản Phẩm Phần Mềm ([`Project/`](./Project/))
Mã nguồn dự án backend và dữ liệu:
- `Project/app/` — Backend FastAPI, Search Services (BM25, Dense, RAG, LoRA).
- `Project/data/` — CSDL SQLite văn bản pháp luật và FAISS index.
- `Project/scripts/` — Script tiền xử lý dữ liệu và huấn luyện LoRA.
- `Project/tests/` — Bộ kiểm thử tự động PyTest đối sánh 4 tầng.

### 4. Ban Cố Vấn & Vận Hành AI ([`.agents/`](./.agents/))
Dành riêng cho AI Agents tham gia phát triển dự án:
- [📄 `.agents/rules/AGENTS.md`](./.agents/rules/AGENTS.md) — **Single Entry Point**: Agent bắt buộc đọc file này đầu tiên khi vào công ty.
- [📄 `.agents/rules/protocol.md`](./.agents/rules/protocol.md) — Hard Rules: Seed 42, VRAM limit, Parameterized queries, Anti-hallucination.
- `.agents/team/` — Hồ sơ chuyên trách của 6 AI Agents (`PM-01`, `MLR-02`, `DE-03`, `SA-04`, `EVAL-05`, `RW-06`) và Role Handmade.

### 5. Khối An Toàn & Chuẩn Mực Vận Hành AAP ([`antigravity-agent-protocol/`](./antigravity-agent-protocol/))
- Các quy định an toàn SecOps, Terminal blacklisting, Pre-flight impact inspection.

---

## ⚡ HƯỚNG DẪN KHỞI CHẠY NHANH (QUICK START)

```powershell
# 1. Kích hoạt môi trường ảo Python
.\manage_venv.ps1 activate

# 2. Cài đặt các thư viện phụ thuộc
pip install -r Project/requirements.txt

# 3. Chạy bộ kiểm thử hệ thống
pytest Project/tests/ -v

# 4. Khởi chạy FastAPI Backend Service
uvicorn Project.app.main:app --reload --port 8000
```
