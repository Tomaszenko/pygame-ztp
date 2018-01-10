from app.models import ModifierObject
from app.models.events import HealthBonus


class Life(ModifierObject):
    def __init__(self, location, width, height, strategy):
        super().__init__(location=location, width=width, height=height, strategy=strategy)

    def get_name(self):
        return "life"

    def on_player_collision(self):
        return HealthBonus()
