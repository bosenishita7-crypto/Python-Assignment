
import numpy as np
from scipy.linalg import solve

# 1) Solve linear equations
# 2x + 3y = 8
# 4x + 5y = 14

A = np.array([[2, 3], [4, 5]])
B = np.array([8, 14])

x, y = solve(A, B)

print("x =", x)
print("y =", y)


# 2) Speed of cars A and B
# Same direction: 11 hours
# Opposite direction: 1 hour

# Let speeds be A and B
# Distance = speed × time
# Same direction: D = 11(A - B)
# Opposite direction: D = A + B

# Therefore: 11(A-B) = A+B
# => 10A - 12B = 0

A = np.array([[10, -12]])
B = np.array([0])

# From the given information alone, the actual speeds
# cannot be uniquely determined without the distance.

print("For cars, the given information is not enough")
print("to find unique velocities.")