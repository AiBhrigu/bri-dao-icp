# utils/cosmogram_zodiac.py
from skyfield.api import load
from skyfield.data import mpc
from skyfield.api import N, W, wgs84
from datetime import datetime
from pytz import timezone
from skyfield.api import Loader

load = Loader('data')
planets = load('data/de440s.bsp')

# Текущая дата и время
ts = load.timescale()
t = ts.now()

# Список планет
planet_names = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
planet_keys = ['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter barycenter', 'saturn barycenter', 'uranus barycenter', 'neptune barycenter', 'pluto barycenter']

# Наблюдатель - геоцентр
observer = planets['earth']

# Знаки Зодиака
zodiacs = [
    '♈ Aries', '♉ Taurus', '♊ Gemini', '♋ Cancer',
    '♌ Leo', '♍ Virgo', '♎ Libra', '♏ Scorpio',
    '♐ Sagittarius', '♑ Capricorn', '♒ Aquarius', '♓ Pisces'
]

def zodiac_sign(deg):
    index = int(deg / 30) % 12
    return zodiacs[index]

# Расчёт координат
print("🪐 Космограмма (геоцентрическая)\n")
for name, key in zip(planet_names, planet_keys):
    planet = planets[key]
    astrometric = observer.at(t).observe(planet).apparent()
    ecl = astrometric.ecliptic_latlon()
    lon = ecl[1].degrees % 360
    sign = zodiac_sign(lon)
    print(f"{name:8} {lon:6.2f}° {sign}")
