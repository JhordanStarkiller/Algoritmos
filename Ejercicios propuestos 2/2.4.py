import math
costo_hora = float (input ('CH: '))
horas = float (input ('Hrs: '))
if math.floor(horas)==horas:
    horas_cobradas=horas
else:
    horas_cobradas=math.floor(horas)+1
cobro=horas_cobradas*costo_hora
print (cobro)
#print (horas_cobradas)
