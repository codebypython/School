# 🤝 Contributing to School Holdings

> **Hệ sinh thái:** School Holdings — Academic & Engineering Enterprise (DUT Semester 7)  
> **Tiêu chuẩn chất lượng:** MQAVP-2026 | Ngưỡng pass: ≥ 60% / Chuẩn công nghiệp: ≥ 75%

---

## 📋 Quy Trình Đóng Góp Chuẩn

### 1. Clone & Setup

```bash
git clone https://github.com/codebypython/School.git
cd School
```

### 2. Quy Tắc Commit Message

Dùng [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(corp-07-algo): add Week02 RAII lab implementation
fix(links): correct broken file:/// paths in NOTION_INTEGRATION_MASTER_SPEC
docs(vault): add concurrency sources to EXTERNAL_KNOWLEDGE_VAULT
refactor(auditor): improve link pattern regex
test(algo): add test_linked_list.cpp with Catch2
```

**Prefix bắt buộc:** `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

### 3. Tiêu Chuẩn Trước Khi Commit

Chạy kiểm định Level-1 và đảm bảo **0 broken links**:

```powershell
python scripts/holding_system_auditor.py --save
```

### 4. Chuẩn Mực Tài Liệu (Markdown)

- Mọi `DEPARTMENT_CHARTER.md` phải có đủ 7 tầng
- Mọi link nội bộ dùng `file:///d:/User/7th/School/...` (absolute) hoặc relative path đúng
- Không có file rác: `.DS_Store`, `Thumbs.db`, `.tmp`

### 5. Chuẩn Mực Mã Nguồn C++

- Bắt buộc biên dịch với `-Wall -Wextra -Werror -std=c++20`
- 0 memory leaks qua AddressSanitizer (`-fsanitize=address,undefined`)
- Tuyệt đối không dùng `malloc/free`, raw `new/delete`, `using namespace std`

### 6. Chuẩn Mực Mã Nguồn Python

- Type hints đầy đủ, mypy strict pass
- Không có blocking call trong `async def` functions
- Docstrings cho mọi public function/class

---

## 🚫 Những Điều Không Được Làm

- ❌ Commit thẳng lên `main` khi có broken links
- ❌ Sử dụng `any` trong TypeScript hoặc `# type: ignore` không có giải trình
- ❌ Đưa mã nguồn không compile được vào repo
- ❌ Thêm data files lớn (`.pkl`, `.h5`, `.pth`) — dùng Git LFS nếu cần

---

## 📞 Liên Hệ

- **Repo:** [github.com/codebypython/School](https://github.com/codebypython/School)
- **Hệ thống kiểm định:** [`scripts/holding_system_auditor.py`](scripts/holding_system_auditor.py)
