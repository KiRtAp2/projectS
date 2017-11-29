from classes import moving_object
from consts import PLAYER_START_POS as START_POS
from consts import PLAYER_SIZE as SIZE
from texture_loader import textures


class Player(moving_object.MovingObject):

    def __init__(self):
        super(Player, self).__init__(START_POS, SIZE, textures["player"])
