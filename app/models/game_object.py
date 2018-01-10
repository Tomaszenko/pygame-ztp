import uuid
from abc import ABC, abstractmethod


class GameObject(ABC):

    def __init__(self, location, width, height):
        self.id = uuid.uuid4()
        self._width = width
        self._height = height
        self._location = location
        # self.x = x_pos
        # self.y = y_pos
        self.destroyed = False

    def get_size(self):
        return self._width, self._height

    @abstractmethod
    def get_name(self):
        pass

    @property
    def x(self):
        return self._location.x

    @x.setter
    def x(self, value):
        self._location.x = value

    @property
    def y(self):
        return self._location.y

    @y.setter
    def y(self, value):
        self._location.y = value

    def get_location(self):
        return self._location
