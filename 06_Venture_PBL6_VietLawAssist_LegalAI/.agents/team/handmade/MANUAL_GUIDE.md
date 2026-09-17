# 📖 Sổ Tay Hướng Dẫn Thực Hành Thủ Công (Hands-on Manual Guide)

> **Dành cho:** Role **HANDMADE** (Bạn — Kỹ sư thực thi dự án)  
> **Biên soạn bởi:** Hội đồng AI Agents (PM-01, MLR-02, DE-03, SA-04, EVAL-05, RW-06)  
> **Mục tiêu:** Cung cấp hướng dẫn tuần tự từng bước chi tiết (step-by-step) để bạn tự tay thực hiện 3 nhiệm vụ cốt lõi:
> 1. **Thu thập dữ liệu pháp luật (Data Collection)**
> 2. **Chọn mô hình & Kiểm chứng lý thuyết (Model Selection)**
> 3. **Tiền xử lý dữ liệu cho mô hình (Data Preprocessing)**

---

# PHẦN I: THU THẬP DỮ LIỆU THỦ CÔNG (DATA COLLECTION)
*Biên soạn bởi: Kỹ sư Dữ liệu DE-03*

---

### Bước 1.1: Chuẩn Bị Thư Mục Lưu Trữ Dữ Liệu Thô (Raw Data)

Trong kỹ thuật dữ liệu, **nguyên tắc vàng** là dữ liệu thô tải về phải được lưu trữ riêng biệt, không được ghi đè, để luôn có thể tái lập (reproducibility).

Mở PowerShell tại thư mục dự án và chạy lệnh tạo thư mục:
```powershell
New-Item -ItemType Directory -Force -Path "Project\data\raw"
```
Thư mục `Project/data/raw/` này đã được cấu hình trong `.gitignore` để tránh đẩy các file HTML/PDF dung lượng lớn lên GitHub.

---

### Bước 1.2: Tải Về Văn Bản Gốc Của 3 Bộ Luật Trọng Tâm

Bạn có thể lựa chọn 1 trong 2 cách dưới đây:

#### Cách A: Tải Thủ Công Trực Tiếp Bằng Trình Duyệt Web (Khuyến Nghị Cho Lần Đầu)
1. **Hiến pháp 2013 (HP2013 - 120 điều):**
   - Mở trình duyệt, truy cập liên kết chính thức của Cổng Pháp điển Quốc gia:  
     `https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=32801`
   - Nhấn phím `Ctrl + S` trên trình duyệt.
   - Tại ô *Save as type*, chọn **Webpage, Complete** (hoặc **HTML Only**).
   - Đặt tên file là `HP2013.html` và lưu vào thư mục `Project/data/raw/`.
2. **Bộ luật Dân sự 2015 (BLDS2015 - 689 điều):**
   - Truy cập: `https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=96404`
   - Nhấn `Ctrl + S`, lưu với tên `BLDS2015.html` vào `Project/data/raw/`.
3. **Bộ luật Hình sự 2015 (BLHS2015 - 426 điều):**
   - Truy cập: `https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=96405`
   - Nhấn `Ctrl + S`, lưu với tên `BLHS2015.html` vào `Project/data/raw/`.

*(Nếu trang `vbpl.vn` bảo trì, bạn có thể tải bản PDF công báo chính phủ dự phòng từ: `https://datafiles.chinhphu.vn/cpp/files/vbpq/2013/12/hienphap2013.pdf`)*.

#### Cách B: Tải Bằng Lệnh Dòng Lệnh Qua Python (Bán Thủ Công)
Nếu muốn tải tự động nhanh nhưng vẫn kiểm soát từng file, mở PowerShell và chạy đoạn script Python 1 dòng sau:
```powershell
.\.venv\Scripts\python.exe -c "
import urllib.request
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request('https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=32801', headers=headers)
with urllib.request.urlopen(req) as resp, open('Project/data/raw/HP2013.html', 'wb') as f:
    f.write(resp.read())
print('[✓] Đã tải xong Hiến pháp 2013 vào Project/data/raw/HP2013.html')
"
```

---

### Bước 1.3: Kiểm Tra Tính Toàn Vẹn Của Dữ Liệu Thô (Sanity Check)

1. Mở file `Project/data/raw/HP2013.html` bằng trình duyệt hoặc VS Code.
2. Nhấn `Ctrl + F` và gõ `Điều 1.` $\rightarrow$ Kiểm tra xem có hiển thị: *"Điều 1. Nước Cộng hòa xã hội chủ nghĩa Việt Nam..."* không.
3. Nhấn `Ctrl + F` và gõ `Điều 120.` $\rightarrow$ Kiểm tra xem có điều luật cuối cùng của Hiến pháp không.
4. **Kiểm tra lỗi font:** Đảm bảo các chữ có dấu như `đ`, `ă`, `ơ`, `ư` hiển thị rõ ràng, không bị biến thành `&#1234;` hay `Ä iá» u`.

---

# PHẦN II: CHỌN MÔ HÌNH & KIỂM CHỨNG LÝ THUYẾT (MODEL SELECTION)
*Biên soạn bởi: Chuyên gia Nghiên cứu Học máy MLR-02*

---

### Bước 2.1: Hiểu Lý Do Tại Sao Chọn Mô Hình Theo Thang Đo 4 Tầng

Trước khi gõ code, bạn cần nắm chắc luận điểm cốt lõi để trả lời trước hội đồng phản biện:
- **Tại sao không dùng ngay LLM/ChatGPT cho tra cứu luật?**
  - *Lý do:* LLM thường xuyên bị hiện tượng "ảo giác" (hallucination) — bịa đặt số điều luật hoặc chế tài nếu không có dữ liệu gốc chính xác đối chiếu.
  - *Giải pháp:* Phải có tầng **Retrieval** (Trích xuất văn bản chuẩn) trước khi đưa vào LLM.
- **Tại sao Tầng 1 dùng BM25 mà không dùng Deep Learning ngay?**
  - *Lý do:* BM25 không cần GPU, tốc độ cực nhanh (<30ms), bắt chính xác 100% các từ khóa kỹ thuật (ví dụ: *"Điều 20 Hiến pháp"*, *"tội cố ý gây thương tích"*). Đây là mốc chuẩn (baseline) khoa học bắt buộc trong mọi nghiên cứu Information Retrieval.
- **Tại sao Tầng 2 cần Dense Retrieval (PhoBERT)?**
  - *Lý do:* Để giải quyết hạn chế "bất đồng từ khóa" (Vocabulary Mismatch) của BM25 khi người dùng đặt câu hỏi bằng ngôn ngữ đời thường (ví dụ: hỏi *"bao nhiêu tuổi được lấy vợ?"* thì BM25 khó tìm ra điều luật ghi là *"độ tuổi kết hôn của nam là từ đủ 20 tuổi"*).

---

### Bước 2.2: Thao Tác Thủ Công — Thử Nghiệm Tokenizer Tiếng Việt (PyVi vs Underthesea)

Mở PowerShell và khởi động trình thông dịch Python trong môi trường ảo:
```powershell
.\.venv\Scripts\python.exe
```

Sau đó gõ từng dòng lệnh sau và nhấn Enter:

```python
# 1. Thử nghiệm PyVi
from pyvi import ViTokenizer

cau_luat = "Người nào giết người trong tình thế phòng vệ chính đáng thì không phải chịu trách nhiệm hình sự."
tokens_pyvi = ViTokenizer.tokenize(cau_luat)
print("=== KẾT QUẢ PYVI ===")
print(tokens_pyvi)
```

**Quan sát kết quả của bạn trên màn hình:**
`Người_nào giết người trong tình_thế phòng_vệ chính_đáng thì không phải chịu trách_nhiệm hình_sự .`

> **Giải thích của MLR-02:**  
> PyVi tự động nối các từ ghép có nghĩa pháp lý lại với nhau bằng dấu gạch dưới `_`:
> - `tình_thế`, `phòng_vệ`, `chính_đáng`, `trách_nhiệm`, `hình_sự`.  
> Điều này giúp mô hình coi `"phòng_vệ chính_đáng"` là một khái niệm pháp lý hoàn chỉnh, thay vì 2 từ rời rạc `"phòng_vệ"` và `"chính_đáng"`.

Gõ tiếp để thử với Underthesea:
```python
# 2. Thử nghiệm Underthesea
from underthesea import word_tokenize

tokens_uts = word_tokenize(cau_luat, format="text")
print("\n=== KẾT QUẢ UNDERTHESEA ===")
print(tokens_uts)
```

> **Kết luận chọn lựa:**  
> Cả 2 đều tách từ tốt, nhưng **PyVi có tốc độ nhanh gấp ~15 lần Underthesea** và không bị lỗi phụ thuộc, nên dự án chọn **PyVi** làm bộ tách từ chuẩn cho Tầng 1.

Nhấn `exit()` để thoát Python.

---

### Bước 2.3: Thao Tác Thủ Công — Thử Nghiệm Thuật Toán BM25Okapi

Mở lại Python terminal:
```powershell
.\.venv\Scripts\python.exe
```

Gõ đoạn code sau để tự tay xem BM25 tính điểm ra sao:

```python
from rank_bm25 import BM25Okapi
from pyvi import ViTokenizer

# Tạo một tập corpus mini gồm 3 điều luật
corpus_goc = [
    "Điều 19. Quyền sống. Mọi người có quyền sống. Tính mạng con người được pháp luật bảo hộ.",
    "Điều 20. Quyền bất khả xâm phạm về thân thể, được pháp luật bảo hộ về sức khỏe, danh dự.",
    "Điều 21. Quyền bất khả xâm phạm về đời sống riêng tư, bí mật cá nhân và gia đình."
]

# Tách từ tiếng Việt cho từng văn bản
tokenized_corpus = [ViTokenizer.tokenize(doc).lower().split() for doc in corpus_goc]

# Khởi tạo thuật toán BM25Okapi với k1=1.5, b=0.75
bm25 = BM25Okapi(tokenized_corpus, k1=1.5, b=0.75)

# Đặt câu hỏi tìm kiếm
cau_hoi = "Quyền bảo vệ thân thể và sức khỏe"
tokenized_query = ViTokenizer.tokenize(cau_hoi).lower().split()
print("Từ khóa câu hỏi:", tokenized_query)

# Tính điểm cho cả 3 điều luật
scores = bm25.get_scores(tokenized_query)

print("\n--- ĐIỂM SỐ BM25 CỦA TỪNG ĐIỀU LUẬT ---")
for i, score in enumerate(scores):
    print(f"Văn bản #{i+1} [Điểm: {score:.4f}] -> {corpus_goc[i][:60]}...")
```

**Quan sát kết quả:**
Văn bản `#2` (Điều 20) sẽ có **điểm số cao nhất** vì chứa cả cụm `thân_thể` và `sức_khỏe`!  
Bạn vừa tự tay xây dựng và kiểm chứng thành công thuật toán lõi của Tầng 1!

Gõ `exit()` để thoát.

---

# PHẦN III: TIỀN XỬ LÝ DỮ LIỆU THỦ CÔNG (DATA PREPROCESSING)
*Biên soạn bởi: DE-03 và MLR-02*

---

Chu trình tiền xử lý dữ liệu cho bài toán tra cứu văn bản pháp luật gồm **5 bước chuẩn hóa bắt buộc**:

```
Văn bản HTML Thô
      │
      ▼ (Bước 3.1)
Làm sạch & Chuẩn hóa Unicode NFC (Tránh lỗi font)
      │
      ▼ (Bước 3.2)
Regex Bóc Tách: Phân chia theo từng Điều luật ("1 Điều = 1 Document")
      │
      ▼ (Bước 3.3)
Tách từ ghép tiếng Việt bằng PyVi (ViTokenizer)
      │
      ▼ (Bước 3.4)
Lọc bỏ từ dừng pháp lý (mlr-02_stopwords_vi_legal.txt)
      │
      ▼ (Bước 3.5)
Đóng gói vào SQLite DB & File JSON chuẩn Pydantic
```

---

### Bước 3.1: Viết Hàm Làm Sạch & Chuẩn Hóa Unicode NFC

Mở PowerShell và tạo một file script thực hành có tên `Project/scripts/manual_clean_lab.py`:
```powershell
New-Item -ItemType File -Force -Path "Project\scripts\manual_clean_lab.py"
```

Mở file `Project/scripts/manual_clean_lab.py` trong VS Code và dán nội dung sau vào:

```python
import unicodedata
import re

def clean_and_normalize(raw_text: str) -> str:
    """
    Chuẩn hóa chuỗi văn bản tiếng Việt:
    1. Unicode NFC (chuyển các ký tự có dấu tổ hợp về dựng sẵn)
    2. Xóa khoảng trắng ẩn (non-breaking spaces: \xa0, \u200b)
    3. Chuẩn hóa dấu xuống dòng và khoảng trắng thừa
    """
    if not raw_text:
        return ""

    # Chuẩn hóa về NFC
    text = unicodedata.normalize("NFC", raw_text)
    
    # Thay thế khoảng trắng đặc biệt của HTML
    text = text.replace("\xa0", " ").replace("\u200b", "").replace("\r\n", "\n")
    
    # Rút gọn nhiều khoảng trắng liên tiếp thành 1 khoảng trắng
    text = re.sub(r"[ \t]+", " ", text)
    
    # Rút gọn nhiều dòng trống liên tiếp
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    
    return text.strip()

# Thử nghiệm thực tế
if __name__ == "__main__":
    test_str = "Điều   20.   Quyền  bất khả\xa0xâm phạm về  thân thể.\r\n\r\n\r\nNội dung điều luật..."
    print("Văn bản ban đầu:\n", repr(test_str))
    cleaned = clean_and_normalize(test_str)
    print("\nVăn bản sau làm sạch:\n", repr(cleaned))
```

Chạy thử nghiệm trên terminal:
```powershell
.\.venv\Scripts\python.exe Project\scripts\manual_clean_lab.py
```
Bạn sẽ thấy các khoảng trắng thừa `   `, ký tự lạ `\xa0` và dòng trống dư thừa bị triệt tiêu hoàn toàn!

---

### Bước 3.2: Thực Hành Bóc Tách Điều Luật Bằng Biểu Thức Chính Quy (Regex)

Tạo file thực hành bóc tách: `Project/scripts/manual_parse_lab.py` với nội dung:

```python
import re
from typing import List, Dict

# Regex phát hiện dòng bắt đầu bằng chữ "Điều X." hoặc "Điều X:"
ARTICLE_REGEX = re.compile(
    r'^(?:Điều|Điều)\s+(\d+)[\.:\-\–]\s*(.*?)$',
    re.MULTILINE
)

def parse_articles_from_text(raw_text: str, law_code: str = "HP2013") -> List[Dict]:
    """Bóc tách toàn văn thành danh sách các điều luật có cấu trúc."""
    # Tìm tất cả vị trí bắt đầu của các Điều luật
    matches = list(ARTICLE_REGEX.finditer(raw_text))
    articles = []

    for i in range(len(matches)):
        start_pos = matches[i].start()
        # Kết thúc của điều hiện tại là đầu của điều kế tiếp (hoặc hết văn bản)
        end_pos = matches[i+1].start() if i + 1 < len(matches) else len(raw_text)

        article_block = raw_text[start_pos:end_pos].strip()
        lines = article_block.split("\n", 1)
        
        title_line = lines[0].strip()
        content_body = lines[1].strip() if len(lines) > 1 else ""
        
        art_num = int(matches[i].group(1))

        articles.append({
            "article_id": f"{law_code}_D{art_num}",
            "article_number": art_num,
            "title": title_line,
            "content": content_body,
            "full_text": f"{title_line}\n{content_body}".strip()
        })

    return articles

if __name__ == "__main__":
    sample_text = """
Điều 1. Nước Cộng hòa xã hội chủ nghĩa Việt Nam
Nước Cộng hòa xã hội chủ nghĩa Việt Nam là một nước độc lập, có chủ quyền.

Điều 2. Nhà nước pháp quyền xã hội chủ nghĩa
1. Nhà nước Cộng hòa xã hội chủ nghĩa Việt Nam là nhà nước của Nhân dân.
2. Tất cả quyền lực nhà nước thuộc về Nhân dân.
    """
    results = parse_articles_from_text(sample_text)
    print(f"Đã bóc tách thành công {len(results)} điều luật:")
    for r in results:
        print(f"-> Khóa chính: {r['article_id']} | Tiêu đề: {r['title']}")
```

Chạy thử nghiệm:
```powershell
.\.venv\Scripts\python.exe Project\scripts\manual_parse_lab.py
```
Bạn sẽ thấy 2 điều luật được phân rã thành các dictionary có cấu trúc chuẩn xác!

---

### Bước 3.3: Lọc Bỏ Từ Dừng Pháp Lý Chuyên Dụng

Mở file từ dừng đã chuẩn bị tại:
[.agents/outputs/phase1/mlr-02_stopwords_vi_legal.txt](file:///d:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/)

Tạo script thực hành lọc từ dừng: `Project/scripts/manual_stopwords_lab.py`:

```python
from pathlib import Path
from pyvi import ViTokenizer

STOPWORDS_FILE = Path("Project/../.agents/outputs/phase1/mlr-02_stopwords_vi_legal.txt")

def load_stopwords() -> set:
    stopwords = set()
    if STOPWORDS_FILE.exists():
        with open(STOPWORDS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    stopwords.add(line.lower())
    return stopwords

def filter_tokens(text: str, stopwords: set) -> list:
    # 1. Lowercase và tách từ PyVi
    tokenized = ViTokenizer.tokenize(text.lower())
    tokens = tokenized.split()
    # 2. Loại bỏ từ dừng và ký tự đơn lẻ
    cleaned_tokens = [t for t in tokens if t not in stopwords and len(t) > 1]
    return cleaned_tokens

if __name__ == "__main__":
    sw = load_stopwords()
    print(f"Đã nạp {len(sw)} từ dừng pháp lý.")
    
    text = "Căn cứ theo quy định tại Điều 20 của Hiến pháp về quyền bất khả xâm phạm thân thể."
    filtered = filter_tokens(text, sw)
    print("\nCâu gốc:", text)
    print("Tokens sau khi lọc từ dừng:", filtered)
```

Chạy thử nghiệm:
```powershell
.\.venv\Scripts\python.exe Project\scripts\manual_stopwords_lab.py
```

**Quan sát kết quả:**
Các hư từ và từ hành chính như `"căn_cứ"`, `"theo"`, `"quy_định"`, `"tại"`, `"điều"`, `"của"`, `"về"` đều bị loại bỏ!  
Chỉ giữ lại các terms đắt giá mang tải trọng thông tin cao: `['20', 'hiến_pháp', 'quyền', 'bất_khả', 'xâm_phạm', 'thân_thể']`.

---

### Bước 3.4: Đóng Gói Vào CSDL SQLite & Kiểm Tra Thực Tế

Bây giờ bạn sẽ tự tay nạp 30 điều luật mẫu đã chuẩn bị vào CSDL SQLite và chạy một truy vấn kiểm tra.

Chạy lệnh sau trên terminal PowerShell:
```powershell
.\.venv\Scripts\python.exe -c "
import json, sys
sys.path.insert(0, 'Project')
from app.core.database import init_database, get_db_connection
from app.repositories.article_repo import ArticleRepository
from app.models.law_article import LawArticleCreate

# 1. Khởi tạo bảng CSDL
init_database()

# 2. Đọc 30 điều luật mẫu
with open('Project/data/sample/sample_articles.json', 'r', encoding='utf-8') as f:
    raw_articles = json.load(f)

# 3. Nạp vào SQLite qua ArticleRepository
repo = ArticleRepository()
count = 0
for item in raw_articles:
    article_model = LawArticleCreate.model_validate(item)
    repo.save(article_model)
    count += 1

print(f'[✓] Tự tay nạp thành công {count} điều luật vào cơ sở dữ liệu SQLite!')

# 4. Kiểm tra lại bằng lệnh SQL đếm số lượng
with get_db_connection() as conn:
    c = conn.cursor()
    c.execute('SELECT law_code, count(*) FROM law_articles GROUP BY law_code')
    print('\n--- Thống kê điều luật theo từng bộ luật trong SQLite ---')
    for row in c.fetchall():
        print(f'-> Bộ luật: {row[0]:<10} | Số lượng: {row[1]} điều')
"
```

---

# PHẦN IV: CHẠY THỬ NGHIỆM HỆ THỐNG (END-TO-END VERIFICATION)
*Biên soạn bởi: Kiến trúc sư SA-04 và Kiểm thử viên EVAL-05*

---

Sau khi bạn đã hoàn thành việc thu thập, kiểm nghiệm mô hình và nạp dữ liệu thủ công:

### Bước 4.1: Khởi Động Server Backend
Mở PowerShell và chạy:
```powershell
.\manage_venv.ps1 run-server
```
Terminal sẽ hiển thị:
```text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

### Bước 4.2: Truy Cập Giao Diện Trực Quan Swagger Docs
1. Mở trình duyệt web (Chrome, Edge).
2. Truy cập vào địa chỉ: `http://127.0.0.1:8000/docs`
3. Nhấp vào mục `POST /api/retrieve` $\rightarrow$ Nhấn nút **Try it out**.
4. Tại ô Request body, nhập:
   ```json
   {
     "query": "Quyền bất khả xâm phạm về thân thể",
     "top_k": 3
   }
   ```
5. Nhấn **Execute** và xem phản hồi HTTP 200: Điều 20 Hiến pháp 2013 sẽ xuất hiện ở vị trí Rank #1!

---

## 🎯 Tóm Tắt & Checklist Tự Nghiệm Thu (Self-Evaluation)
Khi hoàn thành toàn bộ các bước trên, bạn hãy mở file [.agents/team/handmade/TASKS.md](file:///d:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI/) và tích chọn `[x]` vào các task đã làm. Bạn đã chính thức làm chủ 100% dữ liệu và thuật toán Tầng 1 của dự án!
