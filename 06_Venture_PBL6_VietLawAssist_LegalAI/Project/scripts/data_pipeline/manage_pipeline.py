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
from .exam_crawler import scan_and_harvest_local_exams
from .exam_pairer import pair_separate_exam_and_answer_files, pair_split_sections_in_single_file
from .kaggle_bundle import prepare_kaggle_bundle, upload_to_kaggle
from .kaggle_manager import setup_all_kaggle_artifacts
from .parser import build_combined_corpus, parse_cached_html_file
from .sft_builder import save_and_report_sft_dataset
from .sft_curator import curate_and_build_sft_dataset
from .smart_ocr import ocr_scanned_pdf, ocr_image_folder
from .split_sft import split_sft_stratified


@click.group()
def cli():
    """VietLawAssist Data Pipeline — Hệ thống Quản trị & Xử lý Dữ liệu Toàn diện."""
    pass


@cli.command("ocr")
@click.option("--file", "input_file", default=None, help="Đường dẫn file PDF scan hoặc ảnh cần OCR.")
@click.option("--folder", "input_folder", default=None, help="Thư mục chứa các ảnh scan cần OCR hàng loạt.")
@click.option("--dpi", default=300, help="Độ phân giải DPI khi render PDF (mặc định 300).")
def ocr_cmd(input_file: str, input_folder: str, dpi: int):
    """OCR tiếng Việt miễn phí cục bộ bằng Tesseract v5 cho PDF scan và ảnh crop."""
    if input_file:
        p = Path(input_file)
        if p.suffix.lower() == ".pdf":
            ocr_scanned_pdf(p, dpi=dpi)
        else:
            from .smart_ocr import ocr_single_image
            text = ocr_single_image(p)
            out_p = RAW_DIR / "exams" / f"{p.stem}_ocr.txt"
            out_p.write_text(text, encoding="utf-8")
            logger.success(f"Đã xuất kết quả OCR ảnh ra: {out_p}")
    elif input_folder:
        ocr_image_folder(Path(input_folder))
    else:
        logger.error("Vui lòng cung cấp --file hoặc --folder để thực hiện OCR.")


@cli.command("pair")
@click.option("--questions", "-q", default=None, help="File chứa danh sách đề bài / câu hỏi.")
@click.option("--answers", "-a", default=None, help="File chứa danh sách lời giải / đáp án.")
@click.option("--split-file", "-s", default=None, help="File đơn chứa 2 phần: Đề bài ở trên và Đáp án ở dưới.")
def pair_cmd(questions: str, answers: str, split_file: str):
    """Tự động đồng bộ và ghép nối các file Đề thi và Đáp án rời rạc thành file Q&A chuẩn barem."""
    if questions and answers:
        pair_separate_exam_and_answer_files(questions, answers)
    elif split_file:
        pair_split_sections_in_single_file(split_file)
    else:
        logger.error("Vui lòng cung cấp (-q và -a) hoặc (-s) để thực hiện ghép nối.")


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


@cli.command("crawl-exams")
@click.option("--exam-dir", default=None, help="Thư mục chứa đề thi thô cần quét.")
def crawl_exams_cmd(exam_dir: str):
    """Quét và trích xuất câu hỏi, barem lời giải từ kho đề thi thực tế (data/raw/exams/)."""
    target = Path(exam_dir) if exam_dir else None
    results = scan_and_harvest_local_exams(target)
    logger.info(f"Đã thu hoạch được {len(results)} câu hỏi đề thi.")


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


@cli.command("curate-sft")
@click.option("--target", default=500, help="Số lượng mẫu SFT mục tiêu (mặc định 500).")
def curate_sft_cmd(target: int):
    """Hợp nhất Seeds + Synthetic + Exam Cases, khử trùng lặp và kiểm chuẩn 500 mẫu SFT."""
    curate_and_build_sft_dataset(target_count=target)


@cli.command("split-sft")
@click.option("--val-ratio", default=0.2, help="Tỷ lệ tập validation (mặc định 0.2 tức 20%).")
def split_sft_cmd(val_ratio: float):
    """Phân tầng tập SFT thành Train (80%) và Validation (20%) ở cả dạng Alpaca và ChatML."""
    save_and_report_sft_dataset()
    split_sft_stratified(val_ratio=val_ratio)


@cli.command("setup-kaggle")
def setup_kaggle_cmd():
    """Kiến tạo trọn bộ thư mục Project/kaggle/ (Dataset bundle, Notebook QLoRA, Train script, README)."""
    setup_all_kaggle_artifacts()


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
@click.option("--target-sft", default=500, help="Số lượng mẫu SFT mục tiêu.")
def run_all_cmd(username: str, target_sft: int):
    """Thực thi chuỗi xử lý tự động một chạm: Parse -> Ingest DB -> Curate SFT -> Split -> Kaggle Setup -> Stats."""
    logger.info("🚀 Bắt đầu quy trình tự động hóa dữ liệu một chạm...")
    build_combined_corpus()
    curate_and_build_sft_dataset(target_count=target_sft)
    setup_all_kaggle_artifacts()
    prepare_kaggle_bundle(kaggle_username=username)
    validate_benchmark_integrity()
    logger.success("✅ Toàn bộ quy trình hoàn tất thành công!")


if __name__ == "__main__":
    cli()

