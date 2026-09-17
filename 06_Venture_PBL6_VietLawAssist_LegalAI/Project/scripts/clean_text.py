"""
VietLawAssist — Text Cleaning Utilities
==========================================
Agent-03 (Data Engineer) — Module làm sạch văn bản pháp luật.

Xử lý:
    1. Unicode NFC normalization (tránh lỗi tổ hợp dấu tiếng Việt)
    2. HTML tag stripping
    3. Whitespace normalization
    4. Vietnamese punctuation cleanup
    5. Legal text specific cleaning (số hiệu, ký tự đặc biệt)
"""

import re
import unicodedata
from typing import Optional

from loguru import logger


def normalize_unicode_nfc(text: str) -> str:
    """
    Chuẩn hóa Unicode NFC cho tiếng Việt.

    Tại sao cần NFC?
        Tiếng Việt có 2 cách biểu diễn dấu:
        - NFC (Composed): "ă" = 1 code point (U+0103)
        - NFD (Decomposed): "ă" = "a" + combining breve (U+0061 + U+0306)

        Nếu corpus lẫn NFC + NFD → BM25 tokenizer sẽ coi "ăn" và "ăn" là 2 từ
        khác nhau → giảm recall nghiêm trọng.

    Args:
        text: Văn bản cần chuẩn hóa.

    Returns:
        Văn bản đã chuẩn hóa NFC.
    """
    return unicodedata.normalize("NFC", text)


def strip_html_tags(text: str) -> str:
    """
    Loại bỏ toàn bộ HTML tags khỏi text.

    Args:
        text: Văn bản có thể chứa HTML tags.

    Returns:
        Văn bản thuần text (plain text).
    """
    clean = re.sub(r"<[^>]+>", "", text)
    clean = clean.replace("&nbsp;", " ")
    clean = clean.replace("&amp;", "&")
    clean = clean.replace("&lt;", "<")
    clean = clean.replace("&gt;", ">")
    clean = clean.replace("&quot;", '"')
    clean = clean.replace("&#39;", "'")
    clean = clean.replace("&apos;", "'")
    return clean


def normalize_whitespace(text: str) -> str:
    """
    Chuẩn hóa khoảng trắng:
        - Thay nhiều spaces/tabs liên tiếp bằng 1 space
        - Thay nhiều newlines liên tiếp bằng 1 newline
        - Xóa spaces ở đầu/cuối mỗi dòng

    Args:
        text: Văn bản cần chuẩn hóa.

    Returns:
        Văn bản đã chuẩn hóa khoảng trắng.
    """
    text = text.replace("\t", " ")
    text = re.sub(r"[^\S\n]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = [line.strip() for line in text.split("\n")]
    text = "\n".join(lines)
    return text.strip()


def clean_legal_text(text: str) -> str:
    """
    Xử lý đặc thù cho văn bản pháp luật Việt Nam:
        - Loại bỏ zero-width characters
        - Chuẩn hóa dấu ngoặc kép thông minh
        - Chuẩn hóa dấu gạch ngang
        - Chuẩn hóa circled digits

    Args:
        text: Văn bản pháp luật cần clean.

    Returns:
        Văn bản đã được clean.
    """
    # Loại bỏ zero-width characters
    text = re.sub(r"[\u200b\u200c\u200d\ufeff\u00ad]", "", text)

    # Chuẩn hóa dấu ngoặc kép thông minh
    text = text.replace("\u201c", '"')
    text = text.replace("\u201d", '"')
    text = text.replace("\u2018", "'")
    text = text.replace("\u2019", "'")

    # Chuẩn hóa dấu gạch ngang
    text = text.replace("\u2013", "-")
    text = text.replace("\u2014", "-")

    # Chuẩn hóa dấu ba chấm
    text = text.replace("\u2026", "...")

    # Chuẩn hóa circled digits
    circled_digits = {
        "①": "1)", "②": "2)", "③": "3)", "④": "4)", "⑤": "5)",
        "⑥": "6)", "⑦": "7)", "⑧": "8)", "⑨": "9)", "⑩": "10)",
    }
    for symbol, replacement in circled_digits.items():
        text = text.replace(symbol, replacement)

    return text


def clean_full_pipeline(text: str) -> str:
    """
    Pipeline làm sạch hoàn chỉnh — áp dụng tất cả bước tuần tự.

    Thứ tự:
        1. Unicode NFC → 2. Strip HTML → 3. Legal clean → 4. Whitespace

    Args:
        text: Văn bản thô (raw text từ crawler).

    Returns:
        Văn bản đã làm sạch hoàn chỉnh.
    """
    if not text or not text.strip():
        return ""

    text = normalize_unicode_nfc(text)
    text = strip_html_tags(text)
    text = clean_legal_text(text)
    text = normalize_whitespace(text)

    return text


def count_words(text: str) -> int:
    """Đếm số từ trong văn bản (whitespace split)."""
    if not text or not text.strip():
        return 0
    return len(text.split())


def extract_article_number(text: str) -> Optional[int]:
    """
    Trích xuất số điều từ chuỗi tiêu đề.

    Examples:
        "Điều 20. Quyền bất khả xâm phạm" → 20
        "Điều 158a. ..." → 158

    Returns:
        Số điều (int) hoặc None nếu không tìm thấy.
    """
    match = re.search(r"Điều\s+(\d+)", text)
    if match:
        return int(match.group(1))
    return None


if __name__ == "__main__":
    sample = """
    <p>  Điều 20. Quyền   bất khả xâm phạm về &nbsp; thân thể  </p>
    <br/>
    1. Mọi người có quyền bất khả xâm phạm về thân thể,
    được pháp luật bảo hộ về   sức khoẻ, danh dự và nhân phẩm.

    2. Không ai bị bắt nếu không có quyết định   của Toà án nhân dân.
    """

    cleaned = clean_full_pipeline(sample)
    print("=== CLEANED TEXT ===")
    print(cleaned)
    print(f"\nWord count: {count_words(cleaned)}")
    print(f"Article number: {extract_article_number(cleaned)}")
