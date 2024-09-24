import numpy as np

# Definindo as funções do sistema
# x[0] = x, x[1] = y
def F(x):
    return np.array([x[0] + x[1] - 3, x[0]**2 + x[1]**2 - 9])

# Definindo a Jacobiana do sistema
def JF(x):
    return np.array([[1, 1], [2*x[0], 2*x[1]]])

# Método de Newton-Raphson
# tol = iterações
def newton_raphson(F, JF, x0, tol=2, max_iter=100):
    x = x0
    for i in range(max_iter):
        delta = np.linalg.solve(JF(x), -F(x))
        x = x + delta
        if np.linalg.norm(delta) < tol:
            break
    return x

# Aproximação inicial
x0 = np.array([1, 5])

# Encontrando a solução
sol = newton_raphson(F, JF, x0)
print("Solução encontrada:", sol)
