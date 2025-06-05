import numpy as np

# saída o array e as dimensões pelo método (ndim)
print("\n")
arr1d = np.array([1,2,3])
print(f"Array 1D: {arr1d}, Dimensões: {arr1d.ndim}")    # .ndim = numero de dimensões que tem o vetor/o arranjo
print("\n")

print("\n")
arr2d = np.array([[1,2,3,4,5], [5,6,8,9,6]])
print(f"Array 2D: {arr2d}, Dimensões: {arr2d.ndim}")
print("\n")

print("\n")
arr3d = np.array([[[0,5,6],[5,8,9]],[[4,5,6],[5,9,8]]])
print(f"Array 3D: {arr3d}, Dimensões: {arr3d.ndim}")
print("\n")

# shape (traz o números dos arrays)
print(f"Shape do arr1d: {arr1d.shape}")
print(f"Shape do arr2d: {arr2d.shape}")
print(f"Shape do arr3d: {arr3d.shape}")