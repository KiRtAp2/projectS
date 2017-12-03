import random
import consts


def rand_pos():
    return random.randrange(0, consts.WWIDTH), random.randrange(0, consts.WHEIGHT)