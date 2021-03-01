from blor import blor
from blxor import blxor

def blmux (a, b, sel):
    ora = blor(a, sel)
    orb = blor(b, sel)
    xorab = blxor(ora, orb)
    return blxor(xorab, sel)
