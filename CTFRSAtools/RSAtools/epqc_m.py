import gmpy2
import binascii
import libnum
from RSAtools import epq_d

def solves(e,p,q,c):
	try:
		d = epq_d.solves(e,p,q)
		n = p*q
		m = gmpy2.powmod(c,d,n)
		return m
	except:
		print("failed in epqc")
		exit()

def printf(e,p,q,c):
	m = solves(e,p,q,c)
	print("=" * 99)
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

