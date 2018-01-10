from app.models import ModifierObject
from app.models.events import TexanMassacre


class Saw(ModifierObject):
    def __init__(self, x_pos, width, height, strategy):
        super().__init__(x_pos=x_pos, y_pos=0, width=width, height=height, strategy=strategy)

    def get_name(self):
        return "saw"

    def on_player_collision(self):
        return TexanMassacre()
