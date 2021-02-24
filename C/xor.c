# import nand.c
# import and.c
# import or.c

int blxor (int a, int b)
{
  nandout = blnand(a, b);
  anda = bland(a, nandout);
  andb = bland(b, nandout);
  return or (anda, andb);
}
