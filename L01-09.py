dias = int(input("quantos dias voce alugou o carro? "))
km = float(input("quantos KM foi percorrido com o carro alugado? "))
diasPreco = dias*60
kmPreco = km*0.15
PrecoTotal = kmPreco+diasPreco
print (f" voce devera pagar R${PrecoTotal}")
