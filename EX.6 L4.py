saldo = 1000
opcao = 0

while opcao != 4:
    print("=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == 2:
        valor = float(input("Digite o valor do depósito: "))
        saldo = saldo + valor
        print("Depósito realizado com sucesso!")

    elif opcao == 3:
        valor = float(input("Digite o valor do saque: "))

        if valor > saldo:
            print("Saldo insuficiente!")

        elif valor <= 0:
            print("Valor inválido!")

        else:
            saldo = saldo - valor
            print("Saque realizado com sucesso!")

    elif opcao == 4:
        print("Encerrando o sistema...")

    else:
        print("Opção inválida!")
print(f"-----------------------------------------------")
