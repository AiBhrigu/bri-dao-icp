from skyfield.api import load
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Загрузка эфемерид
planets = load('data/de440s.bsp')
ts = load.timescale()

# Текущее UTC-время
now = datetime.utcnow()
t = ts.utc(now.year, now.month, now.day, now.hour, now.minute, now.second)

planet_names = [
    'sun', 'mercury', 'venus', 'earth', 'moon',
    'mars', 'jupiter barycenter', 'saturn barycenter',
    'uranus barycenter', 'neptune barycenter', 'pluto barycenter'
]

planet_colors = {
    "Sun": "gold",
    "Moon": "lightgray",
    "Mercury": "darkorange",
    "Venus": "orchid",
    "Mars": "red",
    "Jupiter": "saddlebrown",
    "Saturn": "dimgray",
    "Uranus": "skyblue",
    "Neptune": "blue",
    "Pluto": "darkred"
}

earth = planets["earth"]
angles = []

for name in planet_names:
    planet = planets[name]
    astrometric = earth.at(t).observe(planet).apparent()
    lon, lat, dist = astrometric.ecliptic_latlon()
    angles.append((name, lon.degrees % 360))

# Рисуем круг
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
ax.set_theta_direction(-1)
ax.set_theta_zero_location("E")
ax.set_rticks([])
ax.grid(True)

for name, lon in angles:
    theta = np.radians(lon)
    ax.plot(theta, 1, 'o', color=planet_colors.get(name, 'black'), label=name)
    ax.text(theta, 1.08, name, ha='center', va='center', fontsize=10)

ax.set_title(f"Космограмма на {now.strftime('%Y-%m-%d %H:%M:%S')} UTC", va='bottom')
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.show()
