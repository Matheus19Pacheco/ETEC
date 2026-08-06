import random

lista = []
contador = 0
numero = 0
while contador < 10:
    numero = random.randint(1, 100)
    lista.append(numero)
    contador = contador + 1
print(f' Números: {lista}')

maior = lista[0]
menor = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
