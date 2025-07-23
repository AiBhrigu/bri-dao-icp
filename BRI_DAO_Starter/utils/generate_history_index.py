# utils/generate_history_index.py

import os
import datetime
from pathlib import Path

HISTORY_DIR = Path("docs/history")
INDEX_FILE = HISTORY_DIR / "index.md"

def generate_index():
    entries = []
    for file in sorted(HISTORY_DIR.glob("20*.md")):
        if file.name == "index.md":
            continue
        date_str = file.stem
        entries.append(f"- [{date_str}](./{date_str}.md)")

    index_content = "# Исторический индекс\n\n" + "\n".join(entries)
    INDEX_FILE.write_text(index_content, encoding="utf-8")
    print(f"✅ Индекс обновлён: {INDEX_FILE}")
