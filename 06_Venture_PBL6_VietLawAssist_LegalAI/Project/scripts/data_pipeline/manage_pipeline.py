"""
VietLawAssist — Master Data Pipeline CLI Manager
================================================
Agent-03 (Data Engineer) & Agent-02 (ML Researcher)
CLI quản lý một chạm toàn bộ chu trình sống của dữ liệu (Data Lifecycle):
    Download -> Parse -> Ingest DB -> SFT Generation -> Stratified Split -> Kaggle Package -> Sync
"""

import sqlite3
import sys
from pathlib import Path
import click
from loguru import logger

# Đảm bảo Windows console in tiếng Việt không bị lỗi cp1252 charmap
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from .benchmark_builder import validate_benchmark_integrity
from .config import DATA_DIR, DB_PATH, KAGGLE_BUNDLE_DIR, PROCESSED_DIR, RAW_DIR, RAW_HTML_DIR, SAMPLE_DIR
from .downloader import download_all_laws, download_law_html
from .kaggle_bundle import prepare_kaggle_bundle, upload_to_kaggle
from .parser import build_combined_corpus, parse_cached_html_file
from .sft_builder import save_and_report_sft_dataset
from .split_sft import split_sft_stratified


@click.group()
def cli():
    """VietLawAssist Data Pipeline — Hệ thống Quản trị & Xử lý Dữ liệu Toàn diện."""
    pass


@cli.command("download")
@click.option("--law-code", default=None, help="Mã luật cụ thể (VD: HP2013, BLDS2015). Để trống sẽ tải cả 5 bộ luật.")
@click.option("--force", is_flag=True, help="Tải lại dù file cache đã tồn tại.")
def download_cmd(law_code: str, force: bool):
    """Tải toàn văn HTML các bộ luật từ nguồn chính thống và TVPL."""
    if law_code:
        download_law_html(law_code.upper(), force=force)
    else:
        download_all_laws(force=force)


@cli.command("parse")
@click.option("--output", default=str(RAW_DIR / "corpus_combined.json"), help="Đường dẫn file JSON đầu ra.")
def parse_cmd(output: str):
    """Bóc tách HTML đã tải thành tập điều luật cấu trúc JSON."""
    build_combined_corpus(Path(output))


@cli.command("ingest")
@click.option("--corpus", default=str(RAW_DIR / "corpus_combined.json"), help="File corpus JSON cần nạp.")
@click.option("--textbook", default=str(SAMPLE_DIR / "textbook_principles.json"), help="File giáo trình JSON cần nạp.")
@click.option("--reset", is_flag=True, help="Khởi tạo lại cơ sở dữ liệu từ đầu.")
def ingest_cmd(corpus: str, textbook: str, reset: bool):
    """Nạp dữ liệu vào SQLite DB (law_articles & textbook_principles)."""
    from scripts.ingest_db import ingest_all
    ingest_all.callback(reset=reset, raw_json=corpus)


@cli.command("sft-status")
def sft_status_cmd():
    """Kiểm tra tiến độ thu thập và phân bổ của tập 500 mẫu SFT LoRA."""
    save_and_report_sft_dataset()


@cli.command("split-sft")
@click.option("--val-ratio", default=0.2, help="Tỷ lệ tập validation (mặc định 0.2 tức 20%).")
def split_sft_cmd(val_ratio: float):
    """Phân tầng tập SFT thành Train (80%) và Validation (20%) ở cả dạng Alpaca và ChatML."""
    save_and_report_sft_dataset()
    split_sft_stratified(val_ratio=val_ratio)


@cli.command("prep-kaggle")
@click.option("--username", default="vietlawassist", help="Tên tài khoản Kaggle của bạn.")
@click.option("--dataset-slug", default="vietlawassist-pbl6-legal-ai", help="Slug định danh dataset.")
def prep_kaggle_cmd(username: str, dataset_slug: str):
    """Đóng gói tất cả thành phần dữ liệu vào thư mục data/kaggle_bundle/ sẵn sàng upload."""
    split_sft_stratified()
    prepare_kaggle_bundle(kaggle_username=username, dataset_slug=dataset_slug)


@cli.command("upload-kaggle")
@click.option("--message", default="Update dataset version", help="Ghi chú phiên bản cập nhật.")
def upload_kaggle_cmd(message: str):
    """Tải hoặc cập nhật phiên bản mới lên Kaggle qua Kaggle CLI."""
    upload_to_kaggle(message=message)


@cli.command("benchmark")
def benchmark_cmd():
    """Kiểm tra tính toàn vẹn của tập Benchmark test cases."""
    validate_benchmark_integrity()


@cli.command("stats")
def stats_cmd():
    """Thống kê chi tiết số lượng dữ liệu hiện có trong Database."""
    if not DB_PATH.exists():
        logger.error(f"Không tìm thấy Database tại {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT law_code, COUNT(*), SUM(LENGTH(full_text)) FROM law_articles GROUP BY law_code")
    art_stats = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM law_articles")
    total_articles = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM textbook_principles")
    total_principles = cursor.fetchone()[0]
    conn.close()

    logger.info("=== BÁO CÁO TỔNG THỂ DỮ LIỆU TRONG HỆ THỐNG ===")
    logger.info(f"Tổng số điều luật thực định trong DB: {total_articles} điều")
    for code, count, total_len in art_stats:
        avg_len = (total_len or 0) / count if count else 0
        logger.info(f"  - [{code:10s}]: {count:4d} điều (Trung bình {avg_len:.0f} ký tự/điều)")

    logger.info(f"Tổng số nguyên lý giáo trình chuẩn: {total_principles} nguyên lý")


@cli.command("run-all")
@click.option("--username", default="vietlawassist", help="Tên tài khoản Kaggle của bạn.")
def run_all_cmd(username: str):
    """Thực thi chuỗi xử lý tự động một chạm: Parse -> Ingest DB -> SFT -> Split -> Kaggle Prep -> Stats."""
    logger.info("🚀 Bắt đầu quy trình tự động hóa dữ liệu một chạm...")
    build_combined_corpus()
    save_and_report_sft_dataset()
    split_sft_stratified()
    prepare_kaggle_bundle(kaggle_username=username)
    validate_benchmark_integrity()
    logger.success("✅ Toàn bộ quy trình hoàn tất thành công!")


if __name__ == "__main__":
    cli()
