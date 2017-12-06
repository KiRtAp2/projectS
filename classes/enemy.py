import consts
from classes import moving_object
from utility.randomgen import rand_pos_nocenter
from consts import ENEMY_SIZE as SIZE
from utility.texture_loader import textures
import math


class Enemy(moving_object.MovingObject):

    def __init__(self, totem_pos, curr_score):
        super(Enemy, self).__init__(rand_pos_nocenter(SIZE, totem_pos, consts.TOTEM_SIZE[0]), SIZE, textures["enemy"])
        self.velocity = -int(consts.START_ENEMY_VELOCITY+curr_score*0.15)
        try:
            opp = -self.x - self.sx/2 + totem_pos[0]
            adj = totem_pos[1] - self.y + self.sy/2
            rad = math.atan(opp/adj)
            self.rotation = math.degrees(rad)
            if adj > 0:
                self.rotation += 180
        except ZeroDivisionError:
            self.rotation = 0
