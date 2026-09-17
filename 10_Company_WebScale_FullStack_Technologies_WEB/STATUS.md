# 📊 PROJECT STATUS DASHBOARD — WebScale Corp (CORP-10-WEB)

> **Cập nhật lần cuối**: 2026-09-18 | **Tuần hiện tại**: Tuần 1 (JavaScript Engine Deep Dive & Event Loop)  
> **Mentor chuyên trách**: DUT WebScale Full-Stack Mentor (`AGENT_PROFILE.md`)

---

## Current Phase: 🔵 PHASE 1 — JAVASCRIPT UNDER THE HOOD & TYPESCRIPT (Tuần 1-6)

Tập trung mổ xẻ cơ chế hoạt động của V8 Engine, Event Loop (Microtasks vs Macrotasks), Closures, Prototypes và làm chủ toàn diện hệ thống kiểu tĩnh nâng cao của TypeScript.

---

## Implementation & Lab Progress

### Module 1: Bản Chất Sâu Của JavaScript (YDKJSY)
- [x] Thiết lập môi trường Node.js 20 LTS, pnpm, TypeScript 5+
- [x] V8 Engine: Parser, Bytecode (Ignition), JIT Compiler (TurboFan)
- [ ] Execution Context, Lexical Scope, Hoisting, Closures & Memory Leaks
- [ ] Con trỏ `this`, Prototypal Inheritance vs ES6 Classes
- [ ] Event Loop: Phân biệt `Promise.then` (Microtask) vs `setTimeout` (Macrotask)

### Module 2: TypeScript Strict Mastery
- [ ] Type Inference, Structural Subtyping (Duck Typing)
- [ ] Generics, Generic Constraints (`extends keyof`)
- [ ] Advanced Types: Union/Intersection, Conditional Types (`T extends U ? X : Y`), Mapped Types
- [ ] Template Literal Types & Type Guards (`is`, `in`, `typeof`)

### Module 3: Modern React, Next.js & NestJS
- [ ] React Fiber, Reconciliation, Custom Hooks, Zustand State Management
- [ ] Next.js 15: Server Components vs Client Components, Server Actions
- [ ] NestJS Enterprise: Modules, Controllers, Providers, Guards, Interceptors, Prisma ORM

---

## Known Issues & Blockers

| # | Vấn đề | Mức độ | Ghi chú |
|:-:|:---|:---:|:---|
| 1 | Sinh viên lạm dụng kiểu `any` trong TypeScript | 🔴 High | Bật cờ `noImplicitAny: true` và `strict: true` trong `tsconfig.json` |

---

## Next Priority (P0)
- Thiết lập starter repo bài tập Event Loop Simulator và TypeScript Advanced Types Challenge trong `03_Engineering_Labs_and_Code/`.
