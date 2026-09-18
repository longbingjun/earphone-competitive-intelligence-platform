"""Reject company identifiers, secrets, production records and internal runbooks."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SELF = Path(__file__).resolve()
TEXT_SUFFIXES = {".py", ".md", ".json", ".yml", ".yaml", ".ts", ".tsx", ".astro", ".mjs", ".ini", ".txt", ".example"}

FORBIDDEN_PATHS = {
    "docs/IT_DEPLOYMENT_HANDOFF.md",
    "docs/DEPLOYMENT_ARC_POSTGRES_MINIO.md",
    "data/reports",
    "data/videos",
    "data/staging",
    "data/enrich",
    "data/cache",
    "data/seed",
}

# Build organization-specific tokens from fragments so this validator does not
# trigger itself when scanning the repository.
FORBIDDEN_PATTERNS = {
    "organization email/domain": re.compile(r"@sho" + r"kz|gitlab\.sho" + r"kz", re.I),
    "employee identifier": re.compile(r"\b0" + r"17642\b|\b0" + r"14744\b"),
    "employee name": re.compile("龙" + "秉君|张" + "华"),
    "private IPv4 address": re.compile(r"(?<!\d)(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})(?!\d)"),
    "legacy secret variable": re.compile("DEFAULT_MODEL_" + "API_KEY|VIDEO_LLM_" + "API_KEY|VIDEO_" + "COOKIES_FILE|DEEPSEEK_" + "API_KEY"),
    "internal filesystem path": re.compile(r"D:\\intelligences-from-" + r"52audio-local|/data/" + r"52audio", re.I),
    "obvious secret value": re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b|SESS" + r"DATA\s*=|bili_" + r"jct\s*=", re.I),
}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> None:
    failures: list[str] = []
    for forbidden in FORBIDDEN_PATHS:
        if (ROOT / forbidden).exists():
            failures.append(f"forbidden path exists: {forbidden}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or path.resolve() == SELF:
            continue
        rel = relative(path)
        if any(part in {".git", ".venv", "node_modules", "site", "__pycache__"} for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"Dockerfile", "Dockerfile.video-worker", ".env.example"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in FORBIDDEN_PATTERNS.items():
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                failures.append(f"{label}: {rel}:{line}")

    if failures:
        raise SystemExit("\n".join(["Public repository validation failed:", *failures]))
    print("Public repository validation passed.")


if __name__ == "__main__":
    main()
