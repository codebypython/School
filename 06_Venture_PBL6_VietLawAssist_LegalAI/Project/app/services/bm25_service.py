"""
VietLawAssist — BM25 Search Service
======================================
Agent-02 (ML Research) — Tầng 1 BM25Okapi Sparse Retrieval.

Thuật toán BM25Okapi:
    score(Q, D) = Σ IDF(qi) · [ f(qi, D) · (k1 + 1) ]
                               / [ f(qi, D) + k1 · (1 - b + b · |D| / avgdl) ]

    Trong đó:
        - f(qi, D): term frequency của query term qi trong document D
        - |D|: độ dài document D (số từ)
        - avgdl: độ dài trung bình các documents
        - k1: siêu tham số điều chỉnh mức bão hòa TF (default: 1.5)
        - b: siêu tham số cân bằng document length normalization (default: 0.75)

Vietnamese Tokenization:
    Tiếng Việt là ngôn ngữ đơn lập (isolating), từ ghép 2-3 âm tiết.
    VD: "người sử dụng lao động" → ["người_sử_dụng_lao_động"]
    Sử dụng PyVi để tách từ ghép chính xác.

Stopwords:
    Loại bỏ từ dừng tiếng Việt không mang thông tin pháp lý:
    "là", "và", "của", "có", "được", "theo", "trong", "các"...
"""

import pickle
import time
from pathlib import Path
from typing import Optional

from loguru import logger
from rank_bm25 import BM25Okapi

from app.config import get_settings


# ===========================================================
#  VIETNAMESE STOPWORDS (Pháp luật domain)
# ===========================================================
VIETNAMESE_STOPWORDS = {
    # Từ dừng chung
    "là", "và", "của", "có", "được", "theo", "trong", "các",
    "để", "cho", "với", "một", "những", "này", "đó", "đã",
    "sẽ", "đang", "không", "hoặc", "hay", "nhưng", "mà",
    "thì", "nếu", "khi", "tại", "từ", "đến", "về", "do",
    "bởi", "cũng", "như", "trên", "dưới", "sau", "trước",
    "ngoài", "giữa", "qua", "lại", "ra", "vào", "lên",
    "xuống", "rằng", "vì", "nên", "vẫn", "còn", "rồi",
    "đều", "mọi", "tất_cả", "hơn", "nhất", "rất", "quá",
    "bị", "phải", "nào", "gì", "ai", "đâu", "bao_nhiêu",
    "thế", "vậy", "đây", "kia", "ấy", "cái", "con", "người",
    # Từ dừng pháp luật (xuất hiện ở mọi điều luật)
    "điều", "khoản", "điểm", "mục", "chương",
}


class BM25SearchService:
    """
    BM25Okapi Search Engine cho Vietnamese Legal Text.

    Lifecycle:
        1. build_index(documents) → tạo BM25 index từ corpus
        2. save_index(path) → serialize index ra file pickle
        3. load_index(path) → deserialize index từ file
        4. search(query, top_k) → tìm kiếm Top-K documents

    Attributes:
        bm25: BM25Okapi index object
        documents: Danh sách document metadata (article_id, law_code, ...)
        tokenized_corpus: Corpus đã tokenize (list of list of tokens)
        is_loaded: True nếu index đã sẵn sàng cho search
    """

    def __init__(self):
        self.bm25: Optional[BM25Okapi] = None
        self.documents: list[dict] = []
        self.tokenized_corpus: list[list[str]] = []
        self.is_loaded: bool = False
        self._tokenizer_name: str = "pyvi"

    @property
    def corpus_size(self) -> int:
        """Số documents trong index."""
        return len(self.documents)

    def _tokenize_vietnamese(self, text: str) -> list[str]:
        """
        Tách từ tiếng Việt sử dụng PyVi hoặc Underthesea.

        Args:
            text: Văn bản tiếng Việt cần tách từ.

        Returns:
            List các token (từ ghép được nối bởi dấu gạch dưới).

        Example:
            >>> _tokenize_vietnamese("Người lao động có quyền nghỉ phép")
            ["người_lao_động", "quyền", "nghỉ_phép"]
        """
        settings = get_settings()
        text = text.lower().strip()

        if not text:
            return []

        try:
            if settings.tokenizer == "underthesea":
                from underthesea import word_tokenize
                segmented = word_tokenize(text)
            else:
                # Default: PyVi
                from pyvi import ViTokenizer
                segmented_text = ViTokenizer.tokenize(text)
                segmented = segmented_text.split()
        except ImportError as e:
            logger.warning(f"Tokenizer import error: {e}. Falling back to whitespace split.")
            segmented = text.split()

        # Loại bỏ stopwords và tokens quá ngắn
        tokens = [
            token.strip()
            for token in segmented
            if token.strip()
            and token.strip() not in VIETNAMESE_STOPWORDS
            and len(token.strip()) > 1
        ]

        return tokens

    def build_index(self, documents: list[dict]) -> None:
        """
        Xây dựng BM25Okapi index từ danh sách documents.

        Args:
            documents: List of dict, mỗi dict cần có:
                - article_id: str
                - law_code: str
                - law_name: str
                - article_number: int
                - title: str
                - content: str

        Flow:
            1. Tokenize toàn bộ corpus (Vietnamese word segmentation)
            2. Build BM25Okapi index với k1, b từ config
            3. Lưu metadata documents cho lookup khi search

        Raises:
            ValueError: Nếu documents rỗng.
        """
        if not documents:
            raise ValueError("Không thể build index từ corpus rỗng!")

        settings = get_settings()
        logger.info(
            f"Building BM25 index: {len(documents)} documents, "
            f"k1={settings.bm25_k1}, b={settings.bm25_b}"
        )

        start_time = time.perf_counter()

        # 1. Tokenize corpus
        self.tokenized_corpus = []
        for doc in documents:
            # Index trên cả title + content để bắt keyword ở tiêu đề
            text = f"{doc.get('title', '')} {doc['content']}"
            tokens = self._tokenize_vietnamese(text)
            self.tokenized_corpus.append(tokens)

        # 2. Build BM25 index
        self.bm25 = BM25Okapi(
            self.tokenized_corpus,
            k1=settings.bm25_k1,
            b=settings.bm25_b,
        )

        # 3. Lưu document metadata
        self.documents = documents

        self.is_loaded = True
        elapsed = time.perf_counter() - start_time

        logger.success(
            f"✅ BM25 index built: {len(documents)} docs "
            f"in {elapsed:.2f}s"
        )

    def save_index(self, path: str | None = None) -> None:
        """
        Serialize BM25 index ra file pickle.

        Args:
            path: Đường dẫn file. None = dùng config mặc định.
        """
        if not self.is_loaded:
            logger.warning("Không thể save: index chưa được build.")
            return

        if path is None:
            settings = get_settings()
            path = settings.bm25_index_path

        index_path = Path(path)
        index_path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "bm25": self.bm25,
            "documents": self.documents,
            "tokenized_corpus": self.tokenized_corpus,
        }

        with open(index_path, "wb") as f:
            pickle.dump(data, f)

        logger.info(f"BM25 index saved: {index_path}")

    def load_index(self, path: str | None = None) -> bool:
        """
        Load BM25 index từ file pickle.

        Args:
            path: Đường dẫn file. None = dùng config mặc định.

        Returns:
            True nếu load thành công, False nếu file không tồn tại.
        """
        if path is None:
            settings = get_settings()
            path = settings.bm25_index_path

        index_path = Path(path)
        if not index_path.exists():
            logger.debug(f"BM25 index file not found: {index_path}")
            return False

        try:
            with open(index_path, "rb") as f:
                data = pickle.load(f)

            self.bm25 = data["bm25"]
            self.documents = data["documents"]
            self.tokenized_corpus = data["tokenized_corpus"]
            self.is_loaded = True

            logger.info(
                f"BM25 index loaded: {len(self.documents)} docs from {index_path}"
            )
            return True

        except Exception as e:
            logger.error(f"Lỗi load BM25 index: {e}")
            self.is_loaded = False
            return False

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        """
        Tìm kiếm Top-K documents liên quan nhất cho câu hỏi.

        Args:
            query: Câu hỏi pháp luật (tiếng Việt).
            top_k: Số kết quả trả về (default: 5).

        Returns:
            List of dict, mỗi dict chứa:
                - article_id, law_code, law_name, article_number
                - title, content
                - score: BM25 relevance score

        Raises:
            RuntimeError: Nếu index chưa được build/load.

        Example:
            >>> results = bm25_service.search("Quyền bất khả xâm phạm về thân thể")
            >>> results[0]["article_id"]
            "HP2013_D20"
        """
        if not self.is_loaded or self.bm25 is None:
            raise RuntimeError(
                "BM25 index chưa sẵn sàng! "
                "Gọi build_index() hoặc load_index() trước."
            )

        # Tokenize query
        query_tokens = self._tokenize_vietnamese(query)

        if not query_tokens:
            logger.warning(f"Query tokenize ra rỗng: '{query}'")
            return []

        # BM25 scoring
        scores = self.bm25.get_scores(query_tokens)

        # Lấy Top-K indices (sắp xếp giảm dần theo score)
        top_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True,
        )[:top_k]

        # Build results
        results = []
        for idx in top_indices:
            if scores[idx] <= 0:
                continue  # Bỏ qua documents không match bất kỳ term nào

            doc = self.documents[idx]
            results.append({
                "article_id": doc.get("article_id", ""),
                "law_code": doc.get("law_code", ""),
                "law_name": doc.get("law_name", ""),
                "article_number": doc.get("article_number", 0),
                "title": doc.get("title", ""),
                "content": doc.get("content", ""),
                "score": float(scores[idx]),
            })

        return results

    def rebuild_from_db(self) -> int:
        """
        Tiện ích: Load toàn bộ corpus từ SQLite và build lại index.

        Returns:
            Số documents đã index.
        """
        from app.repositories.article_repo import ArticleRepository

        repo = ArticleRepository()
        articles = repo.get_all_for_indexing()

        if not articles:
            logger.warning("Database rỗng — không có gì để index.")
            return 0

        documents = [
            {
                "article_id": a.article_id,
                "law_code": a.law_code,
                "law_name": a.law_name,
                "article_number": a.article_number,
                "title": a.title,
                "content": a.content,
            }
            for a in articles
        ]

        self.build_index(documents)
        self.save_index()
        return len(documents)


# ===========================================================
#  SINGLETON INSTANCE
#  Import bm25_service từ module này để dùng toàn app.
# ===========================================================
bm25_service = BM25SearchService()
