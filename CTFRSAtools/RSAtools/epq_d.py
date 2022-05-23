import gmpy2

def solves(e,p,q):
    try:
        phi = (p-1)*(q-1)
        d = gmpy2.invert(e,phi)
        return d
    except:
        print("failed in epq")
        exit()

def printf(e,p,q):
    d = solves(e,p,q)
    print("=" * 99)
    print("int_d：" + str(d))
    print("=" * 99)
