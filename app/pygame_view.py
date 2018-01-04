import pygame

from app.game_view import GameView
from app.texture_manager import TextureManager
from keyboard_events import KeyboardEvent


class PyGameView(GameView):
    def __init__(self, manager):
        super(GameView, self).__init__()
        pygame.init()
        self.size = self.width, self.height = 640, 400
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Le Froż')

        self._manager = manager
        self._texture_manager = TextureManager()

        self._images = self._texture_manager.load_images()
        self._spritesheets = self._texture_manager.load_sprites()

        self._frog_series = self._spritesheets["frog"]
        self._life_img = self._images["life"]
        self._bomb_img = self._images["bomb"]
        self._saw_img = self._images["saw"]
        self._star_img = self._images["star"]
        self._block_img = self._images["block"]

        self._player_state = 0

        self._floor_level = self._block_img.get_rect().height

        self._prev_locations = {}

    def initialize(self):
        super().initialize()
        self._render_floor(self._block_img)

    def update(self, model, state):
        self.render(model)

    def process_input(self):
        for event in pygame.event.get():
            self.on_event(event)

    def quit(self):
        pass

    def render(self, model):
        self._render_player(model.player, self._frog_series[self._player_state])
        self._player_state += 1
        if self._player_state > 4:
            self._player_state = 0

    def _render_player(self, player, image):
        img_width = image.get_rect().width
        img_height = image.get_rect().height

        rects_to_update = []

        if player.id in self._prev_locations:
            rect_erased = pygame.draw.rect(self._display_surf, (0, 0, 0), [self._prev_locations[player.id][0],
                                                                           self._prev_locations[player.id][1],
                                                                           img_width, img_height])
            rects_to_update.append(rect_erased)

        y_pos = self.height - self._floor_level - image.get_rect().height
        x_pos = player.x

        rect_drawn = self._display_surf.blit(image, (x_pos, y_pos))
        rects_to_update.append(rect_drawn)

        if player.id not in self._prev_locations:
            self._prev_locations[player.id] = [x_pos, y_pos]
        else:
            self._prev_locations[player.id][0] = x_pos
            self._prev_locations[player.id][1] = y_pos

        pygame.display.update(rects_to_update)

    def _render_object(self):
        pass

    def _render_floor(self, image):
        img_width = image.get_rect().width
        img_height = image.get_rect().height

        y_pos = self.height - image.get_rect().height
        x_pos = 0

        rects_to_update = []

        while x_pos < self.width:
            rect_drawn = self._display_surf.blit(image, (x_pos, y_pos))
            rects_to_update.append(rect_drawn)
            x_pos += img_width

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
