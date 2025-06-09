# calcular média, soma e desvio padrão
# escreva uma função chamada estatisticas_array que receba um array e retorne a soma, a média dos seus elementos


import numpy as np

def estatisticas_array(arr):
    soma = np.sum(arr)
    media = np.mean(arr)
    desvio = np.std(arr)
    return soma, media, desvio

# exemplo:
array = np.array([10, 20, 30, 40])
soma, media, desvio = estatisticas_array(array)
print(f"Soma: {soma}, Média: {media}, Desvio Padrão: {desvio:.2f}")


# outra forma de resolução
def estatisticas_array(array):
    soma = np.sum(array)
    media = np.mean(array)
    return soma, media

meu_array = np.array([10, 20, 30, 40, 50])
print(estatisticas_array(meu_array))