from spritesheet import SpriteSheet
from collections import OrderedDict

import pyglet
from pyglet.gl import *
from sprite import Sprite


class Tile:
    def __init__(self, sprite, x, y):
        self.sprite = sprite

        # World position
        self.x = x
        self.y = y

    # # TODO: Not in use.
    # def draw(self):
    #     glLoadIdentity()
    #     glTranslatef(self.x, self.y, 0.0)
    #     glRotatef(self.rot, 0, 0, 1)
    #     glScalef(self.size, self.size, 1.0)
    #     draw image


class Map:
    TILEWIDTH = 32
    TILEHEIGHT = 32

    MAPWIDTH = 50
    MAPHEIGHT = 50

    def __init__(self):
        self.tiles = OrderedDict()
        self.sheet = SpriteSheet("res/Woodland_ground.png")
        self.grass_tiles = [144, 160, 176, 192, 208, 224, 240,
                            145, 161]
        self.sheet.strip_sheet(16, 16, 32, 32)
        self.tile_sprites = []

        self.map_sprite_batch = pyglet.graphics.Batch()

        for x in range(Map.MAPWIDTH):
            for y in range(Map.MAPHEIGHT):
                #tile_rect = pygame.Rect(x * Map.TILEWIDTH, y * Map.TILEHEIGHT, Map.TILEWIDTH, Map.TILEHEIGHT)

                index = len(self.tiles)

                from random import randint, seed
                seed(x * y)
                value = randint(0, len(self.grass_tiles) - 1)
                self.tiles[index] = Tile(Sprite(self.sheet.images[self.grass_tiles[value]], x=x * Map.TILEWIDTH,
                                                y=y * Map.TILEHEIGHT, batch=self.map_sprite_batch), x, y)

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        #glLoadIdentity()

        # Tranformations for the tiles after here.

        self.map_sprite_batch.draw()

    def update(self, dt):
        pass

    def move_tile(self, coord):
        for t in self.tiles:
            self.tiles[t].x = self.tiles[t].sprite.x + coord[0]
            self.tiles[t].y = self.tiles[t].sprite.y + coord[1]

    def world2screen(self):
        pass

    def screen2world(self):
        pass
