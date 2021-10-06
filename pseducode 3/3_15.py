TT = int(input("TT: "))
LA = float(input("LA: "))
if TT == 1:
	AC = LA*0.25
elif TT == 2:
	AC = LA*0.35
elif TT == 3:
	AC = LA*0.40
else:
	AC = LA*0.50
NC = LA+AC 
print("El aumento de credito: "+ repr(AC))
print("Nuevo limite de credito: "+ repr(NC))
