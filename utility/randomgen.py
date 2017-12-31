import random
import consts


def _check_center_ok(centerpos, centersize, pos):
    """Checks whether pos is far away enough from centerpos"""
    x, y = False, False
    if pos[0]-centersize > centerpos[0] or pos[0]+centersize < centerpos[0]: x = True
    if pos[1]-centersize > centerpos[1] or pos[0]+centersize < centerpos[1]: y = True
    return (x and y)


def rand_pos(sx=0, sy=0):
    """Return tuple of random position but not so high that object goes over bounds (size provided by sx and sy)"""
    return random.randrange(0, consts.WWIDTH-sx), random.randrange(0, consts.WHEIGHT-sy)


def rand_pos_nocenter(size, centerpos, centersize):
    """Return random position but not centersize out of centerpos"""
    pos = rand_pos()
    while not _check_center_ok(centerpos, centersize, pos):
        pos = rand_pos()
    return pos
