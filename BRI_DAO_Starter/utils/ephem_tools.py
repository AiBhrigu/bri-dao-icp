# utils/ephem_tools.py

from skyfield.api import load
from datetime import datetime

def get_planet_positions(date=None):
    planets = ['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
    ts = load.timescale()

    if date is None:
        t = ts.now()
    else:
        t = ts.utc(datetime.strptime(date, "%Y-%m-%d"))

    eph = load('data/de440s.bsp')
    observer = eph['earth']

    positions = {}
    for name in planets:
        try:
            planet = eph[name]
            astrometric = observer.at(t).observe(planet).ecliptic_latlon()
            longitude = astrometric[1].degrees
            positions[name.capitalize()] = round(longitude, 2)
        except KeyError:
            continue

    return positions
