N = int(input())
p = input()
if N >10:
    cadena = p[0]+str(N-2)+str(p[N-1])
    print(cadena)
else:
    print(p)