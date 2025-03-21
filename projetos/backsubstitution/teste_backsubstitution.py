import numpy as np
from backsubstitution import backsolve

A = np.array([
    [1, 2, 3],
    [0, 2, 3],
    [0, 0, 3],

])

b = np.array([
    10,
    29,
    14
])

backsubstitution_obj = backsolve(A, b)
