NA=int(input("NA: "))
if(NA >= 100):
    PA = 65.0
else:
    if(NA >= 50):
        PA = 70.0
    else:
         if(NA >= 30):
             PA = 95.0
         else:
             PA = 4000 / NA
TOT = PA * NA
print("El pago individual es: ", PA)
print("El pago total es: ", TOT)