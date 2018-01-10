from app.models.events.player_impact_event import PlayerImpactEvent


class TexanMassacre(PlayerImpactEvent):
    def get_health_change(self):
        return -10

    def get_points_change(self):
        return 0
