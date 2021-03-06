from abc import ABC, abstractmethod


class GameView(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def update(self, model, state):
        pass

    @abstractmethod
    def process_input(self):
        pass

    @abstractmethod
    def quit(self):
        pass