"""
    07. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
"""

print('')

while True:
    try:
        valor_1 = float(input('Digite o primeiro número: '))
        break
    except ValueError:
        print('O valor digitado não é um número.\n')

while True:
    try:
        valor_2 = float(input('Digite o segundo número: '))
        break
    except ValueError:
        print('O valor digitado não é um número.')

media = (valor_1 + valor_2)/2

print(f'A média dos números fornecidos é {media}.\n')