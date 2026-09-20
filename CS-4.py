import numpy as np
from scipy.linalg import lu

np.set_printoptions(precision=4, suppress=True)

# 1. Create a 4x4 square matrix
A = np.array([
    [4, 3, 2, 1],
    [3, 4, 3, 2],
    [2, 3, 4, 3],
    [1, 2, 3, 4]
], dtype=float)

print("Matrix A (4x4):")
print(A)

# 2. Eigenvalues and Eigenvectors
eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues:", eigvals)
print("Eigenvectors (columns):")
print(eigvecs)

# 3. PLU Decomposition
P, L, U = lu(A)
print("Permutation Matrix P:\n", P)
print("Lower Triangular L:\n", L)
print("Upper Triangular U:\n", U)