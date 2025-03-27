numeros_pares = []
numeros_impares = []

while True:
    try:
        numero = (input('Digite um número inteiro, ou "sair" para sair: '))

        if numero == 'sair':
            break
            
        if (int(numero) == 0):
            raise ValueError
        elif numero.isdigit():
            if (int(numero) % 2 == 0):
                numeros_pares.append(int(numero))
            else:
                numeros_impares.append(int(numero))

    except ValueError:
        print('Valor inválido\n')

print(f'\nNúmeros pares: {sorted(numeros_pares)}')
print(f'Números ímpares: {sorted(numeros_impares)}\n')