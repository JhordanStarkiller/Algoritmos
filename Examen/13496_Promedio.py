vector=list(map(int, input().split()))
vector = [int(i) for i in vector]
promedio = sum(vector)/10
print("El promedio es: {0:.3f}".format(promedio))