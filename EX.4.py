n1=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))

o=input("Qual operação você deseja realizar? + - * /: ")

if o=="+":
    soma= n1+n2
    print(f"{soma}")

elif o=="-":
    sub= n1-n2
    print(f"{sub}")

elif o=="*":
    mult= n1*n2
    print(f"{mult}")

elif o=="/":
    div= n1/n2
    print(f"{div}")

else:
    print("Erro")
