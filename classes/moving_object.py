u"""Tu se nahaja definicija razreda MovingObject, ki je podlaga za mnogo drugih razredov"""


import pygame
from pygame.transform import rotate
import consts
from classes import static_object
import math


class MovingObject(static_object.StaticObject):
    u"""Premikajoči objekt je vsak objekt, ki se lahko obrača in spreminja svojo pozicijo na podlagi"""
    
    def __init__(self, pos, size, image):
        u"""Inicializacijska metoda za classes.moving_object.MovingObject"""

        super(MovingObject, self).__init__(pos, size)

        # Nastavi spremenljivki dx, in dy, ki indicirata, za koliko pikslov se objekt premakne vsako sliko
        self.dx = self.dy = 0

        # Kot, pod katerim je obrnjen objekt, izrazen v stopinjah
        self.rotation = 0

        # Vsak premikajoči se objekt ima svojo sliko
        self.image = image

        # Velikost vektorja hitrosti za objekt
        self.velocity = 0

    def move(self):
        u"""Izračunaj self.dx, self.dy in premakni objekt. Vrni True če je objekt na robu."""

        # Razstavi vektor hitrosti
        self.dx = math.sin(math.radians(self.rotation)) * self.velocity
        self.dy = math.cos(math.radians(self.rotation)) * self.velocity

        # Premakni objekt
        self.x += self.dx
        self.y += self.dy

        # Ne dovoli, da gre objekt ven iz okna
        if self.x < 0:
            self.x = 0
            return True

        if self.x+self.sx > consts.WWIDTH:
            self.x = consts.WWIDTH-self.sx
            return True

        if self.y < 0:
            self.y = 0
            return True

        if self.y+self.sy > consts.WHEIGHT:
            self.y = consts.WHEIGHT-self.sy
            return True

    def rotate(self, degrees: int):
        """Obrni se za degrees stopinj v levo"""
        self.rotation += degrees

    def show(self, w: pygame.display):
        """Pokazi se na w"""

        # Obrni svojo sliko
        rotated_image = rotate(self.image, self.rotation)

        # Nastavi svojo velikost na velikost nove slike, da bo zaznavanje dotikov bolj natancno
        self.sx, self.sy = rotated_image.get_size()

        w.blit(rotated_image, (self.x, self.y))
