import pygame
import colors


class StaticObject(object):

    def __init__(self, pos, size):
        self.x, self.y = pos
        self.sx, self.sy = size

    def is_hit_by(self, other):
        """Return whether self is intercepting other"""
        if self.x < other.x+other.sx and self.x+self.sx > other.x:
            if self.y < other.y+other.sy and self.y+self.sy > other.y:
                return True
        return False

    def show(self, w: pygame.display):
        """Draw a black box at self.x, self.y"""
        w.fill(colors.BLACK, (self.x, self.y, self.sx, self.sy))

    def get_pos(self):
        """Return tuple (self.x, self.y)"""
        return self.x, self.y
