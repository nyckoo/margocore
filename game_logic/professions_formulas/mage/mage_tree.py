from dataclasses import dataclass
from math import floor, ceil
from typing import Iterator
from game_logic.professions_formulas.profession_abs_tree_pattern import ProfessionAbsTreePattern


@dataclass(frozen=True)
class MageTree(ProfessionAbsTreePattern):
    blueprint = {
        25: ('fire_ball', 'lightning', 'frozen_spell', 'elements_fusion', 'mana_concentration', 'physical_fitness'),
        35: ('fire_wall', 'lightning_chain', 'hoarfrost', 'healing_wounds', 'absorption_buff', 'critical_hit'),
        50: ('healthy_atmosphere', 'focus_moment', 'suffocating_spell', 'slowing_hit', 'magic_protection', 'innate_speed'),
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

    def _apply_skill_fire_wall(self):
        # missing battle mechanics
        points = self.abs_data['fire_wall']
        passive_dmg = round(.1 * self.eq_stats['intellect'])
        # bad round function
        mana_cost = round(self.lvl * (.65 + .07 * points))
        return (
            'fire_wall',
            {
                'mana_cost': mana_cost
            },
            {
                'fire_dmg': passive_dmg
            }
        )

    def _apply_skill_lightning_chain(self):
        # missing battle mechanics
        points = self.abs_data['lightning_chain']
        passive_dmg = round(.1 * self.eq_stats['intellect'])
        # bad round function
        mana_cost = round(self.lvl * (.75 + .07 * points))
        return (
            'lightning_chain',
            {
                'mana_cost': mana_cost
            },
            {
                'light_dmg': passive_dmg
            }
        )

    def _apply_skill_hoarfrost(self):
        points = self.abs_data['hoarfrost']
        passive_dmg = round(.1 * self.eq_stats['intellect'])
        as_decrease = 4 + points
        mana_cost = round(self.lvl * (.6 + .05 * points))
        return (
            'hoarfrost',
            {
                'as_decrease_percent': as_decrease,
                'turns_duration': 6,
                'turns_delay': 4,
                'mana_cost': mana_cost
            },
            {
                'frost_dmg': passive_dmg
            }
        )

    def _apply_skill_critical_hit(self):
        points = self.abs_data['critical_hit']
        return (
            'critical_hit',
            {},
            {
                'crit': 3.5 + points * .5
            }
        )

    def _apply_skill_healing_wounds(self):
        points = self.abs_data['healing_wounds']
        hp_percent_heal = 22 + points * 3
        mana_cost = round(self.lvl * (.6 + .05 * points))
        return (
            'healing_wounds',
            {
                'hp_healing_percent': hp_percent_heal,
                'mana_cost': mana_cost
            },
            {}
        )

    def _apply_skill_absorption_buff(self):
        points = self.abs_data['absorption_buff']
        absorption_regeneration_percent = 4 + points * .4
        absorption_buff_percentage = points * .1
        eq_as_reduction_protection_percent = points * 5
        range_physical_dmg_absorption = 4 + points
        return (
            'absorption_buff',
            {
                'attack_absorption_regeneration_percent': absorption_regeneration_percent
            },
            {
                'eq_as_reduction_protection_percent': eq_as_reduction_protection_percent,
                'physical_absorption': round(absorption_buff_percentage * self.eq_stats['physical_absorption']),
                'magical_absorption': round(absorption_buff_percentage * self.eq_stats['magical_absorption']),
                'range_physical_dmg_absorption': range_physical_dmg_absorption
            }
        )

    def _apply_skill_healthy_atmosphere(self):
        points = self.abs_data['healthy_atmosphere']
        hp_percent_heal = 10 + points * 2
        mana_cost = round(self.lvl * (.6 + .05 * points))
        return (
            'healthy_atmosphere',
            {
                'hp_healing_percent': hp_percent_heal,
                'mana_cost': mana_cost
            },
            {}
        )

    def _apply_skill_focus_moment(self):
        points = self.abs_data['focus_moment']
        mana_regain = 20 + points * 4
        return (
            'focus_moment',
            {
                'mana_regain': mana_regain,
            },
            {}
        )

    def _apply_skill_suffocating_spell(self):
        points = self.abs_data['suffocating_spell']
        attack_decrease_percent = 5 + points * .5
        mana_cost_points_set = (24, 26, 28, 30, 33, 37, 41, 47, 53, 60)
        return (
            'suffocating_spell',
            {
                'attack_decrease_percent': attack_decrease_percent,
                'turns_duration': 3,
                'mana_cost': mana_cost_points_set[points - 1],
                'combination_point': 1,
            },
            {}
        )

    def _apply_skill_slowing_hit(self):
        points = self.abs_data['slowing_hit']
        return (
            'slowing_hit',
            {},
            {
                'crit_slowness_percent': points
            }
        )

    def _apply_skill_magic_protection(self):
        points = self.abs_data['magic_protection']
        block_bonus_percent = .5 + points * .5
        return (
            'magic_protection',
            {},
            {
                'block_bonus_percent': block_bonus_percent
            }
        )

    def _apply_skill_innate_speed(self):
        points = self.abs_data['innate_speed']
        points_params_set = (20, 40, 50, 60, 65, 70, 73, 76, 78, 80)
        as_bonus = round(self.lvl * .01 * points_params_set[points - 1])
        return (
            'innate_speed',
            {},
            {
                'attack_speed': as_bonus,
            }
        )
