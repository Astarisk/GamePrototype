from spritesheet import SpriteSheet
from sprite import Sprite


class Player:

    PLAYERWIDTH = 24
    PLAYERHEIGHT = 32

    PLAYER_SPEED = 2

    #movement_directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    # 0,0 on the sprite sheet is bot left due to how pyglet does it
    # for movement on base-sprites2 this means
    # NW, W, SW, S, SE, E, NE, N
    # would be how the sprite data is stored by row
    movement_directions = ["NW", "W", "SW", "S", "SE", "E", "NE", "N"]

    def __init__(self):
        self.sprites = []
        self.sheet = SpriteSheet("res/player/base-sprites2.png")
        #self.sheet.strip_sheet(12, 8, 32, 32)
        self.sheet.strip_sheet(8, 8, 32, 32)

        # World position
        self.x = 0
        self.y = 0

        self.facing_direction = "N"

        #Sprite(self.sheet.images[value], x=x * Map.TILEWIDTH, y=y * Map.TILEHEIGHT,
        #       batch=self.map_sprite_batch)
        self.sprite = Sprite(self.sheet.images[0], x=self.x, y=self.y)

        # Animation
        self.animation_frame = 0
        self.animation_frames = 3
        self.frame_time = 0
        self.animation_time = .25

    def draw(self, dt):
        num = 0
        if self.facing_direction in Player.movement_directions:
            num = Player.movement_directions.index(self.facing_direction) * 8
        self.sprite = Sprite(self.sheet.images[num + self.animation_frame], x=self.sprite.x, y=self.sprite.y)
        self.sprite.draw()

        if self.frame_time >= self.animation_time:
            self.frame_time = 0
            self.animation_frame = (self.animation_frame + 1) % self.animation_frames

        self.frame_time = self.frame_time + dt

    def move_player(self, x, y):
        direction = ""

        if y < 0:
            direction = direction + "S"
        if y > 0:
            direction = direction + "N"

        if x > 0:
            direction = direction + "E"
        if x < 0:
            direction = direction + "W"

        self.facing_direction = direction

        self.sprite.x = self.sprite.x + x
        self.sprite.y = self.sprite.y + y

