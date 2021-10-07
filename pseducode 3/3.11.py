N=int(input("N: "))
TI=str(input("TI: "))
TP=str(input("TP: "))

if(TI=="Sencilla"):
    PA = 20.00
else:
    if(TI=="Doble"):
        PA = 25.00
    else:
        PA = 28.00
TO = PA * N
if(TP == "Tarjeta"):
    CA = TO * 0.05
else:
    CA = 0
TOT = TO + CA
print("La Hamburguesa costo: ", PA)
print("Total sin cargo: ", TO)
print("El cargo es: ", CA)
print("El total por pagar es: ", TOT)