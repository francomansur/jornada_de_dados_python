"""    
    Base 2: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
    Caso o número já exista lá dentro, ele não será adicionado.
    No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

numeros = []

while True:
    numero = input('Digite um número inteiro, ou "sair" para parar: ')
    
    if numero == 'sair':
        break
    elif numero.isdigit():
        numero = int(numero)  
        if numero not in numeros:
            numeros.append(numero)
    else:
        print('Número inválido.\n')

print(f'\nNúmeros de forma crescente: {sorted(numeros)}\n')
