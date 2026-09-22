"""
VietLawAssist — Kaggle Dataset Packaging & Sync Module
======================================================
Agent-03 (Data Engineer) — Đóng gói và đồng bộ kho dữ liệu hoàn chỉnh lên Kaggle Datasets.
Cung cấp:
    - Tạo cấu trúc thư mục kaggle_bundle chuẩn hóa
    - Tự động sinh dataset-metadata.json định danh dataset
    - Kiểm tra Checksum MD5 xác nhận tính toàn vẹn của các tệp tin trước khi tải lên
    - Tương tác với Kaggle CLI để tự động đẩy phiên bản mới (Zero-click versioning)
"""

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional
from loguru import logger

from .config import (
    DATA_DIR,
    KAGGLE_BUNDLE_DIR,
    PROCESSED_DIR,
    RAW_DIR,
    SAMPLE_DIR,
)


def compute_md5(file_path: Path) -> str:
    """Tính toán mã băm MD5 của tệp tin để xác thực tính toàn vẹn."""
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def prepare_kaggle_bundle(
    kaggle_username: str = "vietlawassist",
    dataset_slug: str = "vietlawassist-pbl6-legal-ai",
) -> Path:
    """
    Tập hợp tất cả các thành phần dữ liệu cốt lõi vào thư mục đệm data/kaggle_bundle/.
    """
    KAGGLE_BUNDLE_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Tạo dataset-metadata.json
    metadata = {
        "title": "VietLawAssist PBL6 Legal AI Dataset",
        "id": f"{kaggle_username}/{dataset_slug}",
        "licenses": [{"name": "CC0-1.0"}],
        "description": "Kho dữ liệu Pháp luật Đại cương phục vụ huấn luyện RAG 4 tầng và fine-tuning LoRA tại ĐHBK Đà Nẵng (DUT).",
    }
    meta_path = KAGGLE_BUNDLE_DIR / "dataset-metadata.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    # 2. Danh sách tệp cần sao chép vào bundle
    files_to_pack = [
        (RAW_DIR / "corpus_combined.json", KAGGLE_BUNDLE_DIR / "corpus_combined.json"),
        (SAMPLE_DIR / "textbook_principles.json", KAGGLE_BUNDLE_DIR / "textbook_principles.json"),
        (PROCESSED_DIR / "train_sft.json", KAGGLE_BUNDLE_DIR / "train_sft.json"),
        (PROCESSED_DIR / "val_sft.json", KAGGLE_BUNDLE_DIR / "val_sft.json"),
        (PROCESSED_DIR / "train_sft_chatml.json", KAGGLE_BUNDLE_DIR / "train_sft_chatml.json"),
        (SAMPLE_DIR / "eval_queries.json", KAGGLE_BUNDLE_DIR / "eval_benchmark.json"),
    ]

    packed_info = []
    for src, dst in files_to_pack:
        if src.exists():
            shutil.copy2(src, dst)
            md5_hash = compute_md5(dst)
            size_kb = dst.stat().st_size / 1024
            packed_info.append({
                "file": dst.name,
                "size_kb": f"{size_kb:.1f} KB",
                "md5": md5_hash,
            })
        else:
            logger.warning(f"Chưa tìm thấy tệp nguồn để đóng gói: {src.name}")

    # 3. Xuất báo cáo đóng gói
    logger.info("=== BÁO CÁO ĐÓNG GÓI KAGGLE BUNDLE ===")
    logger.info(f"Vị trí thư mục: {KAGGLE_BUNDLE_DIR}")
    for item in packed_info:
        logger.info(f"  - [{item['file']:25s}]: {item['size_kb']:>10s} | MD5: {item['md5']}")

    logger.success(f"Đã đóng gói thành công {len(packed_info)} tệp dữ liệu sẵn sàng cho Kaggle!")
    return KAGGLE_BUNDLE_DIR


def upload_to_kaggle(message: str = "Update dataset version"):
    """
    Tải hoặc cập nhật phiên bản Dataset lên Kaggle qua Kaggle CLI.
    """
    meta_path = KAGGLE_BUNDLE_DIR / "dataset-metadata.json"
    if not meta_path.exists():
        logger.error("Chưa có dataset-metadata.json. Hãy chạy prepare_kaggle_bundle() trước!")
        return

    # Kiểm tra xem kaggle CLI đã có chưa
    kaggle_cmd = shutil.which("kaggle") or (Path(sys.prefix) / "Scripts" / "kaggle.exe")
    if not Path(kaggle_cmd).exists() and not shutil.which("kaggle"):
        logger.error("Không tìm thấy lệnh 'kaggle'. Hãy cài đặt bằng: pip install kaggle")
        return

    logger.info(f"Đang đồng bộ phiên bản mới lên Kaggle với ghi chú: '{message}'...")
    cmd = [str(kaggle_cmd), "datasets", "version", "-p", str(KAGGLE_BUNDLE_DIR), "-m", message]

    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        logger.success("✅ Đã cập nhật phiên bản thành công lên Kaggle!")
        print(res.stdout)
    except subprocess.CalledProcessError as e:
        logger.warning(f"Lệnh update trả về lỗi ({e.stderr.strip()}). Thử tạo mới (datasets create)...")
        create_cmd = [str(kaggle_cmd), "datasets", "create", "-p", str(KAGGLE_BUNDLE_DIR), "--public"]
        try:
            res_create = subprocess.run(create_cmd, capture_output=True, text=True, check=True)
            logger.success("✅ Đã tạo mới Dataset thành công trên Kaggle!")
            print(res_create.stdout)
        except Exception as ex:
            logger.error(f"Thao tác đẩy lên Kaggle thất bại: {ex}")
