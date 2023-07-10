from dataclasses import dataclass
from game_logic.structures.eq_builder import Eq


@dataclass(frozen=True)
class TrackerTree:
    blueprint = {
        25: ('frost_arrow', 'fire_arrow', 'light_arrow', 'double_arrow', 'power_concentration', 'physical_fitness'),
        35: ('double_breath', 'surprise_arrow', 'critical_hit', 'free_dodge', 'exhaustive_arrow', 'crushing_arrow'),
        50: ('innate_speed', 'absorption_buff', 'comfortable_outfit', 'arrows_hail', 'healing_coolness', 'bolt_retrieval'),
        80: ('critical_buff', 'emanating_arrow', 'survival', 'fire_power', 'light_power', 'frost_power'),
        120: ('stinky_bolt', 'armor_buff', 'power_regain', 'callousness', 'finish_attack', 'elemental_protection'),
        170: ('energizing_shock', 'power_durability', 'frost_immunity', 'rapid_arrow', 'fire_immunity', 'light_immunity'),
        230: ('mystical_arrow', 'fear', 'extra_health', 'extra_armor', 'might_source', 'item_enchantment')
    }

    translator = {
        # 25
        'frost_arrow': {
            'battle': ['frost_slow_2t', 'freeze_chance', 'combination_point', 'mana_cost'],
            'features': ['frost_dmg']
        },
        'fire_arrow': {
            'battle': ['burn_dmg_2t', 'extra_fire_dmg', 'dodge_reduction', 'combination_point', 'mana_cost'],
            'features': ['fire_dmg']
        },  # +100% mana when used immediately one after another
        'light_arrow': {
            'battle': ['light_dmg_3t', 'armor_break', 'combination_point', 'mana_cost'],
            'features': ['light_dmg']
        },
        'double_arrow': {
            'battle': ['attack_decrease', 'delay_2t'],
            'features': ['physical_dmg']
        },
        'power_concentration': {
            'battle': ['energy_regen', 'mana_regen'],
            'features': ['energy', 'mana', 'mana_bonus']
        },
        'physical_fitness': {
            'battle': None,
            'features': ['health_points']
        },
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
    eq: Eq
    abs_set: dict[str, int]

    # get loaded abs & return to features, battle stats
    def assign_to_stats_and_features(self):
        ...

    def _apply_skill_frost_arrow(self):
        ...
