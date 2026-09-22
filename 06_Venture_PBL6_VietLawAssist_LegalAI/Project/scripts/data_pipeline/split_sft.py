"""
VietLawAssist — Stratified SFT Dataset Splitting Module
======================================================
Agent-02 (ML Researcher) — Phân chia tập dữ liệu SFT 500 mẫu thành Train (80%) và Validation (20%).
Quy tắc:
    - Bắt buộc phân tầng (Stratified) theo intent_code.
    - Cố định random seed = 42 để đảm bảo tính tái lập 100%.
    - Xuất dữ liệu ra train_sft.json và val_sft.json ở cả định dạng Alpaca và ChatML.
"""

import json
from pathlib import Path
from typing import Optional
from sklearn.model_selection import train_test_split
from loguru import logger

from .config import PROCESSED_DIR
from .sft_builder import convert_to_chatml


def split_sft_stratified(
    input_file: Optional[Path] = None,
    train_output: Optional[Path] = None,
    val_output: Optional[Path] = None,
    val_ratio: float = 0.2,
    seed: int = 42,
) -> tuple[list[dict], list[dict]]:
    """
    Phân chia tập SFT thành Train / Val có phân tầng theo intent_code.
    """
    if input_file is None:
        input_file = PROCESSED_DIR / "sft_vietlaw_500.json"
    if train_output is None:
        train_output = PROCESSED_DIR / "train_sft.json"
    if val_output is None:
        val_output = PROCESSED_DIR / "val_sft.json"

    if not input_file.exists():
        raise FileNotFoundError(f"Không tìm thấy tập dữ liệu SFT nguồn tại: {input_file}")

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if len(data) < 2:
        logger.warning(f"Tập dữ liệu chỉ có {len(data)} mẫu, sao chép sang cả train và val.")
        train_data, val_data = data, data
    else:
        # Nhãn phân tầng
        labels = [item.get("intent_code", "UNKNOWN") for item in data]
        
        # Nếu có nhãn chỉ xuất hiện 1 lần, train_test_split sẽ báo lỗi -> xử lý fallback
        from collections import Counter
        counts = Counter(labels)
        singletons = [k for k, v in counts.items() if v < 2]
        if singletons:
            logger.warning(f"Có nhãn chỉ có 1 mẫu ({singletons}), sử dụng random split thay vì stratified.")
            train_data, val_data = train_test_split(data, test_size=val_ratio, random_state=seed, shuffle=True)
        else:
            train_data, val_data = train_test_split(
                data,
                test_size=val_ratio,
                random_state=seed,
                stratify=labels,
                shuffle=True,
            )

    # Lưu định dạng chuẩn Alpaca
    train_output.parent.mkdir(parents=True, exist_ok=True)
    with open(train_output, "w", encoding="utf-8") as f:
        json.dump(train_data, f, ensure_ascii=False, indent=2)

    with open(val_output, "w", encoding="utf-8") as f:
        json.dump(val_data, f, ensure_ascii=False, indent=2)

    # Lưu thêm phiên bản ChatML (messages format)
    chatml_train_path = PROCESSED_DIR / "train_sft_chatml.json"
    chatml_val_path = PROCESSED_DIR / "val_sft_chatml.json"
    
    with open(chatml_train_path, "w", encoding="utf-8") as f:
        json.dump([convert_to_chatml(x) for x in train_data], f, ensure_ascii=False, indent=2)

    with open(chatml_val_path, "w", encoding="utf-8") as f:
        json.dump([convert_to_chatml(x) for x in val_data], f, ensure_ascii=False, indent=2)

    logger.success(
        f"Phân chia SFT thành công!\n"
        f"  - Train Set: {len(train_data)} mẫu -> {train_output.name} & {chatml_train_path.name}\n"
        f"  - Val Set  : {len(val_data)} mẫu -> {val_output.name} & {chatml_val_path.name}"
    )

    return train_data, val_data
