from RSAtools import ne_d_wiener
import gmpy2
import binascii
import libnum

def solves(n,e,c):
    try:
        d = ne_d_wiener.solves(n,e)
        m = gmpy2.powmod(c,d,n)
        return m
    except:
        print("failed in nec_wiener")
        exit()

def printf(n,e,c):
    print("=" * 99)
    m = solves(n,e,c)
    print("维纳wiener攻击")
    try:
        print("int：" + str(m))
        print("hex：" + str(hex(m)))
    except:
        print("int：" + str(m))
    try:
        print("hex to ascii：" + str(binascii.unhexlify(hex(m)[2:])))
    except:
        try:
            print("libnum(n2s)：" + str(libnum.n2s(hex(m))))
        except:
            print("just hex or int ")
    print("=" * 99)
