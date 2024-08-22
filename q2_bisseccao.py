# tol = erro
# n = num, de iterações

def bissec(f, a, b, tol, n):
    i = 1
    fa = f(a)
    while (i <= n):
        c = (b+a)/2
        fc = f(c)
        if ((fc == 0) or ((b-a)/2 < tol)):
            return c
        i = i + 1
        if (fa * fc > 0):
            a = c
            fa = fc
        else:
            b = c
    raise NameError('Número máximo de iterações excedido!!')

if __name__== '__main__':
    def f(x):
        return x**2 - 3 # função
Raiz = bissec(f, 1, 2, 0.01, 8)
print(Raiz)