preco = float(input("digite o preco da mercadoria! "))
porcentagem = int(input("digite a porcentagem do desconto da mercadoria! "))
PrecoFinal = preco*(porcentagem/100)
desconto = preco-PrecoFinal
print (f" o valor da mercadoria com {porcentagem}% de desconto, ficou custando R${desconto}, e seu desconto em R$ foi de {PrecoFinal}. ")
