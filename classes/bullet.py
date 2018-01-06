u"""V tej datoteki se nahaja razred Bullet."""


import consts
from classes import moving_object
from utility.texture_loader import textures


class Bullet(moving_object.MovingObject):
    u"""Metek je premikajoči se objekt, ki ne spreminja svoje orientacije."""

    def __init__(self, player):
        u"""Inicializacijska metoda za classes.bullet.Bullet."""

        # izracuna pozicijo, kjer naj se pojavi metek.
        # pojavil naj bi se na sredini igralca
        xpos = player.x+player.sx*0.45
        ypos = player.y+player.sy*0.45

        super(Bullet, self).__init__((xpos, ypos), consts.BULLET_SIZE, textures["bullet"])

        self.velocity = consts.BULLET_SPEED

        # 180 dodatnih stopinj je potrebnih, ker se sicer metek premika v napacno smer
        self.rotation = player.rotation + 180
