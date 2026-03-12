salarioAnt = float(input("digite seu salario antigo! "))
porcentagem = int(input("digite a porcentagem do aumento do salario! "))
SalarioNovo = salarioAnt*porcentagem/100+salarioAnt
QntAumento = SalarioNovo - salarioAnt
print (f" seu salario era de R${salarioAnt}, com um aumento de {porcentagem}%, voce teve um aumento de R${QntAumento} e seu novo salario e de R${SalarioNovo}")
