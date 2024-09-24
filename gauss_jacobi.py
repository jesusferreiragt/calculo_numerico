import numpy as np

def jacobi(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
    return x

# Exemplo de uso
A = np.array([[3, 1, 1], [1, 4, 2], [0, 2, 5]]) # coeficientes
b = np.array([7, 4, 5]) # resultados
x0 = np.zeros(len(b))
tol = 1e-10
max_iter = 3

solucao = jacobi(A, b, x0, tol, max_iter)
print("Solução:", solucao)