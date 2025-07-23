from skyfield.api import load
from skyfield.data import mpc
from skyfield.positionlib import Geocentric
import numpy as np
import math

planets_of_interest = [
    'Sun', 'Moon', 'Mercury', 'Venus', 'Mars',
    'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'
]

ASPECTS_DEGREES = {
    'Conjunction': 0,
    'Opposition': 180,
    'Trine': 120,
    'Square': 90,
    'Sextile': 60
}

ASPECT_ORB = 6  # +/- degrees tolerance for aspects

def get_planet_positions(t):
    eph = load('data/de440s.bsp')
    earth = eph['earth']

    positions = {}
    for name in planets_of_interest:
        if name == 'Sun':
            astrometric = earth.at(t).observe(eph['sun']).apparent()
        elif name == 'Moon':
            astrometric = earth.at(t).observe(eph['moon']).apparent()
        else:
            astrometric = earth.at(t).observe(eph[name.lower()]).apparent()

        ra, dec, distance = astrometric.radec()
        ecliptic = astrometric.ecliptic_latlon()
        lon_deg = ecliptic[1].degrees % 360
        positions[name] = lon_deg

    return positions

def calculate_aspect(angle1, angle2):
    diff = abs(angle1 - angle2) % 360
    diff = min(diff, 360 - diff)
    for aspect, exact in ASPECTS_DEGREES.items():
        if abs(diff - exact) <= ASPECT_ORB:
            return aspect
    return None

def get_aspects(positions):
    aspects = []
    planets = list(positions.keys())
    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            p1, p2 = planets[i], planets[j]
            aspect = calculate_aspect(positions[p1], positions[p2])
            if aspect:
                aspects.append({
                    'planet1': p1,
                    'planet2': p2,
                    'aspect': aspect
                })
    return aspects

def get_moon_phase(date_str, t):
    eph = load('data/de440s.bsp')
    earth = eph['earth']
    sun = eph['sun']
    moon = eph['moon']

    e = earth.at(t)
    sun_pos = e.observe(sun).apparent()
    moon_pos = e.observe(moon).apparent()

    sun_lon = sun_pos.ecliptic_latlon()[1].degrees
    moon_lon = moon_pos.ecliptic_latlon()[1].degrees
    angle = (moon_lon - sun_lon) % 360

    if angle < 22.5:
        return "New Moon"
    elif angle < 67.5:
        return "Waxing Crescent"
    elif angle < 112.5:
        return "First Quarter"
    elif angle < 157.5:
        return "Waxing Gibbous"
    elif angle < 202.5:
        return "Full Moon"
    elif angle < 247.5:
        return "Waning Gibbous"
    elif angle < 292.5:
        return "Last Quarter"
    elif angle < 337.5:
        return "Waning Crescent"
    else:
        return "New Moon"
