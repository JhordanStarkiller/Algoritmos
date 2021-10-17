n=int(input())
vector=list(map(int, input().split()))
suma=0
for i in range (1,n+1):
    num=(int(i*(i+1)/2))
    suma+=num
print(suma)