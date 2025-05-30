# Funcionalidades

Operação	Símbolo	Exemplo
Soma	+	00000011 + 00000001 = 00000100
Subtração	-	00000100 - 00000001 = 00000011
Multiplicação	x	00000011 x 00000011 = 00001001
✅ Validação rigorosa de entradas
🚨 Detecção de overflow
🔧 Implementação didática de operações binárias

# Como Usar
Pré-requisitos
Python 3.6+

# Instalação
bash
git clone (https://github.com/Rosajoaohttps/Calculadora-Binaria)

## Soma simples
print(calcular("00000101", "00000011", "+"))  # 5 + 3 = 8 → "00001000"

## Subtração com negativo
print(calcular("00000100", "00001000", "-"))  # 4 - 8 = -4 → "11111100"

## Multiplicação
print(calcular("00000011", "00000011", "x"))  # 3 × 3 = 9 → "00001001"
Tratamento de Erros
python
try:
    resultado = calcular("00001111", "11110000", "+")
except Exception as e:
    print(f"Erro: {e}")  # Overflow na soma!
🧠 Conceitos Implementados
Diagram
Code









# 📚 Documentação Técnica
Representação Numérica
Bits: 0b01111111 = 127 (máximo positivo)

Bits: 0b10000000 = -128 (mínimo negativo)

Algoritmos Chave
Complemento de 2:

python
def inverter_bits(b):
    return ''.join('1' if bit == '0' else '0' for bit in b)
Soma Binária:

Implementação bit a bit com carry

Detecção de Overflow:

Verificação de limites (-128 a 127)

# 🛠️ Testes
Execute os testes unitários:

bash
python -m unittest test_calculadora.py
Cobertura de testes:

Operações básicas

Casos de overflow

Validação de entradas

Números negativos

