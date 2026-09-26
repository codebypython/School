"""
VietLawAssist — Smart PDF & Document Extractor (smart_extractor.py)
==================================================================
Agent-03 (Data Engineer)
Module trích xuất văn bản thông minh từ PDF (kể cả PDF bị khóa copy/paste)
và tài liệu học thuật offline 100% MIỄN PHÍ bằng thư viện PyMuPDF (fitz).

Tính năng:
    1. Trích xuất text từ Digital PDF tốc độ cao (bỏ qua rào cản chặn copy/paste).
    2. Tự động kiểm tra chất lượng text layer (phát hiện trang scan/ảnh).
    3. Làm sạch văn bản, chuẩn hóa tiếng Việt Unicode NFC.
    4. Tự động chuyển đổi và lưu sang data/raw/exams/ dưới dạng .txt sẵn sàng bóc tách.
"""

import sys
from pathlib import Path
from loguru import logger
import fitz  # PyMuPDF

from scripts.clean_text import clean_full_pipeline
from .config import RAW_DIR

RAW_EXAMS_DIR = RAW_DIR / "exams"
RAW_EXAMS_DIR.mkdir(parents=True, exist_ok=True)


def extract_text_from_pdf(pdf_path: Path, output_txt_path: Path = None) -> dict:
    """
    Trích xuất toàn bộ văn bản từ file PDF bằng PyMuPDF.
    Bỏ qua hoàn toàn các hạn chế chống copy-paste trên trình duyệt/web.
    """
    if not pdf_path.exists():
        logger.error(f"Tệp PDF không tồn tại: {pdf_path}")
        return {"success": False, "error": "File not found"}

    try:
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        full_text = []
        scanned_pages = []

        for page_idx in range(total_pages):
            page = doc[page_idx]
            page_text = page.get_text("text").strip()

            if len(page_text) < 50:
                # Trang có quá ít text -> có khả năng cao là ảnh scan
                scanned_pages.append(page_idx + 1)
            else:
                full_text.append(page_text)

        combined_text = "\n\n".join(full_text)
        cleaned_text = clean_full_pipeline(combined_text)

        if not output_txt_path:
            output_txt_path = RAW_EXAMS_DIR / f"{pdf_path.stem}.txt"

        output_txt_path.write_text(cleaned_text, encoding="utf-8")

        result = {
            "success": True,
            "pdf_file": pdf_path.name,
            "output_file": str(output_txt_path),
            "total_pages": total_pages,
            "extracted_pages": total_pages - len(scanned_pages),
            "scanned_pages": scanned_pages,
            "character_count": len(cleaned_text),
            "is_mostly_scanned": len(scanned_pages) > (total_pages / 2)
        }

        logger.info(
            f"Đã trích xuất PDF: {pdf_path.name} -> {output_txt_path.name} "
            f"({result['character_count']} ký tự, {result['extracted_pages']}/{total_pages} trang có text)."
        )
        return result

    except Exception as e:
        logger.error(f"Lỗi khi xử lý PDF {pdf_path.name}: {e}")
        return {"success": False, "error": str(e)}


def batch_convert_exam_pdfs(input_dir: Path) -> list[dict]:
    """Chuyển đổi hàng loạt các file PDF trong thư mục sang text sạch."""
    results = []
    for pdf_file in input_dir.glob("*.pdf"):
        res = extract_text_from_pdf(pdf_file)
        results.append(res)
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
        extract_text_from_pdf(target)
    else:
        logger.info("Chạy smart_extractor: Cung cấp đường dẫn file PDF để trích xuất.")
