u"""Tu se nahaja razred Player"""


import math

from classes import moving_object
from consts import PLAYER_SIZE as SIZE
from consts import PLAYER_START_POS as START_POS
from utility.texture_loader import textures


class Player(moving_object.MovingObject):
    u"""Igralec je objekt, ki ga upravlja uporabnik."""

    def __init__(self):
        """Inicializacijska metoda za classes.player.Player"""

        # Na začetku vsake igre je igralec na sredini zaslona
        super(Player, self).__init__(START_POS, SIZE, textures["player"])

    def rotate(self, mouse_pos):
        u"""Nastavi self.rotation, da objekt gleda proti miški"""
        try:
            # Izracunaj nasprotno in prilezno stranico
            opp = -self.x - self.sx/2 + mouse_pos[0]
            adj = mouse_pos[1] - self.y + self.sy/2

            # Izracunaj kot, pod katerim naj bo objekt obrnjen
            # (+180 je tu, ker bi bil sicer objekt obrnjen v nasprotno smer)
            rad = math.atan2(opp, adj)
            self.rotation = math.degrees(rad)+180

        except ZeroDivisionError:
            # Vcasih bo math.atan2 vrgel ZeroDivisionError. V tem primeru se rotacija objekta to sliko ne spremeni
            return
