# 📜 ĐIỀU LỆ PHÒNG TƯ LIỆU & RFC WEB STANDARDS (LECTURES & RAW MATERIALS DEPT)
## Phòng 02 — Công Ty Công Nghệ Web Full-Stack & Hệ Sinh Thái JS/TS (CORP-10-WEB)

> **Mã Phòng Ban:** `WEB-DEPT-02`  
> **Trưởng phòng phụ trách:** Agent `EKC-03` (Knowledge Curator & Quality Sentinel)  
> **Tiêu chuẩn học liệu:** ER-QVR $\ge 90/100$ | W3C / TC39 ECMAScript / React RFCs / Next.js Architecture

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Tư Liệu là **thư viện chuẩn mực công nghệ Web và tài liệu nền tảng JavaScript**:
1. **Lưu Trữ Đặc Tả Ngôn Ngữ & Proposals (TC39 ECMAScript)**: Phân tích các tiêu chuẩn ECMAScript mới nhất, cú pháp hiện đại và lộ trình tính năng của JavaScript/TypeScript.
2. **Kho Giải Phẫu V8 Engine & Browser Internals**: Lưu trữ sơ đồ kiến trúc V8 (Ignition Interpreter, TurboFan Compiler, Hidden Classes, Inline Caching).
3. **Phân Tích Chuyên Sâu Các RFC Khung Kiến Trúc**: Lưu trữ tài liệu thiết kế gốc của React Server Components (RSC), cơ chế Hydration và hệ thống Caching đa tầng trong Next.js 15.

---

## ⚖️ 2. BỘ QUY TẮC BẢO TỒN TƯ LIỆU BẤT BIẾN (CURATION INVARIANTS)

1. **Chuẩn Mực Nguồn Cung Cấp (Source Provenance)**:
   - Mọi tư liệu kỹ thuật phải đối chiếu với tài liệu gốc của MDN Web Docs, W3C, TC39, hoặc sách Tier A+ trong Knowledge Vault.
2. **Quy Tắc Lọc Bỏ Cú Pháp Đồ Đá (Anti-Legacy Invariant)**:
   - Nghiêm cấm đưa vào tư liệu các cú pháp đã lỗi thời như `var`, Callback Hell, `XMLHttpRequest` trần trụi hoặc `document.write`.
3. **Quy Tắc Trực Quan Hóa Vòng Đời Trình Duyệt**:
   - Mọi bài học về DOM và Render Pipeline phải có sơ đồ mô tả DOM Tree, CSSOM, Render Tree, Layout, Paint và Composite.

---

## 🛠️ 3. TOOLCHAIN & QUY TRÌNH SỐ HÓA BÀI GIẢNG

1. **Vẽ Sơ Đồ Kiến Trúc**: Mermaid.js, Excalidraw, SVG Diagrams.
2. **Phân Tích Performance Web**: Google Lighthouse CLI, Chrome DevTools Performance Trace.
3. **Định Dạng Markdown**: Prettier Formatter, AST Link Validator qua `holding_system_auditor.py`.

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
02_Lectures_and_Raw_Materials/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 v8_internals/                         # Tài liệu giải phẫu V8 Engine
│   ├── event_loop_and_microtasks.md        # Bản chất Event Loop và Microtask Queue
│   └── hidden_classes_and_inline_cache.md  # Tối ưu hóa Object Shapes trong V8
├── 📁 react_architecture/                   # Phân tích kiến trúc React 19 & RSC
│   ├── fiber_reconciliation_engine.md      # Cơ chế lập lịch Fiber Architecture
│   └── server_actions_and_rsc_wire.md      # Giao thức RSC Wire Format
└── 📁 web_standards_rfc/                    # Các đặc tả giao thức mạng và web
    ├── http2_and_http3_quic_deepdive.md    # Phân tích giao thức HTTP/2 và HTTP/3
    └── web_security_csp_cors_csrf.md       # Cẩm nang an ninh Web hiện đại
```

---

## 💻 5. MẪU TƯ LIỆU CHỨNG MINH HỌC THUẬT (GOLD MASTER BROWSER INTERNALS)

```markdown
# 🔬 GIẢI PHẪU V8 ENGINE: TẠI SAO PHÉP GÁN ĐỘNG LÀM CHẬM JIT COMPILER?
> **Nguồn trích:** You Don't Know JS Yet & V8 Dev Blog  
> **Người thẩm định:** Agent `EKC-03` | **Điểm ER-QVR:** 96/100

### 1. Khái niệm Hidden Classes (Shapes)
Trong JavaScript, các object không có schema cố định. V8 giải quyết bằng cách tạo ngầm các Hidden Classes (C0, C1, C2...) liên kết theo cây chuyển đổi (Transition Tree).

### 2. Nguyên nhân Tụt Giảm Hiệu Năng (De-optimization)
Khi khởi tạo hai đối tượng nhưng gán thuộc tính theo thứ tự khác nhau:
```javascript
const obj1 = { a: 1, b: 2 }; // Hidden Class C1
const obj2 = { b: 2, a: 1 }; // Hidden Class C2 (Khác với C1!)
```
$\implies$ Gây hiện tượng Polymorphic hoặc Megamorphic Call Sites, khiến TurboFan Compiler hủy bỏ Inline Caching và rơi về chế độ thông dịch chậm hơn 10 lần!
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU TƯ LIỆU (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: Thông tin kỹ thuật khớp 100% với tài liệu chính thức của ECMAScript và MDN.
- [ ] **DoD-2**: Sơ đồ kiến trúc hiển thị rõ ràng, không bị lỗi cú pháp Mermaid.
- [ ] **DoD-3**: Có ví dụ code minh họa trước và sau khi tối ưu hóa hiệu năng V8.
- [ ] **DoD-4**: Đạt điểm kiểm định chất lượng ER-QVR $\ge 90/100$.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK KHẮC PHỤC SAI LỆCH KIẾN THỨC (CURATION TROUBLESHOOTING RUNBOOK)

Khi phát hiện tư liệu giải thích sai cơ chế Event Loop hoặc mô tả sai React Server Components:
1. **Cô lập tài liệu**: Gắn nhãn `⚠️ INACCURATE SPECIFICATION: Review against official React docs`.
2. **Đối chiếu mã nguồn**: Kiểm tra trực tiếp source code của React hoặc V8.
3. **Hiệu chỉnh & Bổ sung**: Sửa lại nội dung kèm trích dẫn pull request hoặc RFC chính thức.
4. **Xác nhận hoàn tất**: Đảm bảo học viên tiếp cận thông tin chính xác chuẩn quốc tế.
