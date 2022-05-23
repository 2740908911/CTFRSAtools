import gmpy2
from RSAtools import factorN

def solves(e,n):
    try:
        (p,q) = factorN.solves(n)
        phi = (p-1)*(q-1)
        d = gmpy2.invert(e,phi)
        return d
    except:
        print("failed in en")
        exit()

def printf(e,n):
    d = solves(e,n)
    print("=" * 99)
    print("int_d：" + str(d))
    print("=" * 99)
