from app.helper import Point
from app.models import ModifierObject
from app.models.events import Explosion


class Bomb(ModifierObject):
    def __init__(self, location, width, height, strategy):
        super().__init__(location=location, width=width, height=height, strategy=strategy)

    def get_name(self):
        return "bomb"

    def on_player_collision(self, relative_impact=1):
        return Explosion(relative_effect=relative_impact)
