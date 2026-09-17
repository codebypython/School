# 🤖 ĐIỀU LỆ HOẠT ĐỘNG: CÔNG TY KHỞI NGHIỆP AI PHÁP LÝ (VIETLAWASSIST VENTURE)
## Company 06: VietLawAssist — Vietnamese Legal QA & RAG Ecosystem

> **Mã Doanh Nghiệp:** `VENTURE-06-PBL6`  
> **Tên giao dịch:** VietLawAssist Legal Tech Venture  
> **Lĩnh vực chuyên môn:** Xử lý ngôn ngữ tự nhiên tiếng Việt, Hệ thống hỏi đáp pháp luật RAG (Retrieval-Augmented Generation), Tìm kiếm thưa (BM25Okapi), Tìm kiếm dày (PhoBERT + FAISS), Lượng tử hóa 4-bit và LoRA/QLoRA Fine-tuning trên LLM (Qwen2.5-1.5B).  
> **Cố vấn chuyên môn:** Hội đồng 6 AI Agents (`PM-01`, `MLR-02`, `DE-03`, `SA-04`, `EVAL-05`, `RW-06`)  
> **Tổng Giám Đốc Điều Hành (CEO):** Sinh viên (Role Handmade)

---

## 1. SỨ MỆNH & TẦM NHÌN (MISSION & VISION)

- **Sứ mệnh**: Xây dựng giải pháp Trợ lý Thông minh Hỗ trợ Ôn thi và Giải đề Chuẩn Barem môn Pháp luật Đại cương cho sinh viên đại học Việt Nam. Chứng minh năng lực nghiên cứu khoa học và kỹ năng kỹ thuật thông qua việc xây dựng **Bậc thang So sánh 4 Tầng (Comparison Ladder)** từ giải pháp cơ bản (BM25) đến công nghệ AI tạo sinh tiên tiến nhất (RAG + QLoRA).
- **Tiêu chuẩn chất lượng**: Đạt điểm tối đa (10/10) theo Rubric 5 tiêu chí của Hội đồng chấm thi Khoa CNTT — ĐHBK Đà Nẵng (DUT). Tuân thủ bộ quy chuẩn an toàn **Antigravity Agent Protocol (AAP)**.

---

## 2. CƠ CẤU TỔ CHỨC CÁC PHÒNG BAN CHỨC NĂNG

Hồ sơ của Công ty 06 được phân định ranh giới chặt chẽ theo 4 phòng ban chức năng độc lập:

| Phòng Ban | Thư Mục Quản Lý | Điều Lệ / Đặc Tả | Chức Năng Cốt Lõi |
|:---|:---|:---:|:---|
| **Ban Chiến Lược & Học Thuật** | [`01_Strategy_and_Proposal/`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/01_Strategy_and_Proposal/) | [Department Charter](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/01_Strategy_and_Proposal/DEPARTMENT_CHARTER.md) | Quản lý Đề xuất đồ án chính thức, Kế hoạch 15 tuần, Rubric 10đ DUT và Báo cáo quản trị AI Agent. |
| **Ban Nghiệp Vụ & Đặc Tả Kỹ Thuật** | [`02_Domain_and_Specifications/`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/02_Domain_and_Specifications/) | [Department Charter](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/02_Domain_and_Specifications/DEPARTMENT_CHARTER.md) | Quản lý Hồ sơ bài toán PLĐC, Barem 5 dạng đề thi chuẩn hóa, Kiến trúc CSDL SQLite và VRAM profiling. |
| **Ban Kỹ Thuật & Sản Phẩm** | [`Project/`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/Project/) | - | Toàn bộ mã nguồn backend FastAPI, CSDL văn bản luật, script nạp dữ liệu và kiểm thử PyTest tự động. |
| **Ban Cố Vấn & Vận Hành AI** | [`.agents/`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/.agents/) | [Agent Directives](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/.agents/rules/AGENTS.md) | Đội ngũ 6 AI Agents chuyên trách, bộ quy tắc Hard Rules và giao thức bàn giao ca. |
| **Khối Tiêu Chuẩn An Toàn AAP** | [`antigravity-agent-protocol/`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/antigravity-agent-protocol/) | [Safety Rules](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/antigravity-agent-protocol/RULES-SAFETY-GOVERNANCE.md) | Tài liệu lưu trữ tham chiếu về quy chuẩn an toàn vận hành AAP, Pre-flight impact analysis và SecOps. |

---

## 3. NGUYÊN TẮC VẬN HÀNH & BẬC THANG 4 TẦNG

```
TẦNG 1: BM25 Sparse Retrieval ➔ TẦNG 2: PhoBERT Dense Retrieval
                      │
                      ▼
TẦNG 3: RAG Qwen2.5-1.5B 4-bit ➔ TẦNG 4: LoRA Fine-tuned Model
```

- **Mọi thực nghiệm đều phải có Random Seed cố định (`torch.manual_seed(42)`, `np.random.seed(42)`)** để đảm bảo khả năng tái lập 100%.
- **Hoạt động tương thích phần cứng**: Toàn bộ hệ thống được tối ưu để huấn luyện và suy luận trơn tru trên card đồ họa rời RTX 3050 4GB (ngân sách VRAM $\le 3.5\text{GB}$) hoặc Google Colab T4.
- **Quy tắc Chống Ảo Giác Pháp Lý**: Mọi trích dẫn điều luật phải có căn cứ từ CSDL SQLite corpus, tuyệt đối không bịa số hiệu Điều/Khoản.

---

## 4. QUY TRÌNH ĐIỀU HÀNH & THEO DÕI TIẾN ĐỘ

1. **Trước mỗi ca làm việc**: AI Agent và Sinh viên mở [STATUS.md](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/STATUS.md) để kiểm tra tuần hiện tại và các task ưu tiên P0.
2. **Khai thác tài liệu**: Sử dụng [README.md](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/README.md) làm Master Sitemap để truy cập đúng tài liệu đặc tả mà không gây nhiễu loạn ngữ cảnh.
3. **Kết thúc ca làm việc**: Cập nhật mục `## Last Session` trong `STATUS.md` trước khi bàn giao.
