import blnot.py
import bland.py
import blor.py
import blxor.py

def bldmux (x, sel):
    b = bland(x, sel)
    a = bland(blxor(x, sel), blor(x, blnot(sel)))
    return (a, b)
