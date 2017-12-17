from math import tan, radians
import consts
from classes import moving_object
from utility.texture_loader import textures


class Bullet(moving_object.MovingObject):

    def __init__(self, player):
        self.rotation = player.rotation + 180
        xpos = player.x+player.sx/2
        ypos = player.y+player.sy/2
        super(Bullet, self).__init__((xpos, ypos), consts.BULLET_SIZE, textures["bullet"])
        self.velocity = consts.BULLET_SPEED
        self.rotation = player.rotation + 180
