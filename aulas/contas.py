import numpy as np 

A = np.array([
    [3, 0],
    [-1, 2],
    [1, 1]
])

B = np.array([
    [1, 5, 2],
    [-1, 1, 0],
    [-4, 1, 3]
])

C = np.dot(B,A)
print(C)

