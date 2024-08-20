import math

# Normalizando o número

def decimal_to_binary(num, precision=20):
    """Converte um número decimal em binário com uma precisão especificada."""
    # Parte inteira
    integer_part = int(num)
    binary_int_part = bin(integer_part)[2:]

    # Parte fracionária
    fractional_part = num - integer_part
    binary_frac_part = []
    while fractional_part and len(binary_frac_part) < precision:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_frac_part.append(str(bit))
        fractional_part -= bit

    return binary_int_part + '.' + ''.join(binary_frac_part)

def normalize_binary(binary_str):
    """Normaliza o número binário e calcula o expoente."""
    if '.' in binary_str:
        integer_part, fractional_part = binary_str.split('.')
    else:
        integer_part, fractional_part = binary_str, ""

    # Normalização
    first_one_pos = integer_part.find('1')
    if first_one_pos != -1:
        normalized = f"1.{integer_part[first_one_pos + 1:] + fractional_part}"
        exponent = len(integer_part) - 1
    else:
        first_one_pos = fractional_part.find('1')
        normalized = f"1.{fractional_part[first_one_pos + 1:]}"
        exponent = - (first_one_pos + 1)

    return normalized, exponent

"""Alterar valor"""
# Número dado
num = 48.344
binary_rep = decimal_to_binary(num)
normalized_mantissa, exponent = normalize_binary(binary_rep)

print(f"Parte binária: {binary_rep}")
print(f"Mantissa normalizada: {normalized_mantissa}")
print(f"Expoente: {exponent}")

# Expoente polarizado 

def calculate_biased_exponent(exponent, bias=127):
    """Calcula o expoente polarizado."""
    biased_exponent = exponent + bias
    return f"{biased_exponent:08b}"  # Retorna o expoente polarizado em binário com 8 bits

biased_exponent = calculate_biased_exponent(exponent)
print(f"Expoente polarizado em binário: {biased_exponent}")

# mantissa para base 2

def mantissa_to_binary(mantissa_str, bits=23):
    """Converte a mantissa normalizada para binário, truncando para o número de bits especificado."""
    _, mantissa_fraction = mantissa_str.split('.')
    return mantissa_fraction[:bits]

mantissa_binary = mantissa_to_binary(normalized_mantissa)
print(f"Mantissa em binário: {mantissa_binary}")

# Diagrama 

def draw_floating_point_representation(sign, exponent_bin, mantissa_bin):
    """Desenha o diagrama do número em ponto flutuante (formato IEEE 754)."""
    return f"{sign} | {exponent_bin} | {mantissa_bin}"

# Sinal (0 para positivo, 1 para negativo)
sign_bit = '0' if num > 0 else '1'

# Desenhar o número armazenado em 32 bits
diagram = draw_floating_point_representation(sign_bit, biased_exponent, mantissa_binary)
print(f"Representação em ponto flutuante (32 bits): {diagram}")
