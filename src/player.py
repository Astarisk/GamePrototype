from spritesheet import SpriteSheet
from sprite import Sprite


class Player:

    PLAYERWIDTH = 24
    PLAYERHEIGHT = 32

    def __init__(self):
        self.sprites = []
        self.sheet = SpriteSheet("res/player/base-m-light.png")
        self.sheet.strip_sheet(3, 4, 24, 32)

        # World position
        self.x = 0
        self.y = 0

        #Sprite(self.sheet.images[value], x=x * Map.TILEWIDTH, y=y * Map.TILEHEIGHT,
        #       batch=self.map_sprite_batch)
        self.sprite = Sprite(self.sheet.images[0], x=self.x, y=self.y)

    def draw(self):
        self.sprite.draw()

    def move_player(self, x, y):
        self.sprite.x = self.sprite.x + x
        self.sprite.y = self.sprite.y + y


