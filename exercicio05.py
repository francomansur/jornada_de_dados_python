print('')

while True:
    try:
        valor_1 = int(input('Digite um número: '))
        break
    except ValueError:
        print('Número inválido.\n')

quadrado = valor_1 * valor_1

print(f'O quadrado de {valor_1} é {quadrado}\n')