from .nand import nand
from .not import not

def and(a, b):
    return not(nand(a, b))
