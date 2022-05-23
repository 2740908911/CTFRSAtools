import gmpy2
import binascii
import libnum

def solves(e,n,c):
	try:
		k = 0
		while 1:
			res = gmpy2.iroot(c+k*n,e)  #c+k*n 开3次方根 能开3次方即可
			if(res[1] == True):
				return res[0]
			k=k+1
	except:
		print("failed in lowenc")
		exit()

def printf(e,n,c):
	m = solves(e,n,c)
	print("=" * 99)
	print("小指数攻击")
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
