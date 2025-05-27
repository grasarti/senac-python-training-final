# escrever uma função chamada lista_soma que:
#     recebe 2 listas de números inteiros
#     retorna uma nova lista com a soma dos itens de cada índice das 2 listas
#     pode assumir que as 2 listas têm o mesmo tamanho
    
def lista_soma(lista1, lista2):
    resultado = []
    for i in range(len(lista1)):
        soma = lista1[i] + lista2[i]
        resultado.append(soma)
    return resultado

print(lista_soma([1, 2, 3], [4, 5, 6])) # resultado: [5, 7, 9]