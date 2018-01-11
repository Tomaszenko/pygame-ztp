from math import atan2, sin, cos

from app.helper import Point
from app.strategies import MovementBehaviour


class AggressiveBehaviour(MovementBehaviour):
    def __init__(self):
        super().__init__()

    def get_new_location(self, game_object_location, player_object_location, initial_game_object_location):
        y_difference = player_object_location.y - game_object_location.y
        x_difference = player_object_location.x - game_object_location.x

        phi = atan2(y_difference, x_difference)

        x_change = cos(phi) * 0.01
        y_change = sin(phi) * 0.01

        return Point(game_object_location.x + x_change, game_object_location.y + y_change)
