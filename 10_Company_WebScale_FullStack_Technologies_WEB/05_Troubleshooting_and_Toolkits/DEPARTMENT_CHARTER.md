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

## 🚑 2. CẨM NANG XỬ LÝ SỰ CỐ WEB THỰC CHIẾN (TOP 4 WEB RUNBOOKS)

---

### 🚨 RUNBOOK 1: XỬ LÝ LỖI HYDRATION MISMATCH TRONG NEXT.JS APP ROUTER
* **Triệu chứng**: Console trình duyệt báo lỗi đỏ: `Error: Hydration failed because the initial UI does not match what was rendered on the server`.
* **Nguyên nhân phổ biến**:
  1. Render thời gian/ngày tháng (`new Date().toLocaleTimeString()`) hoặc số ngẫu nhiên (`Math.random()`) khiến Server và Client sinh 2 giá trị khác nhau.
  2. Truy cập `localStorage` hoặc `window.innerWidth` trực tiếp trong quá trình render.
  3. Thẻ HTML lồng nhau bất hợp lệ (Ví dụ: `<p>` chứa thẻ `<div>` bên trong).
* **Quy trình khắc phục chuẩn mực**:
  - Đối với dữ liệu chỉ có ở Client: Trì hoãn việc render sang Client sau khi component đã mount bằng `useEffect`:
    ```tsx
    'use client';
    import { useState, useEffect } from 'react';

    export function ClientOnlyTime() {
      const [mounted, setMounted] = useState(false);
      useEffect(() => setMounted(true), []);
      if (!mounted) return null; // Hoặc render skeleton placeholder trên server
      return <span>{new Date().toLocaleTimeString()}</span>;
    }
    ```

---

### 🚨 RUNBOOK 2: PHÁT HIỆN VÀ KHẮC PHỤC RÒ RỈ BỘ NHỚ TRÌNH DUYỆT (HEAP SNAPSHOT)
* **Triệu chứng**: Tab trình duyệt chạy một lúc ngốn hàng Gigabytes RAM và bị crash (Out of Memory).
* **Quy trình cô lập qua Chrome DevTools**:
  1. Mở DevTools $\rightarrow$ Chọn tab **Memory**.
  2. Chụp **Heap Snapshot 1** $\rightarrow$ Thực hiện thao tác người dùng (ví dụ: mở modal rồi đóng 10 lần) $\rightarrow$ Chụp **Heap Snapshot 2**.
  3. Chọn góc nhìn so sánh (**Comparison View**): Lọc các đối tượng `Detached HTMLElement` hoặc `Closure Listeners` không được giải phóng.
  4. Khắc phục bằng cách thêm hàm dọn dẹp (Cleanup Function) trong `useEffect`:
     ```tsx
     useEffect(() => {
       const handler = () => console.log('resize');
       window.addEventListener('resize', handler);
       return () => window.removeEventListener('resize', handler); // Bắt buộc cleanup!
     }, []);
     ```

---

### 🚨 RUNBOOK 3: CHẨN ĐOÁN CHẶN LUỒNG EVENT LOOP TRONG NESTJS VỚI CLINIC.JS
* **Triệu chứng**: Server NestJS có độ trễ p99 tăng vọt lên vài giây dù CPU chỉ sử dụng 30%.
* **Quy trình chẩn đoán**:
  ```bash
  # Chạy ứng dụng dưới sự giám sát của Clinic Doctor
  npx clinic doctor --on-port 'autocannon http://localhost:3000/api/heavy-task' -- node dist/main.js
  ```
* **Báo cáo Clinic Doctor**:
  - Nếu đồ thị báo `Event Loop Delay` cao vọt, tìm ngay các đoạn mã dùng `fs.readFileSync`, `crypto.pbkdf2Sync` hoặc vòng lặp JSON parsing file lớn đồng bộ để chuyển sang luồng Worker Threads hoặc bất đồng bộ.

---

### 🚨 RUNBOOK 4: XỬ LÝ LỖI CORS (CROSS-ORIGIN RESOURCE SHARING)
* **Triệu chứng**: Frontend gọi API backend bị chặn với lỗi: `No 'Access-Control-Allow-Origin' header is present on the requested resource`.
* **Khắc phục trong NestJS**: Cấu hình CORS chặt chẽ ở `main.ts`:
  ```typescript
  app.enableCors({
    origin: process.env.ALLOWED_ORIGINS?.split(',') || ['http://localhost:3000'],
    methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
    credentials: true,
  });
  ```
