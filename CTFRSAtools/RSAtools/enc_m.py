import gmpy2
import binascii
import libnum
from RSAtools import en_d

def solves(e,n,c):
	try:
		d = en_d.solves(e,n)
		m = gmpy2.powmod(c,d,n)
		return m
	except:
		print("failed in enc")
		exit()

def printf(e,n,c):
	m = solves(e,n,c)
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

