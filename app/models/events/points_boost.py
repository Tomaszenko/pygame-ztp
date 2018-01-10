from app.models.events.player_impact_event import PlayerImpactEvent


class PointsBoost(PlayerImpactEvent):
    def get_health_change(self):
        return 0

    def get_points_change(self):
        return 5