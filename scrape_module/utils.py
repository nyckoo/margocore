from dataclasses import dataclass


# Dictionary of possible statistics translated into new names
@dataclass(frozen=True)
class ScrapeItemStatsMapper:
    da: str = 'all_features'
    ds: str = 'strength'
    dz: str = 'agility'
    di: str = 'intellect'
    crit: str = 'crit'
    critval: str = 'physical_crit'
    critmval: str = 'magical_crit'
    energybon: str = 'energy'
    manabon: str = 'mana'
    endest: str = 'energy_subtra'
    manadest: str = 'mana_subtra'
    resdmg: str = 'resist_reduction'
    acdmg: str = 'armor_reduction'
    abdest: str = 'absorb_reduction'
    hp: str = 'health_points'
    heal: str = 'hp_regen'
    sa: str = 'attack_speed'
    slow: str = 'as_reduction'
    evade: str = 'dodge'
    lowevade: str = 'dodge_reduction'
    lowcrit: str = 'crit_reduction'
    dmg: str = 'physical_dmg'
    pdmg: str = 'physical_dmg'  # arrows
    fire: str = 'fire_dmg'
    light: str = 'light_dmg'
    frost: str = 'frost_dmg'
    frost_slow: str = 'frost_slow'
    act: str = 'poison_resist'
    resfire: str = 'fire_resist'
    reslight: str = 'light_resist'
    resfrost: str = 'frost_resist'
    pierce: str = 'armor_pierce'
    lowcritallval: str = 'crit_power_reduction'
    lowheal2turns: str = 'hp_regen_reduction_2t'
    resacdmg: str = 'armor_reduction_protection'
    resmanaendest: str = 'mana_energy_subtra_protection'
    ac: str = 'armor'
    absorb: str = 'physical_absorb'
    absorbm: str = 'magical_absorb'
    blok: str = 'block'
    hpbon: str = 'strength_hp'
    adest: str = 'hp_regen_reduction'
    contra: str = 'contra'
    pierceb: str = 'pierce_block'
    poison: str = 'poison_dmg'
    poison_slow: str = 'poison_slow'
    wound: str = 'wound_dmg'
    legbon: str = 'legendary_bonus'
    bonus: str = 'enchant_bonus'
    enhancement_upgrade_lvl: str = 'upgrade_lvl'
    low_req: str = 'low_req'


# Items' types for all 6 game professions (classes):

weapon_types = {
    'blade_dancer': ['1h', 'sb', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl'],
    'warrior': ['1h', '2h', 'hh', 'sh', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl'],
    'paladin': ['1h', 'hh', 'sh', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl'],
    'mage': ['wa', 'mo', 'sh', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl'],
    'tracker': ['rw', 'am', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl'],
    'hunter': ['rw', 'am', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl']
}

# Ids of accessory types at margohelp.pl for each profession:

prof_translator = {
    'blade_dancer': (1, 5, 8, 9, 10, 11, 12, 13),
    'warrior': (1, 2, 3, 14, 8, 9, 10, 11, 12, 13),
    'paladin': (1, 3, 14, 8, 9, 10, 11, 12, 13),
    'mage': (6, 7, 14, 8, 9, 10, 11, 12, 13),
    'tracker': (4, 21, 8, 9, 10, 11, 12, 13),
    'hunter': (4, 21, 8, 9, 10, 11, 12, 13)
}

# Page url items-margohelp-2022.06' types translator:

item_translator = {
    1: 'Jednoręczne',  # One-handed
    2: 'Dwuręczne',  # Two-handed
    3: 'Półtoraręczne',  # Hand&half
    4: 'Dystansowe',  # Ranged
    5: 'Pomocnicza',  # Secondary
    6: 'Różdżki',  # Rods
    7: 'Orbymagiczne',  # Magical orbs
    8: 'Zbroje',  # Armor
    9: 'Hełmy',  # Headgear
    10: 'Buty',  # Boots
    11: 'Rękawice',  # Gloves
    12: 'Pierścienie',  # Rings
    13: 'Naszyjniki',  # Necklaces
    14: 'Tarcze',  # Shields
    21: 'Strzały'  # Arrows
}

proffesions = {
    'w': 'Wojownik',  # Warrior
    'b': 'Tancerzostrzy',  # Blade dancer
    'p': 'Paladyn',  # Paladin
    'm': 'Mag',  # Mage
    't': 'Tropiciel',  # Tracker
    'h': 'Łowca'  # Hunter
}
