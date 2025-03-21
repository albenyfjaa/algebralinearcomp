import numpy as np
from fractions import Fraction

# Definir matriz A
A = np.array([
    [1, 2],
    [2, 1],
])

# Definir matriz B
B = np.array([
    [1, 2, 6],
    [2, 1, 6],
    [1, 1, 4]
])

C = np.array([
    [1, 2, 1, 0],
    [0, 0, -1, 1],
    [-3, 4, -5, 2],
    [1, 1, 0, -2],
])

# Definir matriz A-1
det = np.linalg.det(C)
print(det)

inv = np.linalg.inv(C)

# Converter A_inv em fração
inv_frac = np.vectorize(lambda x: Fraction(x).limit_denominator())(inv)

print("Matriz inversa: ")
print(inv)

inv_frac_str = str(inv_frac).replace(",","/").replace("Fraction","").replace(" ","").replace(")(",",")

print(inv_frac_str)