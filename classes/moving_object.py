import pygame
from pygame.transform import rotate
import consts
from classes import static_object
import math


class MovingObject(static_object.StaticObject):
    
    def __init__(self, pos, size, image):
        super(MovingObject, self).__init__(pos, size)
        self.dx = self.dy = 0
        self.rotation = 0
        self.image = image
        self.velocity = 0

    def move(self):
        """Calculate self.dx, self.dy and move self self.dx units right and self.dy units down
        Return True if object is at edge"""
        self.dx = math.sin(math.radians(self.rotation)) * self.velocity
        self.dy = math.cos(math.radians(self.rotation)) * self.velocity

        self.x += self.dx
        self.y += self.dy

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

    def rotate(self, degrees):
        """Rotate self by degrees counterclockwise"""
        self.rotation += degrees

    def show(self, w: pygame.display):
        """Blit self.image to screen"""
        rotated_image = rotate(self.image, self.rotation)
        self.sx, self.sy = rotated_image.get_size()
        w.blit(rotated_image, (self.x, self.y))

    def set_rotation(self, rotation):
        """Set self.rotation to rotation. Should only be used for debug purposes!"""
        self.rotation = rotation


