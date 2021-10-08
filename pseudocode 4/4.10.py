SH = 0
PH = float(input("PH: "))
D = 1
while True:
	HT = int(input("HT: "))
	SH = SH+HT
	D = D+1
	if D<=6:
		break

SU = SH*PH
print("Las horas laboradas son: "+repr(SH))
print("El sueldo es: "+repr(SU))
