def calcular(n1, n2, operacao):
    # Validações
    if not (isinstance(n1, str) and isinstance(n2, str) and isinstance(operacao, str)):
        raise Exception("valor invalido")
    if len(n1) != 8 or len(n2) != 8:
        raise Exception("tamanho da entrada invalido")
    if any(c not in '01' for c in n1 + n2):
        raise Exception("valor invalido")
    if operacao not in ['+', '-', 'x']:
        raise Exception("valor invalido")

    def soma(a, b):
        res = ''
        carry = 0
        for i in range(7, -1, -1):
            s = int(a[i]) + int(b[i]) + carry
            res = str(s % 2) + res
            carry = s // 2
        if carry:
            raise Exception("overflow")
        return res

    def subtrai(a, b):
        inv = ''.join('1' if x == '0' else '0' for x in b)
        comp = soma(inv, '00000001')
        return soma(a, comp)

    def soma_ext(a, b):
        a, b = a.zfill(16), b.zfill(16)
        res, carry = '', 0
        for i in range(15, -1, -1):
            s = int(a[i]) + int(b[i]) + carry
            res = str(s % 2) + res
            carry = s // 2
        if carry:
            res = '1' + res
        return res

    def multiplica(a, b):
        res = '00000000'
        for i in range(8):
            if b[7 - i] == '1':
                temp = a + '0' * i
                temp = temp.rjust(16, '0')
                res = soma_ext(res, temp)
        if len(res.lstrip('0')) > 8:
            raise Exception("overflow")
        return res[-8:]

    if operacao == '+':
        return soma(n1, n2)
    elif operacao == '-':
        return subtrai(n1, n2)
    elif operacao == 'x':
        return multiplica(n1, n2)

# Captura os valores do usuário e imprime resultado ou erro
try:
    n1 = input("Digite n1 (8 bits): ")
    n2 = input("Digite n2 (8 bits): ")
    operacao = input("Digite operação (+, -, x): ")
    resultado = calcular(n1, n2, operacao)
    print("Resultado:", resultado)
except Exception as e:
    print("Erro:", e)
