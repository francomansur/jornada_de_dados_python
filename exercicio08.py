"""
    08. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
"""

print('')

while True:
    try:
        base = float(input('Digite a base da potencia: '))
        break
    except ValueError:
        print('O valor digitado não é um número.\n')

while True:
    try:
        expoente = float(input('Digite o expoente da potencia: '))
        break
    except ValueError:
        print('O valor digitado não é um número.\n')

resultado = base ** expoente

print(f'A potencia de {base} ^ {expoente} é {resultado}.\n')