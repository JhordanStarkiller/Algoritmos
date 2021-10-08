N = int(input("N: "))
A = 0
B = 0
C = 0
T1 = 0
T2 = 0
T3 = 0
TT = 0
CN = 1
for i in range (N):
    DT = int(input("DT: "))
    PH = int(input("PH: "))
    SH = 0
    for j in range (DT):
        HT = int(input("HT: "))
        SH = SH + HT
    SS = SH * PH
    print("El sueldo del trabajador es: ", i , "es", SS)
    TOT = TOT + SS
print("El total que se pago es: ",TOT)

