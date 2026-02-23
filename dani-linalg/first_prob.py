import math
import numpy as np

A = np.array([
    [1, -4, -5],
    [0, -1, -4],
    [0, 0, 5]
              ])

B = np.array([7, -3, 5])

X = np.linalg.solve(A, B)

print(X)

# This returns B if it is correct
print(A @ X)


print("finished")


