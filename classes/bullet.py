import consts
from classes import moving_object
from texture_loader import textures


class Bullet(moving_object.MovingObject):

    def __init__(self, player_pos):
        super(Bullet, self).__init__(player_pos, consts.BULLET_SIZE, textures["bullet"])
        self.velocity = consts.BULLET_SPEED
