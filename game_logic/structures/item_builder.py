from dataclasses import dataclass
from stats_utils import AllStats


# Item loaded from db on runtime
@dataclass
class Item:
    lvl: int
    prof: str
    acc_type: str
    name: str
    stats: dict

    def __post_init__(self):
        self.stats = self.parse_raw_types()

    # These stats are handled as if they were scraped
    def parse_raw_types(self):
        parsed_stats = {}
        for key, val in self.stats.items():
            if AllStats.main[key] is int:
                parsed_stats[key] = int(val)
            elif AllStats.main[key] is tuple:
                args = val.split(',')
                match key:
                    case 'physical_dmg':
                        parsed_stats[key] = (int(args[0]) + int(args[1])) / 2
                    case 'wound_dmg':
                        parsed_stats[key[:-3] + 'chance'] = int(args[0])
                    case _:
                        parsed_stats[key[:-3] + 'slow'] = int(args[0])
            else:  # str, legendary bonus
                parsed_stats[key] = val.split(',')[0]
        return parsed_stats
