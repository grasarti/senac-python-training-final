# exemplos de arrays e prints de atributos

import numpy as np

# Array 1D com 5 números inteiros
array_int = np.array([1,2,3,4,5])

# Array 1D com 5 números float
array_float = np.array([1.1, 2.2, 3.3, 4.4, 5.5])

# Array 2D com 2 linhas e 3 colunas de números float
array_2d = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])


# Mostrar as informações de cada array

# Para o array de inteiros:
print("\nArray de inteiros:")
print("Número de dimensões:", array_int.ndim)
print("Forma:", array_int.shape)
print("Total de elementos:", array_int.size)
print("Tipo de dados:", array_int.dtype)
print("Tamanho de cada item em bytes:", array_int.itemsize)
print()

# Para o array de floats:
print("Array de floats:")
print("Número de dimensões:", array_float.ndim)
print("Forma:", array_float.shape)
print("Total de elementos:", array_float.size)
print("Tipo de dados:", array_float.dtype)
print("Tamanho de cada item em bytes:", array_float.itemsize)
print()

# Para o array 2D:
print("Array 2D:")
print("Número de dimensões:", array_2d.ndim)
print("Forma:", array_2d.shape)
print("Total de elementos:", array_2d.size)
print("Tipo de dados:", array_2d.dtype)
print("Tamanho de cada item em bytes:", array_2d.itemsize)
print()