from skyfield.api import load
from datetime import datetime
import math

def get_planet_positions(date):
    planets = load('de440s.bsp')
    ts = load.timescale()
    t = ts.utc(date.year, date.month, date.day)

    names = ['MERCURY', 'VENUS', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 'NEPTUNE', 'PLUTO', 'MOON', 'SUN']
    positions = {}

    for name in names:
        planet = planets[name]
        astrometric = planets['EARTH'].at(t).observe(planet).apparent()
        ra, dec, _ = astrometric.radec()
        ecl = planets['EARTH'].at(t).observe(planet).apparent().ecliptic_latlon()
        lon = ecl[1].degrees
        positions[name] = {
            'lon': lon,
            'ra': ra.hours,
            'dec': dec.degrees
        }

    return positions

def get_aspects(positions):
    aspects = []
    aspect_angles = {
        'Conjunction': 0,
        'Opposition': 180,
        'Trine': 120,
        'Square': 90,
        'Sextile': 60
    }
    orb = 6  # орбис 6°

    planet_names = list(positions.keys())
    for i in range(len(planet_names)):
        for j in range(i + 1, len(planet_names)):
            p1 = planet_names[i]
            p2 = planet_names[j]
            lon1 = positions[p1]['lon']
            lon2 = positions[p2]['lon']
            diff = abs(lon1 - lon2)
            if diff > 180:
                diff = 360 - diff
            for name, angle in aspect_angles.items():
                if abs(diff - angle) <= orb:
                    aspects.append(f"{p1} {name} {p2} ({round(diff,1)}°)")
    return aspects

def get_moon_phase(date, t):
    eph = load('de440s.bsp')
    sun = eph['SUN']
    moon = eph['MOON']
    earth = eph['EARTH']

    astrometric_moon = earth.at(t).observe(moon).apparent()
    astrometric_sun = earth.at(t).observe(sun).apparent()

    _, moon_lon, _ = astrometric_moon.ecliptic_latlon()
    _, sun_lon, _ = astrometric_sun.ecliptic_latlon()

    phase_angle = (moon_lon.degrees - sun_lon.degrees) % 360

    if phase_angle < 45:
        return "🌑 New Moon"
    elif phase_angle < 90:
        return "🌒 Waxing Crescent"
    elif phase_angle < 135:
        return "🌓 First Quarter"
    elif phase_angle < 180:
        return "🌔 Waxing Gibbous"
    elif phase_angle < 225:
        return "🌕 Full Moon"
    elif phase_angle < 270:
        return "🌖 Waning Gibbous"
    elif phase_angle < 315:
        return "🌗 Last Quarter"
    else:
        return "🌘 Waning Crescent"
