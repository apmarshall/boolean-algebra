# import nand.c
# import not.c

int blor (int a, int b) 
{
    a = blnot(a);
    b = blnot(b);
    return blnand(a, b);
}