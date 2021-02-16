from nand import blnand
from blnot import blnot

def blor(a, b):
    a = blnot(a)
    b = blnot(b)
    return blnand(a, b)