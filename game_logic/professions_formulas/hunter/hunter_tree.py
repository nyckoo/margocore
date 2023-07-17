from dataclasses import dataclass
from math import floor, ceil
from typing import Iterator
from game_logic.professions_formulas.profession_abs_tree_pattern import ProfessionAbsTreePattern


@dataclass(frozen=True)
class HunterTree(ProfessionAbsTreePattern):
    blueprint = {
        25: ('swift_arrow', 'double_arrow', 'poisoned_arrow', 'ripping_arrow', 'vigor_enhancement', 'physical_fitness'),
        35: ('devastating_wounds', 'beast_seal', 'break_freeing', 'armor_pierce', 'natural_dodge', 'critical_hit'),
        50: ('arrows_hail', 'bandaging_wounds', 'toxic_shock', 'as_agility', 'arrow_retrieval', 'inborn_speed'),
        80: ('critical_buff', 'diamond_arrow', 'cleanse', 'critical_arrow', 'painful_hit', 'survival'),
        120: ('light_tension', 'dispersion_arrow', 'venom_arrow', 'poisonous_injury', 'core_resistance', 'firm_armor'),
        170: ('foot_shot', 'insidious_arrow', 'remedy', 'wolf_instinct', 'easy_target', 'power_durability'),
        230: ('wild_zeal', 'destructive_arrows', 'might_source', 'armouring', 'great_health', 'fear')
    }

    lvl: int
    eq_stats: dict[str, int]
    abs_data: dict[str, int]

    def create_stats_and_features_generator(self) -> Iterator[tuple[str, dict, dict]]:
        for skill_name in self.abs_data.keys():
            yield getattr(self, f"_apply_skill_{skill_name}")()

    def _apply_skill_swift_arrow(self, combination_points):
        # combination point for armor pierce passive
        # combination points reset
        points = self.abs_data['swift_arrow']
        faster_turn_percent_rate = 6 + 2 * points
        return (
            'swift_arrow',
            {
                'faster_turn_percent_rate': faster_turn_percent_rate,
                'energy_regeneration_percent': 5 * combination_points if combination_points < 4 else 15,
                'turns_delay': 5
            },
            {}
        )

    def _apply_skill_double_arrow(self):
        points = self.abs_data['double_arrow']
        passive_dmg = round(.2 * self.eq_stats['agility'])
        attack_decrease = 26 - points if points < 7 else 32 - points * 2
        energy_cost = 24 + 2 * points if points < 7 else 30 + points
        return (
            'double_arrow',
            {
                'attack_decrease': attack_decrease,
                'turns_delay': 3,
                'energy_cost': energy_cost,
                'combination_point': 1
            }, {
                'physical_dmg': passive_dmg
            }
        )

    def _apply_skill_poisoned_arrow(self):
        points = self.abs_data['poisoned_arrow']
        poison_bonus = round((115 + points * 5) * .01 * self.eq_stats['poison_dmg'])
        energy_cost = 22 + points * 3 if points < 6 else 32 + points
        return (
            'poisoned_arrow',
            {
                'poison_dmg': poison_bonus,
                'turns_duration': 5,
                'dmg_reduction': 10,
                'energy_cost': energy_cost,
                'combination_point': 1
            },
            {}
        )

    def _apply_skill_ripping_arrow(self):
        # combination point for every wound chance applied
        points = self.abs_data['ripping_arrow']
        wound_dmg_bonus = round((42 + points * 4) * .01 * self.eq_stats['wound_dmg'])
        return (
            'ripping_arrow',
            {},
            {
                'wound_dmg': wound_dmg_bonus,
                'wound_chance': points if points < 6 else 2 + ceil(points / 2)
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

    def _apply_skill_vigor_enhancement(self):
        points = self.abs_data['vigor_enhancement']
        energy = 20 + points * 4
        energy_regen = 2 + floor(points / 2)
        return (
            'vigor_enhancement',
            {
                'energy_regen': energy_regen
            }, {
                'energy': energy
            }
        )

    def _apply_skill_armor_pierce(self):
        points = self.abs_data['armor_pierce']
        passive_dmg = round(.1 * self.eq_stats['agility'])
        faster_turn_chance = 2 + points * .5
        return (
            'armor_pierce',
            {
                '4x_faster_turn_chance': faster_turn_chance,
            },
            {
                'armor_pierce': points,
                'physical_dmg': passive_dmg
            }
        )

    def _apply_skill_devastating_wounds(self, combination_points):
        # combination points reset
        points = self.abs_data['devastating_wounds']
        enemy_hp_percent = 2 + points * .1
        attack_bonus = enemy_hp_percent * combination_points if combination_points < 4 else enemy_hp_percent * 3
        energy_cost = 7 + points * 3 if points < 5 else 19 + points * 2
        return (
            'devastating_wounds',
            {
                'attack_percent_bonus': attack_bonus,
                'turns_delay': 5,
                'energy_cost': energy_cost
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

    def _apply_skill_natural_dodge(self):
        points = self.abs_data['natural_dodge']
        dodge_percent = 5 + points
        return (
            'natural_dodge',
            {},
            {
                'dodge_percent': dodge_percent
            }
        )

    def _apply_skill_break_freeing(self, combination_points):
        # combination points reset
        points = self.abs_data['break_freeing']
        eq_as_reduction_protection_percent = 15 + points * 15 if points < 3 else 35 + points * 5
        stun_duration_reduction_percent = 10 + 3 * points
        return (
            'break_freeing',
            {},
            {
                'eq_as_reduction_protection_percent': eq_as_reduction_protection_percent,
                'stun_duration_reduction_percent': stun_duration_reduction_percent
            }
        )

    def _apply_skill_beast_seal(self):
        points = self.abs_data['beast_seal']
        increased_dmg_aura = 15 + points
        energy_cost = 38 + points * 2
        return (
            'beast_seal',
            {
                'increased_dmg_aura_percent': increased_dmg_aura,
                'turns_duration': 4,
                'turns_delay': 4,
                'energy_cost': energy_cost
            },
            {}
        )

    def _apply_skill_arrows_hail(self):
        points = self.abs_data['arrows_hail']
        other_attack_sum = sum((self.eq_stats[x] for x in ('poison_dmg', 'wound_dmg')))
        active_dmg = round(.6 * self.eq_stats['physical_dmg'] + .3 * other_attack_sum)
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

    def _apply_skill_bandaging_wounds(self):
        points = self.abs_data['bandaging_wounds']
        hp_percent_heal = 20 + points
        energy_cost = 38 + points * 2
        return (
            'bandaging_wounds',
            {
                'hp_healing': hp_percent_heal,
                'energy_cost': energy_cost
            },
            {}
        )

    def _apply_skill_as_agility(self):
        points = self.abs_data['as_agility']
        percent_factor = 1 + points * 2 if points < 5 else 5 + points
        as_bonus = floor(self.eq_stats['attack_speed'] * percent_factor / 100)
        return (
            'as_agility',
            {},
            {
                'eq_attack_speed_bonus': as_bonus,
            }
        )

    def _apply_skill_toxic_shock(self):
        points = self.abs_data['toxic_shock']
        return (
            'toxic_shock',
            {
                'poisoned_enemy_dmg_reduction_percent': points
            },
            {}
        )

    def _apply_skill_arrow_retrieval(self):
        return (
            'arrow_retrieval',
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
