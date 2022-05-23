from Crypto.PublicKey import RSA
import gmpy2

def solves():
    try:
        public = RSA.importKey(open("pub.key").read())
        n = gmpy2.mpz(public.n)
        e = gmpy2.mpz(public.e)
        return n,e
    except:
        print("failed in publickey")
        exit()

def printf():
    (n,e) = solves()
    print("=" * 99)
    print("public key")
    print("int_n：" + str(n))
    print("int_e：" + str(e))
    print("=" * 99)
