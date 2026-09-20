
import numpy as np

# Define two 3x3 matrices
A = np.array([
    [2, 1, 1],
    [1, 3, 2],
    [1, 0, 4]
])

B = np.array([
    [4, 2, 1],
    [3, 5, 2],
    [1, 1, 3]
])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Inverse of A
A_inv = np.linalg.inv(A)
print("\nInverse of A:\n", A_inv)

# Determinant of B
det_B = np.linalg.det(B)
print("\nDeterminant of B:", det_B)

# A . A_inverse (should give identity matrix)
identity_check = np.dot(A, A_inv)
print("\nA . A_inverse:\n", identity_check)