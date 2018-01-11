from .player_impact_event import PlayerImpactEvent


class PointsBoost(PlayerImpactEvent):
    def __init__(self, relative_effect):
        super().__init__(relative_effect=relative_effect)

    def get_health_change(self):
        return 0

    def get_points_change(self):
        return 5 * self._relative_effect
