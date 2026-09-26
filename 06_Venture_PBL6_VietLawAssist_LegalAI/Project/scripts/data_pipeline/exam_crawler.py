"""
VietLawAssist — Exam & Case Law Harvester (exam_crawler.py)
===========================================================
Agent-03 (Data Engineer) & Agent-02 (ML Researcher)
Module thu thập, bóc tách và chuẩn hóa ngân hàng đề thi, bài tập tình huống
và bài giải mẫu môn Pháp luật Đại cương từ các nguồn tài liệu học thuật.

Nguồn hỗ trợ:
    1. Trích xuất từ tệp đề thi thô (.txt, .md, .html) trong data/raw/exams/
    2. Crawl câu hỏi tình huống và giải đáp pháp luật từ Cổng thông tin Tạp chí Tòa án & TVPL
    3. Tự động gắn nhãn phân loại Intent Code (CIVIL_INHERIT, VPPL_ELEMENTS, TRUE_FALSE, QPPL_STRUCTURE, CRIMINAL_AGE)
"""

import json
import re
from pathlib import Path
from typing import Optional
from bs4 import BeautifulSoup
import httpx
from loguru import logger

from scripts.clean_text import clean_full_pipeline, normalize_unicode_nfc
from .config import DATA_DIR, RAW_DIR

RAW_EXAMS_DIR = RAW_DIR / "exams"
RAW_EXAMS_DIR.mkdir(parents=True, exist_ok=True)


# Bộ từ khóa nhận diện Intent Code tự động
INTENT_KEYWORDS = {
    "CIVIL_INHERIT": [
        "thừa kế", "di sản", "di chúc", "chia tài sản", "suất thừa kế", 
        "hàng thừa kế", "thế vị", "điều 644", "điều 651", "điều 652"
    ],
    "VPPL_ELEMENTS": [
        "vi phạm pháp luật", "cấu thành", "mặt khách quan", "mặt chủ quan", 
        "khách thể", "chủ thể", "hành vi trái pháp luật", "lỗi cố ý", "lỗi vô ý", "yếu tố cấu thành"
    ],
    "TRUE_FALSE": [
        "đúng hay sai", "nhận định", "khẳng định", "đúng/sai", "đúng hoặc sai", 
        "giải thích tại sao", "nhận định sau đây", "các khẳng định sau"
    ],
    "QPPL_STRUCTURE": [
        "quy phạm pháp luật", "giả định", "quy định", "chế tài", 
        "cơ cấu quy phạm", "bộ phận giả định", "bộ phận quy định", "bộ phận chế tài"
    ],
    "CRIMINAL_AGE": [
        "trách nhiệm hình sự", "tuổi chịu", "tnhs", "tội phạm ít nghiêm trọng", 
        "tội phạm rất nghiêm trọng", "đặc biệt nghiêm trọng", "điều 12", "điều 9", "đủ 14 tuổi", "đủ 16 tuổi"
    ],
}


def detect_intent_from_text(text: str) -> str:
    """
    Phát hiện mã Intent dựa trên phân tích tần số xuất hiện của từ khóa chuyên ngành.
    """
    text_lower = text.lower()
    scores = {}
    for intent, kws in INTENT_KEYWORDS.items():
        score = sum(1 for kw in kws if kw in text_lower)
        scores[intent] = score

    best_intent = max(scores, key=scores.get)
    if scores[best_intent] > 0:
        return best_intent
    return "GENERAL_THEORY"


def parse_raw_exam_document(file_path: Path) -> list[dict]:
    """
    Bóc tách một tệp đề thi hoặc ngân hàng câu hỏi ôn tập thô (.txt, .md, .html)
    thành danh sách các câu hỏi - câu trả lời có cấu trúc.
    
    Quy ước phân cách câu trong đề thi:
        - "Câu 1:", "Câu 2:", "Bài 1:", "Bài tập 1:", "Tình huống 1:"
        - "Trả lời:", "Đáp án:", "Lời giải:", "Hướng dẫn:"
    """
    if not file_path.exists():
        logger.error(f"Tệp không tồn tại: {file_path}")
        return []

    content = file_path.read_text(encoding="utf-8")
    content = clean_full_pipeline(content)

    # Regex phân tách từng câu hỏi
    question_pattern = re.compile(
        r"(?:^|\n)(?:Câu|Bài|Bài tập|Tình huống)\s+(\d+)[\.:\s\-]+(.*?)(?=(?:\n(?:Câu|Bài|Bài tập|Tình huống)\s+\d+[\.:\s\-]|\Z))",
        re.DOTALL | re.IGNORECASE
    )

    matches = question_pattern.findall(content)
    extracted_items = []

    for q_num, block in matches:
        block = block.strip()
        if not block:
            continue

        # Tách phần Đề bài và phần Lời giải (nếu có)
        answer_split = re.split(
            r"\n(?:\*?\*?(?:Trả lời|Đáp án|Lời giải|Hướng dẫn giải|Giải)\*?\*?[\.:\s\-]+)",
            block,
            maxsplit=1,
            flags=re.IGNORECASE
        )

        question_text = answer_split[0].strip()
        answer_text = answer_split[1].strip() if len(answer_split) > 1 else ""

        intent = detect_intent_from_text(question_text)

        item = {
            "source_file": file_path.name,
            "question_number": int(q_num),
            "intent_code": intent,
            "instruction": f"Hãy giải quyết câu hỏi / bài tập tình huống môn Pháp luật Đại cương thuộc dạng {intent}.",
            "input": question_text,
            "output": answer_text,
            "has_answer": bool(answer_text),
        }
        extracted_items.append(item)

    logger.info(f"[{file_path.name}] Đã trích xuất thành công {len(extracted_items)} câu hỏi/bài tập.")
    return extracted_items


def scan_and_harvest_local_exams(target_dir: Optional[Path] = None) -> list[dict]:
    """
    Quét toàn bộ thư mục data/raw/exams/ để thu hoạch tất cả các tài liệu đề thi và bài giải.
    """
    if target_dir is None:
        target_dir = RAW_EXAMS_DIR

    all_exams = []
    supported_exts = [".txt", ".md", ".json", ".html"]

    for ext in supported_exts:
        for f in target_dir.glob(f"*{ext}"):
            if ext == ".json":
                try:
                    with open(f, "r", encoding="utf-8") as jf:
                        items = json.load(jf)
                        if isinstance(items, list):
                            all_exams.extend(items)
                except Exception as e:
                    logger.warning(f"Lỗi đọc JSON {f.name}: {e}")
            else:
                items = parse_raw_exam_document(f)
                all_exams.extend(items)

    logger.info(f"Tổng hợp thu hoạch từ local exams: {len(all_exams)} câu hỏi.")
    return all_exams
