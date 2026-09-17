"""
VietLawAssist — Article Repository
====================================
Tầng Data Access (Repository Pattern) — CRUD operations cho law_articles.
Tuân thủ Clean Architecture: Controller → Service → Repository.

Bảo mật:
    - 100% sử dụng Parameterized Queries (chống SQL Injection).
    - Không bao giờ nối chuỗi trực tiếp vào câu SQL.
"""

import sqlite3
from pathlib import Path
from typing import Optional

from loguru import logger

from app.core.database import get_db_connection
from app.models.law_article import LawArticleCreate, LawArticleSummary


class ArticleRepository:
    """
    Repository quản lý CRUD cho bảng law_articles.

    Attributes:
        db_path: Đường dẫn file SQLite. None = dùng config mặc định.
    """

    def __init__(self, db_path: Path | None = None):
        self.db_path = db_path

    def insert_article(self, article: LawArticleCreate) -> int:
        """
        Thêm 1 điều luật vào database.

        Args:
            article: Dữ liệu điều luật cần thêm.

        Returns:
            ID của bản ghi vừa insert.

        Raises:
            sqlite3.IntegrityError: Nếu article_id đã tồn tại (UNIQUE constraint).
        """
        sql = """
            INSERT INTO law_articles
                (article_id, law_code, law_name, chapter, section,
                 article_number, title, content, full_text,
                 effective_date, source_url, word_count)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (
                article.article_id,
                article.law_code,
                article.law_name,
                article.chapter,
                article.section,
                article.article_number,
                article.title,
                article.content,
                article.full_text,
                article.effective_date,
                article.source_url,
                article.word_count,
            ))
            return cursor.lastrowid

    def insert_many(self, articles: list[LawArticleCreate]) -> int:
        """
        Batch insert nhiều điều luật (hiệu quả hơn insert_article từng cái).

        Args:
            articles: Danh sách điều luật cần thêm.

        Returns:
            Số bản ghi đã insert thành công.
        """
        sql = """
            INSERT OR IGNORE INTO law_articles
                (article_id, law_code, law_name, chapter, section,
                 article_number, title, content, full_text,
                 effective_date, source_url, word_count)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        data = [
            (
                a.article_id, a.law_code, a.law_name, a.chapter, a.section,
                a.article_number, a.title, a.content, a.full_text,
                a.effective_date, a.source_url, a.word_count,
            )
            for a in articles
        ]
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany(sql, data)
            inserted = cursor.rowcount
            logger.info(f"Batch insert: {inserted}/{len(articles)} điều luật")
            return inserted

    def get_by_article_id(self, article_id: str) -> Optional[dict]:
        """
        Tìm điều luật theo article_id (VD: HP2013_D20).

        Args:
            article_id: Mã định danh duy nhất.

        Returns:
            dict hoặc None nếu không tìm thấy.
        """
        sql = "SELECT * FROM law_articles WHERE article_id = ?"
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (article_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def get_by_law_code(self, law_code: str) -> list[dict]:
        """
        Lấy tất cả điều luật thuộc một bộ luật.

        Args:
            law_code: Mã bộ luật (VD: HP2013, BLDS2015).

        Returns:
            List các dict, mỗi dict là 1 điều luật.
        """
        sql = """
            SELECT * FROM law_articles
            WHERE law_code = ?
            ORDER BY article_number ASC
        """
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (law_code,))
            return [dict(row) for row in cursor.fetchall()]

    def get_all_for_indexing(self) -> list[LawArticleSummary]:
        """
        Lấy toàn bộ điều luật (rút gọn) để build BM25 index.

        Returns:
            List LawArticleSummary — chỉ chứa fields cần cho indexing.
        """
        sql = """
            SELECT article_id, law_code, law_name, article_number,
                   title, content, word_count
            FROM law_articles
            ORDER BY law_code, article_number
        """
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            return [
                LawArticleSummary(**dict(row))
                for row in cursor.fetchall()
            ]

    def count_articles(self) -> int:
        """Đếm tổng số điều luật trong database."""
        sql = "SELECT COUNT(*) FROM law_articles"
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchone()[0]

    def search_by_keyword(self, keyword: str, limit: int = 10) -> list[dict]:
        """
        Tìm kiếm cơ bản bằng LIKE (fallback khi BM25 chưa sẵn sàng).

        Args:
            keyword: Từ khóa tìm kiếm.
            limit: Số kết quả tối đa.

        Returns:
            List các dict điều luật phù hợp.
        """
        sql = """
            SELECT * FROM law_articles
            WHERE content LIKE ? OR title LIKE ?
            ORDER BY law_code, article_number
            LIMIT ?
        """
        pattern = f"%{keyword}%"
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (pattern, pattern, limit))
            return [dict(row) for row in cursor.fetchall()]

    def delete_by_law_code(self, law_code: str) -> int:
        """
        Xóa toàn bộ điều luật thuộc một bộ luật (dùng khi re-crawl).

        Args:
            law_code: Mã bộ luật cần xóa.

        Returns:
            Số bản ghi đã xóa.
        """
        sql = "DELETE FROM law_articles WHERE law_code = ?"
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (law_code,))
            deleted = cursor.rowcount
            logger.warning(f"Đã xóa {deleted} điều luật của {law_code}")
            return deleted

    def get_article_count_by_law(self) -> list[dict]:
        """Đếm số điều luật theo từng bộ luật."""
        sql = """
            SELECT law_code, law_name, COUNT(*) as count
            FROM law_articles
            GROUP BY law_code
            ORDER BY count DESC
        """
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            return [dict(row) for row in cursor.fetchall()]
