from RSAtools.RSAhacker import RSAwienerHacker
import gmpy2

def solves(n,e):
    try:
        d = RSAwienerHacker.hack_RSA(e,n)
        return d
    except:
        print("failed in ne_wiener")
        exit()

def printf(n,e):
    print("=" * 99)
    d = solves(n,e)
    print("维纳wiener攻击")
    print("int_d：" + str(d))
    print("=" * 99)