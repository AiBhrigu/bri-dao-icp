from skyfield.api import load
from datetime import datetime
import os

# Путь к директории
HISTORY_DIR = "docs/history"

# Загружаем эфемериды
planets = load('data/de440s.bsp')
ts = load.timescale()
t = ts.now()

planet_names = {
    'Sun': 'Солнце',
    'Moon': 'Луна',
    'Mercury': 'Меркурий',
    'Venus': 'Венера',
    'Mars': 'Марс',
    'Jupiter': 'Юпитер',
    'Saturn': 'Сатурн',
    'Uranus': 'Уран',
    'Neptune': 'Нептун',
    'Pluto': 'Плутон',
}

# Получение координат
def get_positions():
    earth = planets['earth']
    result = []
    for name in planet_names:
        planet = planets[name]
        astrometric = earth.at(t).observe(planet)
        ecl = astrometric.ecliptic_latlon()
        deg = ecl[1].degrees % 360
        result.append((planet_names[name], round(deg, 2)))
    return result

# Форматируем результат
def format_report():
    lines = ["# Исторический отчёт за " + t.utc_strftime('%Y-%m-%d'), "", "_(Автоматически сгенерировано)_", ""]
    lines.append("## 🌌 Положение планет:")
    lines.append("")
    for name, deg in get_positions():
        lines.append(f"- **{name}**: {deg}°")
    lines.append("")
    lines.append(f"_Сгенерировано: {datetime.utcnow().isoformat()} UTC_")
    return "\n".join(lines)

# Сохраняем файл
def save_history_file():
    date_str = t.utc_strftime('%Y-%m-%d')
    filename = os.path.join(HISTORY_DIR, f"{date_str}.md")
    if not os.path.exists(HISTORY_DIR):
        os.makedirs(HISTORY_DIR)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(format_report())
    print(f"✅ Исторический отчёт сохранён: {filename}")

# Запуск
if __name__ == "__main__":
    save_history_file()
