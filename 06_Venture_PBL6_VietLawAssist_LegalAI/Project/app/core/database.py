"""
VietLawAssist — Database Connection Manager
=============================================
Quản lý kết nối SQLite với connection pooling cơ bản.
Tuân thủ Clean Architecture: tầng Infrastructure.

Schema chính:
    law_articles — Bảng lưu trữ toàn bộ điều luật đã crawl & clean.
"""

import sqlite3
from pathlib import Path
from contextlib import contextmanager
from typing import Generator

from loguru import logger

from app.config import get_settings


# ===========================================================
#  SQL: Tạo bảng law_articles
#  Mỗi bản ghi = 1 điều luật (chunking strategy: 1 article = 1 doc)
# ===========================================================
CREATE_LAW_ARTICLES_TABLE = """
CREATE TABLE IF NOT EXISTS law_articles (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    article_id      TEXT    NOT NULL UNIQUE,
    law_code        TEXT    NOT NULL,
    law_name        TEXT    NOT NULL,
    chapter         TEXT    DEFAULT '',
    section         TEXT    DEFAULT '',
    article_number  INTEGER NOT NULL,
    title           TEXT    DEFAULT '',
    content         TEXT    NOT NULL,
    full_text       TEXT    NOT NULL,
    effective_date  TEXT    DEFAULT '',
    source_url      TEXT    DEFAULT '',
    word_count      INTEGER DEFAULT 0,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_INDEXES = """
CREATE INDEX IF NOT EXISTS idx_law_articles_law_code
    ON law_articles (law_code);
CREATE INDEX IF NOT EXISTS idx_law_articles_article_number
    ON law_articles (law_code, article_number);
CREATE INDEX IF NOT EXISTS idx_law_articles_article_id
    ON law_articles (article_id);
"""


# ===========================================================
#  SQL: Tạo bảng textbook_principles
#  Lý luận và cấu trúc barem chuẩn Giáo trình PLĐC
# ===========================================================
CREATE_TEXTBOOK_PRINCIPLES_TABLE = """
CREATE TABLE IF NOT EXISTS textbook_principles (
    id              TEXT PRIMARY KEY,
    topic_code      TEXT NOT NULL,
    chapter         TEXT NOT NULL,
    framework_title TEXT NOT NULL,
    rules_json      TEXT NOT NULL,
    theory_content  TEXT NOT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_TEXTBOOK_INDEXES = """
CREATE INDEX IF NOT EXISTS idx_textbook_topic_code
    ON textbook_principles (topic_code);
"""


def get_database_path() -> Path:
    """Lấy đường dẫn database từ config, tạo thư mục cha nếu chưa có."""
    settings = get_settings()
    db_path = settings.database_path
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return db_path


def init_database(db_path: Path | None = None) -> None:
    """
    Khởi tạo database: tạo các bảng và index nếu chưa tồn tại.

    Args:
        db_path: Đường dẫn tùy chỉnh (dùng trong testing).
                 Nếu None, dùng path từ config.
    """
    if db_path is None:
        db_path = get_database_path()

    logger.info(f"Khởi tạo database tại: {db_path}")

    conn = sqlite3.connect(str(db_path))
    try:
        cursor = conn.cursor()
        # Tạo bảng law_articles
        cursor.executescript(CREATE_LAW_ARTICLES_TABLE)
        cursor.executescript(CREATE_INDEXES)
        # Tạo bảng textbook_principles
        cursor.executescript(CREATE_TEXTBOOK_PRINCIPLES_TABLE)
        cursor.executescript(CREATE_TEXTBOOK_INDEXES)
        conn.commit()
        logger.success(f"Database đã sẵn sàng với 2 bảng: {db_path}")
    except sqlite3.Error as e:
        logger.error(f"Lỗi khởi tạo database: {e}")
        raise
    finally:
        conn.close()


# Alias for backward compatibility
init_db = init_database



@contextmanager
def get_db_connection(db_path: Path | None = None) -> Generator[sqlite3.Connection, None, None]:
    """
    Context manager cho kết nối SQLite.
    Tự động commit khi thành công, rollback khi lỗi.

    Usage:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM law_articles")

    Args:
        db_path: Đường dẫn tùy chỉnh. Nếu None, dùng path từ config.
    """
    if db_path is None:
        db_path = get_database_path()

    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row  # Trả về dict-like rows
    conn.execute("PRAGMA journal_mode=WAL")  # Write-Ahead Logging cho concurrency
    conn.execute("PRAGMA foreign_keys=ON")

    try:
        yield conn
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        logger.error(f"Database error (rollback): {e}")
        raise
    finally:
        conn.close()


def get_corpus_stats(db_path: Path | None = None) -> dict:
    """
    Lấy thống kê tổng quan của corpus trong database.

    Returns:
        dict: {
            "total_articles": int,
            "total_words": int,
            "laws": [{"law_code": str, "law_name": str, "count": int, "avg_words": float}]
        }
    """
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()

        # Tổng số điều luật
        cursor.execute("SELECT COUNT(*) FROM law_articles")
        total_articles = cursor.fetchone()[0]

        # Tổng số nguyên lý lý luận giáo trình
        cursor.execute("SELECT COUNT(*) FROM textbook_principles")
        total_principles = cursor.fetchone()[0]

        # Tổng số từ
        cursor.execute("SELECT COALESCE(SUM(word_count), 0) FROM law_articles")
        total_words = cursor.fetchone()[0]

        # Thống kê theo bộ luật
        cursor.execute("""
            SELECT
                law_code,
                law_name,
                COUNT(*) as article_count,
                ROUND(AVG(word_count), 1) as avg_words,
                MIN(word_count) as min_words,
                MAX(word_count) as max_words
            FROM law_articles
            GROUP BY law_code
            ORDER BY article_count DESC
        """)

        laws = []
        for row in cursor.fetchall():
            laws.append({
                "law_code": row["law_code"],
                "law_name": row["law_name"],
                "count": row["article_count"],
                "avg_words": row["avg_words"],
                "min_words": row["min_words"],
                "max_words": row["max_words"],
            })

    return {
        "total_articles": total_articles,
        "total_principles": total_principles,
        "total_words": total_words,
        "laws": laws,
    }
