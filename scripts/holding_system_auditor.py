#!/usr/bin/env python3
"""
HOLDING SYSTEM QUALITY AUDITOR (HSQA-v2.0)
==========================================
Role: Chief Technical Quality Auditor & Systems Inspector
Mandate: Zero-Tolerance Structural & Schema Integrity Verification
Target: d:/User/7th/School (All 11 Companies + 3 HQ Hubs)

MQAVP-2026 Scoring:
  - Level 1 weight: 15%  (Link integrity + Schema + Core Assets)
  - Pass threshold: >= 60.0%
  - Zero Broken Links: ABSOLUTE REQUIREMENT (1 broken = 0pts for link score)
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from typing import Optional

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

HOLDING_ROOT = Path("D:/User/7th/School").resolve()

# ---------------------------------------------------------------------------
# Mandatory 7-Tier Department Charter Headers (regex, case-insensitive)
# ---------------------------------------------------------------------------
TIER_HEADERS: list[str] = [
    r"##\s+.*1\.\s+.*(CHỨC NĂNG|NHIỆM VỤ|TỔNG QUAN|MỤC ĐÍCH)",
    r"##\s+.*2\.\s+.*(BỘ QUY TẮC BẤT BIẾN|HARD CONSTRAINTS|NGUYÊN TẮC|CURATION INVARIANTS|DEBUGGING INVARIANTS)",
    r"##\s+.*3\.\s+.*(SKILLS ROUTE|BỘ LỆNH|TOOLCHAIN|MA TRẬN|CẤU TRÚC TÀI SẢN)",
    r"##\s+.*4\.\s+.*(CẤU TRÚC THƯ MỤC|CẤU TRÚC TÀI SẢN|TÀI SẢN|HẠ TẦNG|MẪU TƯ LIỆU)",
    r"##\s+.*5\.\s+.*(MẪU KHUNG CODE|BOILERPLATE|GOLD MASTER|MẪU THIẾT KẾ|QUY CHUẨN|MẪU TƯ LIỆU)",
    r"##\s+.*6\.\s+.*(TIÊU CHÍ NGHIỆM THU|DEFINITION OF DONE|DOD|DEFINITION OF READY|DOR|TIÊU CHÍ DUYỆT)",
    r"##\s+.*7\.\s+.*(QUY TRÌNH XỬ LÝ SỰ CỐ|RUNBOOK|TROUBLESHOOTING|SỰ CỐ KHẨN CẤP|ỨNG CỨU|CẨM NANG KHẮC PHỤC|CẨM NANG XỬ LÝ)",
]

COMPANIES: list[str] = [
    "01_Company_Computer_Vision_CV",
    "02_Company_Machine_Learning_ML",
    "03_Company_Network_Management_NMA",
    "04_Company_Network_Security_SEC",
    "05_Company_Japanese_Language_JPN",
    "06_Venture_PBL6_VietLawAssist_LegalAI",
    "07_Company_Algorithms_and_Systems_ALGO",
    "08_Company_Software_Craftsmanship_and_Architecture_CRAFT",
    "09_Company_Agile_and_DevOps_Engineering_AGILE",
    "10_Company_WebScale_FullStack_Technologies_WEB",
    "11_Company_PyScale_Backend_and_Distributed_PY",
]

REQUIRED_CORE_FILES: list[str] = [
    "COMPANY_CHARTER.md",
    "STATUS.md",
]

# ---------------------------------------------------------------------------
# Fixed link pattern (v1.0 had a broken character class)
# Matches:
#   [text](file:///absolute/path)
#   [text](relative/path)
# Excludes:
#   http://, https://, mailto:, pure anchor (#...)
# ---------------------------------------------------------------------------
_LINK_RE = re.compile(
    r"\[([^\]]+)\]"                              # [link text]
    r"\("                                         # opening paren
    r"(file:///[^)\s#]+(?:#[^)\s]*)?"            # file:/// absolute
    r"|(?!https?://|mailto:)(?!#)[^)\s]+"        # OR relative (not http/mailto/anchor)
    r")"
    r"\)",                                        # closing paren
    re.UNICODE,
)


class HoldingAuditor:
    def __init__(self, root_dir: Path) -> None:
        self.root = root_dir
        self.total_links_checked: int = 0
        self.broken_links: list[tuple[str, str, str]] = []  # (file, text, target)
        self.charter_scores: dict[str, float] = {}
        self.fatal_vetos: list[str] = []
        self.missing_core_files: list[str] = []

    # ------------------------------------------------------------------
    # LEVEL 1-A: Broken Link Scan
    # ------------------------------------------------------------------
    def audit_broken_links(self) -> float:
        """
        Scan every .md file for dead file:/// links and invalid relative paths.

        MQAVP rule: ANY broken link → link_score = 0.0 (absolute zero-tolerance).
        """
        md_files = [
            f for f in self.root.rglob("*.md")
            if ".git" not in f.parts
        ]

        valid = 0
        total = 0

        for md_file in md_files:
            try:
                content = md_file.read_text(encoding="utf-8", errors="ignore")
            except OSError as exc:
                self.broken_links.append((str(md_file), "FILE_READ_ERROR", str(exc)))
                continue

            for match in _LINK_RE.finditer(content):
                total += 1
                link_text: str = match.group(1)
                target: str = match.group(2)

                if target.startswith("file:///"):
                    # Strip anchor, normalise Windows path
                    raw_path = target[len("file:///"):]
                    raw_path = raw_path.split("#")[0]
                    # URL-decode %20 etc.
                    try:
                        from urllib.parse import unquote
                        raw_path = unquote(raw_path)
                    except Exception:
                        pass
                    target_path = Path(raw_path)
                    if target_path.exists():
                        valid += 1
                    else:
                        self.broken_links.append(
                            (str(md_file.relative_to(self.root)), link_text, target)
                        )

                else:
                    # Relative link: strip anchor
                    rel = target.split("#")[0] if "#" in target else target
                    if not rel:
                        # Pure anchor in same file — treat as valid
                        valid += 1
                        continue
                    resolved = (md_file.parent / rel).resolve()
                    if resolved.exists():
                        valid += 1
                    else:
                        self.broken_links.append(
                            (str(md_file.relative_to(self.root)), link_text, target)
                        )

        self.total_links_checked = total
        if total == 0:
            return 100.0

        # MQAVP HARD RULE: any broken link → score = 0
        if self.broken_links:
            return 0.0

        return 100.0

    # ------------------------------------------------------------------
    # LEVEL 1-B: 7-Tier Charter Schema
    # ------------------------------------------------------------------
    def audit_charter_schemas(self) -> float:
        """Check all DEPARTMENT_CHARTER.md files for 7-tier compliance."""
        charter_files = [
            f for f in self.root.rglob("DEPARTMENT_CHARTER.md")
            if ".git" not in f.parts
        ]
        if not charter_files:
            self.fatal_vetos.append("FATAL: Zero DEPARTMENT_CHARTER.md files found in holding!")
            return 0.0

        total_possible = len(charter_files) * len(TIER_HEADERS)
        matched = 0

        for cf in sorted(charter_files):
            rel_name = str(cf.relative_to(self.root))
            content = cf.read_text(encoding="utf-8", errors="ignore")
            found = 0
            for pattern in TIER_HEADERS:
                if re.search(pattern, content, re.IGNORECASE):
                    matched += 1
                    found += 1
            pct = (found / len(TIER_HEADERS)) * 100.0
            self.charter_scores[rel_name] = pct

        return (matched / total_possible) * 100.0 if total_possible > 0 else 0.0

    # ------------------------------------------------------------------
    # LEVEL 1-C: Core Asset Verification
    # ------------------------------------------------------------------
    def audit_company_core_assets(self) -> float:
        """Verify each company has COMPANY_CHARTER.md, STATUS.md, and AGENT_PROFILE.md."""
        total_checks = len(COMPANIES) * (len(REQUIRED_CORE_FILES) + 1)  # +1 for agent profile
        passed = 0

        for comp in COMPANIES:
            comp_path = self.root / comp
            if not comp_path.exists():
                self.fatal_vetos.append(f"FATAL: Company folder missing: {comp}")
                continue

            for fname in REQUIRED_CORE_FILES:
                if (comp_path / fname).exists():
                    passed += 1
                else:
                    self.missing_core_files.append(f"{comp}/{fname}")

            # Agent profile can be in multiple locations
            profile_found = (
                (comp_path / "AGENT_PROFILE.md").exists()
                or (comp_path / "01_Strategy_and_Curriculum" / "AGENT_PROFILE.md").exists()
                or (comp_path / ".agents" / "rules" / "AGENTS.md").exists()
                or (comp_path / "01_Strategy_and_Proposal" / "AGENT_PROFILE.md").exists()
            )
            if profile_found:
                passed += 1
            else:
                self.missing_core_files.append(f"{comp}/AGENT_PROFILE.md (not found in any expected location)")

        return (passed / total_checks) * 100.0

    # ------------------------------------------------------------------
    # Report generation
    # ------------------------------------------------------------------
    def generate_report(self, json_output: bool = False) -> str:
        link_score_raw = self.audit_broken_links()
        schema_score = self.audit_charter_schemas()
        core_score = self.audit_company_core_assets()

        # Weighted Level-1 total (per MQAVP spec)
        level_1 = (link_score_raw * 0.40) + (schema_score * 0.40) + (core_score * 0.20)
        passed = level_1 >= 60.0 and len(self.fatal_vetos) == 0

        if json_output:
            data = {
                "link_score": round(link_score_raw, 2),
                "broken_links_count": len(self.broken_links),
                "schema_score": round(schema_score, 2),
                "core_asset_score": round(core_score, 2),
                "level_1_total": round(level_1, 2),
                "passed": passed,
                "fatal_vetos": self.fatal_vetos,
                "broken_links": self.broken_links[:20],
                "charter_scores": self.charter_scores,
            }
            return json.dumps(data, ensure_ascii=False, indent=2)

        lines: list[str] = []
        lines.append("# 📊 HOLDING SYSTEM AUDIT REPORT — Level 1 (Structure & Schema)")
        lines.append(f"> **Root:** `{self.root}`")
        lines.append(f"> **Total links scanned:** {self.total_links_checked}")
        lines.append(f"> **Broken links found:** {len(self.broken_links)}")
        lines.append(f"> **Link Integrity Score:** {link_score_raw:.2f}% {'✅' if link_score_raw == 100.0 else '❌ (MQAVP: must be 100%)'}")
        lines.append(f"> **Schema 7-Tier Score:** {schema_score:.2f}%")
        lines.append(f"> **Core Assets Score:** {core_score:.2f}%")
        lines.append(f"> **LEVEL-1 TOTAL:** **{level_1:.2f}%**")
        verdict = "✅ PASS" if passed else "❌ FATAL FAIL"
        lines.append(f"> **VERDICT:** {verdict}\n")

        if self.fatal_vetos:
            lines.append("### 🚨 FATAL VETOS:")
            for v in self.fatal_vetos:
                lines.append(f"- ❌ {v}")
            lines.append("")

        if self.broken_links:
            lines.append("### ⚠️ BROKEN LINKS (first 20):")
            for f, text, target in self.broken_links[:20]:
                lines.append(f"- `{f}`: [{text}]({target}) → **NOT FOUND**")
            if len(self.broken_links) > 20:
                lines.append(f"- ... và {len(self.broken_links) - 20} broken links khác.")
            lines.append("")

        if self.missing_core_files:
            lines.append("### 📁 MISSING CORE FILES:")
            for m in self.missing_core_files:
                lines.append(f"- ❌ `{m}`")
            lines.append("")

        lines.append("### 🏛️ SCHEMA SCORES BY DEPARTMENT:")
        for name, score in sorted(self.charter_scores.items()):
            if score == 100.0:
                icon = "🟢"
                label = "PERFECT"
            elif score >= 60.0:
                icon = "🟡"
                label = "PARTIAL"
            else:
                icon = "🔴"
                label = "FAILING"
            lines.append(f"- `{name}`: **{score:.1f}%** ({icon} {label})")

        return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="HSQA-v2.0 — Holding System Quality Auditor"
    )
    parser.add_argument(
        "--root", type=Path, default=HOLDING_ROOT,
        help="Root directory of the School Holdings workspace"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output results as JSON instead of markdown"
    )
    parser.add_argument(
        "--save", action="store_true",
        help="Save report to 00_Corporate_Knowledge_Vault/LEVEL_1_AUDIT_REPORT.md"
    )
    args = parser.parse_args()

    auditor = HoldingAuditor(args.root.resolve())
    report = auditor.generate_report(json_output=args.json)
    print(report)

    if args.save and not args.json:
        out_path = args.root / "00_Corporate_Knowledge_Vault" / "LEVEL_1_AUDIT_REPORT.md"
        out_path.write_text(report, encoding="utf-8")
        print(f"\n[OK] Report saved → {out_path}")


if __name__ == "__main__":
    main()
