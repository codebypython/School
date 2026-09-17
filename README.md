# 🏛️ TẬP ĐOÀN HỌC THUẬT & CÔNG NGHỆ SCHOOL HOLDINGS
## School Holdings — Academic & Engineering Enterprise (Semester 7 DUT)

Chào mừng bạn đến với **School Holdings** — Hệ sinh thái Quản trị Tri thức và Nghiên cứu Kỹ thuật được tái cấu trúc toàn diện theo **Mô hình Tập đoàn Đa ngành 3 Cấp (3-Tier Enterprise Architecture)**. Mọi tài liệu, mã nguồn, bài giảng và công cụ đều được phân bổ có trật tự vào các Khối Hội đồng, Công ty con thành viên và các Phòng ban chuyên môn, đảm bảo tiêu chuẩn **Zero-Clutter (Không rác dữ liệu)** và minh bạch về quyền hạn tác nghiệp.

---

## 🏢 CƠ CẤU TỔ CHỨC TẬP ĐOÀN (HOLDING ORGANOGRAM)

```
                            🏛️ TẬP ĐOÀN SCHOOL HOLDINGS (ROOT)
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        ▼                               ▼                               ▼
┌──────────────────┐          ┌──────────────────┐          ┌──────────────────┐
│  .agents/        │          │  00_Central_     │          │  00_Corporate_   │
│  Ban Quản Trị &  │          │  Notion_LMS_Hub/ │          │  Knowledge_Vault/│
│  Hội Đồng AI AOC │          │  Khối Công Nghệ  │          │  Khối Tri Thức   │
└──────────────────┘          └──────────────────┘          └──────────────────┘
                                        │
                                        ▼
                              ┌──────────────────┐
                              │  00_Corporate_   │
                              │  Prompt_and_     │
                              │  Cognitive_Lab/  │
                              │  Khối Nhận Thức  │
                              └──────────────────┘
                                        │
    ┌───────────────┬───────────────────┼───────────────────┬───────────────┐
    ▼               ▼                   ▼                   ▼               ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ 01_Company_   │ │ 02_Company_   │ │ 03_Company_   │ │ 04_Company_   │ │ 05_Company_   │
│ Computer_     │ │ Machine_      │ │ Network_      │ │ Network_      │ │ Japanese_     │
│ Vision_CV/    │ │ Learning_ML/  │ │ Management_   │ │ Security_SEC/ │ │ Language_JPN/ │
│ VisionLab     │ │ CoreAI Corp   │ │ NMA/          │ │ CyberDefense  │ │ GlobalNihongo │
└───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘
        │
        ├───────────────────────────────────────────────────────────────────┐
        ▼                                                                   ▼
┌───────────────────────────────┐                           ┌───────────────────────────────┐
│ 06_Venture_PBL6_              │                           │ KHỐI KỸ NGHỆ PHẦN MỀM (SE)    │
│ VietLawAssist_LegalAI/        │                           │ 07_ALGO (C++ & DSA)           │
│ VietLawAssist Venture         │                           │ 08_CRAFT (OOP/OOAD/TDD)       │
└───────────────────────────────┘                           │ 09_AGILE (Scrum/Git/CI-CD)    │
                                                            │ 10_WEB (JS/TS & Next/Nest)    │
                                                            │ 11_PY (Python & Microservices)│
                                                            └───────────────────────────────┘
```

---

## 🏛️ I. KHỐI TRUNG ƯƠNG & HỘI ĐỒNG LÃNH ĐẠO (CORPORATE HEADQUARTERS)

| Mã Khối | Tên Khối Chuyên Trách | Thư Mục Quản Lý | Điều Lệ Đơn Vị | Chức Năng Cốt Lõi |
| :---: | :--- | :--- | :---: | :--- |
| **`HQ-AOC`** | **Ban Tổng Giám Đốc & Hội Đồng AI AOC** | [`.agents/`](./.agents) | [AOP Protocol](./.agents/rules/academic_operations_protocol.md) | Vận hành 5 Agent lãnh đạo (`ACD-01`, `SMS-02`, `EKC-03`, `PSD-04`, `NKA-05`) và vai trò Kỹ Sư Trưởng Handmade (`HM-00`). |
| **`HQ-PROMPT`**| **Trung Tâm Nghiên Cứu Prompt Nhận Thức** | [`00_Corporate_Prompt_and_Cognitive_Lab/`](./00_Corporate_Prompt_and_Cognitive_Lab) | [Lab Charter](./00_Corporate_Prompt_and_Cognitive_Lab/COMPANY_CHARTER.md) | Tối ưu hóa chuyên sâu mô hình (Gemini 3.1 Pro/3.8 Flash, Claude Sonnet/Opus), Động cơ Prompt chuyên biệt từng môn, Quản trị Working Memory. |
| **`HQ-NOTION`**| **Trung Tâm Công Nghệ Số Notion** | [`00_Central_Notion_LMS_Hub/`](./00_Central_Notion_LMS_Hub) | [Hub Charter](./00_Central_Notion_LMS_Hub/HUB_CHARTER.md) | Quản lý toàn bộ hệ sinh thái CSDL quan hệ Notion, thư viện công thức Formula 2.0 và Dashboard Command Center. |
| **`HQ-VAULT`** | **Khối Tri Thức Kinh Điển Quốc Tế** | [`00_Corporate_Knowledge_Vault/`](./00_Corporate_Knowledge_Vault) | [Vault Charter](./00_Corporate_Knowledge_Vault/VAULT_CHARTER.md) | Thư viện 30+ nguồn giáo trình kinh điển quốc tế (Stanford, MIT, Cisco, Pearson, Shinkanzen, O'Reilly) thẩm định theo chuẩn ER-QVR 100 điểm. |

---

## 🏢 II. DANH MỤC 11 CÔNG TY CON THÀNH VIÊN (SUBSIDIARY UNITS)

| Mã Công Ty | Tên Thương Mại | Thư Mục Công Ty | Điểm Tiếp Nhận (Tầng 1) | Tiến Độ Realtime (Tầng 2) | Lĩnh Vực Chuyên Môn |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **`CORP-01-CV`** | **VisionLab Deep Tech Corp** | [`01_Company_Computer_Vision_CV/`](./01_Company_Computer_Vision_CV) | [Agent Profile](./01_Company_Computer_Vision_CV/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [STATUS.md](./01_Company_Computer_Vision_CV/STATUS.md) | Xử lý ảnh số, Hình học thị giác cổ điển, Deep Learning Backbones, Object Detection, Semantic Segmentation. |
| **`CORP-02-ML`** | **CoreAI Solutions & Intelligence** | [`02_Company_Machine_Learning_ML/`](./02_Company_Machine_Learning_ML) | [Agent Profile](./02_Company_Machine_Learning_ML/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [STATUS.md](./02_Company_Machine_Learning_ML/STATUS.md) | Toán học học máy giải tích, Hồi quy, SVM, Cây quyết định, Ensemble XGBoost, Phân cụm KMeans/FCM, PCA và Sklearn Pipeline. |
| **`CORP-03-NMA`** | **Enterprise NetAdmin & Infrastructure**| [`03_Company_Network_Management_NMA/`](./03_Company_Network_Management_NMA) | [Agent Profile](./03_Company_Network_Management_NMA/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [STATUS.md](./03_Company_Network_Management_NMA/STATUS.md) | Mô hình FCAPS, Quy hoạch IP/Subnetting, Dịch vụ lõi DHCP/DNS/Routing, Active Directory & LDAP, Giám sát SNMP/Syslog. |
| **`CORP-04-SEC`** | **CyberDefense & Cryptography Corp** | [`04_Company_Network_Security_SEC/`](./04_Company_Network_Security_SEC) | [Agent Profile](./04_Company_Network_Security_SEC/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [STATUS.md](./04_Company_Network_Security_SEC/STATUS.md) | Mật mã học ứng dụng (AES, RSA, SHA, PKI), Giao thức bảo mật TLS 1.3 & IPsec VPN, Danh sách ACL, Tường lửa ZBF, Wireshark. |
| **`CORP-05-JPN`** | **Global Nihongo Engineering Institute**| [`05_Company_Japanese_Language_JPN/`](./05_Company_Japanese_Language_JPN) | [Agent Profile](./05_Company_Japanese_Language_JPN/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [STATUS.md](./05_Company_Japanese_Language_JPN/STATUS.md) | Tiếng Nhật kỹ thuật IT, 214 Bộ thủ Hán tự, Ngữ pháp tương phản N3, Đọc hiểu bắt từ khóa và Luyện nghe Shadowing. |
| **`VENTURE-06`** | **VietLawAssist Legal Tech Venture** | [`06_Venture_PBL6_VietLawAssist_LegalAI/`](./06_Venture_PBL6_VietLawAssist_LegalAI) | [Agent Directives](./06_Venture_PBL6_VietLawAssist_LegalAI/.agents/rules/AGENTS.md) | [STATUS.md](./06_Venture_PBL6_VietLawAssist_LegalAI/STATUS.md) | Đồ án tốt nghiệp PBL6: Hệ thống hỏi đáp pháp luật RAG 4 tầng (BM25 $\rightarrow$ PhoBERT FAISS $\rightarrow$ RAG Qwen2.5 $\rightarrow$ LoRA Fine-tune). |
| **`CORP-07-ALGO`** | **AlgoCore Systems Corp** | [`07_Company_Algorithms_and_Systems_ALGO/`](./07_Company_Algorithms_and_Systems_ALGO) | [Agent Profile](./07_Company_Algorithms_and_Systems_ALGO/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [STATUS.md](./07_Company_Algorithms_and_Systems_ALGO/STATUS.md) | C++20, Quản trị bộ nhớ Stack/Heap, Smart Pointers, Cấu trúc dữ liệu & Giải thuật nâng cao (CLRS), Cache Locality, Concurrency. |
| **`CORP-08-CRAFT`** | **SoftwareCraft Architecture Corp** | [`08_Company_Software_Craftsmanship_and_Architecture_CRAFT/`](./08_Company_Software_Craftsmanship_and_Architecture_CRAFT) | [Agent Profile](./08_Company_Software_Craftsmanship_and_Architecture_CRAFT/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [STATUS.md](./08_Company_Software_Craftsmanship_and_Architecture_CRAFT/STATUS.md) | Lập trình Hướng đối tượng nâng cao, Nguyên lý SOLID, 23 Design Patterns (GoF), OOAD UML, TDD (Red-Green-Refactor) & Clean Architecture. |
| **`CORP-09-AGILE`** | **AgileOps Engineering Corp** | [`09_Company_Agile_and_DevOps_Engineering_AGILE/`](./09_Company_Agile_and_DevOps_Engineering_AGILE) | [Agent Profile](./09_Company_Agile_and_DevOps_Engineering_AGILE/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [STATUS.md](./09_Company_Agile_and_DevOps_Engineering_AGILE/STATUS.md) | Quy trình Scrum 2020, Extreme Programming, Git Internals, Phân nhánh Trunk-Based/GitFlow, Code Review và CI/CD Pipelines. |
| **`CORP-10-WEB`** | **WebScale Technologies Corp** | [`10_Company_WebScale_FullStack_Technologies_WEB/`](./10_Company_WebScale_FullStack_Technologies_WEB) | [Agent Profile](./10_Company_WebScale_FullStack_Technologies_WEB/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [STATUS.md](./10_Company_WebScale_FullStack_Technologies_WEB/STATUS.md) | JavaScript Engine V8, TypeScript Strict Mode, Modern React, Next.js 15 App Router (RSC), NestJS Enterprise Backend & WebSockets. |
| **`CORP-11-PY`** | **PyScale Backend & Distributed Corp** | [`11_Company_PyScale_Backend_and_Distributed_PY/`](./11_Company_PyScale_Backend_and_Distributed_PY) | [Agent Profile](./11_Company_PyScale_Backend_and_Distributed_PY/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [STATUS.md](./11_Company_PyScale_Backend_and_Distributed_PY/STATUS.md) | CPython Data Model (`__dunder__`), Lập trình bất đồng bộ AsyncIO, FastAPI High-Performance, SQLAlchemy 2.0 Async, Celery + Redis. |

---

## 📂 III. CẤU TRÚC PHÒNG BAN CHUẨN MỰC TRONG MỖI CÔNG TY

Mọi công ty thành viên đều được tổ chức theo các phòng ban chức năng thống nhất:
1. **`01_Strategy_and_Curriculum/`** (hoặc `01_Strategy_and_Proposal/`): Ban Chiến lược, Lộ trình 15 tuần chuẩn và Hồ sơ Mentor. *(Có file `DEPARTMENT_CHARTER.md` / `AGENT_PROFILE.md`)*.
2. **`02_Lectures_and_Raw_Materials/`** (hoặc `02_Domain_and_Specifications/`): Ban Tư liệu lưu trữ slide gốc, đặc tả kỹ thuật, barem đề thi chuẩn.
3. **`03_Engineering_Labs_and_Code/`** (hoặc `Project/`): Ban Kỹ thuật & Thực nghiệm lưu trữ mã nguồn, notebook, dữ liệu bài lab / đồ án.
4. **`04_Notion_Digital_Workspace/`**: Ban Số hóa lưu trữ các file Markdown sẵn sàng import trực tiếp vào Notion LMS.
5. **`05_Troubleshooting_and_Toolkits/`**: Ban Kiểm soát sự cố, phần mềm chuyên dụng và cẩm nang xử lý lỗi.

---

## 🚀 HƯỚNG DẪN ĐIỀU HƯỚNG DÀNH CHO SINH VIÊN & AI AGENT

- **📖 Cẩm nang Giao tiếp & Mẫu Prompt Chuẩn**: Mở [COMMUNICATION_PLAYBOOK.md](./COMMUNICATION_PLAYBOOK.md) (Copy mẫu prompt để bắt đầu mọi ca làm việc).
- **Xem hiến chương điều hành toàn tập đoàn**: Đọc [AGENTS.md](./AGENTS.md).
- **Lập kế hoạch tuần mới**: Mở [MANUAL_OPERATOR_GUIDE.md](./.agents/team/handmade/MANUAL_OPERATOR_GUIDE.md).
- **Xem kho công thức Notion 2.0**: Mở [NOTION_ADVANCED_FORMULAS.md](./00_Central_Notion_LMS_Hub/NOTION_ADVANCED_FORMULAS.md).
- **Tra cứu tài liệu kinh điển quốc tế**: Mở [EXTERNAL_KNOWLEDGE_VAULT.md](./00_Corporate_Knowledge_Vault/EXTERNAL_KNOWLEDGE_VAULT.md).

