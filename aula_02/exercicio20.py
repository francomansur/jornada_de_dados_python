"""
    20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
"""

print('')

while True:
    try:
        numero_1 = float(input('Digite o primeiro número: '))
        break
    except ValueError:
        print('O valor digitado não é um número.\n')

while True:
    try:
        numero_2 = float(input('Digite o segundo número: '))
        break
    except ValueError:
        print('O valor digitado não é um número.\n')

resultado = (numero_1 != numero_2)

print(f"Resultado da diferença: {resultado}\n")