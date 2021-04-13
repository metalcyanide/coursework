import math


def h1(n):
	if((n % 2 )!= 0):
		return n
	else:
		return h1(n/2)	


def h2(n,s):
	if((n % 2 ) != 0):
		return s
	else:
		return h2(n/2,s+1)

def primality(n):
	if(n<=1):
		print ("false")
	else:
		b = 0
		d = h1(n-1)
		s = h2(n-1,0)
		m = min(n-1,math.floor(2 * ((math.log(n))**2)))
		if(n < 2047):
			L = [2]
		elif(n < 1373653):
			L = [2,3]
		elif(n < 9080191):
			L = [31,73]
		elif(n < 25326001):	
			L = [2,3,5]
		elif(n < 3215031751):
			L = [2,3,5,7]
		elif(n < 4759123141):
			L = [2,7,61]
		elif(n < 1122004669633):
			L = [2,13,23,1662803]
		elif(n < 2152302898747):
			L = [2,3,5,7,11]
		elif(n < 3474749660383):
			L = [2,3,5,7,11,13]
		elif(n < 341550071728321):
			L = [2,3,5,7,11,13,17]
		elif(n < 3825123056546413051):
			L = [2,3,5,7,11,13,17,19,23]
		elif(n < 18446744073709551616):
			L = [2,3,5,7,11,13,17,19,23,29,31,37]
		elif(n < 318665857834031151167461):
			L = [2,3,5,7,11,13,17,19,23,29,31,37]
		elif(n < 3317044064679887385961981):
			L = [2,3,5,7,11,13,17,19,23,29,31,37,41]		
												
		for a in L:
			if (((a**d) - 1)%n == 0):
				continue				
			for r in range(s):
				if( ((a**((2**r)*d) + 1)%n != 0) ):
					b = b + 1
				else:
					break
			if(b == s):
				return 0
		return 1	


print (primality(18446744073709551615))