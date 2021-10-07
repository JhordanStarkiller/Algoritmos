x = int(input("x: "))
if x >= 1000:
	PAG = x*0.85
else:
	PAG = x*0.90
print("el pago es: " + repr(PAG))
