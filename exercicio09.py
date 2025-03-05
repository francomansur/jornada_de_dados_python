print('')
while True:
    try:
        celsius = float(input('Digite a temperatura em Graus Celsius: '))
        break
    except ValueError:
        print('O valor digitado não é um número.\n')

fahrenheit = (celsius * 9/5) + 32

print(f'{celsius} Graus Celsius é igual a {fahrenheit} Fahrenheits.\n')