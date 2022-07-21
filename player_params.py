from math import floor


def get_all_features(lvl: int, prof: str):

    def h_stats(lvl: int, base: dict):
        for _ in range(2, 21):
            base['strength'] += 1
            base['agility'] += 4
        for _ in range(21, lvl + 1):
            base['agility'] += 5
        return base

    def m_stats(lvl: int, base: dict):
        for _ in range(2, 21):
            base['strength'] += 1
            base['agility'] += 1
            base['intellect'] += 3
        for _ in range(21, lvl + 1):
            base['intellect'] += 5
        return base

    def w_stats(lvl: int, base: dict):
        for _ in range(2, 21):
            base['strength'] += 4
            base['agility'] += 1
        for _ in range(21, lvl + 1):
            base['strength'] += 5
        return base

    def t_stats(lvl: int, base: dict):
        for _ in range(2, 21):
            base['strength'] += 1
            base['agility'] += 2
            base['intellect'] += 2
        for i in range(21, lvl + 1):
            if i % 2 == 0:
                base['agility'] += 2
                base['intellect'] += 3
            else:
                base['agility'] += 3
                base['intellect'] += 2
        return base

    def p_stats(lvl: int, base: dict):
        # small tweak from standard approach because of half values
        base['strength'] += 2
        base['agility'] += 1
        base['intellect'] += 2
        for _ in range(3, 21):
            base['strength'] += 2.5
            base['agility'] += 0.5
            base['intellect'] += 2
        for i in range(21, lvl + 1):
            if i % 2 == 0:
                base['strength'] += 2
                base['intellect'] += 3
            else:
                base['strength'] += 3
                base['intellect'] += 2
        return {k: int(v) for k, v in base.items()}

    def b_stats(lvl: int, base: dict):
        for _ in range(2, 21):
            base['strength'] += 3
            base['agility'] += 2
        for i in range(21, lvl + 1):
            if i % 2 == 0:
                base['strength'] += 2
                base['agility'] += 3
            else:
                base['strength'] += 3
                base['agility'] += 2
        return base

    base_f = {'strength': 4, 'agility': 3, 'intellect': 3}

    prof_to_f = {
        'h': h_stats,
        'm': m_stats,
        'w': w_stats,
        't': t_stats,
        'p': p_stats,
        'b': b_stats,
    }

    return prof_to_f[prof](lvl, base_f)


def get_attack_speed(agility: int, eq_as: int):
    base_sa = 100
    if agility < 101:
        base_sa += agility * 2
    else:
        base_sa += 100 * 2
        base_sa += (agility - 100) * 0.2
    base_sa += eq_as
    return float(base_sa / 100)


def get_health_points(lvl: int):
    return floor(20 * pow(lvl, 1.375))
