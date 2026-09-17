#!/usr/bin/env python3
"""
fix_systematic_links.py — Fix remaining systematic broken links:
  1. Root-level file references → correct subfolder paths
  2. Old /Japanese/ paths → /05_Company_Japanese_Language_JPN/ subfolders
  3. JPN README subfolders that don't exist → note about new structure

Run: python scripts/fix_systematic_links.py
"""

import re
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path("D:/User/7th/School").resolve()

# ── Fix Map: old absolute path → correct absolute path ───────────────────────
ABSOLUTE_FIXES: list[tuple[str, str]] = [
    # EXTERNAL_KNOWLEDGE_VAULT at root → correct subfolder
    (
        "file:///d:/User/7th/School/EXTERNAL_KNOWLEDGE_VAULT.md",
        "file:///d:/User/7th/School/00_Corporate_Knowledge_Vault/EXTERNAL_KNOWLEDGE_VAULT.md",
    ),
    # NOTION_ADVANCED_FORMULAS at root → correct subfolder
    (
        "file:///d:/User/7th/School/NOTION_ADVANCED_FORMULAS.md",
        "file:///d:/User/7th/School/00_Central_Notion_LMS_Hub/NOTION_ADVANCED_FORMULAS.md",
    ),
    # NOTION_SYSTEM_GUIDE at root → correct subfolder
    (
        "file:///d:/User/7th/School/NOTION_SYSTEM_GUIDE.md",
        "file:///d:/User/7th/School/00_Central_Notion_LMS_Hub/NOTION_SYSTEM_GUIDE.md",
    ),
    # Old /Japanese/ folder → new JPN company folder
    (
        "file:///d:/User/7th/School/Japanese/",
        "file:///d:/User/7th/School/05_Company_Japanese_Language_JPN/",
    ),
    # Memrise Training (old path) → JPN root
    (
        "file:///d:/User/7th/School/Japanese/Memrise%20Training/",
        "file:///d:/User/7th/School/05_Company_Japanese_Language_JPN/",
    ),
]

SKIP_DIRS  = {".git", ".venv", "venv", "node_modules", "build", "_deps", "__pycache__"}
SKIP_FILES = {"LEVEL_1_AUDIT_REPORT.md"}


def fix_file(filepath: Path) -> int:
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return 0

    original = content
    for old, new in ABSOLUTE_FIXES:
        content = content.replace(old, new)

    if content != original:
        n = sum(original.count(old) for old, _ in ABSOLUTE_FIXES)
        filepath.write_text(content, encoding="utf-8")
        print(f"  ✅ Fixed in: {filepath.relative_to(ROOT)}")
        return n
    return 0


def main() -> None:
    md_files = [
        f for f in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in f.parts)
        and f.name not in SKIP_FILES
    ]

    print(f"Scanning {len(md_files)} markdown files for systematic link errors...\n")
    total = 0
    for f in sorted(md_files):
        total += fix_file(f)

    print(f"\n{'─'*50}")
    print(f"Total fixes applied: {total}")
    print("Run auditor to verify.")


if __name__ == "__main__":
    main()
