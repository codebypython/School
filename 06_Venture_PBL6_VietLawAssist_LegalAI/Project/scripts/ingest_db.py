"""
VietLawAssist — Master Dual Database Ingestion Script
=====================================================
Agent-03 (Data Engineer) — Nạp toàn bộ dữ liệu kép vào SQLite:
    1. Bảng law_articles: Điều luật thực định 5 bộ luật.
    2. Bảng textbook_principles: Lý luận & barem chuẩn Giáo trình PLĐC Bộ GD&ĐT.

Bảo mật & Chuẩn mực:
    - 100% Parameterized Queries qua Repository Pattern.
    - Transaction an toàn, tự động rollback khi lỗi.
    - Chuẩn hóa Unicode NFC và dọn dẹp văn bản tự động.
"""

import json
import sys
from pathlib import Path
import click
from loguru import logger

# Đảm bảo import được app package
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from app.core.database import init_database, get_database_path, get_corpus_stats
from app.models.law_article import LawArticleCreate
from app.models.textbook_principle import TextbookPrincipleCreate
from app.repositories.article_repo import ArticleRepository
from app.repositories.textbook_repo import TextbookPrincipleRepository
from scripts.crawl_laws import build_curated_high_yield_articles, RAW_DIR, SAMPLE_DIR


@click.command()
@click.option("--reset", is_flag=True, help="Xóa và khởi tạo lại database từ đầu")
@click.option("--raw-json", default=None, help="Đường dẫn file JSON corpus tùy chỉnh")
def ingest_all(reset: bool, raw_json: str | None):
    """Thực thi nạp toàn diện kho dữ liệu kép vào SQLite."""
    db_path = get_database_path()
    logger.info(f"Bắt đầu quy trình nạp dữ liệu vào: {db_path}")

    if reset and db_path.exists():
        logger.warning(f"Reset database: Xóa tệp hiện tại tại {db_path}")
        db_path.unlink()

    # 1. Khởi tạo cấu trúc các bảng
    init_database(db_path)

    # 2. Chuẩn bị dữ liệu điều luật
    if raw_json and Path(raw_json).exists():
        with open(raw_json, "r", encoding="utf-8") as f:
            articles_raw = json.load(f)
        logger.info(f"Đọc {len(articles_raw)} điều luật từ {raw_json}")
    else:
        # Nếu chưa có file raw riêng, sử dụng hàm tổng hợp 5 bộ luật
        corpus_combined_path = RAW_DIR / "corpus_combined.json"
        if not corpus_combined_path.exists():
            logger.info("Chưa có corpus_combined.json, tự động khởi tạo dữ liệu trọng tâm...")
            RAW_DIR.mkdir(parents=True, exist_ok=True)
            articles_raw = build_curated_high_yield_articles()
            with open(corpus_combined_path, "w", encoding="utf-8") as f:
                json.dump(articles_raw, f, ensure_ascii=False, indent=2)
        else:
            with open(corpus_combined_path, "r", encoding="utf-8") as f:
                articles_raw = json.load(f)

    # Validate qua Pydantic
    article_models = [LawArticleCreate(**item) for item in articles_raw]

    # Ingest vào law_articles
    article_repo = ArticleRepository(db_path)
    inserted_articles = article_repo.insert_many(article_models)
    logger.success(f"✅ Đã nạp thành công {inserted_articles} điều luật vào bảng law_articles")

    # 3. Chuẩn bị và nạp lý luận giáo trình (textbook_principles)
    principles_file = SAMPLE_DIR / "textbook_principles.json"
    inserted_principles = 0
    if principles_file.exists():
        with open(principles_file, "r", encoding="utf-8") as f:
            principles_raw = json.load(f)
        
        principle_models = [TextbookPrincipleCreate(**item) for item in principles_raw]
        principle_repo = TextbookPrincipleRepository(db_path)
        inserted_principles = principle_repo.insert_many(principle_models)
        logger.success(f"✅ Đã nạp thành công {inserted_principles} nguyên lý giáo trình vào bảng textbook_principles")
    else:
        logger.warning(f"Không tìm thấy file nguyên lý tại: {principles_file}")

    # 4. Xuất báo cáo nghiệm thu
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    stats = get_corpus_stats(db_path)
    print("\n" + "=" * 60)
    print("[*] BAO CAO THONG KE KHO DU LIEU KEP (DUAL-CORPUS STATS)")
    print("=" * 60)
    print(f"[*] Duong dan CSDL       : {db_path}")
    print(f"[*] Tong so Dieu luat    : {stats['total_articles']}")
    print(f"[*] Tong so Nguyen ly GT : {stats.get('total_principles', 0)}")
    print(f"[*] Tong so Tu phap ly   : {stats['total_words']:,} tu")
    print("\n--- Phan bo theo Bo luat ---")
    for law in stats["laws"]:
        print(f"  * {law['law_code']:<10} | {law['law_name'][:45]:<45} | {law['count']:>3} dieu | TB: {law['avg_words']:>5.1f} tu/dieu")
    print("=" * 60)


if __name__ == "__main__":
    ingest_all()
