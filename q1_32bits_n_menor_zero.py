import math

# Passo a: Normalizar o número e representá-lo em notação de ponto flutuante na base 2
x = -48.344

# Conversão da parte fracionária para binário (já que a parte inteira é 0)
parte_fracionaria = abs(x)
binario_fracionario = ''
expoente = 0

# Normalização: encontrar a posição do primeiro bit 1
while parte_fracionaria < 1:
    parte_fracionaria *= 2
    expoente -= 1

# Ajuste da parte fracionária após a normalização
parte_fracionaria -= math.floor(parte_fracionaria)

# Conversão da parte fracionária para binário
while parte_fracionaria > 0 and len(binario_fracionario) < 52:  # Limite de precisão
    parte_fracionaria *= 2
    bit_fracionario = math.floor(parte_fracionaria)
    binario_fracionario += str(bit_fracionario)
    parte_fracionaria -= bit_fracionario

# Combinação da parte normalizada
mantissa = binario_fracionario

# Mostrando a normalização
print(f'Número em binário normalizado: 1.{mantissa} x 2^{expoente}')

# Passo b: Calcular o expoente polarizado
# Precisão simples: expoente polarizado = expoente + 127 (para 32 bits)
expoente_polarizado = expoente + 127
expoente_binario = bin(expoente_polarizado)[2:].zfill(8)

print(f'Expoente polarizado: {expoente_polarizado}')
print(f'Expoente em binário: {expoente_binario}')

# Passo c: Converter a mantissa para a base binária
# Ajuste do tamanho da mantissa
mantissa_binario = mantissa[:23].ljust(23, '0')  # Precisão simples usa 23 bits para a mantissa

# Cálculo do erro relativo (opcional, caso precise ajustar a mantissa)
erro_relativo = (abs(x) - 2**expoente * (1 + int(mantissa_binario, 2) / 2**23)) / abs(x)
print(f'Mantissa em binário: {mantissa_binario}')
print(f'Erro relativo: {erro_relativo}')

# Passo d: Desenho do Diagrama do número armazenado no computador
# Sinal, expoente e mantissa
sinal = '1' if x < 0 else '0'
diagrama_binario = sinal + expoente_binario + mantissa_binario

print(f'Diagrama do número armazenado (32 bits): {diagrama_binario}')
