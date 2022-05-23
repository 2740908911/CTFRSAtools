def solves(n,x):
    return n/x

def printf(n,x):
    nx= solves(n,x)
    print("=" * 99)
    print("p or q：" + str(nx))
    print("=" * 99)