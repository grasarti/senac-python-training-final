nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto (R$): "))

if preco <= 50:
    categoria = "Categoria Econômica"
elif preco <= 100:
    categoria = "Categoria Intermediária"
else:
    categoria = "Categoria Premium"

print(f"\nProduto: {nome_produto}")
print(f"Preço: R$ {preco:.2f}")
print(f"Classificação: {categoria}")