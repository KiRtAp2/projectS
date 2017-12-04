import random
import consts


def rand_pos(sx=0, sy=0):
    """Return tuple of random position but not so high that object goes over bounds (size provided by sx and sy)"""
    return random.randrange(0, consts.WWIDTH-sx), random.randrange(0, consts.WHEIGHT-sy)
