from random import random

from app.helper import Point
from app.models.strategies import MovementBehaviour


class ChasingBehaviour(MovementBehaviour):
    def __init__(self):
        super().__init__()

    def get_new_location(self, game_object_location, player_object_location, initial_game_object_location):
        if player_object_location.x > game_object_location.x + 0.1:
            return Point(game_object_location.x + 0.005, game_object_location.y)
        else:
            if player_object_location.x < game_object_location.x - 0.1:
                return Point(game_object_location.x - 0.005, game_object_location.y)
            else:
                if player_object_location.x > game_object_location.x:
                    return Point(game_object_location.x - 0.002, game_object_location.y)
                else:
                    return Point(game_object_location.x + 0.002, game_object_location.y)
