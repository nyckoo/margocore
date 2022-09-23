from math import floor

# BASE features assignment from very start


def get_base_features(lvl: int, prof: str):

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

# Other statistics derived from 'BASE'


def get_base_attack_speed(agility: int):
    base_sa = 100
    if agility < 101:
        base_sa += agility * 2
    else:
        base_sa += 100 * 2
        base_sa += (agility - 100) * 0.2
    return round(base_sa)


def get_base_health_points(lvl: int, strength: int):
    return floor(20 * pow(lvl, 1.375)) + (strength * 5)


def get_base_dodge_points(agility: int):
    return round(agility / 30)


def get_base_crit_chance(lvl: int):
    return 1.0 + (lvl * 0.02)


def get_base_physical_crit(lvl: int, strength: int):
    return 120 + round(strength / (0.5 * lvl))


def get_base_magical_crit(lvl: int, intellect: int):
    return 120 + round(intellect / (0.5 * lvl))

# Stats getter aggregator


def get_all_params(lvl: int, l_stats: dict):

    params = (
        'crit_strike',
        'attack_speed',
        'health_points',
        'dodge',
        'physical_crit',
        'magical_crit'
    )

    stats_result = (
        get_base_crit_chance(lvl),
        get_base_attack_speed(l_stats['agility']),
        get_base_health_points(lvl, l_stats['strength']),
        get_base_dodge_points(l_stats['agility']),
        get_base_physical_crit(lvl, l_stats['strength']),
        get_base_physical_crit(lvl, l_stats['intellect'])
    )

    for idx in range(len(params)):
        if params[idx] in l_stats:
            l_stats[params[idx]] += stats_result[idx]
        else:
            l_stats[params[idx]] = stats_result[idx]

    # Adding hp from p/w stat 'strength_hp'
    if 'strength_hp' in l_stats:
        l_stats['health_points'] += \
            round(l_stats['strength_hp'] * l_stats['strength'])

    return l_stats
