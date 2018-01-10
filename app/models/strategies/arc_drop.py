from app.helper import Point
from app.models.strategies import MovementBehaviour


class ArcDrop(MovementBehaviour):
    def __init__(self):
        super().__init__()

    def get_new_location(self, game_object_location, player_object_location, initial_object_location):
        print(initial_object_location)
        if initial_object_location.x > 0.5:
            return Point(game_object_location.x - 0.01, game_object_location.y - (1.01 - game_object_location.y)/20)
        else:
            return Point(game_object_location.x + 0.01, game_object_location.y - (1.01 - game_object_location.y)/20)
