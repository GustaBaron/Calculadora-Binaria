# para executar o teste, cole no terminal esse código "python test_calc.py", assim o unittest vai rodar e mostrar se passou tudo ou onde falhou.


import unittest

class TestCalculadora1Byte(unittest.TestCase):

    def test_valitate_input_valid(self):
        # Entradas válidas não geram exceção
        try:
            valitate_input("00000001", "11111111", "+")
        except Exception:
            self.fail("valitate_input levantou exceção inesperada!")

    def test_valitate_input_invalid_type(self):
        # Parâmetros que não são string geram 'valor invalido'
        with self.assertRaises(Exception) as cm:
            valitate_input(1, "00000001", "+")
        self.assertEqual(str(cm.exception), "valor invalido")

    def test_valitate_input_invalid_length(self):
        # Strings com tamanho diferente de 8 geram 'tamanho da entrada invalido'
        with self.assertRaises(Exception) as cm:
            valitate_input("00001", "00000001", "+")
        self.assertEqual(str(cm.exception), "tamanho da entrada invalido")

    def test_valitate_input_invalid_chars(self):
        # Strings com caracteres diferentes de 0 ou 1 geram 'valor invalido'
        with self.assertRaises(Exception) as cm:
            valitate_input("0000000A", "00000001", "+")
        self.assertEqual(str(cm.exception), "valor invalido")

    def test_valitate_input_invalid_operation(self):
        # Operação inválida gera 'valor invalido'
        with self.assertRaises(Exception) as cm:
            valitate_input("00000001", "00000001", "%")
        self.assertEqual(str(cm.exception), "valor invalido")

    def test_somar_normal(self):
        self.assertEqual(somar("00000001", "00000001"), "00000010")
        self.assertEqual(somar("00000010", "00000011"), "00000101")

    def test_somar_overflow(self):
        with self.assertRaises(Exception) as cm:
            somar("01111111", "00000001")  # 127 + 1 = overflow
        self.assertEqual(str(cm.exception), "overflow")

    def test_subtrair_normal(self):
        self.assertEqual(subtrair("00000100", "00000001"), "00000011")
        self.assertEqual(subtrair("00000000", "00000001"), "11111111")  # 0 - 1 = -1

    def test_subtrair_overflow(self):
        with self.assertRaises(Exception) as cm:
            subtrair("10000000", "00000001")  # -128 - 1 = overflow
        self.assertEqual(str(cm.exception), "overflow")

    def test_multiplicar_normal(self):
        self.assertEqual(multiplicar("00000010", "00000010"), "00000100")  # 2 * 2 = 4
        self.assertEqual(multiplicar("11111111", "00000001"), "11111111")  # -1 * 1 = -1

    def test_multiplicar_overflow(self):
        with self.assertRaises(Exception) as cm:
            multiplicar("01111111", "00000010")  # 127 * 2 = overflow
        self.assertEqual(str(cm.exception), "overflow")

    def test_calcular_operacoes(self):
        self.assertEqual(calcular("00000001", "00000001", "+"), "00000010")
        self.assertEqual(calcular("00000010", "00000001", "-"), "00000001")
        self.assertEqual(calcular("00000010", "00000010", "x"), "00000100")

    def test_calcular_erro_entrada(self):
        with self.assertRaises(Exception) as cm:
            calcular("0000001", "00000001", "+")  # tamanho inválido
        self.assertEqual(str(cm.exception), "tamanho da entrada invalido")

    def test_calcular_erro_operacao(self):
        with self.assertRaises(Exception) as cm:
            calcular("00000001", "00000001", "%")  # operação inválida
        self.assertEqual(str(cm.exception), "valor invalido")


if __name__ == '__main__':
    unittest.main()
