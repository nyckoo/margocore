from abc import ABC, abstractmethod
from game_logic.structures.eq_builder import Eq


class ProfessionPattern(ABC):
    def __init__(self, lvl: int, eq: Eq):
        self.lvl = lvl
        self.eq = eq

    @property
    @abstractmethod
    def base_stats(self) -> dict[str, int]:
        raise NotImplementedError("Base stats field has to be defined!")

    @property
    @abstractmethod
    def profession(self) -> str:
        raise NotImplementedError("Profession field has to be defined!")

    @abstractmethod
    def get_base_features(self) -> None:
        pass

    @abstractmethod
    def get_abs_tree_abilities(self) -> None:
        pass
