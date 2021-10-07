TI = int(input("TI: "))
DI = input("DI: ")
TU = input("TU: ")

if TI <= 5:
	PAG = TI*1
elif TI <= 8:
	PAG = (TI-5)*0.8+5
elif TI <= 10:
	PAG = (TI-8)*0.7+7.4
else:
	PAG (TI-10)*0.5+8.8

if DI == "DOM":
	IMP = PAG*0.05
elif TU == "M":
	IMP = PAG*0.15
else:
	IMP = PAG*0.10

TOT = PAG + IMP
print("El pago es: "+ repr(PAG))
print("El impuesto es: "+ repr(IMP))
print("El pagopago total es: "+ repr(TOT))