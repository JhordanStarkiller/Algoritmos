N = int(input())
A = 0
B = 1
M = 0
if N == 0:
    print(A)
elif N == 1:
    print(B)
elif N<=30:
    while M <=(N-2):        
        C = A + B        
        A = B
        B = C
        M = M + 1
    print(C)
    