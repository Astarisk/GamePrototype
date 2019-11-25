import pyglet


class Sprite(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, dt):
        pass



class AnimatedSprite(Sprite):

    def __init__(self):
        self.frames = []
        self.frame_speed = 1

    def update(self):
        pass

