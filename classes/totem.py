u"""Tu je definiran razred Totem."""


import consts
from classes import static_object
from utility.randomgen import rand_pos
from utility.texture_loader import textures


class Totem(static_object.StaticObject):
    u"""Totem je nepremakljiv objekt, ki se na začetku igre pojavi na sredini in ki ga mora igralec zaščititi."""

    def __init__(self):
        u"""Inicializacijska metoda za classes.totem.Totem"""
        super(Totem, self).__init__(rand_pos(*consts.TOTEM_SIZE), consts.TOTEM_SIZE)
        self.image = textures["totem"]

    def show(self, w):
        u"""Pokazi objekt na zaslonu"""
        w.blit(self.image, (self.x, self.y))
