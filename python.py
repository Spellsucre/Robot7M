def somme(n):
	if(n == 0):
		return 0
	else:
		return somme(n-1)+n

b = somme(5)
print(b)

def factorielle(n):
	if(n == 0):
		return 1
	else:
		return n*factorielle(n-1)

print(factorielle(5))

def puissance(x,n):
	if(n>0):
		if(n%2 == 0):
			return puissance(x,n/2)*puissance(x,n/2)
		else:
			return x*puissance(x,(n-1)/2)*puissance(x,(n-1)/2)
	else:
		return 1

print(puissance(2,5))