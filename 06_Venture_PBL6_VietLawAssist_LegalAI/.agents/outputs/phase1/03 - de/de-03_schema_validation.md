# 📖 Báo Cáo Data Schema & Quy Trình Kiểm Thử Dữ Liệu — Agent DE-03

> **Task ID:** D6  
> **Loại output:** 📖 Báo cáo Kỹ thuật + Checklist Validation  
> **Ngày tạo:** 2026-09-09  
> **Dùng cho:** Chương 4.2 Báo cáo đồ án + Tiêu chuẩn dữ liệu dự án VietLawAssist

---

## 1. Thiết Kế Cơ Sở Dữ Liệu SQLite: Bảng `law_articles`

Cơ sở dữ liệu SQLite cục bộ được chọn nhằm đáp ứng tiêu chí gọn nhẹ, phi máy chủ (serverless), tốc độ truy xuất cực nhanh và không phát sinh chi phí hạ tầng.

### 1.1 Chi tiết Lược đồ Bảng (DDL)

```sql
CREATE TABLE IF NOT EXISTS law_articles (
    article_id TEXT PRIMARY KEY,
    law_code TEXT NOT NULL,
    law_name TEXT NOT NULL,
    chapter TEXT DEFAULT '',
    section TEXT DEFAULT '',
    article_number INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    full_text TEXT NOT NULL,
    effective_date TEXT DEFAULT '',
    source_url TEXT DEFAULT '',
    word_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Chỉ mục tối ưu hóa tốc độ lọc và tìm kiếm theo luật
CREATE INDEX IF NOT EXISTS idx_law_articles_law_code ON law_articles(law_code);
CREATE INDEX IF NOT EXISTS idx_law_articles_article_number ON law_articles(article_number);
```

### 1.2 Bảng Đặc Tả Chi Tiết Từng Thuộc Tính

| Tên Cột | Kiểu Dữ Liệu | Ràng buộc | Mục đích & Ví dụ giá trị |
|---|---|---|---|
| `article_id` | `TEXT` | `PRIMARY KEY` | Định danh duy nhất toàn hệ thống. Cú pháp: `{law_code}_D{number}`. VD: `HP2013_D20`. |
| `law_code` | `TEXT` | `NOT NULL` | Mã viết tắt bộ luật: `HP2013`, `BLDS2015`, `BLHS2015`, `LHNGD2014`, `LLD2019`. |
| `law_name` | `TEXT` | `NOT NULL` | Tên đầy đủ: `Hiến pháp nước Cộng hòa xã hội chủ nghĩa Việt Nam năm 2013`. |
| `chapter` | `TEXT` | Mặc định rỗng `''` | Tên Chương chứa điều luật. VD: `Chương II: Quyền con người...`. |
| `section` | `TEXT` | Mặc định rỗng `''` | Tên Mục con (nếu bộ luật có phân cấp Mục). |
| `article_number`| `INTEGER`| `NOT NULL`, $\ge 1$ | Số thứ tự số học của điều luật, phục vụ sắp xếp tự nhiên (`ORDER BY article_number`). |
| `title` | `TEXT` | `NOT NULL` | Tiêu đề điều: `Điều 20. Quyền bất khả xâm phạm về thân thể`. |
| `content` | `TEXT` | `NOT NULL` | Phần thân nội dung của điều luật (gồm các khoản 1, 2, 3...). |
| `full_text` | `TEXT` | `NOT NULL` | Toàn văn kết hợp: `title + "\n" + content`. Đây là trường đưa vào tokenize và BM25 indexing. |
| `effective_date`| `TEXT` | `YYYY-MM-DD` | Ngày bắt đầu áp dụng trên thực tế (VD: `2014-01-01`). |
| `source_url` | `TEXT` | Mặc định rỗng `''` | Đường dẫn gốc chứng minh tính minh bạch của dữ liệu. |
| `word_count` | `INTEGER`| $\ge 0$ | Tổng số từ trong `full_text`, dùng phân tích độ dài tài liệu ($|D|$ trong BM25). |
| `created_at` | `TIMESTAMP` | Auto now | Thời điểm ghi nhận vào cơ sở dữ liệu. |
| `updated_at` | `TIMESTAMP` | Auto now | Thời điểm cập nhật dữ liệu lần cuối. |

---

## 2. Checklist Kiểm Định Dữ Liệu (Data Validation Checklist)

Trước khi dữ liệu thô được nạp (ingest) vào cơ sở dữ liệu và chỉ mục tìm kiếm, pipeline tiền xử lý bắt buộc phải vượt qua bộ 7 tiêu chí kiểm định nghiêm ngặt:

- [ ] **Check 1: Tính duy nhất của Khóa chính (Primary Key Uniqueness)**
  - Không có 2 bản ghi nào trùng `article_id`.
  - Khóa chính phải khớp với quy tắc Regex: `^(HP2013|BLDS2015|BLHS2015|LHNGD2014|LLD2019)_D\d+$`.
- [ ] **Check 2: Chuẩn hóa Bảng mã Tiếng Việt (Unicode Normalization)**
  - Tất cả chuỗi ký tự phải được chuẩn hóa về định dạng **NFC** (`unicodedata.normalize('NFC', text)`).
  - Không tồn tại ký tự Unicode tổ hợp NFD, không còn byte lỗi utf-8 hoặc ký tự điều khiển ẩn.
- [ ] **Check 3: Toàn vẹn Nội dung (Content Completeness)**
  - Cột `content` và `full_text` không được rỗng hoặc chỉ chứa khoảng trắng trắng (`len(content.strip()) > 0`).
  - `word_count` phải lớn hơn 5 từ (loại bỏ các điều luật bị lỗi parse mất nội dung).
- [ ] **Check 4: Tính nhất quán của Số thứ tự Điều (Article Continuity)**
  - Số thứ tự `article_number` phải là số nguyên dương liên tục từ $1$ đến $N$ đối với từng bộ luật (trừ những điều đã bị bãi bỏ chính thức theo luật sửa đổi bổ sung).
- [ ] **Check 5: Khớp nối Tiêu đề và Thân văn bản (Title-Content Consistency)**
  - `title` phải bắt đầu bằng chữ "Điều {article_number}".
  - `full_text` phải bằng chính xác f"{title}\n{content}".
- [ ] **Check 6: Định dạng Thời gian & URLs**
  - `effective_date` tuân thủ ISO 8601 (`YYYY-MM-DD`).
  - `source_url` bắt đầu bằng `http://` hoặc `https://`.
- [ ] **Check 7: Pydantic Schema Validation**
  - Mọi bản ghi thô nạp từ file JSON phải khởi tạo thành công qua class `LawArticleCreate` mà không ném ra ngoại lệ `ValidationError`.

---

## 3. Chính Sách Quản Trị & Cập Nhật Dữ Liệu (Data Governance & Maintenance)

1. **Xử lý Văn bản Hợp nhất & Sửa đổi:**
   - Đối với các bộ luật có sửa đổi bổ sung (như Bộ luật Hình sự 2015 được sửa đổi năm 2017 bởi Luật số 12/2017/QH14), VietLawAssist luôn sử dụng **Văn bản Hợp nhất** mới nhất có hiệu lực thi hành để đảm bảo tính thời sự và pháp lý.
2. **Nguyên tắc Bảo toàn Dữ liệu:**
   - Tuyệt đối không tự ý chỉnh sửa nội dung câu chữ pháp lý. Quá trình làm sạch văn bản chỉ xử lý dấu câu, định dạng khoảng trắng, ngắt dòng và mã hóa ký tự.
3. **Sao lưu & Tái lập (Data Backup & Reproducibility):**
   - Dữ liệu được lưu trữ kép:
     1. Tệp thô có cấu trúc dạng JSON (`Project/data/sample/sample_articles.json`).
     2. Tệp cơ sở dữ liệu thực thi SQLite (`Project/data/laws.db`).
   - Có thể xóa file `.db` và tái lập lại toàn bộ trong vòng dưới 3 giây bằng script khởi tạo.
