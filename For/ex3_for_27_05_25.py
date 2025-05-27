# criar uma função chamada Soma_Positivos que:
#     recebe uma lista de números inteiros
#     retorna a soma dos valores positivos (ou seja maiores que zero)
    
def Soma_Positivos(lista):
    soma = 0
    for numero in lista:
        if numero > 0:
            soma += numero
    return soma

print(Soma_Positivos([3, -2, 7, -1, 0, 5]))