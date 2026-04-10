Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> parede = float(input('Digite a área a ser pintada: '))
... 
... if parede % 54 == 0:
...     lata = parede/54
...     valor = lata * 80
...     print(f'O número de lata(s) {lata} com o valor {valor}')
... else:
...     lata = int(parede/54) + 1
...     valor = lata * 80
...     print(f'O número de lata(s) {lata} com o valor {valor}')
