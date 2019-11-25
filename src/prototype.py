import pyglet


def main2():
    from gamewindow import GameWindow
    gw = GameWindow(vsync=False)
    gw.run()
    #pyglet.app.run()


if __name__ == '__main__':
    main2()
