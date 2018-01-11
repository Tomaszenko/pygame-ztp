from app.events import HealthBonus
from app.models import ModifierObject


class Life(ModifierObject):
    def __init__(self, location, width, height, strategy):
        super().__init__(location=location, width=width, height=height, strategy=strategy)

    def get_name(self):
        return "life"

    def on_player_collision(self, relative_impact=1):
        return HealthBonus(relative_effect=relative_impact)
