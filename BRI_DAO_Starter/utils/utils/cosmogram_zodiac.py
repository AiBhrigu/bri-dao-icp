# utils/cosmogram_zodiac.py

from skyfield.api import load
from datetime import datetime, timezone

# Загрузка эфемерид и шкалы времени
planets = load('data/de440s.bsp')
ts = load.timescale()

# Текущий момент времени
t = ts.now()
observer = planets['earth']

# Список планет
planet_names = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars',
                'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

# Названия знаков зодиака
zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

# Перевод градусов в знак зодиака
def get_zodiac(degrees):
    index = int(degrees // 30)
    sign = zodiac_signs[index]
    deg_in_sign = degrees % 30
    return f"{int(deg_in_sign):02d}° {sign}"

# Вывод положения планет
print(f"🪐 Космограмма на {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC:\n")

for name in planet_names:
    planet = planets[name]
    astrometric = observer.at(t).observe(planet).apparent()
    ecliptic = astrometric.ecliptic_latlon()
    longitude_deg = ecliptic[1].degrees
    zodiac = get_zodiac(longitude_deg)
    print(f"{name:<8} {zodiac}")
