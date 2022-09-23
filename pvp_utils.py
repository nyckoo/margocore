from types import MappingProxyType
# All battle stats
# Offensive, Deffensive / Static, Dynamic

leg_bons = MappingProxyType(
    {
        'verycrit': 13,
        'critred': 20,
        'lastheal': 40,  # +-10%, activated when max_hp < 18%
        'holytouch': 7,  # 0.06 max_hp x3
        'curse': 9,
        'glare': 9,
        'cleanse': 12,
        'dmgred': 16,
        'resgain': 16
    }
)

static_off_attrs = MappingProxyType(
    {
        'all_features': 'int',
        'strength': 'int',
        'agility': 'int',
        'intellect': 'int',
        'crit_strike': 'int',  # rename to 'crit'
        'physical_crit': 'int',
        'magical_crit': 'int',
        'dodge_reduction': 'int',  # works before hit
        # works after first successful hit forever (to 0 hp_regen)
        'hp_regen_reduction': 'int',
    }
)

dynamic_off_attrs = MappingProxyType(
    {
        'as_reduction': 'int',  # works once after first successful hit
        'resist_reduction': 'int',  # works when hit successful
        'armor_reduction': 'int',  # works when hit successful
        'absorb_reduction': 'int',  # works when hit successful
        'attack_speed': 'int',
        'physical_dmg': 'boundaries',
        'fire_dmg': 'int',  # originally boundaries
        'light_dmg': 'int',  # originally boundaries
        'frost_dmg': 'args',  # (slow, dmg)
        'armor_pierce': 'int',
        'pierce_block': 'int',
        'poison_dmg': 'args',  # (slow, dmg)
        'wound_dmg': 'args',  # (chance, dmg)
        'hp_regen_reduction_2t': 'int'  # works after first successful hit for 2 turns
    }
)

static_def_attrs = MappingProxyType(
    {
        'energy_subtra': 'int',
        'mana_subtra': 'int',
        'dodge': 'int',
        'crit_reduction': 'int',  # works before hit
        'crit_power_reduction': 'int',  # works before hit
        'armor_reduction_protection': 'int',  # works when hit successful
        'mana_energy_subtra_protection': 'int',
        'block': 'int',
        'strength_hp': 'int',  # added in eq upload (at func. get_all_params)
        'contra': 'int'
    }
)

dynamic_def_attrs = MappingProxyType(
    {
        'energy': 'int',
        'mana': 'int',
        'health_points': 'int',
        'hp_regen': 'int',
        'poison_resist': 'int',
        'fire_resist': 'int',
        'light_resist': 'int',
        'frost_resist': 'int',
        'armor': 'int',
        'physical_absorb': 'int',
        'magical_absorb': 'int'
    }
)

# Available types after loading from db

all_types_stats = MappingProxyType(
    {
        **static_off_attrs,
        **dynamic_off_attrs,
        **static_def_attrs,
        **dynamic_def_attrs,
        'frost_slow': 'int',
        'poison_slow': 'int',
        'wound_chance': 'int',
        'verycrit': 'bon',
        'holytouch': 'bon',
        'curse': 'bon',
        'critred': 'bon',
        'lastheal': 'bon',
        'glare': 'bon',
        'cleanse': 'bon',
        'dmgred': 'bon',
        'resgain': 'bon',
        'legendary_bonus': 'str'
    }
)

# Character counter stats decreasing enemy stats
# Might be updated by AT_stats

counter_stats = MappingProxyType(
    {
        'dodge_reduction': 'int',  # works before hit
        'hp_regen_reduction': 'int',
        'as_reduction': 'int',  # works once after first successful hit
        'resist_reduction': 'int',  # works when hit successful
        'armor_reduction': 'int',  # works when hit successful
        'absorb_reduction': 'int',  # works when hit successful
        'hp_regen_reduction_2t': 'int',  # works after first successful hit for 2 turns
        'energy_subtra': 'int',
        'mana_subtra': 'int',
        'crit_reduction': 'int',  # works before hit
        'crit_power_reduction': 'int'  # works before hit
    }
)


def parse_custom_type(raw_stats: dict):
    parsed_stats = {}
    for key, val in raw_stats.items():
        if all_types_stats[key] == 'int':
            parsed_stats[key] = int(val)
        elif all_types_stats[key] == 'boundaries':
            dmg_range = val.split('-')
            parsed_stats[key] = (int(dmg_range[0]) + int(dmg_range[1])) / 2
        elif all_types_stats[key] == 'args':
            args = val.split(',')
            parsed_stats[key] = int(args[1])
            if key == 'wound_dmg':
                parsed_stats[key[:-3]+'chance'] = int(args[0])
            else:
                parsed_stats[key[:-3]+'slow'] = int(args[0])
        else:  # str, legendary bonus
            parsed_stats[key] = val.split(',')[0]
    return parsed_stats
