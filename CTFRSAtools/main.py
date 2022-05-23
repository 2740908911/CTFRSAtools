import random
import gmpy2
from banner import banners
import RSAjudge

def showbanner():
	banner=random.choice(banners)
	print(banner)
	
def showhelp():
    funlist = '''
-----About & Help-----
全自动ctfrsa解题
可秒ctf中大部分标准形式的RSA
分解N可能需要联网，如果失败会选用yafu分解
ps.需要sagemath辅助的题型目前未加入CTFRSAtools
帮助详见readme.md
    '''
    print(funlist)

def getdata():
    result = []
    RSAdata={}
    with open("data.txt","r") as f:
        for line in f.readlines():
            line=line.strip('\n').replace(" ","")#去掉列表中每一个元素的换行符
            result.append(line)

    print("-----Your input：-----")
    
    for linedata in result:
        if "n=" in linedata or "N=" in linedata:    #n
            n = gmpy2.mpz(linedata[2:])
            print("n = " + str(n))
            RSAdata['n'] = n

        if ("p=" in linedata and "dp" not in linedata) or ("P=" in linedata and "DP" not in linedata):    #p
            p = gmpy2.mpz(linedata[2:])
            print("p = " + str(p))
            RSAdata['p'] = p

        if ("q=" in linedata and "dq" not in linedata) or ("Q=" in linedata and "DQ" not in linedata):    #q
            q = gmpy2.mpz(linedata[2:])
            print("q = " + str(q))
            RSAdata['q'] = q

        if "e=" in linedata or "E=" in linedata:    #e
            e = gmpy2.mpz(linedata[2:])
            print("e = " + str(e))
            RSAdata['e'] = e

        if "c=" in linedata or "C=" in linedata:    #c
            c = gmpy2.mpz(linedata[2:])
            print("c = " + str(c))
            RSAdata['c'] = c

        if "m=" in linedata or "M=" in linedata:    #m
            m = gmpy2.mpz(linedata[2:])
            print("m = " + str(m))
            RSAdata['m'] = m

        if "d=" in linedata or "D=" in linedata:    #d
            d = gmpy2.mpz(linedata[2:])
            print("d = " + str(d))
            RSAdata['d'] = d

        if "dp=" in linedata or "DP=" in linedata:  #dp
            dp = gmpy2.mpz(linedata[3:])
            print("dp = " + str(dp))
            RSAdata['dp'] = dp

        if "dq=" in linedata or "DQ=" in linedata:  #dq
            dq = gmpy2.mpz(linedata[3:])
            print("dq = " + str(dq))
            RSAdata['dq'] = dq

        if "n1=" in linedata or "N1=" in linedata:  #n1
            n1 = gmpy2.mpz(linedata[3:])
            print("n1 = " + str(n1))
            RSAdata['n1'] = n1

        if "n2=" in linedata or "N2=" in linedata:  #n2
            n2 = gmpy2.mpz(linedata[3:])
            print("n2 = " + str(n2))
            RSAdata['n2'] = n2

        if "e1=" in linedata or "E1=" in linedata:  #e1
            e1 = gmpy2.mpz(linedata[3:])
            print("e1 = " + str(e1))
            RSAdata['e1'] = e1

        if "e2=" in linedata or "E2=" in linedata:  #e2
            e2 = gmpy2.mpz(linedata[3:])
            print("e2 = " + str(e2))
            RSAdata['e2'] = e2

        if "c1=" in linedata or "C1=" in linedata:  #c1
            c1 = gmpy2.mpz(linedata[3:])
            print("c1 = " + str(c1))
            RSAdata['c1'] = c1

        if "c2=" in linedata or "C2=" in linedata:  #c2
            c2 = gmpy2.mpz(linedata[3:])
            print("c2 = " + str(c2))
            RSAdata['c2'] = c2

        if "phi=" in linedata or "PHI=" in linedata:    #phi
            phi = gmpy2.mpz(linedata[4:])
            print("phi = " + str(phi))
            RSAdata['phi'] = phi

    return RSAdata


if __name__ == '__main__':
    showbanner()
    showhelp()
    RSAdata = getdata()
    RSAjudge.judge(RSAdata)

        
        
