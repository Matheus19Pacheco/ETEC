sc = "python123"

tentativas = 3

while tentativas > 0:

    senha = input("Digite a senha: ")

    if senha == sc:
        print("Acesso liberado!")
        break

    tentativas = tentativas - 1

    if tentativas > 0:
        print(f"Senha incorreta! Restam {tentativas} tentativa(s).")

if tentativas == 0:
    print("Conta bloqueada!")
