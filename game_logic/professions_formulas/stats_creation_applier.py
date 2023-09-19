from dataclasses import fields
from math import floor

from game_logic.structures.stats_utils import LegendaryBonuses, CounterStats


class StatsCreationApplier:
    def load_features_compounded_stats(self, summed_stats: dict[str, int], lvl: int) -> dict[str, int]:
        summed_stats['crit'] = summed_stats.get('crit', 0) + self._get_crit_chance(lvl)
        summed_stats['attack_speed'] = summed_stats.get('attack_speed', 0) + self._get_attack_speed(summed_stats['agility'])
        summed_stats['health_points'] = summed_stats.get('health_points', 0) + self._get_health_points(lvl, summed_stats['strength'])
        summed_stats['dodge'] = summed_stats.get('dodge', 0) + self._get_dodge_points(summed_stats['agility'])
        summed_stats['physical_crit'] = summed_stats.get('physical_crit', 0) + self._get_physical_crit(lvl, summed_stats['strength'])
        summed_stats['magical_crit'] = summed_stats.get('magical_crit', 0) + self._get_magical_crit(lvl, summed_stats['intellect'])

        # Adding hp from p/w stat 'strength_hp'
        if summed_stats.get('strength_hp', None):
            summed_stats['health_points'] += round(summed_stats['strength_hp'] * summed_stats['strength'])
        return summed_stats

    @staticmethod
    def load_all_features(base_stats: dict[str, int], eq_stats: dict[str, int]) -> dict[str, int]:
        all_features_stat = eq_stats.get('all_features', 0)
        for stat in base_stats.keys():
            current_stat = eq_stats.get(stat, 0)
            eq_stats[stat] = current_stat + all_features_stat
            eq_stats[stat] += base_stats[stat]
        eq_stats.pop('all_features', None)
        return eq_stats

    @staticmethod
    def convert_legendary_bonuses(legendary_bonuses_count: dict[str, int]) -> dict[str, int]:
        char_leg_bons = {}
        for bon, power in legendary_bonuses_count.items():
            char_leg_bons[bon] = round(
                getattr(LegendaryBonuses, bon) * (1 - .5 ** power) / .5)
        return char_leg_bons
        # {**char_leg_bons, **char.get_full_stats()}

    @staticmethod
    def get_counter_stats(full_stats: dict[str, int]) -> dict[str, int]:
        this_char_counter_stats = {}
        for stat in fields(CounterStats):
            this_char_counter_stats[stat.name] = full_stats.get(stat.name, 0)
        return this_char_counter_stats

    @staticmethod
    def _get_attack_speed(agility: int):
        base_sa = 100
        if agility < 101:
            base_sa += agility * 2
        else:
            base_sa += 100 * 2
            base_sa += (agility - 100) * 0.2
        return round(base_sa)

    @staticmethod
    def _get_health_points(lvl: int, strength: int):
        return floor(20 * pow(lvl, 1.375)) + (strength * 5)

    @staticmethod
    def _get_dodge_points(agility: int):  # omit rounding to even numbers -> +0.01
        return round(agility / 30 + 0.01)

    @staticmethod
    def _get_crit_chance(lvl: int):
        return 1.0 + (lvl * 0.02)

    @staticmethod
    def _get_physical_crit(lvl: int, strength: int):
        return 120 + round(strength / (0.5 * lvl))

    @staticmethod
    def _get_magical_crit(lvl: int, intellect: int):
        return 120 + round(intellect / (0.5 * lvl))
