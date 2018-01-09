import uuid
from abc import ABC, abstractmethod


class GameObject(ABC):

    def __init__(self, x_pos, y_pos, width, height):
        self.id = uuid.uuid4()
        self._width = width
        self._height = height
        self.x = x_pos
        self.y = y_pos
        self.destroyed = False

    def get_size(self):
        return self._width, self._height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @abstractmethod
    def get_name(self):
        pass

