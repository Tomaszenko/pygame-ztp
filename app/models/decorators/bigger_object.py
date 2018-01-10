from .mutant_object import MutantObject


class BiggerObject(MutantObject):
    def __init__(self, base_object, how_many_bigger):
        super().__init__(base_object)
        self._how_many_bigger = how_many_bigger

    def get_size(self):
        return self._width * self._how_many_bigger, self._height * self._how_many_bigger

    def get_name(self):
        return super().get_name()

    def on_player_collision(self):
        return self._base_object.on_player_collision()
