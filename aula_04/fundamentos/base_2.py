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
