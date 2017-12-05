from math import tan, radians
import consts
from classes import moving_object
from utility.texture_loader import textures


def get_position(x, y, rot, sx, sy):
    """Return position to spawn bullet"""
    xpos = x
    ypos = y

    if rot < 0:
        rot += 360
    if rot > 360:
        rot %= 360

    # y
    opp = tan(radians(rot)) / sy
    if rot < 45:
        pass
    elif rot < 90:
        ypos += (sy / 2 - opp)
    elif rot < 135:
        ypos += sy / 2 + opp
    elif rot < 225:
        ypos += sy
    elif rot < 270:
        ypos += sy/2 - opp

    # x
    if rot < 45:
        xpos += sx/2 - opp
    elif rot < 135:
        pass
    elif rot < 180:
        xpos += sx/2 - opp
    elif rot < 225:
        xpos += sx/2 + opp
    elif rot < 315:
        xpos += sx
    else:
        xpos += sx/2 + opp

    return xpos, ypos


class Bullet(moving_object.MovingObject):

    def __init__(self, player):
        self.rotation = player.rotation + 180
        xpos, ypos = get_position(player.x, player.y, self.rotation-180, *consts.PLAYER_SIZE)
        super(Bullet, self).__init__((xpos, ypos), consts.BULLET_SIZE, textures["bullet"])
        self.velocity = consts.BULLET_SPEED
        self.rotation = player.rotation + 180
