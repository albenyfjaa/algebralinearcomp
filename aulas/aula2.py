import numpy as np

A = np.array([
    [1, 2, 3],
    [0, -3, -6],
    [0, 0, 5]
])

b = np.array([
    10,
    -29,
    14
])

n = len(A)

x = np.zeros(3)

#Backward substitution
print("n: ", n)
for i in range(n - 1, 0-1, -1):
    print(f"-------Iteração-------")
    print("i = ", i)
    print("b = ", b[i])
    print("A = ", A[i][i])
    
    sum_ax = 0
    for j in range(i + 1, n): # Não há calculo de j na primeira interação, pois j só começa a partir de 2
        print("j = ", i+ 1)        
        sum_ax += A[i, j] * x[j]
        print(A[i, j], "|" ,x[j])
        print("sum_ax = ", sum_ax)       
    
    x[i] = (b[i] - sum_ax) / A[i,i]
    print(f"x[{i+1},1] = ", x[i])
print(x)