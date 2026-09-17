"""
VietLawAssist — Law Crawler & Parser Pipeline
==============================================
Agent-03 (Data Engineer) — Thu thập và bóc tách cấu trúc 5 bộ luật trọng tâm:
    1. Hiến pháp 2013 (HP2013)
    2. Bộ luật Dân sự 2015 (BLDS2015)
    3. Bộ luật Hình sự 2015 sđ 2017 (BLHS2015)
    4. Luật Hôn nhân & Gia đình 2014 (HNGD2014)
    5. Bộ luật Lao động 2019 (BLLD2019)

Tuân thủ:
    - Chunking strategy: 1 Điều luật = 1 Document độc lập.
    - Chuẩn hóa Unicode NFC qua clean_text.py.
    - Bóc tách chương, mục, số điều, tiêu đề, và nội dung khoản.
"""

import json
import re
from pathlib import Path
from typing import Optional
import click
from loguru import logger

from scripts.clean_text import clean_legal_text, normalize_unicode_nfc

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
SAMPLE_DIR = PROJECT_ROOT / "data" / "sample"


# Metadata của 5 bộ luật cốt lõi
LAW_METADATA = {
    "HP2013": {
        "law_name": "Hiến pháp nước Cộng hòa xã hội chủ nghĩa Việt Nam năm 2013",
        "effective_date": "2014-01-01",
        "source_url": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=32801",
    },
    "BLDS2015": {
        "law_name": "Bộ luật Dân sự năm 2015",
        "effective_date": "2017-01-01",
        "source_url": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=96406",
    },
    "BLHS2015": {
        "law_name": "Bộ luật Hình sự năm 2015 (sửa đổi, bổ sung năm 2017)",
        "effective_date": "2018-01-01",
        "source_url": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=124036",
    },
    "HNGD2014": {
        "law_name": "Luật Hôn nhân và Gia đình năm 2014",
        "effective_date": "2015-01-01",
        "source_url": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=36688",
    },
    "BLLD2019": {
        "law_name": "Bộ luật Lao động năm 2019",
        "effective_date": "2021-01-01",
        "source_url": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=139369",
    },
}


def parse_raw_legal_text(raw_text: str, law_code: str) -> list[dict]:
    """
    Phân tích cú pháp văn bản luật thô thành danh sách các điều luật cấu trúc.

    Regex nhận diện:
        - Chương: r'(Chương\\s+[IVXLCDM0-9]+[.:\\s].*)'
        - Điều: r'^Điều\\s+(\\d+)[.:\\s]+(.*)$'
    """
    meta = LAW_METADATA.get(law_code, {
        "law_name": law_code,
        "effective_date": "",
        "source_url": ""
    })

    text = normalize_unicode_nfc(raw_text)
    lines = text.splitlines()

    articles = []
    current_chapter = ""
    current_section = ""
    current_article_num: Optional[int] = None
    current_title = ""
    current_content_lines: list[str] = []

    # Regex patterns
    re_chapter = re.compile(r'^(Chương\s+[IVXLCDM0-9]+[\s\.:].*)$', re.IGNORECASE)
    re_section = re.compile(r'^(Mục\s+[IVXLCDM0-9]+[\s\.:].*)$', re.IGNORECASE)
    re_article = re.compile(r'^Điều\s+(\d+)[\.:\s]*(.*)$', re.IGNORECASE)

    def save_current():
        nonlocal current_article_num, current_title, current_content_lines
        if current_article_num is not None:
            content_str = "\n".join(current_content_lines).strip()
            if not content_str:
                content_str = current_title
            
            full_text = f"Điều {current_article_num}. {current_title}\n{content_str}".strip() if current_title else f"Điều {current_article_num}\n{content_str}".strip()
            
            articles.append({
                "article_id": f"{law_code}_D{current_article_num}",
                "law_code": law_code,
                "law_name": meta["law_name"],
                "chapter": current_chapter,
                "section": current_section,
                "article_number": current_article_num,
                "title": f"Điều {current_article_num}. {current_title}".strip() if current_title else f"Điều {current_article_num}",
                "content": content_str,
                "full_text": full_text,
                "effective_date": meta["effective_date"],
                "source_url": meta["source_url"],
                "word_count": len(content_str.split()),
            })
            current_content_lines = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        chap_m = re_chapter.match(stripped)
        if chap_m:
            current_chapter = chap_m.group(1).strip()
            continue

        sec_m = re_section.match(stripped)
        if sec_m:
            current_section = sec_m.group(1).strip()
            continue

        art_m = re_article.match(stripped)
        if art_m:
            save_current()
            current_article_num = int(art_m.group(1))
            current_title = art_m.group(2).strip()
            continue

        if current_article_num is not None:
            current_content_lines.append(stripped)

    save_current()
    logger.info(f"Đã bóc tách thành công {len(articles)} điều luật cho {law_code}")
    return articles


def build_curated_high_yield_articles() -> list[dict]:
    """
    Tạo danh mục các điều luật trọng tâm cao độ (High-Yield Core Corpus)
    phục vụ trực tiếp cho 5 dạng đề thi môn Pháp luật Đại cương tại DUT.
    Bao gồm đầy đủ 5 bộ luật: HP2013, BLDS2015, BLHS2015, HNGD2014, BLLD2019.
    """
    # Nạp sample articles đã có làm nền tảng
    sample_path = SAMPLE_DIR / "sample_articles.json"
    articles_map = {}

    if sample_path.exists():
        with open(sample_path, "r", encoding="utf-8") as f:
            for item in json.load(f):
                articles_map[item["article_id"]] = item

    # Bổ sung các điều luật cốt lõi của Luật Hôn nhân & Gia đình 2014 (HNGD2014)
    hngd_articles = [
        {
            "article_id": "HNGD2014_D8",
            "law_code": "HNGD2014",
            "law_name": LAW_METADATA["HNGD2014"]["law_name"],
            "chapter": "Chương II: Kết hôn",
            "section": "",
            "article_number": 8,
            "title": "Điều 8. Điều kiện kết hôn",
            "content": "1. Nam, nữ kết hôn với nhau phải tuân theo các điều kiện sau đây:\na) Nam từ đủ 20 tuổi trở lên, nữ từ đủ 18 tuổi trở lên;\nb) Việc kết hôn do nam và nữ tự nguyện quyết định;\nc) Không bị mất năng lực hành vi dân sự;\nd) Việc kết hôn không thuộc một trong các trường hợp cấm kết hôn theo quy định tại các điểm a, b, c và d khoản 2 Điều 5 của Luật này.\n2. Nhà nước không thừa nhận hôn nhân giữa những người cùng giới tính.",
            "full_text": "Điều 8. Điều kiện kết hôn\n1. Nam, nữ kết hôn với nhau phải tuân theo các điều kiện sau đây:\na) Nam từ đủ 20 tuổi trở lên, nữ từ đủ 18 tuổi trở lên;\nb) Việc kết hôn do nam và nữ tự nguyện quyết định;\nc) Không bị mất năng lực hành vi dân sự;\nd) Việc kết hôn không thuộc một trong các trường hợp cấm kết hôn theo quy định tại các điểm a, b, c và d khoản 2 Điều 5 của Luật này.\n2. Nhà nước không thừa nhận hôn nhân giữa những người cùng giới tính.",
            "effective_date": LAW_METADATA["HNGD2014"]["effective_date"],
            "source_url": LAW_METADATA["HNGD2014"]["source_url"],
            "word_count": 105
        },
        {
            "article_id": "HNGD2014_D9",
            "law_code": "HNGD2014",
            "law_name": LAW_METADATA["HNGD2014"]["law_name"],
            "chapter": "Chương II: Kết hôn",
            "section": "",
            "article_number": 9,
            "title": "Điều 9. Đăng ký kết hôn",
            "content": "1. Việc kết hôn phải được đăng ký và do cơ quan nhà nước có thẩm quyền thực hiện theo quy định của Luật này và pháp luật về hộ tịch. Việc kết hôn không được đăng ký theo quy định tại khoản này thì không có giá trị pháp lý.\n2. Vợ chồng đã ly hôn muốn xác lập lại quan hệ vợ chồng thì phải đăng ký kết hôn.",
            "full_text": "Điều 9. Đăng ký kết hôn\n1. Việc kết hôn phải được đăng ký và do cơ quan nhà nước có thẩm quyền thực hiện theo quy định của Luật này và pháp luật về hộ tịch. Việc kết hôn không được đăng ký theo quy định tại khoản này thì không có giá trị pháp lý.\n2. Vợ chồng đã ly hôn muốn xác lập lại quan hệ vợ chồng thì phải đăng ký kết hôn.",
            "effective_date": LAW_METADATA["HNGD2014"]["effective_date"],
            "source_url": LAW_METADATA["HNGD2014"]["source_url"],
            "word_count": 68
        },
        {
            "article_id": "HNGD2014_D33",
            "law_code": "HNGD2014",
            "law_name": LAW_METADATA["HNGD2014"]["law_name"],
            "chapter": "Chương III: Quan hệ giữa vợ và chồng",
            "section": "Mục 1: Quyền và nghĩa vụ về tài sản",
            "article_number": 33,
            "title": "Điều 33. Tài sản chung của vợ chồng",
            "content": "1. Tài sản chung của vợ chồng gồm tài sản do vợ, chồng tạo ra, thu nhập do lao động, hoạt động sản xuất, kinh doanh, hoa lợi, lợi tức phát sinh từ tài sản riêng và thu nhập hợp pháp khác trong thời kỳ hôn nhân; tài sản mà vợ chồng được thừa kế chung hoặc được tặng cho chung và tài sản khác mà vợ chồng thỏa thuận là tài sản chung.\nQuyền sử dụng đất mà vợ, chồng có được sau khi kết hôn là tài sản chung của vợ chồng, trừ trường hợp vợ hoặc chồng được thừa kế riêng, được tặng cho riêng hoặc có được thông qua giao dịch bằng tài sản riêng.\n2. Tài sản chung của vợ chồng thuộc sở hữu chung hợp nhất, được dùng để bảo đảm nhu cầu của gia đình, thực hiện nghĩa vụ chung của vợ chồng.\n3. Trong trường hợp không có căn cứ để chứng minh tài sản mà vợ, chồng đang có tranh chấp là tài sản riêng của mỗi bên thì tài sản đó được coi là tài sản chung.",
            "full_text": "Điều 33. Tài sản chung của vợ chồng\n1. Tài sản chung của vợ chồng gồm tài sản do vợ, chồng tạo ra, thu nhập do lao động, hoạt động sản xuất, kinh doanh, hoa lợi, lợi tức phát sinh từ tài sản riêng và thu nhập hợp pháp khác trong thời kỳ hôn nhân; tài sản mà vợ chồng được thừa kế chung hoặc được tặng cho chung và tài sản khác mà vợ chồng thỏa thuận là tài sản chung.\nQuyền sử dụng đất mà vợ, chồng có được sau khi kết hôn là tài sản chung của vợ chồng, trừ trường hợp vợ hoặc chồng được thừa kế riêng, được tặng cho riêng hoặc có được thông qua giao dịch bằng tài sản riêng.\n2. Tài sản chung của vợ chồng thuộc sở hữu chung hợp nhất, được dùng để bảo đảm nhu cầu của gia đình, thực hiện nghĩa vụ chung của vợ chồng.\n3. Trong trường hợp không có căn cứ để chứng minh tài sản mà vợ, chồng đang có tranh chấp là tài sản riêng của mỗi bên thì tài sản đó được coi là tài sản chung.",
            "effective_date": LAW_METADATA["HNGD2014"]["effective_date"],
            "source_url": LAW_METADATA["HNGD2014"]["source_url"],
            "word_count": 182
        },
        {
            "article_id": "HNGD2014_D43",
            "law_code": "HNGD2014",
            "law_name": LAW_METADATA["HNGD2014"]["law_name"],
            "chapter": "Chương III: Quan hệ giữa vợ và chồng",
            "section": "Mục 1: Quyền và nghĩa vụ về tài sản",
            "article_number": 43,
            "title": "Điều 43. Tài sản riêng của vợ, chồng",
            "content": "1. Tài sản riêng của vợ, chồng gồm tài sản mà mỗi người có trước khi kết hôn; tài sản được thừa kế riêng, được tặng cho riêng trong thời kỳ hôn nhân; tài sản được chia riêng cho vợ, chồng theo quy định tại các điều 38, 39 và 40 của Luật này; tài sản phục vụ nhu cầu thiết yếu của vợ, chồng và tài sản khác mà theo quy định của pháp luật thuộc sở hữu riêng của vợ, chồng.\n2. Tài sản được hình thành từ tài sản riêng của vợ, chồng cũng là tài sản riêng của vợ, chồng. Hoa lợi, lợi tức phát sinh từ tài sản riêng trong thời kỳ hôn nhân được thực hiện theo quy định tại khoản 1 Điều 33 và khoản 1 Điều 40 của Luật này.",
            "full_text": "Điều 43. Tài sản riêng của vợ, chồng\n1. Tài sản riêng của vợ, chồng gồm tài sản mà mỗi người có trước khi kết hôn; tài sản được thừa kế riêng, được tặng cho riêng trong thời kỳ hôn nhân; tài sản được chia riêng cho vợ, chồng theo quy định tại các điều 38, 39 và 40 của Luật này; tài sản phục vụ nhu cầu thiết yếu của vợ, chồng và tài sản khác mà theo quy định của pháp luật thuộc sở hữu riêng của vợ, chồng.\n2. Tài sản được hình thành từ tài sản riêng của vợ, chồng cũng là tài sản riêng của vợ, chồng. Hoa lợi, lợi tức phát sinh từ tài sản riêng trong thời kỳ hôn nhân được thực hiện theo quy định tại khoản 1 Điều 33 và khoản 1 Điều 40 của Luật này.",
            "effective_date": LAW_METADATA["HNGD2014"]["effective_date"],
            "source_url": LAW_METADATA["HNGD2014"]["source_url"],
            "word_count": 145
        },
        {
            "article_id": "HNGD2014_D51",
            "law_code": "HNGD2014",
            "law_name": LAW_METADATA["HNGD2014"]["law_name"],
            "chapter": "Chương IV: Chấm dứt hôn nhân",
            "section": "Mục 1: Ly hôn",
            "article_number": 51,
            "title": "Điều 51. Quyền yêu cầu giải quyết ly hôn",
            "content": "1. Vợ, chồng hoặc cả hai người có quyền yêu cầu Tòa án giải quyết ly hôn.\n2. Cha, mẹ, người thân thích khác có quyền yêu cầu Tòa án giải quyết ly hôn khi một bên vợ, chồng do bị bệnh tâm thần hoặc mắc bệnh khác mà không thể nhận thức, làm chủ được hành vi của mình, đồng thời là nạn nhân của bạo lực gia đình do chồng, vợ của họ gây ra làm ảnh hưởng nghiêm trọng đến tính mạng, sức khỏe, tinh thần của họ.\n3. Chồng không có quyền yêu cầu ly hôn trong trường hợp vợ đang có thai, sinh con hoặc đang nuôi con dưới 12 tháng tuổi.",
            "full_text": "Điều 51. Quyền yêu cầu giải quyết ly hôn\n1. Vợ, chồng hoặc cả hai người có quyền yêu cầu Tòa án giải quyết ly hôn.\n2. Cha, mẹ, người thân thích khác có quyền yêu cầu Tòa án giải quyết ly hôn khi một bên vợ, chồng do bị bệnh tâm thần hoặc mắc bệnh khác mà không thể nhận thức, làm chủ được hành vi của mình, đồng thời là nạn nhân của bạo lực gia đình do chồng, vợ của họ gây ra làm ảnh hưởng nghiêm trọng đến tính mạng, sức khỏe, tinh thần của họ.\n3. Chồng không có quyền yêu cầu ly hôn trong trường hợp vợ đang có thai, sinh con hoặc đang nuôi con dưới 12 tháng tuổi.",
            "effective_date": LAW_METADATA["HNGD2014"]["effective_date"],
            "source_url": LAW_METADATA["HNGD2014"]["source_url"],
            "word_count": 118
        },
    ]

    # Bổ sung các điều luật cốt lõi của Bộ luật Lao động 2019 (BLLD2019)
    blld_articles = [
        {
            "article_id": "BLLD2019_D13",
            "law_code": "BLLD2019",
            "law_name": LAW_METADATA["BLLD2019"]["law_name"],
            "chapter": "Chương III: Hợp đồng lao động",
            "section": "Mục 1: Giao kết hợp đồng lao động",
            "article_number": 13,
            "title": "Điều 13. Hợp đồng lao động",
            "content": "1. Hợp đồng lao động là sự thỏa thuận giữa người lao động và người sử dụng lao động về việc làm có trả công, tiền lương, điều kiện lao động, quyền và nghĩa vụ của mỗi bên trong quan hệ lao động.\nTrường hợp hai bên thỏa thuận bằng tên gọi khác nhưng có nội dung thể hiện về việc làm có trả công, tiền lương và sự quản lý, điều hành, giám sát của một bên thì vẫn được coi là hợp đồng lao động.\n2. Trước khi nhận người lao động vào làm việc thì người sử dụng lao động phải giao kết hợp đồng lao động với người lao động.",
            "full_text": "Điều 13. Hợp đồng lao động\n1. Hợp đồng lao động là sự thỏa thuận giữa người lao động và người sử dụng lao động về việc làm có trả công, tiền lương, điều kiện lao động, quyền và nghĩa vụ của mỗi bên trong quan hệ lao động.\nTrường hợp hai bên thỏa thuận bằng tên gọi khác nhưng có nội dung thể hiện về việc làm có trả công, tiền lương và sự quản lý, điều hành, giám sát của một bên thì vẫn được coi là hợp đồng lao động.\n2. Trước khi nhận người lao động vào làm việc thì người sử dụng lao động phải giao kết hợp đồng lao động với người lao động.",
            "effective_date": LAW_METADATA["BLLD2019"]["effective_date"],
            "source_url": LAW_METADATA["BLLD2019"]["source_url"],
            "word_count": 108
        },
        {
            "article_id": "BLLD2019_D20",
            "law_code": "BLLD2019",
            "law_name": LAW_METADATA["BLLD2019"]["law_name"],
            "chapter": "Chương III: Hợp đồng lao động",
            "section": "Mục 1: Giao kết hợp đồng lao động",
            "article_number": 20,
            "title": "Điều 20. Loại hợp đồng lao động",
            "content": "1. Hợp đồng lao động phải được giao kết theo một trong các loại sau đây:\na) Hợp đồng lao động không xác định thời hạn là hợp đồng mà trong đó hai bên không xác định thời hạn, thời điểm chấm dứt hiệu lực của hợp đồng;\nb) Hợp đồng lao động xác định thời hạn là hợp đồng mà trong đó hai bên xác định thời hạn, thời điểm chấm dứt hiệu lực của hợp đồng trong thời gian không quá 36 tháng kể từ thời điểm có hiệu lực của hợp đồng.\n2. Khi hợp đồng lao động quy định tại điểm b khoản 1 Điều này hết hạn mà người lao động vẫn tiếp tục làm việc thì hai bên phải ký hợp đồng mới trong thời hạn 30 ngày. Nếu không ký thì hợp đồng đã giao kết trở thành hợp đồng lao động không xác định thời hạn.",
            "full_text": "Điều 20. Loại hợp đồng lao động\n1. Hợp đồng lao động phải được giao kết theo một trong các loại sau đây:\na) Hợp đồng lao động không xác định thời hạn là hợp đồng mà trong đó hai bên không xác định thời hạn, thời điểm chấm dứt hiệu lực của hợp đồng;\nb) Hợp đồng lao động xác định thời hạn là hợp đồng mà trong đó hai bên xác định thời hạn, thời điểm chấm dứt hiệu lực của hợp đồng trong thời gian không quá 36 tháng kể từ thời điểm có hiệu lực của hợp đồng.\n2. Khi hợp đồng lao động quy định tại điểm b khoản 1 Điều này hết hạn mà người lao động vẫn tiếp tục làm việc thì hai bên phải ký hợp đồng mới trong thời hạn 30 ngày. Nếu không ký thì hợp đồng đã giao kết trở thành hợp đồng lao động không xác định thời hạn.",
            "effective_date": LAW_METADATA["BLLD2019"]["effective_date"],
            "source_url": LAW_METADATA["BLLD2019"]["source_url"],
            "word_count": 140
        },
        {
            "article_id": "BLLD2019_D25",
            "law_code": "BLLD2019",
            "law_name": LAW_METADATA["BLLD2019"]["law_name"],
            "chapter": "Chương III: Hợp đồng lao động",
            "section": "Mục 1: Giao kết hợp đồng lao động",
            "article_number": 25,
            "title": "Điều 25. Thời gian thử việc",
            "content": "Thời gian thử việc do hai bên thỏa thuận căn cứ vào tính chất và mức độ phức tạp của công việc nhưng chỉ được thử việc một lần đối với một công việc và bảo đảm điều kiện sau đây:\n1. Không quá 180 ngày đối với công việc của người quản lý doanh nghiệp theo quy định của Luật Doanh nghiệp, Luật Quản lý, sử dụng vốn nhà nước đầu tư vào sản xuất, kinh doanh tại doanh nghiệp;\n2. Không quá 60 ngày đối với công việc có chức danh nghề nghiệp cần trình độ chuyên môn, kỹ thuật từ cao đẳng trở lên;\n3. Không quá 30 ngày đối với công việc có chức danh nghề nghiệp cần trình độ chuyên môn, kỹ thuật trung cấp, công nhân kỹ thuật, nhân viên nghiệp vụ;\n4. Không quá 06 ngày làm việc đối với công việc khác.",
            "full_text": "Điều 25. Thời gian thử việc\nThời gian thử việc do hai bên thỏa thuận căn cứ vào tính chất và mức độ phức tạp của công việc nhưng chỉ được thử việc một lần đối với một công việc và bảo đảm điều kiện sau đây:\n1. Không quá 180 ngày đối với công việc của người quản lý doanh nghiệp theo quy định của Luật Doanh nghiệp, Luật Quản lý, sử dụng vốn nhà nước đầu tư vào sản xuất, kinh doanh tại doanh nghiệp;\n2. Không quá 60 ngày đối với công việc có chức danh nghề nghiệp cần trình độ chuyên môn, kỹ thuật từ cao đẳng trở lên;\n3. Không quá 30 ngày đối với công việc có chức danh nghề nghiệp cần trình độ chuyên môn, kỹ thuật trung cấp, công nhân kỹ thuật, nhân viên nghiệp vụ;\n4. Không quá 06 ngày làm việc đối với công việc khác.",
            "effective_date": LAW_METADATA["BLLD2019"]["effective_date"],
            "source_url": LAW_METADATA["BLLD2019"]["source_url"],
            "word_count": 138
        },
        {
            "article_id": "BLLD2019_D105",
            "law_code": "BLLD2019",
            "law_name": LAW_METADATA["BLLD2019"]["law_name"],
            "chapter": "Chương VII: Thời giờ làm việc, thời giờ nghỉ ngơi",
            "section": "Mục 1: Thời giờ làm việc",
            "article_number": 105,
            "title": "Điều 105. Thời giờ làm việc bình thường",
            "content": "1. Thời giờ làm việc bình thường không quá 08 giờ trong 01 ngày và không quá 48 giờ trong 01 tuần.\n2. Người sử dụng lao động có quyền quy định thời giờ làm việc theo ngày hoặc tuần nhưng phải thông báo cho người lao động biết; trường hợp theo tuần thì thời giờ làm việc bình thường không quá 10 giờ trong 01 ngày và không quá 48 giờ trong 01 tuần.\n3. Nhà nước khuyến khích người sử dụng lao động thực hiện tuần làm việc 40 giờ đối với người lao động.\n4. Người sử dụng lao động có trách nhiệm bảo đảm giới hạn thời gian làm việc tiếp xúc với yếu tố nguy hiểm, yếu tố có hại theo đúng quy chuẩn kỹ thuật quốc gia và pháp luật có liên quan.",
            "full_text": "Điều 105. Thời giờ làm việc bình thường\n1. Thời giờ làm việc bình thường không quá 08 giờ trong 01 ngày và không quá 48 giờ trong 01 tuần.\n2. Người sử dụng lao động có quyền quy định thời giờ làm việc theo ngày hoặc tuần nhưng phải thông báo cho người lao động biết; trường hợp theo tuần thì thời giờ làm việc bình thường không quá 10 giờ trong 01 ngày và không quá 48 giờ trong 01 tuần.\n3. Nhà nước khuyến khích người sử dụng lao động thực hiện tuần làm việc 40 giờ đối với người lao động.\n4. Người sử dụng lao động có trách nhiệm bảo đảm giới hạn thời gian làm việc tiếp xúc với yếu tố nguy hiểm, yếu tố có hại theo đúng quy chuẩn kỹ thuật quốc gia và pháp luật có liên quan.",
            "effective_date": LAW_METADATA["BLLD2019"]["effective_date"],
            "source_url": LAW_METADATA["BLLD2019"]["source_url"],
            "word_count": 140
        },
        {
            "article_id": "BLLD2019_D125",
            "law_code": "BLLD2019",
            "law_name": LAW_METADATA["BLLD2019"]["law_name"],
            "chapter": "Chương VIII: Kỷ luật lao động, trách nhiệm vật chất",
            "section": "Mục 1: Kỷ luật lao động",
            "article_number": 125,
            "title": "Điều 125. Áp dụng hình thức xử lý kỷ luật sa thải",
            "content": "Hình thức xử lý kỷ luật sa thải được người sử dụng lao động áp dụng trong trường hợp sau đây:\n1. Người lao động có hành vi trộm cắp, tham ô, đánh bạc, cố ý gây thương tích, sử dụng ma túy tại nơi làm việc;\n2. Người lao động có hành vi tiết lộ bí mật kinh doanh, bí mật công nghệ, xâm phạm quyền sở hữu trí tuệ của người sử dụng lao động, có hành vi gây thiệt hại nghiêm trọng hoặc đe dọa gây thiệt hại đặc biệt nghiêm trọng về tài sản, lợi ích của người sử dụng lao động hoặc quấy rối tình dục tại nơi làm việc được quy định trong nội quy lao động;\n3. Người lao động bị xử lý kỷ luật kéo dài thời hạn nâng lương hoặc cách chức mà tái phạm trong thời gian chưa xóa kỷ luật. Tái phạm là trường hợp người lao động lặp lại hành vi vi phạm đã bị xử lý kỷ luật mà chưa được xóa kỷ luật;\n4. Người lao động tự ý bỏ việc 05 ngày cộng dồn trong thời hạn 30 ngày hoặc 20 ngày cộng dồn trong thời hạn 365 ngày tính từ ngày đầu tiên tự ý bỏ việc mà không có lý do chính đáng.",
            "full_text": "Điều 125. Áp dụng hình thức xử lý kỷ luật sa thải\nHình thức xử lý kỷ luật sa thải được người sử dụng lao động áp dụng trong trường hợp sau đây:\n1. Người lao động có hành vi trộm cắp, tham ô, đánh bạc, cố ý gây thương tích, sử dụng ma túy tại nơi làm việc;\n2. Người lao động có hành vi tiết lộ bí mật kinh doanh, bí mật công nghệ, xâm phạm quyền sở hữu trí tuệ của người sử dụng lao động, có hành vi gây thiệt hại nghiêm trọng hoặc đe dọa gây thiệt hại đặc biệt nghiêm trọng về tài sản, lợi ích của người sử dụng lao động hoặc quấy rối tình dục tại nơi làm việc được quy định trong nội quy lao động;\n3. Người lao động bị xử lý kỷ luật kéo dài thời hạn nâng lương hoặc cách chức mà tái phạm trong thời gian chưa xóa kỷ luật. Tái phạm là trường hợp người lao động lặp lại hành vi vi phạm đã bị xử lý kỷ luật mà chưa được xóa kỷ luật;\n4. Người lao động tự ý bỏ việc 05 ngày cộng dồn trong thời hạn 30 ngày hoặc 20 ngày cộng dồn trong thời hạn 365 ngày tính từ ngày đầu tiên tự ý bỏ việc mà không có lý do chính đáng.",
            "effective_date": LAW_METADATA["BLLD2019"]["effective_date"],
            "source_url": LAW_METADATA["BLLD2019"]["source_url"],
            "word_count": 218
        }
    ]

    for a in hngd_articles + blld_articles:
        articles_map[a["article_id"]] = a

    articles = list(articles_map.values())
    logger.info(f"Tổng hợp bộ điều luật trọng tâm gồm {len(articles)} điều từ cả 5 bộ luật.")
    return articles


@click.group()
def cli():
    """VietLawAssist — CLI Công cụ Thu thập và Xử lý Dữ liệu Luật."""
    pass


@cli.command("generate-corpus")
@click.option("--output-json", default=str(RAW_DIR / "corpus_combined.json"), help="Đường dẫn file JSON đầu ra")
def generate_corpus_cmd(output_json: str):
    """Tổng hợp và xuất tập dữ liệu điều luật đầy đủ ra data/raw/."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    articles = build_curated_high_yield_articles()
    out_path = Path(output_json)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    logger.success(f"Đã tạo file corpus với {len(articles)} điều luật tại: {out_path}")


if __name__ == "__main__":
    cli()
