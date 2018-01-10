from app.models import ModifierObject
from app.models.events import Explosion


class Bomb(ModifierObject):
    def __init__(self, x_pos, width, height, strategy):
        super().__init__(x_pos=x_pos, y_pos=1, width=width, height=height, strategy=strategy)

    def get_name(self):
        return "bomb"

    def on_player_collision(self):
        return Explosion()
