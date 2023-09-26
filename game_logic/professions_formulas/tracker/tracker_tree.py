from math import floor, ceil
from typing import Iterator
from game_logic.professions_formulas.profession_abs_tree_pattern import ProfessionAbsTreePattern


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

    def __init__(self, lvl: int, eq_stats: dict[str, int], abs_data: dict[str, int]):
        super().__init__(lvl, eq_stats, abs_data)

    def create_stats_and_features_generator(self) -> Iterator[tuple[str, dict, dict]]:
        for skill_name in self.abs_data.keys():
            yield getattr(self, f"_apply_skill_{skill_name}")()

    def _apply_skill_frost_arrow(self):
        points = self.abs_data['frost_arrow']
        passive_dmg = round(.3 * self.eq_stats['intellect'])
        slow = (25 + points * 5)
        freeze = 10 + floor(points / 2)
        mana = 20 + round(.076 * pow(points, 2) + 3.07 * points - 3.4)
        return (
            'frost_arrow',
            {
                'frost_slow': slow,
                'turns_duration': 2,
                'freeze_chance': freeze,
                'combination_point': 1,
                'mana_cost': mana
            }, {
                'frost_dmg': passive_dmg
            }
        )

    def _apply_skill_light_arrow(self):
        points = self.abs_data['light_arrow']
        passive_dmg = round(.3 * self.eq_stats['intellect'])
        light_dmg = (9 + points) * .1
        armor_break = (13 + points) * .1
        mana = 20 + points * 10
        return (
            'light_arrow',
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

    def _apply_skill_fire_arrow(self):
        points = self.abs_data['fire_arrow']
        passive_dmg = round(.3 * self.eq_stats['intellect'])
        polynomial_approx = round(-.034 * pow(points, 3) + 0.406 * pow(points, 2) + 3.637 * points - 3.833)
        burn_dmg = 15 + polynomial_approx
        extra_dmg = 10 + polynomial_approx
        mana = 10 + points * 20
        return (
            'fire_arrow',
            {
                'burn_dmg': burn_dmg,
                'turns_duration': 2,
                'extra_fire_dmg': extra_dmg,
                'dodge_reduction_percent': 5,
                'combination_point': 1,
                'mana_cost': mana
            }, {
                'fire_dmg': passive_dmg
            }
        )

    def _apply_skill_double_arrow(self):
        points = self.abs_data['double_arrow']
        passive_dmg = round(.2 * self.eq_stats['agility'])
        attack_decrease = 32 - points * 2
        energy = 30 + points
        return (
            'double_arrow',
            {
                'attack_decrease': attack_decrease,
                'turns_delay': 2,
                'energy_cost': energy
            }, {
                'physical_dmg': passive_dmg
            }
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

    def _apply_skill_power_concentration(self):
        points = self.abs_data['power_concentration']
        mana_bonus = round(-.02 * pow(points, 2) + 2.3 * points + 3.1) * self.eq_stats['intellect'] / 100
        energy = points * 5
        mana = 15 + points * 10 if points < 8 else 85 + points * 5
        energy_regen = 2 + floor(points / 2)
        mana_regen = points * 2 if points < 5 else 8 + points
        return (
            'power_concentration',
            {
                'energy_regen': energy_regen,
                'mana_regen': mana_regen
            }, {
                'energy': energy,
                'mana': mana + round(mana_bonus)
            }
        )

    def _apply_skill_double_breath(self):
        points = self.abs_data['double_breath']
        as_aura = 4 + points
        mana_cost = 20 + points * 10
        return (
            'double_breath',
            {
                'as_aura_percent': as_aura,
                'turns_duration': 8,
                'turns_delay': 6,
                'mana_cost': mana_cost
            },
            {}
        )

    def _apply_skill_surprise_arrow(self, combination_points):
        # combination points reset
        points = self.abs_data['surprise_arrow']
        attack_bonus = 10 + points
        mana_cost = 7 + points * 3
        return (
            'surprise_arrow',
            {
                'attack_bonus': attack_bonus,
                'turns_delay': 3,
                'dmg_reduction': 15 * combination_points if combination_points < 4 else 45,
                'mana_cost': mana_cost
            },
            {}
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

    def _apply_skill_free_dodge(self):
        # combination point for every dodge passive
        points = self.abs_data['free_dodge']
        dodge_percent = 5 + points
        return (
            'free_dodge',
            {},
            {
                'dodge_percent': dodge_percent
            }
        )

    def _apply_skill_exhaustive_arrow(self, combination_points):
        # combination points reset
        points = self.abs_data['exhaustive_arrow']
        enemy_hp_percent = 2 + points * .1
        attack_bonus = enemy_hp_percent * combination_points if combination_points < 4 else enemy_hp_percent * 3
        energy_cost = 20 + points * 2
        return (
            'exhaustive_arrow',
            {
                'attack_percent_bonus': attack_bonus,
                'turns_delay': 3,
                'energy_cost': energy_cost
            },
            {}
        )

    def _apply_skill_crushing_arrow(self):
        points = self.abs_data['crushing_arrow']
        passive_dmg = round(.1 * self.eq_stats['agility'])
        faster_turn_chance = 5 + points * .5
        return (
            'crushing_arrow',
            {
                '4x_faster_turn_chance': faster_turn_chance,
            },
            {
                'armor_pierce': points,
                'physical_dmg': passive_dmg
            }
        )

    def _apply_skill_arrows_hail(self):
        points = self.abs_data['arrows_hail']
        magic_attack_sum = sum((self.eq_stats[x] for x in ('fire_dmg', 'frost_dmg', 'light_dmg')))
        active_dmg = round(.6 * self.eq_stats['physical_dmg'] + .3 * magic_attack_sum)
        energy_cost = 47 + points * 3
        return (
            'arrows_hail',
            {
                'attack_value': active_dmg,
                'turns_delay': 2,
                'energy_cost': energy_cost
            },
            {}
        )

    def _apply_skill_healing_coolness(self):
        points = self.abs_data['healing_coolness']
        hp_percent_heal = 20 + points * 3
        mana_cost = 95 + points * 5
        return (
            'healing_coolness',
            {
                'hp_healing_percent': hp_percent_heal,
                'mana_cost': mana_cost
            },
            {}
        )

    def _apply_skill_comfortable_outfit(self):
        points = self.abs_data['comfortable_outfit']
        as_bonus = floor(self.eq_stats['attack_speed'] * points / 100)
        eq_as_reduction_protection_percent = 5 + points * 2
        return (
            'comfortable_outfit',
            {},
            {
                'eq_attack_speed_bonus': as_bonus,
                'eq_as_reduction_protection_percent': eq_as_reduction_protection_percent
            }
        )

    def _apply_skill_absorption_buff(self):
        points = self.abs_data['absorption_buff']
        absorption_regeneration_percent = ceil(points / 3)
        absorption_buff_percentage = points * .1
        range_physical_dmg_absorption = 4 + points
        return (
            'absorption_buff',
            {
                'attack_absorption_regeneration_percent': absorption_regeneration_percent
            },
            {
                'physical_absorption': round(absorption_buff_percentage * self.eq_stats['physical_absorption']),
                'magical_absorption': round(absorption_buff_percentage * self.eq_stats['magical_absorption']),
                'range_physical_dmg_absorption': range_physical_dmg_absorption
            }
        )

    def _apply_skill_bolt_retrieval(self):
        return (
            'bolt_retrieval',
            {},
            {}
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
