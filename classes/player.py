import math

from classes import moving_object
from consts import PLAYER_SIZE as SIZE
from consts import PLAYER_START_POS as START_POS
from utility.texture_loader import textures


class Player(moving_object.MovingObject):

    def __init__(self):
        super(Player, self).__init__(START_POS, SIZE, textures["player"])

    def rotate(self, mouse_pos):
        """Set self.rotation so self looks at mouse_pos"""
        try:
            opp = -self.x - self.sx/2 + mouse_pos[0]
            adj = mouse_pos[1] - self.y + self.sy/2
            rad = math.atan(opp/adj)
            self.rotation = math.degrees(rad)
            if adj > 0:
                self.rotation += 180
        except ZeroDivisionError:
            return
