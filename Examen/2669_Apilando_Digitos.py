N = int(input())
if N > 0:
    for i in range(1,N+1):
        for j in range(i):
            print(i,end="")
        print()
    for i in range(N-1, 0,-1):
        for j in range(i):
            print(i,end="")
        print()