# Criar uma lista com os valores [1, 2, 3, 4, 5]
# Pedir ao usuário:
#     Um índice
#     Um novo valor para substituir na lista
# Substituir o valor no índice informado e mostrar a lista atualizada
# Repetir o processo até o usuário digitar -1 para o índice

# Lista inicial
numeros = [1, 2, 3, 4, 5]

while True:
    print("\nLista atual:", numeros)
    
    # Solicita ao usuário o índice que deseja alterar
    indice = int(input("Digite um índice para alterar (-1 para sair): "))
    
    # Encerra o programa se o usuário digitar -1
    if indice == -1:
        print("Programa encerrado.")
        break
    
    # Verifica se o índice está dentro do tamanho da lista
    if 0 <= indice < len(numeros):
        # Solicita o novo valor para substituir
        novo_valor = int(input("Digite o novo valor: "))
        # Substitui o valor na posição informada
        numeros[indice] = novo_valor
    else:
        print("Índice inválido. Tente novamente!")

