dias = int(input("digite a quantidade de dias! "))
horas = int(input("digite a quantidade de horas! "))
minutos = int(input("digite a quantidade de minutos! "))
segundos = int(input("digite a quantidade de segundos! "))
DiasTotal = dias*24*60*60
HorasTotal = horas*60*60
MinutosTotal = minutos*60
SegundosTotal = DiasTotal+HorasTotal+MinutosTotal+segundos
print (f" a quantidade de segundos presente em {dias} dias, {horas} horas, {minutos} minutos e {segundos} e de {SegundosTotal}!  ")
