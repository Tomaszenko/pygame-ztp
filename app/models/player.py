import uuid

from app.models.game_object import GameObject


class Player:
    def __init__(self):
        self.y = 0
        self.x = 0
        self.id = uuid.uuid4()
        self.__jumping = False
        self.__vy = 0
        self.__direction = "right"

    def update(self):
        if self.__direction is not None:
            if self.__direction == "left":
                self.go_left()
            else:
                self.go_right()

        if self.__jumping is True:
            self.y += self.__vy
            self.__vy += 5
            self.y = min(0, self.y)
            if self.y == 0:
                self.__jumping = False

    def turn_left(self):
        self.__direction = "left"

    def turn_right(self):
        self.__direction = "right"

    def jump(self):
        self.__jumping = True
        self.__vy = -10

    def go_left(self):
        self.x -= 10

    def go_right(self):
        self.x += 10
