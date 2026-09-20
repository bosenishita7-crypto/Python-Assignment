import numpy as np



A = np.array([[3, -5],
              [4, -2]])

B = np.array([10, 7])

solution = np.linalg.solve(A, B)

x, y = solution
print("Value of x =", x)
print("Value of y =", y)