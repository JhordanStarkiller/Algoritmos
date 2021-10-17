n=int(input())
ven=0
for i in range(n):
    vector=list(map(int, input().split()))
    ven=ven+(vector[0]*vector[1])
print(ven)