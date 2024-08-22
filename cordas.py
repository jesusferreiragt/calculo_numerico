import math

def f(x):
    # return 1 - 40*(3+x)/(3*x + (x**2)**3)
    # return x**2 - math.exp(x)
    # return x**2 - 3
    # return 14 - 6.3**x
    return -5*x**4 + 216*x**2 - 1296

def cordas():
    x0 = float(input('x0: '))
    x1 = float(input('x1: '))
    iteracoes = int(input('iterações: '))
    iteracao = 0
    while iteracao <= iteracoes:
        x2 = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
        x0 = x1
        x1 = x2
        iteracao += 1
    print(f'A raiz encontrada foi: x = {x2}')
    print(f'f(x) = {f(x2)}')

cordas()