from random import * 
import math
def modulo_addition(a,b,c):
	if (a < c and b < c): 
	 	return (a+b)%c
	else:
	 	return modulo_addition(a%c,b%c,c)
def modulo_mult(a,b,c):
	if (a < c and b < c):
		return (a*b)%c
	else :
		return modulo_mult(a%c,b%c,c)
def modulo_exp(a,b,c):
	if b == 1 :
		return a%c
	else :
		if b%2 == 0 : 
			temp = modulo_exp(a,b/2,c)
			return (temp**2)%c
		else :
			return ((modulo_exp(a,b-1,c))*(a%c))%c

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
def extgcd(a,b):
    if a==0:
        return (b,0,1)
    else:
        g,y,x = extgcd(b%a,a)
        return (g,x-(b//a)*y,y)

def invmod(a,b):
    g,x,y = extgcd(a,b)
    if g!=1:
        return -1
    else:
        return x % b

def rsa_keygen(p,q):
	n = p*q
	phi = (p-1)*(q-1)
	e = 3
	while e < phi :
		if extgcd(e,phi)[0] == 1 :
			break
		else : e = e+1
	d = invmod(e,phi)
	return [n,e,d]
def rsa_encrypt(m,n,e):
	return pow(m,e,n)	
def rsa_decrypt(en,n,d):
	return pow(en,d,n)
def isPrime(n):
	if n == 1: return False
	i = 0
	ans = True
	for i in range(100) :
		x = randrange(1,n)
		if extgcd(x,n)[0] != 1 or pow(x,n-1,n) != 1 : 
			#print(x) 
			return False 
	return ans
def genPrime2(len):
	i = 2**len - 1
	while not isPrime(i) :
		i = i+2
	return i
n_length = 512
ran = 271
p,q = genPrime2(ran),genPrime2(n_length-ran)
key = rsa_keygen(p,q)
m = eval(input())
enc_msg = rsa_encrypt(m,key[0],key[1])
print(enc_msg)
dec = rsa_decrypt(enc_msg,key[0],key[2])
print(dec)
