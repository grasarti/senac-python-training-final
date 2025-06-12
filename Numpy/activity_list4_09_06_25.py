# Gerar array de valores entre dois números
# Escreva uma função chamada gerar_array_intervalo que receba 2 inteiros e
# retome um array contendo todos os inteiros entre eles


import numpy as np

def gerar_array_intervalo(inicio, fim):
    return np.arange(inicio + 1, fim)

# Exemplo:
print(gerar_array_intervalo(3, 10))     #Saída: [4 5 6 7 8 9]
