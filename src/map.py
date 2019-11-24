import pygame
from spritesheet import SpriteSheet
from collections import OrderedDict

class Tile:
    def __init__(self, image, cx, cy):
        self.image = image
        self.cx = cx
        self.cy = cy


class Map:
    TILEWIDTH = 32
    TILEHEIGHT = 32

    MAPWIDTH = 50
    MAPHEIGHT = 50

    def __init__(self):
        self.tile_group = pygame.sprite.Group()
        self.tiles = OrderedDict()
        self.sheet = SpriteSheet("res/Woodland_ground.png")
        self.tile_sprites = []

        self.tile_sprites.append(self.sheet.image_at((0, 0, Map.TILEWIDTH, Map.TILEHEIGHT)))
        self.tile_sprites.append(self.sheet.image_at((0, 32 * 6, Map.TILEWIDTH, Map.TILEHEIGHT)))

        for x in range(Map.MAPWIDTH):
            for y in range(Map.MAPHEIGHT):
                tile_rect = pygame.Rect(x * Map.TILEWIDTH, y * Map.TILEHEIGHT, Map.TILEWIDTH, Map.TILEHEIGHT)

                index = len(self.tiles)

                from random import randint, seed
                seed(x * y)
                value = randint(0, 1)

                self.tiles[index] = pygame.sprite.Sprite()
                self.tiles[index].image = self.tile_sprites[value]
                self.tiles[index].rect = tile_rect
                self.tile_group.add(self.tiles[index])

    def draw(self, display):
        #self.tile_group.update()
        self.tile_group.draw(display)

    def move_tile(self, coord):
        for index in self.tiles:
            self.tiles[index].rect = self.tiles[index].rect.move(coord[0], coord[1])


    def world2screen(self):
        pass

    def screen2world(self):
        pass
