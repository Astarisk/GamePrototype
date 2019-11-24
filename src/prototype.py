import pygame, sys
from pygame.locals import *
from spritesheet import SpriteSheet
from camera import FollowCam
from map import Map
from player import Player

WINWIDTH = 800
WINHEIGHT = 600

HALF_WINWIDTH = WINWIDTH / 2
HALF_WINHEIGHT = WINHEIGHT / 2

#TILEWIDTH = 32
#TILEHEIGHT = 32

MAPWIDTH = 50
MAPHEIGHT = 50

CAM_SPEED = 5


map_tiles = pygame.sprite.Group()

BRIGHTBLUE = (0, 170, 255)
BGCOLOR = BRIGHTBLUE


def main():
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT), DOUBLEBUF)
    print(pygame.display.Info())
    sheet = SpriteSheet("res/Woodland_ground.png")

    #TILE_DEFAULT = sheet.image_at((0, 0, TILEWIDTH, TILEHEIGHT))
    #TILE_DEFAULT_TWO = sheet.image_at((0, 32 * 6, TILEWIDTH, TILEHEIGHT))
    TILE_HIGHLIGHT = pygame.image.load("res/highlight.png").convert_alpha()

    mouse_down = None
    mouse_tile = None
    cam = FollowCam()

    font = pygame.font.Font(None, 30)
    clock = pygame.time.Clock()

    #mapSurf = drawMap((TILE_DEFAULT, TILE_DEFAULT_TWO))

    map = Map()
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                # mouse_down = event.pos
                # mouse_tile = (mouse_down[0] - cam.x, mouse_down[1] - cam.y)
                # mouse_tile = (int(mouse_tile[0] / TILEWIDTH), int(mouse_tile[1] / TILEHEIGHT))
                print(mouse_down)

            if event.type == KEYDOWN:
                if event.key == K_a:
                    # TODO: We can make Tile a sprite and then use the update method to math out the camera translation.
                    #  That way we can just call map update in the camera
                    map.move_tile((32, 0))
                    cam.translate((32, 0))
                if event.key == K_d:
                    map.move_tile((-32,0))
                    cam.translate((-32, 0))
                if event.key == K_w:
                    map.move_tile((0, 32))
                    cam.translate((0, 32))
                if event.key == K_s:
                    map.move_tile((0, -32))
                    cam.translate((0, -32))

        keys = pygame.key.get_pressed()

        # if keys[K_a]:
        #     cam.translate((32, 0))
        # if keys[K_d]:
        #     cam.translate((-32, 0))
        # if keys[K_w]:
        #     cam.translate((0, 32))
        # if keys[K_s]:
        #     cam.translate((0, -32))

        # TODO: read up more on update(rects) vs flip
        pygame.display.update()
        DISPLAYSURF.fill(BGCOLOR)

        #mapSurf = drawMap((TILE_DEFAULT, TILE_DEFAULT_TWO))
        #mapRect = mapSurf.get_rect().move(cam.x, cam.y)
        #mapRect = mapRect.move(cam.x, cam.y)

        #DISPLAYSURF.blit(mapSurf, mapRect)
        #mapSurf.update()
        map.draw(DISPLAYSURF)

        # if mouse_down:
        #     highlightSurf = TILE_HIGHLIGHT
        #     higlightRect = highlightSurf.get_rect()
        #
        #     drawC = (mouse_tile[0] * TILEWIDTH, mouse_tile[1] * TILEHEIGHT)
        #     drawRect = pygame.Rect(drawC[0], drawC[1], TILEWIDTH, TILEHEIGHT).move(cam.x, cam.y)
        #     #drawRect = drawRect.move(cam.x, cam.y)
        #
        #     DISPLAYSURF.blit(highlightSurf, drawRect)

        fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
        #print(clock.get_fps())
        DISPLAYSURF.blit(fps, (50, 50))

        clock.tick()


def map2screen(coord, cam):
    return coord[0] * TILEWIDTH + HALF_WINWIDTH, coord[1] * TILEHEIGHT + HALF_WINHEIGHT


def screen2map(coord, cam):
    tmp = (coord[0] - cam.x, coord[1] - cam.y)
    tmp = (int(tmp[0] / TILEWIDTH), int(tmp[1] / TILEHEIGHT))


def drawMap(tile_default):
    mapSurf = pygame.Surface((TILEWIDTH * MAPWIDTH, TILEHEIGHT * MAPHEIGHT))
    tile_group = pygame.sprite.Group()

    tile_sprite = None

    for x in range(MAPWIDTH):
        for y in range(MAPHEIGHT):
            tile_rect = pygame.Rect(x * TILEWIDTH, y * (TILEHEIGHT), TILEWIDTH, TILEHEIGHT)

            from random import randint, seed
            seed(x * y)
            value = randint(0, 1)
            tile_sprite = pygame.sprite.Sprite()
            tile_sprite.image = tile_default[value]
            tile_sprite.rect = tile_rect
            tile_group.add(tile_sprite)
            #mapSurf.blit(tile_default[value], tile_rect)

    return tile_group


def get_image(posx, posy, width, height, sprite_sheet):
    image = pygame.Surface([width, height])
    image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
    #image.set_colorkey(c.BLACK)

    return image


def loadChunk():
    pass


if __name__ == '__main__':
    main()
