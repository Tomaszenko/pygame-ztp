import uuid

from app.models.game_object import GameObject


class Player(GameObject):
    def __init__(self):
        super().__init__(x_pos=0, y_pos=0, width=0.1, height=0.15)
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
            self.__vy -= 0.01
            if self.y <= 0:
                self.y = 0
                self.__jumping = False

    def turn_left(self):
        self.__direction = "left"

    def turn_right(self):
        self.__direction = "right"

    def jump(self):
        if not self.__jumping:
            self.__jumping = True
            self.__vy = 0.05

    def go_left(self):
        self.x -= 0.01
        self.x = max(self.x, 0)
        if self.x <= 0:
            self.bounce_of_the_wall()

    def go_right(self):
        self.x += 0.01
        self.x = min(self.x, 1 - self.width)
        if self.x >= 1-self.width:
            self.bounce_of_the_wall()

    def bounce_of_the_wall(self):
        if self.__direction == "left":
            self.__direction = "right"
        else:
            self.__direction = "left"

    @property
    def direction(self):
        return self.__direction

    def get_name(self):
        return "player"
