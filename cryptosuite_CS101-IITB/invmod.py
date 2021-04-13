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

print(invmod(7,20))
