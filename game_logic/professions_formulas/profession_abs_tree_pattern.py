from abc import ABC, abstractmethod


class ProfessionAbsTreePattern(ABC):
    def __init__(self, lvl: int, eq_stats: dict[str, int], abs_data: dict[str, int]):
        self.lvl = lvl
        self.eq_stats = eq_stats
        self.abs_data = abs_data

    @property
    @abstractmethod
    def blueprint(self) -> dict[int, tuple]:
        raise NotImplementedError("Blueprint field has to be defined!")

