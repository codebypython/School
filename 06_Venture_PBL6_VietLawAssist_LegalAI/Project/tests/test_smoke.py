"""
VietLawAssist — Automated Smoke Tests
=====================================
Bộ kiểm thử tự động xác minh toàn bộ các thành phần chính:
- Schemas & Pydantic models
- PyVi Vietnamese tokenization
- BM25 indexing & search
- FastAPI health check endpoint
"""

import json
from pathlib import Path
import pytest
from pyvi import ViTokenizer
from rank_bm25 import BM25Okapi

from app.models.law_article import LawArticleCreate
from app.models.textbook_principle import TextbookPrincipleCreate
from app.core.database import get_database_path, get_corpus_stats
from app.repositories.article_repo import ArticleRepository
from app.repositories.textbook_repo import TextbookPrincipleRepository
from app.main import app

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATA_PATH = PROJECT_ROOT / "data" / "sample" / "sample_articles.json"
PRINCIPLES_PATH = PROJECT_ROOT / "data" / "sample" / "textbook_principles.json"


def test_pydantic_schema_validation():
    """Kiểm tra schema Pydantic v2 trên 30 điều luật mẫu."""
    assert SAMPLE_DATA_PATH.exists(), f"Không tìm thấy file: {SAMPLE_DATA_PATH}"
    with open(SAMPLE_DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 30, f"Kỳ vọng 30 điều luật, nhận {len(data)}"
    validated = [LawArticleCreate.model_validate(item) for item in data]
    assert len(validated) == 30
    assert validated[0].article_id == "HP2013_D1"
    assert validated[0].law_code == "HP2013"


def test_textbook_principles_schema():
    """Kiểm tra schema lý luận giáo trình chuẩn 5 dạng đề thi."""
    assert PRINCIPLES_PATH.exists(), f"Không tìm thấy file: {PRINCIPLES_PATH}"
    with open(PRINCIPLES_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) >= 5, f"Kỳ vọng ít nhất 5 nguyên lý, nhận {len(data)}"
    validated = [TextbookPrincipleCreate.model_validate(item) for item in data]
    assert len(validated) >= 5
    topic_codes = {item.topic_code for item in validated}
    assert "QPPL_STRUCTURE" in topic_codes
    assert "VPPL_ELEMENTS" in topic_codes
    assert "CIVIL_INHERIT" in topic_codes
    assert "CRIMINAL_AGE" in topic_codes


def test_pyvi_tokenization():
    """Kiểm tra bộ tách từ tiếng Việt PyVi."""
    text = "Quyền bất khả xâm phạm về thân thể của công dân"
    tokenized = ViTokenizer.tokenize(text)
    tokens = tokenized.split()
    assert "bất_khả" in tokens
    assert "xâm_phạm" in tokens
    assert "thân_thể" in tokens
    assert "công_dân" in tokens


def test_bm25_search_functionality():
    """Kiểm tra thuật toán xếp hạng BM25Okapi."""
    with open(SAMPLE_DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    corpus_tokens = [ViTokenizer.tokenize(item["full_text"]).split() for item in data]
    bm25 = BM25Okapi(corpus_tokens)

    query = "Quyền bất khả xâm phạm về thân thể"
    query_tokens = ViTokenizer.tokenize(query).split()
    scores = bm25.get_scores(query_tokens)

    best_idx = scores.argmax()
    assert data[best_idx]["article_id"] == "HP2013_D20", (
        f"Kỳ vọng Điều 20 Hiến pháp 2013, nhận {data[best_idx]['article_id']}"
    )


def test_database_dual_corpus_integrity():
    """Kiểm tra tính toàn vẹn của CSDL SQLite kho kép."""
    db_path = get_database_path()
    assert db_path.exists(), f"Database chưa tồn tại tại: {db_path}"

    stats = get_corpus_stats(db_path)
    assert stats["total_articles"] >= 40, f"Kỳ vọng >= 40 điều luật, nhận {stats['total_articles']}"
    assert stats["total_principles"] >= 5, f"Kỳ vọng >= 5 nguyên lý, nhận {stats['total_principles']}"
    assert len(stats["laws"]) == 5, f"Kỳ vọng đầy đủ 5 bộ luật, nhận {len(stats['laws'])}"

    # Kiểm tra repository queries
    art_repo = ArticleRepository(db_path)
    hngd_arts = art_repo.get_by_law_code("HNGD2014")
    assert len(hngd_arts) >= 5

    blld_arts = art_repo.get_by_law_code("BLLD2019")
    assert len(blld_arts) >= 5

    textbook_repo = TextbookPrincipleRepository(db_path)
    inherit_principle = textbook_repo.get_by_topic_code("CIVIL_INHERIT")
    assert len(inherit_principle) >= 1
    assert "Điều 644" in inherit_principle[0]["rules_json"] or "BLDS2015_D644" in inherit_principle[0]["rules_json"]


def test_fastapi_app_structure():
    """Kiểm tra ứng dụng FastAPI và danh sách routes."""
    routes = [route.path for route in app.routes]
    assert "/api/health" in routes
    assert "/api/retrieve" in routes
