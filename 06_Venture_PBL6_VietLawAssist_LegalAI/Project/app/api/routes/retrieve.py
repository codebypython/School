"""
VietLawAssist — Retrieve Endpoint
====================================
POST /api/retrieve — Tìm kiếm điều luật liên quan bằng BM25.

Đây là API cốt lõi của Tầng 1 (BM25 Sparse Retrieval):
    1. Nhận câu hỏi pháp luật từ user
    2. Tokenize tiếng Việt (PyVi/Underthesea)
    3. Tìm kiếm BM25Okapi trên corpus ~1.588 điều
    4. Trả về Top-K điều luật có điểm relevance cao nhất
"""

import time

from fastapi import APIRouter, HTTPException
from loguru import logger

from app.models.law_article import (
    SearchRequest,
    SearchResponse,
    SearchResultItem,
)
from app.services.bm25_service import bm25_service


router = APIRouter(prefix="/api", tags=["Retrieval"])


@router.post(
    "/retrieve",
    response_model=SearchResponse,
    summary="Tìm kiếm điều luật (BM25)",
    description="Tìm kiếm điều luật liên quan nhất dựa trên câu hỏi pháp luật",
)
async def retrieve_articles(request: SearchRequest):
    """
    Tìm kiếm điều luật bằng BM25Okapi.

    Flow:
        query → Vietnamese tokenize → BM25 scoring → Top-K results

    Args:
        request: SearchRequest chứa query, method, top_k.

    Returns:
        SearchResponse: Danh sách điều luật có điểm relevance cao nhất.

    Raises:
        HTTPException 503: Nếu BM25 index chưa được build.
        HTTPException 400: Nếu method chưa được hỗ trợ.
    """
    # --- Validate method ---
    if request.method == "dense":
        raise HTTPException(
            status_code=400,
            detail="Dense retrieval (PhoBERT + FAISS) chưa được triển khai. "
                   "Sẽ có trong Phase 2 (Tuần 3-4). "
                   "Hiện tại chỉ hỗ trợ method='bm25'."
        )

    if request.method == "both":
        raise HTTPException(
            status_code=400,
            detail="Hybrid retrieval chưa được triển khai. "
                   "Hiện tại chỉ hỗ trợ method='bm25'."
        )

    # --- Kiểm tra BM25 index ---
    if not bm25_service.is_loaded:
        raise HTTPException(
            status_code=503,
            detail="BM25 index chưa được build. "
                   "Chạy 'python scripts/ingest_db.py' trước, "
                   "sau đó khởi động lại server."
        )

    # --- Thực hiện tìm kiếm ---
    start_time = time.perf_counter()

    try:
        raw_results = bm25_service.search(
            query=request.query,
            top_k=request.top_k,
        )
    except Exception as e:
        logger.error(f"BM25 search error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Lỗi tìm kiếm: {str(e)}"
        )

    elapsed_ms = (time.perf_counter() - start_time) * 1000

    # --- Format response ---
    results = []
    for rank, item in enumerate(raw_results, start=1):
        results.append(SearchResultItem(
            rank=rank,
            article_id=item["article_id"],
            law_code=item["law_code"],
            law_name=item["law_name"],
            article_number=item["article_number"],
            title=item["title"],
            content=item["content"],
            score=round(item["score"], 4),
        ))

    logger.info(
        f"BM25 search: query='{request.query[:50]}...' "
        f"→ {len(results)} results in {elapsed_ms:.1f}ms"
    )

    return SearchResponse(
        query=request.query,
        method="bm25",
        total_results=len(results),
        results=results,
        search_time_ms=round(elapsed_ms, 2),
    )
