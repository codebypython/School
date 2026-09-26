"""
VietLawAssist — SFT Master Dataset Curator (sft_curator.py)
===========================================================
Agent-02 (ML Researcher) & Agent-03 (Data Engineer)
Module tổng hợp, khử trùng lặp và làm giàu tập dữ liệu huấn luyện SFT 500 mẫu.

Quy trình:
    1. Hòa trộn Golden Seeds + Synthetic Cases + Crawled Exam Cases
    2. Khử trùng lặp nội dung (Deduplication) dựa trên chuẩn hóa chuỗi câu hỏi
    3. Chạy Citation Guardrail đối soát trực tiếp với SQLite law_corpus.db
    4. Cân bằng tỷ lệ mẫu (Stratified Class Balancing)
    5. Xuất bản đồng thời: sft_vietlaw_500.json, train/val Alpaca, train/val ChatML
"""

import json
import hashlib
from pathlib import Path
from typing import Optional
from loguru import logger

from .config import DB_PATH, PROCESSED_DIR
from .exam_crawler import scan_and_harvest_local_exams
from .sft_builder import generate_seed_templates, validate_sft_sample, get_existing_db_article_ids
from .split_sft import split_sft_stratified
from .synthetic_engine import LegalSyntheticEngine


def normalize_query_for_dedup(text: str) -> str:
    """Chuẩn hóa câu hỏi để tạo hash so khớp trùng lặp nội dung."""
    text = text.lower().strip()
    # Loại bỏ các từ tiền tố thường gặp
    for prefix in ["tình huống:", "câu hỏi:", "khẳng định:", "bài tập:"]:
        if text.startswith(prefix):
            text = text[len(prefix):].strip()
    return "".join(text.split())


def curate_and_build_sft_dataset(
    target_count: int = 500,
    output_path: Optional[Path] = None,
    samples_per_category: int = 25,
) -> list[dict]:
    """
    Quy trình tích hợp tổng hợp dữ liệu huấn luyện SFT quy mô lớn.
    """
    if output_path is None:
        output_path = PROCESSED_DIR / "sft_vietlaw_500.json"

    logger.info("=== BẮT ĐẦU QUY TRÌNH HỢP NHẤT & LÀM GIÀU DATASET SFT ===")

    # 1. Nạp Golden Seeds
    seeds = generate_seed_templates()
    logger.info(f"Nạp {len(seeds)} Golden Seeds gốc.")

    # 2. Sinh dữ liệu từ Synthetic Engine
    engine = LegalSyntheticEngine(seed=42)
    synthetic_cases = engine.build_full_synthetic_dataset(target_total=target_count)
    logger.info(f"Sinh {len(synthetic_cases)} mẫu tổng hợp chuẩn barem.")

    # 3. Thu hoạch từ kho đề thi thực tế (nếu có)
    crawled_cases = scan_and_harvest_local_exams()
    valid_crawled = [c for c in crawled_cases if c.get("has_answer") and c.get("output")]
    logger.info(f"Thu hoạch {len(valid_crawled)} câu hỏi đề thi thực tế có lời giải.")

    # 4. Hợp nhất và Khử trùng lặp (Deduplication)
    combined = seeds + synthetic_cases + valid_crawled
    seen_hashes = set()
    deduped = []

    for item in combined:
        norm_q = normalize_query_for_dedup(item.get("input", ""))
        q_hash = hashlib.md5(norm_q.encode("utf-8")).hexdigest()
        if q_hash not in seen_hashes:
            seen_hashes.add(q_hash)
            deduped.append(item)

    logger.info(f"Sau khi khử trùng lặp: còn lại {len(deduped)} / {len(combined)} mẫu.")

    # 5. Citation Guardrail Validation
    valid_article_ids = get_existing_db_article_ids()
    approved_samples = []
    rejected_count = 0

    for idx, item in enumerate(deduped, 1):
        item["sample_id"] = f"SFT_{item['intent_code'][:6]}_{idx:03d}"
        errors = validate_sft_sample(item, valid_article_ids)
        if not errors:
            approved_samples.append(item)
        else:
            rejected_count += 1
            logger.warning(f"Từ chối mẫu {item.get('sample_id')}: {errors}")

    logger.success(f"Citation Guardrail: Phê duyệt {len(approved_samples)} mẫu | Loại bỏ {rejected_count} mẫu lỗi.")

    # 6. Lưu tệp chính sft_vietlaw_500.json
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(approved_samples, f, ensure_ascii=False, indent=2)

    logger.success(f"Đã lưu tập SFT đầy đủ tại: {output_path} ({len(approved_samples)} mẫu)")

    # 7. Tự động kích hoạt phân tầng Train/Val
    split_sft_stratified(input_file=output_path)

    return approved_samples
