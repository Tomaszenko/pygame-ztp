from app.models import Bomb, Player, Life, Saw, Star
from random import random, randint


class GameModel:
    def __init__(self):
        self.player = Player()
        self.ref_height = 0.15
        self.ref_width = 0.1
        self.modifier_objects = []
        self.object_types = ["bomb", "life", "saw", "star"]

    def update(self, new_object_probability):
        if random() < new_object_probability:
            new_object_type = self.object_types[randint(0, 3)]
            if new_object_type == "bomb":
                self.modifier_objects.append(Bomb(x_pos=random()*self.ref_width, width=self.ref_width,
                                                  height=self.ref_height, strategy=None))
            if new_object_type == "life":
                self.modifier_objects.append(Life(x_pos=random()*self.ref_width, width=self.ref_width,
                                                  height=self.ref_height, strategy=None))
            if new_object_type == "saw":
                self.modifier_objects.append(Saw(x_pos=random()*self.ref_width, width=self.ref_width,
                                                  height=self.ref_height, strategy=None))
            if new_object_type == "star":
                self.modifier_objects.append(Star(x_pos=random()*self.ref_width, width=self.ref_width,
                                                  height=self.ref_height, strategy=None))

        self.player.update()
