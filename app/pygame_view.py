import pygame

from app.game_view import GameView
from keyboard_events import KeyboardEvent


class PyGameView(GameView):
    def __init__(self, manager):
        super(GameView, self).__init__()
        pygame.init()
        self.size = self.weight, self.height = 640, 400
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Le Froż')
        self._manager = manager
        self._frog_img = pygame.image.load('img/frog.png')
        self._prev_locations = {}
        # self._surface = pygame.display.get_surface()

    def initialize(self):
        super().initialize()

    def update(self, model, state):
        self.render(model)

    def process_input(self):
        for event in pygame.event.get():
            self.on_event(event)

    def quit(self):
        pass

    def render(self, model):
        self._render_rect(model.player)
        # for event in pygame.event.get():
        #     self.on_event(event)

    def _render_rect(self, player):
        img_width = self._frog_img.get_rect().width
        img_height = self._frog_img.get_rect().height

        rects_to_update = []

        if player.id in self._prev_locations:
            rect_erased = pygame.draw.rect(self._display_surf, (0, 0, 0), [self._prev_locations[player.id][0],
                                                                           self._prev_locations[player.id][1],
                                                                           img_width, img_height])
            rects_to_update.append(rect_erased)

        y_pos = self.height - self._frog_img.get_rect().height
        x_pos = player.x
        rect_drawn = self._display_surf.blit(self._frog_img, (x_pos, y_pos))
        rects_to_update.append(rect_drawn)
        # pygame.display.update(rect_drawn)
        if player.id not in self._prev_locations:
            self._prev_locations[player.id] = [x_pos, y_pos]
        else:
            self._prev_locations[player.id][0] = x_pos
            self._prev_locations[player.id][1] = y_pos
        pygame.display.update(rects_to_update)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._manager.on_event(KeyboardEvent.ESCAPE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self._manager.on_event(KeyboardEvent.ESCAPE)
            if event.key == pygame.K_UP:
                self._manager.on_event(KeyboardEvent.UP)
            if event.key == pygame.K_DOWN:
                self._manager.on_event(KeyboardEvent.DOWN)
            if event.key == pygame.K_LEFT:
                self._manager.on_event(KeyboardEvent.LEFT)
            if event.key == pygame.K_RIGHT:
                self._manager.on_event(KeyboardEvent.RIGHT)