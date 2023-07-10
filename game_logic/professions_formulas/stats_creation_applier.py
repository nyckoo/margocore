from math import floor


class StatsCreationApplier:
    def load_features_compounded_stats(self, summed_stats: dict[str, int], lvl: int):
        summed_stats['crit_strike'] = summed_stats.get('crit_strike', 0) + self.get_crit_chance(lvl)
        summed_stats['attack_speed'] = summed_stats.get('attack_speed', 0) + self.get_attack_speed(summed_stats['agility'])
        summed_stats['health_points'] = summed_stats.get('health_points', 0) + self.get_health_points(lvl, summed_stats['strength'])
        summed_stats['dodge'] = summed_stats.get('dodge', 0) + self.get_dodge_points(summed_stats['agility'])
        summed_stats['physical_crit'] = summed_stats.get('physical_crit', 0) + self.get_physical_crit(lvl, summed_stats['strength'])
        summed_stats['magical_crit'] = summed_stats.get('magical_crit', 0) + self.get_magical_crit(lvl, summed_stats['intellect'])

        # Adding hp from p/w stat 'strength_hp'
        if summed_stats.get('strength_hp', None):
            summed_stats['health_points'] += round(summed_stats['strength_hp'] * summed_stats['strength'])
        return summed_stats

    @staticmethod
    def load_all_features(base_stats: dict[str, int], eq_stats: dict[str, int]):
        all_features_stat = eq_stats.get('all_features', 0)
        for stat in base_stats.keys():
            eq_stats[stat] += all_features_stat
            eq_stats[stat] += base_stats[stat]
        eq_stats.pop('all_features', None)
        return eq_stats

    @staticmethod
    def get_attack_speed(agility: int):
        base_sa = 100
        if agility < 101:
            base_sa += agility * 2
        else:
            base_sa += 100 * 2
            base_sa += (agility - 100) * 0.2
        return round(base_sa)

    @staticmethod
    def get_health_points(lvl: int, strength: int):
        return floor(20 * pow(lvl, 1.375)) + (strength * 5)

    @staticmethod
    def get_dodge_points(agility: int):
        return round(agility / 30)

    @staticmethod
    def get_crit_chance(lvl: int):
        return 1.0 + (lvl * 0.02)

    @staticmethod
    def get_physical_crit(lvl: int, strength: int):
        return 120 + round(strength / (0.5 * lvl))

    @staticmethod
    def get_magical_crit(lvl: int, intellect: int):
        return 120 + round(intellect / (0.5 * lvl))