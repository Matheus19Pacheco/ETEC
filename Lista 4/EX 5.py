texto = """The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you."""

# Converte para minúsculas
texto = texto.lower()

# Remove caracteres especiais
for c in ".,:;!?()\"'":
    texto = texto.replace(c, "")

# Divide o texto em palavras
palavras = texto.split()

letras = "python"
contador = 0

# Percorre cada palavra
for palavra in palavras:

    # Verifica se a palavra possui alguma letra de "python"
    for letra in letras:
        if letra in palavra and len(palavra) > 4:
            contador += 1
            break  # Evita contar a mesma palavra mais de uma vez

print(contador)
