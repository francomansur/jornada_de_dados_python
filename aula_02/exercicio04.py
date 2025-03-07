"""
    04. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
"""

print('')

# Solicita o primeiro número inteiro
while True:
    try:
        valor_1 = int(input('Digite o primeiro número inteiro: '))
        break
    except ValueError:
        print('Número inteiro inválido.\n')

# Solicita o segundo número inteiro e evita divisão por zero
while True:
    try:
        valor_2 = int(input('Digite o segundo número inteiro: '))
        if valor_2 == 0:  # Verifica se o usuário digitou zero
            raise ZeroDivisionError  # Lança o erro para cair no except
        break
    except ValueError:
        print('Número inteiro inválido.\n')
    except ZeroDivisionError:
        print('Não é possível dividir um número por 0.\n')

# Realiza a divisão apenas se os valores forem válidos
total = valor_1 / valor_2
print(f'A divisão de {valor_1} por {valor_2} é {total:.2f}\n')
