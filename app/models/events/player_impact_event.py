from abc import ABC, abstractmethod


class PlayerImpactEvent(ABC):
    def __init__(self, relative_effect=1):
        self._relative_effect = relative_effect

    @abstractmethod
    def get_health_change(self):
        pass

    @abstractmethod
    def get_points_change(self):
        pass
