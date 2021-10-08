N = int(input("N: "))
TOT = 0
for I in range (N):
    DT = int(input("DT: "))
    PH = int(input("PH: "))
    SH = 0
    for j in range (DT):
        HT = int(input("HT: "))
        SH = SH + HT
    SS = SH * PH
    print("El sueldo del trabajador es: ", I , "es", SS)
    TOT = TOT + SS
print("El total que se pago es: ",TOT)

