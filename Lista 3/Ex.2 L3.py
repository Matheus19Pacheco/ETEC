usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

while senha == usuario:
    print("Erro! A senha não pode ser igual ao usuário.")
    senha = input("Digite outra senha: ")

print("Cadastro realizado com sucesso!")
