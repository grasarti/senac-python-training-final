# count() - conta quantas vezes uma string ou inteiro tem dentro de um conjunto de dados
minha_string = "Quantas madeiras um esquilo poderia empilhar se um esquilo pudesse empilhar madeiras"
print(minha_string.count("a"))

minha_lista = [1,2,3,5,6,6,9,9,8]
print(minha_lista.count(6))


# replace
minha_palavra = "oi, oi, oi, amigos"
nova_palavra = minha_palavra.replace("Oi", "Olá")
print(nova_palavra)


# usar replace para trocar int
numeros = [12, 23, 42, 25]
 
nova_lista = [int(str(n).replace("2", "9")) for n in numeros]
 
print(nova_lista)


# matriz = lista bidimensional [linhas e colunas]

lista_bidimensional = [[0,1,2,3], [0,8,6,9], [1,2,7,4], [4,5,6,8]]
print(lista_bidimensional[2][2])

[0,1,2,3]
[0,8,6,9]
[1,2,7,4]
[4,5,6,8]
        
print(lista_bidimensional[0][0])
print(lista_bidimensional[1][0])
print(lista_bidimensional[2][0])
print(lista_bidimensional[3][0])