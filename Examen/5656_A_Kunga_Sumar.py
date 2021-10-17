CONDITION = True
while (CONDITION):
    N = int(input())
    RESULT = 0
    if(N>0):
        if(N <= 1000):
            while (N >= 0):
                RESULT = RESULT + N
                N = N-1
        print(RESULT)
    else:
        CONDITION = False