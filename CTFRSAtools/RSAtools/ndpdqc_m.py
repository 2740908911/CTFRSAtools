from RSAtools import ndpdq_d
import gmpy2
import binascii
import libnum

def solves(n,dp,dq,c):
	try:
		d = ndpdq_d.solves(n,dp,dq)
		m = gmpy2.powmod(c, d, n)
		return m
	except:
		print("failed in ndpdqc")
		exit()

def printf(n,dp,dq,c):
	m = solves(n,dp,dq,c)
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

