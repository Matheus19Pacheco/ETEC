numero = int(input("Digite um número - 0 para sair -: "))

while numero != 0:

    i = 1

    while i <= 10:
        resultado = numero * i
        if resultado < 10:
            classificacao = "- pequeno -"

        elif resultado <= 50:
            classificacao = "- médio -"

        else:
            classificacao = "- grande -"

        print(f"{numero} x {i} = {resultado} {classificacao}")
        i = i + 1

    numero = int(input("Digite outro número - 0 para sair -: "))

print("Programa finalizado!")
