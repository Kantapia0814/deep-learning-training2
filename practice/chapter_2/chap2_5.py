import chap2_3

def XOR(x1, x2):
    s1 = chap2_3.OR(x1, x2)
    s2 = chap2_3.NAND(x1, x2)
    y = chap2_3.AND(s1, s2)
    return y