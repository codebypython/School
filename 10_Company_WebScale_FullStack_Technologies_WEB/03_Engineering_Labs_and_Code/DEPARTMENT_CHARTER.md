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

### 3.1 Bộ Lệnh CLI Tác Nghiệp Chuẩn

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

## 💻 4. MẪU KHUNG CODE / TEMPLATE CHUẨN NGHIỆP VỤ (GOLD MASTER NESTJS & TYPESCRIPT)

Mẫu chuẩn mực **NestJS Controller + DTO Validation** theo chuẩn doanh nghiệp:

```typescript
import { Controller, Post, Body, HttpCode, HttpStatus, UsePipes, ValidationPipe } from '@nestjs/common';
import { IsString, IsEmail, MinLength, IsNotEmpty } from 'class-validator';

// Data Transfer Object (DTO) với validation runtime tự động
export class CreateUserDto {
  @IsString({ message: 'Tên người dùng phải là chuỗi ký tự.' })
  @IsNotEmpty({ message: 'Tên người dùng không được để trống.' })
  readonly fullName!: string;

  @IsEmail({}, { message: 'Địa chỉ email không đúng định dạng.' })
  readonly email!: string;

  @IsString()
  @MinLength(8, { message: 'Mật khẩu phải có độ dài tối thiểu 8 ký tự.' })
  readonly password!: string;
}

// Interface định nghĩa phản hồi an toàn kiểu
export interface UserResponse {
  readonly id: string;
  readonly fullName: string;
  readonly email: string;
  readonly createdAt: Date;
}

@Controller('api/v1/users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Post()
  @HttpCode(HttpStatus.CREATED)
  @UsePipes(new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true, transform: true }))
  async createUser(@Body() createUserDto: CreateUserDto): Promise<UserResponse> {
    // Controller chỉ đón nhận request, validate và ủy quyền cho Service xử lý
    return await this.usersService.create(createUserDto);
  }
}
```

---

## 🛡️ 5. BỘ TIÊU CHÍ NGHIỆM THU CHẤT LƯỢNG (DEFINITION OF DONE - DoD)

- [ ] **DoD-1 (Zero Any)**: Không có bất kỳ cảnh báo `@typescript-eslint/no-explicit-any` nào.
- [ ] **DoD-2 (Zero Hydration Errors)**: Ứng dụng Next.js chạy ở chế độ Production không phát sinh lỗi Hydration trên trình duyệt.
- [ ] **DoD-3 (Lighthouse Audit $\ge 90$)**: Điểm Performance, Accessibility, Best Practices và SEO trên Chrome DevTools đạt từ 90 điểm trở lên.
- [ ] **DoD-4 (Test Suite Green)**: Toàn bộ Unit Tests và Integration Tests chạy qua Vitest đạt độ bao phủ $\ge 80\%$.
