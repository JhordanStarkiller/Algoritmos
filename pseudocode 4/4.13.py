P = 5.0
T=0
for i in range (20):
	P=P*2
	print("El pago mensual: "+ repr(P))
	T = T+P
print("El pago total: "+repr(T))
