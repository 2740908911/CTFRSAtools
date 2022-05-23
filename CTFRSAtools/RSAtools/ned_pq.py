import gmpy2

def solves(n,e,d):
    try:
        g = 2
        while True:
            k = e * d - 1
            while not k & 1:
                k //= 2
                p = int(gmpy2.gcd(pow(g, k, n) - 1, n)) % n
                if p > 1:
                    return (p, n // p)
            g = int(gmpy2.next_prime(g))
    except:
        print("failed in ned")
        exit()

def printf(n,e,d):
    (p, q) = solves(n,e,d)
    print("=" * 99)
    print("int_p：" + str(p))
    print("int_q：" + str(q))
    print("=" * 99)
