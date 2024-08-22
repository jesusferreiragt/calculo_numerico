import math

def f(x):
    return x**2 - math.exp(x)

def cordas():
    x0 = float(input('x0: '))
    x1 = float(input('x1:'))
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