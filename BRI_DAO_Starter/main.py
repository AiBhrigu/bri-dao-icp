import argparse
from datetime import datetime
from skyfield.api import load
from ephem_utils import get_planet_positions

def main(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    eph = load('de421.bsp')
    ts = load.timescale()
    positions = get_planet_positions(eph, ts, date)

    print(f"🪐 Положение планет на {date.date()}:")
    for planet, (ra, dec) in positions.items():
        print(f"{planet:8}: RA = {ra:.2f}°, Dec = {dec:.2f}°")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Астрономические координаты планет')
    parser.add_argument('--date', required=True, help='Дата в формате ГГГГ-ММ-ДД')
    args = parser.parse_args()
    main(args.date)
