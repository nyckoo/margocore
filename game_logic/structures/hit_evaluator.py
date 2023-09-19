from random import random, randrange


class HitEvaluator:
    turn_effects_store = {}

    def evaluate_hit(self, updatibles: dict) -> dict:
        dmg_stats = self._apply_dmgs(**updatibles['attack_types'])
        drawn_chances = self._apply_chances(**updatibles['chanceable'])
        to_be_reduced = self._apply_reductions(**updatibles['reducable'])
        hit_stats_summary = {}
        # draw statistics with percentage chance
        for stat, val in drawn_chances.items():
            hit_stats_summary[stat] = val
        # apply standard damage stats
        for stat, val in dmg_stats.items():
            hit_stats_summary[stat] = val
        # apply reducable stats
        for stat, val in to_be_reduced.items():
            hit_stats_summary[stat] = val
        # apply enhanced hit stats
        if hit_stats_summary.get('crit'):
            for magic_crit_dmg_stat in ('fire_dmg', 'light_dmg', 'frost_dmg'):
                if hit_stats_summary.get(magic_crit_dmg_stat):
                    hit_stats_summary[magic_crit_dmg_stat] *= dmg_stats.get('magical_crit', 1)
            if hit_stats_summary.get('physical_dmg'):
                hit_stats_summary['physical_dmg'] *= dmg_stats.get('physical_crit', 1)
        if hit_stats_summary.get('verycrit'):
            for magic_crit_dmg_stat in ('fire_dmg', 'light_dmg', 'frost_dmg'):
                if hit_stats_summary.get(magic_crit_dmg_stat):
                    hit_stats_summary[magic_crit_dmg_stat] *= 2
            if hit_stats_summary.get('physical_dmg'):
                hit_stats_summary['physical_dmg'] *= 2
        if hit_stats_summary.get('holytouch'):
            self.turn_effects_store['off']['holytouch'] = 2
        return hit_stats_summary

    def _apply_dmgs(self, **attack_stats):
        return {attack_stat: self.__evaluate_effect(attack_stat, value) for attack_stat, value in attack_stats.items()}

    @staticmethod
    def _apply_chances(**chanceable_stats):
        return {stat: True if random() < value else False for stat, value in chanceable_stats.items()}

    @staticmethod
    def _apply_reductions(**reducable_stats):
        return {stat: value for stat, value in reducable_stats.items()}

    @staticmethod
    def __evaluate_effect(off_stat, value):
        def _compute_physical_dmg(phys_dmg):
            return randrange(round(0.9 * phys_dmg), round(1.1 * phys_dmg))

        def _compute_fire_dmg(fire_dmg):
            return

        def _compute_light_dmg(light_dmg):
            return

        def _compute_frost_dmg(frost_dmg):
            return

        def _compute_poison_dmg(poison_dmg):
            return

        def _compute_wound_dmg(wound_dmg):
            return

        def _apply_frost_slow(frost_slow):
            return

        def _apply_poison_slow(poison_slow):
            return

        effects_types = {
            'physical_dmg': _compute_physical_dmg,
            'fire_dmg': _compute_fire_dmg,
            'light_dmg': _compute_light_dmg,
            'frost_dmg': _compute_frost_dmg,
            'poison_dmg': _compute_poison_dmg,
            'wound_dmg': _compute_wound_dmg,
            'frost_slow': _apply_frost_slow,
            'poison_slow': _apply_poison_slow
        }
        return effects_types[off_stat](value)