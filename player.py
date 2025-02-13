
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init(x, y, PLAYER_RADIUS):
            self.rotation = 0
