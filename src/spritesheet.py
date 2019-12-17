#import pygame
import pyglet

class SpriteSheet:

    def __init__(self, filename):
        # TODO: error catch loading
        try:
            self.sheet = pyglet.resource.image(filename)
        except pyglet.resource.ResourceNotFoundException:
            print("Unable to load: " + filename)
        self.images = []

    def strip_sheet(self, row, column, width, height):
        sprites = pyglet.image.ImageGrid(self.sheet, row, column, width, height)
        for s in sprites:
            self.images.append(s)
