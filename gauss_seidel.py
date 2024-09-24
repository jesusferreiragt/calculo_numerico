import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    
    for k in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        # Verifica a convergência
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            break
    
    return x

# Exemplo de uso
A = np.array([[3, 1, 1],
              [1, 4, 2],
              [0, 2, 5]], dtype=float)
b = np.array([7, 4, 5], dtype=float)
x0 = np.zeros(len(b))
tol = 1e-10
max_iter = 3

sol = gauss_seidel(A, b, x0, tol, max_iter)
print("Solução:", sol)
