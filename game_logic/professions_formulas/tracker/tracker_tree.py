from dataclasses import dataclass
from math import floor
from game_logic.professions_formulas.profession_abs_tree_pattern import ProfessionAbsTreePattern


@dataclass(frozen=True)
class TrackerTree(ProfessionAbsTreePattern):
    blueprint = {
        25: ('frost_arrow', 'fire_arrow', 'light_arrow', 'double_arrow', 'power_concentration', 'physical_fitness'),
        35: ('double_breath', 'surprise_arrow', 'critical_hit', 'free_dodge', 'exhaustive_arrow', 'crushing_arrow'),
        50: ('innate_speed', 'absorption_buff', 'comfortable_outfit', 'arrows_hail', 'healing_coolness', 'bolt_retrieval'),
        80: ('critical_buff', 'emanating_arrow', 'survival', 'fire_power', 'light_power', 'frost_power'),
        120: ('stinky_bolt', 'armor_buff', 'power_regain', 'callousness', 'finish_attack', 'elemental_protection'),
        170: ('energizing_shock', 'power_durability', 'frost_immunity', 'rapid_arrow', 'fire_immunity', 'light_immunity'),
        230: ('mystical_arrow', 'fear', 'great_health', 'extra_armor', 'might_source', 'items_enchantment')
    }

    translator = {
        # 35
        'surprise_arrow': {
            'battle': ['increased_dmg', 'dmg_reduction', 'delay_3t', 'reset_combination_point'],
            'features': ['physical_dmg']
        },
        'exhaustive_arrow': {
            'battle': ['max_hp_percentage_dmg', 'reset_combination_point', 'inevitable_dmg'],
            'features': None
        },
        'double_breath': {
            'battle': ['attack_speed_8t', 'delay_6t'],
            'features': None
        },
        'crushing_arrow': {
            'battle': ['4x_speed_shot_chance'],
            'features': ['armor_pierce_chance', 'physical_dmg']
        },
        'free_dodge': {
            'battle': ['dodge_combination_point'],
            'features': ['dodge']
        },
        'critical_hit': {
            'battle': None,
            'features': ['crit']
        },
        # 50
        'arrows_hail': {
            'battle': ['many_arrows', 'delay_2t'],
            'features': None
        },
        'healing_coolness': {
            'battle': ['hp_regen_percentage'],
            'features': None
        },
        'comfortable_outfit': {
            'battle': None,
            'features': ['eq_attack_speed_increase', 'eq_attack_speed_decrease_reduction']
        },
        'absorption_buff': {
            'battle': ['abs_regen', 'abs_increase', 'abs_destruction_reduction', 'abs_range_effect'],
            'features': None
        },
        'bolt_retrieval': {  # no effect in pvp
            'battle': None,
            'features': None
        },
        'innate_speed': {
            'battle': None,
            'features': ['attack_speed_increase']
        }
    }

    lvl: int
    eq_stats: dict[str, int]
    abs_set: dict[str, int]

    # get loaded abs & return to features, battle stats
    def assign_to_stats_and_features(self):
        for skill, points in self.abs_set.items():
            pass

    def _apply_skill_frost_arrow(self):
        points = self.abs_set['frost_arrow']
        passive_dmg = round(0.3 * self.eq_stats['intellect'])
        slow = (25 + points * 5)
        freeze = 10 + floor(points / 2)
        mana = 20 + round(.076 * pow(points, 2) + 3.07 * points - 3.4)
        return {
            'battle': {
                'frost_slow_2t': slow,
                'freeze_chance': freeze,
                'combination_point': 1,
                'mana_cost': mana
            },
            'features': {
                'frost_dmg': passive_dmg
            }
        }

    def _apply_skill_light_arrow(self):
        points = self.abs_set['light_arrow']
        passive_dmg = round(0.3 * self.eq_stats['intellect'])
        light_dmg = (9 + points) / 100
        armor_break = (13 + points) / 100
        mana = 20 + points * 10
        return {
            'battle': {
                'light_dmg_3t': light_dmg,
                'armor_break': armor_break,
                'combination_point': 1,
                'mana_cost': mana
            },
            'features': {
                'light_dmg': passive_dmg
            }
        }

    def _apply_skill_fire_arrow(self):
        points = self.abs_set['fire_arrow']
        passive_dmg = round(0.3 * self.eq_stats['intellect'])
        polynomial_approx = round(-.034 * pow(points, 3) + 0.406 * pow(points, 2) + 3.637 * points - 3.833)
        burn_dmg = 15 + polynomial_approx
        extra_dmg = 10 + polynomial_approx
        mana = 10 + points * 20
        return {
            'battle': {
                'burn_dmg_2t': burn_dmg,
                'extra_fire_dmg': extra_dmg,
                'dodge_reduction': 5,
                'combination_point': 1,
                'mana_cost': mana
            },
            'features': {
                'light_dmg': passive_dmg
            }
        }

    def _apply_skill_double_arrow(self):
        points = self.abs_set['double_arrow']
        passive_dmg = round(0.2 * self.eq_stats['agility'])
        attack_decrease = 32 - points * 2
        energy = 30 + points
        return {
            'battle': {
                'attack_decrease': attack_decrease,
                'delay_2t': 2,
                'energy_cost': energy
            },
            'features': {
                'physical_dmg': passive_dmg
            }
        }

    def _apply_skill_physical_fitness(self):
        points = self.abs_set['physical_fitness']
        hp_points = self.lvl * points * 3
        return {
            'battle': None,
            'features': {
                'physical_dmg': hp_points
            }
        }

    def _apply_skill_power_concentration(self):
        points = self.abs_set['power_concentration']
        mana_bonus = round(-.02 * pow(points, 2) + 2.3 * points + 3.1) * self.eq_stats['intellect'] / 100
        energy = points * 5
        mana = 15 + points * 10 if points < 8 else 85 + points * 5
        energy_regen = 2 + floor(points / 2)
        mana_regen = points * 2 if points < 5 else 8 + points
        return {
            'battle': {
                'energy_regen': energy_regen,
                'mana_regen': mana_regen
            },
            'features': {
                'energy': energy,
                'mana': mana,
                'mana_bonus': mana_bonus
            }
        }
