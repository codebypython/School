"""
VietLawAssist — Data Pipeline Configuration
===========================================
Agent-03 (Data Engineer) — Cấu hình các nguồn văn bản pháp luật và đường dẫn lưu trữ.
Hỗ trợ nguồn kép: CSDL Quốc gia VBPL và Thư viện Pháp luật (TVPL).
"""

from pathlib import Path

# Đường dẫn thư mục gốc
SCRIPTS_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = SCRIPTS_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
RAW_HTML_DIR = RAW_DIR / "html"
PROCESSED_DIR = DATA_DIR / "processed"
SAMPLE_DIR = DATA_DIR / "sample"
KAGGLE_BUNDLE_DIR = DATA_DIR / "kaggle_bundle"
DB_PATH = DATA_DIR / "law_corpus.db"

# Đảm bảo các thư mục tồn tại
for path in [RAW_DIR, RAW_HTML_DIR, PROCESSED_DIR, SAMPLE_DIR, KAGGLE_BUNDLE_DIR]:
    path.mkdir(parents=True, exist_ok=True)

# Danh mục 5 bộ luật cốt lõi trong chương trình Pháp luật Đại cương DUT
LAW_TARGETS = {
    "HP2013": {
        "law_code": "HP2013",
        "law_name": "Hiến pháp nước Cộng hòa xã hội chủ nghĩa Việt Nam năm 2013",
        "effective_date": "2014-01-01",
        "tvpl_url": "https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Hien-phap-nam-2013-215627.aspx",
        "vbpl_item_id": "32801",
        "vbpl_url": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=32801",
        "expected_articles": 120,
    },
    "BLDS2015": {
        "law_code": "BLDS2015",
        "law_name": "Bộ luật Dân sự năm 2015",
        "effective_date": "2017-01-01",
        "tvpl_url": "https://thuvienphapluat.vn/van-ban/Quyen-dan-su/Bo-luat-dan-su-2015-283877.aspx",
        "vbpl_item_id": "96406",
        "vbpl_url": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=96406",
        "expected_articles": 689,
    },
    "BLHS2015": {
        "law_code": "BLHS2015",
        "law_name": "Bộ luật Hình sự năm 2015 (sửa đổi, bổ sung năm 2017)",
        "effective_date": "2018-01-01",
        "tvpl_url": "https://thuvienphapluat.vn/van-ban/Trach-nhiem-hinh-su/Van-ban-hop-nhat-01-VBHN-VPQH-2017-Bo-luat-Hinh-su-355150.aspx",
        "vbpl_item_id": "124036",
        "vbpl_url": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=124036",
        "expected_articles": 426,
    },
    "HNGD2014": {
        "law_code": "HNGD2014",
        "law_name": "Luật Hôn nhân và Gia đình năm 2014",
        "effective_date": "2015-01-01",
        "tvpl_url": "https://thuvienphapluat.vn/van-ban/Quyen-dan-su/Luat-Hon-nhan-va-gia-dinh-2014-238640.aspx",
        "vbpl_item_id": "36688",
        "vbpl_url": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=36688",
        "expected_articles": 133,
    },
    "BLLD2019": {
        "law_code": "BLLD2019",
        "law_name": "Bộ luật Lao động năm 2019",
        "effective_date": "2021-01-01",
        "tvpl_url": "https://thuvienphapluat.vn/van-ban/Lao-dong-Tien-luong/Bo-luat-Lao-dong-2019-333670.aspx",
        "vbpl_item_id": "139369",
        "vbpl_url": "https://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=139369",
        "expected_articles": 220,
    },
}
