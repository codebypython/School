# 📖 CẨM NANG GIAO TIẾP & QUY CHUẨN TÁC NGHIỆP AGENT (COMMUNICATION PLAYBOOK)
## School Holdings — Academic & Engineering Enterprise (Semester 7 DUT)

> **Mã văn kiện:** `HQ-PLAYBOOK-01`  
> **Phạm vi áp dụng:** Toàn bộ Hội đồng AI AOC, Ban Giám đốc Khối Trung ương, 6 Công ty con thành viên và Người điều hành (Handmade CEO).  
> **Mục tiêu:** Đảm bảo 100% các phiên làm việc (chat conversations) đều được định vị chuẩn xác, không lãng phí Context Window, giải quyết dứt điểm tình trạng Agent hỏi lại vòng vo hoặc thao tác sai thẩm quyền.

---

## 🧭 I. MÔ HÌNH VẬN HÀNH 3 CẤP (3-TIER CONVERSATION ONBOARDING)

Mỗi khi người dùng mở một cuộc hội thoại mới với bất kỳ AI Agent nào trong workspace này, quy trình nạp dữ liệu định hướng (Onboarding) diễn ra tự động theo sơ đồ sau:

```
┌─────────────────────────────────────────────────────────────────────────┐
│  TẦNG 0: CORPORATE ROUTER (Hệ thống tự nạp tự động)                     │
│  ⭐ Nhận diện [COMPANY-CODE] ➔ Định vị đúng Công ty & Vai trò Mentor    │
│  📍 File: D:\User\7th\School\AGENTS.md                                  │
│  📏 Ngân sách context: ~1.500 tokens                                    │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  TẦNG 1: SUBSIDIARY ENTRY POINT (Agent đọc theo chỉ dẫn từ Tầng 0)      │
│  ⭐ Identity ➔ Kiến trúc chuyên ngành ➔ Hard Rules ➔ Barem / Tiêu chuẩn │
│  📍 File: <company_dir>/AGENT_PROFILE.md hoặc .agents/rules/AGENTS.md   │
│  📏 Ngân sách context: ~2.000 tokens                                    │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  TẦNG 2: REAL-TIME STATUS DASHBOARD (Agent đọc để biết tiến độ)         │
│  ⭐ Tuần hiện tại ➔ Task đã xong ➔ Task đang dở ➔ Next Priority (P0)     │
│  📍 File: <company_dir>/STATUS.md                                       │
│  📏 Ngân sách context: ~1.000 tokens                                    │
└───────────────────────────────┬─────────────────────────────────────────┘
                                │
                                ▼
                    [XÁC NHẬN 2 DÒNG ➔ BẮT ĐẦU TÁC NGHIỆP]
```

> **Tổng ngân sách Onboarding:** $\le 5.000$ tokens ($< 0.5\%$ context window của Gemini / Claude). Agent nắm trọn vẹn bức tranh mà không cần hỏi lại bất kỳ câu nào.

---

## 🏷️ II. BẢNG MÃ ĐỊNH DANH CÔNG TY & ĐIỂM TIẾP NHẬN (ENTRY POINTS)

Khi bắt đầu prompt, người dùng sử dụng cú pháp `[COMPANY-CODE]` ở đầu câu để kích hoạt đúng Agent Mentor:

| Mã Tag | Tên Đơn Vị | Lĩnh Vực Chuyên Trách | File Tiếp Nhận (Tầng 1) | Bảng Tiến Độ (Tầng 2) |
|:---|:---|:---|:---|:---|
| `[CORP-01-CV]` | **VisionLab Corp** | Thị giác máy tính, CNN, YOLO, Szeliski, PyTorch | [`01_Strategy_and_Curriculum/AGENT_PROFILE.md`](file:///D:/User/7th/School/01_Company_Computer_Vision_CV/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [`STATUS.md`](file:///D:/User/7th/School/01_Company_Computer_Vision_CV/STATUS.md) |
| `[CORP-02-ML]` | **CoreAI Corp** | Học máy giải tích, SVM, XGBoost, Clustering, Sklearn | [`01_Strategy_and_Curriculum/AGENT_PROFILE.md`](file:///D:/User/7th/School/02_Company_Machine_Learning_ML/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [`STATUS.md`](file:///D:/User/7th/School/02_Company_Machine_Learning_ML/STATUS.md) |
| `[CORP-03-NMA]` | **NetAdmin Corp** | Quản trị mạng DUT, Cisco, DNS, DHCP, AD DS, Syslog | [`01_Strategy_and_Curriculum/AGENT_PROFILE.md`](file:///D:/User/7th/School/03_Company_Network_Management_NMA/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [`STATUS.md`](file:///D:/User/7th/School/03_Company_Network_Management_NMA/STATUS.md) |
| `[CORP-04-SEC]` | **CyberDefense** | An toàn mạng, Mật mã AES/RSA, PKI, Firewall, VPN | [`01_Strategy_and_Curriculum/AGENT_PROFILE.md`](file:///D:/User/7th/School/04_Company_Network_Security_SEC/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [`STATUS.md`](file:///D:/User/7th/School/04_Company_Network_Security_SEC/STATUS.md) |
| `[CORP-05-JPN]` | **Global Nihongo** | Tiếng Nhật N3 IT, Hán tự Kanji, Ngữ pháp Shinkanzen | [`01_Strategy_and_Curriculum/AGENT_PROFILE.md`](file:///D:/User/7th/School/05_Company_Japanese_Language_JPN/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [`STATUS.md`](file:///D:/User/7th/School/05_Company_Japanese_Language_JPN/STATUS.md) |
| `[VENTURE-06]` | **VietLawAssist** | Đồ án tốt nghiệp PBL6, RAG 4 tầng, Barem đề thi PLĐC | [`.agents/rules/AGENTS.md`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/.agents/rules/AGENTS.md) | [`STATUS.md`](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/STATUS.md) |
| `[CORP-07-ALGO]`| **AlgoCore Systems** | C++20, Quản trị bộ nhớ, DSA chuyên sâu, Cache, Concurrency | [`01_Strategy_and_Curriculum/AGENT_PROFILE.md`](file:///D:/User/7th/School/07_Company_Algorithms_and_Systems_ALGO/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [`STATUS.md`](file:///D:/User/7th/School/07_Company_Algorithms_and_Systems_ALGO/STATUS.md) |
| `[CORP-08-CRAFT]`| **SoftwareCraft** | OOP, OOAD, SOLID, 23 Design Patterns, TDD, Clean Architecture | [`01_Strategy_and_Curriculum/AGENT_PROFILE.md`](file:///D:/User/7th/School/08_Company_Software_Craftsmanship_and_Architecture_CRAFT/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [`STATUS.md`](file:///D:/User/7th/School/08_Company_Software_Craftsmanship_and_Architecture_CRAFT/STATUS.md) |
| `[CORP-09-AGILE]`| **AgileOps Corp** | Scrum Guide 2020, Git Internals, Trunk-Based, CI/CD, DevOps | [`01_Strategy_and_Curriculum/AGENT_PROFILE.md`](file:///D:/User/7th/School/09_Company_Agile_and_DevOps_Engineering_AGILE/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [`STATUS.md`](file:///D:/User/7th/School/09_Company_Agile_and_DevOps_Engineering_AGILE/STATUS.md) |
| `[CORP-10-WEB]` | **WebScale Corp** | JS V8 Engine, TypeScript Strict, React 19 / Next.js 15, NestJS | [`01_Strategy_and_Curriculum/AGENT_PROFILE.md`](file:///D:/User/7th/School/10_Company_WebScale_FullStack_Technologies_WEB/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [`STATUS.md`](file:///D:/User/7th/School/10_Company_WebScale_FullStack_Technologies_WEB/STATUS.md) |
| `[CORP-11-PY]`  | **PyScale Backend** | Python Data Model, AsyncIO, FastAPI, SQLAlchemy, Celery/Redis | [`01_Strategy_and_Curriculum/AGENT_PROFILE.md`](file:///D:/User/7th/School/11_Company_PyScale_Backend_and_Distributed_PY/01_Strategy_and_Curriculum/AGENT_PROFILE.md) | [`STATUS.md`](file:///D:/User/7th/School/11_Company_PyScale_Backend_and_Distributed_PY/STATUS.md) |
| `[HQ-PROMPT]` | **Prompt Intelligence Lab** | Tối ưu hóa mô hình (Gemini 3.1 Pro/3.8 Flash, Claude Sonnet/Opus), Động cơ Prompt chuyên biệt từng môn, Quản trị Working Memory | [`00_Corporate_Prompt_and_Cognitive_Lab/README.md`](file:///D:/User/7th/School/00_Corporate_Prompt_and_Cognitive_Lab/README.md) | [`STATUS.md`](file:///D:/User/7th/School/00_Corporate_Prompt_and_Cognitive_Lab/STATUS.md) |
| `[HQ-NOTION]` | **Notion LMS Hub** | CSDL quan hệ, Formula 2.0, Dashboard, Gamification | [`00_Central_Notion_LMS_Hub/HUB_CHARTER.md`](file:///D:/User/7th/School/00_Central_Notion_LMS_Hub/HUB_CHARTER.md) | - |
| `[HQ-VAULT]` | **Knowledge Vault** | 30+ nguồn học liệu kinh điển quốc tế, Thẩm định ER-QVR | [`00_Corporate_Knowledge_Vault/VAULT_CHARTER.md`](file:///D:/User/7th/School/00_Corporate_Knowledge_Vault/VAULT_CHARTER.md) | - |

---

## 🎯 III. BỘ PROMPT CHUYÊN BIỆT THEO MÔ HÌNH & CHUYÊN MÔN (DẠNG C CAO CẤP)

> [!IMPORTANT]
> **Khuyến nghị từ HQ-PROMPT Lab**: Để đạt hiệu năng cao nhất, không nên dùng prompt chung chung mà hãy truy cập trực tiếp vào **Động cơ Prompt Chuyên biệt** tương ứng với mô hình bạn đang sử dụng:
> - **Gemini 3.1 Pro & 3.8 Flash**: Xem [Nghiên cứu & Cú pháp tối ưu Gemini](file:///D:/User/7th/School/00_Corporate_Prompt_and_Cognitive_Lab/01_Model_Intelligence_Research/GEMINI_3_ARCHITECTURE_AND_OPTIMIZATION.md)
> - **Claude Sonnet & Claude Opus**: Xem [Nghiên cứu & Cú pháp thẻ XML tối ưu Claude](file:///D:/User/7th/School/00_Corporate_Prompt_and_Cognitive_Lab/01_Model_Intelligence_Research/CLAUDE_SONNET_OPUS_ARCHITECTURE_AND_OPTIMIZATION.md)
> - **Kho Prompt Chuyên Biệt 6 Môn**: Tra cứu tại [02_Domain_Cognitive_Engines](file:///D:/User/7th/School/00_Corporate_Prompt_and_Cognitive_Lab/02_Domain_Cognitive_Engines/) | [Ma Trận Lựa Chọn 1-Click](file:///D:/User/7th/School/00_Corporate_Prompt_and_Cognitive_Lab/04_Production_Playbooks/MASTER_PROMPT_MATRIX.md)

Dưới đây là 5 mẫu cơ sở (Quick Start) có gắn Working Memory Snapshot:

### 🚀 Mẫu 1: KHỞI ĐỘNG PHIÊN MỚI (New Task / New Week)
```markdown
[MÃ-CÔNG-TY] Khởi động phiên làm việc mới.
Mục tiêu: [Mô tả ngắn gọn mục tiêu, ví dụ: "Triển khai bài Lab 03 cấu hình DNS Forwarder trên Windows Server 2022"]
Yêu cầu: Đọc file AGENT_PROFILE (hoặc AGENTS.md) và STATUS.md trước khi đề xuất giải pháp.
```

### 🔄 Mẫu 2: TIẾP NỐI PHIÊN TRƯỚC (Continue Previous Work)
```markdown
[MÃ-CÔNG-TY] Tiếp nối phiên trước.
Tóm tắt phiên trước: [Đã làm xong việc X, đã pass test Y]
Nhiệm vụ phiên này: [Thực hiện tiếp việc Z theo mục Next Priority trong STATUS.md]
```

### 🎯 Mẫu 3: GIAO TASK CỤ THỂ (Targeted File Execution)
```markdown
[MÃ-CÔNG-TY] Task: [Tên task cụ thể]
Tệp tin liên quan: [Danh sách đường dẫn các file cần đọc hoặc chỉnh sửa]
Yêu cầu nghiệp vụ: [Mô tả chi tiết tiêu chuẩn kỹ thuật hoặc barem cần tuân thủ]
```

### 📊 Mẫu 4: THẨM ĐỊNH CHẤT LƯỢNG / REVIEW (Audit & Grading)
```markdown
[MÃ-CÔNG-TY] Yêu cầu Review & Thẩm định: [Tên bài Lab / Module / Tài liệu cần chấm]
Tiêu chuẩn đối chiếu: [Rubric DUT 10/10 / Thang đo ER-QVR 100đ / Chuẩn AAP]
Đầu ra mong muốn: Bảng chấm điểm chi tiết từng tiêu chí + Đề xuất cải tiến cụ thể.
```

### 🔥 Mẫu 5: XỬ LÝ SỰ CỐ KHẨN CẤP / HOTFIX (Troubleshooting)
```markdown
[MÃ-CÔNG-TY] Sự cố khẩn cấp: [Mô tả triệu chứng lỗi]
Môi trường: [HĐH, Python version, thiết bị mạng, cấu hình phần cứng]
Log chi tiết: 
[Dán đoạn log báo lỗi hoặc thông điệp lỗi tại đây]
Yêu cầu: Phân tích Root Cause ➔ Đưa ra giải pháp khắc phục tối thiểu (Minimal patch) ➔ Hướng dẫn verify.
```

---

## 📝 IV. QUY TRÌNH BÀN GIAO CA BẮT BUỘC (SESSION HANDOVER RULES)

Để bảo đảm tính liên tục giữa các phiên làm việc, **mọi Agent trước khi kết thúc ca làm việc đều PHẢI thực hiện 2 bước sau**:

### Bước 1: Cập nhật mục `## Last Session` trong `STATUS.md`
Agent tự động ghi đè hoặc bổ sung vào file `STATUS.md` của công ty phụ trách theo cấu trúc chuẩn:
```markdown
## Last Session
- **Date**: YYYY-MM-DD
- **Agent Role**: [Tên Agent / Mentor chuyên trách]
- **Completed**:
  - [x] [Tên công việc đã hoàn thành 1]
  - [x] [Tên công việc đã hoàn thành 2]
- **In Progress**:
  - [ ] [Công việc đang thực hiện dở dang]
- **Blockers / Khó khăn**: [Các điểm nghẽn kỹ thuật hoặc cần xác nhận của sinh viên]
- **Next Priority (P0)**: [Nhiệm vụ số 1 cần làm ngay ở ca tiếp theo]
```

### Bước 2: Thông báo ngắn gọn cho Người điều hành (Handmade CEO)
Xuất 1 đoạn tổng kết 3 dòng:
> *"Đã hoàn thành: [Task A]. Tiến độ hiện tại: [X%]. Đã cập nhật `STATUS.md`. Phiên tiếp theo sẵn sàng thực hiện: [Task B]."*

---

## 🔒 V. CÁC ĐIỀU RĂN KỸ THUẬT BẤT KHẢ XÂM PHẠM (CORPORATE DIRECTIVES)

1. **Academic Scaffolding**: Không giải hộ toàn bộ bài tập ngay lập tức. Dẫn dắt tư duy: `Bản chất (Tại sao) -> Cấu hình (Làm thế nào) -> Xác minh (Kiểm tra ra sao)`.
2. **Reproducibility First**: Mọi mã nguồn thực nghiệm ML/AI bắt buộc cố định `seed=42`.
3. **Anti-Hallucination**: Mọi trích dẫn điều luật, công thức RFC, hay lệnh cấu hình phải truy xuất từ tài liệu đã thẩm định, không được tự suy diễn hoặc bịa số hiệu.
4. **Zero-Clutter Policy**: Không tạo file nháp (`test1.py`, `temp.md`) nằm rải rác ngoài thư mục quy định. Tên tệp phải viết hoa hoặc phân cách bằng dấu gạch dưới chuẩn `SNAKE_CASE`, tuyệt đối không dùng khoảng trắng và ký tự có dấu.
