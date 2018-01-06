from app.models.player import Player


class GameModel:
    def __init__(self):
        self.player = Player()
        self.ref_height = 0.15
        self.ref_width = 0.1

    def update(self):
        self.player.update()
