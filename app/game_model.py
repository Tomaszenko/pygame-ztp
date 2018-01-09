from app.models import Bomb, Player, Life, Saw, Star, BiggerObject
from app.models.strategies import SlowVerticalDrop, FastVerticalDrop, FastHorizontalRandomMovement
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
            is_decorated = False

            if random() > 0.8:
                is_decorated = True

            new_object = None

            if new_object_type == "bomb":
                new_object = Bomb(x_pos=random()*(1-self.ref_width), width=self.ref_width,
                                  height=self.ref_height, strategy=SlowVerticalDrop())
            if new_object_type == "life":
                new_object = Life(x_pos=random()*(1-self.ref_width), width=self.ref_width,
                                  height=self.ref_height, strategy=FastVerticalDrop())
            if new_object_type == "saw":
                new_object = Saw(x_pos=random()*(1-self.ref_width), width=self.ref_width,
                                 height=self.ref_height, strategy=FastHorizontalRandomMovement())
            if new_object_type == "star":
                new_object = Star(x_pos=random()*(1-self.ref_width), width=self.ref_width,
                                  height=self.ref_height, strategy=SlowVerticalDrop())
            print("new_object=" + new_object.get_name())

            if random() > 0.5:
                modified_object = BiggerObject(new_object, 2)
                self.modifier_objects.append(modified_object)
            else:
                self.modifier_objects.append(new_object)

            print(self.modifier_objects[len(self.modifier_objects) - 1])

            print("Name after adding: " + self.modifier_objects[len(self.modifier_objects) - 1].get_name())

        for modifier_object in self.modifier_objects:
            modifier_object.move()

        self.player.update()

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
