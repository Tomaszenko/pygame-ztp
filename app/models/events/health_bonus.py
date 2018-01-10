from app.models.events.player_impact_event import PlayerImpactEvent


class HealthBonus(PlayerImpactEvent):
    def get_health_change(self):
        return 5

    def get_points_change(self):
        return 0
