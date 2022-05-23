import os
import requests
import gmpy2

def yafu(n):
    print("=" * 99)
    print("yafu factor decomposed")
    os.chdir("RSAtools/yafu")
    cmd = f'.\yafu-x64.exe "factor({n})"'
    resall = os.popen(cmd).read()
    print(resall.replace("\n\n","\n"))
    foundpq = resall.split("***factors found***")[1].split("ans")[0].replace(" ","")
    resp = foundpq.split("\n")[2].split("=")[1]
    resq = foundpq.split("\n")[3].split("=")[1]
    if foundpq.split("\n")[4]:
        print("暂时不支持多个分解项自动解，可分解成功pqr后手动加入data.txt运行")
        exit()
    p = gmpy2.mpz(resp)
    q = gmpy2.mpz(resq)
    return p,q

def factordb(n):
    n = str(n)
    print("=" * 99)
    print("factordb.com factor decomposed\n")
    print("Connecting to the site ......")
    url= f"http://factordb.com/index.php?query={n}"
    res=requests.get(url)
    res = res.text
    foundpq = res.split("show")[2].split("moreinfo")[0].split("#000000")
    resp = foundpq[1].split('">')[1].split("<")[0]
    resq = foundpq[2].split('">')[1].split("<")[0]
    try:
        foundpq[3].split('">')[1].split("<")[0]
    except:
        p = gmpy2.mpz(resp)
        q = gmpy2.mpz(resq)
        print("P = " + str(p))
        print("Q = " + str(q))
        return p,q

def solves(n):
    try:
        (p, q) = factordb(n)
        return(p, q)
    except:
        try:
            print("factordb：Online decomposition failed")
            (p, q) = yafu(n)
            return(p, q)
        except:
            print("yafu：decomposition failed")
            print("decomposition failed! check N again!")
            print("=" * 99)
            exit()
            
    

def printf(n):
    (p, q) = solves(n)
    if p == q:
        print("N is prime! check N again!")
        exit()
    print("=" * 99)
    print("int_p：" + str(p))
    print("int_q：" + str(q))
    print("=" * 99)

    
