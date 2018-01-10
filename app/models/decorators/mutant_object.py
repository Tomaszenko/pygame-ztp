from abc import ABC

from app.models import ModifierObject


class MutantObject(ModifierObject, ABC):
    def __init__(self, base_object):
        base_object_width, base_object_height = base_object.get_size()
        super().__init__(base_object.x, base_object.y, base_object_width,
                         base_object_height, base_object.strategy)
        self._base_object = base_object
        self._name = self._base_object.get_name()

    def get_name(self):
        return self._name

    def on_player_collision(self):
        return self._base_object.on_player_collision()
