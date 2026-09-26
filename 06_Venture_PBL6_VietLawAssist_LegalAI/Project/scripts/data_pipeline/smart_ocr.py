"""
VietLawAssist — Offline OCR Engine for Scanned Legal Exams (smart_ocr.py)
========================================================================
Agent-03 (Data Engineer) & Agent-02 (ML Researcher)
Module nhận dạng quang học ký tự (OCR) tiếng Việt cục bộ 100% MIỄN PHÍ.
Sử dụng Tesseract-OCR v5 (vie) kết hợp PyMuPDF render ảnh độ phân giải cao (DPI 300).

Hỗ trợ:
    1. File PDF thuần ảnh scan / ảnh chụp crop.
    2. File ảnh đơn lẻ (.png, .jpg, .jpeg, .bmp, .tiff).
    3. Hàng loạt ảnh trong một thư mục (Batch OCR).
    4. Tiền xử lý ảnh (Grayscale, Contrast enhancement, Thresholding) chống mờ chữ.
"""

import os
import sys
from pathlib import Path
from typing import Optional, Union
from PIL import Image, ImageEnhance, ImageFilter
import fitz  # PyMuPDF
from loguru import logger
import pytesseract

from scripts.clean_text import clean_full_pipeline
from .config import RAW_DIR

RAW_EXAMS_DIR = RAW_DIR / "exams"
RAW_EXAMS_DIR.mkdir(parents=True, exist_ok=True)

# Tự động định vị Tesseract executable trên Windows
TESSERACT_DEFAULT_PATHS = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
]

def configure_tesseract():
    """Tự động kiểm tra và cấu hình đường dẫn tesseract_cmd."""
    for path in TESSERACT_DEFAULT_PATHS:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            return path
    return "tesseract"

configure_tesseract()


def preprocess_image_for_ocr(img: Image.Image) -> Image.Image:
    """
    Tiền xử lý ảnh giúp nâng cao độ chính xác nhận diện tiếng Việt:
    - Chuyển sang ảnh thang xám (Grayscale).
    - Tăng độ tương phản (Contrast Enhancement).
    - Khử nhiễu nhẹ.
    """
    # 1. Chuyển sang ảnh xám
    gray = img.convert("L")
    
    # 2. Tăng độ tương phản chữ
    enhancer = ImageEnhance.Contrast(gray)
    enhanced = enhancer.enhance(1.8)
    
    # 3. Lọc làm sắc nét cạnh chữ
    sharpened = enhanced.filter(ImageFilter.SHARPEN)
    return sharpened


def ocr_single_image(img_path: Union[str, Path], lang: str = "vie") -> str:
    """Nhận dạng văn bản tiếng Việt từ một file ảnh đơn lẻ."""
    img_path = Path(img_path)
    if not img_path.exists():
        logger.error(f"Không tìm thấy ảnh: {img_path}")
        return ""

    try:
        with Image.open(img_path) as img:
            processed_img = preprocess_image_for_ocr(img)
            text = pytesseract.image_to_string(processed_img, lang=lang, config="--psm 1 --oem 1")
            cleaned = clean_full_pipeline(text)
            return cleaned
    except Exception as e:
        logger.error(f"Lỗi OCR ảnh {img_path.name}: {e}")
        return ""


def ocr_scanned_pdf(
    pdf_path: Union[str, Path],
    output_txt_path: Optional[Union[str, Path]] = None,
    dpi: int = 300,
    lang: str = "vie"
) -> dict:
    """
    Nhận dạng toàn bộ các trang ảnh trong file PDF scan/crop.
    Render từng trang ở độ phân giải cao (DPI 300) rồi chạy OCR tiếng Việt.
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        logger.error(f"Không tìm thấy PDF: {pdf_path}")
        return {"success": False, "error": "File not found"}

    logger.info(f"Bắt đầu OCR PDF thuần ảnh: {pdf_path.name} (DPI={dpi}, lang={lang})...")
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    all_pages_text = []

    # Hệ số phóng đại zoom tương ứng với DPI (mặc định 72 DPI)
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)

    for page_idx in range(total_pages):
        page = doc[page_idx]
        pix = page.get_pixmap(matrix=mat, alpha=False)
        
        # Chuyển Pixmap sang PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        processed_img = preprocess_image_for_ocr(img)
        
        # Thực hiện OCR
        page_text = pytesseract.image_to_string(processed_img, lang=lang, config="--psm 1 --oem 1")
        cleaned_page = clean_full_pipeline(page_text)
        
        all_pages_text.append(f"--- TRANG {page_idx + 1} ---\n{cleaned_page}")
        logger.info(f"Đã xử lý OCR trang {page_idx + 1}/{total_pages} ({len(cleaned_page)} ký tự)")

    full_content = "\n\n".join(all_pages_text)

    if not output_txt_path:
        output_txt_path = RAW_EXAMS_DIR / f"{pdf_path.stem}_ocr.txt"
    else:
        output_txt_path = Path(output_txt_path)

    output_txt_path.parent.mkdir(parents=True, exist_ok=True)
    output_txt_path.write_text(full_content, encoding="utf-8")

    logger.success(f"Hoàn thành OCR! Đã xuất văn bản sạch tại: {output_txt_path} ({len(full_content)} ký tự)")
    return {
        "success": True,
        "input_pdf": str(pdf_path),
        "output_file": str(output_txt_path),
        "total_pages": total_pages,
        "character_count": len(full_content)
    }


def ocr_image_folder(folder_path: Union[str, Path], output_txt_path: Optional[Union[str, Path]] = None) -> Path:
    """OCR hàng loạt các file ảnh trong một thư mục và gom thành 1 file text duy nhất."""
    folder = Path(folder_path)
    valid_exts = {".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp"}
    images = sorted([f for f in folder.iterdir() if f.suffix.lower() in valid_exts])

    if not images:
        logger.warning(f"Không tìm thấy file ảnh nào trong: {folder}")
        return None

    logger.info(f"Tìm thấy {len(images)} ảnh cần OCR trong {folder.name}...")
    combined_texts = []

    for idx, img_p in enumerate(images, 1):
        txt = ocr_single_image(img_p)
        combined_texts.append(f"=== ẢNH {idx}: {img_p.name} ===\n{txt}")
        logger.info(f"OCR xong ảnh {idx}/{len(images)}: {img_p.name}")

    full_text = "\n\n".join(combined_texts)
    if not output_txt_path:
        output_txt_path = RAW_EXAMS_DIR / f"{folder.name}_combined_ocr.txt"
    else:
        output_txt_path = Path(output_txt_path)

    output_txt_path.write_text(full_text, encoding="utf-8")
    logger.success(f"Đã gom toàn bộ ảnh OCR vào: {output_txt_path}")
    return output_txt_path
