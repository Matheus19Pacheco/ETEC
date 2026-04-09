import math

print("=== Sistema Loja de Tintas ===")

area = float(input("Digite o tamanho da área a ser pintada (m²): "))

litros_necessarios = area / 3

quantidade_latas = math.ceil(litros_necessarios / 18)

preco_total = quantidade_latas * 80.00

print("-" * 30)
print(f"Litros necessários: {litros_necessarios:.2f} L")
print(f"Quantidade de latas: {quantidade_latas}")
print(f"Preço total: R$ {preco_total:.2f}")
print("-" * 30)
