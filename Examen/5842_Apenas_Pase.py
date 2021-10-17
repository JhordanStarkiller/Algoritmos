k=float(input())
n=int(input())
s=0.0
for i in range(n):
    e=float(input())
    s+=e
p=s/n
if(p>k):
    print("Presume")
else:
    print("Ladra")
