# escrever uma função chamada numeros_pares que:
#     recebe uma lista de numeros inteiros
#     retorna uam nova lista contendo apenas os numeros pares da lista original

l = [0,5,3,6,8,7,94,6,5,10,12,20]

def numeros_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

print(numeros_pares(l))