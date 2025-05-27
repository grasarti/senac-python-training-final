# criar uma função chamada lista_estrelas(lista) que:
#     recebe uma lista de numeros inteiros como argumento
#     para cada número da lista, imprime uma linha com aquela quantidade de asteriscos (*)
    
lista_estrela = [3, 7, 1, 1, 2]

def estrelasCaracter (lista: list):
    for i in lista:
        estrelas = "*" * i
        print(estrelas)
        
estrelasCaracter(lista_estrela)