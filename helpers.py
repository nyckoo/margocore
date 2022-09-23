# Dictionary of possible statistics derived from margonem items, translated into new names

stats = {
    'da': 'all_features',
    'ds': 'strength',
    'dz': 'agility',
    'di': 'intellect',
    'crit': 'crit',
    'critval': 'physical_crit',
    'critmval': 'magical_crit',
    'energybon': 'energy',
    'manabon': 'mana',
    'endest': 'energy_subtra',
    'manadest': 'mana_subtra',
    'resdmg': 'resist_reduction',
    'acdmg': 'armor_reduction',
    'abdest': 'absorb_reduction',
    'hp': 'health_points',
    'heal': 'hp_regen',
    'sa': 'attack_speed',
    'slow': 'as_reduction',
    'evade': 'dodge',
    'lowevade': 'dodge_reduction',
    'lowcrit': 'crit_reduction',
    'dmg': 'physical_dmg',
    'fire': 'fire_dmg',
    'light': 'light_dmg',
    'frost': 'frost_dmg',
    'frost_slow': 'frost_slow',
    'act': 'poison_resist',
    'resfire': 'fire_resist',
    'reslight': 'light_resist',
    'resfrost': 'frost_resist',
    'pierce': 'armor_pierce',
    'lowcritallval': 'crit_power_reduction',
    'lowheal2turns': 'hp_regen_reduction_2t',
    'resacdmg': 'armor_reduction_protection',
    'resmanaendest': 'mana_energy_subtra_protection',
    'ac': 'armor',
    'absorb': 'physical_absorb',
    'absorbm': 'magical_absorb',
    'blok': 'block',
    'hpbon': 'strength_hp',
    'adest': 'hp_regen_reduction',
    'contra': 'contra',
    'pierceb': 'pierce_block',
    'poison': 'poison_dmg',
    'poison_slow': 'poison_slow',
    'wound': 'wound_dmg',
    'legbon': 'legendary_bonus'
}

# Items' types for all 6 game professions (classes):

weapon_types = {
    'blade_dancer': ['1h', 'sb', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl'],
    'warrior': ['1h', '2h', 'hh', 'sh', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl'],
    'paladin': ['1h', 'hh', 'sh', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl'],
    'mage': ['wa', 'mo', 'sh', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl'],
    'tracker': ['rw', 'am', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl'],
    'hunter': ['rw', 'am', 'ar', 'he', 'bo', 'gl', 'ri', 'ne', 'bl']
}

# Id's of accessory types at margohelp url for each proffesion:

prof_translator = {
    'blade_dancer': (1, 5, 8, 9, 10, 11, 12, 13),
    'warrior': (1, 2, 3, 14, 8, 9, 10, 11, 12, 13),
    'paladin': (1, 3, 14, 8, 9, 10, 11, 12, 13),
    'mage': (6, 7, 14, 8, 9, 10, 11, 12, 13),
    'tracker': (4, 21, 8, 9, 10, 11, 12, 13),
    'hunter': (4, 21, 8, 9, 10, 11, 12, 13)
}

# Page url items' types translator:

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
