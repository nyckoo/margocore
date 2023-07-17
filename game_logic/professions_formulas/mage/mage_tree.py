from dataclasses import dataclass
from math import floor, ceil
from typing import Iterator
from game_logic.professions_formulas.profession_abs_tree_pattern import ProfessionAbsTreePattern


@dataclass(frozen=True)
class MageTree(ProfessionAbsTreePattern):
    blueprint = {
        25: ('fire_ball', 'lightning', 'frozen_spell', 'elements_fusion', 'mana_concentration', 'physical_fitness'),
        35: ('fire_wall', 'lightning_chain', 'hoarfrost', 'wounds_healing', 'absorption_buff', 'critical_hit'),
        50: ('healthy_atmosphere', 'focus_moment', 'suffocating_spell', 'slowing_blow', 'magic_protection', 'innate_speed'),
        80: ('fire_power', 'lightning_power', 'frost_power', 'critical_power', 'healing_force', 'survival'),
        120: ('fire_resistance', 'lightning_resistance', 'frost_resistance', 'determination', 'absorbing_shield', 'armor_buff'),
        170: ('magic_barrier', 'stinky_spell', 'apogee', 'weakness', 'curse', 'power_durability'),
        230: ('inner_calmness', 'ritual_robes', 'might_source', 'extra_armor', 'great_health', 'fear')
    }

    lvl: int
    eq_stats: dict[str, int]
    abs_data: dict[str, int]

    def create_stats_and_features_generator(self) -> Iterator[tuple[str, dict, dict]]:
        for skill_name in self.abs_data.keys():
            yield getattr(self, f"_apply_skill_{skill_name}")()

    def _apply_skill_frost_spell(self):
        points = self.abs_data['frost_spell']
        passive_dmg = round(.2 * self.eq_stats['intellect'])
        slow = (15 + points * 5)
        freeze = 10 + floor(points / 2)
        mana_cost_points_set = (24, 26, 28, 30, 33, 37, 41, 47, 53, 60)
        return (
            'frost_spell',
            {
                'frost_slow': slow,
                'turns_duration': 2,
                'freeze_chance': freeze,
                'combination_point': 1,
                'mana_cost': mana_cost_points_set[points - 1]
            }, {
                'frost_dmg': passive_dmg
            }
        )

    def _apply_skill_lightning(self):
        points = self.abs_data['lightning']
        passive_dmg = round(.2 * self.eq_stats['intellect'])
        light_dmg = (150 + 15 * points) * .01
        armor_break = (13 + points) * .1
        mana = 22 + points * 8
        return (
            'lightning',
            {
                'light_dmg': light_dmg,
                'turns_duration': 3,
                'armor_break': armor_break,
                'combination_point': 1,
                'mana_cost': mana
            }, {
                'light_dmg': passive_dmg
            }
        )

    def _apply_skill_fire_ball(self):
        points = self.abs_data['fire_ball']
        passive_dmg = round(.2 * self.eq_stats['intellect'])
        burn_dmg = 8 + points * 2 if points < 7 else 14 + points
        extra_dmg = 1 + points * 6
        mana_cost_points_set = (35, 45, 55, 65, 75, 85, 100, 120, 140, 160)
        return (
            'fire_ball',
            {
                'burn_dmg': burn_dmg,
                'turns_duration': 2,
                'extra_fire_dmg': extra_dmg,
                'combination_point': 1,
                'mana_cost': mana_cost_points_set[points - 1]
            }, {
                'fire_dmg': passive_dmg
            }
        )

    def _apply_skill_elements_fusion(self, combination_points):
        # combination points reset, orb required as secondary weapon
        points = self.abs_data['elements_fusion']
        enemy_hp_percent = 2 + points * .1
        attack_bonus = enemy_hp_percent * combination_points if combination_points < 4 else enemy_hp_percent * 3
        mana_cost = 16 + points * 3
        return (
            'elements_fusion',
            {
                'attack_percent_bonus': attack_bonus,
                'turns_delay': 2,
                'mana_cost': mana_cost
            },
            {}
        )

    def _apply_skill_physical_fitness(self):
        points = self.abs_data['physical_fitness']
        hp_points = self.lvl * points * 3
        return (
            'physical_fitness',
            {},
            {
                'hp': hp_points
            }
        )

    def _apply_skill_mana_concentration(self):
        points = self.abs_data['mana_concentration']
        mana_bonus = round(-.02 * pow(points, 2) + 2.3 * points + 3.1) * self.eq_stats['intellect'] / 100
        mana = 50 + points * 5
        mana_regen = 3 + points * 2 if points < 5 else 8 + points
        return (
            'mana_concentration',
            {
                'mana_regen': mana_regen
            }, {
                'mana': mana + round(mana_bonus)
            }
        )
