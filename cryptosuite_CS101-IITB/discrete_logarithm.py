def discrete_logarithm(a,b,n):
	m = int(math.ceil(math.sqrt(n)))
	dict = {}
	for j in range(m):
		dict.update({j:pow(a,j,n)})
	r = invmod(a,n)**m	
	y = b	
	#print (dict['j'])
	for i in range(m):
		for k in range(m):
			if(dict[k] == y):
				return i*m + k
			else:
				pass
		y = modulo_exp(y,r,n)