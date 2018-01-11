from abc import ABC

from app.models import ModifierObject


class MutantObject(ModifierObject, ABC):
    def __init__(self, base_object):
        self._base_object = base_object

    @property
    def id(self):
        return self._base_object.id

    @id.setter
    def id(self, value):
        self._base_object.id = value

    def get_name(self):
        return self._base_object.get_name()

    @property
    def width(self):
        return self._base_object.width

    @width.setter
    def width(self, value):
        self._base_object.width = value

    @property
    def height(self):
        return self._base_object.width

    @height.setter
    def height(self, value):
        self._base_object.width = value

    @property
    def destroyed(self):
        return self._base_object.destroyed

    @destroyed.setter
    def destroyed(self, value):
        self._base_object.destroyed = value

    def on_player_collision(self):
        return self._base_object.on_player_collision()

    def move(self, player_location):
        self._base_object.move(player_location)

    @property
    def strategy(self):
        return self._base_object.strategy()

    @strategy.setter
    def strategy(self, value):
        self._base_object.strategy = value

    @property
    def x(self):
        return self._base_object.x

    @property
    def y(self):
        return self._base_object.y

    @y.setter
    def y(self, value):
        self._base_object.y = value

    def get_size(self):
        return self._base_object.get_size()

    def get_location(self):
        return self._base_object.get_location()
