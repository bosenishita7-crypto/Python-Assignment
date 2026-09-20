import numpy as np

A = np.array([
    [4, 3, 2, 1],
    [3, 4, 3, 2],
    [2, 3, 4, 3],
    [1, 2, 3, 4]
], dtype=float)

# 1. QR Decomposition
Q, R = np.linalg.qr(A)

# 2. Singular Value Decomposition
U, S, Vt = np.linalg.svd(A)

# 3. Least Squares
b = np.array([1, 2, 3, 4], dtype=float)
x, residuals, rank, sing_vals = np.linalg.lstsq(A, b, rcond=None)