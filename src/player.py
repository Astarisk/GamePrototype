import pygame
from spritesheet import SpriteSheet


class Player:

    PLAYERWIDTH = 24
    PLAYERHEIGHT = 32

    def __init__(self):
        #self.sprite_group = pygame.sprite.Group()
        self.sprites = []
        self.sheet = SpriteSheet("res/player/base-m-light.png")

        self.sprites.append(self.sheet.image_at((0, 0, Player.PLAYERWIDTH, Player.PLAYERHEIGHT)))

        self.x = 0
        self.y = 0

    def draw(self, display):
        pass


