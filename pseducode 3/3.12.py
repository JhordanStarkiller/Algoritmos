NC = int(input("NC: "))
if NC <= 3:
	CC = 200
	TOT = NC*CC
else:
	if NC <= 5:
		CC = 150
		TOT = (NC-3)*150+600
	else:
		if NC <= 8:
			CC = 100
			TOT = (NC-5)*100+900
		else:
			CC = 50
			TOT = (NC-8)*50+1200

print("El costo de la consulta es: "+repr(CC))
print("El costo del tratamiento es: "+repr(TOT))
