from skyfield.api import load
from datetime import datetime
import sys

# Загрузка эфемерид и времени
ts = load.timescale()
planets = load('data/de440s.bsp')

# Получаем дату из аргументов или используем текущую
if len(sys.argv) > 1:
    try:
        date_input = sys.argv[1]
        dt = datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("❌ Неверный формат даты. Используй YYYY-MM-DD.")
        sys.exit(1)
else:
    dt = datetime.utcnow()

t = ts.utc(dt.year, dt.month, dt.day)

# Список планет
from skyfield.api import load

ts = load.timescale()
t = ts.now()

planets = load('data/de440s.bsp')
observer = planets['earth']

planet_map = {
    'Sun': 'sun',
    'Moon': 'moon',
    'Mercury': 'mercury',
    'Venus': 'venus',
    'Mars': 'mars',
    'Jupiter': 'jupiter barycenter',
    'Saturn': 'saturn barycenter',
    'Uranus': 'uranus barycenter',
    'Neptune': 'neptune barycenter',
    'Pluto': 'pluto barycenter'
}

for name in planet_map:
    planet = planets[planet_map[name]]
    astrometric = observer.at(t).observe(planet)
    apparent = astrometric.apparent()
    ra, dec, distance = apparent.radec()
    print(f'{name:8s} RA: {ra}  DEC: {dec}')
