N = int(input("N: "))
A = 0
B = 1
print (A,B)
M = 1
while M <= (N - 2):
    C = A + B
    print(C)
    A = B
    B = C
    M = M + 1