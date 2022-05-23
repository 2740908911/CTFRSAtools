from RSAtools import pqdpdq_d
import gmpy2
import binascii
import libnum

def solves(p,q,dp,dq,c):
	try:
		n = p*q
		d = pqdpdq_d.solves(p,q,dp,dq)
		m = gmpy2.powmod(c, d, n)
		return m
	except:
		print("failed in pqdpdqc")
		exit()

def printf(p,q,dp,dq,c):
	m = solves(p,q,dp,dq,c)
	print("=" * 99)
	print("dp/dq泄露攻击")
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

