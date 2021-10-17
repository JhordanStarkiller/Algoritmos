n=int(input())
matriz=[]
suma=0
for i in range(n):
    vector=list(map(int, input().split()))
    matriz.append(vector)
for i in range(n):
    for j in range(n):
        if i==j:
            suma+=matriz[i][j]
        
if suma/n==matriz[0][0]:    
    print('SI')
else:
    print('NO')
