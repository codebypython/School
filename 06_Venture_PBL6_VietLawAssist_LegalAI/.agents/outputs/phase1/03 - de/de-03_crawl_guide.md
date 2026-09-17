# 🛠 Hướng Dẫn Crawl & Parse Văn Bản Pháp Luật — Agent DE-03

> **Task ID:** D4  
> **Loại output:** 🛠 Hướng dẫn Công cụ + Code Snippet  
> **Ngày tạo:** 2026-09-09  
> **Dùng cho:** Hướng dẫn triển khai Crawler dữ liệu pháp lý tự động & tái lập (Reproducibility)

---

## 1. Giới thiệu Quy trình Khai thác Dữ liệu Pháp lý

Việc thu thập văn bản quy phạm pháp luật Việt Nam (VBQPPL) đòi hỏi quy trình kỹ thuật bài bản vì các trang web cơ quan nhà nước và tra cứu luật có đặc tính:
1. Văn bản rất dài (hàng trăm nghìn từ trên một trang đơn).
2. Định dạng HTML không đồng nhất giữa các thời kỳ số hóa.
3. Chứa nhiều ký tự Unicode tổ hợp (NFD) và ký tự ẩn (non-breaking spaces, control characters).

Hệ thống VietLawAssist ưu tiên 2 phương thức:
- **Phương thức 1 (Chính):** Crawl trực tiếp từ HTML của `vbpl.vn` (Cổng thông tin Pháp điển & VBQPPL Quốc gia).
- **Phương thức 2 (Dự phòng):** Tải file PDF chính thức từ `datafiles.chinhphu.vn` và bóc tách bằng thư viện `PyMuPDF` (`fitz`).

---

## 2. Kỹ thuật Bóc tách HTML từ `vbpl.vn`

### 2.1 CSS Selectors & Cấu trúc DOM
- **URL mẫu:** `https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID={ID}`
- **Vùng chứa toàn văn:** `div.toanvancontent` hoặc `div#toanvancontent`.
- **Đặc điểm:** Toàn bộ văn bản nằm trong một thẻ container duy nhất, bên trong gồm hàng nghìn thẻ `<p>` liên tiếp.
- **Tiêu chí bóc tách Điều luật:** Các thẻ `<p>` có dạng:
  - `<b>Điều {X}. [Tiêu đề]</b>`
  - Hoặc văn bản bắt đầu bằng: `Điều {X}.`

### 2.2 Biểu thức Chính quy (Regex) Phân đoạn Văn bản

```python
import re

# Regex phát hiện bắt đầu một Điều luật
ARTICLE_PATTERN = re.compile(
    r'^(?:Điều|Điều)\s+(\d+)\s*[\.:\-\–]\s*(.*?)$',
    re.MULTILINE | re.IGNORECASE
)

# Regex phát hiện Chương
CHAPTER_PATTERN = re.compile(
    r'^(?:Chương|Chương\s+thứ)\s+([IVXLCDM\d]+)\s*[\.:\-\–]?\s*(.*?)$',
    re.MULTILINE | re.IGNORECASE
)
```

---

## 3. Kỹ thuật Parse PDF bằng `PyMuPDF` (Dự phòng)

Khi nguồn HTML bị lỗi hiển thị hoặc định dạng hỏng, sử dụng file PDF công báo:

```bash
pip install pymupdf==1.23.8
```

```python
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> str:
    """Đọc toàn bộ text từ file PDF văn bản luật với bảo toàn ngắt dòng."""
    doc = fitz.open(pdf_path)
    full_text = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        full_text.append(text)
    doc.close()
    return "\n".join(full_text)
```

---

## 4. Kịch bản Crawl Hoàn Chỉnh: `crawl_sample_law.py`

Dưới đây là mã nguồn hoàn chỉnh với đầy đủ kiểm tra lỗi, rate-limiting (nghỉ 1.5 giây giữa các request), chuẩn hóa Unicode NFC và cấu trúc hóa đối tượng điều luật:

```python
import os
import re
import time
import unicodedata
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any

# Cấu hình Headers giả lập trình duyệt
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

def clean_vietnamese_text(text: str) -> str:
    """Chuẩn hóa Unicode NFC, xóa khoảng trắng thừa và ký tự rác."""
    if not text:
        return ""
    # Chuẩn hóa về NFC
    text = unicodedata.normalize("NFC", text)
    # Thay thế các ký tự khoảng trắng đặc biệt (non-breaking space, tabs)
    text = text.replace("\xa0", " ").replace("\u200b", "")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()

def split_into_articles(raw_html: str, law_code: str, law_name: str, source_url: str) -> List[Dict[str, Any]]:
    """Phân tách HTML toàn văn thành danh sách các bản ghi Điều luật."""
    soup = BeautifulSoup(raw_html, "html.parser")
    
    # Tìm container chứa nội dung chính
    content_div = soup.select_one(".toanvancontent, #toanvancontent, .content-law, body")
    if not content_div:
        raise ValueError("Không tìm thấy container nội dung luật trong trang HTML.")

    # Lấy text từng đoạn <p>
    paragraphs = []
    for p in content_div.find_all(["p", "div"]):
        t = clean_vietnamese_text(p.get_text())
        if t:
            paragraphs.append(t)

    articles = []
    current_chapter = "Chương mở đầu"
    current_article = None
    current_content_lines = []

    article_regex = re.compile(r'^(?:Điều|Điều)\s+(\d+)\s*[\.:\-\–]\s*(.*)$', re.IGNORECASE)
    chapter_regex = re.compile(r'^(?:Chương|Chương\s+thứ)\s+([IVXLCDM\d]+)', re.IGNORECASE)

    for line in paragraphs:
        # Kiểm tra nếu là tiêu đề Chương
        if chapter_regex.match(line):
            current_chapter = line
            continue

        # Kiểm tra nếu là bắt đầu Điều luật mới
        art_match = article_regex.match(line)
        if art_match:
            # Lưu điều luật trước đó nếu có
            if current_article is not None:
                body = "\n".join(current_content_lines).strip()
                current_article["content"] = body
                current_article["full_text"] = f"{current_article['title']}\n{body}".strip()
                current_article["word_count"] = len(current_article["full_text"].split())
                articles.append(current_article)

            # Khởi tạo điều luật mới
            art_num = int(art_match.group(1))
            title_text = clean_vietnamese_text(line)
            current_article = {
                "article_id": f"{law_code}_D{art_num}",
                "law_code": law_code,
                "law_name": law_name,
                "chapter": current_chapter,
                "section": "",
                "article_number": art_num,
                "title": title_text,
                "content": "",
                "full_text": "",
                "effective_date": "",
                "source_url": source_url,
                "word_count": 0
            }
            current_content_lines = []
        else:
            if current_article is not None:
                current_content_lines.append(line)

    # Đóng điều luật cuối cùng
    if current_article is not None:
        body = "\n".join(current_content_lines).strip()
        current_article["content"] = body
        current_article["full_text"] = f"{current_article['title']}\n{body}".strip()
        current_article["word_count"] = len(current_article["full_text"].split())
        articles.append(current_article)

    return articles

def crawl_law(law_code: str, law_name: str, url: str) -> List[Dict[str, Any]]:
    """Hàm wrapper tải trang và parse dữ liệu."""
    print(f"[*] Đang tải dữ liệu từ {url}...")
    resp = requests.get(url, headers=HEADERS, timeout=20)
    resp.encoding = "utf-8"
    if resp.status_code != 200:
        raise ConnectionError(f"Tải trang thất bại với mã trạng thái {resp.status_code}")

    time.sleep(1.5)  # Rate limiting an toàn
    articles = split_into_articles(resp.text, law_code, law_name, url)
    print(f"[✓] Đã bóc tách thành công {len(articles)} điều luật từ {law_code}.")
    return articles
```

---

## 5. Kinh nghiệm Vượt Chướng ngại (Anti-bot & CAPTCHA Troubleshooting)

| Hiện tượng | Nguyên nhân | Biện pháp khắc phục |
|---|---|---|
| **HTTP 403 Forbidden** | Cổng VBPL hoặc TVPL chặn IP hoặc User-Agent rỗng. | Thêm đầy đủ `HEADERS` giả lập Chrome máy tính để bàn. Tránh dùng User-Agent mặc định `python-requests`. |
| **Bị chuyển hướng sang trang CAPTCHA** | Gửi quá nhiều request liên tiếp trong thời gian ngắn. | Giới hạn tần suất: đặt `time.sleep(1.5)` đến `2.0` giây giữa mỗi lần tải. Lưu trang HTML thô ra đĩa local để parse offline, không gửi request lặp lại. |
| **Ký tự tiếng Việt bị lỗi font (`Ä iá» u`)** | Trang web khai báo charset sai hoặc `requests` đoán sai encoding. | Luôn gán tường minh `resp.encoding = "utf-8"` ngay sau khi nhận phản hồi. |
| **Lỗi mất đoạn do thẻ `<br>` lồng nhau** | Nhiều văn bản cũ dùng `<br>` thay vì `<p>`. | Trước khi bóc tách, thay thế `<br/>` và `<br>` bằng ký tự xuống dòng `\n`. |
