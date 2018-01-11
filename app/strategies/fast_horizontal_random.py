from random import random

from app.helper import Point
from app.strategies import MovementBehaviour


class FastHorizontalRandomMovement(MovementBehaviour):
    def __init__(self):
        super().__init__()

    def get_new_location(self, game_object_location, player_object_location, initial_object_location):
        if random() > 0.5:
            return Point(game_object_location.x + 0.01, game_object_location.y)
        else:
            return Point(game_object_location.x - 0.01, game_object_location.y)
