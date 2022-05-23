import gmpy2

def solves(p,q,dp,dq):
    try:
        dd = gmpy2.gcd(p-1, q-1)
        d=(dp-dq)//dd * gmpy2.invert((q-1)//dd, (p-1)//dd) * (q-1) +dq
        return d
    except:
        print("failed in pqdpdq")
        exit()
        
def printf(p,q,dp,dq):
    d = solves(p,q,dp,dq)
    print("=" * 99)
    print("int_d：" + str(d))
    print("=" * 99)