"""
VietLawAssist — HTML & Legal Text Corpus Parser
===============================================
Agent-03 (Data Engineer) — Module bóc tách toàn văn HTML từ TVPL và VBPL thành cấu trúc điều luật JSON.

Chiến lược Chunking:
    - 1 Điều luật = 1 Document độc lập (Article-level chunking).
    - Chuẩn hóa Unicode NFC và làm sạch ký tự đặc biệt.
    - Bóc tách phân cấp: Chương -> Mục -> Điều -> Khoản.
    - Tự động tách từ ghép tiếng Việt (PyVi/Underthesea) cho trường content_tokenized.
"""

import json
import re
from pathlib import Path
from typing import Optional
from bs4 import BeautifulSoup
from loguru import logger

from scripts.clean_text import clean_full_pipeline, normalize_unicode_nfc
from .config import LAW_TARGETS, RAW_DIR, RAW_HTML_DIR


def tokenize_vietnamese_text(text: str) -> str:
    """
    Tách từ ghép tiếng Việt (nối bằng dấu gạch dưới '_') để tối ưu cho BM25.
    """
    try:
        from pyvi import ViTokenizer
        return ViTokenizer.tokenize(text)
    except Exception:
        try:
            from underthesea import word_tokenize
            tokens = word_tokenize(text, format="text")
            return tokens
        except Exception:
            return text


def parse_legal_text(raw_text: str, law_code: str) -> list[dict]:
    """
    Bóc tách chuỗi văn bản thuần thành danh sách các điều luật cấu trúc.
    """
    meta = LAW_TARGETS.get(law_code, {
        "law_name": law_code,
        "effective_date": "",
        "tvpl_url": "",
    })

    cleaned_text = clean_full_pipeline(raw_text)
    lines = cleaned_text.splitlines()

    articles = []
    current_chapter = ""
    current_section = ""
    current_article_num: Optional[int] = None
    current_title = ""
    current_content_lines: list[str] = []

    # Regex nhận diện Chương, Mục, Điều theo thể thức văn bản pháp luật VN
    re_chapter = re.compile(r"^(Chương\s+[IVXLCDM0-9]+[\s\.:\-_].*)$", re.IGNORECASE)
    re_section = re.compile(r"^(Mục\s+[IVXLCDM0-9]+[\s\.:\-_].*)$", re.IGNORECASE)
    re_article = re.compile(r"^Điều\s+(\d+)[\.:\s]*(.*)$", re.IGNORECASE)

    def save_current_article():
        nonlocal current_article_num, current_title, current_content_lines
        if current_article_num is not None:
            content_str = "\n".join(current_content_lines).strip()
            if not content_str:
                content_str = current_title

            title_str = (
                f"Điều {current_article_num}. {current_title}".strip()
                if current_title
                else f"Điều {current_article_num}"
            )
            full_text = f"{title_str}\n{content_str}".strip()

            articles.append({
                "id": f"{law_code}_D{current_article_num}",
                "article_id": f"{law_code}_D{current_article_num}",
                "law_code": law_code,
                "law_name": meta["law_name"],
                "chapter": current_chapter,
                "section": current_section,
                "article_number": current_article_num,
                "clause_number": None,
                "title": title_str,
                "content": content_str,
                "content_raw": full_text,
                "content_tokenized": tokenize_vietnamese_text(full_text.lower()),
                "full_text": full_text,
                "effective_date": meta["effective_date"],
                "source_url": meta.get("tvpl_url") or meta.get("vbpl_url", ""),
                "word_count": len(content_str.split()),
            })
            current_content_lines = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        chap_m = re_chapter.match(stripped)
        if chap_m:
            current_chapter = chap_m.group(1).strip()
            continue

        sec_m = re_section.match(stripped)
        if sec_m:
            current_section = sec_m.group(1).strip()
            continue

        art_m = re_article.match(stripped)
        if art_m:
            save_current_article()
            current_article_num = int(art_m.group(1))
            current_title = art_m.group(2).strip()
            continue

        if current_article_num is not None:
            current_content_lines.append(stripped)

    save_current_article()
    logger.info(f"[{law_code}] Đã bóc tách thành công {len(articles)} điều luật.")
    return articles


def parse_cached_html_file(law_code: str) -> list[dict]:
    """
    Đọc và bóc tách từ file HTML cache trong data/raw/html/.
    Hỗ trợ bóc tách trực tiếp các thẻ p/div từ cấu trúc TVPL.
    """
    html_path = RAW_HTML_DIR / f"{law_code}.html"
    if not html_path.exists():
        logger.warning(f"Không tìm thấy file cache HTML tại {html_path}")
        return []

    html_content = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html_content, "html.parser")

    # Loại bỏ thẻ rác
    for tag in soup(["script", "style", "iframe", "noscript"]):
        tag.decompose()

    raw_text = soup.get_text(separator="\n")
    return parse_legal_text(raw_text, law_code)


def build_combined_corpus(output_path: Optional[Path] = None) -> list[dict]:
    """
    Tổng hợp toàn bộ các điều luật đã bóc tách được từ cả 5 bộ luật,
    kết hợp với bộ điều luật trọng tâm high-yield để đảm bảo độ phủ 100%.
    """
    if output_path is None:
        output_path = RAW_DIR / "corpus_combined.json"

    articles_by_id = {}

    # 1. Thử parse từ các file HTML tải về
    for law_code in LAW_TARGETS:
        parsed = parse_cached_html_file(law_code)
        for art in parsed:
            articles_by_id[art["id"]] = art

    # 2. Hòa trộn bộ curated high-yield từ crawl_laws.py để đảm bảo không thiếu điều trọng tâm
    try:
        from scripts.crawl_laws import build_curated_high_yield_articles
        curated = build_curated_high_yield_articles()
        for art in curated:
            art_id = art.get("id") or art.get("article_id")
            if art_id not in articles_by_id:
                art["id"] = art_id
                art["article_id"] = art_id
                if "content_tokenized" not in art:
                    art["content_tokenized"] = tokenize_vietnamese_text((art.get("full_text") or art.get("content", "")).lower())
                if "content_raw" not in art:
                    art["content_raw"] = art.get("full_text") or art.get("content", "")
                articles_by_id[art_id] = art
    except Exception as e:
        logger.warning(f"Không thể nạp fallback curated articles: {e}")

    all_articles = list(articles_by_id.values())

    # Sắp xếp lại theo bộ luật và số điều
    all_articles.sort(key=lambda x: (x["law_code"], x["article_number"]))

    # Lưu ra file JSON
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_articles, f, ensure_ascii=False, indent=2)

    logger.success(f"Tổng hợp hoàn tất! Đã xuất {len(all_articles)} điều luật ra: {output_path}")
    return all_articles
