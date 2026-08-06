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

# Cria a lista de palavras
palavras = texto.split()

# Letras da palavra "python"
letras = "python"

# Filtra as palavras que começam ou terminam com uma dessas letras
resultado = [
    palavra
    for palavra in palavras
    if palavra[0] in letras or palavra[-1] in letras
]

# Imprime o resultado
print(resultado)
