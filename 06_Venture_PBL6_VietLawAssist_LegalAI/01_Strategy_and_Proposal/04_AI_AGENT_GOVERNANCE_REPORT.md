# 🔬 BÁO CÁO NGHIÊN CỨU: THỰC TRẠNG ỨNG DỤNG AI & QUY TRÌNH QUẢN TRỊ AGENTS TRONG PHÁT TRIỂN PHẦN MỀM
> **Mã tài liệu:** `RESEARCH-AI-GOV-2026`  
> **Lĩnh vực:** Kỹ nghệ Phần mềm Tác tử (Agentic Software Engineering) & Quản trị Bối cảnh (Context Governance)  
> **Tác giả:** Ban Nghiên cứu & Phát triển — VietLawAssist Venture (PBL6 DUT)

---

## 1. TỔNG QUAN XU THẾ ỨNG DỤNG AI AGENTS TRONG KỸ NGHỆ PHẦN MỀM

Trong giai đoạn 2024–2026, ngành công nghệ thông tin đã chứng kiến sự dịch chuyển mang tính bước ngoặt: từ việc lập trình viên sử dụng các công cụ hỗ trợ gợi ý mã dòng lệnh đơn lẻ (Code Completion) sang việc vận hành **các Tác tử Trí tuệ Nhân tạo Tự chủ (Autonomous AI Coding Agents)** như Claude Code, Cursor, Codex, và Antigravity IDE.

Các hệ thống Agentic AI này không chỉ sinh mã nguồn theo yêu cầu mà còn có khả năng:
* Tự động điều hướng và duyệt qua cây thư mục phức tạp.
* Đọc, chỉnh sửa tệp và gọi các công cụ kiểm thử dòng lệnh (Terminal Tools).
* Tự quan sát lỗi biên dịch (Compilation / Linting Errors) để thực hiện vòng lặp tự sửa lỗi (Self-healing Loop).

---

## 2. THÁCH THỨC CỐT TỬ: MẤT KIỂM SOÁT NGỮ CẢNH VÀ SUY GIẢM BỘ NHỚ

Mặc dù có năng lực mạnh mẽ, các AI Agents đối mặt với 3 thách thức kỹ thuật lớn trong môi trường phát triển thực tế:

1. **Hiện tượng Suy giảm Độ chính xác Ngữ cảnh (Context Rot):**  
   Khi phiên làm việc kéo dài qua nhiều tác vụ, lịch sử hội thoại tích lũy hàng chục nghìn tokens. Sự xuất hiện của các đoạn log kiểm thử hoặc mã nguồn cũ gây nhiễu, làm mô hình dễ quên các chỉ thị gốc (System Instructions) và bắt đầu sinh mã sai chuẩn.
2. **Khởi đầu Không Ngữ cảnh (Zero-Context Problem):**  
   Mỗi phiên làm việc mới luôn xuất phát từ trạng thái bộ nhớ trắng. Nếu không có cơ chế quản trị tri thức, kỹ sư phải lặp đi lặp lại các chỉ thị cấu hình cơ bản, gây lãng phí thời gian và tăng chi phí token cơ sở.
3. **Ảo giác vị trí tệp (File Map Hallucination):**  
   Trong các dự án quy mô lớn, Agent thường tự ý tạo tệp mới sai vị trí cấu trúc phân tầng (ví dụ: đặt hàm truy vấn CSDL ngay trong Controller).

---

## 3. GIẢI PHÁP QUẢN TRỊ: CONTEXT BUDGETING & PRE-FLIGHT INSPECTION

Để giải quyết bài toán này, các hệ thống kỹ nghệ tác tử hiện đại áp dụng quy trình kiểm soát bắt buộc gồm hai giai đoạn:

```
[Nhận Prompt Người dùng]
           │
           ▼
┌─────────────────────────────────────────────────────────────┐
│ GIAI ĐOẠN 1: DRY-RUN FILE DISCOVERY                         │
│ • Quét danh sách tệp cần đọc dựa trên yêu cầu               │
│ • Dự toán số lượng token của các tệp + lịch sử hội thoại    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ GIAI ĐOẠN 2: BÁO CÁO DỰ TOÁN NGỮ CẢNH (PRE-FLIGHT REPORT)    │
│ • Tính toán: (Dung lượng yêu cầu / Giới hạn Token của Model)│
│ • Đánh giá ngưỡng an toàn:                                  │
│   - < 60%: An toàn, cho phép thực thi                       │
│   - 60% - 80%: Cảnh báo, đề xuất nén ngữ cảnh (/compact)    │
│   - > 80%: Dừng lại, bắt buộc phân rã tác vụ (Decomposition)│
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼ (Xác nhận từ Kỹ sư)
[Tiến hành Đọc tệp, Lập kế hoạch & Thực thi Mã nguồn]
```

### Phương án Triển khai Kỹ thuật:
- **Cấu hình System Prompt:** Đóng gói chỉ thị bắt buộc vào `CLAUDE.md`, `.cursorrules` hoặc bộ quy tắc `.agents/rules/protocol.md`.
- **Tích hợp Middleware MCP (Model Context Protocol):** Đặt một lớp chặn (Interceptor) đếm token trước mọi tool call `read_file`.
- **Phân tách phiên làm việc (Session Decomposition):** Chia nhỏ chu kỳ phát triển thành các phiên độc lập (Phiên thiết kế $\rightarrow$ Phiên viết mã $\rightarrow$ Phiên kiểm thử QA).

---

## 4. HẠ TẦNG KỸ NĂNG TÁC TỬ (AGENT SKILLS REPOSITORIES & ROUTING)

Các kho lưu trữ kỹ năng (như `awesome-skills`, `agent-rules-books`, `antigravity-agent-protocol`) đóng vai trò là **tầng hạ tầng tri thức (Knowledge Infrastructure)** giải quyết bài toán vận hành:

### Cơ chế "Nạp Lười" 3 Lớp (Progressive Disclosure)
Để mở rộng hàng trăm kỹ năng mà không làm phình to bộ nhớ:
* **Lớp 1 — Discovery (Khám phá):** Chỉ lưu phần mô tả ngắn (description) của kỹ năng trong bộ nhớ (~vài KB).
* **Lớp 2 — Activation (Kích hoạt):** Chỉ nạp toàn văn tệp `SKILL.md` khi người dùng kích hoạt đúng nghiệp vụ liên quan.
* **Lớp 3 — Reference (Tham chiếu):** Chỉ nạp các sơ đồ kiến trúc hoặc danh mục lỗi chuyên sâu khi bước thực thi yêu cầu cụ thể.

---

## 5. ÁP DỤNG THỰC TIỄN VÀO HỆ THỐNG DOANH NGHIỆP VIETLAWASSIST

Trong khuôn khổ Đồ án Chuyên ngành PBL6, nhóm đã chuyển hóa toàn bộ các nghiên cứu trên thành bộ tiêu chuẩn vận hành nội bộ:

1. **Xây dựng Bộ quy chuẩn Antigravity Agent Protocol (AAP):**  
   Gồm các quy trình `STEP-0-SESSION-ONBOARDING.md` (Pre-flight check) và `RULES-SAFETY-GOVERNANCE.md` (File integrity, SecOps, Handover report).
2. **Cơ cấu Tổ chức Đa Tác tử (Multi-Agent Team):**  
   Phân công chuyên môn hóa cho 6 AI Agents độc lập (`PM-01`, `MLR-02`, `DE-03`, `SA-04`, `EVAL-05`, `RW-06`) phối hợp với Kỹ sư trưởng (`Role Handmade`), loại bỏ hoàn toàn tình trạng mã nguồn sinh ra tự phát, sai vị trí hoặc vượt trần tài nguyên.
