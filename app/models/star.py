from app.models import ModifierObject
from app.models.events import PointsBoost


class Star(ModifierObject):
    def __init__(self, location, width, height, strategy):
        super().__init__(location=location, width=width, height=height, strategy=strategy)

    def get_name(self):
        return "star"

    def on_player_collision(self, relative_impact=1):
        return PointsBoost(relative_effect=relative_impact)
