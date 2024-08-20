import numpy as np

# Função para converter decimal para binário
def decimal_para_binario(num, precisao=53):
    parte_inteira = int(num)
    parte_fracionaria = num - parte_inteira
    binario_inteiro = bin(parte_inteira).replace("0b", "")
    binario_fracionario = []
    
    while precisao > 0 and parte_fracionaria > 0:
        parte_fracionaria *= 2
        bit = int(parte_fracionaria)
        binario_fracionario.append(str(bit))
        parte_fracionaria -= bit
        precisao -= 1
    
    return binario_inteiro + "." + "".join(binario_fracionario)

# Número decimal
"""Aletarar valor"""
numero_decimal = 48.344 

# Convertendo para binário
binario = decimal_para_binario(numero_decimal, 64)
print(f"Representação binária de {numero_decimal}: {binario}")

# Normalizando
parte_inteira, parte_fracionaria = binario.split(".")
exponente = len(parte_inteira) - 1
mantissa = parte_inteira[1:] + parte_fracionaria

# Exponencial polarizado
bias = 1023
expoente_polarizado = exponente + bias

# Representação do expoente polarizado em binário
expoente_binario = np.binary_repr(expoente_polarizado, width=11)
print(f"Expoente polarizado (binário): {expoente_binario}")

# Mantissa com 52 bits
mantissa_52_bits = mantissa.ljust(52, '0')[:52]
print(f"Mantissa (52 bits): {mantissa_52_bits}")

# Bit de sinal (0 para positivo)
bit_sinal = '0'

# Representação final
representacao_final = bit_sinal + expoente_binario + mantissa_52_bits
print(f"Representação final em 64 bits: {representacao_final}")

# Desenhando o diagrama
print(f"\nDiagrama em 64 bits:")
print(f"Bit de sinal: {bit_sinal}")
print(f"Expoente (11 bits): {expoente_binario}")
print(f"Mantissa (52 bits): {mantissa_52_bits}")

# Para facilitar o entendimento, representamos o número na notação IEEE 754 64 bits
print(f"IEEE 754 64 bits: {bit_sinal} {expoente_binario} {mantissa_52_bits}")
