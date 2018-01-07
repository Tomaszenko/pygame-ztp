from app.models.game_object import GameObject
from abc import ABC, abstractmethod


class ModifierObject(GameObject, ABC):

    def __init__(self, x_pos, y_pos, width, height, strategy):
        super().__init__(x_pos=x_pos, y_pos=y_pos, width=width, height=height)
        self.__strategy = strategy

    @abstractmethod
    def get_name(self):
        pass
