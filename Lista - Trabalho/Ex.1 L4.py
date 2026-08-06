contador = 0
positivos = 0

while contador < 5:
    numero = int(input("Digite um número inteiro: "))

    if numero > 0:
        print("Positivo")
        positivos += 1
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")

    contador += 1

print("Quantidade de números positivos:", positivos)
