nome = input("Digite um nome: ")
if nome != "jerry":
    quantidade = int(input("Quantidade de porção? "))
    porcao = 5.90
    custo = porcao * quantidade
    print(custo)
else:
    print(nome)