from datetime import datetime
from utils.ephem_utils import get_planet_positions, get_aspects, get_moon_phase
from utils.file_utils import save_markdown_report

def generate_daily_report(date: datetime):
    print(f"📅 Генерация отчета за {date.strftime('%Y-%m-%d')}...")

    positions = get_planet_positions(date)
    aspects = get_aspects(positions)
    moon_phase = get_moon_phase(date)

    markdown = f"# 🪐 Астрологический отчет за {date.strftime('%Y-%m-%d')}\n\n"
    markdown += f"## 🌕 Фаза Луны: {moon_phase}\n\n"
    markdown += "## 📍 Положение планет:\n"
    for planet, pos in positions.items():
        markdown += f"- {planet}: {pos}\n"

    markdown += "\n## 🔭 Аспекты:\n"
    if aspects:
        for aspect in aspects:
            markdown += f"- {aspect}\n"
    else:
        markdown += "- Нет мажорных аспектов сегодня.\n"

    save_markdown_report(date, markdown)
    print("✅ Отчет успешно создан и сохранён.")
