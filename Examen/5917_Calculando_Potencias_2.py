cont = 1
res = 1
n = int(input())
if (n%2 == 0):
	while res!=n:
		res = 2**cont
		cont = cont + 1
	print(repr(cont-1))
