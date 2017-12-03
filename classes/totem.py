import consts
from classes import static_object
from utility.randomgen import rand_pos
from utility.texture_loader import textures
from pygame.transform import rotate


class Totem(static_object.StaticObject):

    def __init__(self):
        super(Totem, self).__init__(rand_pos(), consts.TOTEM_SIZE)
        self.image = textures["totem"]

    def show(self, w):
        w.blit(self.image, (self.x, self.y))
