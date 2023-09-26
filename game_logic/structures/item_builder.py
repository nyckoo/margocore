from dataclasses import dataclass, fields

from game_logic.structures.stats_utils import AllStats
from scrape_module.utils import ScrapeItemStatsMapper


@dataclass
class Item:
    lvl: int
    prof: str
    acc_id: int
    name: str
    stats: dict

    def __post_init__(self):
        self.stats = self.parse_raw_types()

    def parse_raw_types(self):
        parsed_stats = {}

        def __from_int(new_name_key, raw_stat):
            parsed_stats[new_name_key] = int(raw_stat)

        def __from_tuple(new_name_key, raw_stat):
            args = raw_stat.split(',')
            match new_name_key:
                case 'physical_dmg':
                    parsed_stats[new_name_key] = int((int(args[0]) + int(args[1])) / 2)
                case 'physical_dmg_single':
                    parsed_stats['physical_dmg'] = int(args[0])
                case 'light_dmg':
                    parsed_stats[new_name_key] = int((int(args[0]) + int(args[1])) / 2)
                case 'wound_dmg':
                    parsed_stats[new_name_key[:-3] + 'chance'] = int(args[0])
                    parsed_stats[new_name_key] = int(args[1])
                case _:
                    parsed_stats[new_name_key[:-3] + 'slow'] = int(args[0])
                    parsed_stats[new_name_key] = int(args[1])

        def __from_str(new_name_key, raw_stat):
            if new_name_key == 'legendary_bonus':
                parsed_stats[new_name_key] = raw_stat.split(',')[0]

        scrape_stats_mapper = {field.name: field.default for field in fields(ScrapeItemStatsMapper)}
        all_stats = {field.name: field.type for field in fields(AllStats)}

        def parse_by_type(raw_stat_name, raw_stat_value):
            if new_stat_name := scrape_stats_mapper.get(raw_stat_name, False):
                type_converter = {
                    int: __from_int,
                    tuple: __from_tuple,
                    str: __from_str
                }
                return type_converter[all_stats[new_stat_name]](new_stat_name, raw_stat_value)

        for key, val in self.stats.items():
            parse_by_type(key, val)

        return parsed_stats
