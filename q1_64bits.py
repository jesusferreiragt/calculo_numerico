import math

# Passo a: Normalizar o número e representá-lo em notação de ponto flutuante na base 2
x = -0.3436

# Separar a parte inteira e fracionária
parte_inteira = int(abs(x))
parte_fracionaria = abs(x) - parte_inteira

# Conversão da parte inteira para binário
binario_inteiro = bin(parte_inteira)[2:]

# Normalização: encontrar a posição do primeiro bit 1
expoente = len(binario_inteiro) - 1 if parte_inteira > 0 else 0

# Se a parte inteira é zero, ajusta a parte fracionária
if parte_inteira == 0:
    while parte_fracionaria < 1:
        parte_fracionaria *= 2
        expoente -= 1

# Ajuste da parte fracionária após a normalização
parte_fracionaria -= math.floor(parte_fracionaria)

# Conversão da parte fracionária para binário
binario_fracionario = ''
while parte_fracionaria > 0 and len(binario_fracionario) < 52:  # Limite de precisão para 64 bits
    parte_fracionaria *= 2
    bit_fracionario = math.floor(parte_fracionaria)
    binario_fracionario += str(bit_fracionario)
    parte_fracionaria -= bit_fracionario

# Combinação da parte normalizada
mantissa = (binario_inteiro[1:] if parte_inteira > 0 else '') + binario_fracionario

# Mostrando a normalização
print(f'Número em binário normalizado: 1.{mantissa} x 2^{expoente}')

# Passo b: Calcular o expoente polarizado
# Precisão dupla: expoente polarizado = expoente + 1023 (para 64 bits)
expoente_polarizado = expoente + 1023
expoente_binario = bin(expoente_polarizado)[2:].zfill(11)

print(f'Expoente polarizado: {expoente_polarizado}')
print(f'Expoente em binário: {expoente_binario}')

# Passo c: Converter a mantissa para a base binária
# Ajuste do tamanho da mantissa
mantissa_binario = mantissa[:52].ljust(52, '0')  # Precisão dupla usa 52 bits para a mantissa

# Cálculo do erro relativo (opcional, caso precise ajustar a mantissa)
erro_relativo = (abs(x) - 2**expoente * (1 + int(mantissa_binario, 2) / 2**52)) / abs(x)
print(f'Mantissa em binário: {mantissa_binario}')
print(f'Erro relativo: {erro_relativo}')

# Passo d: Desenho do Diagrama do número armazenado no computador
# Sinal, expoente e mantissa
sinal = '1' if x < 0 else '0'
diagrama_binario = sinal + expoente_binario + mantissa_binario

print(f'Diagrama do número armazenado (64 bits): {diagrama_binario}')
