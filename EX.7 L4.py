import random
numero_secreto = random.randint(1, 20)
tentativas = 0
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Digite um número entre 1 e 20: "))
    tentativas = tentativas + 1

    if palpite > numero_secreto:
        print("Muito alto!")

    elif palpite < numero_secreto:
        print("Muito baixo!")

    else:
        print("Acertou!")

print(f"Você acertou em {tentativas} tentativa(s).")
