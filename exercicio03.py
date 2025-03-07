"""
    03.  Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
"""

print('')

while True:
    try:
        print('')
        valor_1 = int(input('Digite o primeiro número: '))
        break
    except ValueError:
        print('Digite um valor númérico válido.')

while True:
    try:
        valor_2 = int(input('Digite o segundo número: '))
        break
    except ValueError:
        print('Digite um valor númérico válido.')

total = valor_1 * valor_2

print(f'A multiplicação de {valor_1} por {valor_2} é {total}\n')


