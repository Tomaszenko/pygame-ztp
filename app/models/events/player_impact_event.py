from abc import ABC, abstractmethod


class PlayerImpactEvent(ABC):
    @abstractmethod
    def get_health_change(self):
        pass

    @abstractmethod
    def get_points_change(self):
        pass
