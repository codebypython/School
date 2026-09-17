"""
VietLawAssist — Pydantic Data Models (Schemas)
================================================
Định nghĩa tất cả data models cho ứng dụng.
Tuân thủ Clean Architecture: tầng Domain/Entity.

Models:
    - LawArticle*    : Schema cho điều luật trong database
    - SearchRequest  : Request body cho API /api/retrieve
    - SearchResult   : Kết quả tìm kiếm 1 điều luật
    - SearchResponse : Response wrapper cho API /api/retrieve
    - HealthResponse : Response cho API /api/health
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


# ===========================================================
#  LAW ARTICLE SCHEMAS
# ===========================================================

class LawArticleBase(BaseModel):
    """Schema cơ bản cho một Điều luật."""
    article_id: str = Field(
        ...,
        description="Mã định danh duy nhất. VD: HP2013_D20",
        examples=["HP2013_D20", "BLDS2015_D158"]
    )
    law_code: str = Field(
        ...,
        description="Mã bộ luật. VD: HP2013, BLDS2015",
        examples=["HP2013", "BLDS2015", "BLHS2015", "LHNGD2014", "LLD2019"]
    )
    law_name: str = Field(
        ...,
        description="Tên đầy đủ của bộ luật",
        examples=["Hiến pháp 2013", "Bộ luật Dân sự 2015"]
    )
    chapter: str = Field(default="", description="Tên chương")
    section: str = Field(default="", description="Tên mục (nếu có)")
    article_number: int = Field(..., description="Số thứ tự điều", ge=1)
    title: str = Field(default="", description="Tiêu đề điều luật")
    content: str = Field(..., description="Nội dung chính của điều luật")
    full_text: str = Field(
        ...,
        description="Toàn văn điều luật (bao gồm tiêu đề + nội dung)"
    )


class LawArticleCreate(LawArticleBase):
    """Schema cho việc tạo mới điều luật (insert vào DB)."""
    effective_date: str = Field(default="", description="Ngày có hiệu lực. VD: 2014-01-01")
    source_url: str = Field(default="", description="URL nguồn crawl")
    word_count: int = Field(default=0, description="Số từ trong nội dung", ge=0)


class LawArticleInDB(LawArticleCreate):
    """Schema cho điều luật đã lưu trong DB (có id và timestamp)."""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class LawArticleSummary(BaseModel):
    """Schema rút gọn — dùng cho kết quả tìm kiếm (không cần full_text)."""
    article_id: str
    law_code: str
    law_name: str
    article_number: int
    title: str
    content: str
    word_count: int = 0


# ===========================================================
#  SEARCH / RETRIEVE SCHEMAS (API /api/retrieve)
# ===========================================================

class SearchRequest(BaseModel):
    """
    Request body cho POST /api/retrieve.

    Attributes:
        query: Câu hỏi pháp luật của người dùng (tiếng Việt).
        method: Phương pháp tìm kiếm — Phase 1 chỉ hỗ trợ "bm25".
        top_k: Số lượng kết quả trả về (default: 5, max: 20).
    """
    query: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="Câu hỏi pháp luật bằng tiếng Việt",
        examples=["Quyền bất khả xâm phạm về thân thể được quy định như thế nào?"]
    )
    method: str = Field(
        default="bm25",
        description="Phương pháp tìm kiếm: bm25 | dense | both",
        pattern="^(bm25|dense|both)$"
    )
    top_k: int = Field(
        default=5,
        description="Số kết quả trả về",
        ge=1,
        le=20
    )


class SearchResultItem(BaseModel):
    """Một kết quả tìm kiếm — điều luật + điểm relevance."""
    rank: int = Field(..., description="Thứ hạng kết quả (1-based)")
    article_id: str
    law_code: str
    law_name: str
    article_number: int
    title: str
    content: str
    score: float = Field(..., description="Điểm relevance (BM25 score)")


class SearchResponse(BaseModel):
    """Response wrapper cho POST /api/retrieve."""
    query: str
    method: str
    total_results: int
    results: list[SearchResultItem]
    search_time_ms: float = Field(
        ...,
        description="Thời gian tìm kiếm (milliseconds)"
    )


# ===========================================================
#  HEALTH CHECK SCHEMA
# ===========================================================

class HealthResponse(BaseModel):
    """Response cho GET /api/health."""
    status: str = Field(default="healthy", description="Trạng thái hệ thống")
    version: str
    environment: str
    database_connected: bool
    corpus_stats: Optional[dict] = Field(
        default=None,
        description="Thống kê corpus (nếu DB đã có dữ liệu)"
    )
    bm25_index_loaded: bool = False
    timestamp: datetime = Field(default_factory=datetime.now)


# ===========================================================
#  CORPUS STATISTICS
# ===========================================================

class CorpusStats(BaseModel):
    """Thống kê tổng quan corpus."""
    total_articles: int
    total_words: int
    laws: list[dict]
