"""
VietLawAssist — Exam & Answer Pairing Engine (exam_pairer.py)
============================================================
Agent-03 (Data Engineer) & Agent-02 (ML Researcher)
Module tự động đồng bộ và ghép nối câu hỏi & đáp án khi:
    1. Đề thi và Đáp án nằm ở 2 file rời rạc riêng biệt (ví dụ: de_thi.txt và dap_an.txt).
    2. Đề thi và Đáp án nằm chung 1 file nhưng ở 2 phần tách biệt (Phần I: Đề, Phần II: Đáp án).
    3. Chuẩn hóa về format 2 mốc neo ("Câu X:" và "Đáp án:") đưa thẳng vào data/raw/exams/.
"""

import re
from pathlib import Path
from typing import Optional, Union
from loguru import logger

from scripts.clean_text import clean_full_pipeline
from .config import RAW_DIR

RAW_EXAMS_DIR = RAW_DIR / "exams"
RAW_EXAMS_DIR.mkdir(parents=True, exist_ok=True)


def parse_numbered_blocks(text: str) -> dict[int, str]:
    """
    Bóc tách văn bản thành từ điển {số_thứ_tự_câu: nội_dung}.
    Hỗ trợ nhận diện chính xác các mốc bắt đầu câu hỏi lớn:
        - "Câu 1:", "Câu 1.", "Câu 1 -"
        - "Bài 1:", "Bài tập 1:", "Tình huống 1:"
        - "Câu hỏi 1:"
    Tránh cắt nhầm các ý gạch đầu dòng con bên trong như:
        - "1. Kết luận:", "2. Giải thích:"
        - "Bước 1:", "Bước 2:"
    """
    cleaned = clean_full_pipeline(text)
    
    # Pattern chỉ bắt các câu hỏi lớn có từ khóa nhận diện rõ ràng
    pattern = re.compile(
        r"(?:^|\n)\s*(?:Câu|Bài|Bài tập|Tình huống|Câu hỏi)\s+(\d+)[\.:\s\-]+(.*?)(?=(?:\n\s*(?:Câu|Bài|Bài tập|Tình huống|Câu hỏi)\s+\d+[\.:\s\-]|\Z))",
        re.DOTALL | re.IGNORECASE
    )

    matches = pattern.findall(cleaned)
    blocks = {}

    for num_str, content in matches:
        try:
            q_num = int(num_str)
            blocks[q_num] = content.strip()
        except ValueError:
            continue

    # Fallback: Nếu không có từ "Câu/Bài" nào, mới tìm kiếm các số thứ tự ở đầu dòng dạng: [1], (1), 1.
    if not blocks:
        fallback_pattern = re.compile(
            r"(?:^|\n)\s*(?:\[(\d+)\]|\((\d+)\)|(\d+)\.)\s+(.*?)(?=(?:\n\s*(?:\[\d+\]|\(\d+\)|\d+\.)\s+|\Z))",
            re.DOTALL
        )
        for g1, g2, g3, content in fallback_pattern.findall(cleaned):
            n_str = g1 or g2 or g3
            try:
                blocks[int(n_str)] = content.strip()
            except ValueError:
                continue

    return blocks


def pair_separate_exam_and_answer_files(
    question_file: Union[str, Path],
    answer_file: Union[str, Path],
    output_file: Optional[Union[str, Path]] = None
) -> Path:
    """
    Ghép nối 2 file rời rạc (File Đề bài và File Đáp án) thành 1 file hoàn chỉnh chuẩn barem.
    Tự động so khớp theo số thứ tự câu (Câu 1 ghép với Đáp án 1, Câu 2 ghép với Đáp án 2...).
    """
    q_path = Path(question_file)
    a_path = Path(answer_file)

    if not q_path.exists():
        logger.error(f"Không tìm thấy file đề: {q_path}")
        return None
    if not a_path.exists():
        logger.error(f"Không tìm thấy file đáp án: {a_path}")
        return None

    q_text = q_path.read_text(encoding="utf-8")
    a_text = a_path.read_text(encoding="utf-8")

    q_blocks = parse_numbered_blocks(q_text)
    a_blocks = parse_numbered_blocks(a_text)

    logger.info(f"Đã phát hiện: {len(q_blocks)} câu hỏi trong đề | {len(a_blocks)} lời giải trong đáp án.")

    paired_entries = []
    all_numbers = sorted(list(set(q_blocks.keys()) | set(a_blocks.keys())))

    for num in all_numbers:
        q_content = q_blocks.get(num, "").strip()
        a_content = a_blocks.get(num, "").strip()

        if q_content and a_content:
            entry = f"Câu {num}: {q_content}\n\nĐáp án:\n{a_content}"
            paired_entries.append(entry)
        elif q_content and not a_content:
            logger.warning(f"Câu {num} có đề bài nhưng thiếu đáp án tương ứng.")
            entry = f"Câu {num}: {q_content}\n\nĐáp án:\n(Chưa có đáp án)"
            paired_entries.append(entry)
        elif not q_content and a_content:
            logger.warning(f"Đáp án câu {num} tồn tại nhưng không tìm thấy đề bài.")

    full_paired_text = "\n\n" + ("=" * 50) + "\n\n".join(paired_entries)

    if not output_file:
        output_file = RAW_EXAMS_DIR / f"{q_path.stem}_paired.txt"
    else:
        output_file = Path(output_file)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(full_paired_text, encoding="utf-8")

    logger.success(f"Đã ghép thành công {len(paired_entries)} cặp Q&A vào: {output_file.name}")
    return output_file


def pair_split_sections_in_single_file(
    input_file: Union[str, Path],
    output_file: Optional[Union[str, Path]] = None
) -> Path:
    """
    Xử lý trường hợp 1 file duy nhất nhưng chia thành 2 phần:
        PHẦN I: ĐỀ BÀI (Câu 1, 2, 3...)
        PHẦN II: ĐÁP ÁN (Câu 1, 2, 3...)
    Tự động tách 2 phần và ghép đôi từng câu lại với nhau.
    """
    in_path = Path(input_file)
    if not in_path.exists():
        logger.error(f"Không tìm thấy file: {in_path}")
        return None

    content = in_path.read_text(encoding="utf-8")

    # Tìm ranh giới giữa phần đề và phần đáp án
    split_pattern = re.compile(
        r"(?:\n|\A)(?:\={3,}|\-{3,})?\s*(?:PHẦN\s*(?:II|2)|ĐÁP\s*ÁN|HƯỚNG\s*DẪN\s*CHẤM|LỜI\s*GIẢI)\s*[\:\-]*(?:\={3,}|\-{3,})?\n",
        re.IGNORECASE
    )

    parts = split_pattern.split(content, maxsplit=1)
    if len(parts) < 2:
        logger.info(f"File {in_path.name} không có phân tách 2 phần Đề/Đáp án lớn. Giữ nguyên.")
        return in_path

    q_section = parts[0]
    a_section = parts[1]

    q_blocks = parse_numbered_blocks(q_section)
    a_blocks = parse_numbered_blocks(a_section)

    logger.info(f"Phân tách 2 phần thành công: {len(q_blocks)} câu hỏi | {len(a_blocks)} câu đáp án.")

    paired_entries = []
    all_numbers = sorted(list(set(q_blocks.keys()) | set(a_blocks.keys())))

    for num in all_numbers:
        q_content = q_blocks.get(num, "").strip()
        a_content = a_blocks.get(num, "").strip()

        if q_content and a_content:
            entry = f"Câu {num}: {q_content}\n\nĐáp án:\n{a_content}"
            paired_entries.append(entry)

    full_paired_text = "\n\n" + ("\n\n" + "=" * 50 + "\n\n").join(paired_entries)

    if not output_file:
        output_file = RAW_EXAMS_DIR / f"{in_path.stem}_normalized.txt"
    else:
        output_file = Path(output_file)

    output_file.write_text(full_paired_text, encoding="utf-8")
    logger.success(f"Đã chuẩn hóa file 2 phần thành file Q&A xen kẽ tại: {output_file.name}")
    return output_file
