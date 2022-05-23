import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from RSAtools import publickey
from RSAtools import factorN
from RSAtools import epq_d
from numpy import long 
import libnum
import binascii

def solves():
	try:
		(n,e) = publickey.solves()
		(p,q) = factorN.solves(n)
		print(p)
		print(q)
		d = epq_d.solves(e,p,q)
		n = long(n)
		e = long(e)
		d = long(d)
		p = long(p)
		q = long(q)
		key = rsa.PrivateKey(n,e,d,p,q)
		filepath1 = "flag.enc"
		filepath2 = "../../flag.enc"
		try:
			try:
				with open(filepath1,'rb') as f:    #文件路径
					f = f.read()
					m = rsa.decrypt(f,key)
				return m
			except:
				pkey = RSA.construct((n,e,d,p,q))
				r = PKCS1_OAEP.new(pkey)
				m = r.decrypt(open(filepath1,'rb').read())
				return m
		except:
			try:
				with open(filepath2,'rb') as f:    #文件路径
					f = f.read()
					m = rsa.decrypt(f,key)
				return m
			except:
				pkey = RSA.construct((n,e,d,p,q))
				r = PKCS1_OAEP.new(pkey)
				m = r.decrypt(open(filepath2,'rb').read())
				return m
	except:
		print("failed in pubenc")
		exit()

def printf():
	m = solves()
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