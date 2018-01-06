u"""V tej datoteki se nahaja razred Enemy."""


import consts
from classes import moving_object
from utility.randomgen import rand_pos_nocenter
from consts import ENEMY_SIZE as SIZE
from utility.texture_loader import textures
import math


class Enemy(moving_object.MovingObject):
    u"""Nasprotnik je premikajoči se objekt, ki ne spremija svoje orientacije."""

    def __init__(self, totem_pos: tuple, curr_score: int):
        u"""Incializacijska metoda za classes.enemy.Enemy."""
        super(Enemy, self).__init__(rand_pos_nocenter(SIZE, totem_pos, consts.TOTEM_SIZE[0]), SIZE, textures["enemy"])

        # Hitrost nasprotnikov(in z njo tezavnost) naj bi se vecala s trenutnimi tockami.
        # Izracuna se po slednji formuli:
        self.velocity = int(min((consts.START_ENEMY_VELOCITY+curr_score*0.15), 7))
        # Smer premika je negativna, ker je izracunana orientacija obrnjena v nasprotno smer

        # Izracun orientacije s trignonmetrijo
        try:
            # Izracuna nasprotno stranico kota rotacije (X direkcija)
            opp = -self.x - self.sx/2 + totem_pos[0]

            # Izracuna prilezno stranico kota orientacije (Y direkcija)
            adj = totem_pos[1] - self.y + self.sy/2

            # Izracuna kot orientacije
            rad = math.atan2(opp, adj)
            self.rotation = math.degrees(rad)

        except ZeroDivisionError:
            # Zelo redko bo bil pri trigonometriji vrzen ZeroDivisionError, zato ga tu ujamemo
            self.rotation = 0
