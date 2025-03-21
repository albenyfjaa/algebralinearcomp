import numpy as np

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


n = len(A) # Armazena tamanho de n com base no tamanho da matriz A
x = np.zeros(n) # Defini um valor de x qualquer (zero) com base no tamanho da matriz A.

print("n: ", n)
for i in range(n - 1, -1, -1): # Iteração em i de trás para frente (inicia no maior valor de i e termina no menor valor)
    print(f"-------Iteração-------")
    print("i = ", i)
    print("b = ", b[i])
    print("A = ", A[i][i])
    
    sum_ax = 0 # Define variável de soma = 0
    for j in range(i + 1, n): # Não há calculo de j na primeira interação
        print("j = ", i+ 1)
        
        sum_ax += A[i, j] * x[j] # Expressão para o somatório    
        print("sum_ax = ", sum_ax)    

    x[i] = (b[i] - sum_ax) / A[i,i] # Expressão da Back Substitution
    print(f"x[{i+1},1] = ", x[i])
    print(x)

           
