A=int(input("A: "))
B=int(input("B: "))
C=int(input("C: "))
if(A > B):
    if(A > C):
        M = A
    else:
        M = C
else:
    if(B > C):
        M = B
    else:
        M = C
print("El Mayor es: ", M)