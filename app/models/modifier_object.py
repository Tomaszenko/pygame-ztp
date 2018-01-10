from app.helper import Point
from app.models.game_object import GameObject
from abc import ABC, abstractmethod


class ModifierObject(GameObject, ABC):

    def __init__(self, location, width, height, strategy):
        super().__init__(location=location, width=width, height=height)
        self.__move_strategy = strategy
        self.__initial_location = location

    def move(self, player_location):
        self._location = self.__move_strategy.get_new_location(
            self._location, player_location, self.__initial_location
        )

    def on_destroy(self):
        pass

    @property
    def strategy(self):
        return self.__move_strategy

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def on_player_collision(self):
        pass
