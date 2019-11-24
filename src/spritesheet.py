import pygame


class SpriteSheet:

    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error:
            print("Unable to load: " + filename)

    def image_at(self, rect, colorkey=None):
        rec = pygame.Rect(rect)
        image = pygame.Surface(rec.size).convert()
        image.blit(self.sheet, (0, 0), rec)

        return image

    def images_at(self, rects, colorkey = None):
        return [self.image_at(rect, colorkey) for rect in rects]

    def strip_sheet(self, rect, image_count, colorkey=None):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

