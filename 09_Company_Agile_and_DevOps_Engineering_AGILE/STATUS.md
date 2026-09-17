# 📊 PROJECT STATUS DASHBOARD — AgileOps Corp (CORP-09-AGILE)

> **Cập nhật lần cuối**: 2026-09-18 | **Tuần hiện tại**: Tuần 1 (Agile Mindset & Scrum Framework 2020)  
> **Mentor chuyên trách**: DUT Agile & DevOps Engineering Mentor (`AGENT_PROFILE.md`)

---

## Current Phase: 🔵 PHASE 1 — AGILE FOUNDATIONS & ADVANCED GIT (Tuần 1-6)

Tập trung thiết lập tư duy Agile Manifesto, bộ khung Scrum 2020 chuẩn mực, tiêu chuẩn User Story (INVEST), và làm chủ cấu trúc nội bộ của Git (Blobs, Trees, Commits, Branches).

---

## Implementation & Lab Progress

### Module 1: Triết Lý Agile & Bộ Khung Scrum 2020
- [x] Thiết lập công cụ quản lý dự án: GitHub Projects / Linear / Notion Agile Board
- [x] 4 Giá trị & 12 Nguyên lý của Agile Manifesto
- [ ] 3 Vai trò (PO, SM, Developers), 5 Sự kiện, 3 Hiện vật trong Scrum
- [ ] Viết User Story theo tiêu chuẩn INVEST & Kỹ thuật Planning Poker

### Module 2: Quản Trị Mã Nguồn Nâng Cao (Advanced Git)
- [ ] Git Internals: Hiểu cấu trúc Object Database (`.git/objects`)
- [ ] Chiến lược phân nhánh: GitFlow vs GitHub Flow vs Trunk-Based Development
- [ ] Làm chủ Git Rebase Interactive (`git rebase -i`), Squashing commits, Cherry-picking
- [ ] Giải quyết xung đột Merge Conflicts và bảo toàn lịch sử commit sạch

### Module 3: Code Review, Quality Gates & CI/CD
- [ ] Thiết lập Conventional Commits (`feat:`, `fix:`, `refactor:`, `chore:`)
- [ ] Pull Request Templates & Review Guidelines
- [ ] Xây dựng GitHub Actions Workflow tự động chạy Linter, Formatter và Tests

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | Sinh viên có thói quen commit trực tiếp vào nhánh `main`/`master` | 🔴 High | Bắt buộc bật Branch Protection Rules trên GitHub repo |

---

## Next Priority (P0)
- Tạo template repo cấu hình sẵn GitHub Actions CI workflow và Branch Protection Rules cho học viên fork.
