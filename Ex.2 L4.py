from datetime import date
data = date.today()
while True:
    X = int(input('1 - Dizer Oi, 2 - Mostrar a data, 3 - Sair.'))
    if X == 1:
        print(f'Você Clicou no número 1!')
        print(f'Oi especial para você!')
    elif X == 2:
        print (f' Você clicou no número 2!')
        print(f'Data Atual: {data}')
    elif X == 3:
        print (f' Você clicou no número 3! Programa encerrando...')
        break
    else:
        print(f"Opção inválida!")
