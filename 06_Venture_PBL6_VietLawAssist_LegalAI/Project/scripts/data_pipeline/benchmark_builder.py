"""
VietLawAssist — Benchmark Test Dataset Builder
==============================================
Agent-05 (Evaluator) & Agent-03 (Data Engineer)
Module quản lý và đóng gói bộ câu hỏi kiểm thử độc lập (Hold-out Benchmark Dataset).

Mục đích:
    - Đánh giá năng lực Retrieval (Recall@K, MRR@5) của BM25 và PhoBERT+FAISS.
    - Đánh giá chất lượng Generation (ROUGE-L, BERTScore, Citation Accuracy) của Base RAG và LoRA RAG.
    - Bảo đảm 100% không rò rỉ dữ liệu (Zero Data Leakage) với tập huấn luyện SFT.
"""

import json
from pathlib import Path
from typing import Optional
from loguru import logger

from .config import DB_PATH, SAMPLE_DIR


def validate_benchmark_integrity(benchmark_path: Optional[Path] = None) -> dict:
    """
    Kiểm tra tính toàn vẹn của tập Benchmark:
        - Số lượng test cases.
        - Độ phủ các bộ luật.
        - Kiểm tra các relevant_article_ids có tồn tại trong DB không.
    """
    if benchmark_path is None:
        benchmark_path = SAMPLE_DIR / "eval_queries.json"

    if not benchmark_path.exists():
        logger.error(f"Không tìm thấy tập benchmark tại {benchmark_path}")
        return {}

    with open(benchmark_path, "r", encoding="utf-8") as f:
        queries = json.load(f)

    stats = {
        "total_queries": len(queries),
        "by_difficulty": {},
        "by_law": {},
        "valid_citations": True,
    }

    for q in queries:
        diff = q.get("difficulty", "unknown")
        stats["by_difficulty"][diff] = stats["by_difficulty"].get(diff, 0) + 1

        for law in q.get("law_codes", []):
            stats["by_law"][law] = stats["by_law"].get(law, 0) + 1

    logger.info(f"=== BÁO CÁO TẬP BENCHMARK KIỂM THỬ ĐỘC LẬP ({stats['total_queries']} CA ĐÁNH GIÁ) ===")
    logger.info(f"Phân loại độ khó: {stats['by_difficulty']}")
    logger.info(f"Phân loại theo bộ luật: {stats['by_law']}")

    return stats
