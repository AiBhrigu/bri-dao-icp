import datetime

def generate_report_text(date_str: str, planet_positions: dict, aspects: list) -> str:
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

    report_lines = [
        f"# Астрологический отчет на {date_obj.strftime('%d.%m.%Y')}",
        "",
        "## 🌍 Положение планет",
        ""
    ]

    for planet, pos in planet_positions.items():
        report_lines.append(f"- **{planet}**: {pos:.2f}°")

    report_lines.append("")
    report_lines.append("## 🔭 Основные аспекты")
    report_lines.append("")

    if aspects:
        for aspect in aspects:
            p1, aspect_name, p2 = aspect
            report_lines.append(f"- {p1} {aspect_name} {p2}")
    else:
        report_lines.append("Нет значимых аспектов.")

    return "\n".join(report_lines)


def save_markdown_report(content: str, date_str: str):
    from pathlib import Path

    output_dir = Path("daily_reports")
    output_dir.mkdir(exist_ok=True)

    file_path = output_dir / f"{date_str}.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

