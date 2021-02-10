from .nand import nand

def not(in):
    return nand(in, in)
