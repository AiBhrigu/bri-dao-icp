import argparse
from skyfield.api import load
from datetime import datetime

def get_planet_positions(date_str=None):
    planets = load('data/de440s.bsp')
    ts = load.timescale()

    if date_str:
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            t = ts.utc(dt.year, dt.month, dt.day)
        except ValueError:
            print("⚠️ Неверный формат даты. Используйте YYYY-MM-DD.")
            return
    else:
        t = ts.now()

    eph = {
        'Sun': planets['sun'],
        'Moon': planets['moon'],
        'Mercury': planets['mercury'],
        'Venus': planets['venus'],
        'Mars': planets['mars'],
        'Jupiter': planets['jupiter barycenter'],
        'Saturn': planets['saturn barycenter'],
        'Uranus': planets['uranus barycenter'],
        'Neptune': planets['neptune barycenter'],
        'Pluto': planets['pluto barycenter']
    }

    earth = planets['earth']
    print(f"\n🪐 Положение планет на {t.utc_strftime('%Y-%m-%d %H:%M:%S UTC')}:\n")
    for name, body in eph.items():
        astrometric = earth.at(t).observe(body)
        lat, lon, distance = astrometric.ecliptic_latlon()
        print(f"{name:<9} {lon.degrees:>7.2f}°")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Показ эфемерид на дату')
    parser.add_argument('--date', type=str, help='Дата в формате YYYY-MM-DD')
    args = parser.parse_args()

    get_planet_positions(date_str=args.date)
