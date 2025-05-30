#aqui estou coloando um código alternativo para analise de melhor resultado

def calcular(n1: str, n2: str, operacao: str) -> str:
    # Função para verificar se uma string é um binário válido (0 e 1)
    def valida_binario(b):
        return all(c in "01" for c in b)

    # Função para inverter bits (para complemento de dois)
    def inverter_bits(b):
        return ''.join('1' if bit == '0' else '0' for bit in b)

    # Função para somar dois binários de 8 bits
    def soma_binarios(a, b):
        resultado = []
        carry = 0
        # Soma bit a bit da direita para esquerda
        for i in range(7, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])
            soma = bit_a + bit_b + carry
            resultado.append(str(soma % 2))
            carry = soma // 2
        resultado.reverse()
        return ''.join(resultado), carry

    # Função para converter binário 8 bits com sinal para inteiro em Python (para validação de overflow)
    def bin_para_int(b):
        # Se bit de sinal é 1, é negativo (complemento de dois)
        if b[0] == '1':
            inv = inverter_bits(b)
            soma, _ = soma_binarios(inv, "00000001")
            # converte para int positivo e depois torna negativo
            valor = 0
            for bit in soma:
                valor = valor * 2 + int(bit)
            return -valor
        else:
            valor = 0
            for bit in b:
                valor = valor * 2 + int(bit)
            return valor

    # Função para converter inteiro (de -128 a 127) para binário 8 bits com sinal
    def int_para_bin(num):
        if num < 0:
            num = 256 + num  # complemento de dois para negativo
        res = ""
        for i in range(8):
            res = str(num % 2) + res
            num //=2
        return res

    # Validações iniciais
    if len(n1) != 8 or len(n2) != 8:
        raise Exception("tamanho da entrada invalido")
    if not valida_binario(n1) or not valida_binario(n2):
        raise Exception("valor invalido")
    if operacao not in ("+", "-", "x"):
        raise Exception("valor invalido")

    # Vamos trabalhar com os valores para operações
    # Conversão para inteiro apenas para checagem de overflow final
    int_n1 = bin_para_int(n1)
    int_n2 = bin_para_int(n2)

    # Definindo operação
    if operacao == "+":
        # Soma binária usando soma_binarios
        resultado_bin, carry = soma_binarios(n1, n2)
        resultado_int = int_n1 + int_n2
    elif operacao == "-":
        # Subtração: n1 - n2 = n1 + (-n2)
        # Para -n2, fazemos complemento de dois de n2
        inv_n2 = inverter_bits(n2)
        n2_complemento = soma_binarios(inv_n2, "00000001")[0]
        resultado_bin, carry = soma_binarios(n1, n2_complemento)
        resultado_int = int_n1 - int_n2
    else:
        # Multiplicação binária (usando método de multiplicação manual bit a bit)
        # Como é 1 byte com sinal, vamos multiplicar valores absolutos e depois ajustar sinal

        # Calcula valor absoluto dos inteiros
        abs_n1 = abs(int_n1)
        abs_n2 = abs(int_n2)

        # Multiplicação binária do valor absoluto (até 8 bits * 8 bits = 16 bits)
        resultado_16bits = [0]*16

        for i in range(8):
            bit = (abs_n2 >> (7 - i)) & 1
            if bit == 1:
                # soma abs_n1 deslocado para a direita posição (i)
                temp = abs_n1 << (7 - i)
                for j in range(16):
                    resultado_16bits[15 - j] += (temp >> j) & 1

        # Ajusta carry e bits > 1 da soma na lista
        for i in range(15, 0, -1):
            if resultado_16bits[i] > 1:
                resultado_16bits[i-1] += resultado_16bits[i] // 2
                resultado_16bits[i] %= 2

        # Agora temos resultado em 16 bits, vamos converter para inteiro
        res_int = 0
        for bit in resultado_16bits:
            res_int = (res_int << 1) | bit

        # Ajusta o sinal do resultado
        if (int_n1 < 0) != (int_n2 < 0):
            res_int = -res_int

        resultado_int = res_int

        # Validar se resultado cabe em 8 bits com sinal
        if resultado_int < -128 or resultado_int > 127:
            raise Exception("overflow")

        # Converte resultado para binário 8 bits com sinal
        resultado_bin = int_para_bin(resultado_int)

        return resultado_bin

    # Após soma ou subtração, validar overflow do resultado (que é resultado_int)
    if resultado_int < -128 or resultado_int > 127:
        raise Exception("overflow")

    # O resultado binário pode estar incorreto se carry estiver presente ou overflow
    # Mas para 8 bits em complemento de dois, soma_binarios gera resultado correto.
    # Se carry for 1, indica overflow em soma de números positivos, verificar:

    # Vamos ajustar resultado para 8 bits (pegar só os 8 bits menos significativos)
    resultado_bin = resultado_bin[-8:]




    return resultado_bin
