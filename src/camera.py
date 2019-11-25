from pyglet.gl import *


class FollowCam:
    def __init__(self, x=0, y=0, zoom=1.0):
        self.x = x
        self.y = y
        self.zoom = zoom

    def translate(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

    def worldProjection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        #widthRatio = self.win.width / self.win.height
        widthRatio = 800 / 600
        gluOrtho2D(0 + self.x, 800 + self.x, 0 + self.y, 600 + self.y)

    # def hudProjection(self):
    #     glMatrixMode(GL_PROJECTION)
    #     glLoadIdentity()
    #     gluOrtho2D(0, self.win.width, 0, self.win.height)