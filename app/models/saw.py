from app.models import ModifierObject
from app.models.events import TexanMassacre


class Saw(ModifierObject):
    def __init__(self, location, width, height, strategy):
        super().__init__(location=location, width=width, height=height, strategy=strategy)

    def get_name(self):
        return "saw"

    def on_player_collision(self):
        return TexanMassacre()
