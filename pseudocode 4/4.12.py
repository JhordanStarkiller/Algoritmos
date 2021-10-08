N = float(input("N: "))
A = 0
B = 0
C = 0
T1 = 0
T2 = 0
T3 = 0
TT = 0
CN = 1
while CN <= N:
    V = float(input("V: "))
    if (V > 1000):
        A = A + 1
        T1 = T1 + 1
    else:
        if (V > 500):
            B = B + 1
            T2 = T2 + 1
        else:
            C = C + 1
            T3 = T3 * 1
    TT = TT + V
    CN = CN + 1
print("La ventas y el total de ventas 1 es: ", A , T1)
print("La ventas y el total de ventas 2 es: ", B , T2)
print("La ventas y el total de ventas 2 es: ", C , T3)
print("el total de ventas es: ", TT)