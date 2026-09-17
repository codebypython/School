# 📜 ĐIỀU LỆ PHÒNG KIỂM SOÁT LỖI HYDRATION & HIỆU NĂNG WEB (TROUBLESHOOTING & TOOLKITS DEPT)
## Phòng 05 — Công Ty Công Nghệ Web Full-Stack & Hệ Sinh Thái JS/TS (CORP-10-WEB)

> **Mã Phòng Ban:** `WEB-DEPT-05`  
> **Trưởng phòng phụ trách:** Agent `SMS-02` (Syllabus Sentinel & Technical Auditor)  
> **Thẩm quyền kỹ thuật:** Chẩn đoán lỗi Next.js Hydration Mismatch, Khử trừ Infinite Re-renders, Profiling Event Loop & Memory Leaks  
> **Bộ công cụ cốt lõi:** Chrome DevTools Memory & Performance / React Developer Tools / Clinic.js (Node.js Profiler)

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kiểm Soát Sự Cố Web là **"Trung tâm Chẩn đoán và Tối ưu hóa Ứng dụng Web"**:
1. **Khắc Phục Lỗi Hydration Mismatch Trong Next.js**: Xử lý triệt để hiện tượng cây DOM render trên Server khác với cây DOM render lần đầu trên Trình duyệt.
2. **Triệt Tiêu Vòng Lặp Re-render Vô Tận (Infinite Render Loops)**: Sử dụng React Profiler để phát hiện các `useEffect` phụ thuộc sai hoặc State mutations kích hoạt re-render liên tục.
3. **Chẩn Đoán Nghẽn Luồng Node.js (Event Loop Starvation)**: Sử dụng Clinic.js Doctor để phát hiện các tác vụ CPU-bound chặn đứng khả năng tiếp nhận I/O của server.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN (DEBUGGING INVARIANTS)

1. **Nguyên Tắc Dựa Trên Profiling Thực Tế**:
   - Nghiêm cấm tối ưu hóa vội vã (Premature Optimization) bằng cách bọc toàn bộ component trong `useMemo`/`useCallback` khi chưa có số liệu từ React Profiler.
2. **Nguyên Tắc Không Tắt Linter Cẩu Thả**:
   - Nghiêm cấm dùng `// eslint-disable-next-line react-hooks/exhaustive-deps` để che giấu dependency bị thiếu. Bắt buộc phải tổ chức lại state logic.
3. **Nguyên Tắc Tách Biệt Môi Trường Thực Thi**:
   - Tuyệt đối không giả định môi trường Server có chứa các đối tượng toàn cục của Trình duyệt (`window`, `navigator`, `document`).

---

## 🛠️ 3. TOOLCHAIN & SKILLS ROUTE CHẨN ĐOÁN FULL-STACK

| Sự Cố / Nhu Cầu | Công Cụ Chuyên Dụng | Cú Pháp / Cách Kích Hoạt |
| :--- | :--- | :--- |
| **Hydration Mismatch & DOM Diff** | Chrome DevTools Console & React DevTools | Kiểm tra warning đỏ và tab Components |
| **Lãng phí Render (Wasted Renders)** | React Scan / Why Did You Render | `import '@scan/react'` trong môi trường dev |
| **Rò rỉ bộ nhớ Node.js Backend** | Chrome Inspect / Clinic.js Heap | `node --inspect index.js` |
| **Nghẽn Event Loop Server** | Clinic.js Doctor | `npx clinic doctor -- on node server.js` |

---

## 📁 4. CẤU TRÚC TÀI SẢN NỘI BỘ PHÒNG BAN

```
05_Troubleshooting_and_Toolkits/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 diagnostic_scripts/                   # Kịch bản chẩn đoán tự động
│   ├── check_bundle_size.sh                # Kiểm tra dung lượng JavaScript bundle
│   └── audit_react_dependencies.js         # Phân tích dependencies rác
└── 📁 runbooks/                             # Cẩm nang xử lý sự cố chi tiết
    ├── hydration_mismatch_runbook.md
    └── infinite_rerender_fix_guide.md
```

---

## 💻 5. MẪU KHUNG CODE CHẨN ĐOÁN & PROFILING (BOILERPLATE TOOLKIT)

```typescript
// Component bọc chẩn đoán: Tự động đo thời gian render của component con
import React, { Profiler, ProfilerOnRenderCallback } from 'react';

const onRenderCallback: ProfilerOnRenderCallback = (
  id,
  phase,
  actualDuration,
  baseDuration,
  startTime,
  commitTime,
) => {
  if (actualDuration > 16.67) {
    // Vượt quá 1 khung hình (60 FPS threshold)
    console.warn(
      `[PERF ALERT] Component <${id}> render chậm (${phase}): ${actualDuration.toFixed(2)}ms (Khung hình bị rớt!)`,
    );
  }
};

export const MonitoredView: React.FC<{
  id: string;
  children: React.ReactNode;
}> = ({ id, children }) => (
  <Profiler id={id} onRender={onRenderCallback}>
    {children}
  </Profiler>
);
```

---

## 🛡️ 6. TIÊU CHÍ NGHIỆM THU CHẨN ĐOÁN (DEFINITION OF DONE - DoD)

- [ ] **DoD-1**: Không còn lỗi Hydration Mismatch hoặc Warning xuất hiện trong Chrome Console.
- [ ] **DoD-2**: Không có re-render thừa (Wasted Renders) đối với các component tĩnh.
- [ ] **DoD-3**: Điểm Google Lighthouse Performance trên mobile đạt tối thiểu 90 điểm.
- [ ] **DoD-4**: Server Node.js không có hiện tượng tăng trưởng bộ nhớ tuyến tính không thu hồi được.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & CẨM NANG KHẮC PHỤC (TOP 4 WEB RUNBOOKS)

### 🚨 RUNBOOK 1: XỬ LÝ LỖI HYDRATION MISMATCH TRONG NEXT.JS APP ROUTER
* **Triệu chứng**: Console trình duyệt báo lỗi: `Error: Hydration failed because the initial UI does not match what was rendered on the server`.
* **Nguyên nhân phổ biến**:
  1. Render thời gian/ngày tháng (`new Date().toLocaleTimeString()`) khiến Server và Client sinh 2 giá trị khác nhau.
  2. Truy cập `localStorage` hoặc `window.innerWidth` trực tiếp trong quá trình render.
* **Quy trình khắc phục chuẩn mực**:
  - Trì hoãn việc render sang Client sau khi component đã mount bằng `useEffect`:
    ```tsx
    'use client';
    import { useState, useEffect } from 'react';

    export function ClientOnlyTime() {
      const [mounted, setMounted] = useState(false);
      useEffect(() => setMounted(true), []);
      if (!mounted) return null;
      return <span>{new Date().toLocaleTimeString()}</span>;
    }
    ```

---

### 🚨 RUNBOOK 2: CẤP CỨU VÒNG LẶP RE-RENDER VÔ TẬN TRONG REACT
* **Triệu chứng**: `Error: Maximum update depth exceeded. This can happen when a component repeatedly calls setState inside componentWillUpdate or componentDidUpdate`.
* **Khắc phục**:
  1. Không bao giờ gọi hàm cập nhật state trực tiếp trong thân component (`setCount(count + 1)` mà không bọc trong sự kiện).
  2. Nếu dùng object trong dependency array của `useEffect`, phải memoize bằng `useMemo` hoặc so sánh từng thuộc tính nguyên thủy.

---

### 🚨 RUNBOOK 3: KHẮC PHỤC BUNDLE SIZE QUÁ LỚN GÂY CHẬM FCP
* **Triệu chứng**: First Contentful Paint (FCP) chậm > 3s trên mạng 4G.
* **Khắc phục**:
  1. Dùng `@next/bundle-analyzer` để soi các thư viện cồng kềnh (Lodash, Moment.js).
  2. Thay thế `moment` bằng `date-fns` hoặc Native `Intl`.
  3. Áp dụng Dynamic Import: `const HeavyComponent = dynamic(() => import('./HeavyComponent'), { ssr: false })`.

---

### 🚨 RUNBOOK 4: XỬ LÝ LỖI CORS KHI KẾT NỐI FRONTEND - BACKEND
* **Triệu chứng**: `Access to fetch at 'http://api...' from origin 'http://localhost:3000' has been blocked by CORS policy`.
* **Khắc phục**:
  1. Trong NestJS: Cấu hình `app.enableCors({ origin: 'http://localhost:3000', credentials: true })`.
  2. Trong Next.js: Sử dụng Next.js Rewrites trong `next.config.js` để proxy các request qua cùng domain.
