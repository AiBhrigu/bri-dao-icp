def save_markdown_report(markdown: str, date_str: str):
    filename = f"history/{date_str}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"✅ Отчет сохранен: {filename}")
