print("=== Sistema de Controle do João Papo-de-Pescador ===")

peso = float(input("Digite o peso total de peixes (kg): "))

limite = 50.0

if peso > limite:
    excesso = peso - limite
    multa = excesso * 4.00
    print(f"Houve um excesso de {excesso:.2f} kg.")
    print(f"O valor da multa a pagar é: R$ {multa:.2f}")
else:
    excesso = 0
    multa = 0
    print("Peso dentro do limite permitido.")
    print(f"Excesso: {excesso}")
    print(f"Multa: R$ {multa}")
