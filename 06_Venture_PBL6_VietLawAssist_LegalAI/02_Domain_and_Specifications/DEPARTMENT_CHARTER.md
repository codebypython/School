# ⚖️ PHÒNG NGHIỆP VỤ PHÁP LÝ & ĐẶC TẢ KỸ THUẬT (DOMAIN & SPECIFICATIONS DIVISION)
> **Phòng ban:** `02_Domain_and_Specifications` | **Dự án:** VietLawAssist — Hệ thống Trợ lý Thông minh Ôn thi Môn Pháp luật Đại cương  
> **Mã dự án:** `VENTURE-06-PBL6` | **Khoa CNTT — ĐHBK Đà Nẵng (DUT)**

---

## 📌 DANH MỤC HỒ SƠ ĐẶC TẢ (SPECIFICATIONS INVENTORY)

Phòng `02_Domain_and_Specifications/` chịu trách nhiệm lưu trữ toàn bộ các tài liệu đặc tả kiến trúc kỹ thuật, thiết kế dữ liệu và bộ tiêu chuẩn barem chấm thi của môn Pháp luật Đại cương:

| STT | Tên tệp hồ sơ | Mục đích sử dụng | Đối tượng đọc chính |
| :-: | :--- | :--- | :--- |
| **01** | [**`01_PROJECT_CONCEPT.md`**](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/02_Domain_and_Specifications/01_PROJECT_CONCEPT.md) | Thấu hiểu bối cảnh ra đời, nỗi đau của sinh viên khi ôn thi PLĐC, đối tượng thụ hưởng và giá trị sư phạm. | Giảng viên, Hội đồng phản biện, Sinh viên |
| **02** | [**`02_TECHNICAL_SPECIFICATIONS.md`**](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/02_Domain_and_Specifications/02_TECHNICAL_SPECIFICATIONS.md) | Đặc tả kỹ thuật chi tiết: Kiến trúc 4 tầng ML, CSDL SQLite, FAISS Index, cấu hình VRAM RTX 3050, FastAPI backend. | Kỹ sư ML, System Architect, Backend Dev |
| **03** | [**`03_EXAM_BAREM_TEMPLATES.md`**](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/02_Domain_and_Specifications/03_EXAM_BAREM_TEMPLATES.md) | Bộ khung barem 5 dạng đề thi cốt lõi + 1 dạng lý thuyết, cấu trúc JSON Schemas và các ví dụ output chuẩn sư phạm. | LLM Prompt Engineer, Evaluator, AI Agents |
| **04** | [**`04_PROJECT_ROADMAP.md`**](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/02_Domain_and_Specifications/04_PROJECT_ROADMAP.md) | Lộ trình kỹ thuật 15 tuần, phân kỳ chi tiết theo từng sprint và barem đối chiếu. | Project Manager, Kỹ sư trưởng |

---

## 🔒 NGUYÊN TẮC NGHIỆP VỤ BẤT KHẢ XÂM PHẠM
1. **Chuẩn barem tuyệt đối**: Mọi output sinh ra từ các tầng RAG / LoRA phải khớp 100% với JSON Schema trong `03_EXAM_BAREM_TEMPLATES.md`.
2. **Chống ảo giác pháp lý**: Mọi điều luật trích dẫn trong giải đề phải được đối soát với CSDL luật thực định, tuyệt đối không bịa số Điều/Khoản.
3. **Giới hạn tài nguyên phần cứng**: Toàn bộ mô hình và dịch vụ truy vấn phải vận hành ổn định trong ngân sách VRAM $\le 3.5\text{GB}$ của card đồ họa RTX 3050 (4GB).
