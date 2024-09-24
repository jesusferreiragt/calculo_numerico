import numpy as np
import sys

n = int(input('Insira o número de incógnitas: '))
a = np.zeros((n,n+1))
x = np.zeros(n)

print('Insira os coeficientes da matriz aumentada:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# Implementando o pivoteamento parcial
for i in range(n):
    # Encontra o maior valor na coluna i a partir da linha i
    max_row = i + np.argmax(np.abs(a[i:n, i]))
    
    # Se o maior valor não estiver na linha atual, troca as linhas
    if i != max_row:
        a[[i, max_row]] = a[[max_row, i]]

    if a[i][i] == 0.0:
        sys.exit('Divisão por zero detectada, mesmo após pivoteamento!')

    for j in range(i+1, n):
        ratio = a[j][i] / a[i][i]
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Substituição retroativa
x[n-1] = a[n-1][n] / a[n-1][n-1]

for i in range(n-2, -1, -1):
    x[i] = a[i][n]
    for j in range(i+1, n):
        x[i] = x[i] - a[i][j] * x[j]
    x[i] = x[i] / a[i][i]

print('\nA solução é: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')
