# Operações entre matrizes

import numpy as np

def somar_matrizes(m1, m2):
    m1 = np.array(m1)
    m2 = np.array(m2)
    
    if m1.shape != m2.shape:
        return "Erro: As matrizes não tem o mesmo tamanho."
    
    return m1 + m2

# exemplo:
m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]

resultado = somar_matrizes(m1, m2)
print(resultado)

# saída:
# [[6 8]
#   [10 12]]

