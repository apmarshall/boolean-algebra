from nand import blnand
from bland import bland
from blor import blor

def blxor(a, b):
    nandout = blnand(a, b)
    return blor(bland(a, nandout), bland(b, nandout))
