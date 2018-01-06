u"""Tu je definicija razreda StaticObject"""


import pygame

from utility import colors


class StaticObject(object):
    u"""Nepremakljiv objekt je vsak objekt, ki lahko miruje"""

    def __init__(self, pos, size):
        u"""Incializacijska metoda za classes.static_object.StaticObject"""
        self.x, self.y = pos
        self.sx, self.sy = size

    def is_hit_by(self, other):
        """Vrni True, ce se objekt dotika other"""
        if self.x < other.x+other.sx and self.x+self.sx > other.x:
            if self.y < other.y+other.sy and self.y+self.sy > other.y:
                return True
        return False

    def show(self, w: pygame.display):
        u"""Nariši crn pravokotnik na self.x, self.y"""
        w.fill(colors.BLACK, (self.x, self.y, self.sx, self.sy))

    @property
    def get_pos(self):
        """Vrni tuple (self.x, self.y)."""
        return self.x, self.y
