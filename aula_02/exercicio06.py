"""
    06. Escreva um programa que receba dois números flutuantes e realize sua adição.
"""

print('')

while True:
    try:
        valor_1 = float(input('Digite o primeiro número: '))
        break
    except ValueError:
        print('O valor digitado não é um número.')

while True:
    try:
        valor_2 = float(input('Digite o segundo número: '))
        break
    except ValueError:
        print('O valor digitado não é um número.')

soma = valor_1 + valor_2

print(f'A soma de {valor_1} + {valor_2} é {soma}\n')