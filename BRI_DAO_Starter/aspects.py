# utils/aspects.py
import math

# Основные аспекты и их допуски (орбисы)
ASPECTS = {
    "Conjunction": (0, 8),
    "Opposition": (180, 8),
    "Trine": (120, 6),
    "Square": (90, 6),
    "Sextile": (60, 4),
}

def angle_diff(a, b):
    """Возвращает разницу между двумя углами в пределах [0, 180]"""
    diff = abs(a - b) % 360
    return diff if diff <= 180 else 360 - diff

def find_aspects(planets):
    """Ищет аспекты между парами планет"""
    results = []
    names = list(planets.keys())

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            name1, name2 = names[i], names[j]
            angle1, angle2 = planets[name1], planets[name2]
            diff = angle_diff(angle1, angle2)

            for aspect, (target, orb) in ASPECTS.items():
                if abs(diff - target) <= orb:
                    results.append((name1, name2, aspect, round(diff, 2)))
                    break

    return results
