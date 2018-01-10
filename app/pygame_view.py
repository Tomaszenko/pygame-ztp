import pygame

from app.game_view import GameView
from app.texture_manager import TextureManager
from keyboard_events import KeyboardEvent


class PyGameView(GameView):
    def __init__(self, manager):
        super(GameView, self).__init__()
        pygame.init()
        self.size = self.width, self.height = 1024, 768
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Le Froż')

        self._manager = manager
        self._texture_manager = TextureManager()

        self._text_font = pygame.font.SysFont("monospace", 24)

        self._images = self.load_base_images()
        self._spritesheets = self.load_base_sprites()
        self._background = self.load_background()

        self._player_state = 0

        self._floor_level = self._images["block"].get_rect().height

        self._prev_locations = {}

    def load_base_images(self):
        return self._texture_manager.load_images()

    def load_base_sprites(self):
        return self._texture_manager.load_sprites()

    def load_background(self):
        return self._texture_manager.load_background()

    def get_image_for_player_object(self, player_object):
        image = self.find_player_image(player_object)

        rect_in_memory = image.get_rect().width, image.get_rect().height
        rect_needed = self.calculate_pixel_size(player_object)

        if rect_in_memory[0] != rect_needed[0] or rect_in_memory[1] != rect_needed[1]:
            new_image = pygame.transform.scale(image, (rect_needed[0], rect_needed[1]))
            self._spritesheets[self._player_state] = new_image
            return new_image
        else:
            return image

    def get_image_for_object(self, game_object):
        image = self.find_object_image(game_object=game_object)

        rect_in_memory = image.get_rect().width, image.get_rect().height
        rect_needed = self.calculate_pixel_size(game_object)

        if rect_in_memory[0] != rect_needed[0] or rect_in_memory[1] != rect_needed[1]:
            new_image = pygame.transform.scale(image, (rect_needed[0], rect_needed[1]))
            self._spritesheets[self._player_state] = new_image
            return new_image
        else:
            return image

    def find_object_image(self, game_object):
        object_name = game_object.get_name()
        return self._images[object_name]

    def find_player_image(self, player):
        return self._spritesheets["frog"][self._player_state]

    def calculate_pixel_position(self, game_object):
        object_pixel_width, object_pixel_height = game_object.get_size()
        pixel_x = game_object.x * self.width
        pixel_y = (1 - game_object.y - object_pixel_height) * self.height - self._floor_level

        return pixel_x, pixel_y

    def calculate_pixel_size(self, game_object):
        game_object_width, game_object_height = game_object.get_size()

        pixel_width = int(game_object_width * self.width)
        pixel_height = int(game_object_height * self.height)

        return pixel_width, pixel_height

    def initialize(self):
        super().initialize()
        self._render_floor(self._images["block"])

    def update(self, model, destroyed_objects=None, state="game"):
        if destroyed_objects is not None:
            rects_erased = []
            for destroyed_object in destroyed_objects:
                if destroyed_object.id in self._prev_locations:
                    rect_erased = pygame.draw.rect(self._display_surf, (0, 0, 0),
                                                   [self._prev_locations[destroyed_object.id][0],
                                                    self._prev_locations[destroyed_object.id][1],
                                                    self.calculate_pixel_size(destroyed_object)[0],
                                                    self.calculate_pixel_size(destroyed_object)[1]])
                    rects_erased.append(rect_erased)
            pygame.display.update(rects_erased)
        self.render(model)

    def process_input(self):
        for event in pygame.event.get():
            self.on_event(event)

    def quit(self):
        pass

    def render(self, model):
        rects_to_update = []

        rects_to_update += self._redraw_player(model.player)

        for modifier_object in model.modifier_objects:
            rects_to_update += self._redraw_object(modifier_object=modifier_object)

        rects_to_update += self._redraw_health(model.player.health_points, 0.75*self.width, 0.05*self.height)
        rects_to_update += self._redraw_points(model.player.score, 0.75*self.width, 0.15*self.height)

        pygame.display.update()

        self._player_state -= 1
        if self._player_state < 0:
            self._player_state = 4

    def _redraw_player(self, player):
        image = self.get_image_for_player_object(player)

        img_width = image.get_rect().width
        img_height = image.get_rect().height

        rects_to_update = []

        if player.id in self._prev_locations:
            rect_erased = pygame.draw.rect(self._display_surf, (0, 0, 0), [self._prev_locations[player.id][0],
                                                                           self._prev_locations[player.id][1],
                                                                           img_width, img_height])
            rects_to_update.append(rect_erased)

        x_pos, y_pos = self.calculate_pixel_position(player)

        if player.direction == "left":
            rect_drawn = self._display_surf.blit(image, (x_pos, y_pos))
        else:
            rect_drawn = self._display_surf.blit(pygame.transform.flip(image, True, False), (x_pos, y_pos))

        rects_to_update.append(rect_drawn)

        if player.id not in self._prev_locations:
            self._prev_locations[player.id] = [x_pos, y_pos]
        else:
            self._prev_locations[player.id][0] = x_pos
            self._prev_locations[player.id][1] = y_pos

        return rects_to_update

    def _redraw_object(self, modifier_object):
        image = self.get_image_for_object(modifier_object)

        img_width = image.get_rect().width
        img_height = image.get_rect().height

        rects_to_update = []

        if modifier_object.id in self._prev_locations:
            rect_erased = pygame.draw.rect(self._display_surf, (0, 0, 0), [self._prev_locations[modifier_object.id][0],
                                                                           self._prev_locations[modifier_object.id][1],
                                                                           img_width, img_height])
            rects_to_update.append(rect_erased)

        x_pos, y_pos = self.calculate_pixel_position(modifier_object)

        rect_drawn = self._display_surf.blit(image, (x_pos, y_pos))

        rects_to_update.append(rect_drawn)

        if modifier_object.id not in self._prev_locations:
            self._prev_locations[modifier_object.id] = [x_pos, y_pos]
        else:
            self._prev_locations[modifier_object.id][0] = x_pos
            self._prev_locations[modifier_object.id][1] = y_pos

        return rects_to_update

    def _render_background(self):
        background = self._background["background"]
        main_surface = self._display_surf.blit(background, (0, 0))

        rects_to_update = [main_surface]
        pygame.display.update(rects_to_update)

    def _render_floor(self, image):
        rects_to_update = []

        img_width = image.get_rect().width

        y_pos = self.height - image.get_rect().height
        x_pos = 0

        while x_pos < self.width:
            rect_drawn = self._display_surf.blit(image, (x_pos, y_pos))
            rects_to_update.append(rect_drawn)
            x_pos += img_width

        pygame.display.update(rects_to_update)

    def _redraw_health(self, m_health, x, y):
        rect_erased = self._display_surf.fill(pygame.Color("black"), (x, y, 0.2*self.width, 0.1*self.height))
        health = self._text_font.render("ZDROWIE: " + str(m_health), 1, (128, 255, 0))
        rect_drawn = self._display_surf.blit(health, (x, y))
        return [rect_erased, rect_drawn]

    def _redraw_points(self, m_points, x, y):
        rect_erased = self._display_surf.fill(pygame.Color("black"), (x, y, 0.2*self.width, 0.1*self.height))
        scored_points = self._text_font.render("PUNKTY: " + str(m_points), 1, (128, 255, 0))
        rect_drawn = self._display_surf.blit(scored_points, (x, y))
        return [rect_erased, rect_drawn]

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
