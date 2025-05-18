from settings.globals import HEIGHT, WIDTH
import math

def xperc(x, perc):
    """
        Returns a percentage of original length x.
    """
    return math.ceil(x * (perc / 100))


def hperc(perc=100, h=HEIGHT):
    return xperc(h, perc)


def wperc(perc=100, w=WIDTH):
    return xperc(w, perc)


