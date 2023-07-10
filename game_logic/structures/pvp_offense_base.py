from dataclasses import dataclass
from random import random, randrange

# attack params applicable for each profession for pvp, might be loaded dynamically
# based on toa_stats & eq


@dataclass
class AttackTypes:
    physical_dmg: str
    fire_dmg: str  # originally interval
    light_dmg: str  # originally interval
    frost_dmg: str
    poison_dmg: str
    wound_dmg: str
    physical_crit: str
    magical_crit: str


@dataclass
class OffChanceable:
    crit_strike: str  # rename to 'crit'
    verycrit: str
    holytouch: str
    curse: str
    armor_pierce: str
    wound_chance: str


@dataclass
class OffReducable:
    frost_slow: str
    poison_slow: str
    as_reduction: str  # works once after first successful hit
    resist_reduction: str  # works when hit successful
    armor_reduction: str  # works when hit successful
    absorb_reduction: str  # works when hit successful
    hp_regen_reduction: str
    hp_regen_reduction_2t: str
    mana_energy_subtra_protection: str


@dataclass
class OffChangeable:
    attack_speed: int


@dataclass(frozen=True)
class Offense:
    params = frozenset({
        'crit_strike',
        'verycrit',
        'holytouch',
        'curse',
        'armor_pierce',
        'wound_chance',
        'physical_dmg',
        'fire_dmg',
        'light_dmg',
        'frost_dmg',
        'poison_dmg',
        'wound_dmg',
        'physical_crit',
        'magical_crit'
        'frost_slow',
        'poison_slow',
        'as_reduction',
        'resist_reduction',
        'armor_reduction',
        'absorb_reduction',
        'hp_regen_reduction',
        'hp_regen_reduction_2t',
        'mana_energy_subtra_protection',
        'attack_speed'
    })


def _apply_chances(**chanceable_stats):
    return {stat: True if random() < value else False for stat, value in chanceable_stats.items()}


def _apply_dmgs(**attack_stats):
    return {stat: _evaluate_effect(value) for stat, value in attack_stats.items()}


def _apply_reductions(**reducable_stats):
    return {stat: value for stat, value in reducable_stats.items()}


def _evaluate_hit(updatibles):
    dmg_stats = _apply_dmgs(**updatibles['attack_types'])
    drawn_chances = _apply_chances(**updatibles['chanceable'])
    to_be_reduced = _apply_reductions(**updatibles['reducable'])
    hit_stats_summary = {}
    # draw statistics with percentage chance
    for stat, val in drawn_chances.items():
        hit_stats_summary[stat] = val
    # apply standard damage stats
    for stat, val in dmg_stats.items():
        hit_stats_summary[stat] = val
    # apply enhanced hit stats
    if hit_stats_summary.get('crit_strike'):
        for magic_crit_dmg_stat in ('fire_dmg', 'light_dmg', 'frost_dmg'):
            if hit_stats_summary.get(magic_crit_dmg_stat):
                hit_stats_summary[magic_crit_dmg_stat] *= dmg_stats.get('magical_crit', 1)
        if hit_stats_summary.get('physical_dmg'):
            hit_stats_summary['physical_dmg'] *= dmg_stats.get('physical_crit', 1)
    # pass wound_chance to wound_dmg dependency
    if not hit_stats_summary.get('wound_chance'):
        del hit_stats_summary['wound_dmg']
    # apply reducable stats
    for stat, val in to_be_reduced.items():
        hit_stats_summary[stat] = val
    return hit_stats_summary


# Single operation functions evaluator
def _evaluate_effect(off_stat, value):

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

    def _compute_crit_dmg(crit_power):
        return

    def _apply_frost_slow(frost_slow):
        return

    def _apply_poison_slow(poison_slow):
        return

    def _apply_as_reduction():  # should work once
        return

    effects_types = {
        'physical_dmg': _compute_physical_dmg,
        'fire_dmg': _compute_fire_dmg,
        'light_dmg': _compute_light_dmg,
        'frost_dmg': _compute_frost_dmg,
        'poison_dmg': _compute_poison_dmg,
        'wound_dmg': _compute_wound_dmg,
        'crit_strike': _compute_crit_dmg,
        'frost_slow': _apply_frost_slow,
        'poison_slow': _apply_poison_slow,
        'as_reduction': _apply_as_reduction
    }
    return effects_types[off_stat](value)


attack_params_proxy = {
    'chanceable': {
        'crit_strike',  # rename to 'crit'
        'verycrit',
        'holytouch',
        'curse',
        'armor_pierce',
        'wound_chance'
    },
    'attack_types': {
        'physical_dmg',
        'fire_dmg',  # originally boundaries
        'light_dmg',  # originally boundaries
        'frost_dmg',
        'poison_dmg',
        'wound_dmg',
        'physical_crit',
        'magical_crit'
    },
    'reducable': {
        'frost_slow',
        'poison_slow',
        'as_reduction',  # works once after first successful hit
        'resist_reduction',  # works when hit successful
        'armor_reduction',  # works when hit successful
        'absorb_reduction',  # works when hit successful
        'hp_regen_reduction',
        'hp_regen_reduction_2t',
        'mana_energy_subtra_protection'
    },
    'changeable': {
        'attack_speed'
    }
}