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

    def on_init(self):
        self._view = PyGameView(self)
        self._view.initialize()
        self._model = GameModel()
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

    def on_render(self):
        self._view.update(self._model, None)

    def on_cleanup(self):
        self._view.quit()

    def run(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            # for event in pygame.event.get():
            #     self.on_event(event)
            self.update_model()
            self.on_render()
            self._view.process_input()
            self._clock.tick(60)
        self.on_cleanup()

