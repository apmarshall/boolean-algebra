# import not.c
# import and.c
# import or.c
# import xor.c

int dmux (int in, int sel) {
  b = bland(in, sel);
  xora = blxor(in, sel);
  nsel = blnot(sel);
  ora = blor(xora, nsel);
  a = bland(xora, ora);
  return (a, b);
}
