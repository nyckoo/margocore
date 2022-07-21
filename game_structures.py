# Basic class structures for item, eq, player relation
import secrets
from dataclasses import dataclass, field


@dataclass
class Item:
    lvl: int
    prof: str
    atype: str
    name: str
    stats: dict

    def __repr__(self):
        return f'{self.lvl}/{self.prof}/{self.atype}/{self.name}'

    def to_list(self):
        return [self.lvl, self.prof, self.atype, self.name, self.stats]


@dataclass
class Eq:
    items: list = field(default_factory=lambda: [])
    stats: dict = field(default_factory=lambda: {})

    def check(self, item: Item):
        # Check compatibility of classes with 1st item in eq
        zipped = set(zip(self.items[0].prof, item.prof))
        for el in zipped:
            if el[0] == el[1]:
                return True
        return False

    def add(self, item: Item):
        # Check if new item type existed before
        self.remove(item.atype)
        # Append new item to eq
        self.items.append(item)
        for key, val in item.stats.items():
            if key in self.stats:
                self.stats[key] += val
            else:
                self.stats[key] = val

    def remove(self, acctype: str):
        for i in self.items:
            if i.atype == acctype:
                self.items.remove(i)
                for key, val in i.stats.items():
                    if key in self.stats:
                        self.stats[key] -= val
                    if self.stats[key] == 0:
                        del self.stats[key]


@dataclass
class Player:
    idx: str = field(init=False)
    lvl: int
    proffesion: str
    eq_stats: dict
    um_stats: dict

    def __post_init__(self):
        self.idx = ''.join([secrets.choice('0123456789abcdef')
                           for _ in range(10)])

    def __repr__(self):
        return f'{self.idx}/{self.lvl}/{self.proffesion}'

    @staticmethod
    def get_stats(lvl: int, prof: str):
        pass


@dataclass
class FightSimulator:
    players: list = field(default_factory=lambda: [])

    @staticmethod
    def fight_simulator(op, dp):
        initial_stats = []
        updatibles = []
        final_stats = []
