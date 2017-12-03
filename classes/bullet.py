import consts
from classes import moving_object
from utility.texture_loader import textures


class Bullet(moving_object.MovingObject):

    def __init__(self, player):

        # calculates how much to the right the bullet should spawn
        if player.rotation > 180:
            r = player.rotation-90
        else:
            r = player.rotation+90
        if r > 360:
            r -= 360
        if r > 135:
            k = 1
        elif r < 45:
            k = 0
        else:
            k = (r-45)/90
        k = 1 - k
        xadd = k*player.sx
        super(Bullet, self).__init__((player.x+xadd, player.y), consts.BULLET_SIZE, textures["bullet"])
        self.velocity = consts.BULLET_SPEED
        self.rotation = player.rotation+180
