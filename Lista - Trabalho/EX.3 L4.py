notas = 0
quantidade = 0
while True:
    X = float(input('Digite a nova nota / -1 p/parar: '))
    if X == -1:
        if notaM >= 7:
            print(f'APROVADO! Sua média foi {notaM}, você digitou notas {quantidade} vezes.')
        elif notaM >= 5 and notaM < 7:
            print (f'RECUPERAÇÃO! Sua média foi {notaM}, você digitou notas {quantidade} vezes.')
        else:
            print(f'REPROVADO! Sua média foi {notaM}, você digitou notas {quantidade} vezes.')
        break
    else:
        notas = notas + X
        quantidade = quantidade + 1
        notaM = notas / quantidade
        
