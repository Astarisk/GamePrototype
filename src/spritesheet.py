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
        print(len(sprites))


    # def image_at(self, rect, colorkey=None):
    #     rec = pygame.Rect(rect)
    #     image = pygame.Surface(rec.size).convert()
    #     image.blit(self.sheet, (0, 0), rec)
    #
    #     return image
    #
    # def images_at(self, rects, colorkey = None):
    #     return [self.image_at(rect, colorkey) for rect in rects]

    # def strip_sheet(self, rect, image_count, colorkey=None):
    #     tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
    #             for x in range(image_count)]
    #     return self.images_at(tups, colorkey)
    #
