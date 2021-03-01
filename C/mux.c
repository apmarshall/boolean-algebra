# import or.c
# import xor.c

int blmux (int a, int b, int sel) {
    ora = blor(a, sel)
    orb = blor(b, sel)
    xorab = blxor(ora, orb)
    return blxor(xorab, sel)
}