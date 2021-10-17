n=int(input())
lista= []
while n!=1:
    lista.append(int(n))
    if n%2 ==0:
        n= n/2		
    else:
        n=(n*3)+1
lista.append(1)
for i in lista:
	print(i, end=' ')