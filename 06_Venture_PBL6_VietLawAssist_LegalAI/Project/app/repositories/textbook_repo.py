"""
VietLawAssist — Textbook Principles Repository
================================================
Tầng Data Access (Repository Pattern) — CRUD cho textbook_principles.
Tuân thủ Clean Architecture và 100% Parameterized Queries.
"""

from pathlib import Path
from typing import Optional
from loguru import logger

from app.core.database import get_db_connection
from app.models.textbook_principle import TextbookPrincipleCreate


class TextbookPrincipleRepository:
    """Repository quản lý CRUD cho bảng textbook_principles."""

    def __init__(self, db_path: Path | None = None):
        self.db_path = db_path

    def insert_principle(self, principle: TextbookPrincipleCreate) -> str:
        """Thêm 1 nguyên lý lý luận vào database."""
        sql = """
            INSERT OR REPLACE INTO textbook_principles
                (id, topic_code, chapter, framework_title, rules_json, theory_content)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (
                principle.id,
                principle.topic_code,
                principle.chapter,
                principle.framework_title,
                principle.rules_json,
                principle.theory_content,
            ))
            return principle.id

    def insert_many(self, principles: list[TextbookPrincipleCreate]) -> int:
        """Batch insert nhiều nguyên lý giáo trình."""
        sql = """
            INSERT OR REPLACE INTO textbook_principles
                (id, topic_code, chapter, framework_title, rules_json, theory_content)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        data = [
            (
                p.id, p.topic_code, p.chapter, p.framework_title,
                p.rules_json, p.theory_content,
            )
            for p in principles
        ]
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany(sql, data)
            inserted = cursor.rowcount
            logger.info(f"Batch insert: {inserted}/{len(principles)} nguyên lý giáo trình")
            return inserted

    def get_by_id(self, principle_id: str) -> Optional[dict]:
        """Tìm nguyên lý theo id."""
        sql = "SELECT * FROM textbook_principles WHERE id = ?"
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (principle_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def get_by_topic_code(self, topic_code: str) -> list[dict]:
        """Lấy tất cả nguyên lý thuộc một chủ đề dạng đề thi."""
        sql = """
            SELECT * FROM textbook_principles
            WHERE topic_code = ?
            ORDER BY id ASC
        """
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (topic_code,))
            return [dict(row) for row in cursor.fetchall()]

    def get_all(self) -> list[dict]:
        """Lấy toàn bộ nguyên lý giáo trình."""
        sql = "SELECT * FROM textbook_principles ORDER BY topic_code, id"
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            return [dict(row) for row in cursor.fetchall()]

    def count_principles(self) -> int:
        """Đếm tổng số nguyên lý trong database."""
        sql = "SELECT COUNT(*) FROM textbook_principles"
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchone()[0]
