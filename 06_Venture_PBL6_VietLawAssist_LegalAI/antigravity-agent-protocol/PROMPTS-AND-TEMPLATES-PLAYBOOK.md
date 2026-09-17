# THƯ VIỆN PROMPT MẪU CHUẨN HÓA (PROMPTS PLAYBOOK)
> **Vị trí tài liệu:** `d:\Development\TDD concept\antigravity-agent-protocol\PROMPTS-AND-TEMPLATES-PLAYBOOK.md`  
> **Mục đích:** Cung cấp bộ Prompt mẫu có cấu trúc kỹ thuật chặt chẽ (Boundary + Objective + Stop Conditions) cho từng giai đoạn làm việc với Antigravity.

---

## 1. PROMPT KHỞI ĐỘNG PHIÊN & PHÂN TÍCH TÁC ĐỘNG (SESSION START)

```markdown
Đọc STEP-0-SESSION-ONBOARDING.md và RULES-SAFETY-GOVERNANCE.md.
Mục tiêu của tôi trong phiên làm việc này là: [Mô tả tính năng / bài toán cần giải quyết].

Yêu cầu Agent:
1. Quét trạng thái Git và dependencies hiện tại.
2. Liệt kê danh sách các tệp dự kiến sẽ đọc và ước tính token.
3. Xuất bảng [PRE-FLIGHT IMPACT & CONTEXT BUDGET REPORT] theo mẫu chuẩn.
4. Đưa ra các giải pháp quan trọng cần thực hiện trước khi viết code (Checkpoint Git, kiểm tra biến môi trường).
5. Tuyệt đối KHÔNG tự ý sửa file hoặc chạy lệnh terminal thay đổi hệ thống khi tôi chưa xác nhận báo cáo.
```

---

## 2. PROMPT YÊU CẦU LẬP IMPLEMENTATION PLAN (PLANNING FIRST)

```markdown
Dựa trên kết quả phân tích hiện trạng, hãy kích hoạt Planning Mode và tạo tài liệu `implementation_plan.md`.

Bản kế hoạch bắt buộc phải bao gồm:
1. Mục tiêu và bối cảnh kỹ thuật.
2. Bảng phân tích rủi ro & những quyết định cần tôi duyệt (User Review Required).
3. Danh sách các câu hỏi làm rõ (Open Questions).
4. Chi tiết từng bước thực hiện phân nhóm theo từng file ([NEW], [MODIFY], [DELETE]).
5. Kế hoạch kiểm thử tự động (Automated Tests) và kiểm thử thủ công (Manual Verification).
```

---

## 3. PROMPT THỰC THI TDD CHUẨN CÔNG NGHIỆP (TDD IMPLEMENTATION)

```markdown
Tuân thủ quy chuẩn TDD Workflow và Coding Standards trong rules.
Chúng ta sẽ thực hiện Task: [Tên Task cụ thể].

Quy trình bắt buộc:
- Bước 1 (RED): Viết file Unit Test trong thư mục tests/ mô tả đúng hành vi mong muốn. Chạy test để chứng minh bài test đang FAIL.
- Bước 2 (GREEN): Viết mã triển khai tối thiểu trong file nguồn để bài test chuyển sang PASS.
- Bước 3 (REFACTOR): Tối ưu hóa mã nguồn, đảm bảo Clean Code và không phá vỡ bất kỳ test nào.
Báo cáo lại kết quả chạy test sau mỗi bước.
```

---

## 4. PROMPT CHẨN ĐOÁN LỖI SÂU & HOTFIX KHẨN CẤP (DEEP DIAGNOSIS)

```markdown
Hệ thống gặp sự cố sau khi thực thi:
- Mô tả lỗi: [Mô tả hiện tượng]
- Log lỗi / Stack trace:
```
[Dán đoạn log lỗi vào đây]
```

Yêu cầu Agent:
1. Xác định nguyên nhân gốc rễ (Root Cause Analysis - RCA).
2. Kiểm tra xem lỗi do logic mã nguồn, sai lệch kiểu dữ liệu, hay thiếu biến môi trường.
3. Đề xuất bản vá tối thiểu (Minimal Patch) không gây ảnh hưởng chéo (No side-effects) tới các module khác.
4. Chạy lại test suite để xác nhận lỗi đã được khắc phục hoàn toàn.
```

---

## 5. PROMPT RÀ SOÁT BẢO MẬT & CHECKLIST OWASP TRƯỚC KHI BÀN GIAO

```markdown
Đọc tài liệu @RULES-SAFETY-GOVERNANCE.md và skill @security-review.
Hãy thực hiện rà soát an ninh toàn bộ các thay đổi vừa thực hiện:

Kiểm tra nghiêm ngặt:
- [ ] Có hardcode secrets / API keys nào trong mã nguồn không?
- [ ] Tất cả câu truy vấn database đã được tham số hóa (Parameterized) chống SQLi chưa?
- [ ] Dữ liệu đầu vào của người dùng đã được validate bằng schema (Zod/Pydantic) chưa?
- [ ] Token xác thực có được bảo vệ qua HttpOnly Cookie không?
- [ ] Có lộ thông tin nhạy cảm qua `console.log` hoặc thông báo lỗi không?
Xuất bảng ma trận đánh giá rủi ro và các khuyến nghị khắc phục.
```

---

## 6. PROMPT YÊU CẦU XUẤT BẢN BÁO CÁO TỔNG KẾT PHIÊN (SESSION HANDOVER)

```markdown
Chúng ta đã hoàn thành xong nhiệm vụ của phiên làm việc này.
Hãy thực hiện:
1. Chạy toàn bộ test suite để đảm bảo 100% tests PASS.
2. Kiểm tra `git status --short` để đảm bảo không còn file rác chưa dọn.
3. Xuất Bản Báo Cáo Tổng Kết Phiên Làm Việc (Session Handover Card) theo định dạng chuẩn tại RULES-SAFETY-GOVERNANCE.md để tôi gửi cho Tech Lead / Giảng viên hướng dẫn.
```

---

## 7. PROMPT NÉN NGỮ CẢNH KHI PHIÊN CHAT BẮT ĐẦU DÀI (COMPACTION PROMPT)

```markdown
Phiên hội thoại hiện tại đã dài. Hãy thực hiện nén ngữ cảnh (/compact) với các tiêu chí:
1. Tóm tắt ngắn gọn các quyết định kiến trúc và tính năng ĐÃ HOÀN THÀNH.
2. Lưu giữ trạng thái các biến, cấu hình và file đang chỉnh sửa dở dang.
3. Xóa bỏ toàn bộ các đoạn log lỗi dài và mã nguồn trung gian đã xử lý xong.
4. Báo cáo dung lượng ngữ cảnh sau khi nén.
```
