# 📜 ĐIỀU LỆ PHÒNG CHIẾN LƯỢC & LỘ TRÌNH ĐÀO TẠO (STRATEGY & CURRICULUM DEPT)
## Phòng 01 — Công Ty Công Nghệ Web Full-Stack & Hệ Sinh Thái JS/TS (CORP-10-WEB)

> **Mã Phòng Ban:** `WEB-DEPT-01`  
> **Trưởng phòng phụ trách:** Agent `PSD-04` (Pedagogical Scaffolding Designer) & `ACD-01` (Academic Curriculum Director)  
> **Tiêu chuẩn học thuật:** You Don't Know JS Yet (Getify) / TypeScript Handbook (Microsoft) / React.dev / Next.js 15 / NestJS 10

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Chiến Lược & Lộ Trình là **bộ não định hình công nghệ Web Full-Stack hiện đại**:
1. **Thiết Kế Khung Chương Trình 15 Tuần Chuẩn**: Dẫn dắt học viên từ Bản chất V8 Engine & Bất đồng bộ $\rightarrow$ TypeScript Nâng cao $\rightarrow$ React 19 & Next.js 15 App Router (RSC) $\rightarrow$ Backend NestJS Modular IoC $\rightarrow$ Real-time WebSockets & Capstone Full-stack.
2. **Cập Nhật Chuẩn Công Nghệ Mới Nhất**: Tuyệt đối không dạy Class Components cũ kỹ trong React, không dạy Pages Router lỗi thời trong Next.js; cập nhật 100% sang Function Components, Custom Hooks, Server Components, và Server Actions.
3. **Đảm Bảo Chuẩn Đầu Ra Kỹ Sư Full-Stack**: Học viên có khả năng tự tay xây dựng ứng dụng Web hoàn chỉnh có độ an toàn kiểu tĩnh từ Frontend đến Database (End-to-End Type Safety).

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (PEDAGOGICAL INVARIANTS)

1. **Tuân Thủ Mô Hình 4 Tầng Sư Phạm**:
   - Mọi tuần học bắt buộc phải có: *Tầng 1 (Bản chất V8 Runtime/Giao thức HTTP)* $\rightarrow$ *Tầng 2 (Cài đặt TypeScript/Next.js/NestJS)* $\rightarrow$ *Tầng 3 (⚠️ Cảnh báo Hydration Mismatch & Re-render loop)* $\rightarrow$ *Tầng 4 (Bài lab Full-Stack)*.
2. **Nguyên Tắc Dạy Bản Chất Trước Khi Dạy Framework**:
   - Bắt buộc học viên phải hiểu sâu về Closures, Event Loop, Prototypal Inheritance và TypeScript Generics trước khi chạm vào React hay NestJS.
3. **Quy Tắc Nghiêm Cấm Kiểu `any` Trong Mọi Bài Giảng**:
   - Mọi đoạn code mẫu trong bài giảng hoặc slide tuyệt đối không được chứa kiểu `any`. Bắt buộc dùng `unknown`, generics hoặc discriminated unions.

---

## 🛠️ 3. TOOLCHAIN & SKILLS ROUTE ĐÀO TẠO FULL-STACK

| Hạng Mục | Bộ Công Cụ & Thước Đo | Mục Đích Sư Phạm |
| :--- | :--- | :--- |
| **Runtime & Trình quản lý gói** | Node.js 20+ LTS, PNPM / Bun | Quản lý monorepo và dependencies nhanh chóng |
| **Kiểm tra Kiểu & Linter** | TypeScript 5.5+, ESLint, Biome | Đảm bảo an toàn kiểu tĩnh và format tự động |
| **Khung Kiểm thử Tự động** | Vitest, React Testing Library, Playwright | Unit test component và E2E testing toàn diện |
| **Kiến trúc Frameworks** | Next.js 15 (App Router), NestJS 10, Prisma ORM | Xây dựng full-stack enterprise application |

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
01_Strategy_and_Curriculum/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📄 AGENT_PROFILE.md                      # Hồ sơ năng lực Mentor AI WebScale
├── 📄 ROADMAP_AND_CURRICULUM.md             # Giáo trình Master 15 tuần Web Full-Stack
├── 📁 rubrics/                              # Thang điểm đánh giá đồ án
│   └── fullstack_capstone_rubric.md        # Tiêu chí chấm điểm đồ án Next.js & NestJS
└── 📁 exam_blueprints/                      # Ma trận đề thi trắc nghiệm & thực hành
    ├── midterm_frontend_blueprint.md        # Đề thi giữa kỳ: V8, TS, React Hooks
    └── final_fullstack_blueprint.md         # Đề thi cuối kỳ: Next.js, NestJS, Real-time
```

---

## 💻 5. MẪU THIẾT KẾ BÀI HỌC 4 TẦNG QUY CHUẨN (GOLD MASTER SYLLABUS UNIT)

```markdown
### Tuần X: [Tên Chủ Đề Web Full-Stack]
- **Tầng 1 (Bản chất V8 Runtime & Browser DOM - Nguồn: YDKJSY / MDN)**:
  - Cơ chế thực thi của Event Loop (Call Stack, Web APIs, Task Queue, Microtask Queue).
  - Vòng đời Component: Reconciliation, Virtual DOM vs Incremental DOM.
- **Tầng 2 (Cài đặt Modern Next.js 15 & TypeScript)**:
  - Tách biệt rõ ràng Server Components (RSC) vs Client Components (`'use client'`).
  - Code mẫu an toàn kiểu với Zod Schema Validation và Server Actions.
- **Tầng 3 (⚠️ Cảnh báo bẫy thường gặp & Anti-patterns)**:
  - Bẫy Hydration Mismatch do render dữ liệu không đồng nhất giữa Server và Client.
  - Bẫy Infinite Re-rendering do khai báo dependencies trong `useEffect` sai cách.
- **Tầng 4 (Bài tập Lab & Tiêu chí DoD)**:
  - Đề bài: Triển khai tính năng với 100% Type-Safe API, Pass toàn bộ Vitest test cases.
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU GIÁO TRÌNH (DEFINITION OF READY - DoR)

- [ ] **DoR-1**: Khung chương trình bám sát tài liệu chính thức mới nhất của Next.js 15 và NestJS 10.
- [ ] **DoR-2**: Các bài học về React đều có sơ đồ luồng dữ liệu (Data Flow) và vòng đời Render Phase vs Commit Phase.
- [ ] **DoR-3**: Đã có starter repo tích hợp sẵn ESLint strict và Vitest để học viên thực hành.
- [ ] **DoR-4**: Không chứa bất kỳ dòng code mẫu nào sử dụng `any` hoặc React Class Component.
- [ ] **DoR-5**: Có câu hỏi phản biện Micro-quiz về sự khác biệt giữa SSR, SSG và RSC.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK GIÁM ĐỊNH LỘ TRÌNH (CURRICULUM TROUBLESHOOTING RUNBOOK)

Khi phát hiện bài giảng chứa kiến thức lỗi thời hoặc code mẫu vi phạm quy chuẩn kiểu:
1. **Phát hiện (Detection)**: Sinh viên hoặc Agent Audit phát hiện code mẫu dùng kiểu `any` hoặc thư viện deprecated.
2. **Đình chỉ module (Quarantine)**: Gắn nhãn `⚠️ DEPRECATED SYNTAX DETECTED` tại `STATUS.md`.
3. **Cập nhật chuẩn mực**: Viết lại bằng Modern TypeScript Type Narrowing hoặc Server Components.
4. **Kiểm tra biên dịch**: Chạy `tsc --noEmit` để chứng minh 0 lỗi kiểu phát sinh.
