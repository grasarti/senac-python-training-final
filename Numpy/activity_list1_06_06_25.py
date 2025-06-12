# Objetivo escrever uma função chamada criar_array que receba uma lista de números inteiros e retorne um array Numpy

import numpy as np

def criar_array(lista):
    return np.array(lista) # np.array converte a lista em array

# exemplo

minha_lista = [10, 20, 30, 40]
meu_array = criar_array(minha_lista)

print(meu_array)

# uma lista em Python é algo assim: [1,2,3,4]
# um array Numpy é tipo uma lista mais poderosa, com mais funções matemáticas
# a função np.array() serve para transformar uma lista em array