from dataclasses import dataclass, fields

from game_logic.structures.stats_utils import AllStats
from scrape_module.utils import ScrapeItemStatsMapper


# Item loaded from db on runtime
@dataclass
class Item:
    lvl: int
    prof: str
    acc_id: int
    name: str
    stats: dict

    def __post_init__(self):
        self.stats = self.parse_raw_types()

    # These stats are handled as if they were scraped
    def parse_raw_types(self):
        scrape_stats_mapper = {field.name: field.default for field in fields(ScrapeItemStatsMapper)}
        all_stats = {field.name: field.type for field in fields(AllStats)}
        parsed_stats = {}
        for key, val in self.stats.items():
            if new_name_key := scrape_stats_mapper.get(key, False):
                if all_stats[new_name_key] is int:
                    parsed_stats[new_name_key] = int(val)
                elif all_stats[new_name_key] is tuple:
                    args = val.split(',')
                    match new_name_key:
                        case 'physical_dmg':
                            parsed_stats[new_name_key] = (int(args[0]) + int(args[1])) / 2
                        case 'wound_dmg':
                            parsed_stats[new_name_key[:-3] + 'chance'] = int(args[0])
                        case _:
                            parsed_stats[new_name_key[:-3] + 'slow'] = int(args[0])
                else:  # all_stats[new_name_key] is str
                    if new_name_key == 'legendary_bonus':
                        parsed_stats[new_name_key] = val.split(',')[0]
        return parsed_stats
