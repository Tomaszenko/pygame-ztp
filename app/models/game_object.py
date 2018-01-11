import uuid
from abc import ABC, abstractmethod


class GameObject(ABC):

    def __init__(self, location, width, height):
        self._id = uuid.uuid4()
        self._width = width
        self._height = height
        self._location = location
        # self.x = x_pos
        # self.y = y_pos
        self._destroyed = False

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def destroyed(self):
        return self._destroyed

    @destroyed.setter
    def destroyed(self, value):
        self._destroyed = value

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

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def get_location(self):
        return self._location
