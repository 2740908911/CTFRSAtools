import gmpy2
from RSAtools import factorN

def solves(n,dp,dq):
    try:
        (p,q) = factorN.solves(n)
        dd = gmpy2.gcd(p-1, q-1)
        d=(dp-dq)//dd * gmpy2.invert((q-1)//dd, (p-1)//dd) * (q-1) +dq
        return d
    except:
        print("failed in ndpdq")
        exit()
        
def printf(n,dp,dq):
    d = solves(n,dp,dq)
    print("=" * 99)
    print("int_d：" + str(d))
    print("=" * 99)