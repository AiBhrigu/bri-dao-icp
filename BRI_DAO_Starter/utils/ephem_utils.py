from skyfield.api import load, Topos
from skyfield.api import N, E
from skyfield.almanac import moon_phase
from datetime import datetime
import math

# Планетарные коды NASA JPL (вместо имён)
PLANET_CODES = {
    'Sun': '10',
    'Moon': '301',
    'Mercury': '199',
    'Venus': '299',
    'Earth': '399',
    'Mars': '499',
    'Jupiter': '599',
    'Saturn': '699',
    'Uranus': '799',
    'Neptune': '899',
    'Pluto': '999'
}

# Загрузка эфемерид
eph = load('de440s.bsp')
ts = load.timescale()


from skyfield.api import load

def get_planet_positions(ts, date):
    planets = ['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
    eph = load('de421.bsp')
    obs = eph['earth'].at(ts.utc(date.year, date.month, date.day))
    positions = {}

    for planet in planets:
        body = eph[planet]
        astrometric = obs.observe(body)
        lon, lat, distance = astrometric.ecliptic_latlon()
        positions[planet.capitalize()] = round(lon.degrees, 2)

    return positions


def get_aspects(positions, orb=6):
    """Определяет аспекты между планетами с заданным орбом."""
    aspects = []
    aspect_angles = {
        0: 'Conjunction',
        60: 'Sextile',
        90: 'Square',
        120: 'Trine',
        180: 'Opposition',
    }

    planets = list(positions.keys())

    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            p1, p2 = planets[i], planets[j]
            lon1, lon2 = positions[p1], positions[p2]
            angle = abs(lon1 - lon2)
            angle = angle if angle <= 180 else 360 - angle

            for target_angle, name in aspect_angles.items():
                if abs(angle - target_angle) <= orb:
                    aspects.append((p1, p2, name, round(angle, 1)))

    return aspects


def get_moon_phase(date: datetime):
    """Определяет фазу Луны на заданную дату."""
    t = ts.utc(date.year, date.month, date.day)
    phase_angle = moon_phase(eph, t).degrees % 360

    if phase_angle < 45:
        return 'New Moon'
    elif phase_angle < 90:
        return 'First Quarter'
    elif phase_angle < 135:
        return 'Waxing Gibbous'
    elif phase_angle < 180:
        return 'Full Moon'
    elif phase_angle < 225:
        return 'Waning Gibbous'
    elif phase_angle < 270:
        return 'Last Quarter'
    else:
        return 'Waning Crescent'
