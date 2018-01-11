from app.events import TexanMassacre
from app.models import ModifierObject


class Saw(ModifierObject):
    def __init__(self, location, width, height, strategy):
        super().__init__(location=location, width=width, height=height, strategy=strategy)

    def get_name(self):
        return "saw"

    def on_player_collision(self, relative_impact=1):
        return TexanMassacre(relative_effect=relative_impact)
