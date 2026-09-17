"""
VietLawAssist — Models Package
"""

from app.models.law_article import (
    LawArticleBase,
    LawArticleCreate,
    LawArticleInDB,
    LawArticleSummary,
    SearchRequest,
    SearchResultItem,
    SearchResponse,
    HealthResponse,
    CorpusStats,
)
from app.models.textbook_principle import (
    TextbookPrincipleBase,
    TextbookPrincipleCreate,
    TextbookPrincipleInDB,
)

__all__ = [
    "LawArticleBase",
    "LawArticleCreate",
    "LawArticleInDB",
    "LawArticleSummary",
    "SearchRequest",
    "SearchResultItem",
    "SearchResponse",
    "HealthResponse",
    "CorpusStats",
    "TextbookPrincipleBase",
    "TextbookPrincipleCreate",
    "TextbookPrincipleInDB",
]
