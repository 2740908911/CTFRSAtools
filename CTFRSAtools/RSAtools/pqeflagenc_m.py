import rsa
from RSAtools import epq_d
from numpy import long 
import libnum
import binascii

def solves(p,q,e):
	try:
		d = epq_d.solves(e,p,q)
		n = long(n)
		e = long(e)
		d = long(d)
		p = long(p)
		q = long(q)
		key = rsa.PrivateKey(n,e,d,p,q)
		with open("flag.enc",'rb') as f:    #文件路径
			f = f.read()
			m = rsa.decrypt(f,key)
		return m
	except:
		print("failed in pqeflagenc")
		exit()

def printf(p,q,e):
	m = solves(p,q,e)
	print("=" * 99)
	try:
		print("int：" + str(m))
		print("hex：" + str(hex(m)))
	except:
		pass

	try:
		print("hex to ascii：" + str(binascii.unhexlify(hex(m)[2:])))
	except:
		try:
			print("libnum(n2s)：" + str(libnum.n2s(hex(m))))
		except:
			print("just int or hex ")
	print("=" * 99)