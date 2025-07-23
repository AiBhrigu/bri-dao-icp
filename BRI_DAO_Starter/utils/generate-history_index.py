import os
from datetime import datetime
from skyfield.api import load

planets = load('data/de440s.bsp')
ts = load.timescale()

PLANET_NAMES = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

def get_planet_positions_for_date(date_str):
    t = ts.utc(datetime.strptime(date_str, "%Y-%m-%d"))
    results = []
    for name in PLANET_NAMES:
        planet = planets[name]
        astrometric = planets['earth'].at(t).observe(planet).ecliptic_position()
        lon_deg = astrometric[0].degrees % 360
        results.append((name, lon_deg))
    return results

def generate_daily_report(date_str):
    positions = get_planet_positions_for_date(date_str)
    report_lines = [f"# Исторический отчёт за {date_str}\n", "_(Автоматически созданный шаблон)_\n", "\n## Положение планет:\n"]
    for name, lon in positions:
        report_lines.append(f"- {name}: {lon:.2f}°")
    return "\n".join(report_lines)

def save_daily_report(date_str):
    content = generate_daily_report(date_str)
    file_path = f"docs/history/{date_str}.md"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Запуск генерации
if __name__ == "__main__":
    today_str = datetime.utcnow().strftime("%Y-%m-%d")
    save_daily_report(today_str)
