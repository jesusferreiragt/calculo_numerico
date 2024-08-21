# epsilon = erro
# iter = iterações

def Newton(f, df, x0, epsilon, Iter):
    if abs(f(x0)) <= epsilon:
        return x0
    print('k\t x0\t\t f(x0)')
    k = 1
    while k <= Iter:
        x1 = x0 - f(x0)/df(x0)
        print('%d %e\t %e' %(k, x1, f(x1)))
        if abs(f(x1)) <= epsilon:
            return x1
        x0 = x1
        k = k+1
    print('Erro: máximo de iterações atingido')
    return x1

if __name__== '__main__':
    def f(x):
        return x**3 - 2*x**2 - 5 # função
    def df(x):
        return 3*x**2 - 4*x # derivada da função
Raiz = Newton(f, df, 4, 0.001, 20)
print(Raiz)