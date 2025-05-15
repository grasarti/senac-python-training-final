precoProduto = float(input("Qual o preço do produto? "))

valorDesconto = int(input("Qual o percentual de desconto? "))

porcentagem = precoProduto * (valorDesconto / 100)

valorNovo = precoProduto - porcentagem

print(f"O valor do desconto é de {porcentagem} e o valor do produto é {valorNovo} ")