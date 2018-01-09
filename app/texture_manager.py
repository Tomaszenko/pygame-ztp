import pygame


class TextureManager:
    __instance = None

    class __TextureManager:
        def __init__(self):
            self.__base_sprites = {
                "frog": [
                    pygame.image.load('img/boi1.png'),
                    pygame.image.load('img/boi2.png'),
                    pygame.image.load('img/boi3.png'),
                    pygame.image.load('img/boi4.png'),
                    pygame.image.load('img/boi5.png')
                ]
            }

            self.__base_images = {
                "life": pygame.image.load("img/life.png"),
                "star": pygame.image.load("img/star.png"),
                "bomb": pygame.image.load("img/bomb.png"),
                "saw": pygame.image.load("img/saw.png"),
                "block": pygame.image.load("img/block.bmp")
            }

            self.__background = {
                "background": pygame.image.load("img/background.jpg")
            }

        def sprites(self):
            return self.__base_sprites

        def images(self):
            return self.__base_images

        def background(self):
            return self.__background

    def __init__(self):
        if TextureManager.__instance is None:
            TextureManager.__instance = TextureManager.__TextureManager()

    def load_sprites(self):
        if self.__instance is None:
            raise Exception('texture manager has not been instantiated yet')
        return self.__instance.sprites()

    def load_images(self):
        if self.__instance is None:
            raise Exception('texture manager has not been instantiated yet')
        return self.__instance.images()

    def load_background(self):
        if self.__instance is None:
            raise Exception('texture manager has not been instantiated yet')
        return self.__instance.background()
