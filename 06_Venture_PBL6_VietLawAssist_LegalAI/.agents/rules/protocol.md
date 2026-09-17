# Agent Protocol — VietLawAssist (VENTURE-06-PBL6)

> Bộ quy tắc liên kết đội ngũ AI Agents với quy chuẩn vận hành dự án.
> File này được load tự động bởi hệ thống rules. Đọc [AGENTS.md](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/.agents/rules/AGENTS.md) trước nếu chưa hiểu dự án.

---

## 1. Quy trình Chuẩn cho Mỗi Phiên Làm việc

```
1. Đọc .agents/rules/AGENTS.md  → Hiểu identity, architecture, domain, rules
2. Đọc STATUS.md               → Biết task nào xong, task nào tiếp theo
3. Đọc file domain tùy task     → 02_Domain_and_Specifications/ (Barem, Specs) | 01_Strategy_and_Proposal/ (Rubrics)
4. Tiến hành task               → Tuân thủ Hard Rules (Section 2)
5. Cập nhật STATUS.md           → Ghi nhận kết quả phiên
```

## 2. Hard Rules — Quy tắc Bất khả xâm phạm

### 2.1 Machine Learning & Reproducibility
- `torch.manual_seed(42)` + `np.random.seed(42)` trong MỌI script ML
- VRAM budget ≤ 3.5GB (RTX 3050 4GB)
- Device-agnostic: `device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')`
- Chú thích Tensor Shape tại mỗi forward step: `# (batch_size, seq_len, hidden_dim)`

### 2.2 Database & Security
- 100% Parameterized Queries (`?` placeholder) — **CẤM** nối chuỗi SQL
- Zero Secrets in Code — mọi config nhạy cảm qua `.env` + `pydantic_settings`
- WAL mode + PRAGMA FK ON cho SQLite

### 2.3 Legal Domain — Chống Ảo giác Pháp lý
- **KHÔNG BAO GIỜ** bịa số Điều, Khoản, Điểm không tồn tại trong corpus
- Mọi trích dẫn `Điều X Khoản Y` phải verify từ bảng `law_articles` trong DB
- Nếu không tìm thấy điều luật trong DB → gắn tag `[Unverified]`
- Nếu tìm thấy → gắn tag `[Verified]`

### 2.4 Clean Code & Architecture
- Phân tầng: `api/routes/` → `services/` → `repositories/` → `core/` → `models/`
- TDD: RED → GREEN → REFACTOR
- Hàm không dài quá 30 dòng (Single Responsibility)
- 100% type hints + docstrings cho public functions

## 3. Quy chuẩn An toàn (AAP Reference)

Tham khảo thêm tại:
- [RULES-SAFETY-GOVERNANCE.md](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/antigravity-agent-protocol/RULES-SAFETY-GOVERNANCE.md) — Terminal governance, file integrity, SecOps
- [STEP-0-SESSION-ONBOARDING.md](file:///D:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/antigravity-agent-protocol/STEP-0-SESSION-ONBOARDING.md) — Pre-flight impact analysis (template generic)

### Danh sách đen lệnh Terminal (Cấm nếu chưa có xác nhận)
- `git reset --hard`, `git push --force`, `rm -rf`
- Tự ý cài package mới mà không giải thích

### Danh sách trắng (An toàn chạy tự động)
- `git status`, `git diff`, `git log -n 5`
- `pytest`, `python scripts/*.py --dry-run`
- `pip list`, `python --version`

## 4. Session Handover Format

Khi kết thúc phiên, cập nhật `STATUS.md` mục `## Last Session`:

```markdown
## Last Session
- **Date**: YYYY-MM-DD
- **Work Done**: [Liệt kê task đã hoàn thành]
- **Files Created**: [Danh sách file mới]
- **Files Modified**: [Danh sách file đã sửa]
- **Test Results**: [X/Y tests pass]
- **Blockers**: [Vấn đề chưa giải quyết]
- **Next Priority**: [Task ưu tiên cho phiên sau]
```
