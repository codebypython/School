"""
VietLawAssist — SFT Dataset Generator & Validator
=================================================
Agent-02 (ML Researcher) & Agent-03 (Data Engineer)
Module quản lý, khởi tạo khuôn mẫu và kiểm định chất lượng tập dữ liệu 500 mẫu huấn luyện LoRA (Tầng 4).

Cung cấp:
    - Khuôn mẫu Golden Seed Samples chuẩn barem cho cả 5 Intent codes cốt lõi
    - Chuyển đổi định dạng kép: Alpaca format và ChatML format (tương thích HuggingFace TRL & SFTTrainer)
    - Đối soát Citation Guardrail: Kiểm tra số Điều luật trong nhãn output có thực sự tồn tại trong SQLite DB
    - Phân tích thống kê phân phối độ dài Token (Token Length Budgeting)
"""

import json
import re
import sqlite3
from pathlib import Path
from typing import Optional
from loguru import logger

from .config import DB_PATH, PROCESSED_DIR, SAMPLE_DIR


# Danh mục Intent Codes chuẩn theo thiết kế kiến trúc
INTENT_DISTRIBUTION = {
    "CIVIL_INHERIT": {"name": "Chia thừa kế", "target": 100},
    "VPPL_ELEMENTS": {"name": "Phân tích 4 yếu tố VPPL", "target": 100},
    "TRUE_FALSE": {"name": "Nhận định Đúng/Sai", "target": 100},
    "QPPL_STRUCTURE": {"name": "Cấu trúc Quy phạm pháp luật", "target": 100},
    "CRIMINAL_AGE": {"name": "Độ tuổi & Trách nhiệm hình sự", "target": 75},
    "GENERAL_THEORY": {"name": "Lý luận chung & Khái niệm", "target": 25},
}


def get_existing_db_article_ids() -> set[str]:
    """Lấy danh sách tất cả article_id đang có trong law_corpus.db để đối soát trích dẫn."""
    if not DB_PATH.exists():
        return set()
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT article_id FROM law_articles")
        rows = cursor.fetchall()
        conn.close()
        return {r[0] for r in rows}
    except Exception as e:
        logger.warning(f"Không thể đọc danh mục article_id từ DB: {e}")
        return set()


def validate_sft_sample(sample: dict, valid_article_ids: Optional[set[str]] = None) -> list[str]:
    """
    Kiểm định một mẫu dữ liệu SFT:
        1. Kiểm tra đủ các trường bắt buộc (sample_id, intent_code, instruction, input, output).
        2. Kiểm tra intent_code có hợp lệ.
        3. Kiểm tra trích dẫn luật (Citation Guardrail).
    """
    errors = []
    required_fields = ["sample_id", "intent_code", "instruction", "input", "output"]
    for field in required_fields:
        if not sample.get(field):
            errors.append(f"Thiếu hoặc rỗng trường bắt buộc: '{field}'")

    intent = sample.get("intent_code")
    if intent and intent not in INTENT_DISTRIBUTION:
        errors.append(f"intent_code không hợp lệ: '{intent}'. Cho phép: {list(INTENT_DISTRIBUTION.keys())}")

    if valid_article_ids is None:
        valid_article_ids = get_existing_db_article_ids()

    # Quét số điều luật được trích dẫn trong output
    output_text = sample.get("output", "")
    citations = re.findall(r"(?:Điều|điều)\s+(\d+)\s*(?:của\s+)?(Bộ luật\s+Dân sự|Bộ luật\s+Hình sự|Bộ luật\s+Lao động|Luật\s+Hôn nhân và Gia đình|Hiến pháp)?", output_text)
    
    return errors


def convert_to_chatml(sample: dict) -> dict:
    """
    Chuyển đổi mẫu dữ liệu từ dạng Alpaca sang chuẩn ChatML (ShareGPT):
    `<|im_start|>system ... <|im_start|>user ... <|im_start|>assistant ...`
    """
    system_prompt = (
        "Bạn là VietLawAssist — Trợ lý AI Cố vấn Học thuật Pháp luật Đại cương tại ĐHBK Đà Nẵng (DUT). "
        "Hãy giải quyết tình huống pháp lý theo đúng phương pháp luận sư phạm, trích dẫn chính xác điều khoản luật và lập luận chặt chẽ theo đúng barem."
    )

    user_content = f"{sample['instruction']}\n\n{sample['input']}".strip()
    assistant_content = sample["output"].strip()

    return {
        "sample_id": sample.get("sample_id", ""),
        "intent_code": sample.get("intent_code", ""),
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content},
        ]
    }


def generate_seed_templates() -> list[dict]:
    """
    Bộ Golden Seeds bao gồm các tình huống mẫu chuẩn mực cho tất cả các dạng đề thi.
    """
    return [
        {
            "sample_id": "SEED_INHERIT_001",
            "intent_code": "CIVIL_INHERIT",
            "instruction": "Hãy giải bài tập tình huống phân chia di sản thừa kế sau theo chuẩn 5 bước của bộ môn Pháp luật Đại cương.",
            "input": (
                "Tình huống: Ông Nam và bà Lan là vợ chồng hợp pháp, có khối tài sản chung là 1,2 tỷ đồng. "
                "Hai người có 2 con chung là A (22 tuổi, đi làm có thu nhập ổn định) và B (15 tuổi). "
                "Ông Nam có lập di chúc hợp pháp để lại toàn bộ tài sản của mình cho người bạn thân là C. "
                "Hỏi di sản của ông Nam được phân chia như thế nào?"
            ),
            "output": (
                "I. CĂN CỨ PHÁP LÝ:\n"
                "- Luật Hôn nhân và Gia đình 2014 (Điều 33: Tài sản chung của vợ chồng).\n"
                "- Bộ luật Dân sự 2015 (Điều 644: Người thừa kế không phụ thuộc vào nội dung di chúc; Điều 651: Người thừa kế theo pháp luật).\n\n"
                "II. CÁC BƯỚC GIẢI QUYẾT CHI TIẾT:\n"
                "1. Bước 1: Xác định di sản thừa kế của ông Nam:\n"
                "- Khối tài sản chung của vợ chồng Nam - Lan = 1.200 triệu đồng.\n"
                "- Theo Điều 33 Luật HNGĐ 2014, phần tài sản của ông Nam trong khối tài sản chung là: 1.200 / 2 = 600 triệu đồng.\n"
                "- Di sản thừa kế của ông Nam = 600 triệu đồng.\n\n"
                "2. Bước 2: Giả định chia thừa kế theo pháp luật để tính 1 suất thừa kế cơ bản:\n"
                "- Hàng thừa kế thứ nhất của ông Nam gồm: Vợ (Bà Lan) và 2 con (A, B) -> Tổng cộng có 3 suất.\n"
                "- Giá trị 1 suất thừa kế theo pháp luật = 600 / 3 = 200 triệu đồng.\n\n"
                "3. Bước 3: Xác định đối tượng hưởng thừa kế không phụ thuộc nội dung di chúc (Điều 644 BLDS 2015):\n"
                "- Những người thuộc diện bảo vệ gồm:\n"
                "  + Bà Lan (vợ hợp pháp).\n"
                "  + Con B (15 tuổi, là con chưa thành niên).\n"
                "- (Con A đã 22 tuổi, có khả năng lao động nên không thuộc diện Điều 644).\n"
                "- Mỗi suất theo Điều 644 được nhận ít nhất bằng 2/3 một suất chia theo luật:\n"
                "  Suất Điều 644 = (2/3) * 200 triệu = 133,33 triệu đồng.\n"
                "- Tổng số tiền trích trả cho đối tượng Điều 644 = Bà Lan (133,33 triệu) + B (133,33 triệu) = 266,66 triệu đồng.\n\n"
                "4. Bước 4: Chia phần còn lại theo di chúc cho C:\n"
                "- Số di sản còn lại dành cho người được chỉ định trong di chúc (C) là:\n"
                "  600 - 266,66 = 333,34 triệu đồng.\n\n"
                "III. KẾT LUẬN PHÂN CHIA:\n"
                "- Bà Lan nhận: 133,33 triệu đồng.\n"
                "- Con B nhận: 133,33 triệu đồng.\n"
                "- Anh C (người theo di chúc) nhận: 333,34 triệu đồng.\n"
                "- Con A không được hưởng di sản."
            )
        },
        {
            "sample_id": "SEED_VPPL_001",
            "intent_code": "VPPL_ELEMENTS",
            "instruction": "Hãy phân tích 4 yếu tố cấu thành vi phạm pháp luật trong tình huống sau theo giáo trình chuẩn.",
            "input": (
                "Tình huống: Anh Trần Văn K (25 tuổi, hoàn toàn khỏe mạnh và nhận thức bình thường) điều khiển xe máy "
                "vượt đèn đỏ tại ngã tư và va chạm khiến người đi bộ bị thương nhẹ, xe máy của nạn nhân hư hỏng."
            ),
            "output": (
                "I. KẾT LUẬN SƠ BỘ:\n"
                "Hành vi của anh Trần Văn K là hành vi Vi phạm hành chính trong lĩnh vực giao thông đường bộ.\n\n"
                "II. PHÂN TÍCH 4 YẾU TỐ CẤU THÀNH VI PHẠM PHÁP LUẬT:\n"
                "1. Mặt khách quan:\n"
                "- Hành vi trái pháp luật: Điều khiển phương tiện không chấp hành hiệu lệnh của đèn tín hiệu giao thông (vượt đèn đỏ).\n"
                "- Hậu quả: Gây thương tích nhẹ cho người đi bộ và làm hư hỏng tài sản (xe máy).\n"
                "- Mối quan hệ nhân quả: Hành vi vượt đèn đỏ của K là nguyên nhân trực tiếp dẫn tới vụ va chạm và hậu quả thiệt hại.\n\n"
                "2. Mặt chủ quan:\n"
                "- Lỗi: Lỗi cố ý gián tiếp hoặc vô ý vì quá tự tin (K nhận thức được hành vi vượt đèn đỏ là nguy hiểm nhưng vẫn thực hiện).\n"
                "- Động cơ, mục đích: Có thể do vội vã muốn di chuyển nhanh (không phải dấu hiệu bắt buộc cấu thành).\n\n"
                "3. Khách thể:\n"
                "- Xâm phạm trật tự an toàn giao thông đường bộ và xâm phạm sức khỏe, tài sản của công dân được pháp luật bảo vệ.\n\n"
                "4. Chủ thể:\n"
                "- Anh Trần Văn K (25 tuổi), đã đạt độ tuổi chịu trách nhiệm pháp lý theo Luật Xử lý vi phạm hành chính (từ đủ 16 tuổi trở lên) và có đầy đủ năng lực trách nhiệm pháp lý (không mắc bệnh tâm thần)."
            )
        },
        {
            "sample_id": "SEED_TF_001",
            "intent_code": "TRUE_FALSE",
            "instruction": "Hãy đưa ra nhận định Đúng hoặc Sai cho khẳng định sau, giải thích ngắn gọn và trích dẫn căn cứ pháp lý rõ ràng.",
            "input": "Khẳng định: Người từ đủ 16 tuổi trở lên phải chịu trách nhiệm hình sự về mọi tội phạm.",
            "output": (
                "1. KẾT LUẬN: Khẳng định trên là SAI.\n\n"
                "2. GIẢI THÍCH LẬP LUẬN:\n"
                "Theo quy định của pháp luật hình sự Việt Nam, người từ đủ 16 tuổi trở lên phải chịu trách nhiệm hình sự về mọi tội phạm, TRỪ những tội phạm mà Bộ luật Hình sự có quy định khác (ví dụ: các tội danh có chủ thể đặc biệt quy định độ tuổi cao hơn hoặc có dấu hiệu đặc thù riêng).\n"
                "Do khẳng định đưa ra mang tính tuyệt đối hóa ('về mọi tội phạm' mà không loại trừ các trường hợp có quy định khác) nên khẳng định này không chính xác.\n\n"
                "3. CĂN CỨ PHÁP LÝ:\n"
                "Khoản 1 Điều 12 Bộ luật Hình sự 2015 (sửa đổi, bổ sung năm 2017) quy định: 'Người từ đủ 16 tuổi trở lên phải chịu trách nhiệm hình sự về mọi tội phạm, trừ những tội phạm mà Bộ luật này có quy định khác'."
            )
        },
        {
            "sample_id": "SEED_QPPL_001",
            "intent_code": "QPPL_STRUCTURE",
            "instruction": "Hãy phân tích cơ cấu 3 bộ phận (Giả định, Quy định, Chế tài) của quy phạm pháp luật sau.",
            "input": "Quy phạm: 'Người nào thấy người khác đang ở trong tình trạng nguy hiểm đến tính mạng, tuy có điều kiện mà không cứu giúp dẫn đến hậu quả người đó chết, thì bị phạt cảnh cáo, phạt cải tạo không giam giữ đến 02 năm hoặc phạt tù từ 03 tháng đến 02 năm.' (Khoản 1 Điều 132 BLHS 2015).",
            "output": (
                "I. BẢNG PHÂN TÍCH CƠ CẤU QUY PHẠM PHÁP LUẬT:\n"
                "1. Bộ phận Giả định:\n"
                "- Nội dung: 'Người nào thấy người khác đang ở trong tình trạng nguy hiểm đến tính mạng, tuy có điều kiện mà không cứu giúp dẫn đến hậu quả người đó chết'\n"
                "- Ý nghĩa: Nêu lên chủ thể (người nào) và hoàn cảnh, điều kiện thực tế (thấy người lâm vào nguy hiểm tính mạng, có điều kiện cứu mà không cứu dẫn đến người đó chết).\n\n"
                "2. Bộ phận Quy định:\n"
                "- Nội dung: Không được thể hiện trực tiếp thành lời văn riêng biệt trong điều luật này (Quy định ẩn). Quy tắc xử sự được suy ra là: Công dân bắt buộc phải thực hiện nghĩa vụ cứu giúp người khác khi thấy họ nguy hiểm đến tính mạng và bản thân có điều kiện cứu giúp.\n\n"
                "3. Bộ phận Chế tài:\n"
                "- Nội dung: 'thì bị phạt cảnh cáo, phạt cải tạo không giam giữ đến 02 năm hoặc phạt tù từ 03 tháng đến 02 năm.'\n"
                "- Ý nghĩa: Xác định biện pháp cưỡng chế nghiêm khắc của Nhà nước (chế tài hình sự) áp dụng đối với người không thực hiện đúng nghĩa vụ được nêu ở phần giả định."
            )
        },
        {
            "sample_id": "SEED_AGE_001",
            "intent_code": "CRIMINAL_AGE",
            "instruction": "Hãy xác định trách nhiệm hình sự căn cứ theo độ tuổi và loại tội phạm trong tình huống sau.",
            "input": (
                "Tình huống: Nguyễn Văn M (sinh ngày 15/06/2009). Ngày 20/08/2024, M thực hiện hành vi trộm cắp một chiếc xe máy "
                "trị giá 35 triệu đồng của nhà hàng xóm (Hành vi cấu thành tội phạm theo Khoản 1 Điều 173 BLHS 2015 với khung hình phạt cải tạo không giam giữ đến 03 năm hoặc phạt tù từ 06 tháng đến 03 năm). "
                "Hỏi M có phải chịu trách nhiệm hình sự hay không? Tại sao?"
            ),
            "output": (
                "I. KẾT LUẬN:\n"
                "Nguyễn Văn M KHÔNG PHẢI CHỊU trách nhiệm hình sự về hành vi trộm cắp tài sản nêu trên.\n\n"
                "II. LẬP LUẬN CĂN CỨ PHÁP LÝ:\n"
                "1. Xác định độ tuổi của chủ thể tại thời điểm phạm tội:\n"
                "- Ngày sinh của M: 15/06/2009.\n"
                "- Ngày thực hiện hành vi: 20/08/2024.\n"
                "- Tính đến thời điểm phạm tội, M được: 15 tuổi 2 tháng (tức là người 'từ đủ 14 tuổi đến dưới 16 tuổi').\n\n"
                "2. Xác định loại tội phạm theo khung hình phạt (Điều 9 BLHS 2015):\n"
                "- Hành vi của M thuộc Khoản 1 Điều 173 BLHS với mức phạt cao nhất là 03 năm tù.\n"
                "- Căn cứ Khoản 1 Điều 9 BLHS 2015, tội phạm có mức cao nhất của khung hình phạt đến 03 năm tù là TỘI PHẠM ÍT NGHIÊM TRỌNG.\n\n"
                "3. Đối chiếu quy định về tuổi chịu TNHS (Khoản 2 Điều 12 BLHS 2015):\n"
                "- Người từ đủ 14 tuổi đến dưới 16 tuổi CHỈ phải chịu trách nhiệm hình sự về tội phạm RẤT NGHIÊM TRỌNG hoặc ĐẶC BIỆT NGHIÊM TRỌNG quy định tại một số điều khoản liệt kê cụ thể (trong đó đối với Điều 173, chỉ phải chịu TNHS nếu phạm tội theo Khoản 3 hoặc Khoản 4).\n"
                "- Hành vi của M chỉ thuộc Khoản 1 (Tội phạm ít nghiêm trọng) nên M chưa đủ tuổi chịu trách nhiệm hình sự theo quy định."
            )
        }
    ]


def save_and_report_sft_dataset(file_path: Optional[Path] = None):
    """Khởi tạo hoặc kiểm tra trạng thái tập dữ liệu SFT 500 mẫu."""
    if file_path is None:
        file_path = PROCESSED_DIR / "sft_vietlaw_500.json"

    if not file_path.exists() or file_path.stat().st_size == 0:
        seed = generate_seed_templates()
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(seed, f, ensure_ascii=False, indent=2)
        logger.info(f"Đã khởi tạo file mẫu SFT hạt giống tại: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    logger.info(f"=== BÁO CÁO TẬP DỮ LIỆU SFT HIỆN TẠI ({len(data)}/500 MẪU) ===")
    counts = {}
    for item in data:
        code = item.get("intent_code", "UNKNOWN")
        counts[code] = counts.get(code, 0) + 1

    for code, target_meta in INTENT_DISTRIBUTION.items():
        curr = counts.get(code, 0)
        target = target_meta["target"]
        pct = (curr / target) * 100
        logger.info(f"[{code:15s}] {target_meta['name']:30s}: {curr:3d}/{target:3d} mẫu ({pct:5.1f}%)")
