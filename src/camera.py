class FollowCam:
    def __init__(self):
        self.x = 0
        self.y = 0

    def translate(self, coord):
        self.x = self.x + coord[0]
        self.y = self.y + coord[1]
