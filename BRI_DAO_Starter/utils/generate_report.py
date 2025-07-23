kfrom utils.ephem_tools import get_planet_positions
from utils.markdown_tools import format_report
import os

def generate_daily_report(date=None):
    """
    Генерирует ежедневный астрологический отчет за указанную дату (или текущую, если не задана).
    """
    print(f"📅 Генерация отчета за {date}...")

    # Получаем позиции планет на заданную дату
    positions = get_planet_positions(date=date)

    # Формируем Markdown-отчет
    report_md = format_report(positions, date=date)

    # Сохраняем файл в history/YYYY/MM/DD.md

