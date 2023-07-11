from dataclasses import dataclass, field
from item_builder import Item


@dataclass
class Eq:
    items: list[Item] = field(default_factory=lambda: [])
    stats: dict[str, int] = field(default_factory=lambda: {})
    bonuses: dict[str, int] = field(default_factory=lambda: {})
    item_to_bonus: dict[Item.name, str] = field(default_factory=lambda: {})

    def check(self, item: Item, profession: str):
        # Check compatibility of profs with 1st item in eq
        zipped = set(zip(self.items[0].prof, item.prof))
        for el in zipped:
            return el[0] == el[1]

    def add(self, item: Item):
        # Append new item to eq
        self.items.append(item)
        # Add legendary bonus
        if new_bonus := item.stats['legendary_bonus']:
            self.item_to_bonus[item.name] = new_bonus
            if new_bonus not in self.bonuses:
                self.bonuses[new_bonus] = 1
            else:
                self.bonuses[new_bonus] += 1
            del item.stats['legendary_bonus']
        # Add rest of stats
        for key in item.stats:
            if key in self.stats:
                self.stats[key] += item.stats[key]
            else:
                self.stats[key] = item.stats[key]

        # ToDo
        # Remove item under certain condition (the same name for now)
        # self.remove(item.name)
        # Check if new item type existed before and erase if so

    def remove(self, name: str):
        for el in self.items:
            if el.name == name:
                self.items.remove(el)
                bon_to_del = self.item_to_bonus[el.name]
                self.bonuses[bon_to_del] -= 1
                if self.bonuses[bon_to_del] == 0:
                    del self.bonuses[bon_to_del]
                for key in el.stats:
                    if key in self.stats:
                        self.stats[key] -= el.stats[key]
                    if self.stats[key] == 0:
                        del self.stats[key]
