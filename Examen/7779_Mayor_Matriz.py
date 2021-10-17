f=int(input("F: "))
c=int(input("C: "))
matriz=[]
for i in range(f):
    for j in range(c):
        vector=list(map(int, input().split()))
        matriz.append(vector)
mayor=matriz[0][0]
for f in matriz:
    for valor in f:
        if(valor>mayor):
            mayor=valor
print(mayor)

