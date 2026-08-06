import random

numeros = []
par = []
impar = []

i = 1

while i <= 20:

    numero = random.randint(1, 100)

    numeros.append(numero)

    if numero % 2 == 0:
        par.append(numero)

    else:
        impar.append(numero)

    i = i + 1

print("Lista completa:", numeros)
print("Lista de pares:", par)
print("Lista de ímpares:", impar)
