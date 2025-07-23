def get_planet_positions(eph, ts, date):
    planets = [
        'sun',
        'moon',
        'mercury',
        'venus',
        'mars',
        'jupiter barycenter',
        'saturn barycenter',
        'uranus barycenter',
        'neptune barycenter',
        'pluto barycenter'
    ]
    
    positions = {}
    obs = eph['earth'].at(ts.utc(date.year, date.month, date.day))

    for name in planets:
        body = eph[name]
        astrometric = obs.observe(body)
        ra, dec, _ = astrometric.radec()
        label = name.split()[0].capitalize()
        positions[label] = (ra.degrees, dec.degrees)

    return positions
