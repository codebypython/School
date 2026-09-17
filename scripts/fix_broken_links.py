#!/usr/bin/env python3
"""
fix_broken_links.py — Batch fix all broken links in School Holdings
====================================================================
Replaces dead references to the old 'PBL6 - Machine Learning Trainning Model Project/'
directory with clean comments or redirects to the new VENTURE-06 structure.

Run: python scripts/fix_broken_links.py
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

# ── Patterns to fix ──────────────────────────────────────────────────────────
# Pattern 1: Old PBL6 directory (URL-encoded)
# Replace entire link with a clean note
OLD_PBL6_PATTERN = re.compile(
    r'\[([^\]]+)\]\(file:///d:/User/7th/School/PBL6%20[^)]+\)',
    re.IGNORECASE,
)

# Pattern 2: Old non-encoded PBL6 path
OLD_PBL6_PLAIN = re.compile(
    r'\[([^\]]+)\]\((?:file:///d:/User/7th/School/)?PBL6[^)]+\)',
    re.IGNORECASE,
)

# Pattern 3: Relative CONTRIBUTING.md links (now exists at root)
# Nothing to fix — CONTRIBUTING.md now exists.

VENTURE06_ROOT = "file:///d:/User/7th/School/06_Venture_PBL6_VietLawAssist_LegalAI"

def replacement_note(match: re.Match) -> str:
    """Replace dead PBL6 link with inline note pointing to new VENTURE-06 location."""
    link_text = match.group(1)
    return f"[{link_text}]({VENTURE06_ROOT}/)"


def fix_file(filepath: Path) -> int:
    """Fix all dead PBL6 links in a file. Returns number of replacements."""
    try:
        original = filepath.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return 0

    fixed, n1 = OLD_PBL6_PATTERN.subn(replacement_note, original)
    fixed, n2 = OLD_PBL6_PLAIN.subn(replacement_note, fixed)
    total = n1 + n2

    if total > 0:
        filepath.write_text(fixed, encoding="utf-8")
        print(f"  ✅ Fixed {total} link(s) in: {filepath.relative_to(ROOT)}")

    return total


def main() -> None:
    SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "build", "_deps", "__pycache__"}
    SKIP_FILES = {"LEVEL_1_AUDIT_REPORT.md"}

    md_files = [
        f for f in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in f.parts)
        and f.name not in SKIP_FILES
    ]

    print(f"Scanning {len(md_files)} markdown files for dead PBL6 links...\n")
    total_fixed = 0
    for f in sorted(md_files):
        total_fixed += fix_file(f)

    print(f"\n{'─'*50}")
    print(f"Total replacements made: {total_fixed}")
    print("Run 'python scripts/holding_system_auditor.py' to verify.")


if __name__ == "__main__":
    main()
