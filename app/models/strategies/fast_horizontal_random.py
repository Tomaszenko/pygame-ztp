from random import random

from app.models.strategies import MovementBehaviour


class FastHorizontalRandomMovement(MovementBehaviour):
    def __init__(self):
        super().__init__()

    def get_new_location(self, current_x, current_y):
        if random() > 0.5:
            return current_x + 0.01, current_y
        else:
            return current_x - 0.01, current_y
