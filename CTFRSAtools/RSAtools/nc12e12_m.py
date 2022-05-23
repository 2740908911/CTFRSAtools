import gmpy2
import libnum
import binascii

def solves(n,c1,c2,e1,e2):
	try:
		s = gmpy2.gcdext(e1, e2)
		s1 = s[1]
		s2 = -s[2]
		c2 = gmpy2.invert(c2, n)
		m = (pow(c1,s1,n) * pow(c2,s2,n)) % n
		return m
	except:
		print("failed in nc12e12")
		exit()

def printf(n,c1,c2,e1,e2):
	m = solves(n,c1,c2,e1,e2)
	print("=" * 99)
	print("共模攻击")
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
