# Peça ao usuário para escolher entre adicionar ou remover um item de uma lista
# Se a escolha for "adicionar", deve acrescentar o próximo número sequencial, começando por 1
# Se a escolha for "remover", deve remover o último item da lista
# Mostrar a lista antes e depois de cada operação
# Evitar erro se tentar remover de uma lista vazia

# Lista vazia no início
lista = []
proximo_item = 1

while True:
    # Imprime a lista atual
    print("\nLista atual:", lista)
    
    # Pede ação ao usuário
    acao = input("Digite 'adicionar', 'remover' ou 'sair': ").lower()
    
    if acao == "adicionar":
        # Adiciona o próximo item
        lista.append(proximo_item)
        proximo_item += 1
        print("Item adicionado!")
    
    elif acao == "remover":
        if lista:
            removido = lista.pop()
            print(f"Item {removido} removido!")
        else:
            print("A lista está vazia. Nada para remover.")
            
    elif acao == "sair":
        print("Programa encerrado.")
        break
    else:
        print("Comando inválido. Tente novamente.")
        

# Outra opção de resposta

lista = []
while True:
    opcao = input("O que você quer fazer? + ou -: ")
    if opcao == "+":
        if len(lista) == 0:
            lista.append(1)
        else:
            lista.append(lista[-1] + 1)
    else:
        if len(lista) == 0:
            print("A lista está vazia")
        else:
            lista.pop(len(lista)-1)
    print(lista)