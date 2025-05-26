# criar uma função chamada lista_compras () que:
#     usa while para adicionar itens à lista
#     remove itens se o usuário digitar: <item>
#     encerra quando digitar sair 
#     mostra a lista final em ordem alfabética
    
def lista_compras():
    lista = []
    
    while True:
        comando = input("Digite um item, 'remover:nome' ou 'sair': ").strip()
        
        if comando == "sair":
            break
        
        if "remover:" in comando:
            partes = comando.split(":")
            if len(partes) == 2:
                item_para_remover = partes[1].strip()
                if item_para_remover in lista:
                    lista.remove(item_para_remover)
                    print(f"'{item_para_remover}'removido da lista.")
                else:
                    print(f"'{item_para_remover}' não está na lista.")
            else:
                print("Formato errado. Use 'remover:nome'.")
        else:
            lista.append(comando)
            print(f"'{comando}' adicionado a lista.")
    
    lista.sort()
    print("\nLista final em ordem alfabética: ")
    for item in lista:
        print("- " + item)

# rodar função
lista_compras()

                