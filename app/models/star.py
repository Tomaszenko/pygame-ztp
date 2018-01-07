from app.models import ModifierObject


class Star(ModifierObject):
    def __init__(self, x_pos, width, height, strategy):
        super().__init__(x_pos=x_pos, y_pos=1, width=width, height=height, strategy=strategy)

    def get_name(self):
        return "star"