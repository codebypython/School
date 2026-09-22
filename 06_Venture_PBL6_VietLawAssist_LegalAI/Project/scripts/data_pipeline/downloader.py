"""
VietLawAssist — Multi-Source Legal Document Downloader
======================================================
Agent-03 (Data Engineer) — Tải toàn văn 5 bộ luật từ nguồn chính thống và Thư viện Pháp luật.
Hỗ trợ:
    - Cơ chế Retry và Exponential Backoff chống gián đoạn mạng
    - Tự động trích xuất vùng nội dung văn bản (divContentDoc / toanvancontent) để giảm dung lượng
    - Lưu trữ bản HTML thô vào thư mục data/raw/html/ làm nguồn backup
"""

import time
from pathlib import Path
from typing import Optional
from bs4 import BeautifulSoup
import httpx
from loguru import logger

from .config import LAW_TARGETS, RAW_HTML_DIR


def extract_clean_content_container(html_raw: str) -> str:
    """
    Trích xuất phân vùng chứa toàn văn luật thực sự từ HTML,
    loại bỏ quảng cáo, scripts, css và banner điều hướng.
    """
    soup = BeautifulSoup(html_raw, "html.parser")

    # 1. Thư viện pháp luật: nằm trong divContentDoc hoặc content1
    target = soup.find("div", id="divContentDoc") or soup.find("div", class_="cldivContentDocVn")
    if not target:
        # 2. VBPL: nằm trong toanvancontent
        target = soup.find("div", class_="toanvancontent") or soup.find("div", id="toanvancontent")

    if target:
        # Xóa các script và style rác
        for tag in target(["script", "style", "iframe"]):
            tag.decompose()
        return str(target)

    # Nếu không tìm thấy container đặc thù, trả về toàn bộ HTML
    return html_raw


def download_law_html(law_code: str, force: bool = False) -> Optional[Path]:
    """
    Tải file HTML toàn văn cho một bộ luật cụ thể.
    Ưu tiên TVPL (có đầy đủ 100% văn bản đã số hóa), fallback sang VBPL.
    """
    if law_code not in LAW_TARGETS:
        logger.error(f"Mã luật '{law_code}' không nằm trong danh mục LAW_TARGETS")
        return None

    meta = LAW_TARGETS[law_code]
    dest_file = RAW_HTML_DIR / f"{law_code}.html"

    # Kiểm tra file cache đã tồn tại chưa
    if dest_file.exists() and not force:
        size_kb = dest_file.stat().st_size / 1024
        logger.info(f"[{law_code}] Đã có sẵn file cache tại {dest_file.name} ({size_kb:.1f} KB). Bỏ qua tải lại.")
        return dest_file

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8",
    }

    # Thử lần lượt các URL
    candidate_urls = [meta["tvpl_url"], meta["vbpl_url"]]

    for url in candidate_urls:
        logger.info(f"[{law_code}] Đang gửi yêu cầu tải toàn văn từ: {url}")
        for attempt in range(1, 4):
            try:
                with httpx.Client(timeout=30.0, follow_redirects=True, headers=headers) as client:
                    response = client.get(url)
                    response.raise_for_status()

                    html_text = response.text
                    clean_html = extract_clean_content_container(html_text)

                    dest_file.write_text(clean_html, encoding="utf-8")
                    size_kb = len(clean_html.encode("utf-8")) / 1024
                    logger.success(f"[{law_code}] Tải thành công! Kích thước vùng luật: {size_kb:.1f} KB -> Lưu tại: {dest_file}")
                    return dest_file

            except Exception as e:
                logger.warning(f"[{law_code}] Lần thử {attempt}/3 gặp lỗi: {e}")
                time.sleep(1.5 * attempt)

    logger.error(f"[{law_code}] Không thể tải từ các nguồn!")
    return None


def download_all_laws(force: bool = False) -> dict[str, bool]:
    """
    Tải toàn bộ 5 bộ luật cốt lõi trong danh mục.
    """
    results = {}
    logger.info("=== BẮT ĐẦU TIẾN TRÌNH TẢI TOÀN VĂN 5 BỘ LUẬT ===")
    for code in LAW_TARGETS:
        saved_path = download_law_html(code, force=force)
        results[code] = saved_path is not None
        time.sleep(1.0)

    success_count = sum(results.values())
    logger.info(f"=== KẾT QUẢ TẢI: {success_count}/{len(LAW_TARGETS)} BỘ LUẬT THÀNH CÔNG ===")
    return results
