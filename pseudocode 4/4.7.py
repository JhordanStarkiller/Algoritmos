CP = 0
CN = 0
C = 0
NU = float(input("NU: "))
while True:
	CA = int(input("CA: "))
	if CA > 0:
		CP = CP+1
	else:
		CN = CN+1
	C = C+1
	if C>NU:
		break

print("positivos: "+repr(CP))
print("Negatvos: "+repr(CN))
