# Basic class structures for item, eq, player relation
import secrets

class Item:
    def __init__(self, lvl : int, prof : str, atype : str, name : str, stats : dict):
        self.id = f'{name}-{atype}-{lvl}-{prof}'
        self.lvl = lvl
        self.prof = prof
        self.atype = atype
        self.name = name
        self.stats = stats
        
    def toList(self):
        return [self.lvl, self.prof, self.atype, self.name, self.stats]
        
class Eq(Item):
    def __init__(self):
        self.items = []
        self.stats = {}
        
    def check(self, item : Item):
        # Check compatibility of classes with 1st item in eq
        zipped = set(zip(self.items[0].prof, item.prof))
        for el in zipped:
            if el[0] == el[1]:
                return True
        return False
        
    def add(self, item : Item):
        # Check if new item type existed before
        self.remove(item.atype)
        # Append new item to eq
        self.items.append(item)
        for key, val in item.stats.items():
            if key in self.stats:
                self.stats[key] += val
            else:
                self.stats[key] = val
                
    def remove(self, acctype : str):
        for i in self.items:
            if i.atype == acctype:
                self.items.remove(i)
                for key, val in i.stats.items():
                    if key in self.stats:
                        self.stats[key] -= val
                    if self.stats[key] == 0:
                        del self.stats[key]

class Player:
    def __init__(self, lvl : int, prof : str, eq_stats : dict, um_stats: dict):
        self.id = secrets.token_hex(16)
        self.proffesion = prof
        self.eq_stats = eq_stats
        
    def getStats(lvl : int):
        pass
    
class FightSimulator:
    def __init__(self, players : list):
        self.players = players
        
    @staticmethod
    def fightSimulator(p1, p2):
    
        initial_stats = []
        updatibles = []
        final_stats = []