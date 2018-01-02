import uuid
from abc import ABC, abstractmethod


class GameObject(ABC):

    def __init__(self, location, strategy):
        self.__location = location
        self.__strategy = strategy
        self.__id = uuid.uuid4()

    def get_size(self):
        return 1

    @abstractmethod
    def get_name(self):
        pass

