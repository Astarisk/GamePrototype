from map import Map
from camera import FollowCam
from player import Player

import pyglet
from pyglet import gl
from pyglet.window import key


class GameWindow(pyglet.window.Window):
    WINWIDTH = 800
    WINHEIGHT = 600

    HALF_WINWIDTH = WINWIDTH / 2
    HALF_WINHEIGHT = WINHEIGHT / 2

    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(GameWindow.WINWIDTH, GameWindow.WINHEIGHT, *args, **kwargs)

        # Set the update loop to run 60 times a second.
        pyglet.clock.schedule_interval(self.update, 1 / 60)

        self.fps_display = pyglet.window.FPSDisplay(self)
        self.fps_display.label.font_size = 50
        self.fps_display.label.color = (255, 255, 255, 255)

        # Keyboard controls
        self.keys = {}

        # Cam should be binded to player location once the screen offset is added on.
        self.cam = FollowCam(x=-GameWindow.WINWIDTH/2, y=-GameWindow.WINHEIGHT/2)
        self.map = Map()
        self.player = Player()
        self.alive = True

        self.init_gl()

    def init_gl(self):
        gl.glViewport(0, 0, self.width, self.height)

    def run(self):
        while self.alive:
            # Tick the clock at the end of the frame.
            dt = pyglet.clock.tick()

            event = self.dispatch_events()
            if event:
                print(event)

            #print(dt)
            self.on_draw(dt=dt)


    def on_close(self):
        self.alive = False

    def on_key_release(self, symbol, modifiers):
        try:
            del self.keys[symbol]
        except:
            pass

    def on_key_press(self, symbol, modifiers):
        self.keys[symbol] = True

    def on_draw(self, dt=0.0):
        # Clear the window
        self.clear()

        self.cam.worldProjection()

        # Draw sprites
        self.map.draw()
        self.player.draw(dt)

        # GUI elements
        self.fps_display.draw()

        # since i'm doing my own run for window I need to flip the buffer
        self.flip()

    def update(self, dt):
        interval = Player.PLAYER_SPEED * dt
        xt = 0
        yt = 0

        if key.A in self.keys:
            xt = -32
        if key.D in self.keys:
            xt = 32
        if key.W in self.keys:
            yt = 32
        if key.S in self.keys:
            yt = -32

        self.player.move_player(int(xt * interval), int(yt * interval))

        self.cam.x = int(self.player.sprite.x + -GameWindow.WINWIDTH/2)
        self.cam.y = int(self.player.sprite.y + -GameWindow.WINHEIGHT/2)
