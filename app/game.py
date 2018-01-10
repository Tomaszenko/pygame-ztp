import pygame

from app.game_model import GameModel
from app.pygame_view import PyGameView
from keyboard_events import KeyboardEvent


class Game:
    def __init__(self):
        self._running = True
        self._view = None
        self._model = None
        self._clock = None
        self._destroyed_objects = []

    def on_init(self):
        self._view = PyGameView(self)
        self._view.initialize()
        self._model = GameModel(self)
        self._running = True
        self._clock = pygame.time.Clock()

    def on_event(self, event):
        if event == KeyboardEvent.ESCAPE:
            self._running = False
        if event == KeyboardEvent.LEFT:
            self._model.player.turn_left()
        if event == KeyboardEvent.RIGHT:
            self._model.player.turn_right()
        if event == KeyboardEvent.UP:
            self._model.player.jump()

    def update_model(self):
        self._model.update(new_object_probability=0.005)

    def on_render(self, destroyed_objects=None):
        print(destroyed_objects)
        self._view.update(self._model, destroyed_objects)

    def on_cleanup(self):
        self._view.quit()

    def on_player_kaputt(self):
        self._running = False

    def run(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            self.update_model()
            self._destroyed_objects = self._model.get_destroyed_objects()
            self._model.remove_destroyed_objects()
            self.on_render(self._destroyed_objects)
            self._view.process_input()
            self._clock.tick(30)
        self.on_cleanup()

