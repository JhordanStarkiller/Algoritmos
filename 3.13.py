C=int(input("C: "))
MP=float(input("MP: "))
if (C==3 or C==4):
    MO=MP*0.75
else:
    if(C==1 or C==5):
        MO=MP*0.80
    else:
        MO=MP*0.85
if(C==2 or C==5):
    GF=MP*0.30
else:
    if(C==3 or C==6):
        GF=MP*0.35
    else:
        GF=MP*0.28
CP=MP+MO+GF
PV=CP+CP*0.45
print("El costo de produccion es: ", CP)
print("El precio de venta es: ", PV)