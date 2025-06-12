#Escreva uma função chamada matriz_identidade que receba um número n e retorne uma matriz identidade n x n com Numpy

#Matriz identidade = é uma matriz quadrada(mesmo nº de linhas e colunas),
#   onde os números da diagonal principal são 1 e o resto é 0

#A função np.identity(n) faz isso


import numpy as np

def matriz_identidade(n):
    return np.identity(n)

print(matriz_identidade(4))