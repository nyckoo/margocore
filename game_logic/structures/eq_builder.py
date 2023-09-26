from dataclasses import dataclass, field

from game_logic.structures.item_builder import Item


@dataclass
class Eq:
    items: list[Item] = field(default_factory=lambda: [])
    stats: dict[str, int] = field(default_factory=lambda: {})
    legendary_bonuses_count: dict[str, int] = field(default_factory=lambda: {})
    item_to_bonus: dict[str, str] = field(default_factory=lambda: {})
    cl_items_configurations: list = field(default_factory=lambda: [])

    def check(self, item: Item, profession: str):
        # Check compatibility of profs with 1st item in eq
        zipped = set(zip(self.items[0].prof, item.prof))
        for el in zipped:
            return el[0] == el[1]

    def add(self, item: Item):
        # Append new item to eq
        self.items.append(item)
        # Add legendary bonus
        if new_bonus := item.stats.get('legendary_bonus', False):
            self.item_to_bonus[item.name] = new_bonus
            bonus_count = self.legendary_bonuses_count.get(new_bonus, 0) + 1
            self.legendary_bonuses_count[new_bonus] = bonus_count
            del item.stats['legendary_bonus']
        # Add rest of stats
        for stat, value in item.stats.items():
            if self.stats.get(stat, False):
                self.stats[stat] += value
            else:
                self.stats[stat] = value
