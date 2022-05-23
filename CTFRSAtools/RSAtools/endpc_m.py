import gmpy2
import binascii
import libnum

def solves(e,n,dp,c):
	try:
		for x in range(1, e):
			if(e*dp%x==1):
				p=(e*dp-1)//x+1
				if(n%p!=0):
					continue
				q=n//p
				phi=(p-1)*(q-1)
				d=gmpy2.invert(e, phi)
				m=gmpy2.powmod(c, d, n)
				if(len(hex(m)[2:])%2==1):
					continue
		return m
	except:
		print("failed in endpc")
		exit()

def printf(e,n,dp,c):
	m = solves(e,n,dp,c)
	print("=" * 99)
	print("dp泄露攻击")
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