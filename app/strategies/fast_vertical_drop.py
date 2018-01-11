from app.helper import Point
from app.strategies import MovementBehaviour


class FastVerticalDrop(MovementBehaviour):
    def __init__(self):
        super().__init__()

    def get_new_location(self, game_object_location, player_object_location, initial_object_location):
        return Point(game_object_location.x, game_object_location.y - 0.01)
