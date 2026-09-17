# 📜 ĐIỀU LỆ PHÒNG KỸ THUẬT, FULL-STACK APPS & APIS (ENGINEERING LABS & CODE DEPT)
## Phòng 03 — Công Ty Công Nghệ Web Full-Stack & Hệ Sinh Thái JS/TS (CORP-10-WEB)

> **Mã Phòng Ban:** `WEB-DEPT-03`  
> **Trưởng phòng phụ trách:** Kỹ Sư Trưởng Thực Thi (`HM-00`) & Giám Sát Kỹ Thuật (`SMS-02`)  
> **Cố vấn chuyên môn:** DUT WebScale Full-Stack Mentor (`AGENT_PROFILE.md`)  
> **Tiêu chuẩn chất lượng:** Strict TypeScript v5+ / Next.js 15 App Router (RSC) / NestJS Enterprise / Zero 'any'

---

## 🎯 1. CHỨC NĂNG, NHIỆM VỤ & VAI TRÒ TÁC NGHIỆP

Phòng Kỹ Thuật & Full-Stack Apps là **trung tâm phát triển ứng dụng web quy mô lớn**:
1. **Làm Chủ TypeScript Chuyên Sâu**: Xây dựng các hệ thống kiểm soát kiểu tĩnh nghiêm ngặt, tự động suy luận kiểu cho cả Frontend và Backend (End-to-End Type Safety).
2. **Phát Triển Giao Diện Hiện Đại Với Next.js 15**: Xây dựng kiến trúc React Server Components (RSC), tối ưu hóa SEO, Streaming SSR và quản lý trạng thái bằng Zustand.
3. **Phát Triển Backend Doanh Nghiệp Với NestJS**: Thiết kế hệ thống API theo mô hình phân lớp Modular Architecture (Controller - Service - Repository), tích hợp Prisma ORM và PostgreSQL.

---

## ⚖️ 2. BỘ QUY TẮC BẤT BIẾN & HARD CONSTRAINTS (AGENT BẮT BUỘC TUÂN THỦ)

1. **Quy Tắc TypeScript Strict Bất Biến**:
   - **CẤM TUYỆT ĐỐI**: Sử dụng kiểu `any` trong mã nguồn. Nếu kiểu dữ liệu chưa xác định rõ ràng, bắt buộc dùng `unknown` kết hợp Type Narrowing hoặc Type Guards.
   - Bắt buộc cấu hình: `"strict": true`, `"noImplicitAny": true`, `"strictNullChecks": true` trong `tsconfig.json`.
2. **Quy Tắc React Server Components (Next.js 15)**:
   - Mọi Component mặc định là **Server Component**.
   - Chỉ thêm chỉ thị `'use client'` ở phần lá thấp nhất của cây Component khi có tương tác người dùng (sử dụng State `useState`, Hooks `useEffect`, hoặc sự kiện `onClick`).
   - **CẤM TUYỆT ĐỐI**: Truy cập API trình duyệt (`window`, `localStorage`, `document`) trong quá trình render Server Component để tránh lỗi **Hydration Mismatch**.
3. **Quy Tắc Non-blocking I/O Trong Node.js**:
   - **CẤM TUYỆT ĐỐI**: Chạy các tác vụ CPU nặng đồng bộ (như hash mật khẩu vòng lặp triệu lần bằng hàm sync) bên trong luồng chính của Express/NestJS làm nghẽn Event Loop.

---

## 🛠️ 3. SKILLS ROUTE & TOOLCHAIN ĐIỀU HÀNH CHUẨN

```bash
# 1. Cài đặt toàn bộ dependencies đồng nhất qua pnpm
pnpm install --frozen-lockfile

# 2. Kiểm tra lỗi kiểu tĩnh TypeScript toàn dự án (không sinh file js)
pnpm tsc --noEmit

# 3. Chạy Linter và Formatter tự động sửa lỗi
pnpm eslint . --fix
pnpm prettier --write .

# 4. Chạy bộ kiểm thử đơn vị với Vitest
pnpm vitest run --coverage

# 5. Chạy kiểm thử luồng người dùng E2E với Playwright
pnpm playwright test
```

---

## 📁 4. CẤU TRÚC THƯ MỤC VÀ TÀI SẢN NỘI BỘ QUY CHUẨN

```
03_Engineering_Labs_and_Code/
├── 📄 DEPARTMENT_CHARTER.md                 # Bản điều lệ này
├── 📁 fullstack_template/                   # Khung mẫu Next.js 15 + NestJS Monorepo
│   ├── apps/
│   │   ├── web/                             # Next.js 15 App Router Frontend
│   │   └── api/                             # NestJS 10 Enterprise API
│   └── packages/
│       ├── types/                           # Shared DTOs & Schemas
│       └── ui/                              # Shared Tailwind / UI Components
├── 📁 labs/                                 # 15 Bài Lab phân kỳ theo tuần
│   ├── Week01_Event_Loop_Closures/
│   ├── Week04_TypeScript_Generics/
│   ├── Week08_Nextjs_App_Router_RSC/
│   └── Week15_Capstone_Ecommerce_Fullstack/
└── 📁 tests/                                # E2E Playwright test harness
    └── e2e/
```

---

## 💻 5. MẪU KHUNG CODE / TEMPLATE CHUẨN NGHIỆP VỤ (GOLD MASTER NESTJS & TYPESCRIPT)

```typescript
import {
  Controller,
  Get,
  Param,
  ParseUUIDPipe,
  NotFoundException,
  UseGuards,
} from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse } from '@nestjs/swagger';
import { UsersService } from './users.service';
import { UserResponseDto } from './dto/user-response.dto';
import { JwtAuthGuard } from '../auth/guards/jwt-auth.guard';

@ApiTags('Users')
@Controller('api/v1/users')
@UseGuards(JwtAuthGuard)
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get(':id')
  @ApiOperation({ summary: 'Lấy thông tin người dùng theo UUID' })
  @ApiResponse({ status: 200, type: UserResponseDto })
  async getUserById(
    @Param('id', new ParseUUIDPipe({ version: '4' })) id: string,
  ): Promise<UserResponseDto> {
    const user = await this.usersService.findById(id);
    if (!user) {
      throw new NotFoundException(
        `Người dùng với mã định danh '${id}' không tồn tại.`,
      );
    }
    return user;
  }
}
```

---

## 🛡️ 6. BỘ TIÊU CHÍ NGHIỆM THU CHẤT LƯỢNG (DEFINITION OF DONE - DoD)

- [ ] **DoD-1 (Zero 'any')**: Toàn bộ codebase không chứa từ khóa `any`, vượt qua `pnpm tsc --noEmit` với 0 lỗi.
- [ ] **DoD-2 (Zero Hydration Mismatch)**: Giao diện Next.js render trên server và client hoàn toàn đồng nhất.
- [ ] **DoD-3 (Coverage $\ge 85\%$)**: Bộ test Vitest đạt độ bao phủ tối thiểu 85% trên các service nghiệp vụ cốt lõi.
- [ ] **DoD-4 (E2E Test Pass)**: Luồng nghiệp vụ chính (Đăng nhập, Thanh toán) pass 100% kịch bản Playwright.

---

## 🚨 7. QUY TRÌNH XỬ LÝ SỰ CỐ & RUNBOOK KHẮC PHỤC LỖI WEB FULL-STACK (FULL-STACK TROUBLESHOOTING RUNBOOK)

Khi xảy ra lỗi sập ứng dụng Web hoặc nghẽn hiệu năng:
1. **Khắc Phục Lỗi Hydration Mismatch**:
   - Dấu hiệu: Báo lỗi `Text content did not match. Server: "..." Client: "..."`.
   - Xử lý: Tách biệt logic đọc thời gian hoặc `localStorage` vào `useEffect`; dùng `dynamic(() => import(...), { ssr: false })` cho các component chỉ dùng trên client.
2. **Khắc Phục Lỗi Vòng Lặp Re-render Vô Tận (Infinite Loop)**:
   - Dấu hiệu: `Maximum update depth exceeded`.
   - Xử lý: Kiểm tra các object/array mới được tạo trực tiếp trong dependency array của `useEffect`; bọc hàm bằng `useCallback` hoặc giá trị bằng `useMemo`.
3. **Cứu Hộ Memory Leak Trên Node.js Server**:
   - Dấu hiệu: Heap memory tăng liên tục trên container production.
   - Xử lý: Sử dụng công cụ `node --inspect` và Chrome DevTools Memory Heap Snapshot để tìm con trỏ closure hoặc event listener chưa hủy.
