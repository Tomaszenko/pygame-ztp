from .mutant_object import MutantObject


class StrongerObject(MutantObject):
    def __init__(self, base_object, how_many_stronger):
        super().__init__(base_object)
        self._how_many_stronger = how_many_stronger

    def on_player_collision(self):
        return self._base_object.on_player_collision(2)
