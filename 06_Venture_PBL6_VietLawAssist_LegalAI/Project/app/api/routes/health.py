"""
VietLawAssist — Health Check Endpoint
=======================================
GET /api/health — Kiểm tra trạng thái hệ thống.

Trả về:
    - Phiên bản ứng dụng
    - Trạng thái kết nối database
    - Thống kê corpus (nếu có dữ liệu)
    - Trạng thái BM25 index
"""

from datetime import datetime

from fastapi import APIRouter, Depends
from loguru import logger

from app.config import Settings, get_settings
from app.core.database import get_corpus_stats
from app.models.law_article import HealthResponse


router = APIRouter(prefix="/api", tags=["System"])


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health Check",
    description="Kiểm tra trạng thái hoạt động của hệ thống VietLawAssist",
)
async def health_check(settings: Settings = Depends(get_settings)):
    """
    Endpoint kiểm tra sức khỏe hệ thống.

    Kiểm tra:
        1. Kết nối database SQLite
        2. Thống kê corpus (số điều luật, số từ)
        3. BM25 index có sẵn sàng không

    Returns:
        HealthResponse: Trạng thái chi tiết của hệ thống.
    """
    # --- Kiểm tra database ---
    db_connected = False
    corpus_stats = None
    try:
        stats = get_corpus_stats()
        db_connected = True
        if stats["total_articles"] > 0:
            corpus_stats = stats
    except Exception as e:
        logger.warning(f"Database check failed: {e}")

    # --- Kiểm tra BM25 index ---
    bm25_loaded = False
    try:
        from app.services.bm25_service import bm25_service
        bm25_loaded = bm25_service.is_loaded
    except Exception:
        pass

    return HealthResponse(
        status="healthy" if db_connected else "degraded",
        version=settings.app_version,
        environment=settings.app_env,
        database_connected=db_connected,
        corpus_stats=corpus_stats,
        bm25_index_loaded=bm25_loaded,
        timestamp=datetime.now(),
    )
