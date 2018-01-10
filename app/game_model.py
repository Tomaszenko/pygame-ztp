from app.models import Bomb, Player, Life, Saw, Star
from app.models.strategies import SlowVerticalDrop, FastVerticalDrop, FastHorizontalRandomMovement
from app.models.decorators import BiggerObject, StrongerObject

from app.utils import CollisionUtils

from random import random, randint


class GameModel:
    def __init__(self, controller):
        self.__controller = controller
        self.player = Player()
        self.ref_height = 0.15
        self.ref_width = 0.1
        self.modifier_objects = []
        self.object_types = ["bomb", "life", "saw", "star"]

    def update(self, new_object_probability):
        decoration_probability = 0.2
        if random() < new_object_probability:
            new_object_type = self.object_types[randint(0, 3)]
            new_object = self.generate_new_object(new_object_type)

            if random() < decoration_probability:
                new_object = self.decorate_object(new_object)

            self.modifier_objects.append(new_object)

        for modifier_object in self.modifier_objects:
            modifier_object.move()

        self.player.update()

        for modifier_object in self.modifier_objects:
            if CollisionUtils.check_collision(self.player, modifier_object) is True:
                event = modifier_object.on_player_collision()
                self.player.health_points += event.get_health_change()
                self.player.score += event.get_points_change()

                modifier_object.destroyed = True

                print("HEALTH: " + str(self.player.health_points))
                print("SCORE: " + str(self.player.score))

                if self.player.health_points <= 0:
                    self.__controller.on_player_kaputt()

        for modifier_object in self.modifier_objects:
            self.mark_to_destroy_if_not_in_bounds(modifier_object)

    def generate_new_object(self, object_type):
        new_object = None

        if object_type == "bomb":
            new_object = Bomb(x_pos=random() * (1 - self.ref_width), width=self.ref_width,
                              height=self.ref_height, strategy=SlowVerticalDrop())
        if object_type == "life":
            new_object = Life(x_pos=random() * (1 - self.ref_width), width=self.ref_width,
                              height=self.ref_height, strategy=FastVerticalDrop())
        if object_type == "saw":
            new_object = Saw(x_pos=random() * (1 - self.ref_width), width=self.ref_width,
                             height=self.ref_height, strategy=FastHorizontalRandomMovement())
        if object_type == "star":
            new_object = Star(x_pos=random() * (1 - self.ref_width), width=self.ref_width,
                              height=self.ref_height, strategy=SlowVerticalDrop())
        return new_object

    def decorate_object(self, object_to_decorate):
        if random() > 0.5:
            return BiggerObject(object_to_decorate, 2)
        else:
            return StrongerObject(object_to_decorate, 2)

    def remove_destroyed_objects(self):
        objects_after_removal = self.modifier_objects[:]
        for i in range(len(self.modifier_objects)):
            if self.modifier_objects[i].destroyed:
                objects_after_removal = objects_after_removal[:i] + objects_after_removal[i+1:]
        self.modifier_objects = objects_after_removal

    def get_destroyed_objects(self):
        objects_destroyed = []
        for modifier_object in self.modifier_objects:
            if modifier_object.destroyed:
                objects_destroyed.append(modifier_object)
        print("objects destroyed: " + str(len(objects_destroyed)))
        return objects_destroyed

    def on_object_destroy(self, object_id):
        pass

    def mark_to_destroy_if_not_in_bounds(self, game_object):
        game_object_width, game_object_height = game_object.get_size()
        if game_object.x < 0 - game_object_width or game_object.x > 1 or game_object.y < 0 or game_object.y > 1:
            game_object.destroyed = True


