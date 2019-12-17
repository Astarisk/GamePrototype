class Coord:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        print("n")
        print(other)
        self.x = self.x + other[0]
        print("x")
        print(self.x)
        self.y = self.y + other[1]
