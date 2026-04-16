cigarros = int(input("quantos cigarros voce fuma por dia? "))
anos = int(input("a quantos anos voce fuma cigarro? "))
dias = cigarros*(anos*365)
perda = dias/24/6
print (f" voce ja perdeu {perda} dias de vida, apenas consumindo cigarro! ")
