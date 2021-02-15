from nand import blnand
from blnot import blnot

def bland(a, b):
    return blnot(blnand(a, b))
