from app.models.game_object import GameObject


class ModifierObject(GameObject):

    def __init__(self, location, strategy):
        super().__init__()
        self.__location = location
        self.__strategy = strategy