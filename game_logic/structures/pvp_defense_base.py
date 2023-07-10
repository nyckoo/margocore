from dataclasses import dataclass

# defence params applicable for each profession for pvp, might be loaded dynamically
# based on toa_stats & eq


@dataclass
class DefChanceable:
    glare: str
    cleanse: str
    resgain: str
    dodge: str
    block: str
    pierce_block: str
    contra: str


@dataclass
class DefApplicable:
    lastheal: str  # +-10%, activated when max_hp < 18%
    poison_resist: str
    fire_resist: str
    light_resist: str
    frost_resist: str
    armor: str
    physical_absorb: str
    magical_absorb: str

@dataclass
class DefReducable:
    dmgred: str
    critred: str
    energy_subtra: str
    mana_subtra: str
    armor_reduction_protection: str

@dataclass
class DefChangeable:
    attack_speed: str
    energy: str
    mana: str
    health_points: str
    hp_regen: str


@dataclass(frozen=True)
class Defense:
    params = frozenset({
        'glare',
        'cleanse',
        'resgain',
        'dodge',
        'block',
        'pierce_block',
        'contra',
        'lastheal',
        'poison_resist',
        'fire_resist',
        'light_resist',
        'frost_resist',
        'armor',
        'physical_absorb',
        'magical_absorb',
        'dmgred',
        'critred',
        'energy_subtra',
        'mana_subtra',
        'armor_reduction_protection',
        'energy',
        'mana',
        'health_points',
        'hp_regen',
        'attack_speed'
    })

# To be continued..


defence_params_proxy = {
    'chanceable': {
        'glare',
        'cleanse',
        'resgain',
        'dodge',
        'block',
        'pierce_block',
        'contra'
    },
    'applicable': {
        'lastheal',  # +-10%, activated when max_hp < 18%
        'poison_resist',
        'fire_resist',
        'light_resist',
        'frost_resist',
        'armor',
        'physical_absorb',
        'magical_absorb'
    },
    'reducable': {
        'dmgred',
        'critred',
        'energy_subtra',
        'mana_subtra',
        'armor_reduction_protection'
    },
    'changeable': {
        'attack_speed',
        'energy',
        'mana',
        'health_points',
        'hp_regen'
    }
}