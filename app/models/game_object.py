import uuid
from abc import ABC, abstractmethod


class GameObject(ABC):

    def __init__(self, x_pos, y_pos, width, height):
        self.id = uuid.uuid4()
        self.width = width
        self.height = height
        self.x = x_pos
        self.y = y_pos

    def get_size(self):
        return self.width, self.height

    @abstractmethod
    def get_name(self):
        pass

