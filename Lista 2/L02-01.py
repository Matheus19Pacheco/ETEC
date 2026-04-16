l1 = int(input('Digite o lado 1 do triângulo: '))
l2 = int(input('Digite o lado 2 do triângulo: '))
l3 = int(input('Digite o lado 3 do triângulo: '))

if (l1 + l2 + l3) and (l1 + l3 > l2) and (l3 + l2 > l1):
    #print(f'É um triângulo')
    if (l1 == l2 == l3):
        print('É um triângulo EQUILÁTERO')
    elif (l1 == l2) or (l2 == l3) or (l1 == l3):
        print('É um triângulo ISÓSCELES')
    else:
        print(' É um triângulo ESCALENO')

else:
    print('Não é um triângulo')
