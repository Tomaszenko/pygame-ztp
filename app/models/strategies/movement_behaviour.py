from abc import ABC, abstractmethod


class MovementBehaviour(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_new_location(self, current_x, current_y):
        pass
