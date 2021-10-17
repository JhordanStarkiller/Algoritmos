n=int(input())
vector=list(map(int, input().split()))
valorMaximo=max(vector)
con=0
for i in range(n):
    if(valorMaximo==vector[i]):
        con+=1
print(con)
