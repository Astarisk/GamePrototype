import pyglet
from map import Map
from camera import FollowCam
from pyglet.window import key
from player import Player

from pyglet import gl


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
            event = self.dispatch_events()
            if event:
                print(event)

            self.on_draw()

            # Tick the clock at the end of the frame.
            pyglet.clock.tick()

    def on_close(self):
        self.alive = False

    def on_key_release(self, symbol, modifiers):
        try:
            del self.keys[symbol]
        except:
            pass

    def on_key_press(self, symbol, modifiers):
        self.keys[symbol] = True

    def on_draw(self):
        # Clear the window
        self.clear()

        self.cam.worldProjection()

        # Draw sprites
        self.map.draw()
        self.player.draw()

        # GUI elements
        self.fps_display.draw()

        # since i'm doing my own run for window i need to flip the buffer
        self.flip()

    def update(self, dt):
        interval = Player.PLAYER_SPEED * dt
        if key.A in self.keys:
            #self.cam.translate(int(-32 * Player.PLAYER_SPEED * dt), 0)
            self.player.move_player(-32 * interval, 0)

            self.cam.x = int(self.player.sprite.x + -GameWindow.WINWIDTH/2)
            self.cam.y = int(self.player.sprite.y + -GameWindow.WINHEIGHT/2)
        if key.D in self.keys:
            #self.cam.translate(int(32 * interval), 0)
            self.player.move_player(32 * interval, 0)

            self.cam.x = int(self.player.sprite.x + -GameWindow.WINWIDTH/2)
            self.cam.y = int(self.player.sprite.y + -GameWindow.WINHEIGHT/2)
        if key.W in self.keys:
           # self.cam.translate(0, int(32 * interval * dt))
            self.player.move_player(0, 32 * interval)

            self.cam.x = int(self.player.sprite.x + -GameWindow.WINWIDTH/2)
            self.cam.y = int(self.player.sprite.y + -GameWindow.WINHEIGHT/2)
        if key.S in self.keys:
            #self.cam.translate(0, int(-32 * interval))
            self.player.move_player(0, -32 * interval)

            self.cam.x = int(self.player.sprite.x + -GameWindow.WINWIDTH/2)
            self.cam.y = int(self.player.sprite.y + -GameWindow.WINHEIGHT/2)
