from abc import ABC, abstractmethod


class MovementBehaviour(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_new_location(self, game_object_location, player_object_location, initial_object_location):
        pass
