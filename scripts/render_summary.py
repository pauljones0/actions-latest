"""Bounded job summary with immutable links to full published review artifacts."""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def summarize_changes(text: str, limit: int = 12000) -> str:
    header, *sections = text.split("\n## ")
    result = header
    for index, section in enumerate(sections):
        candidate = "\n## " + section
        if len(result) + len(candidate) > limit or index >= 3:
            result += "\n\nAdditional details are in the complete change report linked above.\n"
            break
        result += candidate
    return result


def main():
    commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, timeout=10
    ).strip()
    prefix = f"https://github.com/pauljones0/actions-latest/blob/{commit}/data"
    print(
        f"[Complete changes]({prefix}/catalog-changes.md) · [Review queue]({prefix}/review-queue.json)"
    )
    print(summarize_changes((ROOT / "data/catalog-changes.md").read_text()))
    print(
        (ROOT / "data/maintenance.md")
        .read_text()
        .replace("/blob/main/data/", f"/blob/{commit}/data/")
    )


if __name__ == "__main__":
    main()
