from app.models.game_object import GameObject
from abc import ABC, abstractmethod


class ModifierObject(GameObject, ABC):

    def __init__(self, x_pos, y_pos, width, height, strategy):
        super().__init__(x_pos=x_pos, y_pos=y_pos, width=width, height=height)
        self.__move_strategy = strategy

    def move(self):
        self.x, self.y = self.__move_strategy.get_new_location(self.x, self.y)
        if self.x < 0-self.width or self.x > 1 or self.y < 0 or self.y > 1:
            self.destroyed = True

    def on_destroy(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
