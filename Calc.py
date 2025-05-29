def valitate_input(n1, n2, operacao):
    # Valida se todos os parâmetros são strings
    if not (isinstance(n1, str) and isinstance(n2, str) and isinstance(operacao, str)):
        raise Exception('valor invalido')
    # Valida se o tamanho de cada número é exatamente 8
    if len(n1) != 8 or len(n2) != 8:
        raise Exception('tamanho da entrada invalido')
    # Valida se os números são somente 0s ou 1s
    if any(c not in ['0', '1'] for c in n1 + n2):
        raise Exception('valor invalido')
    # Valida se a operação é uma das permitidas
    if operacao not in ['+', '-', 'x']:
        raise Exception('valor invalido')


def inverter_bits(b):
    # Inverte bits para calcular complemento de dois
    return ''.join('1' if bit == '0' else '0' for bit in b)


def soma_binarios(a, b):
    # Soma binária de duas strings de 8 bits
    res = ''
    carry = 0
    for i in range(7, -1, -1):
        s = int(a[i]) + int(b[i]) + carry
        res = str(s % 2) + res
        carry = s // 2
    return res


def bin_para_int(b):
    # Converte binário 8 bits com sinal (complemento de dois) para inteiro decimal
    if b[0] == '1':  # negativo
        inv = inverter_bits(b)
        comp = soma_binarios(inv, '00000001')
        valor = 0
        for bit in comp:
            valor = (valor << 1) + int(bit)
        return -valor
    else:
        valor = 0
        for bit in b:
            valor = (valor << 1) + int(bit)
        return valor


def int_para_bin(num):
    # Converte inteiro decimal (-128 a 127) para binário 8 bits com sinal (complemento de dois)
    if num < 0:
        num = 256 + num  # complemento de dois para negativos
    res = ''
    for _ in range(8):
        res = str(num % 2) + res
        num //= 2
    return res


def somar(a, b):
    # Soma binária de a e b
    resultado = soma_binarios(a, b)

    # Converte para int para validar overflow
    int_a = bin_para_int(a)
    int_b = bin_para_int(b)
    int_res = bin_para_int(resultado)

    # Detecta overflow: se soma de positivos dá negativo ou soma de negativos dá positivo
    if (int_a > 0 and int_b > 0 and int_res < 0) or (int_a < 0 and int_b < 0 and int_res >= 0):
        raise Exception('overflow')
    return resultado


def subtrair(a, b):
    # subtrair a - b = a + (-b), para -b calcula complemento de dois de b
    inv_b = inverter_bits(b)
    comp_b = soma_binarios(inv_b, '00000001')
    resultado = soma_binarios(a, comp_b)

    # Converte para int para validar overflow
    int_a = bin_para_int(a)
    int_b = bin_para_int(b)
    int_res = bin_para_int(resultado)

    # Detecta overflow na subtração
    if (int_a > 0 and int_b < 0 and int_res < 0) or (int_a < 0 and int_b > 0 and int_res >= 0):
        raise Exception('overflow')
    return resultado


def multiplicar(a, b):
    # Multiplicação via conversão para inteiro, validação e volta para binário
    int_a = bin_para_int(a)
    int_b = bin_para_int(b)
    resultado_int = int_a * int_b

    # Verifica overflow para 8 bits com sinal
    if resultado_int < -128 or resultado_int > 127:
        raise Exception('overflow')

    return int_para_bin(resultado_int)


def calcular(n1, n2, operacao):
    # Função principal que valida e executa a operação solicitada
    valitate_input(n1, n2, operacao)

    if operacao == '+':
        return somar(n1, n2)
    elif operacao == '-':
        return subtrair(n1, n2)
    elif operacao == 'x':
        return multiplicar(n1, n2)
