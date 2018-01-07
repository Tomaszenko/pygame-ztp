from app.models.strategies import MovementBehaviour


class FastVerticalDrop(MovementBehaviour):
    def __init__(self):
        super().__init__()

    def get_new_location(self, current_x, current_y):
        return current_x, current_y - 0.01
