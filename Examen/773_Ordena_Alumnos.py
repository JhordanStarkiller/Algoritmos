'''n=int(input('Cantidad de alumnos: '))
while True:
    notas = input('ingresa las nota: ')
    # strip() borra espacios de los extremos
    # split(' ') separa un string usando un espacio vacio como separador
    lista = notas.strip().split(' ')
    if len(lista) == n:
        break
# inputs
print('INPUT:')
print('cantidad:', n)
print('notas:', notas)

# devuelve una lista
lista = [int(i) for i in lista]
# ordena la lista
lista.sort(reverse=True)

# resultado
print('\nOUTPUT:')
for i in lista:
    print(i, end=' ')'''
n=int(input())
while True:
    notas = input()
    # strip() borra espacios de los extremos
    # split(' ') separa un string usando un espacio vacio como separador
    lista = notas.strip().split(' ')
    if len(lista) == n:
        break
# inputs
'''print('INPUT:')
print('cantidad:', n)
print('notas:', notas)'''

# devuelve una lista
lista = [int(i) for i in lista]
# ordena la lista
lista.sort(reverse=True)

# resultado
'''print('\nOUTPUT:')'''
for i in lista:
    print(i, end=' ')

    