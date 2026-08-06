senha=123

while True:
    entrar= int(input("Digite sua senha: "))

    if entrar!=senha:
        print("Senha incorreta")

    else:
        print("Senha correta")
        break
