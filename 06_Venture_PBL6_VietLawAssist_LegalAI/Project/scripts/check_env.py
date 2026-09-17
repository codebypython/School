"""
VietLawAssist — Kiểm Tra Trạng Thái Môi Trường & Dependencies
==============================================================
Script kiểm tra toàn bộ các thư viện cốt lõi cho các thành phần:
- Web Backend (FastAPI, Uvicorn, Pydantic v2)
- Data Engineering (Crawling, BeautifulSoup4, PyMuPDF, Pandas)
- Machine Learning & NLP (PyVi, rank-bm25, Underthesea)
- Database & Logging (aiosqlite, loguru, pytest)
"""

import sys
from pathlib import Path

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def main():
    print("=" * 60)
    print(" VIETLAWASSIST — KIỂM TRA MÔI TRƯỜNG & DEPENDENCIES")
    print("=" * 60)
    print(f"[*] Python Executable : {sys.executable}")
    print(f"[*] Python Version    : {sys.version.split()[0]}")
    print(f"[*] Root Directory    : {Path(__file__).resolve().parents[2]}")
    
    packages = [
        ("Tầng Web Backend & API", [
            ("fastapi", "FastAPI"),
            ("uvicorn", "Uvicorn ASGI Server"),
            ("pydantic", "Pydantic v2"),
            ("pydantic_settings", "Pydantic Settings"),
            ("dotenv", "python-dotenv"),
        ]),
        ("Tầng Dữ Liệu & Thu Thập", [
            ("bs4", "BeautifulSoup4"),
            ("httpx", "HTTPX Async Client"),
            ("fitz", "PyMuPDF (PDF Parser)"),
            ("lxml", "lxml HTML parser"),
            ("pandas", "Pandas Data Analysis"),
            ("aiosqlite", "aiosqlite Database Driver"),
        ]),
        ("Tầng Xử Lý Ngôn Ngữ & IR (BM25)", [
            ("pyvi", "PyVi Vietnamese Tokenizer"),
            ("rank_bm25", "rank-bm25 Okapi Retrieval"),
            ("underthesea", "Underthesea NLP Toolkit"),
            ("regex", "regex advanced engine"),
            ("unidecode", "Unidecode transliteration"),
        ]),
        ("Tầng Kiểm Thử & Tiện Ích", [
            ("pytest", "PyTest Test Runner"),
            ("pytest_asyncio", "PyTest AsyncIO Plugin"),
            ("loguru", "Loguru Logging"),
            ("tqdm", "tqdm Progress Bar"),
            ("click", "Click CLI"),
        ])
    ]

    all_passed = True
    for group_name, mods in packages:
        print(f"\n--- {group_name} ---")
        for mod_name, label in mods:
            try:
                mod = __import__(mod_name)
                ver = getattr(mod, "__version__", "installed")
                print(f"  [✓] {label:<32} (v{ver})")
            except ImportError as e:
                print(f"  [✗] {label:<32} LỖI: {e}")
                all_passed = False

    print("\n" + "=" * 60)
    if all_passed:
        print("[THÀNH CÔNG] Toàn bộ 21/21 thư viện cốt lõi đã sẵn sàng 100%!")
        print("Môi trường .venv hoàn toàn đáp ứng hoạt động của mọi thành phần.")
    else:
        print("[CẢNH BÁO] Phát hiện thư viện bị thiếu. Vui lòng kiểm tra lại requirements.txt.")
    print("=" * 60)

if __name__ == "__main__":
    main()
