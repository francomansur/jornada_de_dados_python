"""
    01. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
"""

print('')

while True:  # Loop infinito até receber um número inteiro
    try:
        valor_1 = int(input('Digite o primeiro valor inteiro: '))
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print('O valor precisa ser um número inteiro. Tente novamente. \n')

while True:  # Loop infinito até receber um número inteiro
    try:
        valor_2 = int(input('Digite o segundo valor inteiro: '))
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print('O valor precisa ser um número inteiro. Tente novamente. \n')

soma = valor_1 + valor_2

print(f'A soma de {valor_1} + {valor_2} é igual a {soma}\n')
