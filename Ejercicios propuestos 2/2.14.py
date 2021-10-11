D = int(input("Dias: "))
GH = float(input("Gasto Hotel: "))
GC = float(input("Gasto Comida: "))
TO = (GH * D) + (GC * D) + (D * 100)

print("gasto para comidas es " , GC * D)
print("gasto para hotel es " , GH * D)
print("otros gastos es " , 100 * D)
print(TO, "es el total")