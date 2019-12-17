class Coord:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x = self.x + other[0]
        self.y = self.y + other[1]
