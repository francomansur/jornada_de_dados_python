"""
    19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
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

if numero_1 == numero_2:
    print(f'Os números são iguais. {numero_1} / {numero_2}.\n')
elif numero_1 != numero_2:
    print(f'Os números são diferentes. {numero_1} / {numero_2}.\n')